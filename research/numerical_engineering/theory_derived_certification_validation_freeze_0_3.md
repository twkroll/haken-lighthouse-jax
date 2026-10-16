# NUM-ENG Theory-Derived Certification Validation Freeze 0.3

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING THEORY-VALIDATION RESULT
Rollback point: RB-023

## Authority

MASTER reviews and accepts the returned:

`NUM-ENG Theory-Derived First-Hit Certification Validation Gate 0.3`

from branch:

`engineering/numerics-v0.1`.

Frozen provenance:

- finite pre-execution contract commit: `7a488ed6777d206313c512f437216b05b8e5eb6e`;
- contract blob SHA: `5e3abad7975d912def807d1e41feac6a9bda319e`;
- returned gate blob SHA: `abc32fb5bd9005d2c71040a963b3541a13e5967a`;
- raw result blob SHA: `eb903139f27d4f2cf522ae89635a645221afca21`;
- execution-log blob SHA: `3f576b9e7dfa933036d3161eb49a64fd13cc46b6`;
- physical authority: RB-019 / `NUMENG_PULSE_AWARE_REFERENCE_V1`;
- numerical baseline extension: RB-021;
- frozen theory authority: RB-022.

The finite validation contract was committed before Gate-0.3 outputs were generated.

No fixture/tolerance retuning after output is accepted into RB-023.

## Gate result

`PASS — THEORY-CONSISTENT ENGINEERING VALIDATION (finite, non-formal)`

RB-023 is not a scientific effect result and does not establish formal interval arithmetic, global first-hit correctness, universal chart certification, scaling/speedup or AI performance.

## Frozen result matrix

The prospectively fixed TV-01 through TV-11 families all PASS within their finite contract.

This includes:

- exact alpha-state propagation;
- analytic extrema;
- strict no-hit certificate cases;
- unique regular first-hit bracket cases;
- response derivative bounds;
- alpha-tail mass and finite phase-error bounds;
- regular-chart perturbation persistence;
- local event-time derivatives;
- repaired structural-zero semantics;
- TH-FH-01 through TH-FH-08;
- stale-tape / itinerary-change fail-closed controls.

Zero/equality-margin controls remain classified `UNCERTIFIED` rather than being mislabelled as physical failure.

Exact collision/boundary fixtures remain distinguished as physically meaningful but ordinary-chart invalid where appropriate.

## Decisive finite observations

### Narrow-pulse first hit

For TH-FH-01:

\[
t_{\rm physical}
=
0.5050005053634212,
\]

while the independent segmented quadrature/root reference gives

\[
t_{\rm ref}
=
0.5050005053634210.
\]

Absolute discrepancy:

\[
2.22\times10^{-16}.
\]

The preregistered strict bracket passes without tuning.

### Omitted-history phase bound

Finite omitted-history phase discrepancy:

\[
0.023643397381274,
\]

with frozen theorem-derived upper bound:

\[
0.0325178946640312.
\]

Equality-margin and missing-summability controls remain `UNCERTIFIED`.

### Regular-chart empirical margins

Across the fixed TV-07 perturbation set, the smallest observed empirical margins are approximately:

\[
\nu_{\min}=0.36790092,
\]

\[
\delta_{\rm sep}=0.0027747987,
\]

\[
\delta_{\rm bdry}=0.19437144.
\]

These are finite observed margins only. They are not frozen as rigorous globally valid chart-radius certificates.

### Local derivatives

Maximum absolute AD versus physically rerecorded centered finite-difference discrepancies:

- nonzero structural weight: \(6.09\times10^{-10}\);
- structural zero weight: \(5.42\times10^{-10}\);
- active delay: \(3.02\times10^{-10}\);
- structural-zero delay: \(3.55\times10^{-11}\);
- initial phase: \(1.90\times10^{-10}\).

Fixed-chart JAX replay versus physically certified spike times:

\[
\max |\Delta t|
\approx 9.59\times10^{-14}.
\]

For the structural-zero historical arrival:

\[
D_{\tau_e}A_e
\approx
0.99999999999989,
\]

consistent with the frozen +1 derivative for a fixed launch time.

## TH-FH fixture disposition

RB-023 freezes finite validation consistency of TH-FH-01 through TH-FH-08 exactly as executed under the preregistered contract.

In particular:

- TH-FH-01: certified regular narrow-pulse hit;
- TH-FH-02: certified no-hit;
- TH-FH-03: regular positive-velocity case plus under-resolved `UNCERTIFIED` control;
- TH-FH-04: opposite event orders across perturbations; exact tie physically valid but ordinary-chart invalid;
- TH-FH-05: finite tail certificate plus equality/summability `UNCERTIFIED` controls;
- TH-FH-06: topology-fixed structural-zero semantics validated;
- TH-FH-07: interior/horizon-boundary/no-hit trichotomy;
- TH-FH-08: commuting simultaneous arrivals physically valid but sequential ordinary chart invalid.

## Process / compatibility boundary

Gate-0.3 validation itself completed twice with clean exit code 0.

Three targeted previously frozen modules completed:

`28 tests PASS / exit 0`.

A fresh attempt to rerun the broader previously frozen 250-case aggregate exceeded the external execution-time limit and produced no trustworthy final exit/PASS summary.

RB-023 records this as:

`NOT REPEATED IN GATE 0.3 — NO NEW PASS/FAIL CLASSIFICATION`.

This does not invalidate RB-021's independently frozen 250/250 QA result and is not converted into a new implementation failure.

No Gate-0.3 source change to the RB-019/RB-021 physical/reference implementation was required.

## Formal-rigor limitation

The Gate-0.3 gain enclosure machinery uses exact analytic scalar extrema evaluated in float64 and deterministic refinement.

It is not an outward-rounded interval implementation.

Therefore RB-023 does not establish:

- rigorous floating-point inclusion;
- formal machine-verifiable first-hit certification;
- formal outward-rounded phase-gain bounds;
- globally certified chart radii;
- global first-hit completeness.

These remain open for the next Theory → Numerics cycle.

## Classification

### THEORY-CONSISTENT ENGINEERING VALIDATION

- TV-01…TV-11 finite contract;
- TH-FH-01…TH-FH-08 finite fixture family;
- local event-time derivatives;
- structural-zero chart semantics;
- finite first-hit/no-hit consistency;
- stale-tape fail-closed behavior.

### UNCERTIFIED

- zero/equality-margin cases;
- deliberately under-resolved positive-velocity cases;
- theorem uses lacking required summability assumptions.

### DEFERRED

- outward interval arithmetic;
- formal inclusion proofs in floating point;
- global chart-radius algorithms;
- global first-hit certification;
- full portability rerun beyond already frozen RB-021 evidence.

## Preserved governance boundaries

RB-023 does not:

- alter RB-015 SCIENTIFIC FAIL;
- execute RB-020/TR-27C;
- create any `2711xxx` RNG object;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- create universal numerical-performance claims;
- merge executable engineering source into `main`;
- authorize novelty/manuscript claims.

## STOP

RB-023 freezes only the bounded finite theory-consistency engineering validation.

STOP — FROZEN / STABLE ENGINEERING THEORY-VALIDATION RESULT
