"""Reference algebra for CORE v0.10 local Chenciner unfolding.

This file checks the physical-to-normal-form linear map, invariant-circle roots,
stability sectors, and the fold initializer.  Certification of actual Lighthouse
invariant circles requires the exact-event collocation problem documented in
`docs/core/chenciner_unfolding_v0.10.md`; transient simulation is deliberately not
used as a pass/fail oracle near the Chenciner point.
"""

from __future__ import annotations

import math
import numpy as np

L2 = 0.021546133331
M = np.array(
    [
        [-0.18379443, -0.0505106793],
        [0.08625, 0.0144058630],
    ],
    dtype=float,
)
NS_SLOPE = -0.27482160
DL1_DTAU_NS = -0.0092975000


def beta(dp, dtau):
    return M @ np.array([dp, dtau], dtype=float)


def circle_roots(beta1, beta2):
    disc = beta2 * beta2 - 4.0 * L2 * beta1
    if disc < 0.0:
        return []
    sq = math.sqrt(disc)
    out = []
    for u in ((-beta2 - sq) / (2.0 * L2), (-beta2 + sq) / (2.0 * L2)):
        if u > 0.0:
            out.append(math.sqrt(u))
    return out


def radial_restoring_sign(r, beta2):
    u = r * r
    return beta2 + 2.0 * L2 * u


def main():
    det = float(np.linalg.det(M))
    assert abs(det - 0.0017088287) < 2e-8
    assert abs(det) > 1e-3

    # NS tangent follows beta1=0.
    slope = -M[0, 1] / M[0, 0]
    assert abs(slope - NS_SLOPE) < 3e-7

    # beta2 changes sign along the NS tangent at Chenciner.
    d_beta2_ns = M[1, 0] * NS_SLOPE + M[1, 1]
    assert abs(d_beta2_ns - DL1_DTAU_NS) < 3e-5
    assert d_beta2_ns < 0.0

    # Canonical two-circle wedge example.
    b1, b2 = 1e-6, -5e-4
    roots = circle_roots(b1, b2)
    assert len(roots) == 2
    rin, rout = roots
    assert abs(rin - 0.04701677) < 2e-6
    assert abs(rout - 0.14489804) < 2e-6
    assert radial_restoring_sign(rin, b2) < 0.0
    assert radial_restoring_sign(rout, b2) > 0.0

    # Fold condition and fold radius.
    b2f = -5e-4
    b1f = b2f * b2f / (4.0 * L2)
    rf = math.sqrt(-b2f / (2.0 * L2))
    roots_f = circle_roots(b1f, b2f)
    assert len(roots_f) == 2
    assert abs(roots_f[0] - rf) < 2e-6
    assert abs(roots_f[1] - rf) < 2e-6

    # Linear-map FIC initializer in the physical plane.
    k = (DL1_DTAU_NS**2 / (4.0 * L2)) / M[0, 0]
    assert abs(k + 0.00545721) < 2e-6

    # Sector checks.
    assert len(circle_roots(-1e-6, 5e-4)) == 1   # subcritical side
    assert len(circle_roots(1e-6, 5e-4)) == 0
    assert len(circle_roots(-1e-6, -5e-4)) == 1
    assert len(circle_roots(1e-6, -5e-4)) == 2

    print("CORE v0.10 unfolding checks passed")
    print("unfolding matrix=\n", M)
    print("determinant=", det)
    print("NS slope=", slope)
    print("d beta2/dtau along NS=", d_beta2_ns)
    print("two-circle radii=", roots)
    print("FIC initializer quadratic coefficient=", k)


if __name__ == "__main__":
    main()
