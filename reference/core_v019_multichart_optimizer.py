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
GXn,GWn=leggauss(20); GX=jnp.asarray(GXn); GW=jnp.asarray(GWn)
MODE=np.array([0,1,2]*3,dtype=int); MODEJ=jnp.asarray(MODE)
TARGET=np.array([0,1,2,1,2,0,2,0,1],dtype=int); TARGETJ=jnp.asarray(TARGET)
PSI0=np.array([-0.207423841618632]*3); Q0=np.array([0.780899408476725]*3)
PHI0=np.array([1.838519273976891,1.488519273976891,1.658519273976891])
CANON=((0,0),(2,0),(1,0),(0,1),(2,1),(1,1))
KIND_A=0; KIND_F=1

class Tokens(NamedTuple):
    kind:jax.Array; idx:jax.Array; guess:jax.Array; slot0:jax.Array; slot1:jax.Array
class JState(NamedTuple):
    t:jax.Array; psi:jax.Array; q:jax.Array; phi:jax.Array; active:jax.Array; edge_id:jax.Array; rho:jax.Array; counts:jax.Array; obs:jax.Array

def edge_weight_np(p,e):
    r=e%3; return 1.0 if r==0 else (p if r==1 else -p)
def phase_gain_np(psi,q,dt):
    s=.5*dt*(GXn+1); ee=np.exp(-ALPHA*s); ps=ee*(psi+q*s); y=ps+1.; vals=np.where(y>0,np.exp(-1/np.maximum(y,1e-15)**2),0.)
    return float(.5*dt*np.dot(GWn,vals))
def firing_time_np(psi,q,phi):
    deficit=TWO_PI-phi
    if deficit<=1e-12:return 0.
    f=lambda t:phase_gain_np(psi,q,t)-deficit
    hi=1.
    while f(hi)<0: hi*=2
    return brentq(f,0,hi,xtol=1e-13,rtol=1e-13)
@dataclass
class NS:
    t:float; psi:np.ndarray; q:np.ndarray; phi:np.ndarray; active:np.ndarray; edge_id:np.ndarray; rho:np.ndarray

def ns0():return NS(0.,PSI0.copy(),Q0.copy(),PHI0.copy(),np.zeros(QMAX,bool),np.zeros(QMAX,int),np.zeros(QMAX))
def adv_np(st,dt,tau):
    op=st.psi.copy(); oq=st.q.copy(); st.phi += np.array([phase_gain_np(op[i],oq[i],dt) for i in range(N)])
    e=math.exp(-ALPHA*dt); st.psi=e*(op+oq*dt); st.q=e*oq
    speed=np.where(MODE[st.edge_id]==1,.5,1./tau); st.rho=np.where(st.active,st.rho-speed*dt,st.rho); st.t+=dt

def record_tokens(theta):
    p,tau=map(float,theta); st=ns0(); counts=np.zeros(N,int); obs=np.full((N,2),np.nan); rows=[]
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
            for sl,e in zip(free,(3*i+1,3*i+2)):st.active[sl]=True;st.edge_id[sl]=e;st.rho[sl]=1.
            if counts[i]<2:obs[i,counts[i]]=st.t
            counts[i]+=1;rows.append((kind,i,dt,int(free[0]),int(free[1])))
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
def js0():return JState(jnp.array(0.),jnp.asarray(PSI0),jnp.asarray(Q0),jnp.asarray(PHI0),jnp.zeros(QMAX,bool),jnp.zeros(QMAX,jnp.int32),jnp.zeros(QMAX),jnp.zeros(N,jnp.int32),jnp.full((N,2),jnp.nan))
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
    p,tau=theta; st=js0()
    def body(k,st):
        kind=tok.kind[k];idx=tok.idx[k];guess=tok.guess[k];ft,at=candidate_times(st,tau,guess);dt=jnp.where(kind==KIND_F,ft[idx],at[idx]);st=adv(st,dt,tau);return process_one(st,p,kind,idx,tok.slot0[k],tok.slot1[k])
    st=jax.lax.fori_loop(0,NEVENT,body,st);return jnp.stack([st.obs[i,j] for i,j in CANON])
def margin_tokens(theta,tok):
    p,tau=theta;st=js0();m=jnp.array(jnp.inf)
    def body(k,carry):
        st,m=carry;kind=tok.kind[k];idx=tok.idx[k];guess=tok.guess[k];ft,at=candidate_times(st,tau,guess)
        fcomp=ft.at[idx].set(jnp.inf); acomp=at.at[idx].set(jnp.inf)
        sel=jnp.where(kind==KIND_F,ft[idx],at[idx]); comp=jnp.where(kind==KIND_F,jnp.minimum(jnp.min(fcomp),jnp.min(at)),jnp.minimum(jnp.min(ft),jnp.min(acomp)))
        st=adv(st,sel,tau);st=process_one(st,p,kind,idx,tok.slot0[k],tok.slot1[k]);return st,jnp.minimum(m,comp-sel)
    _,m=jax.lax.fori_loop(0,NEVENT,body,(st,m));return m

REPLAY=jax.jit(replay_tokens); JAC=jax.jit(jax.jacfwd(replay_tokens,argnums=0)); MARGIN=jax.jit(margin_tokens)
TRUTH_TOK,TRUTH_Y=record_tokens((P_TRUE,TAU_TRUE))

def sig(tok):return tuple(zip(np.asarray(tok.kind).tolist(),np.asarray(tok.idx).tolist()))
def pobj(x):return .5*np.sum((record_tokens(x)[1]-TRUTH_Y)**2)
@dataclass
class Result:
    x:np.ndarray;obj:float;iterations:int;switches:int;hits:int;history:list;crossings:list

def optimize(x0,maxit=15):
    x=np.array(x0,float);tok,_=record_tokens(x);switches=hits=0;hist=[];cross=[]
    for it in range(maxit):
        y=np.asarray(REPLAY(jnp.asarray(x),tok));r=y-TRUTH_Y;obj=.5*r@r;m=float(MARGIN(jnp.asarray(x),tok));hist.append((it,x.copy(),obj,m,sig(tok)))
        if np.linalg.norm(r)<1e-11:return Result(x,float(obj),it,switches,hits,hist,cross)
        J=np.asarray(JAC(jnp.asarray(x),tok));s=-np.linalg.lstsq(J,r,rcond=None)[0];scale=max(abs(s[0])/.55,abs(s[1])/.55,1.);s/=scale
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

def finite_difference_jac(theta,tok,h=1e-6):
    theta=np.asarray(theta,float); cols=[]
    for j in range(2):
        e=np.zeros(2);e[j]=1.0
        yp=np.asarray(REPLAY(jnp.asarray(theta+h*e),tok))
        ym=np.asarray(REPLAY(jnp.asarray(theta-h*e),tok))
        cols.append((yp-ym)/(2*h))
    return np.column_stack(cols)

def benchmark_checks(run_all_starts=False):
    truth_err=float(np.max(np.abs(np.asarray(REPLAY(jnp.asarray([P_TRUE,TAU_TRUE]),TRUTH_TOK))-TRUTH_Y)))
    assert truth_err < 1e-12
    x0=np.array([-4.0,8.0]); tok0,_=record_tokens(x0)
    J0=np.asarray(JAC(jnp.asarray(x0),tok0)); J0fd=finite_difference_jac(x0,tok0)
    rel0=float(np.linalg.norm(J0-J0fd)/np.linalg.norm(J0fd)); assert rel0 < 2e-8
    r0=np.asarray(REPLAY(jnp.asarray(x0),tok0))-TRUTH_Y
    s=-np.linalg.lstsq(J0,r0,rcond=None)[0]; s=s/max(abs(s[0])/.55,abs(s[1])/.55,1.0)
    m0=float(MARGIN(jnp.asarray(x0),tok0)); mcand=float(MARGIN(jnp.asarray(x0+s),tok0))
    gm=np.asarray(jax.grad(margin_tokens,argnums=0)(jnp.asarray(x0),tok0)); d=float(gm@s); alpha_lin=float(-m0/d)
    lo,hi=0.0,1.0
    for _ in range(60):
        mid=.5*(lo+hi)
        if float(MARGIN(jnp.asarray(x0+mid*s),tok0))>0: lo=mid
        else: hi=mid
    alpha_exact=.5*(lo+hi)
    assert m0>0 and mcand<0 and abs(alpha_lin-alpha_exact)/alpha_exact < 0.005
    cross=optimize(x0)
    assert cross.switches==1 and cross.hits==1 and cross.iterations <= 6
    assert np.max(np.abs(cross.x-np.array([P_TRUE,TAU_TRUE]))) < 5e-12 and cross.obj < 1e-24
    c=cross.crossings[0]; assert c['safe_margin']>0 and c['old_sig'] != c['new_sig'] and c['cross_obj'] < c['safe_obj'] < c['old_obj']
    xpost=np.asarray(c['cross_point']); tokpost,_=record_tokens(xpost)
    Jp=np.asarray(JAC(jnp.asarray(xpost),tokpost)); Jpfd=finite_difference_jac(xpost,tokpost)
    relp=float(np.linalg.norm(Jp-Jpfd)/np.linalg.norm(Jpfd)); assert relp < 2e-8
    regular=optimize((-3.5,8.2)); assert regular.switches==0 and regular.hits==0 and regular.iterations <= 5
    assert np.max(np.abs(regular.x-np.array([P_TRUE,TAU_TRUE]))) < 5e-12
    extras=[]
    if run_all_starts:
        for start in [(-4.1,7.8),(-3.95,8.25)]:
            o=optimize(start); assert o.switches==1 and o.hits==1 and o.iterations<=7
            assert np.max(np.abs(o.x-np.array([P_TRUE,TAU_TRUE]))) < 5e-12; extras.append((start,o.x,o.iterations))
    return {'truth_replay_max_error':truth_err,'prechart_jax_fd_relative_error':rel0,'postchart_jax_fd_relative_error':relp,'initial_objective':pobj(x0),'initial_margin':m0,'naive_trust_step':s,'naive_candidate_margin':mcand,'margin_gradient':gm,'alpha_linear_prediction':alpha_lin,'alpha_exact_boundary':alpha_exact,'alpha_prediction_relative_error':abs(alpha_lin-alpha_exact)/alpha_exact,'boundary_point':c['boundary_point'],'safe_point':c['safe_point'],'safe_margin':c['safe_margin'],'cross_point':c['cross_point'],'old_last_events':c['old_sig'][9:12],'new_last_events':c['new_sig'][9:12],'old_objective':c['old_obj'],'safe_objective':c['safe_obj'],'cross_objective':c['cross_obj'],'crossing_solution':cross.x,'crossing_iterations':cross.iterations,'chart_switches':cross.switches,'boundary_hits':cross.hits,'regular_solution':regular.x,'regular_iterations':regular.iterations,'extras':extras}

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--all-starts',action='store_true'); args=ap.parse_args()
    out=benchmark_checks(args.all_starts)
    print('CORE v0.19 hybrid multi-chart optimizer checks passed')
    for k,v in out.items(): print(k,v)
if __name__=='__main__': main()
