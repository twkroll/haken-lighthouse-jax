"""Independent SciPy/Numpy reference for CORE v0.8.

Verifies the first hybrid codimension-two Lighthouse benchmark: intersection of
an N=3 ring Neimark--Sacker locus with a tangential response-threshold contact.

Run from the repository root with

    python reference/core_v08_codimension_two.py
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import brentq, root

from core_v07_event_normal_forms import (
    ALPHA,
    KAPPA,
    PI,
    SpikeHistoryMap,
    alpha_comb,
    complex_B,
    complex_C,
    jacobian_fd,
    physical_ring_q,
    q_weighted,
    response,
    response_prime,
    split_int,
)


BASE_DELAYS = np.array([0.0, 2.0])


def alpha_comb_prime(t, T, alpha=ALPHA):
    t = np.asarray(t, dtype=float)
    u = np.mod(t, T)
    r = np.exp(-alpha * T)
    A = u / (1.0 - r) + T * r / (1.0 - r) ** 2
    return alpha**2 * np.exp(-alpha * u) * (
        1.0 / (1.0 - r) - alpha * A
    )


def ring_weights(p):
    return np.array([1.0, p, -p])


def ring_delays(tau3):
    return np.array([0.0, 2.0, tau3])


def ring_psi(s, T, p, tau3):
    w = ring_weights(p)
    d = ring_delays(tau3)
    return sum(wd * alpha_comb(np.asarray(s) - td, T, ALPHA) for wd, td in zip(w, d))


def ring_psi_prime(s, T, p, tau3):
    w = ring_weights(p)
    d = ring_delays(tau3)
    return sum(
        wd * alpha_comb_prime(np.asarray(s) - td, T, ALPHA)
        for wd, td in zip(w, d)
    )


def sync_residual(T, p, tau3):
    d = ring_delays(tau3)
    return 2.0 * PI - split_int(
        lambda s: response(ring_psi(s, T, p, tau3)),
        0.0,
        T,
        [td % T for td in d],
    )


def ring_E(mu, T, p, tau3, qsector=1):
    w = ring_weights(p)
    d = ring_delays(tau3)
    points = [td % T for td in d]
    H = 0.0j
    for displacement, (wd, td) in enumerate(zip(w, d)):
        phase = np.exp(-1j * KAPPA * qsector * displacement)
        H += wd * phase * split_int(
            lambda s, td=td: response_prime(ring_psi(s, T, p, tau3))
            * q_weighted(np.asarray(s) - td, T, ALPHA, mu),
            0.0,
            T,
            points,
        )
    nu = float(response(ring_psi(0.0, T, p, tau3)))
    return nu * (complex(mu) - 1.0) - H


def codim_residual(z):
    T, p, Omega, tau3, sstar = z
    E = ring_E(np.exp(1j * Omega), T, p, tau3)
    return np.array(
        [
            sync_residual(T, p, tau3),
            E.real,
            E.imag,
            float(ring_psi(sstar, T, p, tau3)) + 1.0,
            float(ring_psi_prime(sstar, T, p, tau3)),
        ]
    )


def solve_codim2():
    guess = np.array([17.6954, -7.216, 0.4610, 13.1412, 4.3808])
    sol = root(codim_residual, guess, tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x, np.linalg.norm(sol.fun)


def solve_ns_at_tau3(tau3, guess):
    def residual(z):
        T, p, Omega = z
        E = ring_E(np.exp(1j * Omega), T, p, tau3)
        return np.array([sync_residual(T, p, tau3), E.real, E.imag])

    sol = root(residual, np.asarray(guess, dtype=float), tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x


def solve_threshold_at_tau3(tau3, guess):
    def residual(z):
        T, p, sstar = z
        return np.array(
            [
                sync_residual(T, p, tau3),
                float(ring_psi(sstar, T, p, tau3)) + 1.0,
                float(ring_psi_prime(sstar, T, p, tau3)),
            ]
        )

    sol = root(residual, np.asarray(guess, dtype=float), tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x


def ring_matrices(p, tau3):
    w = ring_weights(p)
    d = ring_delays(tau3)
    W = np.empty((3, 3))
    D = np.empty((3, 3))
    for i in range(3):
        for j in range(3):
            displacement = (i - j) % 3
            W[i, j] = w[displacement]
            D[i, j] = d[displacement]
    return W, D


def event_map_ell1(T, p, Omega, tau3, history_length=4, h=2.5e-3):
    W, D = ring_matrices(p, tau3)
    P = SpikeHistoryMap(W, T, D, history_length=history_length)
    x0 = np.zeros(3 * history_length)
    L = jacobian_fd(P, x0)

    target = np.exp(1j * Omega)
    vals = np.linalg.eigvals(L)
    mu = vals[np.argmin(np.abs(vals - target))]
    q = physical_ring_q(mu, history_length)

    vals_t, vecs_t = np.linalg.eig(L.T)
    pleft = vecs_t[:, np.argmin(np.abs(vals_t - np.conj(mu)))]
    pleft /= np.conj(np.vdot(pleft, q))

    Bqq = complex_B(P, q, q, h)
    Bqb = complex_B(P, q, np.conj(q), h)
    h20 = np.linalg.solve(mu**2 * np.eye(len(q)) - L, Bqq)
    h11 = np.linalg.solve(np.eye(len(q)) - L, Bqb)
    G21 = np.vdot(
        pleft,
        complex_C(P, q, q, np.conj(q), h)
        + complex_B(P, np.conj(q), h20, h)
        + 2.0 * complex_B(P, q, h11, h),
    )
    ell1 = 0.5 * np.real(np.exp(-1j * np.angle(mu)) * G21)
    qres = np.linalg.norm(L @ q - mu * q) / np.linalg.norm(q)
    return float(ell1), mu, float(qres)


def characteristic_root_for_p(p, Tguess, muguess, tau3):
    T = brentq(lambda x: sync_residual(x, p, tau3), Tguess - 2.0, Tguess + 2.0)

    def residual(z):
        E = ring_E(z[0] + 1j * z[1], T, p, tau3)
        return np.array([E.real, E.imag])

    sol = root(residual, np.array([muguess.real, muguess.imag]), tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return T, complex(sol.x[0], sol.x[1])


def main():
    z, residual_norm = solve_codim2()
    T, p, Omega, tau3, sstar = z
    mu = np.exp(1j * Omega)

    assert residual_norm < 1e-9
    assert abs(T - 17.69540826) < 5e-6
    assert abs(p + 7.21591135) < 5e-6
    assert abs(tau3 - 13.14117538) < 5e-6
    assert abs(Omega - 0.46104577) < 5e-6
    assert abs(sstar - 4.38076296) < 5e-6

    # Threshold curvature and event transversality.
    hcurv = 2e-4
    psi2 = (
        ring_psi(sstar + hcurv, T, p, tau3)
        - 2.0 * ring_psi(sstar, T, p, tau3)
        + ring_psi(sstar - hcurv, T, p, tau3)
    ) / hcurv**2
    nu = float(response(ring_psi(0.0, T, p, tau3)))
    assert abs(float(psi2) - 0.25) < 2e-5
    assert nu > 0.7

    # Local tangents of the two loci.
    ht = 1e-4
    nsp = solve_ns_at_tau3(tau3 + ht, [T, p, Omega])
    nsm = solve_ns_at_tau3(tau3 - ht, [T, p, Omega])
    thp = solve_threshold_at_tau3(tau3 + ht, [T, p, sstar])
    thm = solve_threshold_at_tau3(tau3 - ht, [T, p, sstar])
    dpdt_ns = (nsp[1] - nsm[1]) / (2.0 * ht)
    dpdt_th = (thp[1] - thm[1]) / (2.0 * ht)
    assert abs(dpdt_ns + 2.26337357) < 3e-4
    assert abs(dpdt_th + 0.29189680) < 3e-4
    assert abs(dpdt_ns - dpdt_th) > 1.0

    # Radial crossing at fixed tau3.
    hp = 1e-5
    _, mup = characteristic_root_for_p(p + hp, T, mu, tau3)
    _, mum = characteristic_root_for_p(p - hp, T, mu, tau3)
    radial = (abs(mup) - abs(mum)) / (2.0 * hp)
    assert abs(radial + 0.01969526) < 3e-4

    # Direct event-map cubic coefficient and history convergence.
    ell4, mu4, qres4 = event_map_ell1(T, p, Omega, tau3, 4)
    ell5, mu5, qres5 = event_map_ell1(T, p, Omega, tau3, 5)
    assert qres4 < 2e-6 and qres5 < 2e-6
    assert abs(abs(mu4) - 1.0) < 5e-5
    assert abs(abs(mu5) - 1.0) < 5e-5
    assert abs(ell4 + 14.50060663) < 3e-3
    assert abs(ell5 + 14.50060668) < 3e-3
    assert abs(ell4 - ell5) < 1e-5

    print("CORE v0.8 reference checks passed")
    print("codim2:", z, "residual norm=", residual_norm)
    print("mu=", mu, "psi''=", psi2, "nu=", nu)
    print("locus slopes dp/dtau3 NS/TH:", dpdt_ns, dpdt_th)
    print("radial slope d|mu|/dp:", radial)
    print("ell1 L4/L5:", ell4, ell5)


if __name__ == "__main__":
    main()
