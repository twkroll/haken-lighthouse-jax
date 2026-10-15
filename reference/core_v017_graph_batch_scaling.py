"""Sparse graph, batching, and scaling regression for CORE v0.17."""
from __future__ import annotations

import argparse
import time
import numpy as np
import jax
import jax.numpy as jnp

from core_v017_graph_queue_kernel import (
    ALPHA, A_FIC, C0, C_NS, TAU_FIC, T_NS,
    batched_center_seed, batched_run_cycles, center_seed,
    fixed_arrival_weight_derivative, make_state, permute_edges,
    ring_graph, run_cycles_jit, run_to_tau_jit, set_adaptation,
    stack_states, stack_graphs, batched_run_graphs,
)

jax.config.update("jax_enable_x64", True)

N3_PERIOD = 16.29749605483085
N3_A0 = 0.0010023850245501774
N3_SKIP = 0.0010058631750129
N3_SKIP_ORACLE_V016 = 0.0010058631750


def specialization_checks():
    graph = ring_graph(3)
    state = make_state(graph, 12, c=C_NS, c0=C_NS)
    state, _ = run_cycles_jit(state, graph, 80)
    assert abs(float(state.last_period) - N3_PERIOD) < 3e-11
    assert abs(float(state.last_period) - T_NS) < 5e-9
    assert int(state.max_active) == 6
    assert not bool(state.overflow)

    state = center_seed(state, graph, 1e-3)
    state, _ = run_cycles_jit(state, graph, 20)
    assert abs(float(state.A_held) - N3_A0) < 2e-12
    return graph, state


def capacity_checks():
    graph = ring_graph(3)
    q5 = make_state(graph, 5, c=C_NS, c0=C_NS)
    q6 = make_state(graph, 6, c=C_NS, c0=C_NS)
    assert bool(q5.overflow)
    assert int(jnp.sum(q5.active)) == 5
    assert not bool(q6.overflow)
    assert int(jnp.sum(q6.active)) == 6


def permutation_checks():
    graph = ring_graph(3)
    perm = np.random.default_rng(7).permutation(graph.src.shape[0])
    shuffled = permute_edges(graph, perm)

    def run(g):
        st = make_state(g, 12, c=C_NS, c0=C_NS)
        st, _ = run_cycles_jit(st, g, 80)
        st = center_seed(st, g, 1e-3)
        st, _ = run_cycles_jit(st, g, 120)
        return st

    a, b = run(graph), run(shuffled)
    names = ["t", "psi", "q", "phi", "c", "count", "last_spike", "A_held", "last_period"]
    err = 0.0
    for name in names:
        err = max(err, float(np.max(np.abs(np.asarray(getattr(a, name)) - np.asarray(getattr(b, name))))))
    assert err < 1e-12
    assert int(a.event_count) == int(b.event_count)
    return err


def batch_checks():
    graph = ring_graph(3)
    base = make_state(graph, 12, c=C_NS, c0=C_NS)
    base, _ = run_cycles_jit(base, graph, 80)
    amps = jnp.asarray([0.0, 5e-4, 1e-3, 2e-3])
    batch = stack_states([base] * len(amps))
    batch = batched_center_seed(batch, graph, amps)
    batch_fun = jax.jit(batched_run_cycles, static_argnames=("cycles",))
    bout = batch_fun(batch, graph, 30)

    singles = []
    for a in np.asarray(amps):
        st = center_seed(base, graph, float(a))
        st, _ = run_cycles_jit(st, graph, 30)
        singles.append(st)

    maxerr = 0.0
    for name in ["t", "psi", "q", "phi", "c", "rho", "count", "last_spike", "A_held", "last_period"]:
        x = np.asarray(getattr(bout, name))
        y = np.stack([np.asarray(getattr(st, name)) for st in singles])
        maxerr = max(maxerr, float(np.max(np.abs(x - y))))
    assert maxerr < 1e-10
    return maxerr


def graph_parameter_batch_checks():
    ps = np.array([-3.2682, -3.2680, -3.2678, -3.2676])
    graphs = [ring_graph(3, float(p)) for p in ps]
    states = [make_state(g, 12, c=C_NS, c0=C_NS) for g in graphs]
    bg = stack_graphs(graphs)
    bs = stack_states(states)
    fun = jax.jit(batched_run_graphs, static_argnames=("cycles",))
    bout = fun(bs, bg, 40)
    singles = []
    for st, g in zip(states, graphs):
        out, _ = run_cycles_jit(st, g, 40)
        singles.append(out)
    maxerr = 0.0
    for name in ["t", "psi", "q", "phi", "count", "last_spike", "A_held", "last_period"]:
        x = np.asarray(getattr(bout, name))
        y = np.stack([np.asarray(getattr(st, name)) for st in singles])
        maxerr = max(maxerr, float(np.max(np.abs(x-y))))
    assert maxerr < 1e-10
    return maxerr


def slow_direct():
    graph, state = specialization_checks()
    state = set_adaptation(state, 1e-5, kappa=0.0, c0=C0)
    state, cycles, events = run_to_tau_jit(state, graph, TAU_FIC)
    A = float(state.A_held)
    assert int(cycles) == 15002
    assert abs(A - N3_SKIP) < 5e-12
    assert abs(A - N3_SKIP_ORACLE_V016) / N3_SKIP_ORACLE_V016 < 1e-8
    assert A / A_FIC < 0.02
    assert int(state.max_active) == 6
    assert not bool(state.overflow)
    print("v0.17 N=3 slow specialization:", int(cycles), int(events), A, A / A_FIC)


def parameter_chart_check():
    graph = ring_graph(3)
    d = float(fixed_arrival_weight_derivative(graph, edge=1))
    assert abs(d - ALPHA**2) < 1e-14
    return d


def scaling_checks(sizes=(3, 8, 16, 32, 64), cycles=20):
    rows = []
    for N in sizes:
        graph = ring_graph(N)
        state = make_state(graph, 4 * N, c=C_NS, c0=C_NS)
        fun = jax.jit(lambda st: run_cycles_jit(st, graph, cycles)[0])
        state = fun(state)
        jax.block_until_ready(state.t)
        t0 = time.perf_counter()
        state2 = fun(make_state(graph, 4 * N, c=C_NS, c0=C_NS))
        jax.block_until_ready(state2.t)
        elapsed = time.perf_counter() - t0
        row = {
            "N": N,
            "E": 3 * N,
            "Q": 4 * N,
            "period": float(state.last_period),
            "max_active": int(state.max_active),
            "overflow": bool(state.overflow),
            "seconds_second_call": elapsed,
        }
        assert abs(row["period"] - N3_PERIOD) < 5e-10
        assert row["max_active"] == 2 * N
        assert not row["overflow"]
        rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slow-direct", action="store_true")
    parser.add_argument("--scaling", action="store_true")
    parser.add_argument("--scaling-large", action="store_true")
    args = parser.parse_args()

    graph, state = specialization_checks()
    capacity_checks()
    perr = permutation_checks()
    berr = batch_checks()
    gberr = graph_parameter_batch_checks()
    dw = parameter_chart_check()

    print("CORE v0.17 graph/batch checks passed")
    print("N=3 frozen period/max_active:", N3_PERIOD, int(state.max_active))
    print("edge-permutation max physical error:", perr)
    print("vmap-vs-single max error:", berr)
    print("batched-graph-vs-single max error:", gberr)
    print("fixed-arrival dq_target/dw:", dw)

    if args.slow_direct:
        slow_direct()
    if args.scaling:
        for row in scaling_checks():
            print(row)
    if args.scaling_large:
        for row in scaling_checks((128, 256)):
            print(row)


if __name__ == "__main__":
    main()
