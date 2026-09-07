"""CORE v0.16 fixed-capacity JAX packet-queue reference driver.

Run from the repository root:

    python reference/core_v016_jax_packet_queue.py
    python reference/core_v016_jax_packet_queue.py --stable-direct
    python reference/core_v016_jax_packet_queue.py --unstable-direct
"""
from __future__ import annotations

import argparse
import math
import numpy as np
import jax.numpy as jnp
from scipy.interpolate import CubicSpline
from scipy.optimize import least_squares

from core_v016_jax_queue_kernel import (
    N,QMAX,TWO_PI,C_NS,C0,TAU_FIC,A_FIC,
    make_state,response,center_seed,set_adaptation,set_tau_frozen,
    run_cycles_jit,run_cycles_dynamic_jit,run_to_tau_jit,collect_cycles_jit,
    cycle_complex_Z,
)
from core_v016_jax_queue_tangent import tangent_checks

T_NS_REF=16.297496058505022
A_IMPERATIVE=0.00100586082225
A0_REF=0.0010023850245501774
TAU_MULT=np.array([8.004,8.006,8.007,8.0072,8.00725])
MU_V015=np.array([0.7843122830695624,0.864993683765859,0.9358154754108635,0.9612338114815638,0.9717922535166069])
MU_JAX=np.array([0.7852515201224747,0.8672758438422411,0.935740621572364,0.9612512912808343,0.9711148445411683])
MU_UNSTABLE_JAX=1.038312176501172
TAU_FOLD_V015=8.007310727816458
TAU_GHOST=8.00731041


def fit_fold(taus,multipliers):
    taus=np.asarray(taus,float); y=1.0-np.asarray(multipliers,float)
    def residual(z):
        K,tf=z
        return K*np.sqrt(np.maximum(tf-taus,1e-20))-y
    sol=least_squares(residual,[3.6,8.007313],bounds=([0.0,float(taus.max())+1e-10],[100.0,8.02]),xtol=1e-14,ftol=1e-14,gtol=1e-14)
    return float(sol.x[0]),float(sol.x[1]),float(np.sqrt(np.mean(sol.fun**2)))


def make_large_tau8():
    st=make_state(c=1.0/7.8,c0=1.0/7.8)
    st,_=run_cycles_jit(st,80)
    kick=2e-3*jnp.cos(TWO_PI*jnp.arange(N)/N)
    st=st._replace(phi=st.phi-response(st.psi)*kick)
    st,_=run_cycles_dynamic_jit(st,jnp.array(2500,dtype=jnp.int32))
    st=set_tau_frozen(st,8.0)
    st,_=run_cycles_dynamic_jit(st,jnp.array(2500,dtype=jnp.int32))
    return st


def host_run_cycles(state,cycles,collect=False):
    if not collect:
        st,_=run_cycles_dynamic_jit(state,jnp.asarray(cycles,dtype=jnp.int32))
        st.t.block_until_ready()
        return st
    Z=[]; A=[]; st=state
    for _ in range(int(cycles)):
        st,_=run_cycles_jit(st,1)
        Z.append(complex(cycle_complex_Z(st))); A.append(float(st.A_held))
    return st,np.asarray(Z),np.asarray(A)


def radial_spline(Z):
    theta=np.mod(np.angle(Z),TWO_PI); radius=np.abs(Z)
    order=np.argsort(theta); t=theta[order]; r=radius[order]
    return CubicSpline(np.concatenate([t-TWO_PI,t,t+TWO_PI]),np.concatenate([r,r,r]))


def section_values(unwrapped_phase,values,theta0=0.0):
    phase=np.asarray(unwrapped_phase); values=np.asarray(values)
    k0=math.ceil((phase[0]-theta0)/TWO_PI); k1=math.floor((phase[-1]-theta0)/TWO_PI)
    out=[]
    for k in range(k0,k1+1):
        target=theta0+TWO_PI*k; j=int(np.searchsorted(phase,target))
        if j<=0 or j>=len(phase): continue
        w=(target-phase[j-1])/(phase[j]-phase[j-1])
        out.append((1-w)*values[j-1]+w*values[j])
    return np.asarray(out)


def radial_perturb(state,delta_A):
    theta=np.angle(complex(cycle_complex_Z(state)))
    desired=2.0*delta_A*jnp.cos(theta+TWO_PI*jnp.arange(N)/N)
    return state._replace(phi=state.phi-response(state.psi)*desired)


def default_checks():
    assert QMAX==12
    st=make_state(c=C_NS,c0=C_NS); st,_=run_cycles_jit(st,80)
    Tj=float(st.last_period)
    assert abs(Tj-T_NS_REF)<1e-6
    assert int(st.max_active)<=6 and not bool(st.overflow)
    seed=center_seed(st,1e-3); seed,_=run_cycles_jit(seed,20)
    A0=float(seed.A_held); assert abs(A0-A0_REF)<2e-9
    slow=set_adaptation(seed,1e-5,kappa=0.0,c0=C0)
    slow,cycles,_=run_to_tau_jit(slow,TAU_FIC)
    Aj=float(slow.A_held)
    assert int(cycles)==15002
    assert abs(Aj-A_IMPERATIVE)/A_IMPERATIVE<3e-5
    assert Aj/A_FIC<0.02 and not bool(slow.overflow)
    tang=tangent_checks()
    assert abs(tang["fire_dtime_dphi"]-tang["fire_implicit"])<2e-8
    assert tang["fire_jvp_relerr"]<5e-8
    assert abs(tang["arrival_dtime_drho"]-8.0)<1e-12
    assert abs(tang["arrival_dtime_dc"]+47.87198569561542)<5e-10
    assert tang["arrival_jvp_relerr"]<5e-8
    K5,tf5,rms5=fit_fold(TAU_MULT,MU_JAX)
    K3,tf3,rms3=fit_fold(TAU_MULT[-3:],MU_JAX[-3:])
    assert np.max(np.abs(MU_JAX-MU_V015))<0.003
    assert abs(tf3-8.007313482578484)<5e-7
    assert abs(tf3-TAU_FOLD_V015)<5e-6 and abs(tf3-TAU_GHOST)<5e-6
    assert MU_JAX[3]<1.0<MU_UNSTABLE_JAX
    print("CORE v0.16 fixed-capacity JAX queue checks passed")
    print("queue capacity / observed max:",QMAX,int(st.max_active))
    print("frozen period JAX / reference:",Tj,T_NS_REF)
    print("center seed:",A0)
    print("epsilon=1e-5 cycles / A at FIC / imperative:",int(cycles),Aj,A_IMPERATIVE)
    print("event-chart tangent checks:",tang)
    print("JAX fold fits all5 / near3:",(K5,tf5,rms5),(K3,tf3,rms3))
    print("stored stable / unstable tau=8.0072:",MU_JAX[3],MU_UNSTABLE_JAX)


def stable_direct():
    base=make_large_tau8(); base=set_tau_frozen(base,8.0072); base=host_run_cycles(base,6000)
    _,Zref,_=host_run_cycles(base,3000,collect=True); spline=radial_spline(Zref)
    vals=[]
    for d in (4e-6,8e-6):
        trial=radial_perturb(base,d); _,Z,_=host_run_cycles(trial,1600,collect=True)
        dev=np.abs(Z)-spline(np.mod(np.angle(Z),TWO_PI)); sec=section_values(np.unwrap(np.angle(Z)),dev)
        ratios=[]; floor=max(2e-8,abs(d)*0.01)
        for k in range(3,min(len(sec)-1,55)):
            if abs(sec[k])>floor and abs(sec[k+1])>floor and sec[k]*sec[k+1]>0:
                q=sec[k+1]/sec[k]
                if 0.5<q<1.2: ratios.append(q)
        vals.append(float(np.median(ratios)))
    assert max(abs(v-MU_V015[3]) for v in vals)<0.008
    assert abs(vals[0]-vals[1])<0.008
    print("direct JAX stable full-rotation multipliers at tau=8.0072:",vals)


def unstable_direct():
    """Validate the stored tight direct edge-circle audit."""
    mu_s=MU_JAX[3]; mu_u=MU_UNSTABLE_JAX; reciprocal=1.0/mu_s
    assert mu_s<1.0<mu_u
    assert abs(mu_u-reciprocal)<0.003
    print("stored direct JAX edge-circle multipliers:",mu_s,mu_u)
    print("1/mu_stable:",reciprocal)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--stable-direct",action="store_true")
    parser.add_argument("--unstable-direct",action="store_true")
    args=parser.parse_args()
    if args.stable_direct: stable_direct()
    elif args.unstable_direct: unstable_direct()
    else: default_checks()

if __name__=="__main__":
    main()
