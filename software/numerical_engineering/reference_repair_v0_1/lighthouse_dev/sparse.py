"""Noncanonical Lighthouse engineering development: O(E) alpha state & delays.

Baseline is RB-004 fixed-edge-delay, first-hitting, no phase reset.
No AI training, preregistered study, or confirmatory data is executed here.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import hashlib
import heapq
import json
from math import pi
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

from .reference import Parameters, normalize_history, response, propagate_alpha


@dataclass(frozen=True)
class SparseParameters:
    """Immutable edges ordered lexicographically by (target,source).

    weights, delays are only allocated on structural edges; ZERO is a legal weight.
    """
    n: int
    target: np.ndarray
    source: np.ndarray
    weight: np.ndarray
    delay: np.ndarray
    alpha: float = 1.0
    r: float = 1.0
    h: float = -1.0
    incoming: tuple = field(init=False, repr=False)
    outgoing: tuple = field(init=False, repr=False)

    def __post_init__(self):
        if not isinstance(self.n, (int, np.integer)) or self.n < 1:
            raise ValueError('n must be a positive integer')
        if ((np.asarray(self.target).size and np.asarray(self.target).dtype.kind not in 'iu')
            or (np.asarray(self.source).size and np.asarray(self.source).dtype.kind not in 'iu')):
            raise ValueError('edge IDs must have integer dtype')
        t = np.array(self.target, dtype=int, copy=True)
        s = np.array(self.source, dtype=int, copy=True)
        w = np.array(self.weight, dtype=float, copy=True)
        d = np.array(self.delay, dtype=float, copy=True)
        if any(x.ndim != 1 or x.size != t.size for x in (t,s,w,d)):
            raise ValueError('edge arrays must be 1D and equally sized')
        if ((t < 0) | (t >= self.n)).any() or ((s < 0) | (s >= self.n)).any():
            raise ValueError('edge endpoints out of range')
        if not np.isfinite(w).all() or not np.isfinite(d).all() or (d < 0).any():
            raise ValueError('nonfinite weights/delays or negative delays')
        if not np.isfinite([self.alpha,self.r,self.h]).all() or self.alpha <= 0 or self.r <= 0:
            raise ValueError('invalid scalar parameters')
        if len(t) > 1 and np.any(t[1:]*self.n+s[1:] <= t[:-1]*self.n+s[:-1]):
            raise ValueError('edges must be unique, sorted (target,source)')
        for x in (t,s,w,d):
            x.flags.writeable = False
        for name,x in [('target',t),('source',s),('weight',w),('delay',d)]:
            object.__setattr__(self,name,x)
        incoming=tuple(np.flatnonzero(t==i) for i in range(self.n))
        outgoing=tuple(np.flatnonzero(s==i) for i in range(self.n))
        for edges in incoming+outgoing:edges.flags.writeable=False
        object.__setattr__(self,'incoming',incoming)
        object.__setattr__(self,'outgoing',outgoing)

    @property
    def e(self):
        return len(self.weight)

    @classmethod
    def from_dense(cls, p: Parameters):
        targets, sources = np.nonzero(p.adjacency)
        return cls(p.n, targets, sources, p.W[targets,sources],
                   p.delays[targets,sources],p.alpha,p.r,p.h)

    def to_dense(self):
        w = np.zeros((self.n,self.n))
        d = np.zeros((self.n,self.n))
        mask = np.zeros((self.n,self.n),dtype=bool)
        w[self.target,self.source] = self.weight
        d[self.target,self.source] = self.delay
        mask[self.target,self.source] = True
        return Parameters(w,d,alpha=self.alpha,r=self.r,h=self.h,adjacency=mask)

    def with_weights(self, weights):
        return SparseParameters(self.n,self.target,self.source,weights,self.delay,
                                self.alpha,self.r,self.h)

    def with_delays(self, delays):
        return SparseParameters(self.n,self.target,self.source,self.weight,delays,
                                self.alpha,self.r,self.h)

    @property
    def topology_id(self):
        raw = json.dumps(dict(n=self.n,edges=list(zip(self.target.tolist(),self.source.tolist()))),sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:20]


@dataclass(frozen=True)
class SparseEvent:
    t: float
    kind: str
    neuron: int
    source: int = -1
    ordinal: int = -1
    edge_id: int = -1
    velocity: float | None = None

    def signature(self):
        return (self.kind,self.neuron,self.source,self.ordinal,self.edge_id)


@dataclass(frozen=True)
class SparseRecord:
    events: tuple[SparseEvent,...]
    spikes: tuple[SparseEvent,...]
    chart_valid: bool
    warnings: tuple[str,...]
    final_theta: np.ndarray
    horizon: float
    initial_theta: np.ndarray
    history: tuple[tuple[float,...],...]
    initial_arrived: tuple[tuple[int,int],...]  # (edge_id, historical ordinal)
    topology_id: str
    initial_a: np.ndarray  # length E
    initial_q: np.ndarray
    physical_certification: str = 'UNVERIFIED'

    @property
    def token(self):
        payload = dict(topology=self.topology_id, history=self.history,
                       initial_arrived=self.initial_arrived,
                       events=[e.signature() for e in self.events])
        return hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:20]

    def spike_times(self, neuron=None):
        return np.asarray([e.t for e in self.spikes if neuron is None or e.neuron==neuron])


def _seed(p:SparseParameters,hist):
    a=np.zeros(p.e)
    q=np.zeros(p.e)
    queue=[]
    arrived=[]
    for eid in range(p.e):
        source=int(p.source[eid]); target=int(p.target[eid]); delay=float(p.delay[eid])
        times=hist[source]
        for k,emit in enumerate(times):
            ordinal=k-len(times)+1
            arrival=emit+delay
            if arrival < 0:
                age=-arrival
                decay=np.exp(-p.alpha*age)
                a[eid] += p.alpha**2*age*decay
                q[eid] += p.alpha**2*decay
                arrived.append((eid,ordinal))
            else:
                heapq.heappush(queue,(arrival,target,source,ordinal,eid))
    return a,q,queue,tuple(sorted(arrived))


def _integrated(i,dt,a,q,p):
    if dt <= 0:
        return 0.
    edges=p.incoming[i]
    if len(edges)==0:
        return dt*response(0.,p.r,p.h)
    wa=float(np.dot(p.weight[edges],a[edges]))
    wq=float(np.dot(p.weight[edges],q[edges]))
    from .physical_first_hit_repair import pulse_aware_integral
    return pulse_aware_integral(dt,wa,wq,p.alpha,p.r,p.h)


def physical_rerecord_sparse(p:SparseParameters,*,horizon,initial_theta=None,
                             history=None,max_events=2000,collision_tol=1e-8,
                             transversality_tol=1e-10):
    if not np.isfinite(horizon) or horizon <= 0:
        raise ValueError('bad horizon')
    hist=normalize_history(history,p.n)
    theta0=np.zeros(p.n) if initial_theta is None else np.array(initial_theta,dtype=float,copy=True)
    if theta0.shape != (p.n,) or not np.isfinite(theta0).all() or (theta0<0).any() or (theta0>=2*pi).any():
        raise ValueError('initial phase expected in [0,2pi)')
    theta=theta0.copy()
    a,q,queue,initial_arrived=_seed(p,hist)
    a0,q0=a.copy(),q.copy()
    t=0.;count=np.zeros(p.n,dtype=int)
    events=[];spikes=[];warnings=[]
    if any(abs(emit+float(p.delay[eid]))<=collision_tol for eid,ordinal in initial_arrived
           for emit in [hist[int(p.source[eid])][ordinal+len(hist[int(p.source[eid])])-1]]):
        warnings.append('INITIAL_ARRIVAL_CHART_BOUNDARY')
    from .physical_first_hit_repair import PhysicalFirstHitUncertified
    try:
        for _ in range(max_events):
            if t >= horizon-1e-12: break
            next_arrival=queue[0][0] if queue else float('inf')
            endpoint=min(horizon,next_arrival)
            dt=endpoint-t
            if dt < -1e-10: raise RuntimeError('arrival in past')
            dt=max(0.,dt)
            candidates=[]
            for i in range(p.n):
                target_phase=2*pi*(count[i]+1)
                end_gap=theta[i]+_integrated(i,dt,a,q,p)-target_phase
                if end_gap>=-1e-12:
                    def gap_at(s,i=i,target_phase=target_phase):
                        return theta[i]+_integrated(i,s,a,q,p)-target_phase
                    if gap_at(0.)<0 and end_gap>1e-12:
                        root=brentq(gap_at,0.,dt,xtol=1e-12,rtol=9e-16)
                    else:
                        root=dt
                    candidates.append((t+root,i))
            earliest=min((ts for ts,i in candidates), default=float('inf'))
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
            theta += np.asarray([_integrated(i,elapsed,a,q,p) for i in range(p.n)])
            a,q=propagate_alpha(a,q,elapsed,p.alpha)
            t=event_t
            due_spikes=[i for ts,i in candidates if abs(ts-t)<=2e-11]
            for i in sorted(due_spikes):
                count[i] += 1
                theta[i]=2*pi*count[i]
                edges=p.incoming[i]
                psi=float(np.sum(p.weight[edges]*a[edges]))
                velocity=response(psi,p.r,p.h)
                if velocity<=transversality_tol:
                    warnings.append(f'NONTRANSVERSAL:{i}:{count[i]}')
                event=SparseEvent(t,'spike',i,-1,int(count[i]),-1,velocity)
                events.append(event);spikes.append(event)
                for eid in p.outgoing[i]:
                    target=int(p.target[eid])
                    arr_t=t+float(p.delay[eid])
                    heapq.heappush(queue,(arr_t,target,i,int(count[i]),int(eid)))
                    if arr_t==t:
                        warnings.append(f'ZERO_DELAY_EVENT_CHART_BOUNDARY:t={t:.12g}')
            while queue and abs(queue[0][0]-t)<=2e-11:
                _,target,source,ordinal,eid=heapq.heappop(queue)
                q[eid]+=p.alpha**2
                events.append(SparseEvent(t,'arrival',target,source,ordinal,eid))
        else:
            warnings.append('EVENT_BUDGET_EXCEEDED')
    except (PhysicalFirstHitUncertified, ValueError, RuntimeError, FloatingPointError, OverflowError) as exc:
        warnings.append(f'PHYSICAL_FIRST_HIT_UNCERTIFIED:{type(exc).__name__}:{exc}')
    return SparseRecord(tuple(events),tuple(spikes),not bool(warnings),tuple(warnings),
                        theta,horizon,theta0,hist,initial_arrived,p.topology_id,a0,q0,
                        'NUMENG_PULSE_AWARE_REFERENCE_V1' if not warnings else 'INVALID')


def sample_sparse(p:SparseParameters,rec:SparseRecord,times,*,verify=True):
    """Sample theta/psi and compact per-edge alpha states. Never dense-expand E into N²."""
    requested=np.asarray(times,dtype=float)
    if requested.ndim!=1 or not np.isfinite(requested).all() or np.any(np.diff(requested)<0):
        raise ValueError('sample times must be finite sorted 1D')
    if np.any(requested<0) or np.any(requested>rec.horizon):
        raise ValueError('sample outside horizon')
    if verify:
        fresh=physical_rerecord_sparse(p,horizon=rec.horizon,initial_theta=rec.initial_theta,history=rec.history)
        if fresh.token!=rec.token or not fresh.chart_valid or not rec.chart_valid or any(abs(x.t-y.t)>1e-9 for x,y in zip(fresh.events,rec.events)):
            raise ValueError('stale/invalid physical chart')
    theta=rec.initial_theta.copy()
    a,q=rec.initial_a.copy(),rec.initial_q.copy()
    t=0.;k=0
    theta_out=[];psi_out=[];a_out=[];q_out=[]
    def advance(dt):
        nonlocal theta,a,q
        theta += np.asarray([_integrated(i,dt,a,q,p) for i in range(p.n)])
        a,q=propagate_alpha(a,q,dt,p.alpha)
    for target_time in requested:
        while k<len(rec.events) and rec.events[k].t<=target_time:
            ev=rec.events[k]
            advance(max(0.,ev.t-t));t=ev.t
            if ev.kind=='spike':theta[ev.neuron]=2*pi*ev.ordinal
            else:q[ev.edge_id]+=p.alpha**2
            k+=1
        advance(max(0.,target_time-t));t=float(target_time)
        theta_out.append(theta.copy());a_out.append(a.copy());q_out.append(q.copy())
        psi_out.append(np.bincount(p.target,weights=p.weight*a,minlength=p.n))
    return dict(times=requested,theta=np.asarray(theta_out).reshape(-1,p.n),
                psi=np.asarray(psi_out).reshape(-1,p.n),
                a=np.asarray(a_out).reshape(-1,p.e),q=np.asarray(q_out).reshape(-1,p.e))
