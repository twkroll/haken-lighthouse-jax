"""Optional tighter velocity-bound and safeguarded Newton first-hitting v0.9.

Not a replacement for canonical Layer A. Mathematical baseline RB-004 fixed-delay,
no phase reset. Exact alpha propagation and adaptive quad still used; only
safe velocity-bound rejection and same-segment primitive caching are new.

No stochastic data, training, inference or confirmation is performed here.
"""
from __future__ import annotations

from math import pi
import heapq
import numpy as np
from scipy.optimize import brentq

from . import sparse
from .reference import normalize_history, response, propagate_alpha
from .sparse import SparseParameters, SparseEvent, SparseRecord


def _integrated(i: int, dt: float, a: np.ndarray, q: np.ndarray, p: SparseParameters) -> float:
    """Expose same physical phase integration to deterministic work instrumentation."""
    return sparse._integrated(i, dt, a, q, p)



def _safe_velocity_upper(i:int, dt:float, a:np.ndarray, q:np.ndarray, p:SparseParameters)->float:
    """Rigorous maximum segment rate for baseline S, from alpha-input extrema.

    Each node input is exp(-alpha*s) * (wa + s*wq) for s in [0,dt].
    This has at most one internal stationary point. S is nondecreasing.
    Round upward a few ulps to avoid accidental exclusion at floating edges.
    """
    edges=p.incoming[i]
    if len(edges)==0:
        return float(np.nextafter(response(0.,p.r,p.h),np.inf))
    wa=float(np.dot(p.weight[edges],a[edges]))
    wq=float(np.dot(p.weight[edges],q[edges]))
    xs=[wa,float(np.exp(-p.alpha*dt)*(wa+dt*wq))]
    if wq!=0.0:
        stationary=1.0/p.alpha-wa/wq
        if 0 < stationary < dt:
            xs.append(float(np.exp(-p.alpha*stationary)*(wa+stationary*wq)))
    return float(np.nextafter(response(max(xs),p.r,p.h),np.inf))


def _newton_bracketed(i:int,dt:float,gap:float,endpoint_integral:float,
                      a:np.ndarray,q:np.ndarray,p:SparseParameters)->float:
    """Safeguarded monotone event root. The original Brent solve is fallback.

    Endpoint and internal integrals use unchanged authoritative scipy.quad.
    In contrast to an interpolation-only event solve, this returns ONLY after
    checking the physical section residual against a fixed tolerance.
    """
    edges=p.incoming[i]
    wa=float(np.dot(p.weight[edges],a[edges]))
    wq=float(np.dot(p.weight[edges],q[edges]))
    lo=0.;hi=dt
    x=float(np.clip(dt*gap/endpoint_integral,0.05*dt,0.95*dt))
    for it in range(7):
        value=_integrated(i,x,a,q,p)-gap
        if abs(value)<=2e-12:
            return x
        if value>0.: hi=x
        else:lo=x
        psi=float(np.exp(-p.alpha*x)*(wa+x*wq))
        slope=response(psi,p.r,p.h)
        proposal=x-value/slope if slope>1e-10 else np.nan
        if not np.isfinite(proposal) or proposal<=lo or proposal>=hi:
            proposal=0.5*(lo+hi)
        x=float(proposal)
    # Fallback never substitutes an approximate interpolant for true first hit.
    return brentq(lambda s:_integrated(i,s,a,q,p)-gap,lo,hi,
                  xtol=1e-12,rtol=9e-16)

def physical_rerecord_v09(p: SparseParameters, *, horizon: float,
                             initial_theta=None, history=None, max_events=2000,
                             collision_tol=1e-8, transversality_tol=1e-10):
    """Alternative physical rerecorder with conservative phase-bound skipping.

    Between discontinuities 0<=theta_dot<1 (RB-004), so a neuron with
    theta_target - theta_now >= next_interval_length cannot fire in the
    interval. Endpoint integration is skipped for it but never for its
    eventual state advance. Endpoint values are cached for the phase update
    if the next physical event is that endpoint. Root-finding uses precisely
    the baseline `_integrated` and brentq tolerance and stays event-driven.
    """
    if not np.isfinite(horizon) or horizon <= 0:
        raise ValueError('bad horizon')
    hist=normalize_history(history,p.n)
    theta0=np.zeros(p.n) if initial_theta is None else np.array(initial_theta,dtype=float,copy=True)
    if theta0.shape != (p.n,) or not np.isfinite(theta0).all() or (theta0 < 0).any() or (theta0 >= 2*pi).any():
        raise ValueError('initial phase expected in [0,2pi)')
    theta=theta0.copy()
    a,q,queue,initial_arrived=sparse._seed(p,hist)
    a0,q0=a.copy(),q.copy()
    t=0.; count=np.zeros(p.n,dtype=int)
    events=[]; spikes=[]; warnings=[]
    if any(abs(emit+float(p.delay[eid]))<=collision_tol for eid,ordinal in initial_arrived
           for emit in [hist[int(p.source[eid])][ordinal+len(hist[int(p.source[eid])])-1]]):
        warnings.append('INITIAL_ARRIVAL_CHART_BOUNDARY')

    for _ in range(max_events):
        if t >= horizon-1e-12:
            break
        next_arrival=queue[0][0] if queue else float('inf')
        endpoint=min(horizon,next_arrival)
        dt=endpoint-t
        if dt < -1e-10: raise RuntimeError('arrival in past')
        dt=max(0.,dt)
        endpoint_integrals=np.full(p.n,np.nan)
        candidates=[]
        for i in range(p.n):
            target_phase=2*pi*(count[i]+1)
            gap=target_phase-theta[i]
            # Rigorous global upper bound theta_dot<1 for RB-004 response.
            # Skip endpoint search only; the final state flow is never skipped.
            if gap >= dt or gap > dt*_safe_velocity_upper(i,dt,a,q,p)+2e-14:
                continue
            integrated_endpoint=_integrated(i,dt,a,q,p)
            endpoint_integrals[i]=integrated_endpoint
            end_gap=integrated_endpoint-gap
            if end_gap>=-1e-12:
                if -gap<0 and end_gap>1e-12:
                    root=_newton_bracketed(i,dt,gap,integrated_endpoint,a,q,p)
                else:
                    root=dt
                candidates.append((t+root,i))
        earliest=min((ts for ts,i in candidates),default=float('inf'))
        event_t=min(endpoint,earliest)
        near_spikes=[i for ts,i in candidates if abs(ts-event_t)<=collision_tol]
        near_arrivals=[item for item in queue if abs(item[0]-event_t)<=collision_tol]
        if len(near_spikes)+len(near_arrivals)>1:
            warnings.append(f'EVENT_CHART_COLLISION_NEAR:t={event_t:.12g}')
        if near_arrivals and abs(event_t)<=collision_tol:
            warnings.append('INITIAL_ARRIVAL_CHART_BOUNDARY')
        if (near_spikes or near_arrivals) and abs(event_t-horizon)<=collision_tol:
            warnings.append('HORIZON_EVENT_CHART_BOUNDARY')
        elapsed=max(0.,event_t-t)
        if elapsed == dt:
            increments=np.asarray([
                float(endpoint_integrals[i]) if np.isfinite(endpoint_integrals[i]) else _integrated(i,elapsed,a,q,p)
                for i in range(p.n)
            ])
        else:
            increments=np.asarray([_integrated(i,elapsed,a,q,p) for i in range(p.n)])
        theta+=increments
        a,q=propagate_alpha(a,q,elapsed,p.alpha)
        t=event_t
        due_spikes=[i for ts,i in candidates if abs(ts-t)<=2e-11]
        for i in sorted(due_spikes):
            count[i]+=1
            theta[i]=2*pi*count[i]
            edges=p.incoming[i]
            psi=float(np.sum(p.weight[edges]*a[edges]))
            velocity=response(psi,p.r,p.h)
            if velocity<=transversality_tol:
                warnings.append(f'NONTRANSVERSAL:{i}:{count[i]}')
            event=SparseEvent(t,'spike',i,-1,int(count[i]),-1,velocity)
            events.append(event);spikes.append(event)
            for eid in p.outgoing[i]:
                target=int(p.target[eid]);arr_t=t+float(p.delay[eid])
                heapq.heappush(queue,(arr_t,target,i,int(count[i]),int(eid)))
                if arr_t==t:
                    warnings.append(f'ZERO_DELAY_EVENT_CHART_BOUNDARY:t={t:.12g}')
        while queue and abs(queue[0][0]-t)<=2e-11:
            _,target,source,ordinal,eid=heapq.heappop(queue)
            q[eid]+=p.alpha**2
            events.append(SparseEvent(t,'arrival',target,source,ordinal,eid))
    else:
        warnings.append('EVENT_BUDGET_EXCEEDED')
    return SparseRecord(tuple(events),tuple(spikes),not bool(warnings),tuple(warnings),
                        theta,horizon,theta0,hist,initial_arrived,p.topology_id,a0,q0)
