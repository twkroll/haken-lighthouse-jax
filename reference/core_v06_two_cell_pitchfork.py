"""Independent SciPy reference for CORE v0.6 numerical benchmarks.

This is intentionally not JAX code. It provides a small double-precision
reference implementation against which event/JAX implementations can be checked.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, root

PI = math.pi


def alpha_comb(t, T, alpha):
    """Periodic alpha-kernel comb R_T(t), valid pointwise."""
    t = np.asarray(t, dtype=float)
    u = np.mod(t, T)
    r = np.exp(-alpha * T)
    return alpha**2 * np.exp(-alpha * u) * (
        u / (1.0 - r) + T * r / (1.0 - r) ** 2
    )


def alpha_comb_prime(t, T, alpha):
    """Piecewise derivative of R_T away from arrival points."""
    t = np.asarray(t, dtype=float)
    u = np.mod(t, T)
    r = np.exp(-alpha * T)
    A = u / (1.0 - r) + T * r / (1.0 - r) ** 2
    return alpha**2 * np.exp(-alpha * u) * (
        1.0 / (1.0 - r) - alpha * A
    )


def response(x, r0=1.0, h=-1.0):
    """Coombes/Haken smooth-above-threshold response."""
    x = np.asarray(x, dtype=float)
    y = x - h
    out = np.zeros_like(y)
    mask = y > 0.0
    out[mask] = np.exp(-r0 / y[mask] ** 2)
    return out.item() if out.ndim == 0 else out


def response_prime(x, r0=1.0, h=-1.0):
    x = np.asarray(x, dtype=float)
    y = x - h
    out = np.zeros_like(y)
    mask = y > 0.0
    out[mask] = np.exp(-r0 / y[mask] ** 2) * 2.0 * r0 / y[mask] ** 3
    return out.item() if out.ndim == 0 else out


def linear_nontrivial_multipliers(
    alpha, Gamma=1.0, gamma=PI, Theta=-1.0, w_hat=2.0
):
    """Exact zero-delay roots after removing the gauge factor mu-1."""
    T = (gamma * Gamma - 2.0 * PI) / Theta
    r = math.exp(-alpha * T)
    P0 = alpha**2 * T * r / (1.0 - r) ** 2
    nu = gamma * Gamma * P0 - Theta
    # nu (mu-r)^2 - gamma*w_hat*alpha^2*T*r*mu = 0
    A = nu
    B = -2.0 * nu * r - gamma * w_hat * alpha**2 * T * r
    C = nu * r * r
    roots = np.roots([A, B, C])
    roots = np.sort(np.real_if_close(roots))[::-1]
    return T, r, P0, nu, roots


# Nonlinear two-cell benchmark -----------------------------------------------

ALPHA = 0.5
W_SELF = 1.0
W_CROSS = 1.0
TAU_SELF = 0.0


def _cell_integral(T, chi, tau_cross, cell):
    if cell == 1:
        cross_shift = chi * T + tau_cross
    elif cell == 2:
        cross_shift = tau_cross - chi * T
    else:
        raise ValueError("cell must be 1 or 2")

    def integrand(s):
        psi = (
            W_SELF * alpha_comb(s - TAU_SELF, T, ALPHA)
            + W_CROSS * alpha_comb(s - cross_shift, T, ALPHA)
        )
        return response(psi)

    points = []
    p = cross_shift % T
    if 1e-12 < p < T - 1e-12:
        points.append(p)
    return quad(
        integrand,
        0.0,
        T,
        points=points,
        epsabs=1e-10,
        epsrel=1e-10,
        limit=300,
    )[0]


def Fpm(T, chi, tau_cross):
    f1 = 2.0 * PI - _cell_integral(T, chi, tau_cross, 1)
    f2 = 2.0 * PI - _cell_integral(T, chi, tau_cross, 2)
    return 0.5 * (f1 + f2), 0.5 * (f1 - f2)


def B_correct(T, tau_cross):
    """Corrected v0.3 B = + T*w_c int_0^T S'(Psi0) R'_c ds."""

    def integrand(s):
        psi = (
            W_SELF * alpha_comb(s, T, ALPHA)
            + W_CROSS * alpha_comb(s - tau_cross, T, ALPHA)
        )
        return response_prime(psi) * alpha_comb_prime(s - tau_cross, T, ALPHA)

    p = tau_cross % T
    points = [p] if 1e-12 < p < T - 1e-12 else []
    I = quad(
        integrand,
        0.0,
        T,
        points=points,
        epsabs=1e-11,
        epsrel=1e-11,
        limit=300,
    )[0]
    return T * W_CROSS * I


def solve_critical():
    sol = root(
        lambda z: np.array([Fpm(z[0], 0.0, z[1])[0], B_correct(z[0], z[1])]),
        np.array([13.43, 6.715]),
        tol=1e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return float(sol.x[0]), float(sol.x[1])


def sync_T(tau_cross):
    return brentq(lambda T: Fpm(T, 0.0, tau_cross)[0], 11.0, 16.0, xtol=1e-12)


def q_weighted(x, T, alpha, mu):
    """Floquet-weighted derivative comb from CORE v0.4 Eq. F26."""
    x = np.asarray(x, dtype=float)
    q = np.floor(x / T).astype(int)
    u = x - q * T
    r = np.exp(-alpha * T)
    mu = complex(mu)
    z = r / mu
    return (
        mu**q
        * alpha**2
        * np.exp(-alpha * u)
        * (
            (1.0 - alpha * u) / (1.0 - z)
            - alpha * T * z / (1.0 - z) ** 2
        )
    )


def Eminus(mu, T, tau_cross):
    def psi(s):
        return (
            W_SELF * alpha_comb(s, T, ALPHA)
            + W_CROSS * alpha_comb(s - tau_cross, T, ALPHA)
        )

    def integrate_complex(fun):
        p = tau_cross % T
        points = [p] if 1e-12 < p < T - 1e-12 else []
        re = quad(
            lambda s: float(np.real(fun(s))),
            0.0,
            T,
            points=points,
            epsabs=2e-10,
            epsrel=2e-10,
            limit=300,
        )[0]
        im = quad(
            lambda s: float(np.imag(fun(s))),
            0.0,
            T,
            points=points,
            epsabs=2e-10,
            epsrel=2e-10,
            limit=300,
        )[0]
        return re + 1j * im

    hs = W_SELF * integrate_complex(
        lambda s: response_prime(psi(s)) * q_weighted(s, T, ALPHA, mu)
    )
    hc = W_CROSS * integrate_complex(
        lambda s: response_prime(psi(s))
        * q_weighted(s - tau_cross, T, ALPHA, mu)
    )
    nu = response(psi(0.0))
    return nu * (complex(mu) - 1.0) - hs + hc


def reduction_coefficients(Tstar, pstar):
    h = 2e-4
    F0 = Fpm(Tstar, 0.0, pstar)[0]
    Fp_T = (
        Fpm(Tstar + h, 0.0, pstar)[0] - Fpm(Tstar - h, 0.0, pstar)[0]
    ) / (2 * h)
    Fp_cc = (
        Fpm(Tstar, h, pstar)[0]
        - 2 * F0
        + Fpm(Tstar, -h, pstar)[0]
    ) / h**2

    # B is F_{-,chi}; use direct integration rather than nested differencing.
    a = (B_correct(Tstar, pstar + h) - B_correct(Tstar, pstar - h)) / (2 * h)
    fm_chiT = (
        B_correct(Tstar + h, pstar) - B_correct(Tstar - h, pstar)
    ) / (2 * h)

    cT = -Fp_cc / (2.0 * Fp_T)
    # F_{-,chichichi}=0 at this half-period interchange point to numerical precision.
    b = -fm_chiT * Fp_cc / (2.0 * Fp_T)
    branch_ratio = -a / b

    hm = 2e-4
    E_mu = (
        Eminus(1.0 + hm, Tstar, pstar).real
        - Eminus(1.0 - hm, Tstar, pstar).real
    ) / (2.0 * hm)
    # E_-(1)=2B/T at synchrony.
    E_p = 2.0 * a / Tstar
    sigma = -E_p / E_mu
    c_chi = -sigma / branch_ratio
    return {
        "Fplus_T": Fp_T,
        "Fplus_chichi": Fp_cc,
        "Fminus_chip": a,
        "Fminus_chiT": fm_chiT,
        "c_T": cT,
        "a": a,
        "b": b,
        "branch_ratio": branch_ratio,
        "E_mu": E_mu,
        "sigma": sigma,
        "c_chi": c_chi,
    }


def solve_broken_branch(Tstar, pstar, delta_p):
    coeff = reduction_coefficients(Tstar, pstar)
    chi0 = math.sqrt(coeff["branch_ratio"] * delta_p)
    sol = root(
        lambda z: np.array(Fpm(z[0], z[1], pstar + delta_p)),
        np.array([Tstar + 2.0 * delta_p, chi0]),
        tol=1e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return float(sol.x[0]), abs(float(sol.x[1]))


def main():
    # Linear audit
    T2, _, _, _, roots2 = linear_nontrivial_multipliers(2.0)
    T5, _, _, _, roots5 = linear_nontrivial_multipliers(5.0)
    assert abs(T2 - PI) < 1e-13 and abs(T5 - PI) < 1e-13
    assert np.allclose(
        roots2,
        [0.1409982290992954, 2.473323515115286e-5],
        rtol=2e-10,
    )
    assert np.allclose(
        roots5,
        [7.466665573660435e-5, 3.041653661757237e-10],
        rtol=5e-7,
    )

    # Nonlinear critical point
    Tstar, pstar = solve_critical()
    assert abs(Tstar - 13.43069020) < 3e-6
    assert abs(pstar - 6.71534510) < 3e-6
    assert abs(pstar - 0.5 * Tstar) < 2e-7

    coeff = reduction_coefficients(Tstar, pstar)
    assert abs(coeff["branch_ratio"] - 2.02561773) < 3e-4
    assert abs(coeff["sigma"] + 0.01840410) < 3e-5
    assert abs(coeff["c_chi"] - 0.00908568) < 3e-5

    Tb, chib = solve_broken_branch(Tstar, pstar, 1e-4)
    assert abs(Tb - 13.43089020) < 3e-6
    assert abs(chib - 0.01423174) < 3e-5

    print("CORE v0.6 reference checks passed")
    print("critical:", Tstar, pstar)
    print("coefficients:", coeff)
    print("broken branch delta_p=1e-4:", Tb, chib)


if __name__ == "__main__":
    main()
