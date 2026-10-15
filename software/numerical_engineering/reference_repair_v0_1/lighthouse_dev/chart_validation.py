"""Experimental v0.5 chart margin and physically re-recorded FD diagnostics.

NONCANONICAL numerical engineering tool. This module neither defines new
Lighthouse physics nor certifies a globally valid differentiation radius.
Only the physically re-recorded event itinerary can authorize local replay.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from .sparse import SparseParameters, SparseRecord, physical_rerecord_sparse
from .sparse_replay import derivative_record_sparse


@dataclass(frozen=True)
class ChartMargins:
    """Diagnostic distances in their own units; NOT a certified parameter radius."""
    min_event_separation: float
    min_endpoint_separation: float
    min_history_arrival_separation: float
    min_spike_velocity: float
    event_count: int
    spike_count: int
    token: str
    chart_valid: bool
    warnings: tuple[str, ...]


def chart_margins(p: SparseParameters, rec: SparseRecord) -> ChartMargins:
    if rec.topology_id != p.topology_id:
        raise ValueError('topology mismatch')
    time = sorted(float(ev.t) for ev in rec.events)
    gap = min(np.diff(time), default=math.inf) if len(time)>1 else math.inf
    endpoint_gap = min([min(abs(t), abs(rec.horizon-t)) for t in time], default=math.inf)
    history_gap = math.inf
    for eid in range(p.e):
        source = int(p.source[eid])
        for emitted in rec.history[source]:
            history_gap = min(history_gap, abs(float(emitted) + float(p.delay[eid])))
    speed = min((float(ev.velocity) for ev in rec.spikes),default=math.inf)
    return ChartMargins(float(gap),float(endpoint_gap),float(history_gap),float(speed),
                        len(rec.events),len(rec.spikes),rec.token,rec.chart_valid,rec.warnings)


@dataclass(frozen=True)
class PerturbationCheck:
    delta: float
    status: str
    token_matches: bool
    chart_valid: bool
    spike_count: int
    reason: str
    min_event_separation: float


def _modified(p: SparseParameters, initial: np.ndarray, kind: str, index: int, delta: float):
    if kind == 'weight':
        values=p.weight.copy(); values[index]+=delta
        return p.with_weights(values),initial
    if kind == 'delay':
        values=p.delay.copy(); values[index]+=delta
        return p.with_delays(values),initial
    if kind == 'phase':
        values=np.array(initial,copy=True);values[index]+=delta
        return p,values
    raise ValueError('kind must be weight, delay, phase')


def _check_inputs(p,rec,kind,index):
    if kind not in ('weight','delay','phase'):
        raise ValueError('kind must be weight, delay, phase')
    dim=p.n if kind=='phase' else p.e
    if not isinstance(index,(int,np.integer)) or index<0 or index>=dim:
        raise IndexError('invalid parameter index')
    if rec.topology_id != p.topology_id:
        raise ValueError('topology mismatch')


def perturbation_check(p: SparseParameters, rec: SparseRecord, kind:str, index:int, delta:float):
    """Physically rerecord, then compare the *complete* token and regularity."""
    _check_inputs(p,rec,kind,index)
    if not math.isfinite(float(delta)):
        raise ValueError('perturbation must be finite')
    try:
        proposal, phases=_modified(p,rec.initial_theta,kind,index,float(delta))
        new=physical_rerecord_sparse(proposal,horizon=rec.horizon,
                                    initial_theta=phases,history=rec.history)
    except (ValueError,RuntimeError,FloatingPointError,OverflowError) as exc:
        return PerturbationCheck(float(delta),'INVALID_PARAMETER',False,False,0,
                                 f'{type(exc).__name__}: {exc}',math.nan)
    same=(new.token==rec.token)
    valid=bool(new.chart_valid)
    status=('SAME_CHART' if same and valid and rec.chart_valid else
            'INVALID_CHART' if not valid or not rec.chart_valid else 'CHART_CHANGED')
    reason='; '.join(new.warnings) if new.warnings else ('event itinerary changed' if not same else '')
    return PerturbationCheck(float(delta),status,same,valid,len(new.spikes),reason,
                             chart_margins(proposal,new).min_event_separation)


@dataclass(frozen=True)
class GradientProbe:
    kind:str
    index:int
    step:float
    status:str
    token:str
    tested_offsets:tuple[float,...]
    reference_max_error:float | None
    ad_values:tuple[float,...] | None
    fd_values:tuple[float,...] | None
    max_absolute_error:float | None
    max_relative_error:float | None
    checks:tuple[PerturbationCheck,...]
    notes:str


def five_point_probe(p: SparseParameters,rec:SparseRecord,kind:str,index:int,
                     *,step:float=1e-4, absolute_tolerance:float=1e-5,
                     relative_tolerance:float=1e-4):
    """Check AD via physical 5-point central FD on +/-h and +/-2h.

    Never evaluate a cross-chart difference as an estimate of a same-chart
    derivative. Error checks are engineering thresholds, not scientific criteria.
    """
    _check_inputs(p,rec,kind,index)
    if not math.isfinite(step) or step<=0:
        raise ValueError('positive finite step required')
    center=physical_rerecord_sparse(p,horizon=rec.horizon,
                                   initial_theta=rec.initial_theta,history=rec.history)
    if not rec.chart_valid or not center.chart_valid or center.token!=rec.token:
        return GradientProbe(kind,index,step,'INVALID_CENTER',rec.token,(),None,None,None,
                             None,None,(),'baseline physical event chart invalid/stale')
    if len(rec.spikes)==0:
        return GradientProbe(kind,index,step,'NO_SPIKES',rec.token,(),None,None,None,
                             None,None,(),'no spike times to differentiate')
    offsets=(-2*step,-step,step,2*step)
    checks=tuple(perturbation_check(p,rec,kind,index,x) for x in offsets)
    if any(c.status!='SAME_CHART' for c in checks):
        return GradientProbe(kind,index,step,'CHART_EXIT',rec.token,offsets,None,None,None,
                             None,None,checks,'at least one FD stencil point is on a different or invalid chart')
    outputs=[]
    for delta in offsets:
        proposal,phases=_modified(p,rec.initial_theta,kind,index,delta)
        new=physical_rerecord_sparse(proposal,horizon=rec.horizon,
                                     initial_theta=phases,history=rec.history)
        outputs.append(new.spike_times())
    fm2,fm1,fp1,fp2=outputs
    fd=(fm2-8*fm1+8*fp1-fp2)/(12*step)
    try:
        dr=derivative_record_sparse(p,rec)
        jac={'weight':dr.d_times_d_edge_weights,'delay':dr.d_times_d_edge_delays,
             'phase':dr.d_times_d_initial_theta}[kind]
        ad=np.asarray(jac[:,index],dtype=float)
        discrepancy=np.abs(ad-fd)
        max_abs=float(discrepancy.max())
        max_rel=float((discrepancy/np.maximum(np.maximum(np.abs(ad),np.abs(fd)),1e-12)).max())
        within=np.all(discrepancy <= absolute_tolerance + relative_tolerance*np.maximum(np.abs(ad),np.abs(fd)))
        status='PASS' if within else 'DERIVATIVE_MISMATCH'
        return GradientProbe(kind,index,step,status,rec.token,offsets,dr.max_reference_disagreement,
                             tuple(ad.tolist()),tuple(fd.tolist()),max_abs,max_rel,checks,
                             'same event itinerary at all 4 stencil points; per-component mixed abs/rel criterion')
    except (ValueError,RuntimeError,FloatingPointError) as exc:
        return GradientProbe(kind,index,step,'REPLAY_ERROR',rec.token,offsets,None,None,None,
                             None,None,checks,f'{type(exc).__name__}: {exc}')
