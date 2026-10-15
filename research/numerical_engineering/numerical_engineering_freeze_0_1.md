# NUM-ENG Numerical Engineering Freeze 0.1

Date: 2026-10-15
Status: FROZEN / STABLE ENGINEERING BASELINE
Rollback point: RB-019

## Authority

MASTER reviews and accepts the returned:

`NUM-ENG Reference/Rerecord Repair & Controlled Integration Gate 0.1`

from development branch:

`engineering/numerics-v0.1`.

Frozen source authorities:

- gate file: `research/numerical_engineering/reference_rerecord_repair_integration_gate_0_1.md`;
- gate blob SHA: `a93e9c2508a1c0dbf70cefcb569bd8487d605a6c`;
- source integration commit: `aa8b4ac234a1c1960a5829fc3d24982e8002105d`;
- integrated subtree: `software/numerical_engineering/reference_repair_v0_1/`;
- pre-repair contract SHA-256: `a0a7742b53159a204e815f72d7d7e53aff293825e5901fcd684b6e98f01188d4`;
- repaired working-tree manifest SHA-256: `7dd31eb6add44c719c749421d6261a9df050076b16d44e2030da728336bce71d`;
- intake authority: RB-017;
- audit authority: RB-018.

The executable source remains on the isolated engineering branch. This freeze does not merge executable software to `main`.

## Frozen gate result

`PASS — ENGINEERING ONLY`

This is not a scientific result and does not promote any timing, speedup, scaling, optimizer, learning or AI-performance claim.

## Frozen engineering baseline

RB-019 accepts, within the finite audited envelope, the following as the stable engineering baseline:

1. repaired pulse-aware dense/sparse physical first-hit authority;
2. explicit fail-closed physical-certification semantics;
3. physical rerecording as the authority for accepted event tapes;
4. high-level chart/JAX guards that reject incomplete, stale or uncertified physical tapes;
5. conditional fixed-chart JAX replay only after certified physical rerecording;
6. structural zero-weight edge representation in the audited cases;
7. analytic alpha-state propagation and fixed-delay semantics consistent with RB-004;
8. complete provenance, environment, manifest and test-log structure under the frozen engineering subtree.

Accepted physical records are tagged:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

That tag denotes finite engineering certification under this contract, not a mathematical proof of global first-hit correctness.

## Frozen pre-repair numerical contract

The prospectively fixed repair contract includes:

- pulse/arrival-aware interval segmentation;
- QUADPACK controls `epsabs=2e-13`, `epsrel=2e-12`;
- finite error-budget and analytic-tail requirements;
- Brent root solve `xtol=1e-12`, `rtol=9e-16`;
- event collision tolerance `1e-8`;
- transversality threshold `1e-10`;
- finite segment/event/search budgets;
- explicit `PHYSICAL_FIRST_HIT_UNCERTIFIED` style failure rather than silently truncated accepted tapes;
- fixed finite QA tolerances for RRI validation.

These values are engineering-quality controls. They are not scientific success thresholds and do not establish interval-arithmetic rigor.

## Validation freeze

The repaired baseline passed:

- all original 11 RB-017 modules / 180 tests with clean exits;
- 14 new RRI repair tests;
- combined aggregate run: `194 passed`, clean exit 0.

The mandatory repair matrix RRI-01 through RRI-08 passes within its explicitly finite fixture set.

In particular, the RB-018 narrow-pulse regression now yields one regular spike at approximately:

`0.5050005053634212`

and agrees with the independent segmented reference within the prospectively frozen tolerance.

## Component status

### ENGINEERING-APPROVED

Within the audited finite envelope:

- repaired dense/sparse physical reference;
- pulse-window segmentation and bounded/error-controlled adaptive quadrature;
- physical tape certification;
- fail-closed high-level chart/JAX guards;
- regular-chart conditional JAX replay with physical residual checks;
- structural-zero support;
- original plus RRI test infrastructure;
- profiling hook correction;
- complete provenance/manifest/log bundle.

### DEVELOPMENT COMPARATOR ONLY

Historical accelerated schedulers are retained for comparison and regression but remain tagged `UNVERIFIED` as independent physical authorities.

### DEFERRED

RB-019 does not establish:

- global correctness outside the explicit numerical budget/fixture envelope;
- formally rigorous interval enclosures;
- unconditional direct fixed-chart JAX validity;
- platform-independent teardown guarantees;
- general speedup or scaling laws;
- scientific meaning of the local one-weight learning smoke test;
- AI benchmark performance.

## Scientific and application boundaries

RB-019 does not:

- alter RB-004 mathematics;
- alter or rescue RB-015 SCIENTIFIC FAIL;
- authorize `2711xxx` RNG creation;
- execute or validate v0.27c confirmatory science;
- authorize APP-3 training or benchmark execution;
- create any novelty or manuscript claim;
- merge executable engineering source to `main`.

All pre-existing numerical performance and learning-smoke outputs remain DEVELOPMENT EVIDENCE.

## Future use

Future scientific or APP-3 work may use RB-019 as a frozen engineering dependency only if its own pre-execution contract specifies which RB-019 APIs/certification semantics are relied upon and preserves the relevant fail-closed boundaries.

## STOP

`NUM-ENG Numerical Engineering Freeze 0.1` is established.

STOP — FROZEN / STABLE ENGINEERING BASELINE
