"""CORE v0.21 — optimal observation design for hybrid Lighthouse inference.

Extends the v0.20 four-unknown inverse problem
    theta = (p, tau3, eta1, eta2)
from two observed cycles (six labelled spikes) to four cycles (twelve candidate
spike times). Exhaustive subset selection benchmarks E-, D-, and A-optimal
observation plans, horizon/neuron restrictions, and a controlled fifth unknown:
a global observation clock offset.

All derivatives are fixed-chart one-sided JAX derivatives on the physical truth
chart. The experiment-design layer selects rows of the same hybrid sensitivity
matrix; it does not differentiate through event-order argmin operations.
"""
from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass
from typing import NamedTuple

import jax
import jax.numpy as jnp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, least_squares

jax.config.update("jax_enable_x64", True)

ALPHA = 0.5
TWO_PI = 2.0 * math.pi
N = 3
QMAX = 24
NCYC = 4
P_TRUE = -3.267985407948901
TAU_TRUE = 8.0
THETA_TRUE = np.array([P_TRUE, TAU_TRUE, 0.0, 0.0])
SIGMA_T = 1.0e-4

GX_NP, GW_NP = leggauss(20)
GX = jnp.asarray(GX_NP)
GW = jnp.asarray(GW_NP)
MODE = np.array([0, 1, 2] * 3, dtype=int)
MODEJ = jnp.asarray(MODE)
TARGET = np.array([0, 1, 2, 1, 2, 0, 2, 0, 1], dtype=int)
TARGETJ = jnp.asarray(TARGET)
PSI0 = np.array([-0.207423841618632] * 3)
Q0 = np.array([0.780899408476725] * 3)
PHI_BASE = np.array([1.838519273976891, 1.488519273976891, 1.658519273976891])
LATENT_B = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, -1.0]])
LATENT_BJ = jnp.asarray(LATENT_B)
KIND_A = 0
KIND_F = 1
LABELS = tuple((i, c) for c in range(NCYC) for i in range(N))
BASELINE6 = tuple(range(6))


class Tokens(NamedTuple):
    kind: jax.Array
    idx: jax.Array
    guess: jax.Array
    slot0: jax.Array
    slot1: jax.Array


class JState(NamedTuple):
    t: jax.Array
    psi: jax.Array
    q: jax.Array
    phi: jax.Array
    active: jax.Array
    edge_id: jax.Array
    rho: jax.Array
    counts: jax.Array
    obs: jax.Array


@dataclass
class NPState:
    t: float
    psi: np.ndarray
    q: np.ndarray
    phi: np.ndarray
    active: np.ndarray
    edge_id: np.ndarray
    rho: np.ndarray


def edge_weight_np(p, edge):
    r = edge % 3
    return 1.0 if r == 0 else (p if r == 1 else -p)


def response_np(x):
    y = x + 1.0
    return np.where(y > 0.0, np.exp(-1.0 / np.maximum(y, 1.0e-15) ** 2), 0.0)


def phase_gain_np(psi, q, dt):
    s = 0.5 * dt * (GX_NP + 1.0)
    e = np.exp(-ALPHA * s)
    return float(0.5 * dt * np.dot(GW_NP, response_np(e * (psi + q * s))))


def firing_time_np(psi, q, phi):
    deficit = TWO_PI - phi
    if deficit <= 1.0e-12:
        return 0.0
    f = lambda t: phase_gain_np(psi, q, t) - deficit
    hi = 1.0
    for _ in range(30):
        if f(hi) >= 0.0:
            break
        hi *= 2.0
    return brentq(f, 0.0, hi, xtol=1.0e-13, rtol=1.0e-13)


def np_state(theta):
    eta = np.asarray(theta, float)[2:4]
    return NPState(
        0.0, PSI0.copy(), Q0.copy(), PHI_BASE + LATENT_B @ eta,
        np.zeros(QMAX, bool), np.zeros(QMAX, int), np.zeros(QMAX),
    )


def advance_np(st, dt, tau):
    old_psi, old_q = st.psi.copy(), st.q.copy()
    st.phi += np.array([phase_gain_np(old_psi[i], old_q[i], dt) for i in range(N)])
    e = math.exp(-ALPHA * dt)
    st.psi = e * (old_psi + old_q * dt)
    st.q = e * old_q
    speed = np.where(MODE[st.edge_id] == 1, 0.5, 1.0 / tau)
    st.rho = np.where(st.active, st.rho - speed * dt, st.rho)
    st.t += dt


def record_truth_chart(theta=THETA_TRUE):
    p, tau = map(float, theta[:2])
    st = np_state(theta)
    counts = np.zeros(N, int)
    obs = np.full((N, NCYC), np.nan)
    rows, margins, event_of_label = [], [], {}

    while np.min(counts) < NCYC:
        ft = np.array([firing_time_np(st.psi[i], st.q[i], st.phi[i]) for i in range(N)])
        at = np.full(QMAX, np.inf)
        for k in np.where(st.active)[0]:
            edge = st.edge_id[k]
            at[k] = st.rho[k] / (0.5 if MODE[edge] == 1 else 1.0 / tau)
        fi, ai = int(np.argmin(ft)), int(np.argmin(at))
        if ft[fi] <= at[ai]:
            kind, idx, dt = KIND_F, fi, ft[fi]
            competitor = min(np.min(np.delete(ft, fi)), np.min(at))
        else:
            kind, idx, dt = KIND_A, ai, at[ai]
            competitor = min(np.min(ft), np.min(np.delete(at, ai)))
        margins.append(competitor - dt)
        advance_np(st, dt, tau)
        if kind == KIND_A:
            edge = int(st.edge_id[idx])
            st.q[TARGET[edge]] += edge_weight_np(p, edge) * ALPHA**2
            st.active[idx] = False
            st.rho[idx] = 0.0
            rows.append((kind, idx, dt, 0, 0))
        else:
            i, cyc = idx, int(counts[idx])
            st.phi[i] -= TWO_PI
            st.q[i] += ALPHA**2
            free = np.where(~st.active)[0][:2]
            for slot, edge in zip(free, (3 * i + 1, 3 * i + 2)):
                st.active[slot] = True
                st.edge_id[slot] = edge
                st.rho[slot] = 1.0
            if cyc < NCYC:
                obs[i, cyc] = st.t
                event_of_label[(i, cyc)] = len(rows)
            counts[i] += 1
            rows.append((kind, i, dt, int(free[0]), int(free[1])))

    a = np.asarray(rows)
    tok = Tokens(
        jnp.asarray(a[:, 0], jnp.int32), jnp.asarray(a[:, 1], jnp.int32),
        jnp.asarray(a[:, 2], jnp.float64), jnp.asarray(a[:, 3], jnp.int32),
        jnp.asarray(a[:, 4], jnp.int32),
    )
    y = np.array([obs[i, c] for i, c in LABELS])
    return tok, y, np.asarray(margins), event_of_label


def response(x):
    y = x + 1.0
    ys = jnp.maximum(y, 1.0e-15)
    return jnp.where(y > 0.0, jnp.exp(-1.0 / (ys * ys)), 0.0)


def phase_gain_single(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    return 0.5 * dt * jnp.sum(GW * response(e * (psi + q * s)))


def phase_gain_vec(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    return 0.5 * dt * jnp.sum(GW[None, :] * response(ps), axis=1)


def firing_root(psi, q, phi, guess):
    t = jax.lax.stop_gradient(guess)
    def body(_, tt):
        g = phi + phase_gain_single(psi, q, tt) - TWO_PI
        e = jnp.exp(-ALPHA * tt)
        return tt - g / response(e * (psi + q * tt))
    return jax.lax.fori_loop(0, 7, body, t)


def edge_weight(p, edge):
    r = edge % 3
    return jnp.where(r == 0, 1.0, jnp.where(r == 1, p, -p))


def jstate(theta):
    phi = jnp.asarray(PHI_BASE) + LATENT_BJ @ theta[2:4]
    return JState(
        jnp.array(0.0), jnp.asarray(PSI0), jnp.asarray(Q0), phi,
        jnp.zeros(QMAX, bool), jnp.zeros(QMAX, jnp.int32), jnp.zeros(QMAX),
        jnp.zeros(N, jnp.int32), jnp.full((N, NCYC), jnp.nan),
    )


def advance(st, dt, tau):
    e = jnp.exp(-ALPHA * dt)
    psi = e * (st.psi + st.q * dt)
    q = e * st.q
    phi = st.phi + phase_gain_vec(st.psi, st.q, dt)
    speed = jnp.where(MODEJ[st.edge_id] == 1, 0.5, 1.0 / tau)
    rho = jnp.where(st.active, st.rho - speed * dt, st.rho)
    return st._replace(t=st.t + dt, psi=psi, q=q, phi=phi, rho=rho)


def candidate_times(st, tau, guess):
    ft = jax.vmap(lambda i: firing_root(st.psi[i], st.q[i], st.phi[i], guess))(jnp.arange(N))
    speed = jnp.where(MODEJ[st.edge_id] == 1, 0.5, 1.0 / tau)
    at = jnp.where(st.active, st.rho / speed, jnp.inf)
    return ft, at


def process_one(st, p, kind, idx, slot0, slot1):
    def arrival(s):
        edge = s.edge_id[idx]
        q = s.q.at[TARGETJ[edge]].add(edge_weight(p, edge) * ALPHA**2)
        return s._replace(q=q, active=s.active.at[idx].set(False), rho=s.rho.at[idx].set(0.0))

    def firing(s):
        i = idx
        c = s.counts[i]
        obs = jax.lax.cond(c < NCYC, lambda o: o.at[i, c].set(s.t), lambda o: o, s.obs)
        phi = s.phi.at[i].add(-TWO_PI)
        q = s.q.at[i].add(ALPHA**2)
        active = s.active.at[slot0].set(True).at[slot1].set(True)
        edge_id = s.edge_id.at[slot0].set(3 * i + 1).at[slot1].set(3 * i + 2)
        rho = s.rho.at[slot0].set(1.0).at[slot1].set(1.0)
        return s._replace(
            phi=phi, q=q, active=active, edge_id=edge_id, rho=rho,
            counts=s.counts.at[i].add(1), obs=obs,
        )

    return jax.lax.cond(kind == KIND_A, arrival, firing, st)


def replay(theta, tok):
    p, tau = theta[:2]
    st = jstate(theta)
    def body(k, s):
        kind, idx, guess = tok.kind[k], tok.idx[k], tok.guess[k]
        ft, at = candidate_times(s, tau, guess)
        dt = jnp.where(kind == KIND_F, ft[idx], at[idx])
        s = advance(s, dt, tau)
        return process_one(s, p, kind, idx, tok.slot0[k], tok.slot1[k])
    st = jax.lax.fori_loop(0, tok.kind.shape[0], body, st)
    return jnp.stack([st.obs[i, c] for i, c in LABELS])


def design_stats(J, inds, sigma=SIGMA_T):
    JJ = J[list(inds)]
    sv = np.linalg.svd(JJ, compute_uv=False)
    rank = np.linalg.matrix_rank(JJ, 1.0e-10)
    if rank < JJ.shape[1]:
        return dict(rank=rank, singular_values=sv, sigma_min=0.0, logdet=-np.inf, trace_cov=np.inf)
    gram = JJ.T @ JJ
    sign, logdet = np.linalg.slogdet(gram)
    cov = sigma**2 * np.linalg.inv(gram)
    return dict(
        rank=rank, singular_values=sv, sigma_min=float(sv[-1]),
        logdet=float(logdet if sign > 0 else -np.inf),
        trace_cov=float(np.trace(cov)), std=np.sqrt(np.diag(cov)),
        corr=cov / np.outer(np.sqrt(np.diag(cov)), np.sqrt(np.diag(cov))),
    )


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


def fixed_fd_jac(theta, tok, h=1.0e-6):
    cols = []
    theta = np.asarray(theta, float)
    for j in range(4):
        d = np.zeros(4); d[j] = 1.0
        yp = np.asarray(replay(jnp.asarray(theta + h * d), tok))
        ym = np.asarray(replay(jnp.asarray(theta - h * d), tok))
        cols.append((yp - ym) / (2.0 * h))
    return np.column_stack(cols)


def benchmark_checks():
    tok, y, margins, event_of_label = record_truth_chart()
    replay_fun = jax.jit(lambda th: replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay(th, tok)))
    theta = jnp.asarray(THETA_TRUE)
    yj = np.asarray(replay_fun(theta))
    assert np.max(np.abs(yj - y)) < 2.0e-12
    J = np.asarray(jac_fun(theta))
    Jfd = fixed_fd_jac(THETA_TRUE, tok)
    rel = float(np.linalg.norm(J - Jfd) / np.linalg.norm(Jfd))
    assert rel < 1.0e-8

    baseline = design_stats(J, BASELINE6)
    assert abs(baseline["sigma_min"] - 0.10170597626076935) < 2.0e-10

    e4 = best_subset(J, range(12), 4, "E")
    e5 = best_subset(J, range(12), 5, "E")
    e6 = best_subset(J, range(12), 6, "E")
    d6 = best_subset(J, range(12), 6, "D")
    a6 = best_subset(J, range(12), 6, "A")
    assert e4[1] == (1, 2, 9, 11)
    assert e6[1] == (1, 2, 3, 4, 9, 11)
    assert d6[1] == (1, 2, 7, 9, 10, 11)
    assert a6[1] == e6[1]
    assert e6[2]["sigma_min"] / baseline["sigma_min"] > 3.0

    horizon = {}
    for cycles in (2, 3, 4):
        available = [i for i, (_, c) in enumerate(LABELS) if c < cycles]
        horizon[cycles] = best_subset(J, available, min(6, len(available)), "E")
    assert horizon[2][2]["sigma_min"] < 0.102
    assert horizon[3][2]["sigma_min"] > 0.204
    assert horizon[4][2]["sigma_min"] > 0.308

    baseline_last_event = max(event_of_label[LABELS[i]] for i in BASELINE6)
    e6_last_event = max(event_of_label[LABELS[i]] for i in e6[1])
    baseline_margin = float(np.min(margins[:baseline_last_event + 1]))
    e6_margin = float(np.min(margins[:e6_last_event + 1]))
    assert abs(e6_margin - baseline_margin) < 2.0e-13

    neuron_restrictions = {}
    for nodes in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
        inds = [i for i, (n, _) in enumerate(LABELS) if n in nodes]
        neuron_restrictions[nodes] = design_stats(J, inds)
    assert all(neuron_restrictions[(i,)]["rank"] == 4 for i in range(3))
    assert max(neuron_restrictions[(i,)]["sigma_min"] for i in range(3)) < 0.03
    assert neuron_restrictions[(0, 2)]["sigma_min"] > 0.23

    Jclock = np.column_stack([J, np.ones(12)])
    clock_e6 = best_subset(Jclock, range(12), 6, "E")
    clock_d6 = best_subset(Jclock, range(12), 6, "D")
    assert clock_e6[1] == (0, 1, 2, 3, 9, 11)
    assert clock_e6[2]["sigma_min"] > 0.298
    assert clock_e6[2]["rank"] == 5

    return dict(
        event_count=int(tok.kind.shape[0]), truth_spikes=y, labels=LABELS,
        truth_chart_min_margin=baseline_margin, jax_fd_relative_error=rel,
        full12=design_stats(J, tuple(range(12))), baseline6=baseline,
        e_opt4=e4, e_opt5=e5, e_opt6=e6, d_opt6=d6, a_opt6=a6,
        horizon=horizon, neuron_restrictions=neuron_restrictions,
        clock_e_opt6=clock_e6, clock_d_opt6=clock_d6,
    )


def noise_direct():
    tok, _, _, _ = record_truth_chart()
    replay_fun = jax.jit(lambda th: replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay(th, tok)))
    _ = np.asarray(replay_fun(jnp.asarray(THETA_TRUE)))
    J = np.asarray(jac_fun(jnp.asarray(THETA_TRUE)))
    e6 = best_subset(J, range(12), 6, "E")[1]
    audits = []
    for name, inds, seed in (("baseline", BASELINE6, 12345), ("e_opt6", e6, 54321)):
        inds = np.asarray(inds, int)
        truth = np.asarray(replay_fun(jnp.asarray(THETA_TRUE)))[inds]
        rng, xs = np.random.default_rng(seed), []
        for _ in range(20):
            data = truth + rng.normal(scale=SIGMA_T, size=len(inds))
            sol = least_squares(
                lambda x: np.asarray(replay_fun(jnp.asarray(x)))[inds] - data,
                THETA_TRUE + np.array([0.01, -0.01, 0.001, -0.001]),
                jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[inds],
                max_nfev=20, xtol=1e-12, ftol=1e-12, gtol=1e-12,
            )
            xs.append(sol.x)
        xs = np.asarray(xs)
        audits.append((name, xs.mean(0), xs.std(0, ddof=1)))

    Jclock = np.column_stack([J, np.ones(12)])
    inds = np.asarray(best_subset(Jclock, range(12), 6, "E")[1], int)
    truth = np.asarray(replay_fun(jnp.asarray(THETA_TRUE)))[inds]
    rng, xs = np.random.default_rng(222), []
    for _ in range(20):
        data = truth + rng.normal(scale=SIGMA_T, size=len(inds))
        def fun(x):
            return np.asarray(replay_fun(jnp.asarray(x[:4])))[inds] + x[4] - data
        def jac(x):
            return np.column_stack([np.asarray(jac_fun(jnp.asarray(x[:4])))[inds], np.ones(len(inds))])
        x0 = np.r_[THETA_TRUE + np.array([0.01, -0.01, 0.001, -0.001]), 1.0e-4]
        xs.append(least_squares(fun, x0, jac=jac, max_nfev=20,
                                xtol=1e-12, ftol=1e-12, gtol=1e-12).x)
    xs = np.asarray(xs)
    audits.append(("clock_e_opt6", xs.mean(0), xs.std(0, ddof=1)))
    return audits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()
    out = benchmark_checks()
    print("CORE v0.21 observation-design checks passed")
    print("baseline6 sigma_min/std", out["baseline6"]["sigma_min"], out["baseline6"]["std"])
    print("E-opt6", out["e_opt6"][1], out["e_opt6"][2]["sigma_min"], out["e_opt6"][2]["std"])
    print("D-opt6", out["d_opt6"][1], out["d_opt6"][2]["logdet"])
    print("E-opt4", out["e_opt4"][1], out["e_opt4"][2]["sigma_min"])
    print("horizon E-opt6", {k: v[2]["sigma_min"] for k, v in out["horizon"].items()})
    print("clock E-opt6", out["clock_e_opt6"][1], out["clock_e_opt6"][2]["singular_values"], out["clock_e_opt6"][2]["std"])
    if args.noise_direct:
        for row in noise_direct():
            print("noise", row)


if __name__ == "__main__":
    main()
