"""Sparse-graph fixed-capacity JAX packet queue for CORE v0.17.

The v0.16 N=3 ring is represented as a graph specialization. Topology labels
(src, target, edge mode) are discrete chart data; continuous edge parameters
(weight, length, fixed speed) remain ordinary JAX arrays.
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

MODE_ZERO = 0
MODE_FIXED = 1
MODE_ADAPTIVE = 2

_gx, _gw = leggauss(20)
GX = jnp.asarray(_gx)
GW = jnp.asarray(_gw)


class Graph(NamedTuple):
    src: jax.Array
    target: jax.Array
    weight: jax.Array
    length: jax.Array
    mode: jax.Array
    fixed_speed: jax.Array
    observer_re: jax.Array
    observer_im: jax.Array


class State(NamedTuple):
    t: jax.Array
    psi: jax.Array
    q: jax.Array
    phi: jax.Array
    c: jax.Array
    epsilon: jax.Array
    kappa: jax.Array
    c0: jax.Array
    active: jax.Array
    edge_id: jax.Array
    rho: jax.Array
    count: jax.Array
    last_spike: jax.Array
    A_held: jax.Array
    last_cycle_mean: jax.Array
    last_period: jax.Array
    overflow: jax.Array
    max_active: jax.Array
    event_count: jax.Array


def ring_graph(N=3, p=P_ADAPT):
    """Sparse three-edge-per-node ring that specializes exactly to v0.16 at N=3."""
    src = []
    target = []
    weight = []
    length = []
    mode = []
    fixed_speed = []
    for s in range(int(N)):
        src.extend([s, s, s])
        target.extend([s, (s + 1) % N, (s + 2) % N])
        weight.extend([1.0, p, -p])
        length.extend([0.0, 1.0, 1.0])
        mode.extend([MODE_ZERO, MODE_FIXED, MODE_ADAPTIVE])
        fixed_speed.extend([0.0, 0.5, 0.0])
    angles = TWO_PI * np.arange(N) / N
    return Graph(
        src=jnp.asarray(src, dtype=jnp.int32),
        target=jnp.asarray(target, dtype=jnp.int32),
        weight=jnp.asarray(weight, dtype=jnp.float64),
        length=jnp.asarray(length, dtype=jnp.float64),
        mode=jnp.asarray(mode, dtype=jnp.int32),
        fixed_speed=jnp.asarray(fixed_speed, dtype=jnp.float64),
        observer_re=jnp.asarray(np.cos(angles), dtype=jnp.float64),
        observer_im=jnp.asarray(-np.sin(angles), dtype=jnp.float64),
    )


def permute_edges(graph, permutation):
    p = jnp.asarray(permutation, dtype=jnp.int32)
    return Graph(
        graph.src[p], graph.target[p], graph.weight[p], graph.length[p],
        graph.mode[p], graph.fixed_speed[p], graph.observer_re, graph.observer_im,
    )


def response(x):
    y = x + 1.0
    ys = jnp.maximum(y, 1.0e-15)
    return jnp.where(y > 0.0, jnp.exp(-1.0 / (ys * ys)), 0.0)


def phase_gain_single(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e * (psi + q * s)
    return 0.5 * dt * jnp.sum(GW * response(ps))


def phase_gain_vec(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    return 0.5 * dt * jnp.sum(GW[None, :] * response(ps), axis=1)


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
    Q = active.shape[0]
    idx = jnp.arange(Q, dtype=jnp.int32)
    return jnp.min(jnp.where(~active, idx, Q))


def _insert_edge_packet(state, graph, edge):
    Q = state.active.shape[0]
    slot = _first_inactive(state.active)
    ok = slot < Q
    safe = jnp.minimum(slot, Q - 1)
    return state._replace(
        active=state.active.at[safe].set(jnp.where(ok, True, state.active[safe])),
        edge_id=state.edge_id.at[safe].set(jnp.where(ok, edge, state.edge_id[safe])),
        rho=state.rho.at[safe].set(jnp.where(ok, graph.length[edge], state.rho[safe])),
        overflow=state.overflow | (~ok),
    )


def _emit_mask(state, graph, firing_mask):
    zero = (graph.mode == MODE_ZERO) & firing_mask[graph.src]
    dq = jnp.zeros_like(state.q).at[graph.target].add(
        jnp.where(zero, graph.weight * ALPHA**2, 0.0)
    )
    state = state._replace(q=state.q + dq)
    E = graph.src.shape[0]

    def body(edge, st):
        delayed = (graph.mode[edge] != MODE_ZERO) & firing_mask[graph.src[edge]]
        return jax.lax.cond(
            delayed,
            lambda x: _insert_edge_packet(x, graph, edge),
            lambda x: x,
            st,
        )

    state = jax.lax.fori_loop(0, E, body, state)
    nactive = jnp.sum(state.active.astype(jnp.int32))
    return state._replace(max_active=jnp.maximum(state.max_active, nactive))


def make_state(graph, queue_capacity, *, c=C_NS, epsilon=0.0, kappa=0.0, c0=C0):
    N = graph.observer_re.shape[0]
    Q = int(queue_capacity)
    state = State(
        t=jnp.array(0.0),
        psi=jnp.zeros(N, dtype=jnp.float64),
        q=jnp.zeros(N, dtype=jnp.float64),
        phi=jnp.zeros(N, dtype=jnp.float64),
        c=jnp.asarray(c, dtype=jnp.float64),
        epsilon=jnp.asarray(epsilon, dtype=jnp.float64),
        kappa=jnp.asarray(kappa, dtype=jnp.float64),
        c0=jnp.asarray(c0, dtype=jnp.float64),
        active=jnp.zeros(Q, dtype=bool),
        edge_id=jnp.zeros(Q, dtype=jnp.int32),
        rho=jnp.zeros(Q, dtype=jnp.float64),
        count=jnp.zeros(N, dtype=jnp.int32),
        last_spike=jnp.zeros(N, dtype=jnp.float64),
        A_held=jnp.array(0.0),
        last_cycle_mean=jnp.array(jnp.nan),
        last_period=jnp.array(jnp.nan),
        overflow=jnp.array(False),
        max_active=jnp.array(0, dtype=jnp.int32),
        event_count=jnp.array(0, dtype=jnp.int32),
    )
    return _emit_mask(state, graph, jnp.ones(N, dtype=bool))


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
            ceq + (state.c - ceq) * jnp.exp(-lam * t),
            state.c,
        )
        return jnp.maximum(0.0, t - f / jnp.maximum(c_t, 1.0e-12))

    return jax.lax.fori_loop(0, 8, body, t0)


def packet_times(state, graph):
    edge = state.edge_id
    mode = graph.mode[edge]
    fixed = state.rho / jnp.maximum(graph.fixed_speed[edge], 1.0e-15)
    adaptive = jax.vmap(lambda r: _adaptive_packet_time(state, r))(state.rho)
    dt = jnp.where(mode == MODE_FIXED, fixed, adaptive)
    return jnp.where(state.active, dt, jnp.inf)


def next_arrival_dt(state, graph):
    return jnp.min(packet_times(state, graph))


def _spike_root_single(state, neuron, dtmax):
    deficit = TWO_PI - state.phi[neuron]
    psi = state.psi[neuron]
    q = state.q[neuron]

    def gain(dt):
        return phase_gain_single(psi, q, dt)

    finite = jnp.isfinite(dtmax)
    gain_max = jax.lax.cond(finite, lambda _: gain(dtmax), lambda _: jnp.inf, operand=None)
    possible = (~finite) | (gain_max + 1.0e-13 >= deficit)

    def expand(_, hi):
        return jnp.where(gain(hi) < deficit, 2.0 * hi, hi)

    hi_free = jax.lax.fori_loop(0, 12, expand, jnp.array(1.0))
    hi = jnp.where(finite, dtmax, hi_free)

    def bisect(_, bounds):
        lo, hi = bounds
        mid = 0.5 * (lo + hi)
        f = gain(mid) - deficit
        return jnp.where(f < 0.0, mid, lo), jnp.where(f < 0.0, hi, mid)

    lo, hi = jax.lax.fori_loop(0, 58, bisect, (jnp.array(0.0), hi))
    root = 0.5 * (lo + hi)
    return jnp.where(deficit <= 1.0e-12, 0.0, jnp.where(possible, root, jnp.inf))


def spike_times(state, dtmax):
    N = state.phi.shape[0]
    return jax.vmap(lambda i: _spike_root_single(state, i, dtmax))(
        jnp.arange(N, dtype=jnp.int32)
    )


def next_spike_dt(state, dtmax):
    return jnp.min(spike_times(state, dtmax))


def advance(state, graph, dt):
    phi = state.phi + phase_gain_vec(state.psi, state.q, dt)
    e = jnp.exp(-ALPHA * dt)
    psi = e * (state.psi + state.q * dt)
    q = e * state.q
    edge = state.edge_id
    mode = graph.mode[edge]
    travelled = jnp.where(
        mode == MODE_FIXED,
        graph.fixed_speed[edge] * dt,
        adaptive_distance(state, dt),
    )
    rho = jnp.where(state.active, state.rho - travelled, state.rho)
    return state._replace(
        t=state.t + dt,
        phi=phi,
        psi=psi,
        q=q,
        rho=rho,
        c=advance_c(state, dt),
    )


def process_arrivals(state, graph, tol=1.0e-9):
    arrived = state.active & (state.rho <= tol)
    edge = state.edge_id
    dq = jnp.zeros_like(state.q).at[graph.target[edge]].add(
        jnp.where(arrived, graph.weight[edge] * ALPHA**2, 0.0)
    )
    return state._replace(
        q=state.q + dq,
        active=state.active & (~arrived),
        rho=jnp.where(arrived, 0.0, state.rho),
    )


def _update_cycle_if_complete(state, graph):
    m = jnp.min(state.count)
    complete = (m > 0) & jnp.all(state.count == m)
    mean = jnp.mean(state.last_spike)
    centered = state.last_spike - mean
    zr = jnp.mean(centered * graph.observer_re)
    zi = jnp.mean(centered * graph.observer_im)
    A = jnp.sqrt(zr * zr + zi * zi)
    period = mean - state.last_cycle_mean
    return state._replace(
        A_held=jnp.where(complete, A, state.A_held),
        last_period=jnp.where(
            complete & jnp.isfinite(state.last_cycle_mean), period, state.last_period
        ),
        last_cycle_mean=jnp.where(complete, mean, state.last_cycle_mean),
    )


def process_spikes(state, graph, tol=2.0e-8):
    firing = state.phi >= TWO_PI - tol
    phi = jnp.where(firing, state.phi - TWO_PI, state.phi)
    phi = jnp.where(jnp.abs(phi) < 1.0e-10, 0.0, phi)
    state = state._replace(
        phi=phi,
        count=state.count + firing.astype(jnp.int32),
        last_spike=jnp.where(firing, state.t, state.last_spike),
    )
    state = _emit_mask(state, graph, firing)
    return _update_cycle_if_complete(state, graph)


def step(state, graph):
    dta = next_arrival_dt(state, graph)
    dts = next_spike_dt(state, dta)
    dt = jnp.minimum(dta, dts)
    state = advance(state, graph, dt)
    state = jax.lax.cond(
        dta <= dt + 1.0e-8,
        lambda x: process_arrivals(x, graph),
        lambda x: x,
        state,
    )
    state = process_spikes(state, graph)
    return state._replace(event_count=state.event_count + 1)


def run_until_cycles(state, graph, cycles, max_events=2_000_000):
    target = jnp.min(state.count) + int(cycles)

    def cond(carry):
        st, k = carry
        return (jnp.min(st.count) < target) & (k < max_events) & (~st.overflow)

    def body(carry):
        st, k = carry
        return step(st, graph), k + 1

    return jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))


def run_to_tau(state, graph, tau_target, max_events=5_000_000):
    start = jnp.min(state.count)

    def cond(carry):
        st, k = carry
        return (1.0 / st.c > tau_target) & (k < max_events) & (~st.overflow)

    def body(carry):
        st, k = carry
        return step(st, graph), k + 1

    state, k = jax.lax.while_loop(cond, body, (state, jnp.array(0, dtype=jnp.int32)))
    return state, jnp.min(state.count) - start, k


run_cycles_jit = jax.jit(run_until_cycles, static_argnames=("cycles", "max_events"))
run_to_tau_jit = jax.jit(run_to_tau, static_argnames=("max_events",))
step_jit = jax.jit(step)


def center_seed(state, graph, A_guess=1.0e-3):
    desired = 2.0 * A_guess * graph.observer_re
    return state._replace(phi=state.phi - response(state.psi) * desired)


def cycle_complex_Z(state, graph):
    mean = jnp.mean(state.last_spike)
    centered = state.last_spike - mean
    return jnp.mean(centered * (graph.observer_re + 1j * graph.observer_im))


def stack_states(states):
    return jax.tree.map(lambda *xs: jnp.stack(xs), *states)


def batched_run_cycles(states, graph, cycles):
    return jax.vmap(lambda st: run_until_cycles(st, graph, cycles)[0])(states)


def batched_center_seed(states, graph, amplitudes):
    return jax.vmap(lambda st, a: center_seed(st, graph, a))(states, amplitudes)


def stack_graphs(graphs):
    return jax.tree.map(lambda *xs: jnp.stack(xs), *graphs)


def batched_run_graphs(states, graphs, cycles):
    """vmap over states and equal-shape graph parameter tensors/topology charts."""
    return jax.vmap(lambda st, g: run_until_cycles(st, g, cycles)[0])(states, graphs)


def fixed_arrival_weight_derivative(graph, edge=1):
    """Chart-local derivative d q_target^+ / d weight_edge = alpha^2."""
    st = make_state(graph, max(4, 4 * graph.observer_re.shape[0]), c=C_NS, c0=C_NS)
    active = jnp.zeros_like(st.active).at[0].set(True)
    edge_id = jnp.zeros_like(st.edge_id).at[0].set(edge)
    rho = jnp.zeros_like(st.rho)
    st = st._replace(active=active, edge_id=edge_id, rho=rho, q=jnp.zeros_like(st.q))
    tgt = int(np.asarray(graph.target)[edge])

    def observable(w):
        weights = graph.weight.at[edge].set(w)
        g = graph._replace(weight=weights)
        return process_arrivals(st, g).q[tgt]

    return jax.grad(observable)(graph.weight[edge])
