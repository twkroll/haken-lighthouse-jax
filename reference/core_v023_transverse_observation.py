"""CORE v0.23 — transverse observation breaks the spike-time weak direction.

Adds one non-perturbing pre-event observable to the v0.22 six-unknown inverse
problem.  With v=(2,-1,-1)/sqrt(6), before the first hybrid event

    z_psi(t) = v^T psi(t) = exp(-alpha*t) * (xi_psi + t*xi_q).

The script optimizes the measurement time, checks the rank-one interlacing
bound, compares psi/q-only sensors, redesigns spike subsets under a mixed-noise
model, and optionally reruns nonlinear multistart/noise audits.
"""
from __future__ import annotations

import argparse
import itertools
import math
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import least_squares, minimize_scalar

import core_v022_latent_synaptic_state as v22

jax.config.update("jax_enable_x64", True)

SIGMA_T = 1.0e-4
SIGMA_Z = 2.0e-4
RHO = SIGMA_T / SIGMA_Z
TSTAR_REF = 0.6989193008948172


def measurement(theta, t):
    """Projected pre-event synaptic drive v^T psi(t)."""
    return math.exp(-v22.v21.ALPHA * t) * (theta[4] + t * theta[5])


def measurement_row(t):
    e = math.exp(-v22.v21.ALPHA * t)
    return np.array([0.0, 0.0, 0.0, 0.0, e, t * e])


def q0_row():
    return np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])


def psi0_row():
    return np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0])


def stats(A):
    sv = np.linalg.svd(A, compute_uv=False)
    return dict(singular_values=sv, sigma_min=float(sv[-1]),
                condition_number=float(sv[0] / sv[-1]))


def best_subset_with_row(J, k, row):
    best = None
    for inds in itertools.combinations(range(J.shape[0]), k):
        A = np.vstack([J[list(inds)], row])
        if np.linalg.matrix_rank(A, 1.0e-10) < J.shape[1]:
            continue
        sv = np.linalg.svd(A, compute_uv=False)
        score = float(sv[-1])
        if best is None or score > best[0]:
            best = (score, inds, sv)
    return best


def model_objects():
    tok, y, margins, _ = v22.record_chart()
    replay_fun = jax.jit(lambda th: v22.replay(th, tok))
    jac_fun = jax.jit(jax.jacfwd(lambda th: v22.replay(th, tok)))
    theta = jnp.asarray(v22.THETA_TRUE)
    assert np.max(np.abs(np.asarray(replay_fun(theta)) - y)) < 2.0e-12
    J = np.asarray(jac_fun(theta))
    return tok, y, margins, replay_fun, jac_fun, J


def optimize_measurement_time(J, first_event):
    f = lambda t: -np.linalg.svd(np.vstack([J, measurement_row(t)]), compute_uv=False)[-1]
    sol = minimize_scalar(f, bounds=(0.0, first_event - 1.0e-6), method="bounded",
                          options={"xatol": 1.0e-13})
    return float(sol.x), float(-sol.fun)


def fisher_std(Jspike, row, sigma_z=SIGMA_Z):
    F = Jspike.T @ Jspike / SIGMA_T**2 + np.outer(row, row) / sigma_z**2
    return np.sqrt(np.diag(np.linalg.inv(F)))


def sensor_noise_for_gain(J, row, target_gain):
    s0 = np.linalg.svd(J, compute_uv=False)[-1]
    lo, hi = 1.0e-6, 1.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        rho = SIGMA_T / mid
        gain = np.linalg.svd(np.vstack([J, rho * row]), compute_uv=False)[-1] / s0
        if gain >= target_gain:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def benchmark_checks():
    tok, y, margins, replay_fun, jac_fun, J = model_objects()
    base = v22.benchmark_checks()
    sv0 = np.linalg.svd(J, compute_uv=False)
    assert abs(sv0[-1] - 9.137484227978426e-4) < 2.0e-12

    first_event = float(np.min(y))
    tstar, sigma_star = optimize_measurement_time(J, first_event)
    row_star = measurement_row(tstar)
    assert abs(tstar - TSTAR_REF) < 3.0e-6
    # Rank-one PSD update interlacing: sigma_6(new) cannot exceed old sigma_5.
    assert abs(sigma_star - sv0[-2]) < 3.0e-12
    assert sigma_star / sv0[-1] > 250.0
    assert first_event - tstar > 7.45

    psi0 = stats(np.vstack([J, psi0_row()]))
    q0 = stats(np.vstack([J, q0_row()]))
    timed = stats(np.vstack([J, row_star]))
    assert psi0["sigma_min"] / sv0[-1] > 216.0
    assert q0["sigma_min"] / sv0[-1] > 28.0
    assert timed["sigma_min"] > psi0["sigma_min"]

    # Mixed-noise whitening, expressed in timing-noise units.
    weighted_full = stats(np.vstack([J, RHO * row_star]))
    assert abs(weighted_full["sigma_min"] - sv0[-2]) < 3.0e-12
    e5 = best_subset_with_row(J, 5, RHO * row_star)
    e6 = best_subset_with_row(J, 6, RHO * row_star)
    assert e5[1] == (0, 2, 9, 10, 11)
    assert e6[1] == (0, 2, 3, 9, 10, 11)
    assert e6[2][-1] > 0.200

    std_full = fisher_std(J, row_star)
    std_e6 = fisher_std(J[list(e6[1])], row_star)

    weak = np.asarray(base["weak_singular_vector"])
    weak_theta = v22.THETA_TRUE + 0.01 * weak
    weak_signal = float(measurement(weak_theta, tstar))
    alias = np.asarray(base["v021_alias"]["solution"])
    alias_signal = float(measurement(alias, tstar))
    assert abs(weak_signal) / SIGMA_Z > 25.0
    assert abs(alias_signal) / SIGMA_Z > 20.0

    sigma100 = sensor_noise_for_gain(J, row_star, 100.0)
    sigma200 = sensor_noise_for_gain(J, row_star, 200.0)
    assert sigma100 > 5.6e-4 and sigma200 > 2.8e-4

    return dict(
        event_count=int(tok.kind.shape[0]), first_spike=first_event,
        truth_chart_min_margin=float(np.min(margins)),
        old_singular_values=sv0, old_sigma_min=float(sv0[-1]),
        old_second_smallest=float(sv0[-2]),
        optimal_measurement_time=tstar,
        preevent_safety_margin=first_event - tstar,
        measurement_row=row_star,
        raw_timed=timed, raw_psi0=psi0, raw_q0=q0,
        raw_gain=float(timed["sigma_min"] / sv0[-1]),
        weighted_full=weighted_full,
        reference_noise=dict(sigma_t=SIGMA_T, sigma_z=SIGMA_Z, rho=RHO),
        weighted_e5=dict(indices=e5[1], singular_values=e5[2]),
        weighted_e6=dict(indices=e6[1], singular_values=e6[2], fisher_std=std_e6),
        weighted_full_fisher_std=std_full,
        weak_direction_signal=weak_signal,
        weak_direction_signal_in_sigma=abs(weak_signal) / SIGMA_Z,
        old_alias_signal=alias_signal,
        old_alias_signal_in_sigma=abs(alias_signal) / SIGMA_Z,
        sigma_z_for_100x_gain=sigma100,
        sigma_z_for_200x_gain=sigma200,
    )


def multistart_direct():
    _, y, _, replay_fun, jac_fun, J = model_objects()
    tstar, _ = optimize_measurement_time(J, float(np.min(y)))
    row = measurement_row(tstar)
    e5 = best_subset_with_row(J, 5, RHO * row)[1]
    e6 = best_subset_with_row(J, 6, RHO * row)[1]
    rng = np.random.default_rng(20260906)
    starts = [v22.THETA_TRUE + rng.normal(size=6) *
              np.array([0.02, 0.02, 0.005, 0.005, 0.008, 0.002]) for _ in range(12)]
    out = {}
    for name, inds in (("E5_plus_zpsi", e5), ("E6_plus_zpsi", e6)):
        ii = np.asarray(inds, int)
        dists = []
        for x0 in starts:
            fun = lambda x: np.r_[np.asarray(replay_fun(jnp.asarray(x)))[ii] - y[ii],
                                  measurement(x, tstar)]
            jac = lambda x: np.vstack([np.asarray(jac_fun(jnp.asarray(x)))[ii], row])
            sol = least_squares(fun, x0, jac=jac, max_nfev=100,
                                xtol=1e-13, ftol=1e-13, gtol=1e-13)
            dists.append(np.linalg.norm(sol.x - v22.THETA_TRUE))
        dists = np.asarray(dists)
        assert np.sum(dists < 1.0e-6) == 12
        out[name] = dists
    return out


def noise_direct():
    _, y, _, replay_fun, jac_fun, J = model_objects()
    tstar, _ = optimize_measurement_time(J, float(np.min(y)))
    row = measurement_row(tstar)
    inds = np.asarray(best_subset_with_row(J, 6, RHO * row)[1], int)
    pred = fisher_std(J[inds], row)
    rng = np.random.default_rng(20260908)
    xs = []
    for _ in range(30):
        data_t = y[inds] + rng.normal(scale=SIGMA_T, size=len(inds))
        data_z = rng.normal(scale=SIGMA_Z)
        def fun(x):
            return np.r_[(np.asarray(replay_fun(jnp.asarray(x)))[inds] - data_t) / SIGMA_T,
                         (measurement(x, tstar) - data_z) / SIGMA_Z]
        def jac(x):
            return np.vstack([np.asarray(jac_fun(jnp.asarray(x)))[inds] / SIGMA_T,
                              row / SIGMA_Z])
        x0 = v22.THETA_TRUE + np.array([2e-4, -2e-4, 2e-4, -2e-4, 2e-4, -1e-4])
        sol = least_squares(fun, x0, jac=jac, max_nfev=60,
                            xtol=1e-12, ftol=1e-12, gtol=1e-12)
        xs.append(sol.x)
    xs = np.asarray(xs)
    empirical = xs.std(0, ddof=1)
    ratio = empirical / pred
    assert np.all(ratio > 0.70) and np.all(ratio < 1.20)
    return dict(mean=xs.mean(0), empirical_std=empirical, fisher_std=pred, ratio=ratio)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--multistart-direct", action="store_true")
    ap.add_argument("--noise-direct", action="store_true")
    args = ap.parse_args()
    out = benchmark_checks()
    print("CORE v0.23 transverse-observation checks passed")
    print("t* / safety", out["optimal_measurement_time"], out["preevent_safety_margin"])
    print("old -> augmented sigma_min", out["old_sigma_min"], out["raw_timed"]["sigma_min"], out["raw_gain"])
    print("psi0 / q0", out["raw_psi0"]["sigma_min"], out["raw_q0"]["sigma_min"])
    print("weighted E6", out["weighted_e6"])
    print("weak/alias sensor sigma", out["weak_direction_signal_in_sigma"], out["old_alias_signal_in_sigma"])
    if args.multistart_direct:
        print("multistart", multistart_direct())
    if args.noise_direct:
        print("noise", noise_direct())


if __name__ == "__main__":
    main()
