# CORE v0.27 Hierarchical Repeated-Trial Scope & Preregistration Gate 0.1

Date: 2026-09-07
Authority: MASTER
Status: AUTHORIZED / NOT YET EXECUTED

## Purpose

Open the first genuinely new CORE layer beyond the frozen legacy recovery corpus.

This gate must define and preregister a hierarchical repeated-trial extension of the Lighthouse inference problem using only canonical frozen premises. It must not treat legacy v0.22–v0.26 optimized numerical effects as established facts and must not execute the new model numerically.

## Canonical premises

Fresh-read and reuse without redundant re-derivation:

- `PROJECT_GOVERNANCE.md`
- `research/master/command_protocol_v0_2.md`
- `research/core/mathematical_freeze_0_1.md` — RB-004
- `research/core/v0_2_benchmark_result_freeze_0_1.md` — RB-006
- `research/core/v0_3_continuation_theory_freeze_0_1.md` — RB-007
- `research/core/v0_3_continuation_validation_result_freeze_0_1.md` — RB-009
- `research/core/v0_4_floquet_theory_freeze_0_1.md` — RB-010
- `research/core/legacy_verification_sweep_freeze_0_1.md` — RB-011
- `research/core/consolidated_c1_theory_freeze_0_1.md` — RB-012

Legacy recovery SHA `287eae8a86560b78ed94f30a2786243714c33ac0` may be consulted only as hypothesis/provenance input. No legacy C3 effect is a premise.

## Scientific target

Define the smallest coherent hierarchical repeated-trial model that extends the frozen v0.26 nuisance mathematics to repeated experiments with trial-to-trial preparation variability and imperfect spike observations.

The gate must decide one explicit first target rather than opening multiple branches. At minimum it must settle:

1. **Shared scientific parameters.** Define the shared parameter block to be estimated across trials and justify any deviation from the legacy `(p,tau3)` example.
2. **Trial-specific latent preparation.** Define the per-trial latent state block and its relation to the frozen q=1/state/gauge conventions.
3. **Hierarchical preparation law.** Specify a finite-dimensional population-level model for trial preparation variability, including parameterization, identifiability constraints and whether the law is deterministic-random-effects, Gaussian, or another explicitly justified first model.
4. **Observation model.** Specify labelled spike-time observations and one explicit first imperfection model. Choose a minimal first scope: timing noise plus missing spikes is preferred unless a stronger alternative is justified. Do not simultaneously add unknown topology, unlabelled spikes and multiple unrelated observation defects.
5. **Calibration treatment.** Respect RB-012: fixed-time `(A,beta,gamma)` calibration changes are structurally absorbable by free trial-state nuisance under its stated assumptions. Decide whether the first v0.27 target uses externally calibrated pulses, no active pulse, or explicitly excludes pulse calibration from the first execution.
6. **Likelihood / objective.** Define the exact statistical objective or estimating equations for the first target, including treatment of latent trial variables and missing data. State whether inference is profiled, marginalized, Laplace-approximated, EM-like, variational, or another method; choose one primary route for the first execution.
7. **Identifiability questions.** State the precise structural/local identifiability claims to be tested, including how nuisance-profile information from RB-012 generalizes to many trials.
8. **Synthetic data generator.** Predefine the model ingredients required for a later deterministic/stochastic validation dataset, while leaving numerical values to a separately frozen execution contract if effect-bearing.
9. **Success/failure observables.** Define finite primary metrics for a future execution: recovery bias/error, uncertainty calibration/coverage if applicable, rank/conditioning/profiled information, missing-spike recovery diagnostics and chart/admissibility failure rates.
10. **Anti-cherry-picking boundary.** List every quantity that must be frozen before any later numerical output is inspected: parameter truth, number of trials, preparation distribution, noise/missingness levels, observation horizon, optimizer/inference method, initialisation policy, chart rules, tolerances, metrics and PASS/FAIL criteria.
11. **Implementation dependencies.** Identify which C2 components from the legacy sweep are truly required for the first v0.27 execution. Do not replay unrelated legacy code merely because it exists.
12. **Novelty boundary.** No novelty claim. Mark all new v0.27 mathematics as PROJECT DERIVATION / ASSUMPTION / OPEN QUESTION until separately frozen and later literature-audited.

## Required comparison with legacy v0.26

Produce a concise dependency table with columns:

`v0.26 element | status after RB-011/RB-012 | reused in v0.27? | reason | new assumption/change`

At minimum include:

- shared parameter block;
- per-trial latent preparation;
- nuisance projector/profiled sensitivity;
- pulse calibration ambiguity;
- numerical uncertainty values;
- preparation-jitter amplitudes;
- noise/multistart results.

The table must make clear that legacy numerical scales/effect sizes remain C3 and are not silently imported.

## Required deliverable

Create:

`research/core/v0_27_hierarchical_repeated_trial_scope_preregistration_gate_0_1.md`

The deliverable must include:

1. provenance and freeze-chain identity;
2. exact v0.27 first-target model;
3. notation and unknown blocks;
4. hierarchical preparation model;
5. observation/noise/missingness model;
6. calibration handling;
7. inference objective and nuisance treatment;
8. structural/local identifiability questions;
9. minimal synthetic-data/validation design skeleton;
10. required C2 implementation dependencies only;
11. anti-cherry-picking freeze list;
12. explicit exclusions/deferred branches;
13. PASS / FAIL / CONDITIONAL decision on whether a governed v0.27 execution contract can be written next;
14. proposed contents of that later execution contract, without executing it;
15. STOP.

## PASS criterion

PASS means the first genuinely new v0.27 scientific target is sufficiently narrow, mathematically coherent, traceable to frozen premises and preregisterable before numerical execution.

PASS does **not** mean the hierarchical model works, is identifiable, improves inference, handles missing spikes successfully, or establishes novelty.

## Forbidden in this gate

- no v0.27 numerical simulation or inference run;
- no parameter scan or tuning;
- no reuse of legacy optimized pulse/P2/subset as confirmatory truth;
- no import of legacy C3 effect sizes as priors or acceptance targets unless explicitly treated only as non-binding historical context;
- no application work;
- no independent novelty positioning;
- no manuscript claim freeze.

## STOP

After the deliverable is committed, set CORE STATUS to RETURN TO MASTER or BLOCKED and stop.

STOP — RETURN TO MASTER
