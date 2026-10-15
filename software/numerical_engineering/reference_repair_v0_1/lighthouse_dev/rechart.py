"""v0.6 LOCAL ENGINEERING: collision audit and chart-aware physical re-recording.

The canonical Lighthouse model is NOT extended. No confirmatory datasets or AI
learning tasks occur here. Physical simulation remains authoritative; JAX only
replays a physically verified regular itinerary.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import inf, isfinite
from typing import Optional

import numpy as np

from .sparse import SparseParameters, SparseRecord, physical_rerecord_sparse


@dataclass(frozen=True)
class EventPair:
    """Two consecutive events in the physical tape (times in model units)."""
    left_index: int
    right_index: int
    kind: str
    dt: float
    left_signature: tuple
    right_signature: tuple


@dataclass(frozen=True)
class CollisionAudit:
    token: str
    chart_valid: bool
    closest_pair: Optional[EventPair]
    closest_by_type: dict[str, Optional[EventPair]]
    pairs_below_threshold: tuple[EventPair, ...]
    min_transversality: float
    min_initial_arrival_distance: float
    min_horizon_distance: float
    warnings: tuple[str, ...]


def collision_audit(p: SparseParameters, rec: SparseRecord, *, threshold: float = 1e-8):
    """Audit adjacency of recorded events; never certify an open chart radius.

    For sorted real event times, the closest pair must be consecutive. This
    function checks all consecutive pairs and distinguishes the pair classes.
    A single scalar threshold in *time units* is just a diagnostic setting;
    only the authoritative physical rerecord determines chart validity.
    """
    if rec.topology_id != p.topology_id:
        raise ValueError('topology does not match record')
    if not isfinite(threshold) or threshold < 0:
        raise ValueError('threshold must be nonnegative finite')
    events = rec.events
    pairs = []
    for k in range(len(events) - 1):
        left, right = events[k], events[k+1]
        gap = float(right.t - left.t)
        if gap < -1e-10:
            raise ValueError('recorded events out of chronological order')
        kind = ('SPIKE_SPIKE' if left.kind == right.kind == 'spike' else
                'ARRIVAL_ARRIVAL' if left.kind == right.kind == 'arrival' else
                'SPIKE_ARRIVAL')
        pairs.append(EventPair(k, k+1, kind, gap,
                               left.signature(), right.signature()))
    close = tuple(pair for pair in pairs if pair.dt <= threshold)
    best_by = {name: min((pair for pair in pairs if pair.kind == name),
                         key=lambda x:x.dt, default=None)
               for name in ('SPIKE_SPIKE','SPIKE_ARRIVAL','ARRIVAL_ARRIVAL')}
    best = min(pairs, key=lambda x:x.dt, default=None)
    history_d = inf
    for eid in range(p.e):
        for em in rec.history[int(p.source[eid])]:
            history_d = min(history_d, abs(float(em) + float(p.delay[eid])))
    return CollisionAudit(
        rec.token, rec.chart_valid, best, best_by, close,
        min((float(event.velocity) for event in rec.spikes), default=inf),
        history_d,
        min((min(abs(ev.t), abs(rec.horizon-ev.t)) for ev in events), default=inf),
        rec.warnings,
    )


@dataclass(frozen=True)
class ProposalResult:
    index: int
    status: str
    token: Optional[str]
    physical_spike_times: tuple[float, ...]
    replay_spike_times: Optional[tuple[float, ...]]
    max_replay_error: Optional[float]
    warnings: tuple[str, ...]
    detail: str


@dataclass(frozen=True)
class BatchRerecordResult:
    """Per-proposal result; different buckets have different event shapes."""
    entries: tuple[ProposalResult, ...]
    buckets: tuple[tuple[str, tuple[int,...]], ...]
    physical_evaluations: int
    vmap_calls: int

    @property
    def counts(self):
        return {s: sum(r.status == s for r in self.entries)
                for s in sorted({r.status for r in self.entries})}


def rechart_batch(p: SparseParameters, base: SparseRecord, weight_batch,
                  *, delay_batch=None, phase_batch=None, replay: bool = True,
                  replay_tolerance: float = 1e-7, collision_tol: float = 1e-8):
    """Physically rerecord EVERY candidate, then group by full itinerary token.

    SAME_CHART: physical record is regular and matches baseline event itinerary;
    RECHARTED: physical record is regular but needs a new event itinerary;
    INVALID_CHART: physically invalid (collision, horizon, nontransversality);
    INVALID_PARAMETER: invalid weights, delays or phases;
    REPLAY_MISMATCH: a physically valid record and fixed-chart JAX disagree.

    No success is claimed for an unvalidated fixed-chart replay. Each bucket's
    replay receives the *representative physically recorded* event structure;
    JAX never sorts or invents event order. This function DOES NOT cache or
    reuse derivatives across parameter changes.
    """
    if not isfinite(replay_tolerance) or replay_tolerance <= 0:
        raise ValueError('replay_tolerance must be strictly positive finite')
    if not isfinite(collision_tol) or collision_tol <= 0:
        raise ValueError('collision_tol must be strictly positive finite')
    weights = np.asarray(weight_batch, dtype=float)
    if weights.ndim != 2 or weights.shape[1] != p.e:
        raise ValueError('weights must have shape [batch, edges]')
    b = len(weights)
    ds = (np.broadcast_to(p.delay, (b,p.e)) if delay_batch is None else
          np.asarray(delay_batch,dtype=float))
    th = (np.broadcast_to(base.initial_theta, (b,p.n)) if phase_batch is None else
          np.asarray(phase_batch,dtype=float))
    if ds.shape != (b,p.e) or th.shape != (b,p.n):
        raise ValueError('delay and phase batch sizes must match weights')
    if base.topology_id != p.topology_id or not base.chart_valid:
        raise ValueError('base chart must be regular and match topology')
    check = physical_rerecord_sparse(p, horizon=base.horizon,
                                    initial_theta=base.initial_theta,
                                    history=base.history, collision_tol=collision_tol)
    # A token encodes the itinerary, not the physical parameter point. A
    # re-record may keep the same event order while moving the event times.
    # Distinguish this kind of stale reference from a chart-token mismatch.
    same_times = (len(check.events) == len(base.events) and
                  all(abs(a.t-b.t) <= 1e-9
                      for a,b in zip(check.events,base.events)))
    same_initial_alpha = (np.allclose(check.initial_a,base.initial_a,rtol=0,atol=1e-9)
                          and np.allclose(check.initial_q,base.initial_q,rtol=0,atol=1e-9))
    if (not check.chart_valid or check.token != base.token or
            not same_times or not same_initial_alpha):
        raise ValueError('baseline record is stale or invalid')
    evaluation_count = 1

    entries: list[Optional[ProposalResult]] = [None] * b
    fresh_records: dict[int,SparseRecord] = {}
    grouped: dict[str,list[int]] = {}
    for i in range(b):
        try:
            cp = SparseParameters(p.n,p.target,p.source,weights[i],ds[i],
                                  p.alpha,p.r,p.h)
            rec = physical_rerecord_sparse(cp, horizon=base.horizon,
                                           initial_theta=th[i], history=base.history,
                                           collision_tol=collision_tol)
            evaluation_count += 1
        except (ValueError, RuntimeError, OverflowError, FloatingPointError) as exc:
            entries[i] = ProposalResult(i,'INVALID_PARAMETER',None,(),None,None,(),
                                        f'{type(exc).__name__}: {exc}')
            continue
        if not rec.chart_valid:
            entries[i] = ProposalResult(i,'INVALID_CHART',rec.token,
                                        tuple(rec.spike_times().tolist()),None,None,
                                        rec.warnings, 'physical record rejected')
            continue
        fresh_records[i] = rec
        grouped.setdefault(rec.token, []).append(i)
        state = 'SAME_CHART' if rec.token == base.token else 'RECHARTED'
        entries[i] = ProposalResult(i,state,rec.token,
                                    tuple(rec.spike_times().tolist()),None,None,(),
                                    'physical itinerary validated')

    buckets = tuple((token, tuple(indices)) for token,indices in grouped.items())
    calls = 0
    if replay and fresh_records:
        # Import JAX only if fixed-chart evaluation was requested.
        import jax
        from .sparse_replay import prepare_replay, replay_sparse_fixed_chart
        for token, indices in buckets:
            representative = fresh_records[indices[0]]
            pp = SparseParameters(p.n,p.target,p.source,weights[indices[0]],
                                  ds[indices[0]],p.alpha,p.r,p.h)
            tape = prepare_replay(representative,pp)
            def f(w,d,theta):
                return replay_sparse_fixed_chart(w,d,theta,representative,pp,prepared=tape)
            calls += 1
            predicted = np.asarray(jax.vmap(f)(weights[list(indices)],
                                                ds[list(indices)],th[list(indices)]))
            if predicted.ndim != 2:
                raise RuntimeError('batched fixed-chart replay returned invalid shape')
            for j,i in enumerate(indices):
                current = entries[i]
                phys = np.asarray(current.physical_spike_times)
                pred = np.asarray(predicted[j])
                discrepancy = (float(np.max(np.abs(pred-phys))) if len(phys)
                               else 0.)
                if pred.shape != phys.shape or not np.isfinite(pred).all() or (
                        not np.isfinite(discrepancy) or discrepancy > replay_tolerance):
                    entries[i] = ProposalResult(i,'REPLAY_MISMATCH',current.token,
                                               current.physical_spike_times,None,
                                               discrepancy,current.warnings,
                                               'fixed-chart JAX disagrees with physical rerecord')
                else:
                    entries[i] = ProposalResult(i,current.status,current.token,
                                               current.physical_spike_times,
                                               tuple(pred.tolist()),discrepancy,(),
                                               'physically certified + chart-local replay')
    return BatchRerecordResult(tuple(entries),buckets,evaluation_count,calls)
