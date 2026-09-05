"""Corrected SciPy/Numpy reference for CORE v0.8.1.

This audit verifies the hybrid intersection of the q=1 Neimark--Sacker locus
with a tangential response-threshold contact in the N=3 Lighthouse ring.

The original v0.8 script mixed a 48-point result with the 32-point quadrature
imported from v0.7.  This corrected version performs its own quadrature and
checks convergence between 96 and 128 Gauss points.  It intentionally does NOT
certify a first Lyapunov coefficient at the threshold boundary; that coefficient
was found to be quadrature/finite-difference sensitive and is superseded by the
smooth v0.9 Chenciner calculation.
"""

from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, root

from core_v07_event_normal_forms import (
    ALPHA,
    KAPPA,
    PI,
    alpha_comb,
    q_weighted,
    response,
    response_prime,
)


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
    return sum(
        w * alpha_comb(np.asarray(s) - d, T, ALPHA)
        for w, d in zip(ring_weights(p), ring_delays(tau3))
    )


def ring_psi_prime(s, T, p, tau3):
    return sum(
        w * alpha_comb_prime(np.asarray(s) - d, T, ALPHA)
        for w, d in zip(ring_weights(p), ring_delays(tau3))
    )


def make_split(n):
    gx, gw = leggauss(n)

    def gauss(fun, a, b):
        if b <= a:
            return 0.0
        x = 0.5 * (b - a) * gx + 0.5 * (a + b)
        return 0.5 * (b - a) * np.sum(gw * fun(x))

    def split(fun, a, b, points=()):
        pts = [a] + sorted(
            float(x) for x in points if a + 1e-12 < x < b - 1e-12
        ) + [b]
        return sum(gauss(fun, pts[k], pts[k + 1]) for k in range(len(pts) - 1))

    return split


def problem(n):
    split = make_split(n)

    def sync_residual(T, p, tau3):
        d = ring_delays(tau3)
        return 2.0 * PI - split(
            lambda s: response(ring_psi(s, T, p, tau3)),
            0.0,
            T,
            [x % T for x in d],
        )

    def ring_E(mu, T, p, tau3, qsector=1):
        w = ring_weights(p)
        d = ring_delays(tau3)
        points = [x % T for x in d]
        H = 0.0j
        for disp, (wd, td) in enumerate(zip(w, d)):
            phase = np.exp(-1j * KAPPA * qsector * disp)
            H += wd * phase * split(
                lambda s, td=td: response_prime(ring_psi(s, T, p, tau3))
                * q_weighted(np.asarray(s) - td, T, ALPHA, mu),
                0.0,
                T,
                points,
            )
        nu = float(response(ring_psi(0.0, T, p, tau3)))
        return nu * (complex(mu) - 1.0) - H

    return sync_residual, ring_E


def solve_codim(n, guess):
    sync, Efun = problem(n)

    def residual(z):
        T, p, Omega, tau3, sstar = z
        E = Efun(np.exp(1j * Omega), T, p, tau3)
        return np.array(
            [
                sync(T, p, tau3),
                E.real,
                E.imag,
                float(ring_psi(sstar, T, p, tau3)) + 1.0,
                float(ring_psi_prime(sstar, T, p, tau3)),
            ]
        )

    sol = root(residual, np.asarray(guess, dtype=float), tol=1e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x, np.linalg.norm(sol.fun)


def solve_ns(n, tau3, guess):
    sync, Efun = problem(n)

    def residual(z):
        T, p, Omega = z
        E = Efun(np.exp(1j * Omega), T, p, tau3)
        return np.array([sync(T, p, tau3), E.real, E.imag])

    sol = root(residual, np.asarray(guess, dtype=float), tol=1e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x


def solve_threshold(n, tau3, guess):
    sync, _ = problem(n)

    def residual(z):
        T, p, sstar = z
        return np.array(
            [
                sync(T, p, tau3),
                float(ring_psi(sstar, T, p, tau3)) + 1.0,
                float(ring_psi_prime(sstar, T, p, tau3)),
            ]
        )

    sol = root(residual, np.asarray(guess, dtype=float), tol=1e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.x


def characteristic_root(n, p, tau3, Tguess, muguess):
    sync, Efun = problem(n)
    T = brentq(lambda x: sync(x, p, tau3), Tguess - 1.0, Tguess + 1.0, xtol=1e-13)

    def residual(z):
        E = Efun(z[0] + 1j * z[1], T, p, tau3)
        return np.array([E.real, E.imag])

    sol = root(residual, np.array([muguess.real, muguess.imag]), tol=1e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    return T, complex(sol.x[0], sol.x[1])


def main():
    guess = [17.6951, -7.21564, 0.461034, 13.14025, 4.380708]
    z96, r96 = solve_codim(96, guess)
    z128, r128 = solve_codim(128, z96)
    T, p, Omega, tau3, sstar = z128
    mu = np.exp(1j * Omega)

    target = np.array(
        [
            17.69506502372353,
            -7.21564040067306,
            0.4610342074202,
            13.14024821048378,
            4.38070788630572,
        ]
    )
    assert r96 < 1e-9 and r128 < 1e-9
    assert np.max(np.abs(z128 - target)) < 5e-7
    assert np.max(np.abs(z128 - z96)) < 5e-7

    h = 1e-4
    psi2 = (
        ring_psi(sstar + h, T, p, tau3)
        - 2.0 * ring_psi(sstar, T, p, tau3)
        + ring_psi(sstar - h, T, p, tau3)
    ) / h**2
    nu = float(response(ring_psi(0.0, T, p, tau3)))
    assert abs(float(psi2) - 0.25) < 2e-6
    assert nu > 0.7

    ht = 1e-4
    nsp = solve_ns(128, tau3 + ht, [T, p, Omega])
    nsm = solve_ns(128, tau3 - ht, [T, p, Omega])
    thp = solve_threshold(128, tau3 + ht, [T, p, sstar])
    thm = solve_threshold(128, tau3 - ht, [T, p, sstar])
    dpdt_ns = (nsp[1] - nsm[1]) / (2.0 * ht)
    dpdt_th = (thp[1] - thm[1]) / (2.0 * ht)
    assert abs(dpdt_ns + 2.272331439) < 5e-4
    assert abs(dpdt_th + 0.291825733) < 5e-4
    assert abs(dpdt_ns - dpdt_th) > 1.0

    hp = 1e-5
    _, mup = characteristic_root(128, p + hp, tau3, T, mu)
    _, mum = characteristic_root(128, p - hp, tau3, T, mu)
    radial = (abs(mup) - abs(mum)) / (2.0 * hp)
    assert abs(radial + 0.019617079) < 5e-4

    print("CORE v0.8.1 corrected reference checks passed")
    print("96-point:", z96)
    print("128-point:", z128)
    print("mu:", mu)
    print("psi'' / nu:", psi2, nu)
    print("dp/dtau NS / threshold:", dpdt_ns, dpdt_th)
    print("radial slope:", radial)
    print("ell1 at threshold boundary: intentionally NOT certified")


if __name__ == "__main__":
    main()
