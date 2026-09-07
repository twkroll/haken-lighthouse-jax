# CORE v0.3 Continuation Theory Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-007

## Authority

MASTER authorizes this narrow theory freeze after PASS of `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`.

Frozen source artifact:

- file: `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`
- blob SHA: `7c04401994b749f7918ff74c8e27339bcaf3d3c7`
- creation commit: `ebb85eaa5f53282e6c5144bf43872b1af38d25f7`

Underlying authorities remain:

- RB-004 `CORE Mathematical Freeze 0.1`
- RB-005 `CORE Benchmark Contract Freeze 0.1`
- RB-006 `CORE v0.2 Benchmark Result Freeze 0.1`

## Frozen contents

The following contents of the source artifact are frozen:

1. normalized phase-coordinate map and unwrapped continuation coordinates, (V3.1)–(V3.5);
2. baseline normalized branch operator with no external drive, (V3.6)–(V3.9);
3. phase-coordinate Jacobian and gauge identities, (V3.10)–(V3.13);
4. fixed-physical-delay period derivative and local/almost-everywhere comb-period derivative, (V3.14)–(V3.18), only under the stated regularity assumptions;
5. general scalar-parameter derivative, (V3.19)–(V3.20), under stated differentiability assumptions;
6. exact global gauge invariance and the rule that wrapped phase crossings are coordinate boundaries rather than physical singularities;
7. pseudo-arclength equations (V3.22)–(V3.24) as a project method definition only, with no implementation or performance claim;
8. smooth-chart and arrival-kink qualifications from Section 8;
9. event transversality and first-hitting admissibility, (V3.26)–(V3.27);
10. the strict taxonomy separating existence regularity/singularity, dynamical stability, hybrid/event-chart singularity, and representation/chart boundaries;
11. the regular-branch implicit-function theorem statement and generic fold statement only conditionally on the stated local `C^2` regularity and nondegeneracy assumptions;
12. exchange-symmetric two-cell parity, block diagonalization and corrected negative antisymmetric coefficient `B`, (V3.29)–(V3.31);
13. the C1–C5 classifications and explicit exclusions recorded in the gate.

## Canonical repairs relative to legacy v0.3

The freeze explicitly preserves two corrections from the audit:

1. For the frozen smooth baseline response C2, threshold contact `Psi=h` is not by itself a nonsmooth branch boundary. Hard-threshold / Heaviside contact theory belongs only to separately authorized nonsmooth variants.
2. Alpha-kernel arrival collisions are event-chart / representation boundaries and do not automatically imply rank loss or discontinuity of the integrated existence Jacobian.

The independently re-derived two-cell antisymmetric coefficient carries the negative sign

`B = -T^2 w_c integral_0^1 S'(Psi_0) R_T'(T sigma - tau_c) d sigma`.

This resolves the historical sign erratum at the mathematical level.

## Freeze boundary

RB-007 does **not** freeze, validate or authorize:

- any numerical continuation branch;
- any actual Lighthouse fold or pitchfork location;
- any B11–B22 benchmark output or legacy tolerance;
- any continuation step-size or corrector-performance claim;
- any v0.4 Floquet spectrum, multiplier or stability boundary;
- any numerically estimated normal-form coefficient;
- unconditional `C^2` or `C^3` regularity of the exact alpha branch operator across moving/coincident arrival kinks;
- unconditional baseline pitchfork coefficients/scaling;
- adaptive-delay dynamics or commensurability effects;
- v0.4+ theory, v0.6+ numerical atlas work, production/JAX implementation, inference, observation design, active experiment design, v0.27, application claims or novelty claims.

The legacy branch `core/theory-v0.1` remains read-only recovery evidence and is not merged.

## Change control

Any change to the frozen v0.3 continuation theory requires a new MASTER-authorized gate and a new versioned freeze. Future numerical or algorithmic validation must be governed by a pre-execution contract fixed before outputs are observed.

## STOP

`CORE v0.3 Continuation Theory Freeze 0.1` is established.

STOP — FROZEN
