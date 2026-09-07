# Lighthouse-JAX — Canonical Project Status

Version: 1.2
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance Initialization 0.1 remains STABLE. `CORE Recovery & Canonicalization Gate 0.1` and `CORE Mathematical Scope Canonicalization Gate 0.1` have both completed with PASS.

MASTER has reviewed the mathematical scope canonicalization result and authorizes `CORE Mathematical Freeze 0.1` as `RB-004`. The freeze is recorded in `research/core/mathematical_freeze_0_1.md` and is anchored to source artifact blob `d34ba1129dfca892e76342f3c2d66b6b493535dd` created at commit `8d2fcb3f1cb020e4e6b3388ad05987f8c6bf3be2`.

The freeze is intentionally narrow: baseline definitions, source/provenance distinctions, assumptions, variant registry, fixed-delay/event semantics and elementary C1 derivations D1–D18 only. No legacy v0.3–v0.26 numerical, implementation, inference or active-design result is frozen.

MASTER also finds that the frozen legacy recovery snapshot contains `docs/core/derivations_v0.2.md` and `docs/core/benchmark_contract_v0.2.md`, but no standalone v0.2 reference script or v0.2 benchmark JSON. Therefore the next step is not an execution/replay. The single authorized next scientific action is `CORE v0.2 Benchmark Contract Canonicalization Gate 0.1`, which must pre-specify the first validation contract before any benchmark execution.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.2 benchmark-contract canonicalization result |
| 10 CORE | READY | execute v0.2 Benchmark Contract Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | CORE source verification complete for Freeze 0.1; no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance rules: STABLE 0.1
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.2
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- Legacy CORE v0.3–v0.26 scientific claims: NON-CANONICAL / NOT FROZEN
- Application candidates: NOT YET AUTHORIZED
- Claims / novelty: OPEN

## CORE Mathematical Freeze 0.1

Canonical freeze file:

`research/core/mathematical_freeze_0_1.md`

Frozen content includes:

1. source map S1–S6, with S6 registry-only;
2. baseline equations C1–C11;
3. lifted-phase first-hitting event convention and no-reset-below-threshold baseline choice;
4. normalized alpha kernel and exact `(a,q)` state-space equivalence;
5. fixed edge-delay semantics;
6. assumptions A1–A13;
7. variant registry V-R0 through V-P1;
8. independently re-derived elementary identities D1–D18;
9. analytical validation targets;
10. explicit exclusions.

This is the first scientific rollback point in the project. Any future baseline change requires a new MASTER-authorized gate and versioned freeze.

## Branch-independent results

- Governance process 0.1: STABLE.
- MASTER reporting process v0.2: STABLE administrative artifact.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.

## Branch-dependent scientific results

No downstream legacy numerical result is canonical scientific evidence yet.

The legacy branch remains read-only recovery evidence. Its v0.3–v0.26 artifacts retain the C1–C5 recovery classifications but have not been merged or promoted.

## Result classifications

Frozen mathematical statements in RB-004 retain the epistemic labels established in `research/core/mathematical_scope_canonicalization_gate_0_1.md`, including LEMMA / PROVED and PROPOSITION / PROVED for the elementary D1–D18 derivations.

No STRONG, WEAK, NULL or FAIL classification is assigned to any legacy numerical result.

## Benchmark-contract disposition

Legacy recovery inspection confirms:

- `docs/core/derivations_v0.2.md` exists;
- `docs/core/benchmark_contract_v0.2.md` exists;
- no standalone `reference/core_v02...` script exists at recovery HEAD;
- no `benchmarks/core_v02...` JSON exists at recovery HEAD;
- executable reference assets begin only at later versions.

Therefore MASTER authorizes contract canonicalization before execution. The current gate may use the two legacy v0.2 documents only as historical candidate input and must define all benchmark inputs, observables, tolerances and pass/fail rules before any benchmark is run.

## Active blocker

A governed validation contract has not yet been frozen. Until this is completed:

- no benchmark execution;
- no legacy v0.3+ replay/rerun;
- no implementation continuation;
- no active hybrid experiment design;
- no v0.27;
- no application execution;
- no novelty or manuscript claim freeze.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE
2. RB-002 CORE Legacy Recovery Input Snapshot 0.1 at `287eae8a86560b78ed94f30a2786243714c33ac0` — STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
3. RB-003 CORE Recovery Classification 0.1 — STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
4. RB-004 CORE Mathematical Freeze 0.1 — FROZEN / STABLE SCIENTIFIC BASELINE

## Manuscript

WAIT. RB-004 establishes a mathematical baseline but does not authorize manuscript claims based on legacy numerical results. Existing communication briefings remain NON-CANONICAL / PRE-CORE.

## Literature positioning

WAIT. Primary-source verification needed for the mathematical freeze has been completed inside CORE. Independent novelty positioning remains unauthorized until MASTER opens LIT.

## Cross-branch integration

The foundational mathematical layer has now been integrated scientifically through RB-004 without merging `core/theory-v0.1`.

Further integration must proceed gate-by-gate. The immediate next layer is the pre-execution benchmark contract, not a wholesale replay or merge.

## Next global step

Execute `CORE v0.2 Benchmark Contract Canonicalization Gate 0.1` in `10 – CORE – Haupttheorie / mathematischer Kern` by issuing exactly:

`GO`

Prompt:

`research/master/prompts/core_v0_2_benchmark_contract_canonicalization_gate_0_1.md`

This gate must not execute benchmarks. It only produces a fully pre-specified benchmark contract suitable for a later MASTER freeze.

After CORE creates `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`, updates `research/core/STATUS.md`, and stops, return to MASTER and issue `Status?`.

## STOP

STOP — AWAIT CORE V0.2 BENCHMARK CONTRACT CANONICALIZATION GO
