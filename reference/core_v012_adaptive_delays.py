"""Reference slow-fast benchmark for CORE v0.12 adaptive delays.

This script does not yet implement a fully state-dependent-delay event network.
It couples the exact frozen NS/FIC numbers certified by CORE v0.11 to the
reduced radial Chenciner envelope and a slow conduction-speed plasticity law.

Run from the repository root with

    python reference/core_v012_adaptive_delays.py
"""

from __future__ import annotations

import math

from scipy.integrate import solve_ivp
from scipy.optimize import brentq

P_ADAPT = -3.267985407948901
TAU_FIC = 7.94140373739
A_FIC = 0.0660575
L2 = 0.021546133331
T_NS_REF = 16.297496058505022
TAU_NS_REF = 7.941411830425917
OMEGA_NS_REF = 0.265668898005473
S_TAU_REF = -0.050533543527464524

TAU_TARGET = TAU_FIC - 5.0e-5
C0 = 1.0 / TAU_TARGET
U_S = 0.03**2
KAPPA = 2.0e-6
A_SEED = 1.0e-3
ESCAPE_A = 0.1

WINDOW = TAU_NS_REF - TAU_FIC
BETA1_FIC = S_TAU_REF * (TAU_FIC - TAU_NS_REF)
BETA2_EFF = -math.sqrt(4.0 * L2 * BETA1_FIC)
A_FIC_CAL = math.sqrt(-BETA2_EFF / (2.0 * L2))


def H(u):
    return u / (u + U_S)


def reduced_rhs(eps, kappa):
    def rhs(n, y):
        A, c = y
        tau = 1.0 / c
        beta1 = S_TAU_REF * (tau - TAU_NS_REF)
        radial = A * (beta1 + BETA2_EFF * A**2 + L2 * A**4)
        dc = eps * (C0 - c + kappa * H(A * A))
        return [radial, dc]

    return rhs


def integrate_to_fic(eps, kappa, seed=A_SEED):
    def event_fic(n, y):
        return 1.0 / y[1] - TAU_FIC

    event_fic.terminal = True
    event_fic.direction = -1

    sol = solve_ivp(
        reduced_rhs(eps, kappa),
        [0.0, 4.0e9],
        [seed, 1.0 / TAU_NS_REF],
        events=event_fic,
        rtol=2e-9,
        atol=[1e-12, 1e-15],
        max_step=2.0e5,
    )
    if not len(sol.t_events[0]):
        raise RuntimeError("FIC not reached")
    return float(sol.t_events[0][0]), float(sol.y_events[0][0, 0])


def integrate_escape(eps, kappa, seed=A_SEED):
    def event_fic(n, y):
        return 1.0 / y[1] - TAU_FIC

    event_fic.terminal = False
    event_fic.direction = -1

    def event_escape(n, y):
        return y[0] - ESCAPE_A

    event_escape.terminal = True
    event_escape.direction = 1

    sol = solve_ivp(
        reduced_rhs(eps, kappa),
        [0.0, 4.0e9],
        [seed, 1.0 / TAU_NS_REF],
        events=[event_fic, event_escape],
        rtol=2e-9,
        atol=[1e-12, 1e-15],
        max_step=2.0e5,
    )
    if not len(sol.t_events[0]) or not len(sol.t_events[1]):
        raise RuntimeError("FIC or escape threshold not reached")
    nf = float(sol.t_events[0][0])
    ne = float(sol.t_events[1][0])
    tau_escape = float(1.0 / sol.y_events[1][0, 1])
    return nf, ne, ne - nf, tau_escape


def tracking_epsilon(kappa, fraction=0.9):
    target = fraction * A_FIC

    def f(logeps):
        _, A = integrate_to_fic(10.0**logeps, kappa)
        return A - target

    return 10.0 ** brentq(f, -9.7, -8.0, xtol=5e-6)


def linear_capture_bound(seed=A_SEED):
    c_ns = 1.0 / TAU_NS_REF
    sweep_factor = TAU_NS_REF**2 * (C0 - c_ns)
    gain_required = math.log(A_FIC / seed)
    v_tau = abs(S_TAU_REF) * WINDOW**2 / (2.0 * gain_required)
    return v_tau / sweep_factor


def main():
    # Frozen exact skeleton / radial calibration.
    assert WINDOW > 0.0
    assert abs(WINDOW - 8.09303591698e-6) < 2e-15
    assert abs(BETA1_FIC - 4.08969782780e-7) < 2e-17
    assert abs(BETA2_EFF + 1.877414974706e-4) < 2e-16
    assert abs(A_FIC_CAL - 0.066005552315) < 2e-12
    assert abs(A_FIC_CAL - A_FIC) / A_FIC < 8e-4

    # Optimistic linear capture estimate.
    eps_lin = linear_capture_bound()
    assert abs(eps_lin - 6.7979341220e-9) < 3e-13

    # Nonlinear 90% tracking thresholds.
    eps90_no = tracking_epsilon(0.0)
    eps90_fb = tracking_epsilon(KAPPA)
    assert abs(eps90_no - 1.7303e-9) / eps90_no < 3e-3
    assert abs(eps90_fb - 5.8264e-10) / eps90_fb < 3e-3
    assert eps90_fb < eps90_no / 2.8

    # Representative slow passage: the static stable-circle window is skipped.
    n_no, A_no = integrate_to_fic(1e-6, 0.0)
    n_fb, A_fb = integrate_to_fic(1e-6, KAPPA)
    assert abs(A_no - 0.00103191) < 2e-6
    assert abs(A_fb - 0.00103182) < 2e-6
    assert A_no / A_FIC < 0.02 and A_fb / A_FIC < 0.02

    # Local post-FIC escape trigger.
    nf_no, ne_no, lag_no, tau_e_no = integrate_escape(1e-6, 0.0)
    nf_fb, ne_fb, lag_fb, tau_e_fb = integrate_escape(1e-6, KAPPA)
    assert lag_fb < lag_no
    assert tau_e_fb < tau_e_no

    base = C0 - 1.0 / TAU_NS_REF
    accel = (base + KAPPA * H(A_FIC**2)) / base
    assert abs(accel - 2.79995) < 2e-4

    print("CORE v0.12 adaptive-delay reduced checks passed")
    print("fixed coupling p=", P_ADAPT)
    print("frozen NS T/tau/Omega=", T_NS_REF, TAU_NS_REF, OMEGA_NS_REF)
    print("frozen NS-FIC window=", WINDOW)
    print("beta2_eff=", BETA2_EFF, "A_FIC_cal=", A_FIC_CAL)
    print("linear optimistic epsilon capture bound=", eps_lin)
    print("epsilon_90 no-feedback / feedback=", eps90_no, eps90_fb)
    print("eps=1e-6 cycles to FIC no-feedback / feedback=", n_no, n_fb)
    print("eps=1e-6 A_at_FIC no-feedback / feedback=", A_no, A_fb)
    print("eps=1e-6 post-FIC escape lag no-feedback / feedback=", lag_no, lag_fb)
    print("tau at escape no-feedback / feedback=", tau_e_no, tau_e_fb)
    print("activity acceleration factor at FIC=", accel)


if __name__ == "__main__":
    main()
