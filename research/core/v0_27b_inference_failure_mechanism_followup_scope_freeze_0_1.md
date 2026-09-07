# CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE DIAGNOSTIC + FOLLOW-UP SCOPE
Rollback point: RB-016

## Authority

MASTER accepts `research/core/v0_27b_inference_failure_mechanism_followup_preregistration_gate_0_1.md` as the governed diagnostic result following RB-015.

Frozen source artifact:

- file: `research/core/v0_27b_inference_failure_mechanism_followup_preregistration_gate_0_1.md`
- blob SHA: `aca57e3771b38fc3db0252db6b7a16178c094752`
- result commit: `81d5fd3de5fb2b429fd5299c1004ac418c6e0549`
- RETURN-TO-MASTER commit: `30877a5f15096eb902dfce2bca9d0910fc02d65d`
- failed-result authority: RB-015
- execution-contract authority: RB-014
- scope authority: RB-013.

## Frozen gate result

`PASS — FAILURE MECHANISM SUFFICIENTLY DIAGNOSED; ONE FOLLOW-UP ROUTE PREREGISTERED IN SCOPE`

RB-015 remains unchanged and final as `SCIENTIFIC FAIL` for the original RB-014 branch.

## Frozen diagnostic classification

The dominant observed numerical mechanism is:

`inner BFGS / Strong-Wolfe globalization + quasi-Newton stagnation, not event-chart invalidity`.

The following development findings are frozen as POST-HOC / DEVELOPMENT EVIDENCE only:

- valid same-itinerary dyadic probes exist for all 96 exposed failure directions;
- Armijo descent exists for 95/96 directions, while simultaneous Armijo + Strong-Wolfe appears on only 12/96 fixed probes;
- 82/96 failures meet the preregistered quasi-Newton-stagnation diagnostic;
- stratified AD/FD checks do not support an incorrect fixed-chart gradient as the dominant mechanism;
- 11/12 stratified local Hessians are positive definite, so universal local indefiniteness is not the explanation;
- development Candidate A (Armijo-only BFGS) converges strictly on 4/12 exposed trials;
- development Candidate B (whitened Strong-Wolfe BFGS) converges strictly on 3/12 exposed trials;
- development Candidate C (whitened trust-region nonlinear least squares) gives finite development termination on 94/96 exposed failed trials, with two prototype invalid-step cases requiring explicit radius contraction/retry.

None of these post-hoc counts is a confirmatory performance result or success threshold.

## Frozen follow-up scope

Exactly one follow-up route is authorized in scope:

`v0.27c Whitened Trust-Region Laplace Route`.

The statistical/scientific model remains inherited from RB-014. The inner random effects are parameterized by `u=S(lambda)^(-1)z`, and the trial mode is posed as the exact augmented nonlinear least-squares problem

`min_u 0.5 || [M(y-F(theta_s,S u))/sigma_t ; u] ||^2`.

The intended solver class is deterministic trust-region Gauss-Newton / nonlinear least squares with exact current-chart JAX Jacobians, physical rerecording at every proposal, and mandatory rejection plus radius contraction for physically/chart-invalid proposals. The final Laplace Hessian/logdet remains based on the original trial objective with the existing no-jitter validity semantics unless a later MASTER-authorized algebraic-equivalence repair is required.

Inherited unchanged unless separately authorized prospectively before confirmatory output:

- physical graph/model, truth and parameter boxes;
- hierarchical Gaussian law and population block;
- `R=16`, `H=4`, timing noise and MCAR missingness;
- outer bounded-Powell class, three outer starts and tie breaking;
- scientific recovery, identifiability, coverage, failure and usable-fit thresholds;
- no active pulse/probe and no alternate EM/VI/MCMC objective.

## Confirmatory data boundary

The RB-015 seed namespace `2701000`–`2701095` is permanently DEVELOPMENT ONLY for v0.27c method selection.

Reserved but UNGENERATED / UNEVALUATED confirmatory namespace:

- `seed_z^c(d)=2711000+3d`
- `seed_noise^c(d)=2711001+3d`
- `seed_mask^c(d)=2711002+3d`
- `d=0,...,31`.

No `2711xxx` RNG object was created or inspected in the v0.27b gate.

## Mandatory next contract requirements

Before any `2711xxx` RNG creation, a separate v0.27c execution-contract gate must freeze:

- the exact trust-region algorithm;
- initial/minimum/maximum trust radius;
- acceptance-ratio and radius-update rules;
- convergence/stationarity criteria;
- iteration/evaluation/invalid-proposal budgets;
- exact failure handling;
- TR-27C-01 through TR-27C-07 finite deterministic validation cases, tolerances and negative controls;
- complete outer-start assembly rule;
- inherited RB-014 scientific thresholds and the disjoint seed namespace.

All TR-27C checks must pass before confirmatory RNG creation.

## Change control and exclusions

RB-016 does not authorize confirmatory v0.27c execution. It does not relabel or rescue RB-015, and it does not validate the 94/96 development feasibility count as a scientific result.

No v0.28, active pulse/probe extension, alternate hierarchy, EM/VI/MCMC, legacy C3 promotion, application work, novelty positioning or manuscript claim freeze is authorized here.

## STOP

`CORE v0.27b Inference Failure Mechanism & Follow-up Scope Freeze 0.1` is established.

STOP — FROZEN
