"""CORE v0.22 — latent synaptic-state information limit.

Adds a minimal two-variable synaptic latent block to the v0.21 inverse model:
    theta = (p, tau3, eta1, eta2, xi_psi, xi_q)
with
    psi0 = psi_base + xi_psi * v,
    q0   = q_base   + xi_q   * v,
    v = (2,-1,-1)/sqrt(6).

The script reuses the validated v0.21 event primitives. It benchmarks local
rank/sloppiness, redesigns six-row observation schedules, exhibits a finite
same-chart weak direction and an exact nonlinear alias, and optionally reruns
multistart and small-noise audits.
"""
from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

import jax
import jax.numpy as jnp
import numpy as np
from scipy.optimize import least_squares

import core_v021_observation_design as v21

jax.config.update("jax_enable_x64", True)

THETA_TRUE = np.array([v21.P_TRUE, v21.TAU_TRUE, 0.0, 0.0, 0.0, 0.0])
SYNAPTIC_MODE = np.array([2.0, -1.0, -1.0]) / math.sqrt(6.0)
SYNAPTIC_MODE_J = jnp.asarray(SYNAPTIC_MODE)
SIGMA_T = 1.0e-4
SIGMA_LINEAR_AUDIT = 1.0e-6
BASELINE6 = (0, 1, 2, 3, 4, 5)
V021_E6 = (1, 2, 3, 4, 9, 11)


@dataclass
class ResultSummary:
    truth_count: int
    distances: np.ndarray
    max_cost: float


def np_state(theta):
    theta = np.asarray(theta, float)
    eta = theta[2:4]
    return v21.NPState(
        0.0,
        v21.PSI0 + theta[4] * SYNAPTIC_MODE,
        v21.Q0 + theta[5] * SYNAPTIC_MODE,
        v21.PHI_BASE + v21.LATENT_B @ eta,
        np.zeros(v21.QMAX, bool), np.zeros(v21.QMAX, int), np.zeros(v21.QMAX),
    )


def record_chart(theta=THETA_TRUE):
    p, tau = map(float, theta[:2])
    st = np_state(theta)
    counts = np.zeros(v21.N, int)
    obs = np.full((v21.N, v21.NCYC), np.nan)
    rows, margins, event_of_label = [], [], {}

    while np.min(counts) < v21.NCYC:
        ft = np.array([v21.firing_time_np(st.psi[i], st.q[i], st.phi[i]) for i in range(v21.N)])
        at = np.full(v21.QMAX, np.inf)
        for k in np.where(st.active)[0]:
            edge = st.edge_id[k]
            at[k] = st.rho[k] / (0.5 if v21.MODE[edge] == 1 else 1.0 / tau)
        fi, ai = int(np.argmin(ft)), int(np.argmin(at))
        if ft[fi] <= at[ai]:
            kind, idx, dt = v21.KIND_F, fi, ft[fi]
            competitor = min(np.min(np.delete(ft, fi)), np.min(at))
        else:
            kind, idx, dt = v21.KIND_A, ai, at[ai]
            competitor = min(np.min(ft), np.min(np.delete(at, ai)))
        margins.append(competitor - dt)
        v21.advance_np(st, dt, tau)
        if kind == v21.KIND_A:
            edge = int(st.edge_id[idx])
            st.q[v21.TARGET[edge]] += v21.edge_weight_np(p, edge) * v21.ALPHA**2
            st.active[idx] = False
            st.rho[idx] = 0.0
            rows.append((kind, idx, dt, 0, 0))
        else:
            i, cyc = idx, int(counts[idx])
            st.phi[i] -= v21.TWO_PI
            st.q[i] += v21.ALPHA**2
            free = np.where(~st.active)[0][:2]
            for slot, edge in zip(free, (3 * i + 1, 3 * i + 2)):
                st.active[slot] = True
                st.edge_id[slot] = edge
                st.rho[slot] = 1.0
            if cyc < v21.NCYC:
                obs[i, cyc] = st.t
                event_of_label[(i, cyc)] = len(rows)
            counts[i] += 1
            rows.append((kind, i, dt, int(free[0]), int(free[1])))

    a = np.asarray(rows)
    tok = v21.Tokens(
        jnp.asarray(a[:, 0], jnp.int32), jnp.asarray(a[:, 1], jnp.int32),
        jnp.asarray(a[:, 2], jnp.float64), jnp.asarray(a[:, 3], jnp.int32),
        jnp.asarray(a[:, 4], jnp.int32),
    )
    y = np.array([obs[i, c] for i, c in v21.LABELS])
    return tok, y, np.asarray(margins), event_of_label


def jstate(theta):
    phi = jnp.asarray(v21.PHI_BASE) + v21.LATENT_BJ @ theta[2:4]
    psi = jnp.asarray(v21.PSI0) + theta[4] * SYNAPTIC_MODE_J
    q = jnp.asarray(v21.Q0) + theta[5] * SYNAPTIC_MODE_J
    return v21.JState(
        jnp.array(0.0), psi, q, phi,
        jnp.zeros(v21.QMAX, bool), jnp.zeros(v21.QMAX, jnp.int32), jnp.zeros(v21.QMAX),
        jnp.zeros(v21.N, jnp.int32), jnp.full((v21.N, v21.NCYC), jnp.nan),
    )


def replay(theta, tok):
    p, tau = theta[:2]
    st = jstate(theta)
    def body(k, s):
        kind, idx, guess = tok.kind[k], tok.idx[k], tok.guess[k]
        ft, at = v21.candidate_times(s, tau, guess)
        dt = jnp.where(kind == v21.KIND_F, ft[idx], at[idx])
        s = v21.advance(s, dt, tau)
        return v21.process_one(s, p, kind, idx, tok.slot0[k], tok.slot1[k])
    st = jax.lax.fori_loop(0, tok.kind.shape[0], body, st)
    return jnp.stack([st.obs[i, c] for i, c in v21.LABELS])


def fixed_fd_jac(theta, tok, h=1.0e-6):
    theta = np.asarray(theta, float)
    cols = []
    for j in range(6):
        d = np.zeros(6); d[j] = 1.0
        yp = np.asarray(replay(jnp.asarray(theta + h * d), tok))
        ym = np.asarray(replay(jnp.asarray(theta - h * d), tok))
        cols.append((yp - ym) / (2.0 * h))
    return np.column_stack(cols)


def design_stats(J, inds, sigma=SIGMA_T):
    A = J[list(inds)]
    sv = np.linalg.svd(A, compute_uv=False)
    rank = np.linalg.matrix_rank(A, 1.0e-10)
    if rank < J.shape[1]:
        return dict(rank=rank, singular_values=sv, sigma_min=0.0, logdet=-np.inf, trace_cov=np.inf)
    gram = A.T @ A
    sign, logdet = np.linalg.slogdet(gram)
    cov = sigma**2 * np.linalg.inv(gram)
    return dict(rank=rank, singular_values=sv, sigma_min=float(sv[-1]),
                condition_number=float(sv[0] / sv[-1]),
                logdet=float(logdet if sign > 0 else -np.inf),
                trace_cov=float(np.trace(cov)), std=np.sqrt(np.diag(cov)))


def best_subset(J, available, k, criterion="E"):
    best = None
    for inds in itertools.combinations(available, k):
        st = design_stats(J, inds)
        if st["rank"] < J.shape[1]:
            continue
        score = st["sigma_min"] if criterion == "E" else (st["logdet"] if criterion == "D" else -st["trace_cov"])
        if best is None or score > best[0]:
            best = (score, inds, st)
    return best


def signature(tok):
    return tuple(zip(np.asarray(tok.kind).tolist(), np.asarray(tok.idx).tolist()))


def benchmark_checks():
    tok, y, margins, _ = record_chart()
    replay_fun = jax.jit(lambda th: replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay(th, tok)))
    yj = np.asarray(replay_fun(jnp.asarray(THETA_TRUE)))
    truth_err = float(np.max(np.abs(yj - y)))
    assert truth_err < 2.0e-12
    J = np.asarray(jac_fun(jnp.asarray(THETA_TRUE)))
    Jfd = fixed_fd_jac(THETA_TRUE, tok)
    jac_rel = float(np.linalg.norm(J - Jfd) / np.linalg.norm(Jfd))
    assert jac_rel < 1.0e-8

    baseline = design_stats(J, BASELINE6)
    v021 = design_stats(J, V021_E6)
    e6 = best_subset(J, range(12), 6, "E")
    d6 = best_subset(J, range(12), 6, "D")
    e9 = best_subset(J, range(12), 9, "E")
    full12 = design_stats(J, tuple(range(12)))
    assert e6[1] == (0, 1, 2, 3, 4, 11)
    assert d6[1] == (0, 1, 2, 9, 10, 11)
    assert e9[1] == (0, 1, 2, 3, 4, 5, 7, 9, 11)
    assert abs(full12["sigma_min"] - 9.137484227978426e-4) < 2.0e-12
    assert v021["sigma_min"] < 0.3 * baseline["sigma_min"]
    assert np.all(v021["std"][2:] / baseline["std"][2:] > 3.2)
    assert baseline["std"][0] / d6[2]["std"][0] > 3.3
    assert baseline["std"][1] / d6[2]["std"][1] > 2.7
    assert np.all(baseline["std"][2:] / d6[2]["std"][2:] > 1.0)

    horizon = {}
    for cycles in (2, 3, 4):
        available = [i for i, (_, c) in enumerate(v21.LABELS) if c < cycles]
        horizon[cycles] = best_subset(J, available, 6, "E")
    assert horizon[2][1] == BASELINE6
    assert horizon[3][1] == (0, 1, 2, 3, 4, 8)
    assert horizon[4][1] == (0, 1, 2, 3, 4, 11)
    assert horizon[4][2]["sigma_min"] / horizon[2][2]["sigma_min"] < 1.02
    assert full12["sigma_min"] / baseline["sigma_min"] < 1.04

    _, S, Vh = np.linalg.svd(J, full_matrices=False)
    weak = Vh[-1]
    assert np.linalg.norm(weak[2:]) > 0.999
    assert abs(weak[4]) > 0.78

    th_weak = THETA_TRUE + 0.01 * weak
    tok_w, y_w, margins_w, _ = record_chart(th_weak)
    dy = y_w - y
    weak_rms = float(np.sqrt(np.mean(dy**2)))
    weak_max = float(np.max(np.abs(dy)))
    weak_norm_sigma = float(np.linalg.norm(dy) / SIGMA_T)
    assert signature(tok_w) == signature(tok)
    assert weak_max < 0.30 * SIGMA_T
    assert weak_norm_sigma < 0.60
    assert np.min(margins_w) > 0.0728

    x0 = THETA_TRUE + np.array([0.01, -0.01, 0.002, -0.002, 0.003, -0.001])
    inds = np.asarray(V021_E6, int)
    sol_alias = least_squares(
        lambda x: np.asarray(replay_fun(jnp.asarray(x)))[inds] - y[inds],
        x0, jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[inds],
        max_nfev=80, xtol=1e-13, ftol=1e-13, gtol=1e-13)
    delta = sol_alias.x - THETA_TRUE
    tok_a, y_a, margins_a, _ = record_chart(sol_alias.x)
    alias_align = float(abs(np.dot(delta, weak)) / np.linalg.norm(delta))
    assert np.linalg.norm(delta) > 0.007
    assert np.max(np.abs((y_a - y)[inds])) < 5.0e-13
    assert np.max(np.abs(y_a - y)) > 3.0e-5
    assert alias_align > 0.999
    assert signature(tok_a) == signature(tok)

    return dict(event_count=int(tok.kind.shape[0]), truth_spikes=y,
                truth_chart_min_margin=float(np.min(margins)), truth_replay_max_error=truth_err,
                jax_fd_relative_error=jac_rel, full12=full12, baseline6=baseline,
                v021_e6=v021, v022_e6=e6, v022_d6=d6, v022_e9=e9, horizon=horizon,
                weak_singular_vector=weak, weak_sigma_min=float(S[-1]),
                weak_profile=dict(theta=th_weak, rms_spike_shift=weak_rms,
                                  max_spike_shift=weak_max,
                                  residual_norm_in_sigma=weak_norm_sigma,
                                  min_chart_margin=float(np.min(margins_w))),
                v021_alias=dict(solution=sol_alias.x,
                                parameter_distance=float(np.linalg.norm(delta)),
                                weak_alignment=alias_align,
                                selected_max_residual=float(np.max(np.abs((y_a-y)[inds]))),
                                full12_max_residual=float(np.max(np.abs(y_a-y))),
                                min_chart_margin=float(np.min(margins_a))))


def multistart_direct():
    tok, y, _, _ = record_chart()
    replay_fun = jax.jit(lambda th: replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay(th, tok)))
    J = np.asarray(jac_fun(jnp.asarray(THETA_TRUE)))
    designs = {f"E{k}": best_subset(J, range(12), k, "E")[1] for k in range(6, 10)}
    designs["FULL12"] = tuple(range(12))
    rng = np.random.default_rng(20260906)
    starts = [THETA_TRUE + rng.normal(size=6) * np.array([0.02, 0.02, 0.005, 0.005, 0.008, 0.002]) for _ in range(12)]
    out = {}
    for name, inds in designs.items():
        ii = np.asarray(inds, int)
        dists, costs = [], []
        for x0 in starts:
            sol = least_squares(lambda x: np.asarray(replay_fun(jnp.asarray(x)))[ii] - y[ii], x0,
                                jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[ii],
                                max_nfev=100, xtol=1e-13, ftol=1e-13, gtol=1e-13)
            dists.append(np.linalg.norm(sol.x - THETA_TRUE)); costs.append(sol.cost)
        dists = np.asarray(dists)
        out[name] = ResultSummary(int(np.sum(dists < 1e-6)), dists, float(np.max(costs)))
    assert out["E6"].truth_count < 12 and out["E8"].truth_count < 12
    assert out["E9"].truth_count == 12 and out["FULL12"].truth_count == 12
    return out


def noise_direct():
    tok, y, _, _ = record_chart()
    replay_fun = jax.jit(lambda th: replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay(th, tok)))
    J = np.asarray(jac_fun(jnp.asarray(THETA_TRUE)))
    d6 = best_subset(J, range(12), 6, "D")[1]
    audits = []
    for name, inds, seed in (("baseline6", BASELINE6, 222), ("v022_D6", d6, 333)):
        ii = np.asarray(inds, int)
        A = J[ii]
        fisher = SIGMA_LINEAR_AUDIT * np.sqrt(np.diag(np.linalg.inv(A.T @ A)))
        rng, xs = np.random.default_rng(seed), []
        for _ in range(30):
            data = y[ii] + rng.normal(scale=SIGMA_LINEAR_AUDIT, size=len(ii))
            x0 = THETA_TRUE + np.array([1e-4, -1e-4, 1e-4, -1e-4, 1e-4, -1e-4])
            sol = least_squares(lambda x: np.asarray(replay_fun(jnp.asarray(x)))[ii] - data, x0,
                                jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[ii],
                                max_nfev=100, xtol=1e-13, ftol=1e-13, gtol=1e-13)
            xs.append(sol.x)
        xs = np.asarray(xs); empirical = xs.std(0, ddof=1)
        assert np.all((empirical / fisher) > 0.65) and np.all((empirical / fisher) < 1.25)
        audits.append((name, xs.mean(0), empirical, fisher))
    return audits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--multistart-direct", action="store_true")
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()
    out = benchmark_checks()
    print("CORE v0.22 latent-synaptic-state checks passed")
    print("baseline6", out["baseline6"]["sigma_min"], out["baseline6"]["std"])
    print("v0.21 E6 expanded", out["v021_e6"]["sigma_min"], out["v021_e6"]["std"])
    print("v0.22 E6", out["v022_e6"][1], out["v022_e6"][2]["sigma_min"])
    print("v0.22 D6", out["v022_d6"][1], out["v022_d6"][2]["std"])
    print("full12 weak", out["weak_sigma_min"], out["weak_singular_vector"])
    print("weak profile", out["weak_profile"])
    print("v0.21 nonlinear alias", out["v021_alias"])
    if args.multistart_direct:
        print("multistart", multistart_direct())
    if args.noise_direct:
        for row in noise_direct(): print("noise", row)


if __name__ == "__main__":
    main()
