# Lighthouse-JAX — Canonical Project Status

Version: 1.7
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. Recovery, mathematical-scope canonicalization, governed v0.2 validation, v0.3 continuation-theory canonicalization, v0.3 validation-contract canonicalization and governed v0.3 validation execution have completed.

MASTER reviews the corrected `research/core/v0_3_continuation_validation_execution_gate_0_1.md` and accepts its PASS.

Result:

`PASS — V3C01–V3C09 ALL PASS UNDER RB-008`.

The post-write V3C04 issue is accepted as a clerical/result-serialization defect under the already frozen RB-008 software-plumbing rule. V3C04 was rerun from the beginning with the unchanged scientific contract and remained PASS; the incorrect preliminary table remains preserved and invalidated in Git history.

MASTER therefore establishes `CORE v0.3 Continuation Validation Result Freeze 0.1` as RB-009 in `research/core/v0_3_continuation_validation_result_freeze_0_1.md`.

RB-009 validates only the deterministic v0.3 C2 layer. It does not promote a Lighthouse continuation branch, Lighthouse fold/pitchfork location, Floquet multiplier, stability boundary, v0.4 result or downstream effect.

Recovery classifies legacy v0.3–v0.5 theory contracts C1/C2 by claim. The next coherent layer is v0.4 spike-time Floquet/symmetry mathematics. MASTER therefore authorizes exactly one next scientific action: `CORE v0.4 Floquet Theory Canonicalization Gate 0.1`.

That gate is mathematical/source verification only. It must not execute B23–B40, search actual Lighthouse multipliers, select a stability boundary, start v0.5 normal forms or continue downstream legacy science.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.4 Floquet-theory canonicalization result |
| 10 CORE | READY | execute v0.4 Floquet Theory Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.7
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-009 CORE v0.3 Continuation Validation Result Freeze 0.1: FROZEN / STABLE RESULT
- Legacy CORE downstream claims: NON-CANONICAL / NOT FROZEN except material separately promoted through governed gates
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## Frozen scientific layers

### RB-004 — mathematical baseline

Canonical baseline equations, event/delay semantics, assumptions, variant registry and elementary identities D1–D18.

### RB-006 — governed v0.2 validation

`PASS — BC01–BC10 ALL PASS UNDER RB-005`.

### RB-007 — v0.3 continuation theory

Normalized phase coordinates, fixed-domain branch operator, phase Jacobian, fixed-physical-delay period derivative, scalar-parameter derivative, gauge structure, pseudo-arclength algebra as a method definition, event/admissibility qualifications, existence/stability/hybrid/chart taxonomy and exchange-symmetric two-cell block structure with corrected negative antisymmetric coefficient `B`.

### RB-008 — v0.3 validation contract

Finite deterministic pre-execution contract V3C01–V3C09 with fixed parameters, derivative conventions, stencils, chart margins, tolerances, negative controls and PASS/FAIL/INVALID rules.

### RB-009 — v0.3 validation result

`PASS — V3C01–V3C09 ALL PASS UNDER RB-008`.

Key frozen result classes include coordinate/gauge equivalence, analytic-vs-five-point derivative agreement, synthetic pseudo-arclength fold machinery, exchange-symmetry/`B` checks, synthetic pitchfork algebra, first-hitting/transversality controls, arrival-aware chart behavior and exact regular autapse sensitivity.

The declared V3C08 arrival-boundary pointwise derivative remains `ARRIVAL_CHART_BOUNDARY / DERIVATIVE_INVALID` exactly as required by RB-008; the integrated quantity remains valid and passes.

## V3C04 correction disposition

The preliminary human-readable V3C04 table in commit `872199d6f885489898d64ac8bf957c629770d249` was a transcription/serialization error. CORE reran V3C04 from the beginning under unchanged RB-008 and produced the corrected record committed at `f94049ef4037a0687384dafb01a042219592b53d`.

MASTER accepts the correction because no scientific specification changed and the incorrect preliminary table is retained but invalidated as evidence. This does not reopen RB-008.

## Branch-independent results

- Governance process 0.1: STABLE.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 v0.2 benchmark contract: STABLE pre-execution contract.
- RB-006 governed v0.2 validation: STABLE scientific result freeze.
- RB-007 v0.3 continuation theory: STABLE scientific theory freeze.
- RB-008 v0.3 continuation validation contract: STABLE pre-execution contract.
- RB-009 governed v0.3 continuation validation: STABLE scientific result freeze.

## Branch-dependent scientific results

No downstream legacy numerical effect result is canonical scientific evidence unless separately promoted through a governed gate.

No actual Lighthouse continuation branch, fold location, pitchfork location/scaling, Floquet spectrum, stability boundary or active-design effect has been promoted.

## v0.4 recovery disposition

Legacy v0.4 contains three relevant mathematical/contract artifacts at frozen recovery SHA `287eae8a86560b78ed94f30a2786243714c33ac0`:

- `docs/core/spike_time_floquet_v0.4.md`;
- `docs/core/symmetry_reductions_v0.4.md`;
- `docs/core/floquet_contract_v0.4.md`.

The first two contain C1/C2-eligible mathematical candidates: spike-time recurrence, nonlinear characteristic operator, exact neutral time-translation mode, alpha weighted derivative-comb representation, multiplier/exponent conventions, two-cell/ring Fourier reductions, cluster quotient conditions and general symmetry-sector structure.

The third contains legacy B23–B40 validation ideas. These are not adopted or executed now. Their test membership/tolerances must be re-canonicalized only after the mathematical v0.4 layer has passed a dedicated audit.

## Active blocker

A canonical v0.4 Floquet/symmetry mathematical layer does not yet exist. Until `CORE v0.4 Floquet Theory Canonicalization Gate 0.1` returns and MASTER decides on it:

- no B23–B40 execution;
- no actual Lighthouse multiplier/root search;
- no stability-boundary search or stability atlas;
- no v0.5 normal-form execution;
- no v0.6+ recovery execution;
- no production/JAX Floquet implementation continuation;
- no active hybrid experiment design;
- no v0.27;
- no application execution;
- no independent novelty positioning;
- no manuscript claim freeze.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE
2. RB-002 CORE Legacy Recovery Input Snapshot 0.1 at `287eae8a86560b78ed94f30a2786243714c33ac0` — STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
3. RB-003 CORE Recovery Classification 0.1 — STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
4. RB-004 CORE Mathematical Freeze 0.1 — FROZEN / STABLE SCIENTIFIC BASELINE
5. RB-005 CORE Benchmark Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
6. RB-006 CORE v0.2 Benchmark Result Freeze 0.1 — FROZEN / STABLE RESULT
7. RB-007 CORE v0.3 Continuation Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY
8. RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
9. RB-009 CORE v0.3 Continuation Validation Result Freeze 0.1 — FROZEN / STABLE RESULT

## Manuscript

WAIT. Existing freezes do not authorize manuscript claims based on downstream legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized until MASTER explicitly opens LIT. Source verification inside the authorized CORE theory gate is permitted only as provenance work, not novelty positioning.

## Cross-branch integration

The baseline, governed v0.2 validation, v0.3 continuation theory, its frozen validation contract and governed validation PASS are integrated on `main` without merging `core/theory-v0.1`.

Further integration remains gate-by-gate.

## Next global step

Execute `CORE v0.4 Floquet Theory Canonicalization Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_4_floquet_theory_canonicalization_gate_0_1.md`

The gate must audit/re-derive the mathematical spike-time Floquet and symmetry layer only. It may not execute B23–B40 or start a second gate.

After CORE creates `research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.4 FLOQUET THEORY CANONICALIZATION GO
