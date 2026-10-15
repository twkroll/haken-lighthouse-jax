from __future__ import annotations
import math
from dataclasses import dataclass
from typing import NamedTuple
import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
jax.config.update('jax_enable_x64', True)

ALPHA=.5; TWO_PI=2*math.pi; N=3; QMAX=12; NEVENT=12
P_TRUE=-3.267985407948901; TAU_TRUE=8.0
THETA_TRUE=np.array([P_TRUE,TAU_TRUE,0.,0.])
GXn,GWn=leggauss(20); GX=jnp.asarray(GXn); GW=jnp.asarray(GWn)
MODE=np.array([0,1,2]*3,dtype=int); MODEJ=jnp.asarray(MODE)
TARGET=np.array([0,1,2,1,2,0,2,0,1],dtype=int); TARGETJ=jnp.asarray(TARGET)
PSI0=np.array([-0.207423841618632]*3); Q0=np.array([0.780899408476725]*3)
PHI_BASE=np.array([1.838519273976891,1.488519273976891,1.658519273976891])
LATENT_B=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
LATENT_BJ=jnp.asarray(LATENT_B)
CANON=((0,0),(2,0),(1,0),(0,1),(2,1),(1,1))
KIND_A=0; KIND_F=1

class Tokens(NamedTuple):
    kind:jax.Array; idx:jax.Array; guess:jax.Array; slot0:jax.Array; slot1:jax.Array
class JState(NamedTuple):
    t:jax.Array; psi:jax.Array; q:jax.Array; phi:jax.Array; active:jax.Array; edge_id:jax.Array; rho:jax.Array; counts:jax.Array; obs:jax.Array

def edge_weight_np(p,e):
    r=e%3; return 1.0 if r==0 else (p if r==1 else -p)
def response_np(x):
    y=x+1.; return np.where(y>0,np.exp(-1/np.maximum(y,1e-15)**2),0.)
def phase_gain_np(psi,q,dt):
    s=.5*dt*(GXn+1); ee=np.exp(-ALPHA*s); ps=ee*(psi+q*s)
    return float(.5*dt*np.dot(GWn,response_np(ps)))
def firing_time_np(psi,q,phi):
    deficit=TWO_PI-phi
    if deficit<=1e-12:return 0.
    f=lambda t:phase_gain_np(psi,q,t)-deficit
    hi=1.
    for _ in range(20):
        if f(hi)>=0: break
        hi*=2
    return brentq(f,0,hi,xtol=1e-13,rtol=1e-13)
@dataclass
class NS:
    t:float; psi:np.ndarray; q:np.ndarray; phi:np.ndarray; active:np.ndarray; edge_id:np.ndarray; rho:np.ndarray

def phi_from_eta_np(eta): return PHI_BASE + LATENT_B@np.asarray(eta,float)
def ns0(theta):
    eta=np.asarray(theta,float)[2:4]
    return NS(0.,PSI0.copy(),Q0.copy(),phi_from_eta_np(eta),np.zeros(QMAX,bool),np.zeros(QMAX,int),np.zeros(QMAX))
def adv_np(st,dt,tau):
    op=st.psi.copy(); oq=st.q.copy(); st.phi += np.array([phase_gain_np(op[i],oq[i],dt) for i in range(N)])
    e=math.exp(-ALPHA*dt); st.psi=e*(op+oq*dt); st.q=e*oq
    speed=np.where(MODE[st.edge_id]==1,.5,1./tau); st.rho=np.where(st.active,st.rho-speed*dt,st.rho); st.t+=dt

def record_tokens(theta):
    p,tau=map(float,theta[:2]); st=ns0(theta); counts=np.zeros(N,int); obs=np.full((N,2),np.nan); rows=[]
    while len(rows)<NEVENT:
        ft=np.array([firing_time_np(st.psi[i],st.q[i],st.phi[i]) for i in range(N)])
        at=np.full(QMAX,np.inf)
        for k in np.where(st.active)[0]:
            e=st.edge_id[k]; at[k]=st.rho[k]/(.5 if MODE[e]==1 else 1./tau)
        fi=int(np.argmin(ft)); ai=int(np.argmin(at))
        if ft[fi] <= at[ai]: kind=KIND_F; idx=fi; dt=ft[fi]
        else: kind=KIND_A; idx=ai; dt=at[ai]
        adv_np(st,dt,tau)
        if kind==KIND_A:
            e=int(st.edge_id[idx]); st.q[TARGET[e]]+=edge_weight_np(p,e)*ALPHA**2; st.active[idx]=False; st.rho[idx]=0.; rows.append((kind,idx,dt,0,0))
        else:
            i=idx; st.phi[i]-=TWO_PI; st.q[i]+=ALPHA**2; free=np.where(~st.active)[0][:2]
            for sl,e in zip(free,(3*i+1,3*i+2)): st.active[sl]=True;st.edge_id[sl]=e;st.rho[sl]=1.
            if counts[i]<2:obs[i,counts[i]]=st.t
            counts[i]+=1; rows.append((kind,i,dt,int(free[0]),int(free[1])))
    y=np.array([obs[i,j] for i,j in CANON])
    a=np.array(rows)
    tok=Tokens(jnp.asarray(a[:,0],jnp.int32),jnp.asarray(a[:,1],jnp.int32),jnp.asarray(a[:,2],jnp.float64),jnp.asarray(a[:,3],jnp.int32),jnp.asarray(a[:,4],jnp.int32))
    return tok,y

def response(x):
    y=x+1.; ys=jnp.maximum(y,1e-15); return jnp.where(y>0,jnp.exp(-1/(ys*ys)),0.)
def phase_gain_single(psi,q,dt):
    s=.5*dt*(GX+1); e=jnp.exp(-ALPHA*s); ps=e*(psi+q*s); return .5*dt*jnp.sum(GW*response(ps))
def phase_gain_vec(psi,q,dt):
    s=.5*dt*(GX+1); e=jnp.exp(-ALPHA*s); ps=e[None,:]*(psi[:,None]+q[:,None]*s[None,:]); return .5*dt*jnp.sum(GW[None,:]*response(ps),axis=1)
def firing_root(psi,q,phi,guess):
    t=jax.lax.stop_gradient(guess)
    def body(_,t):
        g=phi+phase_gain_single(psi,q,t)-TWO_PI; e=jnp.exp(-ALPHA*t); pe=e*(psi+q*t); return t-g/response(pe)
    return jax.lax.fori_loop(0,7,body,t)
def edge_weight(p,e):
    r=e%3;return jnp.where(r==0,1.,jnp.where(r==1,p,-p))
def js0(theta):
    eta=theta[2:4]; phi=jnp.asarray(PHI_BASE)+LATENT_BJ@eta
    return JState(jnp.array(0.),jnp.asarray(PSI0),jnp.asarray(Q0),phi,jnp.zeros(QMAX,bool),jnp.zeros(QMAX,jnp.int32),jnp.zeros(QMAX),jnp.zeros(N,jnp.int32),jnp.full((N,2),jnp.nan))
def adv(st,dt,tau):
    e=jnp.exp(-ALPHA*dt); psi=e*(st.psi+st.q*dt);q=e*st.q;phi=st.phi+phase_gain_vec(st.psi,st.q,dt);speed=jnp.where(MODEJ[st.edge_id]==1,.5,1./tau);rho=jnp.where(st.active,st.rho-speed*dt,st.rho);return st._replace(t=st.t+dt,psi=psi,q=q,phi=phi,rho=rho)
def candidate_times(st,tau,guess):
    ft=jax.vmap(lambda i:firing_root(st.psi[i],st.q[i],st.phi[i],guess))(jnp.arange(N))
    speed=jnp.where(MODEJ[st.edge_id]==1,.5,1./tau);at=jnp.where(st.active,st.rho/speed,jnp.inf);return ft,at
def process_one(st,p,kind,idx,slot0,slot1):
    def arr(s):
        e=s.edge_id[idx];q=s.q.at[TARGETJ[e]].add(edge_weight(p,e)*ALPHA**2);return s._replace(q=q,active=s.active.at[idx].set(False),rho=s.rho.at[idx].set(0.))
    def fire(s):
        i=idx; c=s.counts[i]; obs=jax.lax.cond(c<2,lambda o:o.at[i,c].set(s.t),lambda o:o,s.obs);phi=s.phi.at[i].add(-TWO_PI);q=s.q.at[i].add(ALPHA**2);active=s.active.at[slot0].set(True).at[slot1].set(True);eid=s.edge_id.at[slot0].set(3*i+1).at[slot1].set(3*i+2);rho=s.rho.at[slot0].set(1.).at[slot1].set(1.);counts=s.counts.at[i].add(1);return s._replace(phi=phi,q=q,active=active,edge_id=eid,rho=rho,counts=counts,obs=obs)
    return jax.lax.cond(kind==KIND_A,arr,fire,st)
def replay_tokens(theta,tok):
    p,tau=theta[:2]; st=js0(theta)
    def body(k,st):
        kind=tok.kind[k];idx=tok.idx[k];guess=tok.guess[k];ft,at=candidate_times(st,tau,guess);dt=jnp.where(kind==KIND_F,ft[idx],at[idx]);st=adv(st,dt,tau);return process_one(st,p,kind,idx,tok.slot0[k],tok.slot1[k])
    st=jax.lax.fori_loop(0,NEVENT,body,st);return jnp.stack([st.obs[i,j] for i,j in CANON])
def margin_tokens(theta,tok):
    p,tau=theta[:2];st=js0(theta);m=jnp.array(jnp.inf)
    def body(k,carry):
        st,m=carry;kind=tok.kind[k];idx=tok.idx[k];guess=tok.guess[k];ft,at=candidate_times(st,tau,guess)
        fcomp=ft.at[idx].set(jnp.inf); acomp=at.at[idx].set(jnp.inf)
        sel=jnp.where(kind==KIND_F,ft[idx],at[idx]); comp=jnp.where(kind==KIND_F,jnp.minimum(jnp.min(fcomp),jnp.min(at)),jnp.minimum(jnp.min(ft),jnp.min(acomp)))
        st=adv(st,sel,tau);st=process_one(st,p,kind,idx,tok.slot0[k],tok.slot1[k]);return st,jnp.minimum(m,comp-sel)
    _,m=jax.lax.fori_loop(0,NEVENT,body,(st,m));return m

REPLAY=jax.jit(replay_tokens); JAC=jax.jit(jax.jacfwd(replay_tokens,argnums=0)); MARGIN=jax.jit(margin_tokens)
TRUTH_TOK,TRUTH_Y=record_tokens(THETA_TRUE)
def sig(tok):return tuple(zip(np.asarray(tok.kind).tolist(),np.asarray(tok.idx).tolist()))
def pobj(x):return .5*np.sum((record_tokens(x)[1]-TRUTH_Y)**2)

@dataclass
class Result:
    x:np.ndarray;obj:float;iterations:int;switches:int;hits:int;history:list;crossings:list

def optimize(x0,maxit=20,trust=(.55,.55,.20,.20)):
    x=np.array(x0,float);tok,_=record_tokens(x);switches=hits=0;hist=[];cross=[]
    tr=np.asarray(trust,float)
    for it in range(maxit):
        y=np.asarray(REPLAY(jnp.asarray(x),tok));r=y-TRUTH_Y;obj=.5*r@r;m=float(MARGIN(jnp.asarray(x),tok));hist.append((it,x.copy(),obj,m,sig(tok)))
        if np.linalg.norm(r)<1e-11:return Result(x,float(obj),it,switches,hits,hist,cross)
        J=np.asarray(JAC(jnp.asarray(x),tok));s=-np.linalg.lstsq(J,r,rcond=None)[0];scale=max(np.max(np.abs(s)/tr),1.);s/=scale
        mc=float(MARGIN(jnp.asarray(x+s),tok))
        if mc>1e-8:
            a=1.
            while a>1e-5:
                xt=x+a*s
                if float(MARGIN(jnp.asarray(xt),tok))>1e-8 and pobj(xt)<obj: x=xt;break
                a*=.5
            else: raise RuntimeError('descent failed')
        else:
            hits+=1;origin=x.copy();old=sig(tok)
            def mf(a):return float(MARGIN(jnp.asarray(origin+a*s),tok))
            lo,hi=0.,1.
            for _ in range(55):
                mid=.5*(lo+hi)
                if mf(mid)>0:lo=mid
                else:hi=mid
            ab=.5*(lo+hi);safe=origin+max(0,ab-1e-4)*s;safeobj=pobj(safe)
            across=min(1.,ab+2e-4);xc=origin+across*s;newtok,_=record_tokens(xc);new=sig(newtok);crossobj=pobj(xc)
            cross.append({'alpha_boundary':ab,'boundary_point':origin+ab*s,'safe_point':safe,'safe_margin':float(MARGIN(jnp.asarray(safe),tok)),'cross_point':xc,'old_sig':old,'new_sig':new,'old_obj':obj,'safe_obj':safeobj,'cross_obj':crossobj})
            if crossobj<=safeobj*(1+1e-7):x=xc;tok=newtok;switches+=int(new!=old)
            else:x=safe;tok,_=record_tokens(x)
    return Result(x,pobj(x),maxit,switches,hits,hist,cross)

def fd_jac(theta,tok,h=1e-6):
    theta=np.asarray(theta,float); cols=[]
    for j in range(4):
        e=np.zeros(4);e[j]=1.
        cols.append((np.asarray(REPLAY(jnp.asarray(theta+h*e),tok))-np.asarray(REPLAY(jnp.asarray(theta-h*e),tok)))/(2*h))
    return np.column_stack(cols)

def margins_tokens(theta,tok):
    p,tau=theta[:2];st=js0(theta);out=jnp.zeros(NEVENT)
    def body(k,carry):
        st,out=carry;kind=tok.kind[k];idx=tok.idx[k];guess=tok.guess[k];ft,at=candidate_times(st,tau,guess)
        fcomp=ft.at[idx].set(jnp.inf); acomp=at.at[idx].set(jnp.inf)
        sel=jnp.where(kind==KIND_F,ft[idx],at[idx]); comp=jnp.where(kind==KIND_F,jnp.minimum(jnp.min(fcomp),jnp.min(at)),jnp.minimum(jnp.min(ft),jnp.min(acomp)))
        out=out.at[k].set(comp-sel)
        st=adv(st,sel,tau);st=process_one(st,p,kind,idx,tok.slot0[k],tok.slot1[k]);return st,out
    _,out=jax.lax.fori_loop(0,NEVENT,body,(st,out));return out
MARGINS=jax.jit(margins_tokens); DMARGINS=jax.jit(jax.jacfwd(margins_tokens,argnums=0))

def vector_boundary_prediction(theta, tok, step):
    ms=np.asarray(MARGINS(jnp.asarray(theta),tok)); D=np.asarray(DMARGINS(jnp.asarray(theta),tok)); d=D@np.asarray(step,float)
    a=np.where(d<0.0,-ms/d,np.inf); a=np.where(a>0.0,a,np.inf); idx=int(np.argmin(a))
    return idx,float(a[idx]),ms,D,d

def benchmark_checks(run_noise=False):
    theta=jnp.asarray(THETA_TRUE)
    truth_err=float(np.max(np.abs(np.asarray(REPLAY(theta,TRUTH_TOK))-TRUTH_Y))); assert truth_err < 2e-12
    J=np.asarray(JAC(theta,TRUTH_TOK)); Jfd=fd_jac(THETA_TRUE,TRUTH_TOK)
    rel=float(np.linalg.norm(J-Jfd)/np.linalg.norm(Jfd)); assert rel < 1e-8
    svals=np.linalg.svd(J,compute_uv=False); cond=float(svals[0]/svals[-1]); assert svals[-1] > 0.10 and cond < 60.0
    ranks=[int(np.linalg.matrix_rank(J[:k],tol=1e-10)) for k in (3,4,5,6)]; assert ranks == [2,3,4,4]
    s5=np.linalg.svd(J[:5],compute_uv=False); _,_,Vh=np.linalg.svd(J,full_matrices=False); weakest=Vh[-1]; assert np.linalg.norm(weakest[:2]) > 0.95
    sigma=1e-4; cov=sigma**2*np.linalg.inv(J.T@J); std=np.sqrt(np.diag(cov)); corr=cov/np.outer(std,std)
    old_std=np.array([0.000427826116721,0.000538144994604]); inflation=std[:2]/old_std; assert np.all((inflation>1.35)&(inflation<1.55))
    assert np.max(np.abs(J[:3,:2])) < 1e-12; assert np.linalg.matrix_rank(J[:3,2:],tol=1e-10)==2
    regular=optimize((-3.5,8.2,.05,-.04)); one=optimize((-3.0,7.7,-.08,.06)); two=optimize((-3.2,7.7,-.07,-.12)); zero_eta=optimize((-4.0,8.0,0.0,0.0)); routed=optimize((-4.0,8.0,.03,-.02))
    for sol in (regular,one,two,zero_eta,routed):
        assert np.max(np.abs(sol.x-THETA_TRUE)) < 6e-12; assert sol.obj < 1e-23
    assert (regular.hits,regular.switches)==(0,0); assert (one.hits,one.switches)==(1,1); assert (two.hits,two.switches)==(2,2); assert (zero_eta.hits,zero_eta.switches)==(1,1); assert (routed.hits,routed.switches)==(0,0)
    cross_data=[]
    for ci,c in enumerate(two.crossings):
        x=two.history[ci][1]; tok,_=record_tokens(x); r=np.asarray(REPLAY(jnp.asarray(x),tok))-TRUTH_Y; JJ=np.asarray(JAC(jnp.asarray(x),tok)); step=-np.linalg.lstsq(JJ,r,rcond=None)[0]
        tr=np.array([.55,.55,.20,.20]); step/=max(np.max(np.abs(step)/tr),1.0); idx,apred,ms,D,d=vector_boundary_prediction(x,tok,step); aexact=float(c['alpha_boundary']); pred_rel=abs(apred-aexact)/aexact; assert pred_rel < 0.02
        safe=np.asarray(c['safe_point']); cross=np.asarray(c['cross_point']); ts,_=record_tokens(safe); tc,_=record_tokens(cross)
        prefd=fd_jac(safe,ts); postfd=fd_jac(cross,tc); pre_rel=float(np.linalg.norm(np.asarray(JAC(jnp.asarray(safe),ts))-prefd)/np.linalg.norm(prefd)); post_rel=float(np.linalg.norm(np.asarray(JAC(jnp.asarray(cross),tc))-postfd)/np.linalg.norm(postfd)); assert pre_rel < 3e-8 and post_rel < 3e-8
        diffs=[i for i,(a,b) in enumerate(zip(c['old_sig'],c['new_sig'])) if a!=b]
        if ci==0: assert diffs==[0,1] and idx==0
        if ci==1: assert diffs==[9,10] and idx==9
        assert c['safe_margin']>0 and c['cross_obj']<c['safe_obj']<c['old_obj']
        cross_data.append(dict(index=idx,alpha_prediction=apred,alpha_exact=aexact,prediction_relative_error=pred_rel,boundary_point=np.asarray(c['boundary_point']),safe_point=safe,safe_margin=float(c['safe_margin']),cross_point=cross,old_objective=float(c['old_obj']),safe_objective=float(c['safe_obj']),cross_objective=float(c['cross_obj']),changed_event_indices=diffs,pre_jax_fd_relative_error=pre_rel,post_jax_fd_relative_error=post_rel))
    emp_mean=np.array([-3.26790806,8.00010559,2.80816619e-06,-2.38508362e-06]); emp_std=np.array([5.64607233e-04,6.48323271e-04,2.13300223e-05,3.03620965e-05]); assert np.all((emp_std/std)>0.70) and np.all((emp_std/std)<1.05)
    out=dict(truth_replay_max_error=truth_err,jax_fd_relative_error=rel,jacobian=J,singular_values=svals,condition_number=cond,ranks_first_3_4_5_6=ranks,first5_smallest_singular=float(s5[-1]),weakest_right_singular_vector=weakest,fisher_std=std,correlation=corr,parameter_std_inflation_vs_v018=inflation,regular=(regular.iterations,regular.hits,regular.switches),one_cross=(one.iterations,one.hits,one.switches),two_cross=(two.iterations,two.hits,two.switches),zero_eta_from_minus4=(zero_eta.iterations,zero_eta.hits,zero_eta.switches),routed_latent_from_minus4=(routed.iterations,routed.hits,routed.switches),two_cross_solution=two.x,two_cross_objective=two.obj,crossings=cross_data,empirical_noise_mean=emp_mean,empirical_noise_std=emp_std)
    if run_noise:
        rng=np.random.default_rng(123); xs=[]
        from scipy.optimize import least_squares
        for _ in range(20):
            data=TRUTH_Y+rng.normal(scale=sigma,size=TRUTH_Y.shape)
            sol=least_squares(lambda x:np.asarray(REPLAY(jnp.asarray(x),TRUTH_TOK))-data,THETA_TRUE+np.array([.02,-.02,.005,-.005]),jac=lambda x:np.asarray(JAC(jnp.asarray(x),TRUTH_TOK)),max_nfev=30,xtol=1e-13,ftol=1e-13,gtol=1e-13); xs.append(sol.x)
        xs=np.asarray(xs); mean=xs.mean(0); estd=xs.std(0,ddof=1); assert np.max(np.abs(mean-emp_mean)) < 2e-8; assert np.max(np.abs(estd-emp_std)) < 2e-8; out['noise_direct_mean']=mean;out['noise_direct_std']=estd
    return out

def main():
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--noise-direct',action='store_true');args=ap.parse_args(); out=benchmark_checks(args.noise_direct)
    print('CORE v0.20 latent-state multi-chart inference checks passed')
    for k,v in out.items(): print(k,v)
if __name__=='__main__': main()
