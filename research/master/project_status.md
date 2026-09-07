# Lighthouse-JAX — Canonical Project Status

Version: 2.2
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

The verification-first command rule remains:

`Reconstruct state, not frozen science.`

The recovered legacy corpus v0.4–v0.26 remains classified in RB-011 and its strongest independently verified C1 mathematics remains frozen in RB-012. No legacy C3 numerical effect has been promoted.

The first genuinely new v0.27 branch is now complete through governed execution.

Frozen scope: RB-013.
Frozen execution contract: RB-014.
Frozen execution result: RB-015.

Overall v0.27 result:

`SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS`.

MASTER accepts the result exactly as returned and establishes `CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1` / RB-015.

The SCIENTIFIC FAIL is final for the RB-014 preregistered branch and may not be rescued or relabelled by later method development.

## Frozen v0.27 execution findings

### Implementation validation

C2-27-01 through C2-27-08 all PASS with required negative controls. The failure is therefore not classified as IMPLEMENTATION FAIL/BLOCKED.

### Data/admissibility

All 32 immutable datasets were generated only after C2 PASS.

- `INSUFFICIENT_MASK = 0/32`;
- truth physical/chart invalid = `0/32`;
- minimum mask-rich trials in any dataset = `15/16`;
- no seed or dataset was replaced.

### Conservative shared information

The nuisance-profiled two-parameter audit is positive:

- rank-two/regular fraction = `32/32 = 1.000`;
- condition numbers range from `348731` to `712596`, below the frozen `1e8` threshold.

This positive result must be retained with the inference failure and does not imply global identifiability.

### Frozen Laplace inference failure

For 32 datasets x 3 frozen outer starts:

- starts attempted = `96`;
- finite complete initial Laplace objectives = `0/96`;
- every start contains at least one trial-mode `INNER_MODE_FAIL` from the frozen 20-trial strong-Wolfe line-search limit;
- `OUTER_OPT_FAIL = 32/32`;
- usable fits = `0/32`;
- valid five-parameter uncertainty intervals = `0/32`.

The hard failure criteria therefore select `SCIENTIFIC FAIL`, not `SCIENTIFIC CONDITIONAL`.

No extra starts, warm starts, relaxed line search, trust region, ridge, alternative optimizer, EM/VI/MCMC route, seed replacement or data replacement was used.

## Interpretation boundary

RB-015 does not prove that the hierarchical scientific model is globally non-identifiable or that another preregistered inference algorithm would fail.

It proves only that the exact RB-014 Laplace-marginal inference implementation/optimization route fails its preregistered scientific branch criteria on the immutable dataset set.

## Data-use boundary after failure

The 32 RB-015 datasets and optimization traces are now observed and may be used only as development/diagnostic evidence in a separately authorized method-development gate.

If a redesigned inference method is selected using these data, confirmatory evaluation must use a new MASTER-frozen execution contract and a disjoint, previously ungenerated seed namespace. The RB-015 datasets cannot be reused as a fresh confirmatory test set.

## Command protocol

- `GO`: execute only the current READY Next instruction and reuse FROZEN/STABLE premises.
- `RESUME`: preferred for a new/replacement chat; reconstruct Git state and execute the current READY instruction without redundant re-derivation.
- `VERIFY-LEGACY`: no active sweep; the legacy sweep is complete and frozen as RB-011.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.27b failure-mechanism/follow-up preregistration result |
| 10 CORE | READY | execute v0.27b Inference Failure Mechanism & Follow-up Preregistration Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance / command protocol v0.2: STABLE ADMINISTRATIVE
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v2.2
- RB-002 CORE Legacy Recovery Input Snapshot 0.1: STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003 CORE Recovery Classification 0.1: STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004 CORE Mathematical Freeze 0.1: FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005 CORE Benchmark Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-009 CORE v0.3 Continuation Validation Result Freeze 0.1: FROZEN / STABLE RESULT
- RB-010 CORE v0.4 Floquet Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-011 CORE Legacy Verification Sweep Freeze 0.1: FROZEN / STABLE VERIFICATION AUDIT
- RB-012 CORE Consolidated C1 Theory Freeze 0.1: FROZEN / STABLE SCIENTIFIC THEORY
- RB-013 CORE v0.27 Hierarchical Repeated-Trial Scope Freeze 0.1: FROZEN / STABLE NEW-SCIENCE SCOPE
- RB-014 CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1: FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-015 CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1: FROZEN / STABLE SCIENTIFIC RESULT — FAIL

## Next scientific question

The next branch is not a rescue execution. It is a controlled failure-mechanism and method-development/preregistration gate.

It may diagnose why the frozen inner BFGS/strong-Wolfe route universally failed, using RB-015 data only as explicitly POST-HOC / DEVELOPMENT evidence. It must select at most one follow-up inference route and, if one is defensible, preregister a later confirmatory strategy with a disjoint new seed namespace.

No redesigned confirmatory performance may be claimed in that diagnostic gate.

## Active blocker

The sole active blocker is completion of `CORE v0.27b Inference Failure Mechanism & Follow-up Preregistration Gate 0.1`.

Until return:

- no redesigned confirmatory execution;
- no relabelling of RB-015;
- no v0.28 effect-bearing work;
- no active pulse/probe extension;
- no legacy C3 promotion;
- no application execution;
- no independent novelty positioning;
- no manuscript claim freeze.

## Rollback points

1. RB-001 Governance Initialization 0.1 — STABLE
2. RB-002 CORE Legacy Recovery Input Snapshot 0.1 — STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
3. RB-003 CORE Recovery Classification 0.1 — STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
4. RB-004 CORE Mathematical Freeze 0.1 — FROZEN / STABLE SCIENTIFIC BASELINE
5. RB-005 CORE Benchmark Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
6. RB-006 CORE v0.2 Benchmark Result Freeze 0.1 — FROZEN / STABLE RESULT
7. RB-007 CORE v0.3 Continuation Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY
8. RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
9. RB-009 CORE v0.3 Continuation Validation Result Freeze 0.1 — FROZEN / STABLE RESULT
10. RB-010 CORE v0.4 Floquet Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY
11. RB-011 CORE Legacy Verification Sweep Freeze 0.1 — FROZEN / STABLE VERIFICATION AUDIT
12. RB-012 CORE Consolidated C1 Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY
13. RB-013 CORE v0.27 Hierarchical Repeated-Trial Scope Freeze 0.1 — FROZEN / STABLE NEW-SCIENCE SCOPE
14. RB-014 CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
15. RB-015 CORE v0.27 Hierarchical Repeated-Trial Result Freeze 0.1 — FROZEN / STABLE SCIENTIFIC RESULT — FAIL

## Manuscript

WAIT. RB-015 is a valid negative result, but no manuscript claim freeze is authorized.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized.

## Next global step

In `10 – CORE – Haupttheorie / mathematischer Kern`, execute:

`GO`

For a new/replacement CORE chat, execute:

`RESUME`

Current prompt:

`research/master/prompts/core_v0_27b_inference_failure_mechanism_followup_preregistration_gate_0_1.md`

The gate returns once after diagnosis/preregistration and must not self-authorize confirmatory re-execution.

## STOP

STOP — AWAIT CORE V0.27B INFERENCE FAILURE MECHANISM & FOLLOW-UP PREREGISTRATION
