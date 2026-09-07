# MASTER Prompt — CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1

Date: 2026-09-07
Authority: MASTER
Workstream: `10 – CORE – Haupttheorie / mathematischer Kern`

## Purpose

Construct a fully pre-execution, governance-compliant validation contract for the C2 / algorithmic validation layer implied by `CORE v0.3 Continuation Theory Freeze 0.1` / RB-007.

This gate defines what a later execution gate may test and exactly how PASS/FAIL will be judged. It must **not execute** any v0.3 numerical validation, continuation, fold/pitchfork search, B11–B22 benchmark, or downstream science.

## Canonical authorities

Read and obey at minimum:

- `PROJECT_GOVERNANCE.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/core/mathematical_freeze_0_1.md` — RB-004
- `research/core/benchmark_contract_freeze_0_1.md` — RB-005
- `research/core/v0_2_benchmark_result_freeze_0_1.md` — RB-006
- `research/core/v0_3_continuation_theory_freeze_0_1.md` — RB-007
- `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`

Historical candidate input may be inspected only at frozen recovery commit `287eae8a86560b78ed94f30a2786243714c33ac0`:

- `docs/core/continuation_contract_v0.3.md`
- `docs/core/continuation_bifurcations_v0.3.md`

Legacy B11–B22 definitions and recommended tolerances are candidate ideas only and are not canonical until independently audited and explicitly adopted here.

## Authorized scope

Produce a finite, anti-cherry-picking validation contract tied strictly to RB-007. It may define tests for:

1. normalized-vs-dimensional coordinate equivalence and global gauge invariance;
2. analytic v0.3 phase-Jacobian validation at predetermined smooth-chart points;
3. fixed-physical-delay period derivative and selected scalar-parameter derivative checks at predetermined regular points;
4. pseudo-arclength machinery on a synthetic fold only;
5. exchange-symmetric two-cell parity/block structure and corrected negative `B` coefficient;
6. synthetic pitchfork algebra only if clearly separated from any Lighthouse-specific pitchfork claim;
7. first-hitting and transversality consistency traceable to RB-004/RB-007;
8. arrival-aware integration / derivative handling using predetermined cases that distinguish representation/chart changes from genuine singularities;
9. implicit branch sensitivity only at predetermined regular points and fixed parameterizations;
10. explicit negative controls for invalid derivative charts where mathematically justified.

## Required deferrals

The contract must defer and must not define acceptance of:

- any actual Lighthouse fold or pitchfork parameter/location found by search;
- any post-hoc selection of critical branch points;
- any v0.4 Floquet/multiplier/stability object;
- any B16 stability-classifier result that requires v0.4 objects;
- hard-threshold contact tests unless MASTER separately authorizes a nonsmooth response variant;
- adaptive-delay/commensurability tests;
- general symmetry/Fourier Floquet sectors;
- production/JAX performance;
- surrogate-continuation scientific agreement;
- v0.4+ work, inference, observation design, active experiment design, applications, novelty or v0.27.

## Anti-cherry-picking requirements

Before any later execution, this gate must freeze for every proposed test:

- exact model / registered variant;
- graph/coupling geometry;
- parameter values and parameterization convention;
- branch/reference state or synthetic problem;
- histories and event itinerary where relevant;
- derivative convention, including what is held fixed;
- chart/admissibility margins;
- finite test cases;
- horizon/domain;
- grid/resolution if any;
- permitted method class;
- internal solver/quadrature tolerances;
- observables;
- independent reference construction;
- acceptance tolerances;
- PASS/FAIL/INVALID rules;
- negative controls;
- treatment of software-plumbing defects;
- explicit rule that no case may be dropped/replaced after output inspection.

No open-ended scan, optimizer, continuation search, tuning loop, or effect-strength selection may be embedded in the contract.

## Suggested legacy mapping to audit

Audit, retain/repair/defer rather than copy blindly:

- B11 coordinate equivalence/gauge — likely retain/repair;
- B12 branch Jacobian — retain only at fixed smooth-chart cases;
- B13 pseudo-arclength — synthetic fold portion only; Lighthouse-fold portion defer;
- B14 two-cell block structure / `B` integral — high-priority retain/repair;
- B15 pitchfork — synthetic algebraic portion only; Lighthouse-specific portion defer;
- B16 existence/stability classifier — defer until v0.4 canonicalization;
- B17 transversality — elementary/event-chart portion only; saltation/Floquet portions defer;
- B18 arrival-aware handling — retain/repair with RB-007 qualifications;
- B19 threshold contact — defer for frozen smooth baseline;
- B20 implicit branch sensitivity — retain only with predetermined regular point and fixed parameterization;
- B21 adaptive-delay commensurability — defer;
- B22 first-hitting admissibility — retain/repair.

## Deliverable

Create:

`research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`

It must contain at minimum:

1. Git / provenance identity;
2. frozen-authority map RB-004 through RB-007;
3. legacy B11–B22 inclusion/exclusion matrix;
4. contract-wide execution conventions;
5. fully pre-specified finite validation cases with new canonical IDs;
6. exact parameter sets / synthetic problems / branch reference construction;
7. derivative conventions and chart/admissibility requirements;
8. symbolic versus numerical/algorithmic separation;
9. tolerances and rationale fixed before execution;
10. PASS/FAIL/INVALID rules and negative controls;
11. deferred-item boundary;
12. statement that no validation has been executed;
13. gate decision PASS / FAIL / CONDITIONAL;
14. proposed contents of `CORE v0.3 Continuation Validation Contract Freeze 0.1` if PASS;
15. exact proposed later execution gate if and only if MASTER freezes the contract;
16. open questions;
17. STOP.

## Forbidden execution

Do not:

- run the proposed validation suite;
- numerically continue a Lighthouse branch;
- search for folds/pitchforks/critical points;
- inspect legacy effect-bearing v0.3 numerical outputs to choose cases;
- execute B11–B22;
- start v0.4+ work;
- implement production/JAX continuation;
- perform active experiment design;
- modify RB-004, RB-005, RB-006 or RB-007.

## Status update and STOP

After creating the deliverable, update `research/core/STATUS.md` to `RETURN TO MASTER` or `BLOCKED` with no second CORE task.

Then stop.

`STOP — RETURN TO MASTER`
