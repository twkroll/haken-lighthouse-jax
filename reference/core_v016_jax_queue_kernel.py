"""Fixed-capacity JAX packet queue kernel for CORE v0.16.

This module is a static-shape realization of the three-cell adaptive Lighthouse
reference used in CORE v0.14--v0.15.  It keeps event ordering explicit while
making all state arrays compatible with ``jax.jit`` and ``lax.while_loop``.

The queue is intentionally overprovisioned (12 slots; the certified N=3 ring
uses at most six active packets in the v0.14/v0.15 benchmark region).
"""
from __future__ import annotations

from typing import NamedTuple
import math
import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.legendre import leggauss

jax.config.update("jax_enable_x64", True)

PI = math.pi
TWO_PI = 2.0 * PI
ALPHA = 0.5
N = 3
QMAX = 12
P_ADAPT = -3.267985407948901
T_NS = 16.297496058505022
TAU_NS = 7.941411830425917
TAU_FIC = 7.94140373739
A_FIC = 0.0660575
C_NS = 1.0 / TAU_NS
TAU_TARGET = TAU_FIC - 5.0e-5
C0 = 1.0 / TAU_TARGET
KAPPA_ACTIVITY = 2.0e-6
U_S = 0.03**2

_gx, _gw = leggauss(20)
GX = jnp.asarray(_gx)
GW = jnp.asarray(_gw)

KIND_INACTIVE = 0
KIND_SHORT = 1
KIND_ADAPTIVE = 2

class State(NamedTuple):
    t: jax.Array
    psi: jax.Array
    q: jax.Array
    phi: jax.Array
    c: jax.Array
    p: jax.Array
    epsilon: jax.Array
    kappa: jax.Array
    c0: jax.Array
    active: jax.Array
    source: jax.Array
    target: jax.Array
    weight: jax.Array
    rho: jax.Array
    kind: jax.Array
    count: jax.Array
    last_spike: jax.Array
    A_held: jax.Array
    last_cycle_mean: jax.Array
    last_period: jax.Array
    overflow: jax.Array
    max_active: jax.Array
    event_count: jax.Array


def response(x):
    y = x + 1.0
    ys = jnp.maximum(y, 1.0e-15)
    return jnp.where(y > 0.0, jnp.exp(-1.0 / (ys * ys)), 0.0)


def phase_gain_vec(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    psi_s = e[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    return 0.5 * dt * jnp.sum(GW[None, :] * response(psi_s), axis=1)


def activity_gate(u):
    return u / (u + U_S)


def rate(state):
    return state.epsilon / T_NS


def c_equilibrium(state):
    return state.c0 + state.kappa * activity_gate(state.A_held**2)


def adaptive_distance(state, dt):
    lam = rate(state)
    ceq = c_equilibrium(state)
    z = lam * dt
    integ = jnp.where(jnp.abs(lam) > 1.0e-18, -jnp.expm1(-z) / lam, dt)
    return ceq * dt + (state.c - ceq) * integ


def advance_c(state, dt):
    lam = rate(state)
    ceq = c_equilibrium(state)
    return jnp.where(
        jnp.abs(lam) > 1.0e-18,
        ceq + (state.c - ceq) * jnp.exp(-lam * dt),
        state.c,
    )


def _first_inactive(active):
    idx = jnp.arange(QMAX, dtype=jnp.int32)
    return jnp.min(jnp.where(~active, idx, QMAX))


def _insert_packet(state, src, tgt, w, kind):
    slot = _first_inactive(state.active)
    ok = slot < QMAX
    safe = jnp.minimum(slot, QMAX - 1)
    active = state.active.at[safe].set(jnp.where(ok, True, state.active[safe]))
    source = state.source.at[safe].set(jnp.where(ok, src, state.source[safe]))
    target = state.target.at[safe].set(jnp.where(ok, tgt, state.target[safe]))
    weight = state.weight.at[safe].set(jnp.where(ok, w, state.weight[safe]))
    rho = state.rho.at[safe].set(jnp.where(ok, 1.0, state.rho[safe]))
    kinds = state.kind.at[safe].set(jnp.where(ok, kind, state.kind[safe]))
    return state._replace(
        active=active, source=source, target=target, weight=weight, rho=rho,
        kind=kinds, overflow=state.overflow | (~ok),
    )


def _emit_one(state, src):
    q = state.q.at[src].add(ALPHA**2)
    st = state._replace(q=q)
    st = _insert_packet(st, src, (src + 1) % N, st.p, KIND_SHORT)
    st = _insert_packet(st, src, (src + 2) % N, -st.p, KIND_ADAPTIVE)
    return st


def _emit_mask(state, firing_mask):
    def body(i, st):
        return jax.lax.cond(firing_mask[i], lambda x: _emit_one(x, i), lambda x: x, st)
    st = jax.lax.fori_loop(0, N, body, state)
    nact = jnp.sum(st.active.astype(jnp.int32))
    return st._replace(max_active=jnp.maximum(st.max_active, nact))


def make_state(*, p=P_ADAPT, c=C_NS, epsilon=0.0, kappa=0.0, c0=C0):
    zN = jnp.zeros(N, dtype=jnp.float64)
    active = jnp.zeros(QMAX, dtype=bool)
    zi = jnp.zeros(QMAX, dtype=jnp.int32)
    zq = jnp.zeros(QMAX, dtype=jnp.float64)
    st = State(
        t=jnp.array(0.0), psi=zN, q=zN, phi=zN,
        c=jnp.array(c), p=jnp.array(p), epsilon=jnp.array(epsilon),
        kappa=jnp.array(kappa), c0=jnp.array(c0),
        active=active, source=zi, target=zi, weight=zq, rho=zq,
        kind=zi, count=jnp.zeros(N, dtype=jnp.int32),
        last_spike=jnp.zeros(N, dtype=jnp.float64), A_held=jnp.array(0.0),
        last_cycle_mean=jnp.array(jnp.nan), last_period=jnp.array(jnp.nan),
        overflow=jnp.array(False), max_active=jnp.array(0, dtype=jnp.int32),
        event_count=jnp.array(0, dtype=jnp.int32),
    )
    return _emit_mask(st, jnp.ones(N, dtype=bool))


def set_adaptation(state, epsilon, *, kappa=None, c0=None):
    return state._replace(
        epsilon=jnp.asarray(epsilon, dtype=jnp.float64),
        kappa=state.kappa if kappa is None else jnp.asarray(kappa, dtype=jnp.float64),
        c0=state.c0 if c0 is None else jnp.asarray(c0, dtype=jnp.float64),
    )


def set_tau_frozen(state, tau):
    c = 1.0 / jnp.asarray(tau, dtype=jnp.float64)
    return state._replace(c=c, c0=c, epsilon=jnp.array(0.0), kappa=jnp.array(0.0))


def _adaptive_packet_time(state, rho):
    ceq = c_equilibrium(state)
    lam = rate(state)
    t0 = rho / jnp.maximum(state.c, 1.0e-12)
    def body(_, t):
        f = adaptive_distance(state, t) - rho
        c_t = jnp.where(
            jnp.abs(lam) > 1.0e-18,
            ceq + (state.c-ceq)*jnp.exp(-lam*t),
            state.c,
        )
        return jnp.maximum(0.0, t - f/jnp.maximum(c_t,1.0e-12))
    return jax.lax.fori_loop(0, 8, body, t0)


def packet_times(state):
    short = state.rho / 0.5
    adapt = jax.vmap(lambda r: _adaptive_packet_time(state, r))(state.rho)
    dt = jnp.where(state.kind == KIND_SHORT, short, adapt)
    return jnp.where(state.active, dt, jnp.inf)


def next_arrival_dt(state):
    return jnp.min(packet_times(state))


def _spike_root_single(state, i, dtmax):
    deficit = TWO_PI - state.phi[i]
    psi = state.psi[i:i+1]
    q = state.q[i:i+1]
    def gain(dt):
        return phase_gain_vec(psi, q, dt)[0]
    finite_max = jnp.isfinite(dtmax)
    gain_max = jax.lax.cond(finite_max, lambda _: gain(dtmax), lambda _: jnp.inf, operand=None)
    possible_before = (~finite_max) | (gain_max + 1.0e-13 >= deficit)
    def expand_body(_, hi):
        return jnp.where(gain(hi) < deficit, 2.0 * hi, hi)
    hi_free = jax.lax.fori_loop(0, 12, expand_body, jnp.array(1.0))
    hi = jnp.where(finite_max, dtmax, hi_free)
    def bisect(_, lr):
        lo, hi = lr
        mid = 0.5 * (lo + hi)
        f = gain(mid) - deficit
        return (jnp.where(f < 0.0, mid, lo), jnp.where(f < 0.0, hi, mid))
    lo, hi = jax.lax.fori_loop(0, 58, bisect, (jnp.array(0.0), hi))
    root = 0.5 * (lo + hi)
    return jnp.where(deficit <= 1.0e-12, 0.0, jnp.where(possible_before, root, jnp.inf))


def spike_times(state, dtmax):
    return jnp.stack([_spike_root_single(state, i, dtmax) for i in range(N)])


def next_spike_dt(state, dtmax):
    return jnp.min(spike_times(state, dtmax))


def advance(state, dt):
    phi = state.phi + phase_gain_vec(state.psi, state.q, dt)
    e = jnp.exp(-ALPHA * dt)
    psi = e * (state.psi + state.q * dt)
    q = e * state.q
    long_dist = adaptive_distance(state, dt)
    dr = jnp.where(state.kind == KIND_SHORT, 0.5 * dt, long_dist)
    rho = jnp.where(state.active, state.rho - dr, state.rho)
    c = advance_c(state, dt)
    return state._replace(t=state.t + dt, phi=phi, psi=psi, q=q, rho=rho, c=c)


def process_arrivals(state, tol=1.0e-9):
    arrived = state.active & (state.rho <= tol)
    dq = jnp.zeros(N, dtype=jnp.float64).at[state.target].add(
        jnp.where(arrived, state.weight * ALPHA**2, 0.0)
    )
    q = state.q + dq
    active = state.active & (~arrived)
    kind = jnp.where(arrived, KIND_INACTIVE, state.kind)
    rho = jnp.where(arrived, 0.0, state.rho)
    return state._replace(q=q, active=active, kind=kind, rho=rho)


def _update_cycle_if_complete(state):
    m = jnp.min(state.count)
    complete = (m > 0) & jnp.all(state.count == m)
    mean = jnp.mean(state.last_spike)
    angles = TWO_PI * jnp.arange(N) / N
    centered = state.last_spike - mean
    zr = jnp.mean(centered * jnp.cos(angles))
    zi = -jnp.mean(centered * jnp.sin(angles))
    A = jnp.sqrt(zr*zr + zi*zi)
    period = mean - state.last_cycle_mean
    return state._replace(
        A_held=jnp.where(complete, A, state.A_held),
        last_period=jnp.where(complete & jnp.isfinite(state.last_cycle_mean), period, state.last_period),
        last_cycle_mean=jnp.where(complete, mean, state.last_cycle_mean),
    )


def process_spikes(state, tol=2.0e-8):
    firing = state.phi >= TWO_PI - tol
    phi = jnp.where(firing, state.phi - TWO_PI, state.phi)
    phi = jnp.where(jnp.abs(phi) < 1.0e-10, 0.0, phi)
    count = state.count + firing.astype(jnp.int32)
    last = jnp.where(firing, state.t, state.last_spike)
    st = state._replace(phi=phi, count=count, last_spike=last)
    st = _emit_mask(st, firing)
    return _update_cycle_if_complete(st)


def step(state):
    dta = next_arrival_dt(state)
    dts = next_spike_dt(state, dta)
    dt = jnp.minimum(dta, dts)
    st = advance(state, dt)
    st = jax.lax.cond(dta <= dt + 1.0e-8, process_arrivals, lambda x: x, st)
    st = process_spikes(st)
    return st._replace(event_count=st.event_count + 1)


def run_until_cycles(state, cycles, max_events=2_000_000):
    start = jnp.min(state.count)
    target = start + int(cycles)
    def cond(carry):
        st, k = carry
        return (jnp.min(st.count) < target) & (k < max_events) & (~st.overflow)
    def body(carry):
        st, k = carry
        return step(st), k + 1
    return jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))


def run_to_tau(state, tau_target, max_events=5_000_000):
    start = jnp.min(state.count)
    def cond(carry):
        st, k = carry
        return (1.0 / st.c > tau_target) & (k < max_events) & (~st.overflow)
    def body(carry):
        st, k = carry
        return step(st), k + 1
    st, k = jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))
    return st, jnp.min(st.count) - start, k

run_cycles_jit = jax.jit(run_until_cycles, static_argnames=("cycles", "max_events"))
run_to_tau_jit = jax.jit(run_to_tau, static_argnames=("max_events",))
step_jit = jax.jit(step)


def center_seed(state, A_guess=1.0e-3):
    nu = response(state.psi)
    desired = 2.0 * A_guess * jnp.cos(TWO_PI * jnp.arange(N) / N)
    return state._replace(phi=state.phi - nu * desired)


def cycle_complex_Z(state):
    mean = jnp.mean(state.last_spike)
    centered = state.last_spike - mean
    angles = TWO_PI * jnp.arange(N) / N
    return jnp.mean(centered * (jnp.cos(angles) - 1j*jnp.sin(angles)))


def _one_cycle(state):
    target = jnp.min(state.count) + 1
    def cond(carry):
        st, k = carry
        return (jnp.min(st.count) < target) & (k < 128) & (~st.overflow)
    def body(carry):
        st, k = carry
        return step(st), k + 1
    st, _ = jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))
    return st


def collect_cycles(state, cycles):
    def body(st, _):
        st = _one_cycle(st)
        return st, jnp.stack([
            jnp.real(cycle_complex_Z(st)), jnp.imag(cycle_complex_Z(st)),
            st.A_held, st.last_period,
        ])
    return jax.lax.scan(body, state, xs=None, length=cycles)

collect_cycles_jit = jax.jit(collect_cycles, static_argnames=("cycles",))


def run_until_cycles_dynamic(state, cycles, max_events=2_000_000):
    target = jnp.min(state.count) + jnp.asarray(cycles, dtype=jnp.int32)
    def cond(carry):
        st, k = carry
        return (jnp.min(st.count) < target) & (k < max_events) & (~st.overflow)
    def body(carry):
        st, k = carry
        return step(st), k + 1
    return jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))

run_cycles_dynamic_jit = jax.jit(run_until_cycles_dynamic)
