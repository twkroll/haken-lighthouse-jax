# CORE v0.27b Inference Failure Mechanism & Follow-up Preregistration Gate 0.1

Date: 2026-09-07
Status: PASS — FAILURE MECHANISM SUFFICIENTLY DIAGNOSED; ONE FOLLOW-UP ROUTE PREREGISTERED IN SCOPE

## 1. Authority, Git identity, and provenance boundary

This gate executes the MASTER-authorized prompt

`research/master/prompts/core_v0_27b_inference_failure_mechanism_followup_preregistration_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `7ed49bf8d5ac51b51896693d041db7703db22989`
- CORE STATUS blob: `3a8a7b75e2e0a2a9d431a980c6b1d530cbe61960`
- MASTER prompt blob: `7309575eb936d2ab060a0e6ddcdb399e11f91f37`
- MASTER STATUS blob: `7599ea613ec4b8dfac890e1914016a4086631b60`
- MASTER project-status blob: `dc5b278ec1b0ad118fb767d585b811efd8afd723`
- RB-013 scope freeze blob: `287b8942a17bb363e888bee7fe367b2066e3051e`
- RB-014 execution-contract freeze blob: `dec52d17974ee49c792e6553c68aed72d5ae5813`
- RB-015 result freeze blob: `92625f130bdcf510ce95493c69eaab3e00db2454`
- frozen RB-015 execution result commit: `07a813e42107d3eea69fec1e858e586adad367bb`
- frozen RB-015 RETURN-TO-MASTER commit: `e17489514be283b5daa3e254504e97edd7ee5fa6`

The 32 RB-015 datasets and their retained optimization traces are observed data. Every numerical probe in Sections 4–6 is therefore labelled **POST-HOC / DEVELOPMENT EVIDENCE**. None is a confirmatory recovery, coverage, identifiability or performance result.

No RB-015 label, metric, seed, dataset or frozen result is overwritten. No new confirmatory seed in the namespace proposed below was generated or inspected in this gate.

---

## 2. Exact frozen RB-015 result

RB-015 remains:

`SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS`.

Frozen facts reused without reinterpretation:

1. C2-27-01 through C2-27-08 all passed, including negative controls.
2. `INSUFFICIENT_MASK=0/32` and truth physical/chart invalid `=0/32`.
3. Conservative nuisance-profiled shared information was rank-two/regular in `32/32`, with condition numbers `348731`–`712596 < 1e8`.
4. All `32 x 3 = 96` frozen outer starts had a non-finite complete initial Laplace objective because at least one trial-mode BFGS solve hit `STRONG_WOLFE_20_FAIL`.
5. Consequently `OUTER_OPT_FAIL=32/32`, usable fits `0/32`, valid five-parameter uncertainty intervals `0/32`.
6. The branch result is and remains **SCIENTIFIC FAIL**.

This gate does not treat the positive `I_free` audit as a rescue of the failed inference route, and does not treat the failed inference route as proof of global non-identifiability.

---

## 3. Failure-mechanism hypotheses fixed before diagnostic families

The following hypotheses were stated before their corresponding diagnostic families were evaluated.

| ID | Hypothesis | Diagnostic discriminator |
|---|---|---|
| H1 | event-chart or physical invalidity is the dominant cause | failed-line directions should encounter chart changes, collision/transversality failure, or no valid descent step |
| H2 | incorrect/non-smooth fixed-chart gradient is the dominant cause | development directional finite differences should disagree materially with AD inside unchanged charts |
| H3 | Strong-Wolfe compatibility/globalization is the dominant cause | valid Armijo descent points should exist while simultaneous Strong-Wolfe points are rare or inaccessible to the frozen search |
| H4 | BFGS inverse-Hessian scaling/stagnation is a major contributor | failed directions should collapse to numerically tiny steps/directional derivatives before the fixed gradient tolerance is met; whitening alone may or may not cure it |
| H5 | the 16-trial aggregation itself creates failure although individual modes are otherwise straightforward | failure should be localized to specific trial modes rather than physical dataset invalidity; a solver class not requiring Strong-Wolfe should obtain finite development modes on the exposed failed trials |

No hypothesis changes the RB-015 result.

---

## 4. POST-HOC / DEVELOPMENT diagnostic protocol and results

### 4.1 D1 — all 96 frozen failure points: fixed directional grid and chart audit

For each of the 96 RB-015 failed outer-start/trial-mode traces, reconstruct the exact BFGS failure iterate `z`, gradient `g` and final descent direction `d` immediately before `STRONG_WOLFE_20_FAIL`.

Evaluate the physical objective and current-chart gradient on the fixed dyadic grid

`alpha_k = 2^(-k), k=0,...,30`,

using physical rerecording at every grid point. For each point record:

- physical/chart validity;
- whether the event itinerary equals that at the failure iterate;
- Armijo sufficient decrease with `c1=1e-4`;
- Strong-Wolfe curvature with `c2=0.9`;
- simultaneous Armijo + Strong-Wolfe satisfaction.

Results:

- at least one valid grid point: `96/96`;
- all valid grid points remained on the failure-point event itinerary: `96/96` failure directions; no observed grid chart change;
- at least one Armijo point: `95/96`;
- at least one curvature-satisfying point: `93/96`;
- at least one point satisfying both Armijo and Strong-Wolfe: `12/96`.

**Interpretation:** H1 is strongly disfavored as the dominant cause. The frozen failures are not explained by an inability to take any physically valid descent step. H3 is supported: ordinary sufficient-decrease steps are ubiquitous while the simultaneous strong-Wolfe condition is much more restrictive on the exposed directions.

### 4.2 D2 — BFGS direction-collapse audit on all 96 failures

At the same failure points classify a failure as `quasi-Newton stagnation` when either

`abs(g^T d) < 1e-12`

or

`||d||_2 < 1e-8`.

Results:

- quasi-Newton-stagnation failures: `82/96`;
- remaining finite-step failures: `14/96`;
- median failure BFGS iteration: `13` (range `1`–`20`);
- median `||g||_inf` at failure: `6.583106976876252e-06`;
- failures with `||g||_inf < 1e-6`: `34/96`;
- failures with `||g||_inf < 1e-5`: `53/96`;
- failures with `||d||_2 < 1e-8`: `62/96`;
- failures with `abs(g^T d)<1e-12`: `82/96`.

Within the 82 stagnation failures:

- at least one Armijo point exists on the dyadic grid in `81/82`;
- a simultaneous Strong-Wolfe grid point exists in only `3/82`.

Within the 14 finite-step failures:

- an Armijo point exists in `14/14`;
- a simultaneous Strong-Wolfe grid point exists in `9/14`.

**Interpretation:** H4 is strongly supported as a major mechanism. In most failures the BFGS inverse-Hessian approximation has collapsed the search direction to a numerically tiny direction before the fixed `gtol=1e-8` criterion is met. The subsequent Strong-Wolfe curvature test is then imposed relative to a tiny directional derivative, creating a numerical globalization/termination mismatch rather than an event-chart failure.

### 4.3 D3 — stratified gradient/smoothness audit

Use the deterministic stratified subset

`dataset d in {0,8,16,24} x outer start {S0,S1,S2}`,

and the first RB-015 failed trial for that start, giving 12 failure points.

For each point, normalize the failed BFGS direction to unit length and compare `g^T u` with physically rerecorded centered directional finite differences at the fixed steps `1e-4`, `1e-5`, `1e-6`.

Relative disagreement is `|FD-AD|/max(1,|FD|,|AD|)`.

Results:

| FD step | median relative disagreement | maximum relative disagreement |
|---:|---:|---:|
| `1e-4` | `2.40358e-7` | `4.72743e-6` |
| `1e-5` | `1.62190e-7` | `1.20391e-6` |
| `1e-6` | `2.15028e-6` | `1.00433e-5` |

The nonmonotone smallest-step error is consistent with subtraction/noise in finite differences of a physically integrated objective. Together with the already frozen C2-27-03 actual-Lighthouse AD/FD relative error `1.41455e-9`, these diagnostics do not support H2 as the dominant failure mechanism.

### 4.4 D4 — local Hessian curvature on the same 12 points

Compute the exact fixed-chart trial-objective Hessian at the 12 stratified failure iterates.

Results:

- positive definite: `11/12`;
- one point is locally indefinite (`lambda_min approximately -808.95`);
- positive/absolute raw Hessian condition numbers range approximately `171`–`3336` on this subset.

Thus the inner objective is not globally convex and one local indefinite case exists, but universal local indefiniteness is ruled out. This further supports a globalization problem rather than a universal absence of local curvature.

---

## 5. POST-HOC / DEVELOPMENT candidate-solver comparison

This section is method development only. No redesigned-method recovery, bias, coverage or population-parameter performance was computed or claimed.

### Candidate A — Armijo-only BFGS in original `z` coordinates

On the same 12 stratified exposed failed trials, use BFGS from `z=0` with ordinary Armijo backtracking instead of Strong-Wolfe; retain the strict `||g||_inf<=1e-8` target for this diagnostic.

Result:

- strict convergence: `4/12`;
- `8/12` still terminate by Armijo failure or the finite iteration budget.

Conclusion: removing the curvature condition alone is insufficient.

### Candidate B — Strong-Wolfe BFGS in whitened coordinates

Use the natural random-effect whitening

`u = S(lambda)^(-1) z`,

where

`S(lambda)=diag(sigma_phi,sigma_phi,sigma_psi,sigma_psi,sigma_q,sigma_q)`,

so the Gaussian prior contribution is `0.5 ||u||^2` up to the log-determinant term.

Keep Strong-Wolfe BFGS otherwise unchanged.

Result on the 12 stratified exposed trials:

- strict convergence: `3/12`.

Conclusion: parameter whitening alone is insufficient; H4 is not merely a units problem.

### Candidate C — whitened trust-region nonlinear least squares

Write the trial mode objective, up to the lambda-dependent constant, as the augmented nonlinear least-squares problem

`0.5 || r_aug(u) ||^2`,

with

`r_aug(u) = [ M(y-F(theta_s,S(lambda)u))/sigma_t ; u ]`.

Use physical rerecording plus exact current-chart JAX Jacobians, and a standard trust-region least-squares DEVELOPMENT prototype. This prototype did not yet contain the required production rule to reject an invalid physical/chart step by shrinking the trust region; therefore any proposed invalid step was conservatively recorded as a development failure.

Results:

- standard finite termination on the 12 stratified exposed failed trials: `12/12`;
- broad development feasibility on all 96 exposed RB-015 failure trials: `94/96` finite terminations;
- the remaining two cases are exactly `d=5/S2/r0` and `d=9/S2/r0`, where the standard prototype proposed a physically/chart-invalid trial step and lacked the required radius-contraction/retry policy;
- among the 94 finite prototype terminations, median function evaluations `26`, maximum `69`;
- these termination counts/gradients are DEVELOPMENT diagnostics only and are not confirmatory solver-success thresholds.

Conclusion: Candidate C directly removes dependence on a BFGS inverse-Hessian approximation and Strong-Wolfe compatibility, exploits the exact least-squares structure of the trial posterior mode, and exposes one remaining implementation requirement clearly: physical/chart-invalid proposals must be rejected by trust-radius contraction rather than causing solver abort.

---

## 6. Dominant failure-mechanism classification

### Classification

**Dominant mechanism: BFGS/Strong-Wolfe globalization and quasi-Newton stagnation in the inner trial-mode problem, not event-chart invalidity.**

More precisely:

1. **High confidence** that event-chart invalidity is not the dominant mechanism, because all 96 failed directions admit valid same-itinerary dyadic probes and the frozen truth/C2 paths are physically regular.
2. **High confidence** that Strong-Wolfe/BFGS stagnation is a dominant mechanism, because 82/96 failures have numerically collapsed descent directions/directional derivatives while most still possess a valid Armijo descent point.
3. **Moderate-to-high confidence** that a trust-region least-squares globalization is an appropriate controlled follow-up class, because the augmented residual structure is exact and the development prototype obtains finite modes in 94/96 exposed failure trials without changing the scientific model or data.
4. **Limitation:** these 32 datasets are observed and the candidate comparison is post hoc. The 94/96 result is not evidence of confirmatory recovery performance and cannot be used as a later success threshold.
5. **Limitation:** the exact trust-region radius rules, acceptance ratio, convergence tolerances and evaluation budgets have not been frozen here. They require a separate pre-execution contract and deterministic validation before any new confirmatory RNG is instantiated.

H5 is partly supported in the narrow numerical sense: a single failing trial mode makes an entire outer point non-finite, so inner globalization failure is amplified by 16-trial aggregation. This does not imply that 16 trials are scientifically inappropriate; `R=16` remains inherited unchanged.

---

## 7. Exactly one follow-up inference route preregistered in scope

The only proposed follow-up route is:

### `v0.27c Whitened Trust-Region Laplace Route`

#### 7.1 Inner parameterization

For every trial use whitened random effects

`u_r = S(lambda)^(-1) z_r`,

with `z_r=S(lambda)u_r`.

The statistical model is unchanged. This is a numerical parameterization only.

#### 7.2 Inner solver class

Solve the exact augmented residual problem

`min_u 0.5 || [M(y-F(theta_s,S u))/sigma_t ; u] ||^2`

by a deterministic **trust-region Gauss-Newton / nonlinear-least-squares** method with exact current-chart JAX Jacobians.

Every proposed point must be physically rerecorded. If it is physically invalid, colliding, nontransverse, or derivative-chart invalid, the proposal is rejected and the trust radius is contracted; a stale event token is never accepted. Exact acceptance-ratio, radius update, convergence and budget constants must be frozen in a later execution-contract gate before confirmatory data generation.

The final trial-mode Laplace Hessian remains the exact second derivative of the original `Phi_r` in physical `z` coordinates (or its exactly transformed equivalent), with the existing no-jitter positive-definiteness/log-determinant rules unless a later MASTER gate finds a purely algebraic equivalence repair is required.

#### 7.3 Population inference retained

The following remain inherited unchanged from RB-014 unless MASTER explicitly opens a separate justified branch before the new confirmatory contract:

- hierarchical Gaussian model and Laplace marginal objective;
- population unknowns `(p,tau_3,lambda_phi,lambda_psi,lambda_q)`;
- outer five-parameter box scaling and bounded Powell class;
- the same three population starts and deterministic tie breaking;
- outer Hessian/Schur/uncertainty definitions;
- all scientific recovery, identifiability, coverage, failure-fraction and usable-fit thresholds.

No EM, VI, MCMC, active sensing or alternate scientific objective is part of v0.27c.

---

## 8. Scientific design inheritance and new confirmatory data boundary

### 8.1 Inherited unchanged from RB-014

The follow-up keeps unchanged:

- `N=3` directed cycle and all `W^(0),B,Tau^(0),C` matrices;
- `alpha=1,r=1,h=-1`;
- nominal preparation and gauge;
- truth `p*=0.05,tau_3*=0.90`;
- `Theta=[-0.20,0.20] x [0.60,1.60]`;
- zero-mean Gaussian three-scale random-effects law;
- truth `sigma_phi*=sigma_psi*=sigma_q*=0.05` and the same `Lambda` box;
- `R=16`, `H=4`, `K=12`;
- known `sigma_t=0.02`;
- MCAR `pi_miss=0.20`;
- `D=32` confirmatory replicates;
- minimal-mask, physical timeout, event/chart and collision semantics;
- no active pulse or direct subthreshold sensor;
- the RB-014 scientific decision thresholds.

No scientific design variable is changed in response to RB-015 effect inspection.

### 8.2 Old-data exclusion

The RB-015 datasets with seeds `2701000`–`2701095` are permanently **DEVELOPMENT ONLY** for any method selected in this gate. They are excluded from the v0.27c confirmatory performance decision.

### 8.3 New disjoint confirmatory seed namespace

Reserve, but do **not** generate in this gate, exactly 32 new replicate triplets for `d=0,...,31`:

`seed_z^c(d)     = 2711000 + 3d`,

`seed_noise^c(d) = 2711001 + 3d`,

`seed_mask^c(d)  = 2711002 + 3d`.

This namespace is disjoint from RB-015. No RNG object using any `2711xxx` confirmatory seed was created or inspected in this gate.

---

## 9. Mandatory deterministic redesigned-solver validation contract to be frozen before confirmatory execution

A later v0.27c execution contract must include at least the following finite suite, with exact tolerances/budgets frozen before any `2711xxx` RNG creation.

### TR-27C-01 — whitening algebra identity

At fixed `lambda`, verify for deterministic vectors/matrices that

`z=S u`, `0.5 z^T Sigma^-1 z = 0.5 u^T u`,

`g_u=S g_z`, and `H_u=S H_z S` for the transformed scalar objective on a fixed valid chart.

Required negative control: permute one scale block; comparator must fail.

### TR-27C-02 — exact linear-Gaussian mode

Reuse the deterministic linear-Gaussian six-random-effect toy structure from C2-27-06, expressed in whitened coordinates. Compare the trust-region mode with the exact normal-equation solution and compare final original-coordinate Hessian/logdet with the analytical reference.

Required negative control: corrupt one Jacobian column; comparator must fail.

### TR-27C-03 — actual Lighthouse residual/Jacobian transformation

At the frozen physical graph and a deterministic full-observation no-noise fixture, compare the augmented whitened residual Jacobian against physically rerecorded centered finite differences and against the already validated physical `z`-Jacobian transformed by `S`.

### TR-27C-04 — trust-region invalid-step contraction

Use a deterministic chart-boundary fixture derived from C2-27-04 plus at least one development-only RB-015 hard fixture. Force/provoke a proposed invalid step. The solver must reject the proposal, contract its radius, rerecord physically, and never evaluate/accept a stale-chart derivative.

A crash, artificial event ordering, stale-token acceptance or silent step clipping is FAIL.

### TR-27C-05 — stationarity and objective consistency

For a deterministic Lighthouse trial with a valid isolated mode, compare the final trust-region point against an independent high-accuracy local reference and verify the original `Phi_r`, whitened residual objective and transformed gradients agree algebraically/numerically.

### TR-27C-06 — deterministic development regression suite

Use a frozen finite subset of RB-015 failure traces strictly as DEVELOPMENT fixtures, including both prototype-invalid-step cases `d=5/S2/r0` and `d=9/S2/r0`. The purpose is implementation regression only; no recovery/error/coverage metric from these old datasets can enter the confirmatory scientific decision.

### TR-27C-07 — finite outer-start assembly

On deterministic non-stochastic fixtures, verify that 16 valid trial modes assemble into a finite Laplace objective for each of the three inherited outer starts and that a deliberately invalid trial produces the documented non-finite/failure classification rather than a SciPy crash.

### Suite boundary

All TR-27C checks must pass before any new `2711xxx` confirmatory RNG object is created. Any failure returns to MASTER without confirmatory science. Exact tolerances, trust-radius constants and budgets are to be frozen in the next pre-execution contract, not selected from new confirmatory outputs.

---

## 10. Finite follow-up observables to be fixed before confirmatory execution

The later v0.27c pre-execution contract must freeze numerical thresholds for the redesigned solver before new RNG creation, including:

1. per-trial inner convergence/stationarity criterion in a dimensionless/whitened norm;
2. maximum trust-region iterations, residual/Jacobian evaluations and invalid-proposal contractions;
3. trust-radius initialization, minimum/maximum radius and acceptance-ratio thresholds;
4. finite-complete-start fraction and `INNER_MODE_FAIL`/`INNER_HESSIAN_FAIL` fractions;
5. exact treatment of an outer point if one or more trial modes fail;
6. all existing RB-014 scientific recovery/identifiability/coverage/usable-fit thresholds, inherited unchanged unless MASTER explicitly authorizes a separate prospective reason to change them before confirmatory output.

The old `94/96` development feasibility count is expressly **not** a success threshold.

---

## 11. Deferred branches remain deferred

This gate does not authorize:

- a confirmatory v0.27c run;
- v0.28 science;
- active pulse/probe design or direct subthreshold sensing;
- pulse calibration inference;
- unknown topology or unlabelled spikes;
- changed truth, graph, `R`, `H`, timing noise or missingness;
- alternative hierarchical families;
- EM, VI or MCMC;
- legacy C3 optimized designs/gains;
- applications, novelty positioning or manuscript claims.

---

## 12. Gate decision

# PASS — FAILURE MECHANISM SUFFICIENTLY DIAGNOSED; ONE FOLLOW-UP ROUTE PREREGISTERED IN SCOPE

The evidence is sufficient to distinguish the frozen failure from an event-chart implementation failure and to identify the dominant numerical mechanism as inner BFGS/Strong-Wolfe globalization/stagnation. One and only one follow-up route is proposed: a whitened trust-region nonlinear-least-squares trial-mode solver inside the otherwise inherited Laplace hierarchy, with explicit physical invalid-step rejection/radius contraction.

This PASS does **not** establish that v0.27c will recover the parameters, satisfy coverage, yield a finite outer optimum, or pass scientifically. All method-comparison evidence here is POST-HOC / DEVELOPMENT.

No confirmatory redesigned-method performance was established in this gate.

## 13. Proposed MASTER decision

If MASTER accepts this gate, the narrow next action should be a separate

`CORE v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1`

that freezes the exact trust-region algorithm, radius/acceptance rules, deterministic TR-27C validation tolerances, budgets, failure handling, inherited scientific thresholds and the reserved disjoint `2711xxx` seed namespace **before** any confirmatory dataset is generated.

CORE does not self-authorize that contract freeze or any confirmatory execution.

## STOP

STOP — RETURN TO MASTER; RB-015 REMAINS SCIENTIFIC FAIL; NO REDESIGNED CONFIRMATORY EXECUTION
