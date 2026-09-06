"""CORE v0.24 — active pulse experiment design with spike-time-only readout.

The six-dimensional inverse problem from v0.22 is retained:
    theta = (p, tau3, eta1, eta2, xi_psi, xi_q).

A known pre-event pulse is applied at fixed time t_p:
    psi^+ = psi^- + A cos(beta) d(gamma)
    q^+   = q^-   + A sin(beta) d(gamma)

with zero-mean spatial direction
    d(gamma) = cos(gamma) v1 + sin(gamma) v2,
    v1=(2,-1,-1)/sqrt(6), v2=(0,1,-1)/sqrt(2).

Only labelled spike times are observed after the pulse. The default benchmark checks
the constrained reference pulse, chart safety, JAX/FD agreement, information gain,
joint spike subset design, and rejection of the v0.22 weak direction/alias.
Optional modes rerun the constrained pulse optimization, multistart recovery, and
small-noise audits.
"""
from __future__ import annotations

import argparse
import itertools
import math
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import least_squares, minimize

import core_v022_latent_synaptic_state as v22

jax.config.update("jax_enable_x64", True)

SIGMA_T = 1.0e-4
A_MAX = 0.12
MARGIN_MIN = 0.05
V1 = np.asarray(v22.SYNAPTIC_MODE, float)
V2 = np.array([0.0, 1.0, -1.0]) / math.sqrt(2.0)
V1J = jnp.asarray(V1)
V2J = jnp.asarray(V2)

# (t_p, A, gamma, beta)
PULSE_REF = np.array([
    0.017411818295092,
    0.12,
    -0.100648763423705,
    0.524490031205894,
])

WEAK_V022 = np.array([
    -0.0004136503499338386, -0.0007066283199000029,
    -0.5482714311676711, 0.27420530916575925,
    0.7863479906534645, -0.07659016487597305,
])
ALIAS_V022 = np.array([
    -3.267999605293241, 7.999965530031933,
    -0.004377403087449034, 0.002189830412793823,
    0.006090917284445635, -0.0005068021586924667,
])


def pulse_direction(gamma: float) -> np.ndarray:
    return math.cos(gamma) * V1 + math.sin(gamma) * V2


def pulse_components(pulse):
    tp, amp, gamma, beta = map(float, pulse)
    d = pulse_direction(gamma)
    return amp * math.cos(beta) * d, amp * math.sin(beta) * d


def signature(tok):
    return tuple(zip(np.asarray(tok.kind).tolist(), np.asarray(tok.idx).tolist()))


def record_pulse_chart(theta=v22.THETA_TRUE, pulse=PULSE_REF):
    """Physical NumPy scheduler with one fixed-time pulse inserted before first event."""
    theta = np.asarray(theta, float)
    p, tau = map(float, theta[:2])
    tp, amp, gamma, beta = map(float, pulse)
    st = v22.np_state(theta)
    counts = np.zeros(v22.v21.N, int)
    obs = np.full((v22.v21.N, v22.v21.NCYC), np.nan)
    rows, margins = [], []
    pulse_done = False
    dpsi, dq = pulse_components(pulse)

    while np.min(counts) < v22.v21.NCYC:
        ft = np.array([
            v22.v21.firing_time_np(st.psi[i], st.q[i], st.phi[i])
            for i in range(v22.v21.N)
        ])
        at = np.full(v22.v21.QMAX, np.inf)
        for k in np.where(st.active)[0]:
            edge = st.edge_id[k]
            speed = 0.5 if v22.v21.MODE[edge] == 1 else 1.0 / tau
            at[k] = st.rho[k] / speed
        fi, ai = int(np.argmin(ft)), int(np.argmin(at))
        if ft[fi] <= at[ai]:
            kind, idx, dt = v22.v21.KIND_F, fi, ft[fi]
            competitor = min(np.min(np.delete(ft, fi)), np.min(at))
        else:
            kind, idx, dt = v22.v21.KIND_A, ai, at[ai]
            competitor = min(np.min(ft), np.min(np.delete(at, ai)))

        if (not pulse_done) and st.t < tp < st.t + dt - 1.0e-12:
            v22.v21.advance_np(st, tp - st.t, tau)
            st.psi = st.psi + dpsi
            st.q = st.q + dq
            pulse_done = True
            continue

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
        jnp.asarray(a[:, 0], jnp.int32),
        jnp.asarray(a[:, 1], jnp.int32),
        jnp.asarray(a[:, 2], jnp.float64),
        jnp.asarray(a[:, 3], jnp.int32),
        jnp.asarray(a[:, 4], jnp.int32),
    )
    y = np.array([obs[i, c] for c in range(v22.v21.NCYC) for i in range(v22.v21.N)])
    return tok, y, np.asarray(margins)


def replay_pulse(theta, pulse, tok):
    """Fixed-chart JAX replay. The pulse is a known fixed-time additive reset."""
    p, tau = theta[:2]
    tp, amp, gamma, beta = pulse
    st = v22.jstate(theta)
    st = v22.v21.advance(st, tp, tau)
    d = jnp.cos(gamma) * V1J + jnp.sin(gamma) * V2J
    st = st._replace(
        psi=st.psi + amp * jnp.cos(beta) * d,
        q=st.q + amp * jnp.sin(beta) * d,
    )

    def body(k, s):
        kind, idx, guess = tok.kind[k], tok.idx[k], tok.guess[k]
        ft, at = v22.v21.candidate_times(s, tau, guess)
        dt = jnp.where(kind == v22.v21.KIND_F, ft[idx], at[idx])
        s = v22.v21.advance(s, dt, tau)
        return v22.v21.process_one(s, p, kind, idx, tok.slot0[k], tok.slot1[k])

    st = jax.lax.fori_loop(0, tok.kind.shape[0], body, st)
    return jnp.stack([st.obs[i, c] for c in range(v22.v21.NCYC) for i in range(v22.v21.N)])


def fixed_fd_jac(theta, pulse, tok, h=1.0e-6):
    theta = np.asarray(theta, float)
    cols = []
    for j in range(6):
        d = np.zeros(6); d[j] = h
        yp = np.asarray(replay_pulse(jnp.asarray(theta + d), jnp.asarray(pulse), tok))
        ym = np.asarray(replay_pulse(jnp.asarray(theta - d), jnp.asarray(pulse), tok))
        cols.append((yp - ym) / (2.0 * h))
    return np.column_stack(cols)


def design_stats(J, inds, sigma=SIGMA_T):
    A = J[list(inds)]
    sv = np.linalg.svd(A, compute_uv=False)
    rank = np.linalg.matrix_rank(A, 1.0e-10)
    if rank < 6:
        return dict(rank=rank, sigma_min=0.0, singular_values=sv)
    cov = sigma**2 * np.linalg.inv(A.T @ A)
    sign, logdet = np.linalg.slogdet(A.T @ A)
    return dict(rank=rank, sigma_min=float(sv[-1]), singular_values=sv,
                condition_number=float(sv[0] / sv[-1]),
                std=np.sqrt(np.diag(cov)),
                logdet=float(logdet if sign > 0 else -np.inf))


def best_subset(J, k, criterion="E"):
    best = None
    for inds in itertools.combinations(range(12), k):
        st = design_stats(J, inds)
        if st["rank"] < 6:
            continue
        score = st["sigma_min"] if criterion == "E" else st["logdet"]
        if best is None or score > best[0]:
            best = (score, inds, st)
    return best


def benchmark_checks():
    base_tok, _, _, _ = v22.record_chart()
    tok, y, margins = record_pulse_chart(v22.THETA_TRUE, PULSE_REF)
    assert signature(tok) == signature(base_tok)
    assert abs(float(np.min(margins)) - MARGIN_MIN) < 2.0e-8

    f = jax.jit(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok))
    jf = jax.jit(jax.jacfwd(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok)))
    yj = np.asarray(f(jnp.asarray(v22.THETA_TRUE)))
    assert np.max(np.abs(yj - y)) < 2.0e-12
    J = np.asarray(jf(jnp.asarray(v22.THETA_TRUE)))
    Jfd = fixed_fd_jac(v22.THETA_TRUE, PULSE_REF, tok)
    rel = float(np.linalg.norm(J - Jfd) / np.linalg.norm(Jfd))
    assert rel < 1.0e-8

    J0 = np.asarray(jax.jacfwd(lambda th: v22.replay(th, base_tok))(jnp.asarray(v22.THETA_TRUE)))
    s0 = np.linalg.svd(J0, compute_uv=False)
    sp = np.linalg.svd(J, compute_uv=False)
    gain = float(sp[-1] / s0[-1])
    assert gain > 100.0
    assert abs(sp[-1] - 0.091761628357647) < 2.0e-8

    full = design_stats(J, tuple(range(12)))
    e6 = best_subset(J, 6, "E")
    d6 = best_subset(J, 6, "D")
    assert e6[1] == (0, 1, 2, 3, 10, 11)
    assert d6[1] == (0, 1, 2, 9, 10, 11)
    assert e6[2]["sigma_min"] > 0.085

    thw = v22.THETA_TRUE + 0.01 * WEAK_V022
    _, yw, mw = record_pulse_chart(thw, PULSE_REF)
    _, ya, ma = record_pulse_chart(ALIAS_V022, PULSE_REF)
    weak_sigma = float(np.linalg.norm(yw - y) / SIGMA_T)
    alias_sigma = float(np.linalg.norm(ya - y) / SIGMA_T)
    assert weak_sigma > 24.0
    assert alias_sigma > 19.0
    assert np.min(mw) > MARGIN_MIN and np.min(ma) > MARGIN_MIN

    amp_curve = []
    for amp in (0.02, 0.04, 0.06, 0.08, 0.10, 0.12):
        pulse = PULSE_REF.copy(); pulse[1] = amp
        tka, _, ma = record_pulse_chart(v22.THETA_TRUE, pulse)
        Ja = np.asarray(jax.jacfwd(lambda th: replay_pulse(th, jnp.asarray(pulse), tka))
                        (jnp.asarray(v22.THETA_TRUE)))
        amp_curve.append((amp, float(np.linalg.svd(Ja, compute_uv=False)[-1]), float(np.min(ma))))
    assert all(amp_curve[i+1][1] > amp_curve[i][1] for i in range(len(amp_curve)-1))
    assert all(m >= MARGIN_MIN - 1.0e-10 for _, _, m in amp_curve)

    return dict(
        pulse=PULSE_REF.copy(), pulse_direction=pulse_direction(PULSE_REF[2]),
        pulse_components=pulse_components(PULSE_REF),
        truth_spikes=y, chart_margin=float(np.min(margins)),
        jax_fd_relative_error=rel,
        spike_only_singular_values=s0, pulsed_singular_values=sp,
        information_gain=gain, full12=full, e_opt6=e6, d_opt6=d6,
        weak_rejection_sigma=weak_sigma, alias_rejection_sigma=alias_sigma,
        amplitude_curve=amp_curve,
    )


def optimize_direct():
    """Reproduce the constrained reference optimum from multiple starts."""
    base_tok, _, _, _ = v22.record_chart()
    base_sig = signature(base_tok)

    jac_pulse = jax.jit(jax.jacfwd(
        lambda th, pulse: replay_pulse(th, pulse, base_tok), argnums=0
    ))
    _ = np.asarray(jac_pulse(jnp.asarray(v22.THETA_TRUE), jnp.asarray(PULSE_REF)))

    def objective(x):
        J = np.asarray(jac_pulse(jnp.asarray(v22.THETA_TRUE), jnp.asarray(x)))
        return -float(np.linalg.svd(J, compute_uv=False)[-1])

    def margin_constraint(x):
        tok, _, margins = record_pulse_chart(v22.THETA_TRUE, x)
        if signature(tok) != base_sig:
            return -0.1
        return float(np.min(margins) - MARGIN_MIN)

    starts = [
        [0.10, 0.08, 0.0, 0.0],
        [0.30, 0.10, -0.2, 0.3],
        [0.05, 0.12, 0.1, 0.5],
        [0.50, 0.08, 0.3, -0.2],
        [0.05, 0.10, -0.1, 0.6],
    ]
    sols = []
    for x0 in starts:
        sol = minimize(
            objective, x0, method="SLSQP",
            bounds=[(0.001, 2.0), (0.001, A_MAX),
                    (-math.pi, math.pi), (-math.pi/2, math.pi/2)],
            constraints=[{"type": "ineq", "fun": margin_constraint}],
            options={"maxiter": 120, "ftol": 1.0e-11},
        )
        sols.append(sol)
    assert all(s.success for s in sols)
    assert all(-s.fun > 0.0917 for s in sols)
    assert all(abs(s.x[1] - A_MAX) < 1.0e-8 for s in sols)
    assert max(np.linalg.norm(s.x - sols[0].x) for s in sols[1:]) < 4.0e-6
    return sols


def multistart_direct():
    tok, y, _ = record_pulse_chart(v22.THETA_TRUE, PULSE_REF)
    f = jax.jit(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok))
    jf = jax.jit(jax.jacfwd(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok)))
    J = np.asarray(jf(jnp.asarray(v22.THETA_TRUE)))
    e6 = best_subset(J, 6, "E")[1]

    rng = np.random.default_rng(20260906)
    starts = [
        v22.THETA_TRUE + rng.normal(size=6) *
        np.array([0.02, 0.02, 0.005, 0.005, 0.008, 0.002])
        for _ in range(12)
    ]
    result = {}
    for name, inds in (("E6", e6), ("FULL12", tuple(range(12)))):
        ii = np.asarray(inds, int)
        dists = []
        for x0 in starts:
            sol = least_squares(
                lambda x: np.asarray(f(jnp.asarray(x)))[ii] - y[ii], x0,
                jac=lambda x: np.asarray(jf(jnp.asarray(x)))[ii],
                max_nfev=80, xtol=1e-13, ftol=1e-13, gtol=1e-13,
            )
            dists.append(np.linalg.norm(sol.x - v22.THETA_TRUE))
        result[name] = np.asarray(dists)
        assert np.sum(result[name] < 1.0e-6) == 12
    return result


def noise_direct():
    tok, y, _ = record_pulse_chart(v22.THETA_TRUE, PULSE_REF)
    f = jax.jit(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok))
    jf = jax.jit(jax.jacfwd(lambda th: replay_pulse(th, jnp.asarray(PULSE_REF), tok)))
    J = np.asarray(jf(jnp.asarray(v22.THETA_TRUE)))
    e6 = best_subset(J, 6, "E")[1]
    audits = []
    for name, inds, seed in (("E6", e6, 20260909), ("FULL12", tuple(range(12)), 20260910)):
        ii = np.asarray(inds, int)
        A = J[ii]
        fisher = SIGMA_T * np.sqrt(np.diag(np.linalg.inv(A.T @ A)))
        rng = np.random.default_rng(seed)
        xs = []
        for _ in range(30):
            data = y[ii] + rng.normal(scale=SIGMA_T, size=len(ii))
            x0 = v22.THETA_TRUE + np.array([1e-3, -1e-3, 2e-4, -2e-4, 3e-4, -1e-4])
            sol = least_squares(
                lambda x: np.asarray(f(jnp.asarray(x)))[ii] - data, x0,
                jac=lambda x: np.asarray(jf(jnp.asarray(x)))[ii],
                max_nfev=50, xtol=1e-12, ftol=1e-12, gtol=1e-12,
            )
            xs.append(sol.x)
        xs = np.asarray(xs)
        empirical = xs.std(0, ddof=1)
        ratio = empirical / fisher
        assert np.all(ratio > 0.9) and np.all(ratio < 1.2)
        audits.append((name, xs.mean(0), empirical, fisher, ratio))
    return audits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--optimize-direct", action="store_true")
    ap.add_argument("--multistart-direct", action="store_true")
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()

    out = benchmark_checks()
    print("CORE v0.24 active-pulse checks passed")
    print("pulse", out["pulse"])
    print("margin", out["chart_margin"])
    print("sigma_min/gain", out["pulsed_singular_values"][-1], out["information_gain"])
    print("E-opt6", out["e_opt6"][1], out["e_opt6"][2]["sigma_min"])
    print("weak/alias rejection sigma", out["weak_rejection_sigma"], out["alias_rejection_sigma"])
    if args.optimize_direct:
        for s in optimize_direct():
            print("opt", s.fun, s.x)
    if args.multistart_direct:
        print("multistart", multistart_direct())
    if args.noise_direct:
        for row in noise_direct():
            print("noise", row)


if __name__ == "__main__":
    main()
