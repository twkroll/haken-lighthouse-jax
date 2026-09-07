# Lighthouse-JAX — Canonical Project Status

Version: 1.5
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. Recovery, mathematical-scope canonicalization, governed v0.2 benchmark-contract canonicalization, governed v0.2 benchmark execution, and v0.3 continuation-theory canonicalization have completed.

MASTER reviews `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md` and accepts its PASS. The gate independently re-derives and qualifies the recoverable v0.3 mathematical continuation layer without executing numerical continuation or B11–B22.

MASTER therefore establishes `CORE v0.3 Continuation Theory Freeze 0.1` as RB-007 in `research/core/v0_3_continuation_theory_freeze_0_1.md`.

RB-007 freezes normalized phase coordinates, the fixed-domain branch operator, phase Jacobian, fixed-physical-delay period derivative, parameter derivative, gauge structure, pseudo-arclength algebra as a definition, event/admissibility qualifications, existence-vs-stability-vs-hybrid taxonomy, and the exchange-symmetric two-cell block structure with the corrected negative antisymmetric coefficient `B`.

The freeze also preserves two repairs to the legacy formulation: the frozen smooth baseline response is not nonsmooth merely at threshold contact, and alpha-arrival collisions are representation/event-chart boundaries rather than automatic existence-Jacobian singularities.

No numerical continuation, actual Lighthouse fold/pitchfork claim, B11–B22 output, v0.4 stability result, implementation result, inference result or active-design result is promoted by RB-007.

MASTER authorizes exactly one next scientific action: `CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1`. It is pre-execution only and must define finite cases, derivative conventions, tolerances and PASS/FAIL rules before any v0.3 validation is run.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.3 continuation-validation-contract canonicalization result |
| 10 CORE | READY | execute v0.3 Continuation Validation Contract Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.5
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- Legacy CORE v0.3–v0.26 scientific claims: NON-CANONICAL / NOT FROZEN except material separately promoted through governed gates
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## RB-006 — governed v0.2 validation result

Canonical result-freeze file:

`research/core/v0_2_benchmark_result_freeze_0_1.md`

Result:

`PASS — BC01–BC10 ALL PASS UNDER RB-005`

This remains the first governed validation-result layer and is unchanged.

## RB-007 — v0.3 continuation theory

Canonical theory-freeze file:

`research/core/v0_3_continuation_theory_freeze_0_1.md`

Frozen source:

`research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`

Key frozen contents include:

1. `phi_i=T chi_i`, normalized firing times and unwrapped internal phase coordinates;
2. gauge fixing `chi_1=0`;
3. fixed-domain phase-locked branch operator;
4. independently re-derived phase Jacobian and gauge null identity;
5. fixed-physical-delay period derivative with explicit comb-period derivative under stated local regularity;
6. general scalar-parameter derivative under stated differentiability;
7. pseudo-arclength algebra as a method definition only;
8. smooth-chart, arrival-kink and wrapped-coordinate qualifications;
9. event transversality and first-hitting admissibility;
10. existence / dynamical-stability / hybrid-event / representation-boundary taxonomy;
11. conditional generic fold statement only under local `C^2` assumptions;
12. exchange-symmetric two-cell parity/block structure and corrected negative coefficient `B`.

Not frozen are actual Lighthouse fold/pitchfork locations, unconditional higher regularity, B11–B22 results, Floquet/stability objects or downstream numerical effects.

## Branch-independent results

- Governance process 0.1: STABLE.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 benchmark contract: STABLE pre-execution scientific contract.
- RB-006 governed v0.2 analytical validation: STABLE scientific result freeze.
- RB-007 v0.3 continuation theory: STABLE scientific theory freeze.

## Branch-dependent scientific results

No legacy downstream numerical result is canonical scientific evidence unless separately promoted through a governed gate.

The legacy branch remains read-only recovery evidence. v0.3 numerical continuation and v0.4–v0.26 artifacts retain their recovery classifications only.

## Result classifications

- RB-004 mathematical statements retain their frozen epistemic labels.
- RB-006: governed analytical validation PASS.
- RB-007: narrow v0.3 continuation mathematics frozen with explicit conditional and deferred boundaries.
- No STRONG, WEAK, NULL or FAIL classification is assigned to any downstream legacy effect result.

## v0.3 validation disposition

The legacy `continuation_contract_v0.3.md` remains candidate input only. MASTER does not adopt B11–B22 or their recommended tolerances wholesale.

The current contract-canonicalization gate may pre-specify finite validation cases for coordinate equivalence/gauge, Jacobians, period/parameter derivatives, synthetic pseudo-arclength machinery, two-cell block structure/`B`, elementary transversality/first-hitting, arrival-aware handling, and fixed-point branch sensitivity.

It must defer actual Lighthouse fold/pitchfork search, v0.4 stability interfaces, hard-threshold tests for the smooth baseline, adaptive delays and all downstream science.

## Active blocker

A governed pre-execution validation contract for RB-007 has not yet been frozen. Until that contract returns and MASTER decides on it:

- no v0.3 validation execution or B11–B22 execution;
- no numerical continuation or critical-point search;
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

## Manuscript

WAIT. Existing freezes do not authorize manuscript claims based on downstream legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized until MASTER explicitly opens LIT.

## Cross-branch integration

The mathematical baseline, first governed analytical validation layer, and narrow v0.3 continuation theory are now integrated on `main` without merging `core/theory-v0.1`.

Further integration remains gate-by-gate. The immediate next layer is a pre-execution v0.3 validation contract, not numerical continuation.

## Next global step

Execute `CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`

The gate must define a fully pre-specified finite validation contract only. It may not execute any validation or start a second gate.

After CORE creates `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.3 CONTINUATION VALIDATION CONTRACT CANONICALIZATION GO
