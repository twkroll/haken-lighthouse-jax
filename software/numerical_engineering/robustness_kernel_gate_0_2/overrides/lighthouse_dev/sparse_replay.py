"""Noncanonical JAX edge-coordinate fixed-chart replay (RB-004 baseline).

Chart is static data; derivative_record_sparse PHYSICALLY re-records before AD.
Direct replay is unguarded and only meaningful on a verified regular chart.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from .sparse import SparseParameters, SparseRecord, physical_rerecord_sparse


@lru_cache(None)
def _quadrature(k=64):
    nodes,weights=np.polynomial.legendre.leggauss(k)
    # Endpoint-clustered transformation s=dt*u**2 resolves sharp alpha
    # arrivals without changing the physical equations. Fixed-node JAX is
    # still validated by the pulse-aware physical authority before AD.
    return np.asarray((nodes+1)/2),np.asarray(weights/2)


def _rate(psi,r,h):
    gap=psi-h
    return jnp.where(gap>0,jnp.exp(-r/jnp.maximum(gap,1e-50)**2),0.)


def _flow(theta,a,q,dt,weights,targets,n,alpha,r,h):
    nodes_np,quadweights_np=_quadrature()
    # The endpoint-clustered rule is used only for fast alpha pulses.
    # Preserve the tested legacy 64-point Gauss rule for ordinary alpha.
    if alpha >= 100.:
        u=nodes_np
        nodes_np,quadweights_np=nodes_np*nodes_np,2*u*quadweights_np
    nodes,quadweights=jnp.asarray(nodes_np),jnp.asarray(quadweights_np)
    s=dt*nodes
    aq=jnp.exp(-alpha*s[:,None])*(a[None,:]+s[:,None]*q[None,:])
    contributions=aq*weights[None,:]
    psi=jnp.zeros((len(nodes),n),dtype=weights.dtype).at[:,targets].add(contributions)
    integrated=dt*jnp.sum(quadweights[:,None]*_rate(psi,r,h),axis=0)
    decay=jnp.exp(-alpha*dt)
    return theta+integrated,decay*(a+dt*q),decay*q


def _velocity(i,dt,a,q,weights,targets,n,alpha,r,h):
    aq=jnp.exp(-alpha*dt)*(a+dt*q)
    psi=jnp.zeros((n,),dtype=weights.dtype).at[targets].add(weights*aq)
    return _rate(psi[i],r,h)


def _root_duration(i,target,guess,theta,a,q,weights,targets,n,alpha,r,h):
    def update(_,duration):
        future,_,_=_flow(theta,a,q,duration,weights,targets,n,alpha,r,h)
        v=_velocity(i,duration,a,q,weights,targets,n,alpha,r,h)
        return duration-(future[i]-target)/jnp.maximum(v,1e-12)
    return jax.lax.fori_loop(0,12,update,jnp.asarray(guess))


def prepare_replay(record:SparseRecord,p:SparseParameters):
    """Build fixed-size event/arrival/emission arrays for jax.lax.scan.

    Not a physical chart validation; repeated physical validation is done at
    each proposed point by derivative_record_sparse or caller guard.
    """
    if not record.chart_valid or record.topology_id!=p.topology_id:
        raise ValueError('invalid or wrong reference chart/topology')
    emitted={}
    history_values=[]
    for src,times in enumerate(record.history):
        for idx,t in enumerate(times):
            ordinal=idx-len(times)+1
            emitted[(src,ordinal)]=len(history_values)
            history_values.append(float(t))
    offset=len(history_values)
    kind=[];neuron=[];edge=[];ordinals=[];guess=[];arrival_emission=[];emit_slot=[]
    prev=0.
    for idx,ev in enumerate(record.events):
        is_spike=(ev.kind=='spike')
        if is_spike:
            emitted[(ev.neuron,ev.ordinal)]=offset+idx
        else:
            if (ev.source,ev.ordinal) not in emitted:
                raise ValueError('Arrival has no emitted spike')
        kind.append(int(is_spike))
        neuron.append(ev.neuron)
        edge.append(ev.edge_id if not is_spike else 0)
        ordinals.append(ev.ordinal if is_spike else 0)
        guess.append(ev.t-prev)
        arrival_emission.append(emitted.get((ev.source,ev.ordinal),0) if not is_spike else 0)
        emit_slot.append(offset+idx if is_spike else 0)
        prev=ev.t
    arrived_edges=[];arrived_emits=[]
    for eid,ordinal in record.initial_arrived:
        source=int(p.source[eid]);times=record.history[source]
        arrived_edges.append(eid)
        arrived_emits.append(times[ordinal+len(times)-1])
    data={
        'kind':jnp.asarray(kind,dtype=jnp.int32),
        'neuron':jnp.asarray(neuron,dtype=jnp.int32),
        'edge':jnp.asarray(edge,dtype=jnp.int32),
        'ordinal':jnp.asarray(ordinals,dtype=jnp.int32),
        'guess':jnp.asarray(guess,dtype=jnp.float64),
        'arrival_emission':jnp.asarray(arrival_emission,dtype=jnp.int32),
        'emit_slot':jnp.asarray(emit_slot,dtype=jnp.int32),
        'initial_arrived_edges':jnp.asarray(arrived_edges,dtype=jnp.int32),
        'initial_arrived_emits':jnp.asarray(arrived_emits,dtype=jnp.float64),
        'emission_init':jnp.asarray(history_values+[0.]*len(record.events),dtype=jnp.float64),
        'targets':jnp.asarray(p.target,dtype=jnp.int32),
        'spike_positions':np.asarray([k for k,e in enumerate(record.events) if e.kind=='spike'],dtype=int),
    }
    return data


def replay_sparse_fixed_chart(weights,delays,initial_theta,record:SparseRecord,
                              p:SparseParameters,*, prepared=None):
    """Pure JAX scan with fixed chart. Does not physically certify new proposals."""
    data=prepare_replay(record,p) if prepared is None else prepared
    weights=jnp.asarray(weights)
    # No arrivals and no spikes: JAX cannot trace dynamic indexing of an
    # empty emissions array, even if scan has zero iterations. The physical
    # event tape is static: returning an empty spike vector is exact.
    if len(record.events) == 0:
        return jnp.zeros((0,), dtype=weights.dtype)
    delays=jnp.asarray(delays)
    theta=jnp.asarray(initial_theta)
    targets=data['targets']
    n=p.n;alpha=p.alpha;r=p.r;h=p.h
    arrived_edges=data['initial_arrived_edges']
    arrived_age=-(data['initial_arrived_emits']+delays[arrived_edges])
    factors=jnp.exp(-alpha*arrived_age)*alpha**2
    a=jnp.zeros_like(weights).at[arrived_edges].add(arrived_age*factors)
    q=jnp.zeros_like(weights).at[arrived_edges].add(factors)
    init=(jnp.asarray(0.,dtype=weights.dtype),theta,a,q,data['emission_init'])
    def scan_step(carry,event_data):
        t,th,aa,qq,emissions=carry
        kind,neuron,eid,ordinal,guess,emission_idx,slot=event_data
        def on_spike(_):
            target=2*jnp.pi*ordinal
            dt=_root_duration(neuron,target,guess,th,aa,qq,weights,targets,n,alpha,r,h)
            newtheta,newa,newq=_flow(th,aa,qq,dt,weights,targets,n,alpha,r,h)
            newtheta=newtheta.at[neuron].set(target)
            return t+dt,newtheta,newa,newq
        def on_arrival(_):
            # The zero-edge graph has no arrivals, but lax.cond traces this
            # branch anyway. Avoid indexing the empty edge axis during tracing.
            if p.e:
                delay=jnp.take(delays,eid,mode='fill',fill_value=0.)
                arrival=emissions[emission_idx]+delay
                dt=arrival-t
                newtheta,newa,newq=_flow(th,aa,qq,dt,weights,targets,n,alpha,r,h)
                newq=newq.at[eid].add(alpha**2)
            else:
                arrival=t
                newtheta,newa,newq=th,aa,qq
            return arrival,newtheta,newa,newq
        newt,newtheta,newa,newq=jax.lax.cond(kind==1,on_spike,on_arrival,operand=None)
        emissions=emissions.at[slot].set(jnp.where(kind==1,newt,emissions[slot]))
        return (newt,newtheta,newa,newq,emissions),newt
    event_data=tuple(data[k] for k in ('kind','neuron','edge','ordinal','guess','arrival_emission','emit_slot'))
    _,event_times=jax.lax.scan(scan_step,init,event_data)
    return event_times[data['spike_positions']]


@dataclass(frozen=True)
class SparseDerivativeRecord:
    token:str
    times:np.ndarray
    d_times_d_edge_weights:np.ndarray
    d_times_d_edge_delays:np.ndarray
    d_times_d_initial_theta:np.ndarray
    max_reference_disagreement:float


def _require_certified_physical_tape(p:SparseParameters,record:SparseRecord,*,tol=1e-8):
    """Re-record base, fail closed on *timestamp*-stale or internally forged tapes.

    Token equality alone only checks labelled itinerary; timestamps, spike list
    and initial alpha state are validated separately. Direct fixed-chart JAX
    remains intentionally unguarded and must not be used as physical authority.
    """
    physical=physical_rerecord_sparse(p,horizon=record.horizon,
                                     initial_theta=record.initial_theta,
                                     history=record.history)
    valid=(record.chart_valid and physical.chart_valid and
           record.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1' and
           physical.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1' and
           record.topology_id==p.topology_id==physical.topology_id and
           record.token==physical.token and
           len(record.events)==len(physical.events) and
           record.initial_arrived==physical.initial_arrived and
           record.spikes==tuple(ev for ev in record.events if ev.kind=='spike'))
    if valid:
        valid=(all(np.isfinite([a.t,b.t]).all() and abs(a.t-b.t)<=tol
                   for a,b in zip(record.events,physical.events)) and
               np.shape(record.initial_a)==np.shape(physical.initial_a) and
               np.shape(record.initial_q)==np.shape(physical.initial_q) and
               np.shape(record.final_theta)==np.shape(physical.final_theta) and
               np.isfinite(record.initial_a).all() and
               np.isfinite(record.initial_q).all() and
               np.isfinite(record.final_theta).all() and
               np.allclose(record.initial_a,physical.initial_a,rtol=0,atol=1e-12) and
               np.allclose(record.initial_q,physical.initial_q,rtol=0,atol=1e-12) and
               np.allclose(record.final_theta,physical.final_theta,rtol=0,atol=3e-8))
    if not valid:
        raise ValueError('Stale/invalid chart: incomplete, uncertified or inconsistent physical tape; rerecord required')
    return physical


def derivative_record_sparse(p:SparseParameters,record:SparseRecord,*,tol=1e-7):
    physical=_require_certified_physical_tape(p,record)
    prepared=prepare_replay(record,p)
    def f(w,d,th):
        return replay_sparse_fixed_chart(w,d,th,record,p,prepared=prepared)
    values=np.asarray(f(p.weight,p.delay,record.initial_theta))
    expected=physical.spike_times()
    diff=float(np.max(np.abs(values-expected))) if len(values) else 0.
    if not np.isfinite(diff) or diff>tol:
        raise ValueError(f'Sparse replay disagrees with reference {diff}')
    dw,dd,dt=jax.jacrev(f,argnums=(0,1,2))(p.weight,p.delay,record.initial_theta)
    result=SparseDerivativeRecord(record.token,values,np.asarray(dw),np.asarray(dd),np.asarray(dt),diff)
    if not all(np.isfinite(x).all() for x in (result.d_times_d_edge_weights,
        result.d_times_d_edge_delays,result.d_times_d_initial_theta)):
        raise ValueError('nonfinite fixed-chart Jacobian')
    return result


def guarded_batch_replay(p:SparseParameters,record:SparseRecord,weights,*,delays=None,initial_theta=None):
    """Vmap on a bucket containing *one physically validated event itinerary*.

    Rejects the ENTIRE batch on any topology/chart change (no silent interpolation).
    All proposals are independently physically rerecorded first.
    """
    # Before evaluating any batch candidates, certify the supplied base tape.
    # Candidate-only rerecords cannot detect stale base timestamps with the
    # same itinerary token (a regression discovered in Gate 0.2).
    _require_certified_physical_tape(p,record)
    weight_batch=np.asarray(weights,dtype=float)
    if weight_batch.ndim!=2 or weight_batch.shape[1]!=p.e:
        raise ValueError('weight batch must be [B,E]')
    b=len(weight_batch)
    d_batch=np.broadcast_to(p.delay,(b,p.e)) if delays is None else np.asarray(delays,dtype=float)
    th_batch=np.broadcast_to(record.initial_theta,(b,p.n)) if initial_theta is None else np.asarray(initial_theta,dtype=float)
    if d_batch.shape!=(b,p.e) or th_batch.shape!=(b,p.n):
        raise ValueError('delay/phase batch shapes mismatch')
    expected=[]
    for weight,delay,theta in zip(weight_batch,d_batch,th_batch):
        proposal=SparseParameters(p.n,p.target,p.source,weight,delay,p.alpha,p.r,p.h)
        fresh=physical_rerecord_sparse(proposal,horizon=record.horizon,initial_theta=theta,history=record.history)
        if (not record.chart_valid or not fresh.chart_valid or
            record.physical_certification != 'NUMENG_PULSE_AWARE_REFERENCE_V1' or
            fresh.physical_certification != 'NUMENG_PULSE_AWARE_REFERENCE_V1' or
            fresh.token != record.token or len(fresh.events) != len(record.events)):
            raise ValueError('Stale/invalid chart in batch: incomplete or uncertified physical tape; rerecord required')
        expected.append(fresh.spike_times())
    prepared=prepare_replay(record,p)
    def function(weight,delay,theta):
        return replay_sparse_fixed_chart(weight,delay,theta,record,p,prepared=prepared)
    predicted=np.asarray(jax.vmap(function)(weight_batch,d_batch,th_batch))
    physical=np.asarray(expected)
    if predicted.shape!=physical.shape or not np.isfinite(predicted).all() or not np.allclose(predicted,physical,rtol=0,atol=1e-7):
        raise ValueError('Batched replay disagrees with rerecorded physical times')
    return predicted
