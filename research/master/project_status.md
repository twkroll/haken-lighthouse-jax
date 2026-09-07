# Lighthouse-JAX — Canonical Project Status

Version: 1.8
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

Governance has been amended with the verification-first command protocol v0.2 in `research/master/command_protocol_v0_2.md` and `PROJECT_GOVERNANCE.md`.

Canonical rule:

`Reconstruct state, not frozen science.`

FROZEN/STABLE scientific artifacts are reusable premises. New/replacement chats fresh-read Git and the freeze/dependency chain, but do not re-derive already frozen science merely to regain conversational context.

Completed canonical scientific layers now include:

- RB-004 CORE Mathematical Freeze 0.1;
- RB-006 governed v0.2 analytical validation PASS;
- RB-007 v0.3 continuation theory;
- RB-008 v0.3 continuation validation contract;
- RB-009 governed v0.3 continuation validation PASS;
- RB-010 v0.4 Floquet Theory Freeze 0.1.

MASTER reviews `research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md` and accepts its PASS. The gate independently re-derived and repaired the narrow spike-time Floquet/symmetry mathematics without executing B23–B40 or searching actual Lighthouse multipliers/stability boundaries.

MASTER therefore establishes `CORE v0.4 Floquet Theory Freeze 0.1` as RB-010 in `research/core/v0_4_floquet_theory_freeze_0_1.md`.

The old serial pattern of one micro-gate per already-existing legacy version is now replaced by one consolidated verification-first action: `CORE Legacy Verification Sweep 0.1`.

The sweep audits v0.4–v0.26 in one CORE session against the freeze chain. It must not return to MASTER between individual legacy versions.

## Command protocol v0.2

### `GO`
Execute the current `Next instruction` after a fresh Git/STATUS check and reuse all FROZEN/STABLE dependencies as premises.

### `RESUME`
Preferred command for a new/replacement chat. Reconstruct Git state and, if READY, execute the current `Next instruction` in the same session without redundant re-derivation of frozen dependencies.

### `VERIFY-LEGACY`
CORE-only command for the currently authorized batch sweep. It runs the complete v0.4–v0.26 verification pass before RETURN TO MASTER.

The verification sweep may perform mathematical consistency checks, provenance/static artifact checks and faithful exact replay where artifact/environment closure permits. It may not silently promote exploratory C3 numerical effects or rescue legacy results through post-hoc redesign.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting full Legacy Verification Sweep result |
| 10 CORE | READY | execute `CORE Legacy Verification Sweep 0.1` only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance command protocol v0.2: STABLE ADMINISTRATIVE
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v1.8
- Communication briefings: NON-CANONICAL / PRE-CORE
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-009 CORE v0.3 Continuation Validation Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-010 CORE v0.4 Floquet Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
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

### RB-008 / RB-009 — v0.3 validation

Finite deterministic V3C01–V3C09 contract and governed result:

`PASS — V3C01–V3C09 ALL PASS UNDER RB-008`.

The documented V3C04 result-table transcription defect was corrected by a full unchanged-contract rerun; the incorrect preliminary table remains invalidated in Git history.

### RB-010 — v0.4 Floquet theory

Freezes the narrow spike-time Floquet/symmetry formulation established in the v0.4 theory gate, including:

- spike-time linear recurrence under regular fixed-chart assumptions;
- exact periodic row-sum cancellation;
- nonlinear characteristic operator `M(mu)=(mu-1)D_nu-H(mu)`;
- raw alpha lag-series convergence domain and derivative-comb representation;
- exact neutral global time-translation mode;
- multiplier/exponent conventions;
- normalized simple nonlinear-eigenvalue sensitivity;
- existence/dynamic/event/chart taxonomy;
- event-index relabelling covariance;
- two-cell, circulant/Fourier and cluster/symmetry reductions under full-operator symmetry conditions.

RB-010 does not validate B23–B40, any actual Lighthouse multiplier/root set, stability boundary or v0.5+ result.

## Legacy Verification Sweep 0.1

Prompt:

`research/master/prompts/core_legacy_verification_sweep_0_1.md`

Frozen recovery input:

`287eae8a86560b78ed94f30a2786243714c33ac0`

The sweep must audit legacy v0.4–v0.26 and classify each material unit as one of:

- ALREADY CANONICAL
- MATHEMATICALLY VERIFIED IN SWEEP
- STATICALLY CONSISTENT
- EXACT REPLAY PASS
- EXACT REPLAY FAIL
- REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP
- PREREGISTERED RERUN REQUIRED
- SOURCE/PROVENANCE REPAIR REQUIRED
- SUPERSEDED / REJECT
- DEFER / OPEN QUESTION

The sweep must also retain recovery classes C1/C2/C3/C4/C5 and identify the minimal genuinely unresolved queue after all reusable frozen work is removed.

For exploratory/effect-selected numerical results, particularly v0.6–v0.15 and v0.21–v0.26, static consistency or exact replay does not by itself convert the result into confirmatory evidence. Fresh preregistration remains required where the recovery provenance is C3.

## Branch-independent results

- Governance / command protocol: STABLE.
- RB-002 recovery provenance: STABLE administrative artifact.
- RB-003 recovery classification: STABLE administrative/audit artifact.
- RB-004 mathematical baseline: STABLE scientific freeze.
- RB-005 v0.2 benchmark contract: STABLE pre-execution contract.
- RB-006 governed v0.2 validation: STABLE scientific result freeze.
- RB-007 v0.3 continuation theory: STABLE scientific theory freeze.
- RB-008 v0.3 validation contract: STABLE pre-execution contract.
- RB-009 governed v0.3 validation: STABLE scientific result freeze.
- RB-010 v0.4 Floquet theory: STABLE scientific theory freeze.

## Branch-dependent scientific results

No downstream legacy numerical effect result is canonical scientific evidence unless separately promoted through a governed gate.

No actual Lighthouse continuation branch, fold/pitchfork location or scaling, Floquet spectrum, stability boundary, invariant-circle/global-object result, implementation-performance claim, inference-performance result or active-design effect has yet been promoted beyond the freezes listed above.

## Active blocker

The project no longer has a serial v0.4→v0.5→… micro-gate blocker. The active blocker is now consolidated:

`CORE Legacy Verification Sweep 0.1` must classify the entire existing v0.4–v0.26 corpus before MASTER opens new science or decides which few remaining validation gates are genuinely necessary.

Until the sweep returns:

- no post-hoc rescue tuning or new effect search;
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
10. RB-010 CORE v0.4 Floquet Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY

## Manuscript

WAIT. Existing freezes do not yet authorize downstream legacy numerical claims as manuscript evidence.

## Literature positioning

WAIT. Source verification internal to CORE is allowed for provenance; independent novelty positioning remains unauthorized until MASTER explicitly opens LIT.

## Cross-branch integration

The canonical baseline, governed v0.2 validation, v0.3 theory/validation and v0.4 Floquet theory are integrated on `main` without merging `core/theory-v0.1`.

Legacy recovery remains verification input only.

## Next global step

In `10 – CORE – Haupttheorie / mathematischer Kern`, issue exactly:

`VERIFY-LEGACY`

For a new/replacement CORE chat, issue instead:

`RESUME`

Both commands must fresh-read Git. With current CORE STATUS, either route executes the same `CORE Legacy Verification Sweep 0.1`.

The sweep returns to MASTER only after the complete v0.4–v0.26 audit is written.

## STOP

STOP — AWAIT FULL CORE LEGACY VERIFICATION SWEEP
