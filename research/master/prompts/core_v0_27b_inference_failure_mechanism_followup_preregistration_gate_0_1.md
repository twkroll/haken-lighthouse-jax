# CORE v0.27b Inference Failure Mechanism & Follow-up Preregistration Gate 0.1

## Purpose

Diagnose the frozen RB-015 v0.27 inference failure and define one scientifically defensible follow-up inference branch without erasing, reclassifying, or rescuing the original SCIENTIFIC FAIL.

This is a method-development / preregistration gate. It is not a confirmatory scientific execution.

## Mandatory inputs

Read and use as authority:

- `PROJECT_GOVERNANCE.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- RB-013 scope freeze
- RB-014 execution-contract freeze
- RB-015 result freeze
- `research/core/v0_27_hierarchical_repeated_trial_execution_gate_0_1.md`

Reuse all FROZEN/STABLE upstream mathematics. Do not re-derive frozen science merely to reconstruct context.

## Frozen facts that may not be changed

1. The first v0.27 branch result is `SCIENTIFIC FAIL`.
2. C2-27-01 through C2-27-08 passed.
3. The conservative nuisance-profiled shared information audit passed 32/32.
4. All 32 RB-015 datasets are observed and may not be treated as a fresh confirmatory set.
5. The frozen Laplace route had 0/96 finite complete initial outer-start objectives because at least one inner BFGS mode solve hit `STRONG_WOLFE_20_FAIL` at every frozen start.
6. No legacy C3 pulse/sensor/subset/gain may be promoted.

## Allowed diagnostic work

You may use the existing RB-015 datasets and retained execution traces only for diagnosis/method development. You may perform deterministic, explicitly labelled post-hoc diagnostic probes needed to distinguish plausible failure mechanisms, including:

- inspect objective/gradient/line-search behavior near failed trial-mode iterates;
- distinguish event-chart invalidity from ordinary line-search failure;
- inspect local smoothness/curvature of `Phi_r` inside recorded valid charts;
- test whether failure is caused by strong-Wolfe compatibility, scaling, parameterization, non-finite trial aggregation, or another precisely documented numerical mechanism;
- compare a small finite set of candidate inner-mode solver classes only as DEVELOPMENT diagnostics, not confirmatory performance claims.

Every diagnostic using RB-015 data must be labelled POST-HOC / DEVELOPMENT EVIDENCE.

## Forbidden

- do not change or rerun the RB-014 branch as if it remained confirmatory;
- do not relabel the original SCIENTIFIC FAIL;
- do not report recovery/coverage performance from a redesigned method on the same 32 datasets as confirmatory evidence;
- do not select new truth, graph, R, H, noise, missingness, or active sensing based on favorable effect inspection;
- do not import legacy C3 optimized pulses/sensors/subsets;
- no application, novelty, or manuscript work;
- no v0.28 scientific execution.

## Required output

Create:

`research/core/v0_27b_inference_failure_mechanism_followup_preregistration_gate_0_1.md`

The document must contain:

1. Git/provenance identity.
2. Exact restatement of the frozen RB-015 failure.
3. Failure-mechanism hypotheses defined before each diagnostic family.
4. Finite diagnostic protocol and results, clearly marked POST-HOC / DEVELOPMENT.
5. A classification of the dominant failure mechanism with confidence/limitations.
6. Exactly one proposed follow-up inference route, or an explicit decision that no defensible follow-up is ready.
7. If a follow-up is proposed, freeze in scope:
   - the solver/parameterization class to be used;
   - which scientific model/design quantities remain inherited unchanged from RB-014 and which, if any, require a separately justified new branch;
   - a mandatory deterministic implementation-validation contract for the redesigned solver;
   - a new disjoint confirmatory seed namespace not generated or inspected in this gate;
   - a rule that the old 32 RB-015 datasets are development-only and excluded from the confirmatory performance decision;
   - finite success/failure observables to be fixed later before confirmatory execution.
8. Explicit statement that no confirmatory redesigned-method performance was established in this gate.
9. Proposed MASTER decision and STOP.

## Decision classes

- `PASS — FAILURE MECHANISM SUFFICIENTLY DIAGNOSED; ONE FOLLOW-UP ROUTE PREREGISTERED IN SCOPE`
- `CONDITIONAL — DIAGNOSIS NARROWED BUT NO SINGLE DEFENSIBLE FOLLOW-UP ROUTE YET`
- `FAIL — DIAGNOSTIC EVIDENCE DOES NOT SUPPORT A CONTROLLED FOLLOW-UP`

Any outcome is valid.

## STOP boundary

After writing the result and updating CORE STATUS to RETURN TO MASTER/BLOCKED, stop.

Do not self-authorize a redesigned confirmatory execution.
