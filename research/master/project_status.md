# Lighthouse-JAX — Canonical Project Status

Version: 2.9
Date: 2026-10-16

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference, AI/temporal learning and later neuromorphic implementation?

## Governance state

Canonical rule:

`Reconstruct state, not frozen science.`

The current frozen chain extends through RB-021.

Preserved boundaries:

- RB-015 remains immutable `SCIENTIFIC FAIL`;
- RB-019 is the first stable Numerical Engineering baseline;
- RB-020 freezes the complete v0.27c Whitened Trust-Region Laplace pre-execution contract, but TR-27C-01…07 remain UNEVALUATED and every `2711xxx` stream remains UNGENERATED / UNEVALUATED;
- RB-021 extends the numerical engineering baseline with deterministic robustness, local scaling/work observations and stronger high-level tape/JAX guards;
- APP-3 remains PARKED / PROTECTED / WAIT.

## CORE theory lane

`CORE Event-Chart Regularity & Certified First-Hit Theory Gate 0.1` returned a candidate PASS and created:

`research/core/event_chart_first_hit_theory_gate_0_1.md`.

The candidate establishes substantial new mathematical material, including:

- exact alpha-state extrema on arrival-free intervals;
- sufficient no-hit and unique transversal first-hit conditions;
- finite-certification logic under strict phase/transversality margins and convergent enclosures;
- global smoothness of the frozen response with explicit derivative bounds;
- alpha-tail and accumulated phase-error bounds;
- finite-event ordinary event-chart regularity;
- local event-time differentiability;
- existence of a positive local chart neighborhood;
- an explicit theorem-vs-engineering certification boundary;
- theory-derived future fixtures TH-FH-01 through TH-FH-08.

MASTER does **not** yet establish the proposed theory freeze.

### Freeze blocker

The returned candidate contains one canonical semantic conflict:

it states that structural zero-weight edges are not physical arrival events in the ordinary chart and proposes TH-FH-06 accordingly.

That conflicts with the topology-fixed structural-coordinate convention already frozen/accepted in the numerical lineage:

- structural edge existence is independent of weight value;
- a structurally present edge remains present at exactly zero weight;
- its packet/arrival event remains labelled;
- the state jump is zero at w=0;
- perturbing the weight through zero must not change topology;
- the weight derivative at zero may be nonzero.

MASTER therefore opens only:

`CORE Event-Chart / Structural-Zero Semantic Repair Gate 0.1`.

Status: READY.

The repair must preserve the original candidate as audit history and correct only the affected structural-zero/event-chart statements plus dependent consistency consequences. No numerical validation is allowed in this repair gate.

## NUM-ENG lane

`NUM-ENG Robustness, Scaling & Differentiable Kernel Gate 0.2` returned:

`PASS — ENGINEERING ONLY`.

MASTER establishes:

`NUM-ENG Numerical Engineering Freeze 0.2` / RB-021.

Status:

`FROZEN / STABLE ENGINEERING BASELINE EXTENSION`.

### Frozen Gate-0.2 findings

Prospectively fixed robustness matrix:

- 17/17 dense-vs-sparse physical comparisons PASS;
- physical invalid/fail-closed controls behave as preregistered;
- 28/28 predeclared acceleration comparisons agree on the finite comparison set, but all accelerators remain DEVELOPMENT COMPARATORS;
- regular-chart JAX replay and physically rerecorded finite-difference checks pass for weight, delay and initial phase;
- JVP/VJP and JVP/Jacobian consistency pass at floating-point precision.

### Stale base-tape defect

Gate 0.2 discovered an additional high-level JAX batch-guard defect:

a stale certified base event tape with shifted event times could preserve the event token and be silently accepted by the batch route.

The defect was recorded before repair-output inspection in a prospective repair addendum. The resulting overlay strengthens high-level physical tape validation without changing the RB-019 physical authority.

Repair QA:

- dedicated new guard tests 8/8 PASS;
- original RB-019 baseline 194/194 PASS;
- Gate-0.2 stress suite 48/48 PASS twice;
- patched targeted suite 56/56 PASS;
- patched aggregate 250/250 PASS with clean exit.

### Local scaling observations

A deterministic sparse family with approximately E=2N was profiled for N={5,12,24,48}.

The two alpha-state float64 arrays use storage proportional to E in the sparse representation versus N^2 in the corresponding dense state representation.

Event/work counts and CPU wall times are retained only as LOCAL ENGINEERING METRICS.

No universal complexity exponent, speedup law, hardware-portability claim or scientific performance result is frozen.

NUM-ENG now has no active gate.

## CORE v0.27c lane

RB-020 remains unchanged.

The actual v0.27c execution is parked.

- TR-27C-01…07: UNEVALUATED.
- `2711xxx`: UNGENERATED / UNEVALUATED.
- no confirmatory v0.27c performance exists.

## APP-3

APP-3 remains:

`PROTECTED / WAIT`.

The AI scope prompt is retained but PARKED / NOT EXECUTABLE under the current Numerics + Theory priority.

No APP-3 execution, training, benchmark or held-out inspection has occurred.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | CORE semantic-repair oversight |
| 10 CORE | READY | structural-zero/event-chart semantic repair only |
| 20 NUM-ENG | FROZEN / WAIT | RB-021 engineering baseline extension |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | unchanged |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | later electronic/neuromorphic branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | AI prompt parked |
| 80 LIT | WAIT | no independent novelty positioning |
| 90 MANUSCRIPT | WAIT | no manuscript claim freeze |

## Current rollback points

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
16. RB-016 CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1 — FROZEN / STABLE DIAGNOSTIC + FOLLOW-UP SCOPE
17. RB-017 Numerical Engineering v0.10 Intake Snapshot 0.1 — STABLE ADMINISTRATIVE / DEVELOPMENT EVIDENCE INPUT
18. RB-018 NUM-ENG Numerical Engineering Audit Freeze 0.1 — FROZEN / STABLE ENGINEERING AUDIT — CONDITIONAL / BLOCKED
19. RB-019 NUM-ENG Numerical Engineering Freeze 0.1 — FROZEN / STABLE ENGINEERING BASELINE
20. RB-020 CORE v0.27c Whitened Trust-Region Laplace Execution Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
21. RB-021 NUM-ENG Numerical Engineering Freeze 0.2 — FROZEN / STABLE ENGINEERING BASELINE EXTENSION

## Exact next step

### CORE

In the existing CORE chat:

`GO`

In a new/replacement CORE chat:

`RESUME`

Execute only:

`research/master/prompts/core_event_chart_first_hit_theory_semantic_repair_gate_0_1.md`.

### NUM-ENG

No NUM-ENG action is currently authorized. RB-021 is frozen.

### APP-3

No APP-3 action is currently authorized.

After CORE returns, go to MASTER and issue:

`Status?`

## Expected next decision after repair

If the structural-zero semantic repair passes without exposing another material contradiction, MASTER can establish:

`CORE Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1`

as the next theory rollback point.

Only after that will MASTER decide whether to open a theory-derived numerical certification/validation gate, a further theory extension, or another Numerics + Theory step.

## Global STOP boundaries

Until explicit later authorization:

- no TR-27C execution;
- no `2711xxx` RNG creation;
- no v0.27c confirmatory execution;
- no APP-3 scope/training/benchmark execution;
- no RB-015 relabelling;
- no v0.28 effect-bearing science;
- no APP-1/APP-2 execution;
- no novelty positioning;
- no manuscript claim freeze.
