"""CORE v0.24 — chart-safe active pulse design using spike times only.

The six-dimensional unknown block is inherited from v0.22:
    theta=(p,tau3,eta1,eta2,xi_psi,xi_q).

A known pre-event pulse applies
    psi += A*cos(beta)*d(gamma)
    q   += A*sin(beta)*d(gamma)
with d(gamma)=cos(gamma)*v1+sin(gamma)*v2.

The rounded reference design is deliberately interior to the hard hybrid-safety
constraint. The default checks truth replay, fixed-chart JAX derivatives,
conditioning, the E-optimal six-spike subset, and rejection of the v0.22 weak
direction / nonlinear alias. Optional modes rerun multistart and noise audits.
"""
from __future__ import annotations

import argparse
import itertools
import math
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import least_squares

import core_v022_latent_synaptic_state as v22

jax.config.update("jax_enable_x64", True)

TP = 0.05
AMP = 0.1
BETA = 0.55
GAMMA = -0.1
SIGMA_T = 1.0e-4
MIN_MARGIN = 0.06
SPIKE_ONLY_SIGMA_MIN = 9.137484227978426e-4
E6 = (0, 1, 2, 3, 10, 11)
V2 = np.array([0.0, 1.0, -1.0]) / math.sqrt(2.0)
V2J = jnp.asarray(V2)

V022_WEAK = np.array([
    -0.0004136503499338386, -0.0007066283199000029,
    -0.5482714311676711, 0.27420530916575925,
    0.7863479906534645, -0.07659016487597305,
])
V022_ALIAS = np.array([
    -3.267999605293241, 7.999965530031933,
    -0.004377403087449034, 0.002189830412793823,
    0.006090917284445635, -0.0005068021586924667,
])


def direction_np(gamma=GAMMA):
    return math.cos(gamma) * v22.SYNAPTIC_MODE + math.sin(gamma) * V2


def direction_jax(gamma=GAMMA):
    return jnp.cos(gamma) * v22.SYNAPTIC_MODE_J + jnp.sin(gamma) * V2J


def pulse_np(st, amp=AMP, beta=BETA, gamma=GAMMA):
    d = direction_np(gamma)
    st.psi += amp * math.cos(beta) * d
    st.q += amp * math.sin(beta) * d


def pulse_jax(st, amp=AMP, beta=BETA, gamma=GAMMA):
    d = direction_jax(gamma)
    return st._replace(
        psi=st.psi + amp * jnp.cos(beta) * d,
        q=st.q + amp * jnp.sin(beta) * d,
    )


def record_pulsed_chart(theta=v22.THETA_TRUE, tp=TP, amp=AMP, beta=BETA, gamma=GAMMA):
    """Physical scheduler for the known-pulse experiment."""
    theta = np.asarray(theta, float)
    p, tau = map(float, theta[:2])
    st = v22.np_state(theta)
    v22.v21.advance_np(st, tp, tau)
    pulse_np(st, amp, beta, gamma)

    counts = np.zeros(v22.v21.N, int)
    obs = np.full((v22.v21.N, v22.v21.NCYC), np.nan)
    rows, margins = [], []

    while np.min(counts) < v22.v21.NCYC:
        ft = np.array([
            v22.v21.firing_time_np(st.psi[i], st.q[i], st.phi[i])
            for i in range(v22.v21.N)
        ])
        at = np.full(v22.v21.QMAX, np.inf)
        for k in np.where(st.active)[0]:
            edge = st.edge_id[k]
            at[k] = st.rho[k] / (0.5 if v22.v21.MODE[edge] == 1 else 1.0 / tau)
        fi, ai = int(np.argmin(ft)), int(np.argmin(at))

        if ft[fi] <= at[ai]:
            kind, idx, dt = v22.v21.KIND_F, fi, ft[fi]
            competitor = min(np.min(np.delete(ft, fi)), np.min(at))
        else:
            kind, idx, dt = v22.v21.KIND_A, ai, at[ai]
            competitor = min(np.min(ft), np.min(np.delete(at, ai)))
        margins.append(competitor - dt)
        v22.v21.advance_np(st, dt, tau)

        if kind == v22.v21.KIND_A:
            edge = int(st.edge_id[idx])
            st.q[v22.v21.TARGET[edge]] += v22.v21.edge_weight_np(p, edge) * v22.v21.ALPHA**2
            st.active[idx] = False
            st.rho[idx] = 0.0
            rows.append((kind, idx, dt, 0, 0))
        else:
            i, cyc = idx, int(counts[idx])
            st.phi[i] -= v22.v21.TWO_PI
            st.q[i] += v22.v21.ALPHA**2
            free = np.where(~st.active)[0][:2]
            for slot, edge in zip(free, (3 * i + 1, 3 * i + 2)):
                st.active[slot] = True
                st.edge_id[slot] = edge
                st.rho[slot] = 1.0
            if cyc < v22.v21.NCYC:
                obs[i, cyc] = st.t
            counts[i] += 1
            rows.append((kind, i, dt, int(free[0]), int(free[1])))

    a = np.asarray(rows)
    tok = v22.v21.Tokens(
        jnp.asarray(a[:, 0], jnp.int32), jnp.asarray(a[:, 1], jnp.int32),
        jnp.asarray(a[:, 2], jnp.float64), jnp.asarray(a[:, 3], jnp.int32),
        jnp.asarray(a[:, 4], jnp.int32),
    )
    y = np.array([obs[i, c] for i, c in v22.v21.LABELS])
    return tok, y, np.asarray(margins)


def pulsed_jstate(theta, tp=TP, amp=AMP, beta=BETA, gamma=GAMMA):
    st = v22.jstate(theta)
    st = v22.v21.advance(st, tp, theta[1])
    return pulse_jax(st, amp, beta, gamma)


def replay_pulsed(theta, tok, tp=TP, amp=AMP, beta=BETA, gamma=GAMMA):
    p, tau = theta[:2]
    st = pulsed_jstate(theta, tp, amp, beta, gamma)

    def body(k, s):
        kind, idx, guess = tok.kind[k], tok.idx[k], tok.guess[k]
        ft, at = v22.v21.candidate_times(s, tau, guess)
        dt = jnp.where(kind == v22.v21.KIND_F, ft[idx], at[idx])
        s = v22.v21.advance(s, dt, tau)
        return v22.v21.process_one(s, p, kind, idx, tok.slot0[k], tok.slot1[k])

    st = jax.lax.fori_loop(0, tok.kind.shape[0], body, st)
    return jnp.stack([st.obs[i, c] for i, c in v22.v21.LABELS])


def fixed_fd_jac(theta, tok, h=1.0e-6):
    theta = np.asarray(theta, float)
    cols = []
    for j in range(6):
        d = np.zeros(6); d[j] = h
        yp = np.asarray(replay_pulsed(jnp.asarray(theta + d), tok))
        ym = np.asarray(replay_pulsed(jnp.asarray(theta - d), tok))
        cols.append((yp - ym) / (2.0 * h))
    return np.column_stack(cols)


def stats(A, sigma=SIGMA_T):
    sv = np.linalg.svd(A, compute_uv=False)
    rank = np.linalg.matrix_rank(A, 1.0e-10)
    if rank < 6:
        return dict(rank=rank, sigma_min=0.0)
    cov = sigma**2 * np.linalg.inv(A.T @ A)
    return dict(rank=rank, singular_values=sv, sigma_min=float(sv[-1]),
                condition_number=float(sv[0] / sv[-1]),
                std=np.sqrt(np.diag(cov)))


def best_subset(J, k):
    best = None
    for inds in itertools.combinations(range(J.shape[0]), k):
        st = stats(J[list(inds)])
        if st["rank"] < 6:
            continue
        if best is None or st["sigma_min"] > best[0]:
            best = (st["sigma_min"], inds, st)
    return best


def benchmark_checks():
    tok, y, margins = record_pulsed_chart()
    replay_fun = jax.jit(lambda th: replay_pulsed(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay_pulsed(th, tok)))
    theta = jnp.asarray(v22.THETA_TRUE)
    yj = np.asarray(replay_fun(theta))
    replay_err = float(np.max(np.abs(yj - y)))
    assert replay_err < 1.0e-11

    J = np.asarray(jac_fun(theta))
    Jfd = fixed_fd_jac(v22.THETA_TRUE, tok)
    jac_rel = float(np.linalg.norm(J - Jfd) / np.linalg.norm(Jfd))
    assert jac_rel < 1.0e-8

    full = stats(J)
    assert abs(full["sigma_min"] - 0.07955698713429293) < 2.0e-8
    assert full["sigma_min"] / SPIKE_ONLY_SIGMA_MIN > 87.0
    assert np.min(margins) > 0.0628
    assert np.min(margins) > MIN_MARGIN

    e6 = best_subset(J, 6)
    assert e6[1] == E6
    assert e6[2]["sigma_min"] > 0.0748

    truth_sig = v22.signature(tok)
    weak_theta = v22.THETA_TRUE + 0.01 * V022_WEAK
    tok_w, y_w, margins_w = record_pulsed_chart(weak_theta)
    dy_w = y_w - y
    weak_norm_sigma = float(np.linalg.norm(dy_w) / SIGMA_T)
    assert v22.signature(tok_w) == truth_sig
    assert weak_norm_sigma > 20.0
    assert np.min(margins_w) > MIN_MARGIN

    tok_a, y_a, margins_a = record_pulsed_chart(V022_ALIAS)
    dy_a = y_a - y
    alias_norm_sigma = float(np.linalg.norm(dy_a) / SIGMA_T)
    assert v22.signature(tok_a) == truth_sig
    assert alias_norm_sigma > 16.0
    assert np.min(margins_a) > MIN_MARGIN

    return dict(
        event_count=int(tok.kind.shape[0]), truth_spikes=y,
        chart_margin=float(np.min(margins)), replay_error=replay_err,
        jax_fd_relative_error=jac_rel, full12=full, e_opt6=e6,
        weak_norm_sigma=weak_norm_sigma, alias_norm_sigma=alias_norm_sigma,
        weak_margin=float(np.min(margins_w)), alias_margin=float(np.min(margins_a)),
    )


def multistart_direct():
    tok, y, _ = record_pulsed_chart()
    replay_fun = jax.jit(lambda th: replay_pulsed(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay_pulsed(th, tok)))
    rng = np.random.default_rng(20260911)
    scales = np.array([0.02, 0.02, 0.005, 0.005, 0.008, 0.002])
    starts = [v22.THETA_TRUE + rng.normal(size=6) * scales for _ in range(12)]
    out = {}
    for name, inds in (("E6", E6), ("FULL12", tuple(range(12)))):
        ii = np.asarray(inds, int); dists = []
        for x0 in starts:
            sol = least_squares(
                lambda x: np.asarray(replay_fun(jnp.asarray(x)))[ii] - y[ii], x0,
                jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[ii],
                max_nfev=80, xtol=1e-13, ftol=1e-13, gtol=1e-13,
            )
            dists.append(np.linalg.norm(sol.x - v22.THETA_TRUE))
        out[name] = np.asarray(dists)
        assert np.sum(out[name] < 1.0e-6) == 12
    return out


def noise_direct():
    tok, y, _ = record_pulsed_chart()
    replay_fun = jax.jit(lambda th: replay_pulsed(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: replay_pulsed(th, tok)))
    J = np.asarray(jac_fun(jnp.asarray(v22.THETA_TRUE)))
    audits = []
    for name, inds, seed in (("E6", E6, 20260912), ("FULL12", tuple(range(12)), 20260913)):
        ii = np.asarray(inds, int)
        A = J[ii]
        fisher = SIGMA_T * np.sqrt(np.diag(np.linalg.inv(A.T @ A)))
        rng, xs = np.random.default_rng(seed), []
        for _ in range(30):
            data = y[ii] + rng.normal(scale=SIGMA_T, size=len(ii))
            x0 = v22.THETA_TRUE + np.array([0.002, -0.002, 5e-4, -5e-4, 5e-4, -2e-4])
            sol = least_squares(
                lambda x: np.asarray(replay_fun(jnp.asarray(x)))[ii] - data, x0,
                jac=lambda x: np.asarray(jac_fun(jnp.asarray(x)))[ii],
                max_nfev=50, xtol=1e-12, ftol=1e-12, gtol=1e-12,
            )
            xs.append(sol.x)
        xs = np.asarray(xs)
        empirical = xs.std(0, ddof=1)
        audits.append((name, xs.mean(0), empirical, fisher, empirical / fisher))
    return audits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--multistart-direct", action="store_true")
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()
    out = benchmark_checks()
    print("CORE v0.24 active-pulse checks passed")
    print("chart margin", out["chart_margin"])
    print("full12", out["full12"]["singular_values"], out["full12"]["std"])
    print("gain", out["full12"]["sigma_min"] / SPIKE_ONLY_SIGMA_MIN)
    print("E-opt6", out["e_opt6"][1], out["e_opt6"][2]["sigma_min"])
    print("weak/alias sigma norms", out["weak_norm_sigma"], out["alias_norm_sigma"])
    if args.multistart_direct:
        print("multistart", multistart_direct())
    if args.noise_direct:
        for row in noise_direct():
            print("noise", row)


if __name__ == "__main__":
    main()
