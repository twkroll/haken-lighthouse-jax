"""CORE v0.25 — full real q=1 latent synaptic state from two active trials.

Unknown block:
    theta=(p,tau3,eta1,eta2,xi_psi1,xi_psi2,xi_q1,xi_q2).

Both trials share the same reproducibly prepared unknown initial state.  Each
trial uses the chart-safe v0.24 pulse family and observes labelled spike times
only.  P1 is exactly the v0.24 reference; P2 is a rounded complementary probe.

Default checks local rank/conditioning, physical-vs-JAX derivatives, duplicate
trial controls, stacked two-probe information, the stored minimal eight-spike
design, and the refined P2 safety-boundary audit.  Optional modes rerun the
expensive exhaustive C(24,8) design search, nonlinear multistart recovery, and
noise audits.
"""
from __future__ import annotations

import argparse
import itertools
import math
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import brentq, least_squares

import core_v024_active_pulse_design as v24

jax.config.update("jax_enable_x64", True)

V1 = v24.v22.SYNAPTIC_MODE
V1J = v24.v22.SYNAPTIC_MODE_J
V2 = v24.V2
V2J = v24.V2J

THETA_TRUE = np.array([
    v24.v22.v21.P_TRUE, v24.v22.v21.TAU_TRUE,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
])
SIGMA_T = 1.0e-4
MIN_MARGIN = 0.06
P1 = (0.05, 0.1, 0.55, -0.1)
P2 = (0.05, 0.1, 0.20, 3.02)
E8_GLOBAL = (1, 5, 6, 7, 12, 16, 21, 23)


def np_state8(theta):
    th = np.asarray(theta, float)
    psi = v24.v22.v21.PSI0 + th[4] * V1 + th[5] * V2
    q = v24.v22.v21.Q0 + th[6] * V1 + th[7] * V2
    phi = v24.v22.v21.PHI_BASE + v24.v22.v21.LATENT_B @ th[2:4]
    return v24.v22.v21.NPState(
        0.0, psi.copy(), q.copy(), phi.copy(),
        np.zeros(v24.v22.v21.QMAX, bool),
        np.zeros(v24.v22.v21.QMAX, int),
        np.zeros(v24.v22.v21.QMAX),
    )


def record_chart8(theta=THETA_TRUE, pulse=P1):
    """Physical scheduler for one eight-unknown known-pulse experiment."""
    th = np.asarray(theta, float)
    p, tau = map(float, th[:2])
    tp, amp, beta, gamma = pulse
    st = np_state8(th)

    # The pulse must occur before the first natural event.
    ft0 = np.array([
        v24.v22.v21.firing_time_np(st.psi[i], st.q[i], st.phi[i])
        for i in range(v24.v22.v21.N)
    ])
    pre_margin = float(np.min(ft0) - tp)
    if pre_margin <= 0.0:
        raise RuntimeError("pulse is not pre-event")

    v24.v22.v21.advance_np(st, tp, tau)
    v24.pulse_np(st, amp, beta, gamma)

    counts = np.zeros(v24.v22.v21.N, int)
    obs = np.full((v24.v22.v21.N, v24.v22.v21.NCYC), np.nan)
    rows, margins = [], []

    while np.min(counts) < v24.v22.v21.NCYC:
        ft = np.array([
            v24.v22.v21.firing_time_np(st.psi[i], st.q[i], st.phi[i])
            for i in range(v24.v22.v21.N)
        ])
        at = np.full(v24.v22.v21.QMAX, np.inf)
        for k in np.where(st.active)[0]:
            edge = st.edge_id[k]
            speed = 0.5 if v24.v22.v21.MODE[edge] == 1 else 1.0 / tau
            at[k] = st.rho[k] / speed

        fi, ai = int(np.argmin(ft)), int(np.argmin(at))
        if ft[fi] <= at[ai]:
            kind, idx, dt = v24.v22.v21.KIND_F, fi, ft[fi]
            competitor = min(np.min(np.delete(ft, fi)), np.min(at))
        else:
            kind, idx, dt = v24.v22.v21.KIND_A, ai, at[ai]
            competitor = min(np.min(ft), np.min(np.delete(at, ai)))
        margins.append(competitor - dt)
        v24.v22.v21.advance_np(st, dt, tau)

        if kind == v24.v22.v21.KIND_A:
            edge = int(st.edge_id[idx])
            st.q[v24.v22.v21.TARGET[edge]] += (
                v24.v22.v21.edge_weight_np(p, edge) * v24.v22.v21.ALPHA**2
            )
            st.active[idx] = False
            st.rho[idx] = 0.0
            rows.append((kind, idx, dt, 0, 0))
        else:
            i, cyc = idx, int(counts[idx])
            st.phi[i] -= v24.v22.v21.TWO_PI
            st.q[i] += v24.v22.v21.ALPHA**2
            free = np.where(~st.active)[0][:2]
            for slot, edge in zip(free, (3 * i + 1, 3 * i + 2)):
                st.active[slot] = True
                st.edge_id[slot] = edge
                st.rho[slot] = 1.0
            if cyc < v24.v22.v21.NCYC:
                obs[i, cyc] = st.t
            counts[i] += 1
            rows.append((kind, i, dt, int(free[0]), int(free[1])))

    a = np.asarray(rows)
    tok = v24.v22.v21.Tokens(
        jnp.asarray(a[:, 0], jnp.int32),
        jnp.asarray(a[:, 1], jnp.int32),
        jnp.asarray(a[:, 2], jnp.float64),
        jnp.asarray(a[:, 3], jnp.int32),
        jnp.asarray(a[:, 4], jnp.int32),
    )
    y = np.array([obs[i, c] for i, c in v24.v22.v21.LABELS])
    return tok, y, np.asarray(margins), pre_margin


def jstate8(theta, pulse):
    tp, amp, beta, gamma = pulse
    psi = jnp.asarray(v24.v22.v21.PSI0) + theta[4] * V1J + theta[5] * V2J
    q = jnp.asarray(v24.v22.v21.Q0) + theta[6] * V1J + theta[7] * V2J
    phi = jnp.asarray(v24.v22.v21.PHI_BASE) + v24.v22.v21.LATENT_BJ @ theta[2:4]
    st = v24.v22.v21.JState(
        jnp.array(0.0), psi, q, phi,
        jnp.zeros(v24.v22.v21.QMAX, bool),
        jnp.zeros(v24.v22.v21.QMAX, jnp.int32),
        jnp.zeros(v24.v22.v21.QMAX),
        jnp.zeros(v24.v22.v21.N, jnp.int32),
        jnp.full((v24.v22.v21.N, v24.v22.v21.NCYC), jnp.nan),
    )
    st = v24.v22.v21.advance(st, tp, theta[1])
    return v24.pulse_jax(st, amp, beta, gamma)


def replay8(theta, tok, pulse):
    p, tau = theta[:2]
    st = jstate8(theta, pulse)

    def body(k, s):
        kind, idx, guess = tok.kind[k], tok.idx[k], tok.guess[k]
        ft, at = v24.v22.v21.candidate_times(s, tau, guess)
        dt = jnp.where(kind == v24.v22.v21.KIND_F, ft[idx], at[idx])
        s = v24.v22.v21.advance(s, dt, tau)
        return v24.v22.v21.process_one(
            s, p, kind, idx, tok.slot0[k], tok.slot1[k]
        )

    st = jax.lax.fori_loop(0, tok.kind.shape[0], body, st)
    return jnp.stack([st.obs[i, c] for i, c in v24.v22.v21.LABELS])


def stats(A, sigma=SIGMA_T):
    sv = np.linalg.svd(A, compute_uv=False)
    rank = np.linalg.matrix_rank(A, 1.0e-10)
    out = dict(rank=rank, singular_values=sv, sigma_min=float(sv[-1]))
    if rank == A.shape[1]:
        out["condition_number"] = float(sv[0] / sv[-1])
        out["std"] = sigma * np.sqrt(np.diag(np.linalg.inv(A.T @ A)))
    return out


def experiment(pulse):
    tok, y, margins, pre = record_chart8(THETA_TRUE, pulse)
    replay_fun = jax.jit(lambda th: replay8(th, tok, pulse))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay8(th, tok, pulse)))
    theta = jnp.asarray(THETA_TRUE)
    yj = np.asarray(replay_fun(theta))
    J = np.asarray(jac_fun(theta))
    return dict(
        pulse=pulse, tok=tok, y=y, margins=margins, pre_margin=pre,
        replay_fun=replay_fun, jac_fun=jac_fun, J=J,
        replay_error=float(np.max(np.abs(yj - y))),
        margin=min(pre, float(np.min(margins))), stats=stats(J),
    )


def physical_fd(exp, h=1.0e-6):
    cols = []
    sig0 = v24.v22.signature(exp["tok"])
    for j in range(8):
        d = np.zeros(8); d[j] = h
        tp = record_chart8(THETA_TRUE + d, exp["pulse"])
        tm = record_chart8(THETA_TRUE - d, exp["pulse"])
        assert v24.v22.signature(tp[0]) == sig0
        assert v24.v22.signature(tm[0]) == sig0
        cols.append((tp[1] - tm[1]) / (2.0 * h))
    return np.column_stack(cols)


def refined_p2_boundary(e1):
    """At beta=0.2 find the nearby gamma with physical margin exactly 0.06."""
    def margin_minus_floor(gamma):
        _, _, margins, pre = record_chart8(THETA_TRUE, (0.05, 0.1, 0.2, gamma))
        return min(pre, float(np.min(margins))) - MIN_MARGIN

    gamma = brentq(margin_minus_floor, 3.02, 3.05, xtol=1.0e-12)
    e2 = experiment((0.05, 0.1, 0.2, gamma))
    s = stats(np.vstack([e1["J"], e2["J"]))["sigma_min"]
    return gamma, e2["margin"], s


def best8_direct(J):
    best = None
    for inds in itertools.combinations(range(24), 8):
        st = stats(J[list(inds)])
        if st["rank"] < 8:
            continue
        if best is None or st["sigma_min"] > best[0]:
            best = (st["sigma_min"], inds, st)
    return best


def benchmark_checks():
    e1, e2 = experiment(P1), experiment(P2)
    assert e1["replay_error"] < 1.0e-11 and e2["replay_error"] < 1.0e-11
    assert e1["margin"] > MIN_MARGIN and e2["margin"] > MIN_MARGIN
    assert int(e1["tok"].kind.shape[0]) == 30 and int(e2["tok"].kind.shape[0]) == 30

    fd1, fd2 = physical_fd(e1), physical_fd(e2)
    rel1 = float(np.linalg.norm(e1["J"] - fd1) / np.linalg.norm(fd1))
    rel2 = float(np.linalg.norm(e2["J"] - fd2) / np.linalg.norm(fd2))
    assert rel1 < 1.0e-8 and rel2 < 1.0e-8

    assert e1["stats"]["rank"] == 8 and e1["stats"]["sigma_min"] < 2.0e-4

    e0 = experiment((0.05, 0.0, 0.0, 0.0))
    assert e0["stats"]["sigma_min"] < 4.0e-5

    duplicate = stats(np.vstack([e1["J"], e1["J"]]))
    unforced_plus = stats(np.vstack([e0["J"], e1["J"]]))
    stackJ = np.vstack([e1["J"], e2["J"]])
    joint = stats(stackJ)
    assert joint["rank"] == 8
    assert joint["sigma_min"] > 0.146
    assert joint["condition_number"] < 126.0
    assert joint["sigma_min"] / e1["stats"]["sigma_min"] > 780.0
    assert joint["sigma_min"] / duplicate["sigma_min"] > 550.0
    assert unforced_plus["sigma_min"] < joint["sigma_min"]

    gamma_b, margin_b, sigma_b = refined_p2_boundary(e1)
    assert abs(gamma_b - 3.0331068445422606) < 2.0e-8
    assert abs(margin_b - MIN_MARGIN) < 2.0e-10
    assert abs(sigma_b - 0.14696443913750748) < 2.0e-8
    rounded_loss = (sigma_b - joint["sigma_min"]) / sigma_b
    assert rounded_loss < 1.0e-3

    pulse_vecs = []
    for pulse in (P1, P2):
        _, amp, beta, gamma = pulse
        d = v24.direction_np(gamma)
        pulse_vecs.append(np.r_[amp * math.cos(beta) * d, amp * math.sin(beta) * d])
    cosang = float(np.dot(pulse_vecs[0], pulse_vecs[1]) /
                   (np.linalg.norm(pulse_vecs[0]) * np.linalg.norm(pulse_vecs[1])))
    angle = float(np.degrees(np.arccos(cosang)))
    assert 159.0 < angle < 161.0

    e8 = stats(stackJ[list(E8_GLOBAL)])
    assert e8["rank"] == 8 and e8["sigma_min"] > 0.0936

    return dict(
        p1=e1, p2=e2, rel_fd_p1=rel1, rel_fd_p2=rel2,
        unforced=e0, duplicate_p1=duplicate, unforced_plus_p1=unforced_plus,
        joint=joint, refined_boundary=(gamma_b, margin_b, sigma_b, rounded_loss),
        pulse_inner_product=cosang, pulse_angle_deg=angle,
        e_opt8=dict(indices=E8_GLOBAL, stats=e8),
    )


def multistart_direct():
    e1, e2 = experiment(P1), experiment(P2)
    rng = np.random.default_rng(20260914)
    scales = np.array([0.02, 0.02, 0.005, 0.005, 0.008, 0.008, 0.002, 0.002])
    starts = [THETA_TRUE + rng.normal(size=8) * scales for _ in range(12)]
    out = {}

    for name, inds in (("FULL24", tuple(range(24))), ("E8", E8_GLOBAL)):
        inds = np.asarray(inds, int)
        i1, i2 = inds[inds < 12], inds[inds >= 12] - 12
        dists = []
        for x0 in starts:
            def fun(x):
                return np.r_[
                    np.asarray(e1["replay_fun"](jnp.asarray(x)))[i1] - e1["y"][i1],
                    np.asarray(e2["replay_fun"](jnp.asarray(x)))[i2] - e2["y"][i2],
                ]
            def jac(x):
                return np.vstack([
                    np.asarray(e1["jac_fun"](jnp.asarray(x)))[i1],
                    np.asarray(e2["jac_fun"](jnp.asarray(x)))[i2],
                ])
            sol = least_squares(fun, x0, jac=jac, max_nfev=100,
                                xtol=1e-13, ftol=1e-13, gtol=1e-13)
            dists.append(np.linalg.norm(sol.x - THETA_TRUE))
        dists = np.asarray(dists)
        assert np.sum(dists < 1.0e-6) == 12
        out[name] = dists
    return out


def noise_direct(realizations=50):
    e1, e2 = experiment(P1), experiment(P2)
    out = {}
    for name, inds, seed in (
        ("FULL24", tuple(range(24)), 20260915),
        ("E8", E8_GLOBAL, 20260916),
    ):
        inds = np.asarray(inds, int)
        i1, i2 = inds[inds < 12], inds[inds >= 12] - 12
        M = np.vstack([e1["J"][i1], e2["J"][i2]])
        fisher = SIGMA_T * np.sqrt(np.diag(np.linalg.inv(M.T @ M)))
        rng = np.random.default_rng(seed)
        xs = []
        for _ in range(realizations):
            data1 = e1["y"][i1] + rng.normal(scale=SIGMA_T, size=len(i1))
            data2 = e2["y"][i2] + rng.normal(scale=SIGMA_T, size=len(i2))
            x0 = THETA_TRUE + np.array([
                2e-4, -2e-4, 2e-4, -2e-4, 2e-4, -2e-4, 1e-4, -1e-4,
            ])
            def fun(x):
                return np.r_[
                    (np.asarray(e1["replay_fun"](jnp.asarray(x)))[i1] - data1) / SIGMA_T,
                    (np.asarray(e2["replay_fun"](jnp.asarray(x)))[i2] - data2) / SIGMA_T,
                ]
            def jac(x):
                return np.vstack([
                    np.asarray(e1["jac_fun"](jnp.asarray(x)))[i1],
                    np.asarray(e2["jac_fun"](jnp.asarray(x)))[i2],
                ]) / SIGMA_T
            sol = least_squares(fun, x0, jac=jac, max_nfev=80,
                                xtol=1e-12, ftol=1e-12, gtol=1e-12)
            xs.append(sol.x)
        xs = np.asarray(xs)
        empirical = xs.std(0, ddof=1)
        ratio = empirical / fisher
        assert np.all(ratio > 0.90) and np.all(ratio < 1.21)
        out[name] = dict(mean=xs.mean(0), empirical_std=empirical,
                         fisher_std=fisher, ratio=ratio)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--design-direct", action="store_true")
    ap.add_argument("--multistart-direct", action="store_true")
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()

    out = benchmark_checks()
    print("CORE v0.25 full-q1 two-probe checks passed")
    print("margins", out["p1"]["margin"], out["p2"]["margin"])
    print("single P1 sigma", out["p1"]["stats"]["sigma_min"])
    print("duplicate P1 sigma", out["duplicate_p1"]["sigma_min"])
    print("joint singular values", out["joint"]["singular_values"])
    print("joint condition", out["joint"]["condition_number"])
    print("E8", out["e_opt8"])
    print("refined boundary", out["refined_boundary"])

    if args.design_direct:
        e1, e2 = out["p1"], out["p2"]
        best = best8_direct(np.vstack([e1["J"], e2["J"]]))
        assert best[1] == E8_GLOBAL
        print("exact global E8", best)
    if args.multistart_direct:
        print("multistart", multistart_direct())
    if args.noise_direct:
        print("noise", noise_direct())


if __name__ == "__main__":
    main()
