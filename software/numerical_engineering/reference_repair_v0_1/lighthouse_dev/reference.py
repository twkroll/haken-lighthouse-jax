"""Noncanonical reference numerical engine for RB-004 fixed-delay Lighthouse model.

Technical verification only; not an RB-006/RB-009 contract rerun.

Edge arrivals are represented by exact alpha states. A finite user-supplied
prespike history seeds arrived pulses at t=0 and queues in-flight packets.
"""
from dataclasses import dataclass
from math import pi
import hashlib
import heapq
import json
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


@dataclass(frozen=True)
class Parameters:
    W: np.ndarray  # W[target, source], magnitude and sign independent of topology
    delays: np.ndarray  # delays[target, source]
    alpha: float = 1.
    r: float = 1.
    h: float = -1.
    adjacency: np.ndarray | None = None  # explicit structural graph, shape N x N; legacy default W != 0

    def __post_init__(self):
        w = np.array(self.W, dtype=float, copy=True)
        d = np.array(self.delays, dtype=float, copy=True)
        if w.ndim != 2 or w.shape[0] != w.shape[1] or d.shape != w.shape:
            raise ValueError('Expected square W and delays')
        if not np.isfinite(w).all() or not np.isfinite(d).all() or (d < 0).any():
            raise ValueError('Nonfinite matrix or negative delay')
        if not np.isfinite([self.alpha, self.r, self.h]).all() or self.alpha <= 0 or self.r <= 0:
            raise ValueError('Invalid alpha, r or h')
        if self.adjacency is None:
            mask = w != 0   # backward-compatible inference only at creation time
        else:
            raw_mask = np.asarray(self.adjacency)
            if raw_mask.shape != w.shape or raw_mask.dtype.kind != 'b':
                raise ValueError('adjacency must be a square Boolean mask matching W')
            mask = np.array(raw_mask, dtype=bool, copy=True)
            if np.any(w[~mask] != 0):
                raise ValueError('weights on structurally absent edges must be exactly zero')
        w.flags.writeable = False
        d.flags.writeable = False
        mask.flags.writeable = False
        object.__setattr__(self, 'W', w)
        object.__setattr__(self, 'delays', d)
        object.__setattr__(self, 'adjacency', mask)

    @property
    def n(self):
        return len(self.W)

    @property
    def edge_count(self):
        return int(np.count_nonzero(self.adjacency))

    def with_weights(self, new_weights):
        """A new parameter value on the *same physical graph*, including zero crossings."""
        return Parameters(new_weights, self.delays, alpha=self.alpha, r=self.r,
                          h=self.h, adjacency=self.adjacency)



def normalize_history(history, n):
    """Input: iterable of per-neuron strictly increasing, strictly pre-t=0 spike times.

    The k past spikes of a neuron are labelled -k+1,...,0, while new
    simulation spikes start at 1. Prespike history is a DDE initial condition,
    not a claim that those spikes were simulated by the model before t=0.
    """
    if history is None:
        return tuple(() for _ in range(n))
    if len(history) != n:
        raise ValueError('History length must equal neuron count')
    output = []
    for times in history:
        arr = np.asarray(times, dtype=float)
        if arr.ndim != 1 or not np.isfinite(arr).all():
            raise ValueError('History must be 1D finite time arrays')
        if (arr >= 0).any() or (np.diff(arr) <= 0).any():
            raise ValueError('History must be strictly increasing and earlier than t=0')
        output.append(tuple(float(t) for t in arr))
    return tuple(output)


def alpha_kernel(alpha, t):
    return float(alpha**2 * t * np.exp(-alpha*t)) if t >= 0 else 0.


def response(x, r, h):
    gap = np.asarray(x, dtype=float) - h
    safe = np.maximum(gap, 1e-150)
    val = np.where(gap > 0, np.exp(-r/safe**2), 0.)
    return float(val) if val.ndim == 0 else val


def propagate_alpha(a, q, dt, alpha):
    if dt < 0:
        raise ValueError('negative dt')
    e = np.exp(-alpha*dt)
    return e*(a+dt*q), e*q


@dataclass(frozen=True)
class Event:
    t: float
    kind: str
    neuron: int  # target for arrivals; firing neuron for spikes
    source: int = -1
    ordinal: int = -1
    velocity: float | None = None

    def signature(self):
        return (self.kind, self.neuron, self.source, self.ordinal)


@dataclass(frozen=True)
class Record:
    events: tuple[Event, ...]
    spikes: tuple[Event, ...]
    chart_valid: bool
    warnings: tuple[str, ...]
    final_theta: np.ndarray
    horizon: float
    initial_theta: np.ndarray
    history: tuple[tuple[float, ...], ...]
    initial_arrived: tuple[tuple[int, int, int], ...]  # (target, source, ordinal)
    edge_mask: tuple[tuple[bool, ...], ...]
    initial_a: np.ndarray
    initial_q: np.ndarray
    physical_certification: str = 'UNVERIFIED'

    @property
    def token(self):
        """Topology/itinerary token; its reuse also requires a physical rerecord."""
        payload = dict(
            events=[ev.signature() for ev in self.events],
            history=self.history,
            initial_arrived=self.initial_arrived,
            edge_mask=self.edge_mask,
        )
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:20]

    def spike_times(self, neuron=None):
        return np.asarray([e.t for e in self.spikes if neuron is None or e.neuron == neuron])


def _integrated_rate(i, dt, a, q, p):
    if dt <= 0:
        return 0.
    ai, qi, wi = a[i], q[i], p.W[i]
    wa=float(np.dot(wi,ai)); wq=float(np.dot(wi,qi))
    from .physical_first_hit_repair import pulse_aware_integral
    return pulse_aware_integral(dt,wa,wq,p.alpha,p.r,p.h)


def _history_seed(p, history, arrival_epsilon=1e-13):
    """Pre-t0 filtering and future arrival heap from frozen spike history."""
    a = np.zeros_like(p.W)
    q = np.zeros_like(p.W)
    pending = []
    arrived = []
    for source, times in enumerate(history):
        for idx, emit in enumerate(times):
            ordinal = idx - len(times) + 1
            for target in range(p.n):
                if not p.adjacency[target, source]:
                    continue
                arrival = emit + float(p.delays[target, source])
                if arrival < -arrival_epsilon:
                    age = -arrival
                    decay = np.exp(-p.alpha * age)
                    q[target, source] += p.alpha**2 * decay
                    a[target, source] += p.alpha**2 * age * decay
                    arrived.append((target, source, ordinal))
                else:
                    # arrival at t=0 is processed as an actual queue event
                    heapq.heappush(pending, (max(0., arrival), target, source, ordinal))
    return a, q, pending, tuple(sorted(arrived))


def physical_rerecord(p: Parameters, *, horizon: float, initial_theta=None,
                      history=None, max_events=2000, collision_tol=1e-8,
                      transversality_tol=1e-10) -> Record:
    """Physical first-hit rerecord, with finite per-neuron pre-t0 spike history.

    Collision warnings invalidate the *differentiable chart*, not the physical
    packet accumulation. Arrival ties still have a deterministic bookkeeping
    order; derivatives across them are not claimed.
    """
    if not np.isfinite(horizon) or horizon <= 0:
        raise ValueError('bad horizon')
    hist = normalize_history(history, p.n)
    theta0 = np.zeros(p.n) if initial_theta is None else np.array(initial_theta, dtype=float, copy=True)
    if theta0.shape != (p.n,) or not np.isfinite(theta0).all() or (theta0 < 0).any() or (theta0 >= 2*pi).any():
        raise ValueError('initial phase expected in [0,2pi)')
    theta = theta0.copy()
    a, q, queue, initial_arrived = _history_seed(p, hist)
    a0, q0 = a.copy(), q.copy()
    counts = np.zeros(p.n, dtype=int)
    t = 0.
    spikes, events, warnings = [], [], []

    from .physical_first_hit_repair import PhysicalFirstHitUncertified
    try:
        for _ in range(max_events):
            if t >= horizon - 1e-12:
                break
            next_arrival = queue[0][0] if queue else float('inf')
            endpoint = min(horizon, next_arrival)
            dt = endpoint - t
            if dt < -1e-10:
                raise RuntimeError('Arrival in past')
            dt = max(0., dt)
            candidates = []
            for i in range(p.n):
                target_phase = 2*pi*(counts[i]+1)
                end_gap = theta[i] + _integrated_rate(i, dt, a, q, p) - target_phase
                if end_gap >= -1e-12:
                    def gap_at(s, i=i, target_phase=target_phase):
                        return theta[i] + _integrated_rate(i, s, a, q, p) - target_phase
                    if gap_at(0) < 0 and end_gap > 1e-12:
                        root = brentq(gap_at, 0., dt, xtol=1e-12, rtol=9e-16)
                    else:
                        root = dt
                    candidates.append((t+root, i))
            earliest = min((ts for ts, i in candidates), default=float('inf'))
            event_t = min(endpoint, earliest)
            near_spikes = [i for ts, i in candidates if abs(ts-event_t) <= collision_tol]
            near_arrivals = [item for item in queue if abs(item[0]-event_t) <= collision_tol]
            if len(near_spikes) + len(near_arrivals) > 1:
                warnings.append(f'EVENT_CHART_COLLISION_NEAR:t={event_t:.12g}')
            if near_arrivals and abs(event_t) <= collision_tol:
                warnings.append('INITIAL_ARRIVAL_CHART_BOUNDARY')
            if (near_spikes or near_arrivals) and abs(event_t-horizon) <= collision_tol:
                warnings.append('HORIZON_EVENT_CHART_BOUNDARY')
            elapsed = max(0., event_t-t)
            theta += np.asarray([_integrated_rate(i, elapsed, a, q, p) for i in range(p.n)])
            a, q = propagate_alpha(a, q, elapsed, p.alpha)
            t = event_t
            due_spikes = [i for ts, i in candidates if abs(ts-t) <= 2e-11]
            for i in sorted(due_spikes):
                counts[i] += 1
                theta[i] = 2*pi*counts[i]
                velocity = response(np.sum(p.W[i]*a[i]), p.r, p.h)
                if velocity <= transversality_tol:
                    warnings.append(f'NONTRANSVERSAL:{i}:{counts[i]}')
                event = Event(t, 'spike', i, -1, int(counts[i]), velocity)
                events.append(event)
                spikes.append(event)
                for target in range(p.n):
                    if p.adjacency[target, i]:
                        arr_t = t+float(p.delays[target, i])
                        heapq.heappush(queue, (arr_t, target, i, int(counts[i])))
                        if arr_t == t:
                            warnings.append(f'ZERO_DELAY_EVENT_CHART_BOUNDARY:t={t:.12g}')
            while queue and abs(queue[0][0]-t) <= 2e-11:
                _, target, source, ordinal = heapq.heappop(queue)
                q[target, source] += p.alpha**2
                events.append(Event(t, 'arrival', target, source, ordinal))
        else:
            warnings.append('EVENT_BUDGET_EXCEEDED')
    except (PhysicalFirstHitUncertified, ValueError, RuntimeError, FloatingPointError, OverflowError) as exc:
        warnings.append(f'PHYSICAL_FIRST_HIT_UNCERTIFIED:{type(exc).__name__}:{exc}')
    mask = tuple(tuple(bool(v) for v in row) for row in p.adjacency)
    return Record(tuple(events), tuple(spikes), not bool(warnings), tuple(warnings),
                  theta, horizon, theta0, hist, initial_arrived, mask, a0, q0,
                  'NUMENG_PULSE_AWARE_REFERENCE_V1' if not warnings else 'INVALID')


def validate_same_chart(p: Parameters, record: Record):
    rerecord = physical_rerecord(p, horizon=record.horizon,
                                initial_theta=record.initial_theta, history=record.history)
    return record.chart_valid and rerecord.chart_valid and rerecord.token == record.token, rerecord


@dataclass(frozen=True)
class TrajectorySamples:
    """Sampled physical states; events remain authoritative over a time grid."""
    times: np.ndarray
    theta: np.ndarray
    psi: np.ndarray
    a: np.ndarray
    q: np.ndarray


def sample_trajectory(p: Parameters, record: Record, times, *, verify=True):
    """Replay a physical Record on requested observation times.

    Exact alpha propagation and high-accuracy continuous phase quadrature.
    This is an observation utility, not a time-stepped event simulator.
    Samples exactly at a packet arrival use the post-arrival q value.
    """
    samples = np.asarray(times, dtype=float)
    if samples.ndim != 1 or not np.isfinite(samples).all() or np.any(np.diff(samples) < 0):
        raise ValueError('Observation times must be finite and nondecreasing')
    if np.any(samples < 0) or np.any(samples > record.horizon):
        raise ValueError('Observation outside recorded horizon')
    if verify:
        fresh = physical_rerecord(p, horizon=record.horizon,
                                  initial_theta=record.initial_theta,
                                  history=record.history)
        if (fresh.token != record.token or len(fresh.events) != len(record.events)
            or any(abs(x.t - y.t) > 1e-9 for x, y in zip(fresh.events, record.events))):
            raise ValueError('Recorded physical events stale for supplied parameters')
    a, q = record.initial_a.copy(), record.initial_q.copy()
    theta = record.initial_theta.copy()
    t, k = 0., 0
    out_theta, out_psi, out_a, out_q = [], [], [], []

    def advance(dt):
        nonlocal theta, a, q
        theta = theta+np.asarray([_integrated_rate(i, dt, a, q, p) for i in range(p.n)])
        a, q = propagate_alpha(a, q, dt, p.alpha)

    for sample in samples:
        while k < len(record.events) and record.events[k].t <= sample:
            ev = record.events[k]
            advance(max(0., ev.t-t))
            t = ev.t
            if ev.kind == 'spike':
                theta[ev.neuron] = 2*pi*ev.ordinal
            elif ev.kind == 'arrival':
                q[ev.neuron, ev.source] += p.alpha**2
            else:
                raise ValueError('Unknown event')
            k += 1
        advance(max(0., sample-t))
        t = float(sample)
        out_theta.append(theta.copy())
        out_psi.append(np.sum(p.W*a, axis=1).copy())
        out_a.append(a.copy())
        out_q.append(q.copy())

    return TrajectorySamples(samples, np.asarray(out_theta).reshape((-1,p.n)),
                             np.asarray(out_psi).reshape((-1,p.n)),
                             np.asarray(out_a).reshape((-1,p.n,p.n)),
                             np.asarray(out_q).reshape((-1,p.n,p.n)))
