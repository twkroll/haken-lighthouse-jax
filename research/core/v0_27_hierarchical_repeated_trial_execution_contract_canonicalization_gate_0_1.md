# CORE v0.27 Hierarchical Repeated-Trial Execution Contract Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — COMPLETE PRE-EXECUTION CONTRACT FIXED; NO V0.27 SCIENTIFIC DATASET OR INFERENCE EXECUTED

## 1. Authority, identity, and freeze boundary

This gate executes the MASTER-authorized prompt

`research/master/prompts/core_v0_27_hierarchical_repeated_trial_execution_contract_canonicalization_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `7da783b5af0af56b4c684cf813f614887e3935bc`
- CORE status at gate start: `CORE v0.27 Hierarchical Repeated-Trial Execution Contract Canonicalization Gate 0.1 / READY`
- MASTER project status: v2.0
- scope authority: `research/core/v0_27_hierarchical_repeated_trial_scope_freeze_0_1.md`, RB-013, blob `287b8942a17bb363e888bee7fe367b2066e3051e`
- upstream C1 authority: `research/core/consolidated_c1_theory_freeze_0_1.md`, RB-012
- legacy audit authority: `research/core/legacy_verification_sweep_freeze_0_1.md`, RB-011
- frozen legacy recovery input: `287eae8a86560b78ed94f30a2786243714c33ac0`, provenance/C2-candidate input only.

RB-013 is the scientific scope authority. This contract fixes every numerical design quantity used by the first v0.27 execution. No v0.27 scientific dataset, simulation output, stochastic realization, inference result, parameter scan, design optimization, rank result, condition number, recovery error, uncertainty value, or effect size was generated in this gate.

Legacy v0.21–v0.26 optimized pulses, sensors, subsets, gains, noise levels, preparation amplitudes and uncertainty values are not premises and did not determine the choices below.

Epistemic status of all new numerical choices: **PROJECT ASSUMPTION / PREREGISTERED DESIGN**, not source-derived and not a novelty claim.

---

## 2. Complete physical numerical specification

### 2.1 State and edge convention

Use the frozen deterministic Lighthouse baseline with smooth response and alpha synapse. Matrix entry `w_ij` is the weight from source neuron `j` to target neuron `i`.

For numerical scheduling it is convenient to use the exact aggregated postsynaptic alpha state

`dot(q_i) = -alpha q_i`,

`dot(psi_i) = -alpha psi_i + q_i`,

between delayed arrivals. An arrival on edge `j -> i` at time `T_j^m + tau_ij` applies

`q_i^+ = q_i^- + w_ij alpha^2`, `psi_i^+ = psi_i^-`.

This is the delayed state-space realization of the RB-004 alpha convolution. There is no direct synaptic jump at firing because the graph below has no zero-delay self-edge.

The physical lifted phase obeys `dot(theta_i)=S(psi_i)`. A wrapped implementation may subtract `2*pi` on firing only as a coordinate operation; the physical first-hit semantics remain RB-004.

### 2.2 Graph family

Use `N=3` and exactly the directed cycle

`1 -> 2 -> 3 -> 1`.

No other edge is present. The complete affine weight family is

```text
W^(0) = [[0.0, 0.0, 0.8],
         [0.7, 0.0, 0.0],
         [0.0, 0.6, 0.0]]

B     = [[0.0, 0.0, 0.0],
         [1.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]

W(p) = W^(0) + p B.
```

Thus `p` changes only edge `1 -> 2`.

The complete delay family is

```text
Tau^(0) = [[0.0, 0.0, 0.0],
           [0.5, 0.0, 0.0],
           [0.0, 0.8, 0.0]]

C       = [[0.0, 0.0, 1.0],
           [0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0]]

Tau(tau_3) = Tau^(0) + tau_3 C.
```

Thus `tau_3` is the delay on edge `3 -> 1`; delays on absent edges are ignored.

A-priori rationale: the directed 3-cycle is the smallest strongly connected graph with three distinct edge positions. Fixed unequal positive weights/delays break permutation symmetry without adding extra edges. `p` and `tau_3` act on different edges, avoiding a design in which both scientific coordinates are merely two parameterizations of the same edge. This geometry was fixed without evaluating v0.27 identifiability.

### 2.3 Response and alpha constants

Freeze

`alpha = 1.0`, `r = 1.0`, `h = -1.0`,

with

`S(x)=0` for `x<=-1`, and `S(x)=exp[-1/(x+1)^2]` for `x>-1`.

No external drive, process noise, plasticity or adaptive delay is present.

Rationale: `alpha=1` defines the numerical time unit; `r=1` defines the response scale; `h=-1` gives `S(0)=exp(-1)>0`, so the passive system has an autonomous clock even at zero synaptic preparation. These are simple nondimensional constants fixed before output.

### 2.4 Nominal preparation and gauge

Let

`v1=(2,-1,-1)^T/sqrt(6)`, `v2=(0,1,-1)^T/sqrt(2)`, `V=[v1 v2]`.

Freeze

`bar(phi)_0 = (pi/3, pi, 5*pi/3)^T`,

`bar(psi)_0 = (0,0,0)^T`,

`bar(q)_0 = (0,0,0)^T`.

Trial `r` starts from

`phi_0r = bar(phi)_0 + V eta_r`,

`psi_0r = V xi_psi,r`,

`q_0r = V xi_q,r`.

The perturbations remain exactly in `1^perp`; hence the global phase mean is fixed at `pi`. The first observed ordinal for each neuron is the first physical firing strictly after `t=0`, so the implementation uses the appropriate lifted spike counter even if an extremely rare Gaussian preparation crosses a wrapped-coordinate seam. Wrapped phase is representation only.

The initial delayed-arrival queue is empty; there is no prespike history before `t=0`. This is a fixed initial-value experiment, not a stationary-history experiment.

The equally staggered nominal phases are a structural anti-collision choice, not an optimized observation design.

### 2.5 Truth and parameter box

Freeze

`p* = 0.05`, `tau_3* = 0.90`.

Freeze the compact shared domain

`Theta = [-0.20,0.20] x [0.60,1.60]`.

Across this box, the varied edge weight `w_21=0.7+p` remains positive in `[0.5,0.9]`, and every active delay remains positive.

No truth/domain point may be moved after any v0.27 output.

---

## 3. Complete hierarchical numerical specification

### 3.1 Random-effects law

The RB-013 law is used without extension:

`z_r=(eta_1,eta_2,xi_psi1,xi_psi2,xi_q1,xi_q2)`

and

`z_r | lambda ~ iid N(0,Sigma_z(lambda))`,

`Sigma_z = diag(sigma_phi^2 I_2, sigma_psi^2 I_2, sigma_q^2 I_2)`,

`sigma_a=exp(lambda_a)`.

No unknown mean, anisotropy, cross-correlation, mixture or non-Gaussian tail is allowed.

### 3.2 Hyperparameter truth and box

Freeze

`sigma_phi* = sigma_psi* = sigma_q* = 0.05`,

so

`lambda_phi* = lambda_psi* = lambda_q* = log(0.05)`.

For each scale freeze

`0.01 <= sigma_a <= 0.20`,

equivalently

`log(0.01) <= lambda_a <= log(0.20)`.

Thus

`Lambda = [log(0.01),log(0.20)]^3`.

Rationale: `0.05` is a small but nonzero five-percent perturbation on the nondimensional synaptic/response scale and a small angular perturbation in the phase block; the broad 20-fold SD box tests estimation away from a fixed point without importing any legacy v0.26 preparation amplitude.

### 3.3 Trial count

Freeze

`R = 16` independent trials per stochastic dataset.

Sixteen is the first power-of-two repeated-trial design comfortably exceeding the five population parameters and is fixed without power/identifiability search.

---

## 4. Observation and stochastic design

### 4.1 Horizon and slots

Freeze

`H = 4` firing ordinals per neuron after `t=0`,

so each trial has

`K = 3H = 12` labelled candidate timestamps.

Slot order is cycle-major:

`(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),...,(1,4),(2,4),(3,4)`,

where `(i,h)` means neuron `i`, its `h`-th firing strictly after `t=0`.

### 4.2 Timing noise and missingness

Freeze known timing-noise SD

`sigma_t = 0.02` time units.

Freeze MCAR missingness

`pi_miss = 0.20` independently for every labelled slot.

The physical spike always remains in the latent trajectory. Missingness removes only its observed timestamp.

Rationale: `sigma_t=0.02` is two percent of the alpha time constant `alpha^{-1}=1`; `pi_miss=0.20` introduces a nontrivial but single, simple missing-data mechanism. Neither was selected from legacy performance numbers.

### 4.3 Stochastic replicate count and immutable RNG

Freeze exactly

`D = 32` stochastic dataset replicates, indexed `d=0,...,31`.

Use NumPy `PCG64DXSM` in float64-compatible host generation. Each replicate has three independent streams with integer seeds

`seed_z(d)     = 2701000 + 3d`,

`seed_noise(d) = 2701001 + 3d`,

`seed_mask(d)  = 2701002 + 3d`.

For each replicate:

1. draw all `R x 6` standard-normal preparation coordinates from `seed_z(d)` and multiply blockwise by the three frozen SDs;
2. physically generate all `R x 12` latent labelled spike times at the frozen truth;
3. draw all `R x 12` iid `N(0,sigma_t^2)` timing errors from `seed_noise(d)`;
4. draw all `R x 12` iid masks by `U>=pi_miss` from `seed_mask(d)`;
5. retain observed timestamps only where the mask is one.

A failed/awkward realization is never regenerated and no seed is replaced.

No additional noiseless scientific reference dataset is included. Deterministic checks belong only to the C2 validation suite in Section 10 and may not be used to select scientific design constants.

### 4.4 Minimal-data rule

For dataset `d`, define a trial as `mask-rich` if it has at least six observed timestamps. Define the dataset as `INSUFFICIENT_MASK` if either

1. fewer than eight of the sixteen trials are mask-rich, or
2. across all trials any neuron contributes fewer than sixteen observed timestamps in total.

All observed rows of all trials are otherwise retained, including rows from trials with fewer than six observations. An `INSUFFICIENT_MASK` dataset is counted as a missing-data failure and is not regenerated or fitted.

### 4.5 Physical simulation limits

Freeze per-trial wall-clock model horizon

`T_max = 120.0`

and maximum processed physical events

`E_max = 5000`.

Failure to obtain four spikes from every neuron before either limit is `PHYSICAL_TIMEOUT`; it is a recorded dataset/trial failure, never a trigger to extend the horizon.

---

## 5. Primary Laplace-marginal inference algorithm

### 5.1 Objective

For observed-row selector `M_r`, use exactly the RB-013 trial objective

`Phi_r(z;theta_s,lambda) = ||M_r(y_r-F_H(theta_s,z))||^2/(2 sigma_t^2) + 0.5 z^T Sigma_z^{-1} z + 0.5 log det Sigma_z`.

The trial mode is the minimizer from the fixed algorithm below. At a valid mode, let

`H_r = d^2 Phi_r / dz^2`.

Use exactly

`L_Lap(vartheta) = sum_r [Phi_r(z_hat_r;vartheta) + 0.5 log det H_r]`

up to constants independent of `vartheta`.

The five population unknowns are

`vartheta=(p,tau_3,lambda_phi,lambda_psi,lambda_q)`.

### 5.2 Physical-evaluation rule

Every evaluation of `F_H` at a new `(theta_s,z)` begins with a physical event rerecord. Fixed-chart automatic differentiation is applied only after the event itinerary at that exact point has been recorded and declared derivative-valid. A token from a previous parameter point is never silently reused across a changed itinerary.

This intentionally favors correctness over speed in the first v0.27 execution.

### 5.3 Trial-mode optimizer

For every trial and every outer objective evaluation:

- initialize exactly at `z=0`;
- no warm start from a previous outer point;
- no multistart;
- minimize `Phi_r` by deterministic unconstrained BFGS with exact float64 fixed-chart JAX gradient;
- `gtol = 1e-8` on the infinity norm of the gradient;
- maximum `200` BFGS iterations;
- maximum `500` objective/gradient evaluations;
- standard strong-Wolfe line search with at most `20` line-search trials per iteration;
- no stochastic perturbation, ridge, trust-region rescue, or prior alteration.

A candidate step that is physically invalid or derivative-chart invalid has objective `+infinity` for line-search purposes and is rejected. If the fixed budget is exhausted without convergence, the trial is `INNER_MODE_FAIL`.

At the final mode, rerecord physically and compute the full exact fixed-chart Hessian of `Phi_r` by JAX second derivatives.

### 5.4 Inner Hessian and log determinant

Let `S_z=diag(sigma_phi,sigma_phi,sigma_psi,sigma_psi,sigma_q,sigma_q)` and define scaled Hessian

`Htilde_r = S_z H_r S_z`.

A mode is Laplace-valid only if:

1. the physical/event chart is derivative-valid;
2. a no-jitter Cholesky factorization of `H_r` succeeds;
3. all eigenvalues of symmetrized `Htilde_r` are positive; and
4. `lambda_min(Htilde_r) > max(1e-12,1e-10 lambda_max(Htilde_r))`.

The log determinant is computed only as

`log det H_r = 2 sum_i log L_ii`

from the no-jitter Cholesky factor `L`.

No diagonal jitter, eigenvalue clipping or pseudodeterminant is permitted. Failure is `INNER_HESSIAN_FAIL`.

### 5.5 Outer parameter scaling and bounds

For each population coordinate with lower/upper bounds `(l_j,u_j)`, optimize the scaled coordinate

`x_j = 2(vartheta_j-l_j)/(u_j-l_j)-1`,

so `x in [-1,1]^5`.

Bounds are hard and inclusive; no transform changes the statistical objective.

### 5.6 Outer optimizer and fixed starts

Use deterministic bounded Powell directional search on `x in [-1,1]^5` with

- `xtol = 1e-5`;
- `ftol = 1e-8`;
- maximum `300` iterations per start;
- maximum `2500` full outer objective evaluations per start.

Use exactly three starts, expressed in physical coordinates:

- S0: `(p,tau_3,sigma_phi,sigma_psi,sigma_q)=(0.00,1.10,sqrt(0.002),sqrt(0.002),sqrt(0.002))`;
- S1: `(-0.10,0.85,0.03,0.06,0.09)`;
- S2: `(0.10,1.35,0.09,0.06,0.03)`.

The truth vector is not one of the starts.

Among starts that terminate successfully within budget, choose the smallest `L_Lap`. If two final objectives differ by at most

`1e-10 * max(1,abs(L_best))`,

choose the lexicographically smallest scaled five-vector. If no start succeeds, classify the dataset `OUTER_OPT_FAIL`.

No fourth start or alternative optimizer may be added after output inspection.

### 5.7 Failure handling

- invalid inner candidate: rejected by line search;
- invalid complete outer point: `L_Lap=+infinity`;
- all three outer starts fail: `OUTER_OPT_FAIL`;
- a scientifically weak, badly conditioned, biased or non-identifiable successful fit is retained as a scientific result and is not rerun with changed settings.

---

## 6. Event-chart and physical validity contract

### 6.1 Event scheduler

Between arrivals use the exact alpha flow

`q(t+d)=exp(-d) q(t)`,

`psi(t+d)=exp(-d)[psi(t)+d q(t)]`.

Phase gain over a segment is integrated by adaptive Gauss-Kronrod quadrature with

`epsabs=1e-12`, `epsrel=1e-12`, subdivision limit `200`.

First-hit roots use a bracketed Brent method with

`xtol=1e-12`, `rtol=1e-14`, maximum `100` iterations.

Because `S>=0`, the integrated phase is nondecreasing; the first bracketed section crossing is the physical firing event.

### 6.2 Queue semantics

At firing of neuron `j` at `T`, enqueue exactly one arrival for its unique outgoing edge at `T+tau_ij`. At arrival, apply `q_i += w_ij alpha^2`. Queue entries are ordered by physical arrival time. No arrival is deleted because its timestamp is missing from observations.

### 6.3 Numerical validity thresholds

Freeze:

- phase-root residual tolerance: `1e-10` radians;
- physical transversality floor: `nu=S(psi_event) > 1e-8`;
- derivative transversality floor: `nu >= 1e-6`;
- physical collision tolerance: any two competing firing/arrival event times within `1e-8` is `EVENT_COLLISION`;
- derivative-chart margin: minimum gap from every processed event to its nearest competitor must be at least `1e-6`.

A physically regular trajectory with chart margin below `1e-6` may be recorded, but its fixed-chart derivative is invalid and cannot be used by the primary inference path.

### 6.4 Rerecording and collision rule

If a parameter/mode candidate has a different event itinerary from the previous candidate, physically rerecord and compute all derivatives on the new itinerary. A changed itinerary is not itself failure.

A simultaneous/colliding event within `1e-8` is not ordered by neuron index or queue insertion order to manufacture differentiability. It is labeled `EVENT_COLLISION / DERIVATIVE_INVALID`.

No finite-difference or AD derivative is accepted across an itinerary mismatch.

### 6.5 Dataset-level validity

A stochastic dataset is `CHART_INVALID` if any truth-generated trial required for the dataset has a collision, nontransverse firing, root/queue failure, timeout, or derivative chart margin below `1e-6` at the truth.

Such a dataset is retained in the replicate ledger and counted in failure fractions; it is not replaced.

---

## 7. Identifiability and regularity diagnostics

### 7.1 Dimensionless scaling

For rank/conditioning only, scale population coordinates by their half-box widths:

`D_v = diag(0.20,0.50,0.5*(log(0.20)-log(0.01)),0.5*(log(0.20)-log(0.01)),0.5*(log(0.20)-log(0.01)))`.

This prevents units alone from determining a condition number.

### 7.2 Conservative free-nuisance information

For each truth trial and observed mask, compute physical fixed-chart Jacobians at the truth:

`J_s,r = D_(p,tau_3) M_r F_H`, `N_r=D_z M_r F_H`.

Compute `P_Nr=N_r N_r^+` using SVD with singular values counted nonzero when

`s_i > max(1e-12,1e-10 s_max)`.

Then

`R_r=(I-P_Nr)J_s,r`.

Scale shared columns by `diag(0.20,0.50)` and form

`I_free = sigma_t^{-2} sum_r R_r^T R_r`.

The rank-two audit passes for a dataset iff symmetrized `I_free` satisfies

`lambda_min > max(1e-10,1e-8 lambda_max)`

and

`kappa=lambda_max/lambda_min <= 1e8`.

No root or singular value may be dropped merely because it is inconvenient.

### 7.3 Five-dimensional hierarchical Hessian

For every successful fitted dataset, compute the observed Hessian of the fully reoptimized Laplace objective in scaled coordinates at `hat(vartheta)` by symmetric central finite differences.

Use fixed scaled step

`h_H = 1e-3`.

Use the standard centered diagonal stencil and centered four-corner mixed derivative stencil. Repeat the complete Hessian once at `h_H/2`. The `h_H/2` Hessian is the reported Hessian if

`||H_(h/2)-H_h||_F / max(1,||H_(h/2)||_F) <= 0.05`.

Otherwise classify `OUTER_HESSIAN_FAIL`; do not tune the step.

If any required central stencil point falls outside `[-1,1]^5`, classify `OUTER_HESSIAN_BOUNDARY_FAIL`; do not replace it with a one-sided stencil.

The five-dimensional regularity audit passes iff the accepted symmetrized scaled Hessian is positive definite,

`lambda_min > max(1e-10,1e-8 lambda_max)`,

and `kappa<=1e8`.

### 7.4 Shared/profile Schur block

Partition the accepted scaled five-Hessian as

`H5=[[A,B],[B^T,C]]`, with `A` 2x2 shared and `C` 3x3 scale block.

If `C` passes the same positive-rank rule, form

`H_shared = A - B C^{-1} B^T`.

The shared-profile audit passes iff `H_shared` is positive definite, satisfies the same relative eigenvalue floor, and has condition number `<=1e8`.

No pseudoinverse rescue is allowed for a singular `C`; that dataset fails the hierarchical separation audit.

---

## 8. Uncertainty construction

For every successful interior fit with an accepted positive-definite five-Hessian, use

`Cov_x = H5^{-1}`

in scaled coordinates and transform by `D_v` to the physical/log-scale coordinates.

Construct two-sided 95% Wald intervals with fixed normal quantile

`z_0.975 = 1.959963984540054`.

Intervals are not clipped to parameter bounds.

Primary coverage is evaluated for

`p`, `tau_3`, `lambda_phi`, `lambda_psi`, `lambda_q`.

If the estimate is too close to a bound for the central Hessian stencil, the interval is invalid and contributes to the uncertainty-failure fraction; no one-sided or profile-likelihood substitute is introduced.

---

## 9. Finite scientific metrics and decision rule

All error metrics use only the 32 immutable stochastic replicates. Failed/invalid replicates remain in the failure denominators and are never regenerated.

### 9.1 Normalized errors

For `p` and `tau_3`, normalize by full box widths `0.40` and `1.00`.

For each `lambda_a`, normalize by full log-box width `log(20)`.

For each coordinate define:

- absolute normalized signed bias `B_j = |mean(hat(v_j)-v_j*)| / width_j`;
- median normalized absolute error `M_j`;
- 90th-percentile normalized absolute error `Q90_j`.

Shared-parameter thresholds:

- `B_p,B_tau <= 0.05`;
- `M_p,M_tau <= 0.10`;
- `Q90_p,Q90_tau <= 0.25`.

Preparation log-scale thresholds, each of the three coordinates:

- `B_lambda <= 0.08`;
- `M_lambda <= 0.15`;
- `Q90_lambda <= 0.35`.

These are fixed practical recovery criteria in normalized box units; they are not derived from legacy effect sizes.

### 9.2 Identifiability fractions

Among datasets eligible for the corresponding calculation:

- conservative `I_free` rank-two/regular fraction must be at least `0.90`;
- hierarchical five-Hessian regular fraction among successful fits must be at least `0.90`;
- shared Schur/profile regular fraction among five-Hessian-valid fits must be at least `0.90`.

### 9.3 Coverage

At least `26/32` datasets must produce valid five-parameter uncertainty intervals.

For each of the five coordinates, empirical 95% Wald coverage among valid intervals must be at least `0.80`.

No coverage target is redefined after observing the realized count.

### 9.4 Failure fractions

Each is computed over all 32 immutable replicate IDs unless a narrower denominator is explicitly stated:

- `INSUFFICIENT_MASK` fraction `<=0.10`;
- truth physical/chart-invalid fraction `<=0.10`;
- `INNER_MODE_FAIL` or `INNER_HESSIAN_FAIL` dataset fraction `<=0.10`;
- `OUTER_OPT_FAIL` fraction `<=0.10`;
- outer-Hessian/uncertainty-invalid fraction `<=0.20`;
- complete usable-fit fraction must be at least `0.80`.

A dataset can carry more than one diagnostic flag; each fraction is reported separately.

### 9.5 Overall execution decision

The later execution gate must use exactly this hierarchy:

1. **IMPLEMENTATION FAIL / BLOCKED** — any C2 test in Section 10 fails. In this case no stochastic scientific dataset may be generated and there is no scientific v0.27 effect result.
2. **SCIENTIFIC FAIL** — C2 passes, but any identifiability fraction, failure-fraction limit, or minimum usable-fit fraction in Sections 9.2/9.4 fails.
3. **SCIENTIFIC CONDITIONAL** — all hard structural/failure criteria pass, but at least one recovery-error or coverage criterion in Sections 9.1/9.3 fails.
4. **SCIENTIFIC PASS** — C2 passes and every criterion in Sections 9.1–9.4 passes.

A weak/null/fail result is final for this preregistered branch. No truth, R, H, noise, missingness, solver, start, tolerance or metric may be changed to rescue it.

---

## 10. C2 implementation-validation sub-contract

The first v0.27 execution must run C2-27-01 through C2-27-08 in order **before creating any RNG object for the 32 scientific datasets**. Every check must pass. The execution record must retain all measured errors and negative-control outcomes.

No legacy v0.18–v0.20 code is required or imported by this first path. The first execution uses a fresh canonical implementation from RB-004/RB-013. Therefore no legacy implementation blob is promoted by code reuse. Any later decision to substitute legacy code requires a separate governed implementation-provenance change before scientific execution.

All C2 arithmetic is float64 on a deterministic CPU backend.

### C2-27-01 — fixed-delay scheduler / isolated clock

Input:

- `N=3`, `W=0`, no queued arrivals;
- `alpha=1,r=1,h=-1`;
- `phi_0=(pi/3,pi,5pi/3)`, `psi_0=q_0=0`;
- record two firings per neuron.

Independent reference: `S(0)=exp(-1)` and

`t_i,1 = exp(1)*(2*pi-phi_i(0))`,

`t_i,2 = t_i,1 + 2*pi*exp(1)`.

Observable: all six labels/times and section residuals.

PASS: correct physical ordering/labels, maximum absolute time error `<=1e-10`, maximum section residual `<=1e-10`.

Negative control: swap two labels in the reference; comparator must fail.

### C2-27-02 — delayed alpha arrival identity

Input: one emission at `t=0` on one edge of weight `w=0.7`, delay `tau=0.5`, `alpha=1`, target initial `psi=q=0`.

Independent reference:

before `0.5`, `psi=q=0`;

after arrival, with `s=t-0.5>=0`,

`q(t)=0.7 exp(-s)`,

`psi(t)=0.7 s exp(-s)`.

Evaluate at `t=(0.49,0.50,0.60,1.00,2.00)`, interpreting `q(0.50)` after the jump.

PASS: arrival-time error `<=1e-12`, no premature contribution, maximum state error `<=1e-12`.

Negative control: evaluate a deliberately premature jump at `0.49`; comparator must fail.

### C2-27-03 — actual-graph fixed-chart derivative audit

Input: the frozen v0.27 graph at `(p,tau_3)=(0.05,0.90)`, `z=0`, nominal state, full observation, `H=2`, no timing noise or missingness.

Record the physical itinerary once at the base point. Compute JAX fixed-chart derivative of the six labelled times with respect to

`(p,tau_3,eta1,eta2,xi_psi1,xi_psi2,xi_q1,xi_q2)`.

Independent reference: physically rerecorded five-point centered finite differences

`[-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)]/(12h)`

with fixed steps

- `h_p=1e-5`;
- `h_tau=1e-5`;
- every `eta/xi` step `1e-6`.

Every perturbed rerecord must have the same itinerary as the base case. No step reduction is allowed if it does not.

PASS:

`||J_AD-J_FD||_F / max(1,||J_FD||_F) <= 1e-6`

and all base/perturbed charts meet the derivative validity rules.

Negative control: compare one intentionally sign-flipped FD column; comparator must fail.

### C2-27-04 — chart sentinel and physical rerecording

Use two disconnected neurons with `psi=q=0`, response constants as above, and

`phi_1=pi+delta`, `phi_2=pi-delta`.

Cases: `delta=+0.01`, `-0.01`, `0`.

Independent identity: `+0.01` and `-0.01` have opposite first-firing labels; `delta=0` is exactly simultaneous.

PASS: physical rerecord produces opposite valid itineraries for the nonzero cases; `delta=0` is classified `EVENT_COLLISION / DERIVATIVE_INVALID`; a stale token from `+0.01` applied to `-0.01` is rejected by the sentinel.

### C2-27-05 — hierarchical Gaussian penalty

Input:

`z=(0.01,-0.02,0.03,-0.04,0.05,-0.06)`,

`(sigma_phi,sigma_psi,sigma_q)=(0.05,0.08,0.12)`.

Independent identities:

`P=0.5 z^T Sigma^-1 z + 0.5 log det Sigma`,

`grad_z P = Sigma^-1 z`,

for each two-vector block `z_a`,

`dP/dlambda_a = 2 - ||z_a||^2/sigma_a^2`.

PASS: value and all specified gradient components agree to absolute `1e-12`.

Negative control: omit `0.5 log det Sigma`; comparator must fail.

### C2-27-06 — trial-mode Hessian and log determinant

Use a purely linear six-random-effect toy, independent of the Lighthouse scheduler:

```text
A = [[1,0,0,0,0,0],
     [0,1,1,0,0,0],
     [0,0,1,1,0,0],
     [0,0,0,1,1,1]]
```

`y-b=(0.20,-0.10,0.30,0.05)`, `sigma_t=0.20`,

`Sigma=diag(0.3^2 I2,0.4^2 I2,0.5^2 I2)`.

Independent exact mode and Hessian:

`H=A^T A/sigma_t^2 + Sigma^-1`,

`z_hat=H^-1 A^T(y-b)/sigma_t^2`.

PASS: BFGS mode absolute max error `<=1e-9`; Hessian relative Frobenius error `<=1e-10`; Cholesky logdet versus direct `slogdet` absolute error `<=1e-12`.

Negative control: replace one Hessian diagonal by zero; PD/logdet validator must fail.

### C2-27-07 — mask row selection and insufficient-mask rule

Base vector has rows `0,...,11` and mask

`(1,0,1,1,0,0,1,0,1,0,1,1)`.

Expected selected indices are exactly

`(0,2,3,6,8,10,11)`.

Apply the selector to a 12-row vector and a 12-row Jacobian; equality is exact.

Negative-control dataset mask: construct 16 trials where only seven trials have six observed rows and all remaining trials have five. The dataset-level minimal-data validator must return `INSUFFICIENT_MASK` because fewer than eight trials are mask-rich.

PASS: exact row identity plus required negative-control classification.

### C2-27-08 — outer Laplace assembly versus exact linear-Gaussian marginal

Use two linear-Gaussian trials with shared `theta=(0.10,-0.20)`, `sigma_t=0.20`, random-effect scales `(0.30,0.40,0.50)`.

```text
A1 = [[ 1.0, 0.0],
      [ 0.0, 1.0],
      [ 1.0, 1.0],
      [ 1.0,-1.0]]

B1 = [[1,0,0,0,0,0],
      [0,1,0,0,0,0],
      [0,0,1,1,0,0],
      [0,0,0,0,1,1]]

A2 = [[ 0.5, 0.0],
      [ 0.0, 0.5],
      [ 1.0,-0.5],
      [-0.5, 1.0]]

B2 = [[0,1,0,0,0,0],
      [1,0,0,0,0,0],
      [0,0,1,-1,0,0],
      [0,0,0,0,1,-1]]
```

`y1=(0.20,-0.10,0.40,0.05)`, mask1=`(1,1,0,1)`;

`y2=(-0.20,0.30,0.10,-0.05)`, mask2=`(1,0,1,1)`.

For each mask the exact marginal is

`y_M ~ N(A_M theta, sigma_t^2 I + B_M Sigma B_M^T)`.

Compare the parameter-dependent change in assembled Laplace objective between the stated point and fixed comparison point

`theta0=(0,0)`, scales `(0.25,0.35,0.45)`

against the exact Gaussian marginal NLL change, so all irrelevant constants cancel.

PASS: absolute difference of the two objective changes `<=1e-10`.

Negative control: intentionally use mask2 for trial1 in one assembly; comparator must fail by more than `1e-6`.

### C2 suite rule

`C2 PASS` requires all eight positive checks and every listed negative control to behave as specified. No tolerance may be relaxed after any C2 output. Any C2 failure stops the later execution before scientific RNG/dataset generation and returns to MASTER.

---

## 11. Anti-cherry-picking freeze table

| Quantity | Frozen value / rule |
|---|---|
| topology | N=3 directed cycle `1->2->3->1` |
| `W^(0),B` | exact matrices in Sec. 2.2 |
| `Tau^(0),C` | exact matrices in Sec. 2.2 |
| response | `r=1,h=-1` |
| alpha | `alpha=1` |
| external/process noise | none |
| nominal phase | `(pi/3,pi,5pi/3)` |
| nominal psi/q | zero vectors |
| gauge | random phase block in `1^perp`; global mean fixed |
| history | empty pre-t=0 arrival queue |
| truth | `p*=0.05,tau_3*=0.90` |
| Theta | `[-0.20,0.20]x[0.60,1.60]` |
| random-effects law | zero-mean Gaussian, three isotropic 2D blocks |
| scale truth | all three SDs `0.05` |
| scale box | each SD `[0.01,0.20]` |
| R | 16 |
| H / K | 4 / 12 |
| timing noise | known `sigma_t=0.02` |
| missingness | known iid MCAR `pi_miss=0.20` |
| datasets | 32 |
| seeds | exact PCG64DXSM formulas in Sec. 4.3 |
| insufficient-mask rule | Sec. 4.4 |
| model limits | `T_max=120`, `E_max=5000` |
| phase quadrature | GK adaptive `1e-12/1e-12`, limit 200 |
| firing root | Brent `xtol=1e-12,rtol=1e-14,maxiter=100` |
| event validity | root/transversality/collision/chart floors in Sec. 6 |
| rerecording | physical rerecord at every new point; AD only on current chart |
| inner solver | z=0 single-start BFGS, Sec. 5.3 |
| inner Hessian/logdet | exact AD Hessian, no-jitter Cholesky, Sec. 5.4 |
| outer scaling | five box-scaled coordinates in `[-1,1]` |
| outer solver | bounded Powell, exact 3 starts and budgets in Sec. 5.6 |
| tie break | objective then lexicographic scaled vector |
| rank tolerance | relative `1e-8` plus absolute floors, Sec. 7 |
| condition limit | `1e8` |
| outer Hessian | central finite differences `h=1e-3`, fixed `h/2` audit |
| uncertainty | inverse accepted 5-Hessian; 95% untruncated Wald |
| recovery metrics | normalized bias/median/Q90 thresholds in Sec. 9.1 |
| identifiability | 0.90 fraction thresholds in Sec. 9.2 |
| coverage | >=26 valid intervals; per-coordinate coverage >=0.80 |
| failure limits | Sec. 9.4 |
| overall decision | deterministic hierarchy in Sec. 9.5 |
| C2 validation | C2-27-01...08 all mandatory before RNG |
| implementation lineage | fresh canonical implementation; no legacy C2 code imported |

None of these quantities may change after any v0.27/C2 output is inspected except through a new MASTER-authorized branch that preserves the failed/weak/null original result.

Software/package versions and CPU model are execution-environment metadata, not scientific design parameters. The later execution record must capture the exact Python/NumPy/SciPy/JAX/jaxlib versions and environment hash before C2 starts. If that environment changes after C2, the entire C2 suite must rerun from the beginning before science; scientific constants remain unchanged.

---

## 12. Deferred branches

The following remain explicitly outside the first execution:

- active pulses and direct subthreshold sensing;
- pulse timing/amplitude/direction calibration;
- unknown preparation/population mean;
- covariance anisotropy or cross-correlation;
- non-Gaussian preparation laws;
- unknown topology or additional network parameters;
- unlabelled spikes or sequence matching;
- non-MCAR missingness and unknown missingness probability;
- unknown timing-noise scale or observation clock;
- large-network extension;
- EM, VI, MCMC or alternative primary inference objectives;
- legacy optimized C3 sensors/pulses/subsets and legacy 250x/87x/788x/557x effects;
- v0.6–v0.15 C3 bifurcation/global-object confirmation;
- applications, independent novelty positioning and manuscript claims.

Failure of the first target does not authorize any of these automatically.

---

## 13. Gate decision

# PASS

The first v0.27 execution contract is now completely fixed before output. It contains a complete physical model, truth/domain, hierarchical truth/domain, stochastic design and immutable seeds, one primary inference algorithm, event/chart rules, rank/conditioning rules, uncertainty construction, finite scientific metrics, a deterministic overall decision rule, and a finite C2 implementation-validation suite that must pass before scientific dataset generation.

PASS here means only that MASTER can decide whether to freeze this contract. It does **not** mean that the implementation works, the random-effects model is identifiable, passive trials are sufficient, the inference converges, the uncertainty is calibrated, or the scientific target will pass.

No v0.27 scientific execution occurred.

---

## 14. Proposed execution-contract freeze

If MASTER accepts this gate, the proposed

`CORE v0.27 Hierarchical Repeated-Trial Execution Contract Freeze 0.1`

should freeze, as one indivisible pre-output package:

1. RB-013 scientific scope inheritance;
2. Sections 2–4 physical/hierarchical/stochastic numerical design;
3. Section 5 exact inference algorithm, starts, budgets and failure handling;
4. Section 6 event/chart/physical-validity rules;
5. Sections 7–8 identifiability and uncertainty definitions;
6. Section 9 all finite scientific thresholds and overall decision hierarchy;
7. Section 10 C2-27-01 through C2-27-08 including negative controls and mandatory stop-before-science rule;
8. Section 11 anti-cherry-picking table;
9. Section 12 exclusions/deferred branches.

The freeze must state explicitly that at freeze time every C2 check and all 32 stochastic datasets remain **UNEVALUATED**.

CORE does not self-authorize that freeze and does not self-authorize execution.

---

## 15. STOP

No dataset generation, C2 execution, simulation, inference, optimization, rank computation or effect inspection follows this document in the present gate.

STOP — RETURN TO MASTER; NO V0.27 SCIENTIFIC EXECUTION
