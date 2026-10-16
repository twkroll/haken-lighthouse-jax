# NUM-ENG Numerical Engineering Freeze 0.2

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING BASELINE EXTENSION
Rollback point: RB-021

## Authority

MASTER reviews and accepts the returned:

`NUM-ENG Robustness, Scaling & Differentiable Kernel Gate 0.2`

from development branch:

`engineering/numerics-v0.1`.

Frozen authorities:

- returned gate file: `research/numerical_engineering/robustness_scaling_differentiable_kernel_gate_0_2.md`;
- returned gate blob SHA: `8a4fdafda23db56feff70b17e787b63264b63398`;
- prospective stress-matrix commit: `a43314a881437bdc05352cb58f357515c5555f89`;
- prospective defect-repair addendum commit: `780a38b53bd1864ea514a59db553dc8e132c9532`;
- strengthened batch-guard overlay blob: `5606c09aed4dc18202af199f3323062562606d8d`;
- local engineering bundle SHA-256: `762b4467dc30dbaba5ebf24dd662d66f8c87e8d12c4bb086d73d710891292fc6`;
- archive-content manifest SHA-256: `9062c26caa93853de43001de6d5e51c4bb1a6ba0f48a2ed0ede79755664a9e15`;
- baseline physical authority: RB-019 / `NUMENG_PULSE_AWARE_REFERENCE_V1`.

No RB-019 physical-reference source file is replaced by RB-021.

## Gate result

`PASS — ENGINEERING ONLY`

All evidence remains DEVELOPMENT EVIDENCE / LOCAL ENGINEERING METRICS unless a later scientific contract explicitly promotes a claim.

## Frozen robustness result

The prospectively fixed deterministic stress matrix is retained as the Gate-0.2 acceptance authority.

Frozen observations:

- 17/17 dense-vs-sparse physical comparisons PASS;
- max labelled-event time discrepancy: approximately `6.66e-15`;
- max final-phase discrepancy: approximately `7.11e-15`;
- fail-closed invalid controls behave as required for collision, initial-boundary, horizon-boundary and event-budget cases;
- the deliberately insufficient integration-segment budget reports an explicit uncertified failure rather than silently accepting a partial chart.

These results are finite-fixture engineering evidence, not a theorem of global simulator correctness.

## Acceleration classification

The predeclared accelerated comparisons pass 28/28 finite comparisons against the unchanged RB-019 physical authority.

Three additional historical accelerators were inspected only as exploratory development diagnostics.

All six retained acceleration paths remain:

`DEVELOPMENT COMPARATOR`.

None is an independent physical authority and none may replace `NUMENG_PULSE_AWARE_REFERENCE_V1` without a later explicit gate with its own fail-closed certification domain.

No universal speedup claim is frozen.

## Differentiable-kernel result

On the predetermined regular G01 chart:

- fixed-chart JAX replay agrees with physical spike times within approximately `9.6e-14`;
- weight, delay and initial-phase AD-vs-physically-rerecorded finite-difference discrepancies are all below approximately `5.5e-10`;
- JVP/VJP dot-product and JVP/Jacobian consistency checks agree to floating-point precision.

This validates only the tested regular-chart/domain configuration.

Direct unguarded fixed-chart JAX remains a conditional computational primitive, not an independent physical certificate.

## Batch-tape defect and repair

Gate 0.2 discovered, documented and prospectively repaired a high-level batch-guard defect:

a stale physically certified base tape with event timestamps shifted while preserving the same event token could be accepted by `guarded_batch_replay`.

The defect was recorded before repair-validation outputs in the frozen addendum commit `780a38b...`.

RB-021 accepts the versioned high-level validation overlay that now physically rerecords and verifies:

- physical certification;
- topology/signature/token;
- event count and event times;
- spike/event coherence;
- initial arrived-edge mapping;
- finite/consistent initial alpha state;
- final phase consistency.

The direct low-level fixed-chart primitive remains explicitly unguarded.

Added prospective repair QA: 8/8 PASS.

## Regression / process validation

Frozen QA chronology:

- Gate-0.2 stress suite: 48/48 PASS, repeated twice with clean exits;
- RB-019 baseline aggregate: 194/194 PASS, clean exit;
- dedicated batch-guard repair QA: 8/8 PASS;
- patched targeted suite: 56/56 PASS;
- patched aggregate: 250/250 PASS, clean exit.

The environment and runtime controls are part of the gate provenance.

No protected RNG namespace was used.

## Local scaling observations

RB-021 retains the deterministic N/E work and storage measurements only as local engineering metrics.

The audited sparse family used approximately E=2N for N in {5,12,24,48}.

Observed alpha-state storage is linear in E for the two float64 alpha arrays, while the corresponding dense representation scales with N^2 for those arrays.

Observed event/work counters and wall times are recorded exactly in the Gate-0.2 report.

No empirical complexity exponent, universal runtime law, hardware-independent speedup, or end-to-end performance claim is frozen.

## Component disposition

### ENGINEERING-APPROVED WITH DOMAIN

Within the explicitly tested finite domain:

- unchanged RB-019 physical reference;
- strengthened high-level base-tape validation overlay;
- deterministic stress/gradient harness;
- local state-memory/work accounting;
- fail-closed chart/tape handling covered by the frozen QA.

### DEVELOPMENT COMPARATOR

- all six accelerated first-hit paths;
- direct unguarded JAX fixed-chart primitive;
- prior optimizer/learning smoke tests;
- timing extrapolations.

### DEFERRED

- global first-hit correctness;
- formal interval certification;
- independent hardware/GPU portability;
- universal scaling/speedup claims;
- AI/training performance.

### REJECTED

- token equality alone as physical-tape certification;
- unverified accelerated tapes as physical authority;
- scientific/AI claims inferred from local Gate-0.2 engineering measurements.

## Scientific boundaries

RB-021 does not:

- change RB-004 mathematics;
- relabel RB-015 SCIENTIFIC FAIL;
- execute TR-27C;
- create any `2711xxx` RNG object;
- authorize APP-3;
- create a scientific scaling/speedup claim;
- merge executable source to `main`;
- authorize novelty/manuscript claims.

## STOP

`NUM-ENG Numerical Engineering Freeze 0.2` is established.

STOP — FROZEN / STABLE ENGINEERING BASELINE EXTENSION
