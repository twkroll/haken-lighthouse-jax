# Lighthouse-JAX — Canonical Project Status

Version: 1.3
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. `CORE Recovery & Canonicalization Gate 0.1`, `CORE Mathematical Scope Canonicalization Gate 0.1`, and `CORE v0.2 Benchmark Contract Canonicalization Gate 0.1` have completed with PASS.

MASTER previously established `CORE Mathematical Freeze 0.1` as RB-004. MASTER has now reviewed the pre-execution BC01–BC10 benchmark contract and establishes `CORE Benchmark Contract Freeze 0.1` as RB-005 in `research/core/benchmark_contract_freeze_0_1.md`.

RB-005 freezes the execution conventions, all BC01–BC10 benchmark definitions, finite parameter/test sets, histories, horizons, grids/resolutions, method classes, quadrature stopping tolerances, observables, references, acceptance tolerances, pass/fail rules, admissibility/transversality rules, negative controls, and deferred-item boundary before any benchmark output is observed.

No benchmark has yet passed or failed under governed execution. BC01–BC10 remain UNEVALUATED. No legacy v0.3–v0.26 scientific result is promoted by the contract freeze.

MASTER authorizes exactly one next scientific action: `CORE v0.2 Benchmark Execution Gate 0.1`, which must execute BC01–BC10 exactly under RB-005 without tuning or contract modification.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting governed BC01–BC10 execution result |
| 10 CORE | READY | execute v0.2 Benchmark Execution Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.3
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- Legacy CORE v0.3–v0.26 scientific claims: NON-CANONICAL / NOT FROZEN
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## CORE Mathematical Freeze 0.1

Canonical freeze file:

`research/core/mathematical_freeze_0_1.md`

RB-004 freezes source map S1–S6, baseline equations C1–C11, event/delay semantics, assumptions A1–A13, variant registry, elementary identities D1–D18, analytical validation targets and explicit exclusions. Any change requires a new MASTER-authorized gate and versioned freeze.

## CORE Benchmark Contract Freeze 0.1

Canonical freeze file:

`research/core/benchmark_contract_freeze_0_1.md`

Frozen source artifact:

`research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`

RB-005 freezes:

1. Section 4 execution conventions;
2. BC01–BC10 in Section 5;
3. E0/N1/N2/L0 tolerance classes;
4. symbolic-versus-numerical separation;
5. admissibility/transversality rules;
6. DFR-01 through DFR-07 deferred boundary.

Freeze semantics are strictly pre-execution: BC01–BC10 are not classified as PASS merely because the contract gate passed.

## Branch-independent results

- Governance process 0.1: STABLE.
- MASTER reporting process v0.2: STABLE administrative artifact.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 benchmark contract: STABLE pre-execution scientific contract.

## Branch-dependent scientific results

No downstream legacy numerical result is canonical scientific evidence yet.

No governed benchmark execution result exists yet. The legacy branch remains read-only recovery evidence; v0.3–v0.26 artifacts retain recovery classifications only.

## Result classifications

Frozen mathematical statements in RB-004 retain their epistemic labels, including LEMMA / PROVED and PROPOSITION / PROVED for D1–D18.

BC01–BC10: UNEVALUATED under RB-005.

No STRONG, WEAK, NULL or FAIL classification is assigned to any legacy numerical result.

## Benchmark execution boundary

The next gate must execute every required BC01–BC10 benchmark, subcase and negative control exactly as frozen. It may not change parameters, histories, grids, method classes, quadrature tolerances, acceptance tolerances, observables, references or pass/fail rules after observing output.

A scientifically valid benchmark failure is a valid result and must be preserved. Clerical/software-plumbing defects in a minimal validation harness may be corrected only with a documented audit trail and without changing RB-005.

## Active blocker

The frozen validation contract has not yet been executed. Until the governed execution returns:

- no v0.3+ legacy replay/rerun;
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

## Manuscript

WAIT. Mathematical and benchmark-contract freezes do not authorize manuscript claims based on legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized until MASTER explicitly opens LIT.

## Cross-branch integration

The mathematical baseline and its first validation contract are now integrated on `main` without merging `core/theory-v0.1`.

Further recovery remains gate-by-gate. No v0.3+ material is integrated by RB-005.

## Next global step

Execute `CORE v0.2 Benchmark Execution Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_2_benchmark_execution_gate_0_1.md`

The gate must execute BC01–BC10 exactly under RB-005 and return PASS, FAIL or CONDITIONAL to MASTER. It may not start a second gate.

After CORE creates `research/core/v0_2_benchmark_execution_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.2 BENCHMARK EXECUTION GO
