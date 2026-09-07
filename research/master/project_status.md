# Lighthouse-JAX — Canonical Project Status

Version: 2.0
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

The verification-first transition remains complete under command protocol v0.2:

`Reconstruct state, not frozen science.`

The recovered legacy corpus v0.4–v0.26 is frozen as a governed classification in RB-011, and its strongest explicitly proved C1 material is frozen in RB-012. No exploratory C3 numerical effect was promoted by that process.

The first genuinely new CORE scope beyond the recovered corpus has now passed:

`CORE v0.27 Hierarchical Repeated-Trial Scope & Preregistration Gate 0.1`

Result:

`PASS — NARROW HIERARCHICAL REPEATED-TRIAL TARGET PREREGISTERED IN SCOPE; NO V0.27 NUMERICAL EXECUTION`.

MASTER accepts this result and establishes `CORE v0.27 Hierarchical Repeated-Trial Scope Freeze 0.1` / RB-013.

RB-013 freezes the scientific target and preregistration structure only. It does not freeze any numerical truth, effect size, recovery performance or v0.27 result.

The single next scientific action is `CORE v0.27 Hierarchical Repeated-Trial Execution Contract Canonicalization Gate 0.1`, whose purpose is to freeze every numerical design constant, stochastic seed, solver rule, C2 implementation validation, tolerance and PASS/FAIL threshold before any effect-bearing v0.27 output is generated.

## Command protocol

- `GO`: execute only the current READY Next instruction and reuse FROZEN/STABLE premises.
- `RESUME`: preferred for a new/replacement chat; reconstruct Git and execute the READY instruction without redundant re-derivation.
- `VERIFY-LEGACY`: no active sweep; the v0.4–v0.26 sweep is complete and frozen as RB-011.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.27 execution-contract canonicalization result |
| 10 CORE | READY | execute v0.27 Hierarchical Repeated-Trial Execution Contract Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance / command protocol v0.2: STABLE ADMINISTRATIVE
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v2.0
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

## Frozen v0.27 first target

The first target is passive hierarchical recovery of two shared network parameters from repeated independently prepared N=3 Lighthouse trials.

### Shared block

`theta_s=(p,tau_3)` with known topology and fixed affine weight/delay families whose complete numerical matrices must be frozen by the next contract.

### Trial-specific preparation

Each trial has six gauge-fixed zero-mean q=1 preparation coordinates:

`z_r=(eta_r,xi_psi,r,xi_q,r) in R^6`.

The nominal preparation mean is known/fixed in this first branch.

### Hierarchical law

`z_r | lambda ~ iid N(0,Sigma_z(lambda))`,

with three isotropic preparation scales for phase, psi and q. The population-level unknown block is

`vartheta=(p,tau_3,lambda_phi,lambda_psi,lambda_q)`.

Unknown population means, covariance anisotropy/cross-covariance and non-Gaussian laws are deferred.

### Observation model

Labelled spike-time observations have known Gaussian timing-noise scale and an observed iid MCAR missing-slot mask with known missingness probability. A missing timestamp does not remove the physical spike from the latent trajectory.

Unlabelled spikes, unknown topology and unknown global observation clock are deferred.

### Intervention

No active pulse or direct subthreshold sensor is allowed in the first v0.27 execution. Legacy optimized v0.24/v0.25 designs remain C3 and are not imported.

### Primary inference route

Laplace-approximated marginal maximum likelihood is the fixed primary route. It may not be replaced post hoc by EM, VI, MCMC or another objective within this branch if it fails.

### Primary scientific questions

1. Does conservative free-nuisance shared information have rank two under the preregistered design?
2. Is the five-dimensional hierarchical local information/Hessian full rank and numerically regular?
3. Are shared scientific directions distinguishable from the three preparation-scale directions through the corresponding Schur/profile block?
4. Does observed missingness keep information/admissibility failure within the predeclared success rule?

No global-identifiability claim is part of this first scope.

## Mandatory next execution-contract freeze list

Before any v0.27 scientific output, the next contract must freeze:

- complete physical graph matrices/topology and baseline constants;
- nominal initial state and gauge;
- truth and compact parameter/hyperparameter domains;
- preparation-scale truth;
- trial count R and horizon H;
- timing-noise scale and missingness probability;
- stochastic replicate count and immutable seeds;
- minimal-data/admissibility rules;
- trial-mode and outer optimization algorithms, initializations, derivative methods, stopping tolerances and budgets;
- event-chart/rerecording rules;
- numerical rank and conditioning thresholds;
- uncertainty construction and coverage target;
- all finite scientific success/failure thresholds;
- a deterministic C2 implementation validation sub-contract for the exact path required by v0.27.

None may be selected using v0.27 output or favorable legacy C3 effect sizes.

## Required C2 path

Only the minimal implementation path is required before effect-bearing execution:

1. physical fixed-delay alpha event scheduler and labelled events;
2. fixed-chart derivatives with respect to `(p,tau_3,z)`;
3. chart-validity sentinel plus physical rerecording;
4. hierarchical Gaussian penalty, trial-mode Hessian/logdet, mask selection and outer five-parameter Laplace objective.

Legacy v0.18–v0.20 code is C2 candidate material only until validated under a frozen contract.

## Legacy disposition remains unchanged

- Actual Lighthouse bifurcation/global-object effects v0.6–v0.15 remain C3 unless freshly preregistered.
- Optimized/effect-selected inference/design findings v0.21–v0.26 remain C3.
- Legacy ~250x, ~87x, ~788x and ~557x gains remain non-confirmatory historical results.
- Full spike-time/full-hybrid Floquet spectral equivalence and rigorous higher regularity across moving arrival configurations remain open.

## Active blocker

The only blocker is completion of the v0.27 execution-contract canonicalization gate.

Until that contract returns and MASTER freezes it:

- no v0.27 dataset generation;
- no v0.27 scientific simulation/inference;
- no search for favorable truth, R, H, noise or missingness;
- no post-output tolerance or solver changes;
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

## Manuscript

WAIT. No v0.27 scientific result exists yet and no downstream C3 legacy effect is manuscript evidence.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized. The new v0.27 scope is a project research target, not a novelty claim.

## Next global step

In `10 – CORE – Haupttheorie / mathematischer Kern`, execute:

`GO`

For a new/replacement CORE chat, execute:

`RESUME`

Current prompt:

`research/master/prompts/core_v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md`

This next gate freezes the complete execution contract only. It must not generate scientific v0.27 output.

## STOP

STOP — AWAIT CORE V0.27 HIERARCHICAL REPEATED-TRIAL EXECUTION CONTRACT CANONICALIZATION
