# Lighthouse-JAX — Canonical Project Status

Version: 2.3
Date: 2026-09-07

## Central research question

Can Hermann Haken's Lighthouse model be developed into a modern, scalable and differentiable framework for spiking-network dynamics that remains mathematically analyzable while supporting contemporary numerical simulation, inference and neuromorphic applications?

## Global status

The verification-first command rule remains:

`Reconstruct state, not frozen science.`

The recovered legacy corpus v0.4–v0.26 remains classified in RB-011 and its strongest independently verified C1 mathematics remains frozen in RB-012. No legacy C3 numerical effect has been promoted.

The first genuinely new v0.27 branch remains frozen as a valid negative result:

- scope: RB-013;
- execution contract: RB-014;
- result: RB-015 — `SCIENTIFIC FAIL`.

RB-015 is immutable and is not rescued or relabelled by later method development.

The governed failure-mechanism/follow-up preregistration gate has now returned:

`PASS — FAILURE MECHANISM SUFFICIENTLY DIAGNOSED; ONE FOLLOW-UP ROUTE PREREGISTERED IN SCOPE`.

MASTER accepts that result and establishes `CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1` / RB-016.

The single next scientific action is `CORE v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1`.

No confirmatory v0.27c dataset may be generated in that contract gate.

## Frozen RB-015 result remains

`SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS`.

Frozen facts remain:

- C2-27-01 through C2-27-08 PASS;
- `INSUFFICIENT_MASK=0/32`;
- truth physical/chart invalid `=0/32`;
- conservative nuisance-profiled shared information rank-two/regular `32/32`;
- 96 frozen outer starts attempted;
- finite complete initial Laplace objectives `0/96`;
- `OUTER_OPT_FAIL=32/32`;
- usable fits `0/32`;
- valid five-parameter uncertainty intervals `0/32`.

## Frozen v0.27b failure diagnosis

The 32 RB-015 datasets and optimization traces are observed and were used only as POST-HOC / DEVELOPMENT evidence.

The dominant diagnosed numerical mechanism is:

`inner BFGS / Strong-Wolfe globalization + quasi-Newton stagnation, not event-chart invalidity`.

Key governed development findings:

- all 96 exposed failed directions admit valid same-itinerary dyadic probes;
- Armijo points exist for 95/96 directions, while simultaneous Armijo + Strong-Wolfe appears on 12/96 fixed probes;
- 82/96 failures meet the preregistered quasi-Newton-stagnation diagnostic;
- stratified AD/FD checks do not support incorrect fixed-chart gradients as the dominant mechanism;
- 11/12 stratified local Hessians are positive definite;
- Armijo-only BFGS and whitened Strong-Wolfe BFGS do not solve the problem reliably on the exposed subset;
- a whitened trust-region nonlinear-least-squares DEVELOPMENT prototype gives finite termination on 94/96 exposed failed trials, with two invalid-step cases exposing the need for explicit physical/chart-invalid proposal rejection and radius contraction.

The `94/96` count is development evidence only and may not be reused as a confirmatory success threshold.

## Frozen v0.27c follow-up scope

Exactly one follow-up route is permitted:

`v0.27c Whitened Trust-Region Laplace Route`.

The statistical/scientific model remains the RB-014 hierarchy. For each trial:

`u=S(lambda)^(-1)z`, `z=S(lambda)u`,

and the trial mode is posed as

`min_u 0.5 || [M(y-F(theta_s,S u))/sigma_t ; u] ||^2`.

The solver class is deterministic trust-region Gauss-Newton / nonlinear least squares with exact current-chart JAX Jacobians and physical rerecording at every proposal. Physically invalid, colliding, nontransverse or derivative-chart-invalid proposals must be rejected by trust-radius contraction/retry; stale event tokens may never be accepted.

The following remain inherited unchanged unless MASTER separately authorizes a prospective change before confirmatory output:

- N=3 physical graph/model and truth;
- shared/hyperparameter boxes and hierarchical Gaussian family;
- `R=16`, `H=4`;
- timing noise `0.02` and MCAR missingness `0.20`;
- outer bounded-Powell class and the three inherited starts;
- RB-014 scientific recovery, identifiability, coverage, failure and usable-fit thresholds;
- no active pulse/probe and no EM/VI/MCMC alternative.

## Confirmatory data boundary

The RB-015 `2701xxx` seed namespace is permanently DEVELOPMENT ONLY for the v0.27c method selected after observing it.

The v0.27c confirmatory namespace is reserved but remains UNGENERATED / UNEVALUATED:

- `seed_z^c(d)=2711000+3d`;
- `seed_noise^c(d)=2711001+3d`;
- `seed_mask^c(d)=2711002+3d`;
- `d=0,...,31`.

No `2711xxx` RNG object was created or inspected in v0.27b.

## Mandatory v0.27c pre-execution contract

Before any confirmatory RNG creation, the current gate must freeze:

- exact trust-region step algorithm;
- initial/minimum/maximum radius;
- predicted/actual reduction definitions;
- acceptance-ratio thresholds;
- radius contraction/expansion factors and update logic;
- invalid-proposal retry handling;
- whitened stationarity/convergence thresholds;
- iteration/evaluation/contraction budgets;
- final Hessian/logdet coordinate semantics;
- trial failure and outer-point failure semantics;
- deterministic TR-27C-01 through TR-27C-07 fixtures, tolerances and negative controls;
- complete finite outer-start assembly rule;
- inherited RB-014 scientific thresholds;
- disjoint `2711xxx` seed mapping;
- environment and change-control rules.

All TR-27C checks must later PASS before confirmatory RNG creation.

## Command protocol

- `GO`: execute only the current READY Next instruction and reuse FROZEN/STABLE premises.
- `RESUME`: preferred for a new/replacement chat; reconstruct Git state and execute the current READY instruction without redundant re-derivation.
- `VERIFY-LEGACY`: no active sweep; the legacy sweep is complete and frozen as RB-011.

## Workstreams

| Workstream | Status | Current role |
|---|---|---|
| 00 MASTER | FROZEN / WAIT | oversight; awaiting v0.27c execution-contract canonicalization result |
| 10 CORE | READY | execute v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1 only |
| 50 APP-1 Computational Neuroscience | PROTECTED / WAIT | reserved application branch |
| 60 APP-2 Neuromorphic Computing | PROTECTED / WAIT | reserved application branch |
| 70 APP-3 Differentiable Inference / Temporal Learning | PROTECTED / WAIT | reserved application branch |
| 80 LIT | WAIT | no independent novelty positioning yet |
| 90 MANUSCRIPT | WAIT | no manuscript claims before later result/claim freezes |

## Current freezes

- Governance / command protocol v0.2: STABLE ADMINISTRATIVE
- MASTER report snapshot: STABLE v0.2 administrative artifact; administratively behind project status v2.3
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
- RB-016 CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1: FROZEN / STABLE DIAGNOSTIC + FOLLOW-UP SCOPE

## Active blocker

The sole active blocker is completion of `CORE v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1`.

Until return:

- no `2711xxx` RNG creation;
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
16. RB-016 CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1 — FROZEN / STABLE DIAGNOSTIC + FOLLOW-UP SCOPE

## Manuscript

WAIT. RB-015 remains a valid negative result, but no manuscript claim freeze is authorized.

## Literature positioning

WAIT. Independent novelty positioning remains unauthorized.

## Next global step

In `10 – CORE – Haupttheorie / mathematischer Kern`, execute:

`GO`

For a new/replacement CORE chat, execute:

`RESUME`

Current prompt:

`research/master/prompts/core_v0_27c_whitened_trust_region_laplace_execution_contract_canonicalization_gate_0_1.md`

This gate freezes the v0.27c execution contract only. It must not create confirmatory RNG or execute redesigned confirmatory science.

## STOP

STOP — AWAIT CORE V0.27C WHITENED TRUST-REGION LAPLACE EXECUTION CONTRACT CANONICALIZATION
