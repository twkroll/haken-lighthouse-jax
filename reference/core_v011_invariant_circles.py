"""Exact-event invariant-circle reference for CORE v0.11.

This is the first CORE reference that intentionally uses JAX automatic
differentiation.  Earlier SciPy/Numpy references remain independent oracles for
existence/Floquet data; v0.11 uses JAX specifically because the smooth
state-space alpha-synapse event map removes the high-order finite-difference
artifacts diagnosed in v0.8--v0.10.

Run from the repository root with

    python reference/core_v011_invariant_circles.py
"""

from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares

import jax
import jax.numpy as jnp

from core_v08_codimension_two import solve_ns_at_tau3

jax.config.update("jax_enable_x64", True)

PI = math.pi
ALPHA = 0.5
KAPPA = 2.0 * PI / 3.0
L_HIST = 4

TAU_STAR = 7.92140373739
T_STAR = 16.29213672114
P_STAR = -3.26248414452
OMEGA_STAR = 0.266095330801
L2 = 0.021546133331
DL1_DTAU_NS = -0.0092975
DABS_DP = -0.18379443

TAU_TEST = TAU_STAR + 0.02
NS_REF = np.array([16.29749389161298, -3.26798318225628, 0.26566907110085])
C2_EXACT = -0.00100847923835
C2_NF = -0.0010117281573766954
A_FIC_REF = 0.0660575
DP_FIC_REF = -2.225692621316e-6
A_FIC_NF = 0.06568987296649076
DP_FIC_NF = -2.1828841395119243e-6

GX, GW = leggauss(32)
GX = jnp.asarray(GX)
GW = jnp.asarray(GW)


def response(x):
    y = x + 1.0
    return jnp.where(y > 0.0, jnp.exp(-1.0 / (y * y)), 0.0)


def flow_state(psi, q, dt):
    e = jnp.exp(-ALPHA * dt)
    return e * (psi + q * dt), e * q


def integrate_interval(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    psi_s = e * (psi + q * s)
    return 0.5 * dt * jnp.sum(GW * response(psi_s))


def initial_state(history, T, p, tau3, i):
    """Exact recent history plus analytic unperturbed tail at current spike."""
    a = history[0, i]
    weights = (1.0, p, -p)
    delays = (0.0, 2.0, tau3)
    rho = jnp.exp(-ALPHA * T)
    psi = 0.0
    q = 0.0

    for disp in range(3):
        j = (i - disp) % 3
        w = weights[disp]
        delay = delays[disp]

        # Current self-arrival is exactly at the integration start.
        if disp == 0:
            age0 = a - history[0, j] - delay
            q = q + w * ALPHA**2 * jnp.exp(-ALPHA * age0)
            psi = psi + w * ALPHA**2 * age0 * jnp.exp(-ALPHA * age0)

        # Explicit recent past spikes.
        for r in range(1, L_HIST):
            age = a + r * T - history[r, j] - delay
            e = jnp.exp(-ALPHA * age)
            q = q + w * ALPHA**2 * e
            psi = psi + w * ALPHA**2 * age * e

        # Infinite unperturbed tail r >= L_HIST.
        age_L = a + L_HIST * T - delay
        e_L = jnp.exp(-ALPHA * age_L)
        q = q + w * ALPHA**2 * e_L / (1.0 - rho)
        psi = psi + w * ALPHA**2 * e_L * (
            age_L / (1.0 - rho) + T * rho / (1.0 - rho) ** 2
        )

    return psi, q


def gain_and_terminal_psi(delta, history, T, p, tau3, i):
    a = history[0, i]
    psi, q = initial_state(history, T, p, tau3, i)

    j1 = (i - 1) % 3
    j2 = (i - 2) % 3
    t1 = history[0, j1] + 2.0
    t2 = history[0, j2] + tau3

    total = 0.0

    dt = t1 - a
    total = total + integrate_interval(psi, q, dt)
    psi, q = flow_state(psi, q, dt)
    q = q + p * ALPHA**2

    dt = t2 - t1
    total = total + integrate_interval(psi, q, dt)
    psi, q = flow_state(psi, q, dt)
    q = q - p * ALPHA**2

    dt = T + delta - t2
    total = total + integrate_interval(psi, q, dt)
    psi, q = flow_state(psi, q, dt)
    return total, psi


def next_spike(history, T, p, tau3, i):
    delta = 0.0
    for _ in range(7):
        gain, psi_end = gain_and_terminal_psi(delta, history, T, p, tau3, i)
        delta = delta - (gain - 2.0 * PI) / response(psi_end)
    return delta


def event_map(x, T, p, tau3):
    history = x.reshape((L_HIST, 3))
    delta = jnp.stack([next_spike(history, T, p, tau3, i) for i in range(3)])
    gauge = jnp.mean(delta)
    rows = [delta - gauge]
    for r in range(1, L_HIST):
        rows.append(history[r - 1] - gauge)
    return jnp.stack(rows).reshape((-1,))


class CircleSolver:
    def __init__(self, M=5, J=14):
        self.M = int(M)
        self.J = int(J)
        self.phases = jnp.asarray(np.linspace(0.0, 2.0 * PI, self.J, endpoint=False))

        labels = []
        # Current block: gauge removes all spatially uniform n == 0 mod 3 modes.
        for n in range(1, self.M + 1):
            if n % 3 == 0:
                continue
            for kind in ("a", "b"):
                if n == 1:  # fixed amplitude/phase pair
                    continue
                labels.append((0, n, kind))

        # Older history blocks retain gauge-generated uniform components.
        for r in range(1, L_HIST):
            labels.append((r, 0, "a"))
            for n in range(1, self.M + 1):
                labels.append((r, n, "a"))
                labels.append((r, n, "b"))

        self.labels = labels
        self.nc = len(labels)

        self._residual = jax.jit(self._residual_impl)
        self._jacobian = jax.jit(jax.jacfwd(self._residual_impl, 0))
        self._dres_dA = jax.jit(jax.jacfwd(self._residual_impl, 1))

    def K(self, coeff, phases, A):
        out = []
        for phi in phases:
            rows = []
            for r in range(L_HIST):
                values = []
                for i in range(3):
                    theta = phi + KAPPA * i
                    value = 2.0 * A * jnp.cos(theta) if r == 0 else 0.0
                    for k, (rr, n, kind) in enumerate(self.labels):
                        if rr != r:
                            continue
                        if n == 0:
                            basis = 1.0
                        elif kind == "a":
                            basis = jnp.cos(n * theta)
                        else:
                            basis = jnp.sin(n * theta)
                        value = value + coeff[k] * basis
                    values.append(value)
                rows.append(jnp.stack(values))
            out.append(jnp.stack(rows).reshape((-1,)))
        return jnp.stack(out)

    def _residual_impl(self, u, A, tau3):
        coeff = u[: self.nc]
        T, p, omega = u[self.nc : self.nc + 3]
        K0 = self.K(coeff, self.phases, A)
        Kshift = self.K(coeff, self.phases + omega, A)
        P = jax.vmap(lambda x: event_map(x, T, p, tau3))(K0)
        residual = (P - Kshift).reshape((-1,))

        # The gauge-fixed map alone would hide a common period error; enforce
        # zero phase-gain residual on the synchronous orbit explicitly.
        zero_history = jnp.zeros((L_HIST, 3))
        gain0, _ = gain_and_terminal_psi(0.0, zero_history, T, p, tau3, 0)
        return jnp.concatenate([residual, jnp.array([gain0 - 2.0 * PI])])

    def initial(self, A, T, p, omega):
        u = np.zeros(self.nc + 3)
        mu = np.exp(1j * omega)
        values = {}
        for r in range(1, L_HIST):
            z = mu ** (-r)
            values[(r, 1, "a")] = 2.0 * A * z.real
            values[(r, 1, "b")] = -2.0 * A * z.imag
        for k, label in enumerate(self.labels):
            u[k] = values.get(label, 0.0)
        u[self.nc : self.nc + 3] = [T, p, omega]
        return u

    def solve(self, A, tau3, ns, previous=None):
        if previous is None:
            u0 = self.initial(A, *ns)
            dtau = tau3 - TAU_STAR
            beta2 = DL1_DTAU_NS * dtau
            beta1 = -beta2 * A**2 - L2 * A**4
            u0[self.nc + 1] += beta1 / DABS_DP
        else:
            A0, u0 = previous
            u0 = u0.copy()
            ratio = A / A0
            for k, (_, n, _) in enumerate(self.labels):
                u0[k] *= ratio**2 if n == 0 else ratio**n

        fun = lambda u: np.asarray(self._residual(jnp.asarray(u), A, tau3), dtype=float)
        jac = lambda u: np.asarray(self._jacobian(jnp.asarray(u), A, tau3), dtype=float)
        sol = least_squares(
            fun,
            u0,
            jac=jac,
            xtol=2e-13,
            ftol=2e-13,
            gtol=2e-13,
            max_nfev=15,
        )
        return sol.x, fun(sol.x)

    def dp_dA(self, u, A, tau3):
        J = np.asarray(self._jacobian(jnp.asarray(u), A, tau3), dtype=float)
        rA = np.asarray(self._dres_dA(jnp.asarray(u), A, tau3), dtype=float)
        du = np.linalg.lstsq(J, -rA, rcond=None)[0]
        return float(du[self.nc + 1])

    def dense_residual(self, u, A, tau3, Jdense=112):
        coeff = jnp.asarray(u[: self.nc])
        T, p, omega = map(float, u[self.nc : self.nc + 3])
        phases = jnp.asarray(np.linspace(0.0, 2.0 * PI, Jdense, endpoint=False))
        K0 = self.K(coeff, phases, A)
        Kshift = self.K(coeff, phases + omega, A)
        P = jax.vmap(lambda x: event_map(x, T, p, tau3))(K0)
        return np.asarray(P - Kshift)


def critical_projection(solver, u, A, tau3):
    coeff = jnp.asarray(u[: solver.nc])
    T, p, omega = map(float, u[solver.nc : solver.nc + 3])
    phases = jnp.asarray(np.linspace(0.0, 2.0 * PI, solver.J, endpoint=False))
    K0 = solver.K(coeff, phases, A)
    Kshift = solver.K(coeff, phases + omega, A)
    P = np.asarray(jax.vmap(lambda x: event_map(x, T, p, tau3))(K0))
    R = P - np.asarray(Kshift)
    phase_np = np.asarray(phases)
    Rhat = np.mean(R * np.exp(-1j * phase_np)[:, None], axis=0)

    L = np.asarray(jax.jacfwd(lambda x: event_map(x, T, p, tau3))(jnp.zeros(12)))
    vals = np.linalg.eigvals(L)
    target = np.exp(1j * omega)
    mu = vals[np.argmin(np.abs(vals - target))]
    xi = np.exp(1j * KAPPA * np.arange(3))
    q = np.concatenate([mu ** (-r) * xi for r in range(L_HIST)])
    vals_t, vecs_t = np.linalg.eig(L.T)
    left = vecs_t[:, np.argmin(np.abs(vals_t - np.conj(mu)))]
    left /= np.conj(np.vdot(left, q))
    return abs(np.vdot(left, Rhat))


def main():
    # Re-solve the NS reference point using the independent characteristic code.
    ns = solve_ns_at_tau3(TAU_TEST, NS_REF)
    if isinstance(ns, tuple):
        ns = ns[0]
    ns = np.asarray(ns, dtype=float)
    assert np.max(np.abs(ns - NS_REF)) < 2e-7

    solver = CircleSolver(M=5, J=14)

    # Local branch and quadratic scaling.
    points = []
    previous = None
    for A in (0.003, 0.006, 0.009, 0.012, 0.015):
        u, residual = solver.solve(A, TAU_TEST, ns, previous)
        previous = (A, u)
        rms = float(np.sqrt(np.mean(residual**2)))
        assert rms < 1e-10
        points.append((A, u))

    Avec = np.array([x[0] for x in points])
    dp = np.array([x[1][solver.nc + 1] - ns[1] for x in points])
    fit = np.linalg.lstsq(np.column_stack([Avec**2, Avec**4]), dp, rcond=None)[0]
    c2 = float(fit[0])
    assert abs(c2 - C2_EXACT) < 2e-6
    assert abs(c2 - C2_NF) / abs(C2_NF) < 0.01

    # Independent dense-grid and critical-direction residual at A=0.012.
    u12 = points[3][1]
    dense = solver.dense_residual(u12, 0.012, TAU_TEST)
    assert np.max(np.abs(dense)) < 1e-10
    assert critical_projection(solver, u12, 0.012, TAU_TEST) < 1e-10

    # Continue through the fold using amplitude rather than p as branch parameter.
    previous = points[-1]
    fold_data = []
    for A in (0.020, 0.030, 0.040, 0.050, 0.055, 0.060, 0.065, 0.06605, 0.070, 0.075):
        u, residual = solver.solve(A, TAU_TEST, ns, previous)
        previous = (A, u)
        fold_data.append((A, u))
        assert np.sqrt(np.mean(residual**2)) < 1e-8

    # Local polynomial initializer for the fold amplitude.
    local = [(A, u[solver.nc + 1] - ns[1]) for A, u in fold_data if 0.055 <= A <= 0.075]
    aa = np.array([x[0] for x in local])
    pp = np.array([x[1] for x in local])
    center = 0.065
    poly = np.polyfit(aa - center, pp, 4)
    roots = np.roots(np.polyder(poly))
    candidates = [r.real + center for r in roots if abs(r.imag) < 1e-8 and 0.06 < r.real + center < 0.07]
    assert candidates
    Afic = float(candidates[0])

    # One final amplitude solve and implicit branch derivative.
    nearest = min(fold_data, key=lambda x: abs(x[0] - Afic))
    ufic, residual = solver.solve(Afic, TAU_TEST, ns, nearest)
    dpdA = solver.dp_dA(ufic, Afic, TAU_TEST)
    dpf = float(ufic[solver.nc + 1] - ns[1])

    assert abs(Afic - A_FIC_REF) < 2e-4
    assert abs(dpf - DP_FIC_REF) < 5e-8
    assert abs(dpdA) < 2e-6
    assert abs(Afic - A_FIC_NF) / A_FIC_NF < 0.02
    assert abs(dpf - DP_FIC_NF) / abs(DP_FIC_NF) < 0.05

    # Spectral refinement at the fold.
    fine = CircleSolver(M=7, J=22)
    uf0 = fine.initial(Afic, *ns)
    coarse_values = {lab: ufic[k] for k, lab in enumerate(solver.labels)}
    for k, lab in enumerate(fine.labels):
        uf0[k] = coarse_values.get(lab, 0.0)
    uf0[fine.nc : fine.nc + 3] = ufic[solver.nc : solver.nc + 3]

    fun = lambda u: np.asarray(fine._residual(jnp.asarray(u), Afic, TAU_TEST), dtype=float)
    jac = lambda u: np.asarray(fine._jacobian(jnp.asarray(u), Afic, TAU_TEST), dtype=float)
    refined = least_squares(fun, uf0, jac=jac, xtol=2e-13, ftol=2e-13, gtol=2e-13, max_nfev=10)
    rref = fun(refined.x)
    assert np.max(np.abs(rref)) < 1e-9
    assert abs(refined.x[fine.nc + 1] - ufic[solver.nc + 1]) < 1e-9

    print("CORE v0.11 invariant-circle reference checks passed")
    print("NS:", ns)
    print("c2 exact / normal form:", c2, C2_NF)
    print("FIC A, delta p, dp/dA:", Afic, dpf, dpdA)
    print("FIC normal form A, delta p:", A_FIC_NF, DP_FIC_NF)
    print("M7 max residual:", np.max(np.abs(rref)))


if __name__ == "__main__":
    main()
