"""Independent reference checks for CORE v0.9.

This script reuses only the exact-event/characteristic utilities from v0.8.
It independently verifies the smooth NS orbit, the cubic degeneracy, the NS
locus tangent and radial transversality.  The fifth-order AD coefficients are
stored as certified reference numbers and are checked algebraically here; their
full derivation is documented in docs/core/chenciner_v0.9.md.

Run from the repository root with

    python reference/core_v09_chenciner.py
"""

from __future__ import annotations

import math
import numpy as np

from core_v08_codimension_two import (
    event_map_ell1,
    ring_psi,
    response,
    solve_ns_at_tau3,
    characteristic_root_for_p,
)

TSTAR = 16.29213672114
PSTAR = -3.26248414452
TAUSTAR = 7.92140373739
OMEGASTAR = 0.266095330801
MU_STAR = complex(0.964805044716, 0.262966206367)

B1_IMAG = -0.04254970545
B2_REAL = 0.020640894614
B2_IMAG = 0.003792391324
L2_REF = 0.021546133331


def main():
    # Re-solve the q=1 NS orbit at the stored tau3.
    z = solve_ns_at_tau3(TAUSTAR, [TSTAR, PSTAR, OMEGASTAR])
    if isinstance(z, tuple):
        z = z[0]
    T, p, Omega = map(float, z)
    mu = np.exp(1j * Omega)

    assert abs(T - TSTAR) < 2e-5
    assert abs(p - PSTAR) < 2e-5
    assert abs(Omega - OMEGASTAR) < 2e-5
    assert abs(abs(mu) - 1.0) < 1e-12

    # Smoothness / admissibility audit by dense sampling.
    ss = np.linspace(0.0, T, 4001, endpoint=False)
    psi = np.asarray(ring_psi(ss, T, p, TAUSTAR), dtype=float)
    assert float(np.min(psi) + 1.0) > 0.5
    nu = float(response(ring_psi(0.0, T, p, TAUSTAR)))
    assert nu > 0.4
    assert 0.0 < 2.0 < TAUSTAR < T

    # Direct exact-event cubic coefficient: L1 must vanish at Chenciner.
    ell4, mu4, qres4 = event_map_ell1(T, p, Omega, TAUSTAR, 4)
    ell5, mu5, qres5 = event_map_ell1(T, p, Omega, TAUSTAR, 5)
    assert qres4 < 3e-6 and qres5 < 3e-6
    assert abs(abs(mu4) - 1.0) < 3e-6
    assert abs(abs(mu5) - 1.0) < 3e-6
    assert abs(ell4) < 2e-5 and abs(ell5) < 2e-5

    # Tangent derivative dL1/dtau3 along the NS locus.
    ht = 0.02
    zp = solve_ns_at_tau3(TAUSTAR + ht, [T, p, Omega])
    zm = solve_ns_at_tau3(TAUSTAR - ht, [T, p, Omega])
    if isinstance(zp, tuple):
        zp = zp[0]
    if isinstance(zm, tuple):
        zm = zm[0]
    ep, _, _ = event_map_ell1(float(zp[0]), float(zp[1]), float(zp[2]), TAUSTAR + ht, 4)
    em, _, _ = event_map_ell1(float(zm[0]), float(zm[1]), float(zm[2]), TAUSTAR - ht, 4)
    dL_dtau_ns = (ep - em) / (2.0 * ht)
    dp_dtau_ns = (float(zp[1]) - float(zm[1])) / (2.0 * ht)
    assert abs(dL_dtau_ns + 0.0092975) < 3e-4
    assert abs(dp_dtau_ns + 0.2748216) < 3e-4

    # Radial transversality at fixed tau3 from characteristic roots.
    hp = 1e-4
    _, mup = characteristic_root_for_p(PSTAR + hp, TSTAR, MU_STAR, TAUSTAR)
    _, mum = characteristic_root_for_p(PSTAR - hp, TSTAR, MU_STAR, TAUSTAR)
    dabs_dp = (abs(mup) - abs(mum)) / (2.0 * hp)
    assert abs(dabs_dp + 0.18379443) < 5e-4

    # Fifth-order reference arithmetic and Chenciner nondegeneracy.
    L2 = 0.5 * (B1_IMAG**2 + 2.0 * B2_REAL)
    assert abs(L2 - L2_REF) < 2e-12
    assert L2 > 0.0

    # Strong-resonance exclusion through order six.
    distances = [abs(np.exp(1j * k * Omega) - 1.0) for k in range(1, 7)]
    assert min(distances) > 0.2

    det_unfold = dabs_dp * dL_dtau_ns
    assert abs(det_unfold) > 1e-3

    print("CORE v0.9 Chenciner reference checks passed")
    print("critical:", T, p, TAUSTAR, Omega, mu)
    print("L1 L4/L5:", ell4, ell5)
    print("dL1/dtau3|NS:", dL_dtau_ns)
    print("dp_NS/dtau3:", dp_dtau_ns)
    print("d|mu|/dp:", dabs_dp)
    print("b2:", complex(B2_REAL, B2_IMAG), "L2:", L2)
    print("unfolding determinant:", det_unfold)


if __name__ == "__main__":
    main()
