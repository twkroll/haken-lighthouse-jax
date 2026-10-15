"""CORE v0.26 — shared-parameter inference with trial-specific state and calibration nuisance.

Extends CORE v0.25 from a reproducibly identical latent initial state to two
independently prepared trials.  The shared network parameters remain

    (p, tau3),

while each trial has its own six-dimensional relative initial state

    z_r=(eta1,eta2,xi_psi1,xi_psi2,xi_q1,xi_q2).

Pulse calibration is also allowed to vary around the nominal v0.25 controls.
The calibration coordinates are

    du_r=(dt_p,dA,dbeta,dgamma).

A key v0.26 result is structural: at fixed trial initial state freedom, pulse
amplitude / beta / gamma calibration directions lie in the same local output
span as the latent initial state.  They therefore cannot be self-calibrated
from spike times alone.  Shared p,tau3 can nevertheless remain identifiable.
"""
from __future__ import annotations

import argparse
import math
import numpy as np
import jax
import jax.numpy as jnp
from scipy.optimize import least_squares

import core_v025_full_q1_two_probe as v25

jax.config.update("jax_enable_x64", True)

SIGMA_T = 1.0e-4
CAL_SIGMA = np.array([0.002, 0.002, 0.02, 0.02])

Z1_TRUE = np.array([0.0015, -0.0010, 0.0030, -0.0020, 0.0010, -0.0005])
Z2_TRUE = np.array([-0.0003, 0.000325, -0.000625, 0.00055, -0.0002, 0.000175])

DU1_TRUE = np.array([0.0010, -0.0010, 0.010, -0.008])
DU2_TRUE = np.array([-0.0015, 0.0010, -0.012, 0.006])

P1_TRUE = tuple(np.asarray(v25.P1) + DU1_TRUE)
P2_TRUE = tuple(np.asarray(v25.P2) + DU2_TRUE)

SHARED_TRUE = np.array([v25.THETA_TRUE[0], v25.THETA_TRUE[1]])
THETA1_TRUE = np.r_[SHARED_TRUE, Z1_TRUE]
THETA2_TRUE = np.r_[SHARED_TRUE, Z2_TRUE]


def trial(theta, pulse):
    tok, y, margins, pre = v25.record_chart8(theta, pulse)
    replay = jax.jit(lambda th: v25.replay8(th, tok, pulse))
    yj = np.asarray(replay(jnp.asarray(theta)))
    return dict(tok=tok, y=y, margins=margins, pre_margin=pre,
                margin=min(pre, float(np.min(margins))), replay=replay,
                replay_error=float(np.max(np.abs(yj-y))))


def trial_jacobians(theta, pulse, tok):
    fun = lambda th, u: v25.replay8(th, tok, u)
    jac_th, jac_u = jax.jacfwd(fun, argnums=(0, 1))(
        jnp.asarray(theta), jnp.asarray(pulse)
    )
    return np.asarray(jac_th), np.asarray(jac_u)


def physical_fd(theta, pulse, tok, h=1.0e-6):
    sig = v25.v24.v22.signature(tok)
    cols_th, cols_u = [], []
    for j in range(8):
        d = np.zeros(8); d[j] = h
        pp = v25.record_chart8(theta + d, pulse)
        pm = v25.record_chart8(theta - d, pulse)
        assert v25.v24.v22.signature(pp[0]) == sig
        assert v25.v24.v22.signature(pm[0]) == sig
        cols_th.append((pp[1] - pm[1]) / (2.0*h))
    pulse = np.asarray(pulse, float)
    for j in range(4):
        d = np.zeros(4); d[j] = h
        pp = v25.record_chart8(theta, tuple(pulse + d))
        pm = v25.record_chart8(theta, tuple(pulse - d))
        assert v25.v24.v22.signature(pp[0]) == sig
        assert v25.v24.v22.signature(pm[0]) == sig
        cols_u.append((pp[1] - pm[1]) / (2.0*h))
    return np.column_stack(cols_th), np.column_stack(cols_u)


def residualize(A, nuisance, rank=None):
    U, s, _ = np.linalg.svd(nuisance, full_matrices=False)
    if rank is None:
        rank = nuisance.shape[1]
    Q = U[:, :rank]
    return A - Q @ (Q.T @ A), s


def profile_shared(J1, J2):
    R1, _ = residualize(J1[:, :2], J1[:, 2:], rank=6)
    R2, _ = residualize(J2[:, :2], J2[:, 2:], rank=6)
    R = np.vstack([R1, R2])
    cov = SIGMA_T**2 * np.linalg.inv(R.T @ R)
    return dict(R=R, singular_values=np.linalg.svd(R, compute_uv=False),
                std=np.sqrt(np.diag(cov)), cov=cov)


def calibration_span(J, K):
    N = J[:, 2:]
    Q, _ = np.linalg.qr(N, mode="reduced")
    residual = K - Q @ (Q.T @ K)
    aug_sv = np.linalg.svd(np.column_stack([N, K]), compute_uv=False)
    return dict(residual=residual,
                residual_norm=np.linalg.norm(residual, axis=0),
                relative_residual=np.linalg.norm(residual, axis=0)/np.linalg.norm(K, axis=0),
                augmented_singular_values=aug_sv)


def free_time_profile(J1, K1, J2, K2):
    rows = []
    for J, K in ((J1, K1), (J2, K2)):
        N = np.column_stack([J[:, 2:], K[:, 0]])
        U, _, _ = np.linalg.svd(N, full_matrices=False)
        Q = U[:, :7]
        rows.append(J[:, :2] - Q @ (Q.T @ J[:, :2]))
    R = np.vstack(rows)
    cov = SIGMA_T**2 * np.linalg.inv(R.T @ R)
    return dict(singular_values=np.linalg.svd(R, compute_uv=False),
                std=np.sqrt(np.diag(cov)), cov=cov)


def joint14_jac(J1, J2):
    return np.block([
        [J1[:, :2], J1[:, 2:], np.zeros((12, 6))],
        [J2[:, :2], np.zeros((12, 6)), J2[:, 2:]],
    ])


def joint22_spike_jac(J1, K1, J2, K2):
    return np.block([
        [J1[:, :2], J1[:, 2:], np.zeros((12,6)), K1, np.zeros((12,4))],
        [J2[:, :2], np.zeros((12,6)), J2[:, 2:], np.zeros((12,4)), K2],
    ])


def augmented_calibration_jac(J22):
    W = J22 / SIGMA_T
    C = np.zeros((8, 22))
    sig = np.tile(CAL_SIGMA, 2)
    for j in range(8):
        C[j, 14+j] = 1.0/sig[j]
    return np.vstack([W, C])


def benchmark_checks():
    t1, t2 = trial(THETA1_TRUE, P1_TRUE), trial(THETA2_TRUE, P2_TRUE)
    assert t1["replay_error"] < 1.0e-11 and t2["replay_error"] < 1.0e-11
    assert t1["margin"] > 0.06 and t2["margin"] > 0.06

    J1, K1 = trial_jacobians(THETA1_TRUE, P1_TRUE, t1["tok"])
    J2, K2 = trial_jacobians(THETA2_TRUE, P2_TRUE, t2["tok"])
    FDJ1, FDK1 = physical_fd(THETA1_TRUE, P1_TRUE, t1["tok"])
    FDJ2, FDK2 = physical_fd(THETA2_TRUE, P2_TRUE, t2["tok"])
    relJ1 = float(np.linalg.norm(J1-FDJ1)/np.linalg.norm(FDJ1))
    relJ2 = float(np.linalg.norm(J2-FDJ2)/np.linalg.norm(FDJ2))
    relK1 = float(np.linalg.norm(K1-FDK1)/np.linalg.norm(FDK1))
    relK2 = float(np.linalg.norm(K2-FDK2)/np.linalg.norm(FDK2))
    assert max(relJ1, relJ2, relK1, relK2) < 1.0e-8

    J14 = joint14_jac(J1, J2)
    sv14 = np.linalg.svd(J14, compute_uv=False)
    assert np.linalg.matrix_rank(J14, 1.0e-10) == 14
    prof = profile_shared(J1, J2)
    assert prof["singular_values"][-1] > 0.324
    assert prof["std"][0] < 1.56e-4
    assert prof["std"][1] < 2.83e-4

    c1, c2 = calibration_span(J1, K1), calibration_span(J2, K2)
    # Pulse parameter order: tp, A, beta, gamma.  A/beta/gamma are structurally
    # absorbed by the free trial initial state to numerical precision.
    assert np.max(c1["relative_residual"][1:]) < 3.0e-9
    assert np.max(c2["relative_residual"][1:]) < 1.0e-9
    assert c1["relative_residual"][0] < 5.0e-6
    assert c2["relative_residual"][0] < 5.0e-7

    free_t = free_time_profile(J1, K1, J2, K2)
    assert free_t["std"][0] < 2.65e-4
    assert free_t["std"][1] < 4.87e-4

    J22 = joint22_spike_jac(J1, K1, J2, K2)
    sv22 = np.linalg.svd(J22, compute_uv=False)
    # Six essentially exact null directions remain: A/beta/gamma for each trial.
    assert np.sum(sv22 < 1.0e-12) >= 6

    Jaug = augmented_calibration_jac(J22)
    cov_aug = np.linalg.inv(Jaug.T @ Jaug)
    std_aug = np.sqrt(np.diag(cov_aug))
    assert np.max(np.abs(std_aug[:2] - prof["std"])) < 5.0e-9
    assert np.max(np.abs(std_aug[14:22] - np.tile(CAL_SIGMA,2))) < 2.0e-10

    return dict(
        trial1=t1, trial2=t2, J1=J1, J2=J2, K1=K1, K2=K2,
        derivative_errors=dict(J1=relJ1, J2=relJ2, K1=relK1, K2=relK2),
        J14=J14, J14_singular_values=sv14, profile=prof,
        calibration_span1=c1, calibration_span2=c2,
        free_time_profile=free_t, J22=J22, J22_singular_values=sv22,
        augmented_std=std_aug,
    )


def joint14_functions(t1, t2):
    def replay(x):
        th1 = jnp.concatenate([x[:2], x[2:8]])
        th2 = jnp.concatenate([x[:2], x[8:14]])
        return jnp.concatenate([
            v25.replay8(th1, t1["tok"], jnp.asarray(P1_TRUE)),
            v25.replay8(th2, t2["tok"], jnp.asarray(P2_TRUE)),
        ])
    return jax.jit(replay), jax.jit(jax.jacfwd(replay))


def joint22_functions(t1, t2):
    p1 = jnp.asarray(v25.P1); p2 = jnp.asarray(v25.P2)
    def replay(x):
        th1 = jnp.concatenate([x[:2], x[2:8]])
        th2 = jnp.concatenate([x[:2], x[8:14]])
        u1 = p1 + x[14:18]
        u2 = p2 + x[18:22]
        return jnp.concatenate([
            v25.replay8(th1, t1["tok"], u1),
            v25.replay8(th2, t2["tok"], u2),
        ])
    return jax.jit(replay), jax.jit(jax.jacfwd(replay))


def multistart_direct():
    t1, t2 = trial(THETA1_TRUE, P1_TRUE), trial(THETA2_TRUE, P2_TRUE)
    y = np.r_[t1["y"], t2["y"]]

    x14_true = np.r_[SHARED_TRUE, Z1_TRUE, Z2_TRUE]
    f14, j14 = joint14_functions(t1, t2)
    rng = np.random.default_rng(20260915)
    scales14 = np.r_[0.02,0.02,
        [0.003,0.003,0.004,0.004,0.0015,0.0015],
        [0.003,0.003,0.004,0.004,0.0015,0.0015]]
    shared_err14, full_dist14 = [], []
    for _ in range(12):
        x0 = x14_true + rng.normal(size=14)*scales14
        sol = least_squares(lambda x: np.asarray(f14(jnp.asarray(x)))-y, x0,
                            jac=lambda x: np.asarray(j14(jnp.asarray(x))),
                            max_nfev=100, xtol=1e-13, ftol=1e-13, gtol=1e-13)
        shared_err14.append(sol.x[:2]-SHARED_TRUE)
        full_dist14.append(np.linalg.norm(sol.x-x14_true))
    shared_err14 = np.asarray(shared_err14); full_dist14=np.asarray(full_dist14)
    assert np.all(np.max(np.abs(shared_err14),axis=1) < 1.0e-5)
    assert np.sum(full_dist14 < 1.0e-6) < 12

    x22_true = np.r_[SHARED_TRUE, Z1_TRUE, Z2_TRUE, DU1_TRUE, DU2_TRUE]
    f22, j22 = joint22_functions(t1, t2)
    cal_true = np.r_[DU1_TRUE, DU2_TRUE]
    sig = np.tile(CAL_SIGMA,2)
    rng = np.random.default_rng(20260917)
    scales22 = np.r_[0.02,0.02,
        [0.003,0.003,0.004,0.004,0.0015,0.0015],
        [0.003,0.003,0.004,0.004,0.0015,0.0015],
        [0.001,0.001,0.01,0.01], [0.001,0.001,0.01,0.01]]
    shared_err22, full_dist22 = [], []
    for _ in range(12):
        x0 = x22_true + rng.normal(size=22)*scales22
        def fun(x):
            return np.r_[(np.asarray(f22(jnp.asarray(x)))-y)/SIGMA_T,
                         (x[14:22]-cal_true)/sig]
        def jac(x):
            J = np.asarray(j22(jnp.asarray(x)))/SIGMA_T
            C = np.zeros((8,22))
            for j in range(8): C[j,14+j]=1.0/sig[j]
            return np.vstack([J,C])
        sol = least_squares(fun, x0, jac=jac, max_nfev=100,
                            xtol=1e-12, ftol=1e-12, gtol=1e-12)
        shared_err22.append(sol.x[:2]-SHARED_TRUE)
        full_dist22.append(np.linalg.norm(sol.x-x22_true))
    shared_err22=np.asarray(shared_err22);full_dist22=np.asarray(full_dist22)
    assert np.all(np.max(np.abs(shared_err22),axis=1) < 1.0e-5)
    return dict(shared_err14=shared_err14, full_dist14=full_dist14,
                shared_err22=shared_err22, full_dist22=full_dist22)


def noise_direct():
    out = benchmark_checks()
    t1,t2=out["trial1"],out["trial2"]
    y=np.r_[t1["y"],t2["y"]]

    # Known-calibration / trial-specific-state audit.
    x14_true=np.r_[SHARED_TRUE,Z1_TRUE,Z2_TRUE]
    f14,j14=joint14_functions(t1,t2)
    pred14=out["profile"]["std"]
    rng=np.random.default_rng(20260916);xs=[]
    for _ in range(50):
        data=y+rng.normal(scale=SIGMA_T,size=24)
        x0=x14_true+np.r_[[1e-4,-1e-4],np.full(12,1e-4)]
        sol=least_squares(lambda x:(np.asarray(f14(jnp.asarray(x)))-data)/SIGMA_T,
                          x0,jac=lambda x:np.asarray(j14(jnp.asarray(x)))/SIGMA_T,
                          max_nfev=80,xtol=1e-12,ftol=1e-12,gtol=1e-12)
        xs.append(sol.x)
    xs=np.asarray(xs);emp14=xs[:,:2].std(0,ddof=1)
    assert np.all(emp14/pred14 > 0.8) and np.all(emp14/pred14 < 1.2)

    # Calibration-aware audit with external calibration readouts.
    x22_true=np.r_[SHARED_TRUE,Z1_TRUE,Z2_TRUE,DU1_TRUE,DU2_TRUE]
    f22,j22=joint22_functions(t1,t2)
    pred22=out["augmented_std"][:2]
    sig=np.tile(CAL_SIGMA,2)
    rng=np.random.default_rng(20260918);xs22=[]
    for _ in range(50):
        data=y+rng.normal(scale=SIGMA_T,size=24)
        cal=np.r_[DU1_TRUE,DU2_TRUE]+rng.normal(scale=sig)
        x0=x22_true+np.r_[[1e-4,-1e-4],np.full(12,1e-4),
                          [2e-4,2e-4,0.002,0.002,2e-4,2e-4,0.002,0.002]]
        def fun(x):
            return np.r_[(np.asarray(f22(jnp.asarray(x)))-data)/SIGMA_T,
                         (x[14:22]-cal)/sig]
        def jac(x):
            J=np.asarray(j22(jnp.asarray(x)))/SIGMA_T
            C=np.zeros((8,22))
            for j in range(8):C[j,14+j]=1.0/sig[j]
            return np.vstack([J,C])
        sol=least_squares(fun,x0,jac=jac,max_nfev=80,
                          xtol=1e-11,ftol=1e-11,gtol=1e-11)
        xs22.append(sol.x)
    xs22=np.asarray(xs22);emp22=xs22[:,:2].std(0,ddof=1)
    assert np.all(emp22/pred22 > 0.75) and np.all(emp22/pred22 < 1.25)
    return dict(known_calibration=dict(mean=xs[:,:2].mean(0), empirical_std=emp14,
                                       fisher_std=pred14, ratio=emp14/pred14),
                uncertain_calibration=dict(mean=xs22[:,:2].mean(0), empirical_std=emp22,
                                           fisher_std=pred22, ratio=emp22/pred22))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--multistart-direct",action="store_true")
    ap.add_argument("--noise-direct",action="store_true")
    args=ap.parse_args()
    out=benchmark_checks()
    print("CORE v0.26 trial-nuisance/calibration checks passed")
    print("margins",out["trial1"]["margin"],out["trial2"]["margin"])
    print("profile shared",out["profile"]["singular_values"],out["profile"]["std"])
    print("calibration residuals P1",out["calibration_span1"]["relative_residual"])
    print("calibration residuals P2",out["calibration_span2"]["relative_residual"])
    print("free pulse-time shared",out["free_time_profile"]["std"])
    print("calibration-aware shared",out["augmented_std"][:2])
    if args.multistart_direct: print("multistart",multistart_direct())
    if args.noise_direct: print("noise",noise_direct())


if __name__=="__main__":
    main()
