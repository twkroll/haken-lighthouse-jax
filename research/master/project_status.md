# Lighthouse-JAX — Canonical Project Status

Version: 1.4
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. Recovery, mathematical-scope canonicalization, v0.2 benchmark-contract canonicalization and governed v0.2 benchmark execution have all completed.

MASTER reviews `research/core/v0_2_benchmark_execution_gate_0_1.md` and accepts its overall PASS. Every required BC01–BC10 benchmark, fixed subcase and required negative control passed under the frozen pre-execution contract RB-005. The documented root-harness correction is accepted as a software-plumbing correction because it changed no frozen scientific specification and the aborted output was not used as evidence.

MASTER therefore establishes `CORE v0.2 Benchmark Result Freeze 0.1` as RB-006 in `research/core/v0_2_benchmark_result_freeze_0_1.md`.

RB-006 validates only the first governed analytical benchmark layer against RB-004 under RB-005. It does not promote any legacy v0.3–v0.26 numerical, implementation, inference or active-design result.

Recovery classifies v0.3–v0.5 theory contracts C1/C2 by claim and requires dedicated verification before promotion. The legacy v0.3 continuation material contains mathematically separable claims about normalized phase-locked coordinates, branch Jacobians, gauge structure and the distinction among existence, stability and hybrid singularities, alongside later numerical continuation/bifurcation contracts.

MASTER therefore authorizes exactly one next scientific action: `CORE v0.3 Continuation Theory Canonicalization Gate 0.1`. It is mathematical claim-audit only. It must not run numerical continuation, B11+ benchmarks, bifurcation searches or v0.4+ work.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.3 continuation-theory canonicalization result |
| 10 CORE | READY | execute v0.3 Continuation Theory Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.4
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- Legacy CORE v0.3–v0.26 scientific claims: NON-CANONICAL / NOT FROZEN except material separately promoted through governed gates
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## RB-006 — governed v0.2 validation result

Canonical result-freeze file:

`research/core/v0_2_benchmark_result_freeze_0_1.md`

Frozen execution artifact:

`research/core/v0_2_benchmark_execution_gate_0_1.md`

Result:

`PASS — BC01–BC10 ALL PASS UNDER RB-005`

The suite includes all required fixed cases and negative controls. No scientifically valid benchmark failure occurred and no frozen acceptance criterion was loosened or replaced.

## Branch-independent results

- Governance process 0.1: STABLE.
- MASTER reporting process v0.2: STABLE administrative artifact.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 benchmark contract: STABLE pre-execution scientific contract.
- RB-006 governed v0.2 analytical validation: STABLE scientific result freeze.

## Branch-dependent scientific results

No legacy v0.3–v0.26 downstream numerical result is canonical scientific evidence yet.

The legacy branch remains read-only recovery evidence. Its v0.3–v0.26 artifacts retain C1–C5 recovery classifications unless separately audited and promoted through a governed gate.

## Result classifications

- RB-004 mathematical statements retain their epistemic labels, including PROVED elementary identities D1–D18.
- RB-006: governed analytical validation PASS.
- No STRONG, WEAK, NULL or FAIL classification is assigned to any downstream legacy numerical effect result.

## v0.3 disposition

Recovery classifies v0.3–v0.5 theory contracts as C1/C2 by claim, not automatically canonical. The first v0.3 gate is therefore restricted to mathematical canonicalization of:

- normalized phase-locked coordinates and their relation to dimensional offsets;
- global phase/time-translation gauge;
- branch equations in fixed normalized coordinates;
- exact branch Jacobian and period derivative under smooth-chart assumptions;
- chart-boundary conditions;
- formal distinction among existence singularities, dynamical stability changes and hybrid/event singularities.

Legacy v0.3 numerical continuation, fold/pitchfork locations, B11+ benchmark execution and other effect-bearing numerical claims remain excluded.

## Active blocker

The recoverable v0.3 continuation theory has not yet been independently canonicalized. Until that gate returns:

- no v0.3 numerical continuation or B11+ execution;
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

## Manuscript

WAIT. RB-006 adds a governed validation result but does not authorize manuscript claims based on downstream legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized until MASTER explicitly opens LIT.

## Cross-branch integration

The baseline and first governed analytical validation layer are now integrated on `main` without merging `core/theory-v0.1`.

Further integration proceeds claim-by-claim and gate-by-gate. v0.3 theory is the next layer; v0.3 numerical continuation is not yet authorized.

## Next global step

Execute `CORE v0.3 Continuation Theory Canonicalization Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_3_continuation_theory_canonicalization_gate_0_1.md`

The gate must audit and re-derive the mathematical v0.3 continuation claims only and return PASS, FAIL or CONDITIONAL to MASTER. It may not execute numerical continuation or start a second gate.

After CORE creates `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.3 CONTINUATION THEORY CANONICALIZATION GO
