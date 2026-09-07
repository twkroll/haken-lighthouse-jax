# Lighthouse-JAX — Canonical Project Status

Version: 1.6
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. Recovery, mathematical-scope canonicalization, governed v0.2 validation, v0.3 continuation-theory canonicalization and v0.3 continuation-validation-contract canonicalization have completed.

MASTER reviews `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md` and accepts its PASS. The gate pre-specifies a finite deterministic validation suite V3C01–V3C09 for RB-007 without executing any validation, numerical Lighthouse continuation or critical-point search.

MASTER therefore establishes `CORE v0.3 Continuation Validation Contract Freeze 0.1` as RB-008 in `research/core/v0_3_continuation_validation_contract_freeze_0_1.md`.

RB-008 freezes the common reference state R0; execution precision; arrival-aware integration; five-point derivative stencils and fixed derivative steps; chart margins; E0/V3-N1/V3-N2/V3-D1/V3-A1/L0 tolerances; V3C01–V3C09 membership and every subcase/negative control; PASS/FAIL/INVALID rules; software-plumbing audit rules; complete-suite rule; and DFR-V3-01 through DFR-V3-12.

At freeze time V3C01–V3C09 are UNEVALUATED. No Lighthouse fold/pitchfork result, v0.4 stability object or downstream effect claim is promoted.

MASTER authorizes exactly one next scientific action: `CORE v0.3 Continuation Validation Execution Gate 0.1`, which must execute V3C01–V3C09 exactly under RB-008 and return PASS, FAIL or CONDITIONAL.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting governed V3C01–V3C09 execution result |
| 10 CORE | READY | execute v0.3 Continuation Validation Execution Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.6
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- Legacy CORE downstream claims: NON-CANONICAL / NOT FROZEN except material separately promoted through governed gates
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## Frozen scientific layers

### RB-004 — mathematical baseline

Freezes canonical baseline equations, event/delay semantics, assumptions, variant registry and elementary identities D1–D18.

### RB-006 — governed v0.2 validation

Result remains:

`PASS — BC01–BC10 ALL PASS UNDER RB-005`.

### RB-007 — v0.3 continuation theory

Freezes normalized phase coordinates, fixed-domain branch operator, phase Jacobian, fixed-physical-delay period derivative, scalar-parameter derivative, gauge structure, pseudo-arclength algebra as method definition, event/admissibility qualifications, existence/stability/hybrid/chart taxonomy and exchange-symmetric two-cell block structure with corrected negative antisymmetric coefficient `B`.

### RB-008 — v0.3 validation contract

Frozen source:

`research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`

V3C01–V3C09 cover:

1. coordinate equivalence and global gauge;
2. phase Jacobian and gauge-null identity;
3. fixed-physical-delay period derivative and scalar parameter derivative;
4. synthetic pseudo-arclength fold machinery only;
5. exchange-symmetric two-cell block structure and `B`;
6. synthetic pitchfork algebra only;
7. elementary transversality and first-hitting controls;
8. arrival-aware handling under RB-007 chart qualifications;
9. exact regular branch sensitivity.

The contract uses fixed deterministic cases and forbids parameter search, step-size scan, stochasticity and post-output tolerance changes.

## Branch-independent results

- Governance process 0.1: STABLE.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 v0.2 benchmark contract: STABLE pre-execution contract.
- RB-006 governed v0.2 analytical validation: STABLE scientific result freeze.
- RB-007 v0.3 continuation theory: STABLE scientific theory freeze.
- RB-008 v0.3 continuation validation contract: STABLE pre-execution contract.

## Branch-dependent scientific results

No downstream legacy numerical effect result is canonical scientific evidence unless separately promoted through a governed gate.

V3C01–V3C09 are UNEVALUATED at RB-008 establishment.

No Lighthouse continuation branch, fold location, pitchfork location/scaling, Floquet spectrum, stability boundary or downstream effect has been promoted.

## Result classifications

- RB-004 mathematical statements retain their frozen epistemic labels.
- RB-006: governed analytical validation PASS.
- RB-007: narrow v0.3 continuation mathematics frozen with explicit conditional/deferred boundaries.
- RB-008: pre-execution validation contract only; no result classification yet.
- No STRONG, WEAK, NULL or FAIL classification is assigned to downstream legacy effect results.

## Execution boundary

The next gate must execute every V3C01–V3C09 case exactly under RB-008. It may not change model choices, graph, parameters, common reference state, derivative conventions, finite-difference steps, chart margins, solver steps, tolerances, references, benchmark membership or PASS/FAIL rules after observing output.

A scientifically valid failure must be preserved. A software-plumbing correction is permitted only under the frozen audit rule and requires rerunning all affected validation families from the beginning.

## Active blocker

RB-008 has not yet been executed. Until governed V3C01–V3C09 execution returns:

- no Lighthouse continuation or critical-point search;
- no v0.4+ recovery execution;
- no production implementation continuation;
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

## Manuscript

WAIT. Existing freezes do not authorize manuscript claims based on downstream legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized until MASTER explicitly opens LIT.

## Cross-branch integration

The baseline, governed v0.2 validation, narrow v0.3 continuation theory and the frozen v0.3 validation contract are integrated on `main` without merging `core/theory-v0.1`.

Further integration remains gate-by-gate.

## Next global step

Execute `CORE v0.3 Continuation Validation Execution Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_3_continuation_validation_execution_gate_0_1.md`

The gate must execute V3C01–V3C09 exactly under RB-008 and return PASS, FAIL or CONDITIONAL to MASTER. It may not start a second gate.

After CORE creates `research/core/v0_3_continuation_validation_execution_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.3 CONTINUATION VALIDATION EXECUTION GO
