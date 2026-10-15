"""Local fixed-chart JAX replay for the NONCANONICAL Lighthouse engineering scratchpad.

All AD must be guarded by physical rerecording on *the exact history and topology*.
"""
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
import jax
jax.config.update('jax_enable_x64', True)
import jax.numpy as jnp
from .reference import Record, Parameters, physical_rerecord


@lru_cache(None)
def _quadrature(n=64):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(x+1), 0.5*w


def _rate(psi, r, h):
    gap = psi-h
    safe = jnp.maximum(gap, 1e-50)
    return jnp.where(gap > 0, jnp.exp(-r/safe**2), 0.)


def _flow(theta, a, q, dt, W, alpha, r, h):
    """Exact edge alpha flow, 64-point Gauss-Legendre phase quadrature."""
    nodes, weights = _quadrature()
    if alpha >= 100.:
        u=nodes
        nodes,weights=nodes*nodes,2*u*weights
    x, w = jnp.asarray(nodes), jnp.asarray(weights)
    s = dt*x
    decay = jnp.exp(-alpha*s)[:, None, None]
    at = decay*(a[None, :, :]+s[:, None, None]*q[None, :, :])
    psi = jnp.einsum('ij,kij->ki', W, at)
    integral = dt*jnp.sum(w[:, None]*_rate(psi, r, h), axis=0)
    end_decay = jnp.exp(-alpha*dt)
    return theta+integral, end_decay*(a+dt*q), end_decay*q


def _velocity_at(i, dt, a, q, W, alpha, r, h):
    psi = jnp.dot(W[i], jnp.exp(-alpha*dt)*(a[i]+dt*q[i]))
    return _rate(psi, r, h)


def _root_duration(i, target, guess, theta, a, q, W, alpha, r, h):
    """Chart-local Newton; physical rerecord validates its resulting times."""
    def step(_, d):
        future, _, _ = _flow(theta, a, q, d, W, alpha, r, h)
        error = future[i]-target
        v = _velocity_at(i, d, a, q, W, alpha, r, h)
        return d-error/jnp.maximum(v, 1e-12)
    return jax.lax.fori_loop(0, 12, step, jnp.asarray(guess))


def _initial_edge_filters(delays, record: Record, alpha):
    """Reconstruct pre-t0 arrived packets differentiably on fixed history partition."""
    a = jnp.zeros_like(delays)
    q = jnp.zeros_like(delays)
    # A strictly negative arrival has contributed for dt=-arrival by t=0.
    for target, source, ordinal in record.initial_arrived:
        emission = record.history[source][ordinal+len(record.history[source])-1]
        age = -(emission+delays[target, source])
        decay = jnp.exp(-alpha*age)
        a = a.at[target, source].add(alpha**2*age*decay)
        q = q.at[target, source].add(alpha**2*decay)
    return a, q


def replay_fixed_chart(W, delays, initial_theta, record: Record, *, alpha=1., r=1., h=-1.):
    """Fixed recorded ordering and history partition; returns ordered spike timestamps.

    Never call without `physical_rerecord` for each new proposed parameter point.
    """
    if not record.chart_valid:
        raise ValueError('Invalid reference chart')
    # Edges are determined by the reference topology, NOT by W != 0.
    # A structurally present zero-weight edge is retained in all event/arrival
    # records and is a legal differentiation coordinate. Absent edges remain zero.
    W, delays = jnp.asarray(W), jnp.asarray(delays)
    W = W * jnp.asarray(record.edge_mask, dtype=W.dtype)
    theta = jnp.asarray(initial_theta)
    a, q = _initial_edge_filters(delays, record, alpha)
    t = jnp.asarray(0.)
    recorded_prev = 0.
    emitted = {
        (source, idx-len(times)+1): jnp.asarray(emit)
        for source, times in enumerate(record.history)
        for idx, emit in enumerate(times)
    }
    for event in record.events:
        if event.kind == 'spike':
            guess = event.t-recorded_prev
            target = 2*np.pi*event.ordinal
            dt = _root_duration(event.neuron, target, guess, theta, a, q, W, alpha, r, h)
            theta, a, q = _flow(theta, a, q, dt, W, alpha, r, h)
            t += dt
            theta = theta.at[event.neuron].set(target)
            emitted[(event.neuron, event.ordinal)] = t
        elif event.kind == 'arrival':
            emission = emitted.get((event.source, event.ordinal))
            if emission is None:
                raise ValueError('Arrival has no historical/simulated emission')
            arrival = emission+delays[event.neuron, event.source]
            dt = arrival-t
            theta, a, q = _flow(theta, a, q, dt, W, alpha, r, h)
            t = arrival
            q = q.at[event.neuron, event.source].add(alpha**2)
        else:
            raise ValueError(f'Unknown event kind: {event.kind}')
        recorded_prev = event.t
    if not record.spikes:
        return jnp.zeros((0,), dtype=W.dtype)
    return jnp.stack([emitted[(event.neuron, event.ordinal)] for event in record.spikes])


@dataclass(frozen=True)
class DerivativeRecord:
    token: str
    spike_times: np.ndarray
    d_times_d_weights: np.ndarray
    d_times_d_delays: np.ndarray
    d_times_d_initial_theta: np.ndarray
    max_reference_disagreement: float


def derivative_record(p: Parameters, record: Record, *, tol=1e-7):
    """Physical guard + replay residual check before chart-local JAX Jacobians."""
    physical = physical_rerecord(p, horizon=record.horizon,
                                initial_theta=record.initial_theta,
                                history=record.history)
    if (not physical.chart_valid or not record.chart_valid or
        record.physical_certification != 'NUMENG_PULSE_AWARE_REFERENCE_V1' or
        physical.physical_certification != 'NUMENG_PULSE_AWARE_REFERENCE_V1' or
        physical.token != record.token or len(physical.events) != len(record.events) or
        any(abs(a.t-b.t)>1e-8 for a,b in zip(physical.events,record.events))):
        raise ValueError('Stale/invalid chart: incomplete or uncertified physical tape; rerecord required')

    def combined(w, delays, theta):
        return replay_fixed_chart(w, delays, theta, record,
                                  alpha=p.alpha, r=p.r, h=p.h)

    times = np.asarray(combined(p.W, p.delays, record.initial_theta))
    target = physical.spike_times()
    discrepancy = float(np.max(np.abs(times-target))) if len(times) else 0.
    if not np.isfinite(discrepancy) or discrepancy > tol:
        raise ValueError(f'Replay disagrees with physical reference by {discrepancy}')
    # One differentiated trace avoids three independently constructed large
    # local Newton/replay graphs in a multi-neuron history fixture.
    jw, jd, jt = jax.jacrev(combined, argnums=(0, 1, 2))(
        p.W, p.delays, record.initial_theta)
    out = DerivativeRecord(record.token, times, np.asarray(jw), np.asarray(jd),
                           np.asarray(jt), discrepancy)
    if not all(np.isfinite(x).all() for x in (
        out.d_times_d_weights, out.d_times_d_delays,
        out.d_times_d_initial_theta,
    )):
        raise ValueError('Nonfinite derivative on reference chart')
    return out
