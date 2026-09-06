"""Global hybrid invariant-circle fold reference for CORE v0.15.

This reference builds on the full packet-queue engine from CORE v0.14. The
large timing-modulated object crosses an arrival-order switching surface, so
the smooth fixed-itinerary map of v0.11 must not be used for its global fold.

Default invocation checks the stored direct-trajectory diagnostics and the
independent square-root multiplier fit. The expensive direct trajectory modes
can be rerun from the repository root with

    python reference/core_v015_global_circle_fold.py --classification
    python reference/core_v015_global_circle_fold.py --stable-direct

The direct modes are deliberately separated because each requires thousands
of exact packet-queue event cycles.
"""

from __future__ import annotations

import argparse
import copy
import math
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import least_squares

from core_v014_adaptive_event_engine import N, bistability_test, response_scalar

PI = math.pi
TAU_FOLD_ESCAPE = 8.00731041

TAU_MULT = np.array([8.004, 8.006, 8.007, 8.0072, 8.00725])
MU_STABLE_ROT = np.array([
    0.7843122830695624,
    0.8649936837658590,
    0.9358154754108635,
    0.9612338114815638,
    0.9717922535166069,
])

RHO_8 = 0.0385142956218183
Q26_RMS = 0.006298346383219713
FOURIER10_RMS = 0.00023750306235774808
FOURIER10_C1 = 0.7161579099407992
SHORT_MARGIN_MIN = -0.31152993330033496
SHORT_MARGIN_MAX = 4.703420753940009

MU_STABLE_72 = 0.9612338114815638
MU_UNSTABLE_72 = 1.0400409851593622


def cycle_Z(engine):
    times = np.array([engine.spike_times[i][-1] for i in range(N)], dtype=float)
    mean = float(times.mean())
    xi = np.exp(-1j * 2.0 * PI * np.arange(N) / N)
    return complex(np.dot(times - mean, xi) / N)


def set_tau(engine, tau):
    engine.c = 1.0 / float(tau)
    engine.c0 = engine.c
    engine.epsilon = 0.0
    engine.rate = 0.0
    engine.kappa = 0.0


def collect_Z(engine, cycles):
    out = np.empty(cycles, dtype=complex)
    for k in range(cycles):
        engine.run_cycles(1)
        out[k] = cycle_Z(engine)
    return out


def radial_phi_perturb(engine, delta_A):
    z = cycle_Z(engine)
    theta = np.angle(z)
    kappa = 2.0 * PI / 3.0
    desired_dt = 2.0 * delta_A * np.cos(theta + kappa * np.arange(N))
    nu = np.array([response_scalar(float(x)) for x in engine.psi])
    engine.phi += -nu * desired_dt


def radial_spline(Z):
    theta = np.mod(np.angle(Z), 2.0 * PI)
    radius = np.abs(Z)
    order = np.argsort(theta)
    t = theta[order]
    r = radius[order]
    te = np.concatenate([t - 2.0 * PI, t, t + 2.0 * PI])
    re = np.concatenate([r, r, r])
    return CubicSpline(te, re)


def section_values(unwrapped_phase, values, theta0=0.0):
    phase = np.asarray(unwrapped_phase)
    values = np.asarray(values)
    k0 = math.ceil((phase[0] - theta0) / (2.0 * PI))
    k1 = math.floor((phase[-1] - theta0) / (2.0 * PI))
    out = []
    for k in range(k0, k1 + 1):
        target = theta0 + 2.0 * PI * k
        j = int(np.searchsorted(phase, target))
        if j <= 0 or j >= len(phase):
            continue
        w = (target - phase[j - 1]) / (phase[j] - phase[j - 1])
        out.append((1.0 - w) * values[j - 1] + w * values[j])
    return np.asarray(out)


def stable_rotation_multiplier(base, spline, delta_A, cycles):
    trial = copy.deepcopy(base)
    radial_phi_perturb(trial, delta_A)
    Z = collect_Z(trial, cycles)
    dev = np.array([
        abs(z) - float(spline(np.mod(np.angle(z), 2.0 * PI))) for z in Z
    ])
    phase = np.unwrap(np.angle(Z))
    sec = section_values(phase, dev)
    ratios = []
    floor = max(2.0e-8, abs(delta_A) * 0.01)
    for k in range(3, min(len(sec) - 1, 100)):
        if (
            abs(sec[k]) > floor
            and abs(sec[k + 1]) > floor
            and sec[k] * sec[k + 1] > 0.0
        ):
            q = sec[k + 1] / sec[k]
            if 0.5 < q < 1.2:
                ratios.append(q)
    if len(ratios) < 8:
        raise RuntimeError("insufficient normal-return samples")
    return float(np.median(ratios))


def fit_fold(taus, multipliers):
    taus = np.asarray(taus, dtype=float)
    y = 1.0 - np.asarray(multipliers, dtype=float)

    def residual(z):
        K, tau_f = z
        return K * np.sqrt(np.maximum(tau_f - taus, 1.0e-20)) - y

    sol = least_squares(
        residual,
        np.array([3.7, 8.00731]),
        bounds=([0.0, float(taus.max()) + 1.0e-10], [100.0, 8.02]),
        xtol=1.0e-14,
        ftol=1.0e-14,
        gtol=1.0e-14,
    )
    rms = float(np.sqrt(np.mean(sol.fun**2)))
    return float(sol.x[0]), float(sol.x[1]), rms


def stored_checks():
    K5, tf5, rms5 = fit_fold(TAU_MULT, MU_STABLE_ROT)
    K3, tf3, rms3 = fit_fold(TAU_MULT[-3:], MU_STABLE_ROT[-3:])

    assert abs(tf5 - 8.00730554) < 3.0e-7
    assert abs(tf3 - 8.00731073) < 5.0e-7
    assert rms5 < 8.0e-4
    assert rms3 < 4.0e-4
    assert abs(tf3 - TAU_FOLD_ESCAPE) < 1.0e-6

    assert MU_STABLE_72 < 1.0 < MU_UNSTABLE_72
    assert abs(MU_UNSTABLE_72 - 1.0 / MU_STABLE_72) < 6.0e-4

    assert abs(RHO_8 - 1.0 / 26.0) > 5.0e-5
    assert Q26_RMS > 5.0e-3
    assert FOURIER10_RMS < 4.0e-4
    assert abs(FOURIER10_C1 - 0.71615791) < 5.0e-6
    assert SHORT_MARGIN_MIN < 0.0 < SHORT_MARGIN_MAX

    print("CORE v0.15 stored hybrid-circle-fold checks passed")
    print("five-point multiplier fold:", K5, tf5, rms5)
    print("near-fold three-point fit:", K3, tf3, rms3)
    print("escape-ghost fold:", TAU_FOLD_ESCAPE)
    print("stable/unstable return multipliers:", MU_STABLE_72, MU_UNSTABLE_72)


def classification_direct():
    _, _, _, _, large8 = bistability_test()
    Z = collect_Z(large8, 8000)
    m = np.arange(len(Z), dtype=float)
    phase = np.unwrap(np.angle(Z))
    slope, intercept = np.polyfit(m, phase, 1)
    rho = float(slope / (2.0 * PI))

    q26 = float(np.sqrt(np.mean(np.abs(Z[26:] - Z[:-26]) ** 2)))

    theta = slope * m + intercept
    M = 10
    ks = np.arange(-M, M + 1)
    X = np.column_stack([np.exp(1j * k * theta) for k in ks])
    coeff = np.linalg.lstsq(X, Z, rcond=None)[0]
    fit = X @ coeff
    rms = float(np.sqrt(np.mean(np.abs(Z - fit) ** 2)))
    c1 = float(abs(coeff[np.where(ks == 1)[0][0]]))

    K = 5000
    margins = []
    for i in range(N):
        src = (i - 1) % N
        ti = np.asarray(large8.spike_times[i][-K:])
        ts = np.asarray(large8.spike_times[src][-K:]) + 2.0
        margins.extend((ts - ti).tolist())

    assert abs(rho - RHO_8) < 5.0e-6
    assert abs(q26 - Q26_RMS) < 2.0e-3
    assert rms < 6.0e-4
    assert abs(c1 - FOURIER10_C1) < 2.0e-3
    assert min(margins) < -0.2 and max(margins) > 4.0

    print("direct large-circle classification passed")
    print("rho=", rho, "q26 RMS=", q26, "Fourier10 RMS/c1=", rms, c1)
    print("short-arrival margin=", min(margins), max(margins))


def stable_direct():
    _, _, _, _, engine = bistability_test()
    set_tau(engine, 8.0072)
    engine.run_cycles(8000)
    Zref = collect_Z(engine, 5000)
    spline = radial_spline(Zref)

    vals = []
    for delta in (2.0e-6, 8.0e-6):
        vals.append(stable_rotation_multiplier(engine, spline, delta, 2800))

    assert max(abs(x - MU_STABLE_72) for x in vals) < 5.0e-3
    assert abs(vals[0] - vals[1]) < 5.0e-3
    print("direct stable normal multipliers at tau=8.0072:", vals)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--classification", action="store_true")
    parser.add_argument("--stable-direct", action="store_true")
    args = parser.parse_args()

    stored_checks()
    if args.classification:
        classification_direct()
    if args.stable_direct:
        stable_direct()


if __name__ == "__main__":
    main()
