# MASTER Prompt — CORE v0.27 Hierarchical Repeated-Trial Execution Contract Canonicalization Gate 0.1

Date: 2026-09-07
Authority: MASTER
Status: AUTHORIZED / PRE-EXECUTION ONLY

## Purpose

Construct the complete pre-execution numerical and implementation-validation contract for the first new-science target frozen in RB-013.

This gate MUST NOT execute the hierarchical experiment, generate scientific v0.27 output, tune parameters, inspect effect sizes, or optimize design choices.

Canonical rule: `Reconstruct state, not frozen science.` Reuse all FROZEN/STABLE premises.

## Authoritative inputs

Read at minimum:

- `PROJECT_GOVERNANCE.md`
- `research/master/command_protocol_v0_2.md`
- `research/core/STATUS.md`
- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/core/v0_27_hierarchical_repeated_trial_scope_preregistration_gate_0_1.md`
- `research/core/v0_27_hierarchical_repeated_trial_scope_freeze_0_1.md` — RB-013
- `research/core/consolidated_c1_theory_freeze_0_1.md` — RB-012
- `research/core/legacy_verification_sweep_freeze_0_1.md` — RB-011
- any frozen baseline/theory/result files required by those dependencies.

Legacy recovery SHA `287eae8a86560b78ed94f30a2786243714c33ac0` may be consulted only for provenance and reusable C2 code candidates. Legacy C3 outputs may not determine numerical design choices or acceptance thresholds.

## Required contract contents

### 1. Immutable identity and scope

Record exact Git/freeze identities and state explicitly that RB-013 is the scientific scope authority.

### 2. Complete physical numerical specification

Freeze before any output:

- N=3 topology;
- complete `W^(0)`, `B`, `Tau^(0)`, `C` matrices;
- alpha and response-function constants;
- every other fixed baseline constant;
- nominal initial states `bar(phi)_0`, `bar(psi)_0`, `bar(q)_0`;
- gauge convention;
- truth `(p*,tau_3*)`;
- compact parameter domain `Theta`.

Choices must have an a priori structural rationale and may not be obtained by searching for favorable identifiability or recovery.

### 3. Complete hierarchical numerical specification

Freeze:

- truth `(lambda_phi*,lambda_psi*,lambda_q*)` or equivalent SDs;
- compact hyperparameter domain `Lambda`;
- exact random-effects covariance parameterization already fixed by RB-013;
- trial count R;
- any deterministic nominal preparation quantities.

No unknown mean, anisotropy, cross-covariance or alternative distribution may be added.

### 4. Observation and stochastic design

Freeze:

- horizon H and therefore labelled-slot count K=3H;
- timing-noise scale `sigma_t`;
- missingness probability `pi_miss`;
- minimal-data / insufficient-mask rule;
- number of stochastic dataset replicates;
- immutable RNG seeds or a deterministic seed-generation table fixed in the contract;
- whether one additional noiseless/reference dataset is included and exactly how it is used.

Masks must never be silently regenerated because they are unfavorable.

### 5. Primary inference algorithm

Freeze the Laplace-marginal route from RB-013 completely:

- trial-mode optimization algorithm;
- trial-mode initialization policy;
- derivative method;
- Hessian construction;
- positive-definiteness rule;
- log-determinant method;
- outer five-parameter optimizer;
- outer initialization policy;
- bounds handling;
- stopping tolerances;
- iteration/evaluation budgets;
- deterministic tie-breaking;
- failure handling.

No post-output substitution by EM, VI, MCMC, alternative priors/objectives or additional starts is allowed unless those starts are already finite and fixed here.

### 6. Event-chart and physical validity rules

Freeze:

- first-hit/transversality checks;
- event-order/chart validity sentinel;
- physical rerecording rule when crossing chart boundaries;
- derivative invalidation/recomputation rules;
- minimum chart/admissibility margins if used;
- treatment of simultaneous/colliding events;
- exact criteria for trial/dataset invalidity versus scientific failure.

### 7. Conservative and hierarchical identifiability diagnostics

Freeze numerical definitions and thresholds for:

- `I_free` rank two audit;
- five-dimensional hierarchical information/Hessian rank audit;
- shared-parameter Schur/profile block;
- singular-value/eigenvalue rank tolerance;
- condition-number threshold or equivalent regularity rule.

Thresholds must be justified before numerical effect output.

### 8. Finite scientific success/failure metrics

Use only the metric families preregistered by RB-013 and attach explicit finite numerical decision thresholds:

- signed bias and absolute/normalized error for p and tau_3;
- error for the three preparation scales/log-scales;
- conservative shared information metrics;
- hierarchical information and shared-profile metrics;
- uncertainty-interval construction and empirical coverage target;
- missing-data / insufficient-data / chart / Laplace failure fractions;
- optimizer convergence/failure fractions if retained as a primary metric.

Define one overall PASS/FAIL/CONDITIONAL decision rule before execution. Scientifically valid weak/null/fail outcomes must be preserved.

### 9. C2 implementation validation sub-contract

Before effect-bearing v0.27 results may count, freeze a finite deterministic validation suite for exactly the required implementation path:

1. fixed-delay alpha event scheduler;
2. labelled spike extraction and delayed arrival handling;
3. fixed-chart derivatives with respect to `(p,tau_3,z)`;
4. chart sentinel / physical rerecording;
5. hierarchical Gaussian penalty;
6. trial-mode Hessian and log determinant;
7. mask row selection;
8. outer Laplace objective assembly.

For each check specify:

- fixed input;
- independent reference/identity;
- observable;
- numerical method class;
- tolerance;
- PASS/FAIL rule;
- required negative control where appropriate.

If legacy v0.18–v0.20 code is reused, freeze exact blob/SHA provenance and the permitted replay path. Static consistency alone is not production validation.

No scientific stochastic experiment may be run in this gate.

### 10. Anti-cherry-picking declaration

Produce a single explicit table of every quantity frozen before output, including physical constants, truth, parameter boxes, preparation scales, R, H, noise, missingness, seeds, solvers, tolerances, budgets, diagnostics and success rules.

State that none may change after output inspection except under a new MASTER-authorized branch.

### 11. Deferred branches

Retain as deferred:

- active pulses/direct subthreshold sensing;
- unknown pulse calibration;
- unknown population mean;
- covariance anisotropy/cross-correlation;
- non-Gaussian preparation laws;
- unknown topology;
- unlabelled spikes;
- alternative missingness mechanisms;
- large-network extension;
- alternative inference algorithms;
- legacy optimized C3 designs/effect sizes;
- applications, novelty and manuscript claims.

### 12. Gate decision and proposed freeze

Return PASS/FAIL/CONDITIONAL on whether the full execution contract is genuinely fixed before output.

If PASS, propose exact contents of `CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1` but do not self-authorize execution.

## Forbidden actions

- no v0.27 dataset generation;
- no simulation producing scientific outputs;
- no inference/optimization on scientific synthetic data;
- no parameter scan;
- no search for favorable truth, noise, R, H or missingness;
- no tolerance adjustment after seeing errors;
- no import of legacy 250x/87x/788x/557x gains as targets;
- no active pulse or sensor optimization;
- no application, novelty or manuscript work.

## Deliverable

Create:

`research/core/v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md`

Then update CORE STATUS to RETURN TO MASTER/BLOCKED.

## STOP

STOP immediately after the deliverable and CORE STATUS update.

STOP — RETURN TO MASTER; NO V0.27 SCIENTIFIC EXECUTION IN THIS GATE
