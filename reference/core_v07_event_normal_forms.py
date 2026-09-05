"""Independent SciPy/Numpy reference for CORE v0.7.

This file deliberately does not use JAX.  It checks two nonlinear Lighthouse
normal-form benchmarks directly from a gauge-fixed spike-history return map:

1. a generic two-cell flip with a continued period-two spike pattern;
2. a three-node ring Neimark--Sacker point with a direct first Lyapunov coefficient.

Run from the repository root with

    python reference/core_v07_event_normal_forms.py
"""

from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, root

from core_v06_two_cell_pitchfork import (
    alpha_comb,
    q_weighted,
    response,
    response_prime,
)

PI = math.pi
ALPHA = 0.5
GX, GW = leggauss(32)


def eta_alpha(x, alpha=ALPHA):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    mask = x >= 0.0
    out[mask] = alpha**2 * x[mask] * np.exp(-alpha * x[mask])
    return out


def gauss_int(fun, a, b):
    if b <= a:
        return 0.0
    x = 0.5 * (b - a) * GX + 0.5 * (a + b)
    return 0.5 * (b - a) * np.sum(GW * fun(x))


def split_int(fun, a, b, points=()):
    pts = [a] + sorted(float(x) for x in points if a + 1e-12 < x < b - 1e-12) + [b]
    return sum(gauss_int(fun, pts[k], pts[k + 1]) for k in range(len(pts) - 1))


class SpikeHistoryMap:
    """Gauge-fixed exact-event map with an exact periodic base tail.

    `history[r,j]` is the spike-time perturbation of neuron j, r cycles in the
    past.  The unperturbed infinite tail is represented by the exact periodic
    alpha comb; only perturbation corrections are truncated.
    """

    def __init__(self, W, T, delay, history_length=4, alpha=ALPHA):
        self.W = np.asarray(W, dtype=float)
        self.N = self.W.shape[0]
        self.T = float(T)
        self.delay = np.asarray(delay, dtype=float)
        self.L = int(history_length)
        self.alpha = float(alpha)

    def input(self, i, t, history):
        t = np.asarray(t, dtype=float)
        psi = np.zeros_like(t)
        for j in range(self.N):
            dij = self.delay[i, j]
            psi += self.W[i, j] * alpha_comb(t - dij, self.T, self.alpha)
            for r in range(self.L):
                tbase = -r * self.T
                psi += self.W[i, j] * (
                    eta_alpha(t - dij - (tbase + history[r, j]), self.alpha)
                    - eta_alpha(t - dij - tbase, self.alpha)
                )
        return psi

    def phase_gain(self, i, tend, history):
        tstart = history[0, i]
        points = []
        for j in range(self.N):
            dij = self.delay[i, j]
            for r in range(self.L):
                tbase = -r * self.T
                for x in (tbase + dij, tbase + history[r, j] + dij):
                    if tstart + 1e-12 < x < tend - 1e-12:
                        points.append(x)
        return split_int(
            lambda t: response(self.input(i, t, history)),
            tstart,
            tend,
            points,
        )

    def raw_next(self, history):
        out = np.zeros(self.N)
        for i in range(self.N):
            def residual(delta):
                return 2.0 * PI - self.phase_gain(i, self.T + delta, history)

            lo, hi = -2.0, 2.0
            flo, fhi = residual(lo), residual(hi)
            for _ in range(8):
                if flo * fhi <= 0.0:
                    break
                lo -= 2.0
                hi += 2.0
                flo, fhi = residual(lo), residual(hi)
            if flo * fhi > 0.0:
                raise RuntimeError("failed to bracket next spike")
            out[i] = brentq(residual, lo, hi, xtol=2e-12)
        return out

    def __call__(self, x):
        history = np.asarray(x, dtype=float).reshape(self.L, self.N)
        nxt = self.raw_next(history)
        gauge = float(np.mean(nxt))
        out = np.empty_like(history)
        out[0] = nxt - gauge
        for r in range(1, self.L):
            out[r] = history[r - 1] - gauge
        return out.ravel()


def jacobian_fd(fun, x, h=8e-7):
    x = np.asarray(x, dtype=float)
    n = len(x)
    J = np.empty((n, n))
    for k in range(n):
        e = np.zeros(n)
        e[k] = 1.0
        J[:, k] = (fun(x + h * e) - fun(x - h * e)) / (2.0 * h)
    return J


def mixed_B(fun, u, v, h):
    return (
        fun(h * (u + v))
        - fun(h * (u - v))
        - fun(h * (-u + v))
        + fun(-h * (u + v))
    ) / (4.0 * h**2)


def diagonal_C(fun, q, h):
    return (
        fun(2.0 * h * q)
        - 2.0 * fun(h * q)
        + 2.0 * fun(-h * q)
        - fun(-2.0 * h * q)
    ) / (2.0 * h**3)


def mixed_C(fun, u, v, w, h):
    return (
        fun(h * (u + v + w))
        - fun(h * (u + v - w))
        - fun(h * (u - v + w))
        - fun(h * (-u + v + w))
        + fun(h * (u - v - w))
        + fun(h * (-u + v - w))
        + fun(h * (-u - v + w))
        - fun(-h * (u + v + w))
    ) / (8.0 * h**3)


# ---------------------------------------------------------------------------
# Generic two-cell flip


def two_cell_sync_residual(T, what, tau_cross=2.0):
    ws = 0.5 * (1.0 + what)
    wc = 0.5 * (1.0 - what)
    p = tau_cross % T
    return 2.0 * PI - split_int(
        lambda s: response(
            ws * alpha_comb(s, T, ALPHA)
            + wc * alpha_comb(s - tau_cross, T, ALPHA)
        ),
        0.0,
        T,
        [p],
    )


def two_cell_Eminus(mu, T, what, tau_cross=2.0):
    ws = 0.5 * (1.0 + what)
    wc = 0.5 * (1.0 - what)
    p = tau_cross % T

    def psi(s):
        return ws * alpha_comb(s, T, ALPHA) + wc * alpha_comb(s - tau_cross, T, ALPHA)

    hs = ws * split_int(
        lambda s: response_prime(psi(s)) * q_weighted(s, T, ALPHA, mu),
        0.0,
        T,
        [p],
    )
    hc = wc * split_int(
        lambda s: response_prime(psi(s)) * q_weighted(s - tau_cross, T, ALPHA, mu),
        0.0,
        T,
        [p],
    )
    nu = float(response(psi(0.0)))
    return nu * (complex(mu) - 1.0) - hs + hc


def solve_flip_critical():
    sol = root(
        lambda z: np.array(
            [
                two_cell_sync_residual(z[0], z[1]),
                two_cell_Eminus(-1.0, z[0], z[1]).real,
            ]
        ),
        np.array([16.82, 10.51]),
        tol=1e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return float(sol.x[0]), float(sol.x[1])


def period2_residual(T, A, what, tau_cross=2.0):
    P = 2.0 * T
    ws = 0.5 * (1.0 + what)
    wc = 0.5 * (1.0 - what)
    p1 = [A % P, (T - A) % P]
    p2 = [(-A) % P, (T + A) % P]

    def activity(t, phases):
        return sum(alpha_comb(np.asarray(t) - ph, P, ALPHA) for ph in phases)

    def psi1(t):
        t = np.asarray(t)
        return ws * activity(t, p1) + wc * activity(t - tau_cross, p2)

    arrivals = []
    for ph in p1:
        for k in (-1, 0, 1, 2):
            arrivals.append(ph + k * P)
    for ph in p2:
        for k in (-1, 0, 1, 2):
            arrivals.append(ph + tau_cross + k * P)

    def gain(a, b):
        return split_int(
            lambda t: response(psi1(t)),
            a,
            b,
            [x for x in arrivals if a < x < b],
        )

    r1 = 2.0 * PI - gain(A, T - A)
    r2 = 2.0 * PI - gain(T - A, 2.0 * T + A)
    return np.array([r1, r2])


def solve_period2(Tstar, wstar, delta):
    what = wstar + delta

    def residual(z):
        T, A = z
        r = period2_residual(T, A, what)
        return np.array([0.5 * (r[0] + r[1]), (r[0] - r[1]) / (2.0 * A)])

    sol = root(
        residual,
        np.array([Tstar + 0.116 * delta, math.sqrt(0.5373 * delta)]),
        tol=1e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return float(sol.x[0]), abs(float(sol.x[1]))


def flip_map_coefficient(Tstar, wstar, Lhist=4, h=1e-3):
    ws = 0.5 * (1.0 + wstar)
    wc = 0.5 * (1.0 - wstar)
    W = np.array([[ws, wc], [wc, ws]])
    D = np.array([[0.0, 2.0], [2.0, 0.0]])
    P = SpikeHistoryMap(W, Tstar, D, history_length=Lhist)
    x0 = np.zeros(2 * Lhist)
    L = jacobian_fd(P, x0)
    q = np.array(
        [((-1) ** r) * v for r in range(Lhist) for v in (1.0, -1.0)],
        dtype=float,
    )
    vals, vecs = np.linalg.eig(L.T)
    p = np.real(vecs[:, np.argmin(np.abs(vals + 1.0))])
    p /= p @ q

    Bqq = (P(h * q) - 2.0 * P(x0) + P(-h * q)) / h**2
    h2 = np.linalg.solve(np.eye(len(q)) - L, Bqq)
    Cqqq = diagonal_C(P, q, h)
    Bqh2 = mixed_B(P, q, h2, h)
    cf = (p @ Cqqq) / 6.0 + 0.5 * (p @ Bqh2)
    return float(cf), float(np.linalg.norm(L @ q + q))


# ---------------------------------------------------------------------------
# N=3 ring Neimark--Sacker

KAPPA = 2.0 * PI / 3.0
RING_DELAYS = np.array([0.0, 2.0, 5.0])


def ring_weights(p):
    return np.array([1.0, p, -p])


def ring_sync_residual(T, p):
    w = ring_weights(p)
    return 2.0 * PI - split_int(
        lambda s: response(
            sum(wd * alpha_comb(np.asarray(s) - td, T, ALPHA)
                for wd, td in zip(w, RING_DELAYS))
        ),
        0.0,
        T,
        [td % T for td in RING_DELAYS],
    )


def ring_E(mu, T, p, qsector=1):
    w = ring_weights(p)

    def psi(s):
        return sum(wd * alpha_comb(np.asarray(s) - td, T, ALPHA)
                   for wd, td in zip(w, RING_DELAYS))

    H = 0.0j
    for d, (wd, td) in enumerate(zip(w, RING_DELAYS)):
        phase = np.exp(-1j * KAPPA * qsector * d)
        H += wd * phase * split_int(
            lambda s, td=td: response_prime(psi(s))
            * q_weighted(np.asarray(s) - td, T, ALPHA, mu),
            0.0,
            T,
            [x % T for x in RING_DELAYS],
        )
    nu = float(response(psi(0.0)))
    return nu * (complex(mu) - 1.0) - H


def solve_ns_critical():
    def residual(z):
        T, p, Omega = z
        E = ring_E(np.exp(1j * Omega), T, p)
        return np.array([ring_sync_residual(T, p), E.real, E.imag])

    sol = root(residual, np.array([15.565, -2.607, 0.272]), tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return tuple(float(x) for x in sol.x)


def ring_matrices(p):
    w = ring_weights(p)
    W = np.empty((3, 3))
    D = np.empty((3, 3))
    for i in range(3):
        for j in range(3):
            d = (i - j) % 3
            W[i, j] = w[d]
            D[i, j] = RING_DELAYS[d]
    return W, D


def physical_ring_q(mu, Lhist):
    xi = np.exp(1j * KAPPA * np.arange(3))
    return np.concatenate([(mu ** (-r)) * xi for r in range(Lhist)])


def complex_B(P, u, v, h):
    ur, ui = np.real(u), np.imag(u)
    vr, vi = np.real(v), np.imag(v)
    return (
        mixed_B(P, ur, vr, h)
        - mixed_B(P, ui, vi, h)
        + 1j * (mixed_B(P, ur, vi, h) + mixed_B(P, ui, vr, h))
    )


def complex_C(P, u, v, w, h):
    comps = [
        (np.real(u), np.imag(u)),
        (np.real(v), np.imag(v)),
        (np.real(w), np.imag(w)),
    ]
    out = np.zeros(len(u), dtype=complex)
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                out += (1j) ** (a + b + c) * mixed_C(
                    P, comps[0][a], comps[1][b], comps[2][c], h
                )
    return out


def ns_lyapunov(Tstar, pstar, Omega, Lhist=4, h=2.5e-3):
    W, D = ring_matrices(pstar)
    P = SpikeHistoryMap(W, Tstar, D, history_length=Lhist)
    x0 = np.zeros(3 * Lhist)
    L = jacobian_fd(P, x0)

    target = np.exp(1j * Omega)
    vals = np.linalg.eigvals(L)
    mu = vals[np.argmin(np.abs(vals - target))]
    q = physical_ring_q(mu, Lhist)

    vals_t, vecs_t = np.linalg.eig(L.T)
    p = vecs_t[:, np.argmin(np.abs(vals_t - np.conj(mu)))]
    p /= np.conj(np.vdot(p, q))

    Bqq = complex_B(P, q, q, h)
    Bqb = complex_B(P, q, np.conj(q), h)
    h20 = np.linalg.solve(mu**2 * np.eye(len(q)) - L, Bqq)
    h11 = np.linalg.solve(np.eye(len(q)) - L, Bqb)
    G21 = np.vdot(
        p,
        complex_C(P, q, q, np.conj(q), h)
        + complex_B(P, np.conj(q), h20, h)
        + 2.0 * complex_B(P, q, h11, h),
    )
    ell1 = 0.5 * np.real(np.exp(-1j * np.angle(mu)) * G21)
    return float(ell1), mu, float(np.linalg.norm(L @ q - mu * q) / np.linalg.norm(q))


def ns_root_for_parameter(p, Tguess, muguess):
    T = brentq(lambda x: ring_sync_residual(x, p), Tguess - 2.0, Tguess + 2.0)

    def residual(z):
        E = ring_E(z[0] + 1j * z[1], T, p)
        return np.array([E.real, E.imag])

    sol = root(residual, np.array([muguess.real, muguess.imag]), tol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return T, complex(sol.x[0], sol.x[1])


def main():
    # Generic flip critical point.
    Tflip, wflip = solve_flip_critical()
    assert abs(Tflip - 16.81736224376564) < 3e-7
    assert abs(wflip - 10.508451441614785) < 3e-7
    assert abs(two_cell_Eminus(-1.0, Tflip, wflip)) < 2e-8
    assert abs(two_cell_Eminus(1.0, Tflip, wflip).real - 0.7423135516929733) < 2e-6

    cf4, qres4 = flip_map_coefficient(Tflip, wflip, 4)
    cf5, qres5 = flip_map_coefficient(Tflip, wflip, 5)
    assert qres4 < 2e-6 and qres5 < 2e-6
    assert abs(cf4 - 0.5502495) < 2e-4
    assert abs(cf5 - 0.5502496) < 2e-4
    assert abs(cf4 - cf5) < 5e-5

    Tp2, Ap2 = solve_period2(Tflip, wflip, 1e-4)
    ratio = Ap2**2 / 1e-4
    assert abs(ratio - 0.5373) < 2e-3

    # N=3 ring NS point.
    Tns, pns, Omega = solve_ns_critical()
    assert abs(Tns - 15.565320495514536) < 5e-7
    assert abs(pns + 2.6069763661290217) < 5e-7
    assert abs(Omega - 0.27168810585706804) < 5e-7

    ell4, mu4, res4 = ns_lyapunov(Tns, pns, Omega, 4)
    ell5, mu5, res5 = ns_lyapunov(Tns, pns, Omega, 5)
    assert res4 < 2e-6 and res5 < 2e-6
    assert abs(abs(mu4) - 1.0) < 2e-6
    assert abs(abs(mu5) - 1.0) < 2e-6
    assert abs(ell4 - 0.0051639) < 2e-4
    assert abs(ell5 - 0.0051639) < 2e-4
    assert abs(ell4 - ell5) < 5e-5

    # Radial crossing speed from independently solved characteristic roots.
    hp = 1e-4
    _, mup = ns_root_for_parameter(pns + hp, Tns, mu4)
    _, mum = ns_root_for_parameter(pns - hp, Tns, mu4)
    radial_slope = (abs(mup) - abs(mum)) / (2.0 * hp)
    assert abs(radial_slope + 0.1093172533) < 2e-4

    print("CORE v0.7 reference checks passed")
    print("flip critical:", Tflip, wflip)
    print("flip c_f L4/L5:", cf4, cf5)
    print("period-two delta=1e-4:", Tp2, Ap2, "A^2/delta=", ratio)
    print("NS critical:", Tns, pns, Omega, mu4)
    print("NS ell1 L4/L5:", ell4, ell5)
    print("NS radial slope:", radial_slope)


if __name__ == "__main__":
    main()
