"""CORE v0.13 in-flight conduction-delay reference.

Checks physically causal packet propagation for time-dependent conduction speed,
its relation to two common instantaneous-delay conventions, and the size of
the correction on the v0.12 adaptive benchmark.

Run from the repository root with

    python reference/core_v013_inflight_delays.py
"""

from __future__ import annotations

import math

# Frozen/adaptive data inherited from CORE v0.12.
TAU_NS = 7.941411830425917
T_NS = 16.297496058505022
WINDOW_TAU = 8.093035916978408e-6
C0 = 0.1259231150089354
KAPPA = 2e-6
U_S = 9e-4
A_SEED = 1e-3
EPS_TEST = 1e-6
ELL = 1.0

C_NS = 1.0 / TAU_NS


def H(u: float) -> float:
    return u / (u + U_S)


def arrival_linear_path(c: float, gamma: float, ell: float = ELL) -> float:
    """Physical path rule: integral_0^Delta (c+gamma t) dt = ell."""
    if abs(gamma) < 1e-30:
        return ell / c
    return 2.0 * ell / (math.sqrt(c * c + 2.0 * gamma * ell) + c)


def arrival_launch_frozen(c: float, ell: float = ELL) -> float:
    return ell / c


def arrival_receiver_instantaneous(
    c: float, gamma: float, ell: float = ELL
) -> float:
    """Instantaneous-delay/DDE sampling: Delta = ell / c(Delta)."""
    if abs(gamma) < 1e-30:
        return ell / c
    return 2.0 * ell / (math.sqrt(c * c + 4.0 * gamma * ell) + c)


def first_order_path(c: float, gamma: float, ell: float = ELL) -> float:
    tau = ell / c
    return tau - 0.5 * (gamma / c) * tau * tau


def first_order_receiver(c: float, gamma: float, ell: float = ELL) -> float:
    tau = ell / c
    return tau - (gamma / c) * tau * tau


def speed_drift_per_time(eps: float = EPS_TEST) -> float:
    forcing = C0 - C_NS + KAPPA * H(A_SEED * A_SEED)
    return eps * forcing / T_NS


def arrival_exp_v012(eps: float = EPS_TEST) -> float:
    """Exact one-flight arrival if A is frozen during the v0.12 transit.

    dc/dt=(eps/T_NS)*(c_inf-c), with
    c_inf=C0+kappa*H(A_seed^2).  The accumulated distance is integrated
    analytically and its unique zero is found by bisection.
    """
    lam = eps / T_NS
    if lam == 0.0:
        return TAU_NS

    c_inf = C0 + KAPPA * H(A_SEED * A_SEED)
    c_s = C_NS

    def distance(dt: float) -> float:
        return c_inf * dt + (c_s - c_inf) * (-math.expm1(-lam * dt)) / lam

    lo, hi = 0.0, 2.0 * TAU_NS
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if distance(mid) < ELL:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def emission_time_sensitivity(c_emit: float, c_arrive: float) -> float:
    """da/ds for an externally prescribed continuous speed profile."""
    return c_emit / c_arrive


def main() -> None:
    # Constant speed recovers the fixed-delay model exactly.
    assert arrival_linear_path(C_NS, 0.0) == TAU_NS

    # Controlled linear-ramp benchmark.
    chi = 1e-2
    gamma = chi * C_NS * C_NS / ELL
    d_launch = arrival_launch_frozen(C_NS)
    d_path = arrival_linear_path(C_NS, gamma)
    d_current = arrival_receiver_instantaneous(C_NS, gamma)

    assert d_current < d_path < d_launch
    assert abs(d_launch - 7.941411830425917) < 2e-14
    assert abs(d_path - 7.902096946944075) < 2e-13
    assert abs(d_current - 7.863547366887612) < 2e-13

    # First-order physical correction is half the current-delay correction.
    small_gamma = 1e-4 * C_NS * C_NS
    p = arrival_linear_path(C_NS, small_gamma)
    r = arrival_receiver_instantaneous(C_NS, small_gamma)
    assert abs(p - first_order_path(C_NS, small_gamma)) < 5e-8
    assert abs(r - first_order_receiver(C_NS, small_gamma)) < 2e-7

    # v0.12 physically scaled one-flight correction.
    gamma12 = speed_drift_per_time()
    d_path_linearised = arrival_linear_path(C_NS, gamma12)
    d_path_exponential = arrival_exp_v012()
    correction = TAU_NS - d_path_exponential

    assert abs(d_path_linearised - d_path_exponential) < 2e-15
    assert abs(correction - 1.4188e-11) < 3e-15
    assert correction / WINDOW_TAU < 2e-6

    # Arrival transversality / emission-time sensitivity.
    c_arrive = C_NS + gamma * d_path
    sensitivity = emission_time_sensitivity(C_NS, c_arrive)
    assert 0.0 < sensitivity < 1.0
    assert abs(sensitivity - 0.9901475429766743) < 2e-14

    print("CORE v0.13 in-flight delay checks passed")
    print("controlled ramp delays:", d_launch, d_path, d_current)
    print("v0.12 physical speed derivative:", gamma12)
    print("v0.12 one-flight correction:", correction)
    print("correction / NS-FIC window:", correction / WINDOW_TAU)
    print("arrival emission-time sensitivity:", sensitivity)


if __name__ == "__main__":
    main()
