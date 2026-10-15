# CORE v0.27c Whitened Trust-Region Laplace Execution Contract Canonicalization Gate 0.1

Date: 2026-10-15
Status: PASS — COMPLETE PRE-EXECUTION V0.27C CONTRACT FIXED; NO 2711XXX RNG OR CONFIRMATORY EXECUTION

## 1. Authority, Git identity, and freeze boundary

This gate executes the MASTER-authorized prompt

`research/master/prompts/core_v0_27c_whitened_trust_region_laplace_execution_contract_canonicalization_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `262defa1599f49b9b760f3674b29bd7dc921bce4`
- CORE STATUS blob: `225ceba01aa188ae1a8152b917cf3cc5fa01b0b0`
- MASTER prompt blob: `15869ded5b8a53eff16a207754cb89d40d15d27f`
- PROJECT_GOVERNANCE blob: `1c9680db72f6e562b3efbeda2cdeca45c9d5f38a`
- command protocol blob: `f362f8d3628b29cf9482bc40a448098877f5dd0c`
- MASTER STATUS blob: `cc53b0b4794d63ec476b1ed3faa16332438c08ae`
- MASTER project-status blob: `752ac60c0ee7a3567a2b520c1689f1cd92addd89`
- MASTER decision-log blob: `184821b8e18f51d215f9f41ad177ab78ea97412c`
- RB-013 v0.27 scope freeze blob: `287b8942a17bb363e888bee7fe367b2066e3051e`
- RB-014 v0.27 execution-contract freeze blob: `dec52d17974ee49c792e6553c68aed72d5ae5813`
- RB-015 v0.27 result freeze blob: `92625f130bdcf510ce95493c69eaab3e00db2454`
- RB-016 v0.27b follow-up scope freeze blob: `45da28c7857b992ab4bee02d92c0abc365dc12cd`
- governed v0.27b source artifact blob: `aca57e3771b38fc3db0252db6b7a16178c094752`
- RB-019 NUM-ENG engineering freeze blob: `68c674e50772620960b5e52092b9f6cd606d8f42`

RB-015 remains immutable:

`SCIENTIFIC FAIL — C2 PASS; CONSERVATIVE SHARED INFORMATION PASS; FROZEN LAPLACE INFERENCE HAS NO FINITE INITIAL OUTER START ON ANY OF 32 DATASETS`.

This contract does not rescue, overwrite, weaken, or relabel RB-015.

The old `2701xxx` datasets are permanently DEVELOPMENT ONLY for this route. The disjoint `2711xxx` namespace is UNGENERATED / UNEVALUATED at gate start and remains UNGENERATED / UNEVALUATED throughout this gate.

No trust-region validation case, confirmatory stochastic dataset, confirmatory trial fit, population fit, recovery metric, coverage metric, rank result, condition number, uncertainty result, or scientific effect was executed in this contract gate.

### 1.1 Contract-authoring environment metadata

The contract was written under the following environment, but no numerical validation or scientific execution was performed here:

| item | value |
|---|---|
| Python | `3.13.5` |
| NumPy | `2.3.5` |
| SciPy | `1.17.0` |
| JAX | `0.9.0.1` |
| jaxlib | `0.9.0.1` |
| backend | CPU |
| kernel | Linux `6.18.44`, x86_64, glibc 2.41 |
| CPU | AMD EPYC 9V74 80-Core Processor |
| JAX x64 at contract-writing process start | `False` |
| authoring-environment SHA-256 | `2897be55f40e8ab65c01591ce14e51397994474b496f40c9bd58e8b91f45985a` |

The later execution must explicitly enable `jax_enable_x64=True` before any TR-27C validation arithmetic and must assert a CPU backend. The authoring environment is metadata, not a scientific result.

RB-019 is acknowledged as a parallel frozen engineering baseline. This v0.27c contract does **not** silently replace the CORE physical-rerecord implementation with executable code from `engineering/numerics-v0.1`; such a provenance change would require explicit MASTER authorization. The v0.27c route remains the RB-014/RB-016 governed CORE path.

---

## 2. Immutable scientific design inherited from RB-014

Unless explicitly replaced below only for the inner numerical solver, all RB-014 scientific/model/statistical quantities remain unchanged.

### 2.1 Physical model

Use `N=3` and exactly the directed cycle

`1 -> 2 -> 3 -> 1`.

Weight family:

```text
W^(0) = [[0.0, 0.0, 0.8],
         [0.7, 0.0, 0.0],
         [0.0, 0.6, 0.0]]

B     = [[0.0, 0.0, 0.0],
         [1.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]

W(p) = W^(0) + p B.
```

Delay family:

```text
Tau^(0) = [[0.0, 0.0, 0.0],
           [0.5, 0.0, 0.0],
           [0.0, 0.8, 0.0]]

C       = [[0.0, 0.0, 1.0],
           [0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0]]

Tau(tau_3) = Tau^(0) + tau_3 C.
```

Freeze

- `alpha=1.0`,
- `r=1.0`,
- `h=-1.0`,
- no external drive,
- no process noise,
- no adaptive delay or plasticity.

The response is

`S(x)=0` for `x<=-1`, and `S(x)=exp[-1/(x+1)^2]` for `x>-1`.

### 2.2 Preparation and gauge

Let

`v1=(2,-1,-1)^T/sqrt(6)`,
`v2=(0,1,-1)^T/sqrt(2)`,
`V=[v1 v2]`.

Nominal state:

- `bar(phi)_0=(pi/3,pi,5*pi/3)^T`,
- `bar(psi)_0=(0,0,0)^T`,
- `bar(q)_0=(0,0,0)^T`.

For trial `r`,

`phi_0r=bar(phi)_0+V eta_r`,
`psi_0r=V xi_psi,r`,
`q_0r=V xi_q,r`.

The initial delayed-arrival queue is empty. The global phase mean is fixed at `pi`.

### 2.3 Population truth and boxes

Shared truth:

`p*=0.05`, `tau_3*=0.90`.

Shared box:

`Theta=[-0.20,0.20] x [0.60,1.60]`.

Random-effects law:

`z_r=(eta_1,eta_2,xi_psi1,xi_psi2,xi_q1,xi_q2)`,

`z_r|lambda ~ iid N(0,Sigma_z(lambda))`,

`Sigma_z=diag(sigma_phi^2 I_2,sigma_psi^2 I_2,sigma_q^2 I_2)`,

`sigma_a=exp(lambda_a)`.

Truth:

`sigma_phi*=sigma_psi*=sigma_q*=0.05`.

Each scale remains in

`0.01 <= sigma_a <= 0.20`,

or `log(0.01)<=lambda_a<=log(0.20)`.

Population unknown vector:

`vartheta=(p,tau_3,lambda_phi,lambda_psi,lambda_q)`.

### 2.4 Observation design

Freeze:

- `R=16` trials per dataset;
- `H=4` firing ordinals per neuron;
- `K=12` labelled candidate timestamps per trial;
- slot order cycle-major `(1,1),(2,1),(3,1),...,(1,4),(2,4),(3,4)`;
- known timing-noise SD `sigma_t=0.02`;
- iid observed MCAR missingness `pi_miss=0.20`;
- `D=32` confirmatory stochastic datasets.

The RB-014 minimal-data rule, `T_max=120.0`, `E_max=5000`, physical timeout semantics, and no-regeneration rule remain unchanged.

### 2.5 Physical/event validity

Retain RB-014 exactly:

- adaptive Gauss-Kronrod phase integration `epsabs=1e-12`, `epsrel=1e-12`, subdivision limit `200`;
- first-hit Brent solve `xtol=1e-12`, `rtol=1e-14`, maximum `100` iterations;
- phase-root residual tolerance `1e-10`;
- physical transversality `nu>1e-8`;
- derivative transversality `nu>=1e-6`;
- event-collision tolerance `1e-8`;
- derivative-chart margin at least `1e-6`;
- physical rerecording at every new parameter/state point;
- no AD or finite difference across an itinerary mismatch;
- a changed itinerary is not itself invalid if the newly rerecorded trajectory is physically regular and derivative-valid.

---

## 3. Whitened trial-mode problem

Define

`S(lambda)=diag(sigma_phi,sigma_phi,sigma_psi,sigma_psi,sigma_q,sigma_q)`

so that

`Sigma_z=S^2`

and parameterize

`z=S u`.

For observed-row selector `M_r`, define the data residual

`d_r(u) = M_r[y_r-F_H(theta_s,S u)]/sigma_t`.

The exact augmented residual is

`r_aug(u) = [d_r(u); u]`.

At fixed `(theta_s,lambda)`, the mode objective is

`f(u)=0.5 ||r_aug(u)||_2^2`.

The original RB-014 trial objective is exactly

`Phi_r(Su;theta_s,lambda)=f(u)+0.5 log det Sigma_z`

and, because each scale occurs twice,

`0.5 log det Sigma_z = 2(lambda_phi+lambda_psi+lambda_q)`.

This additive term is constant with respect to `u` and therefore does not change the trial mode.

On a current certified chart,

`J(u)=D_u r_aug(u)
     = [-(M_r D_z F_H) S/sigma_t;
         I_6]`.

Define

`g=J^T r_aug`

and the Gauss-Newton matrix

`B_GN=J^T J`.

Because the augmented Jacobian contains the exact `I_6` prior block, `B_GN` is mathematically positive definite in exact arithmetic. No ridge, damping parameter, Levenberg-Marquardt term, pseudoinverse, eigenvalue clipping, or stochastic perturbation is permitted.

The Gauss-Newton matrix is used only to construct the trust-region step. It is **not** substituted for the exact Hessian used by the Laplace approximation.

---

## 4. Exact inner trust-region algorithm

The v0.27c inner solver is a deterministic **whitened dogleg trust-region Gauss-Newton** method.

Every trial mode at every outer objective evaluation starts exactly at

`u_0=0`.

There is no warm start from another trial, outer point, Powell direction, or previous dataset, and no inner multistart.

### 4.1 Frozen trust-region constants

| quantity | frozen value |
|---|---:|
| initial radius `Delta_0` | `1.0` |
| minimum radius `Delta_min` | `1e-10` |
| maximum radius `Delta_max` | `100.0` |
| acceptance threshold `eta_accept` | `0.10` |
| shrink threshold `eta_shrink` | `0.25` |
| expansion threshold `eta_expand` | `0.75` |
| shrink factor `gamma_shrink` | `0.25` |
| invalid-proposal shrink factor `gamma_invalid` | `0.25` |
| expansion factor `gamma_expand` | `2.0` |
| boundary-active threshold | `||p|| >= 0.90 Delta` |
| stationarity tolerance | `||g||_inf <= 1e-8` |
| maximum trust-region iterations | `200` |
| maximum residual/objective evaluations | `500` |
| maximum Jacobian evaluations | `250` |
| maximum physical rerecords | `750` |
| maximum invalid proposals in one trust iteration | `20` |
| maximum invalid proposals over one trial solve | `100` |

All arithmetic is float64.

### 4.2 Current-point certification

Before evaluating `r_aug` or `J` at a current iterate:

1. map `u -> z=S u`;
2. physically rerecord the Lighthouse trajectory;
3. require physical regularity and derivative-chart validity under Section 2.5;
4. evaluate the residual and exact current-chart JAX Jacobian only on that certified tape.

A tape may be reused only for residual/Jacobian calculations at the **exact same** `(theta_s,z)` point. It may never be reused after a state/parameter change.

If the initial/current iterate itself cannot be certified, classify the trial `INNER_MODE_FAIL / CURRENT_POINT_INVALID`.

### 4.3 Deterministic dogleg step

At a certified current point:

1. if `||g||_inf <= 1e-8`, declare inner stationarity and proceed to the exact Hessian checks in Section 5;
2. compute an unpivoted Cholesky factorization of `B_GN=J^T J`;
3. solve the full Gauss-Newton step
   `p_GN=-B_GN^{-1}g`;
4. compute the Cauchy step
   `p_U=-(g^T g)/(g^T B_GN g) g`.

If the Cholesky factorization fails, or if `g^T B_GN g` is non-finite/non-positive while the stationarity criterion is not met, classify
`INNER_MODE_FAIL / TR_LINEAR_SOLVE_FAIL`.
No ridge or fallback solve is allowed.

The dogleg step `p` is then:

- if `||p_GN||_2 <= Delta`, set `p=p_GN`;
- else if `||p_U||_2 >= Delta`, set
  `p=-Delta g/||g||_2`;
- otherwise let `d=p_GN-p_U` and choose the unique `tau in (0,1)` satisfying
  `||p_U+tau d||_2=Delta`.

For the third case compute `tau` from

`a tau^2+b tau+c=0`

with

`a=d^T d`,
`b=2 p_U^T d`,
`c=p_U^T p_U-Delta^2`

and use the positive in-segment root

`tau=(-b+sqrt(b^2-4ac))/(2a)`.

No step clipping beyond this dogleg construction is allowed.

### 4.4 Predicted reduction

For every proposed dogleg step,

`pred = -(g^T p + 0.5 p^T B_GN p)`.

`pred` must be finite and strictly positive. If not, while stationarity is not met, classify

`INNER_MODE_FAIL / TR_MODEL_REDUCTION_FAIL`.

### 4.5 Physical proposal handling

For proposal `u_trial=u+p`:

1. physically rerecord at `z_trial=S u_trial`;
2. if the proposal is colliding, nontransverse, physically invalid, timed out, or derivative-chart invalid, do **not** evaluate/accept a stale-chart derivative;
3. leave the current iterate unchanged;
4. set
   `Delta <- gamma_invalid Delta = 0.25 Delta`;
5. increment the invalid-proposal counters and physical-rerecord counter;
6. recompute the dogleg step from the unchanged current `r,J,g,B_GN` at the smaller radius.

An itinerary change by itself is not invalid: if the new itinerary is physically and derivative-chart valid, it is a valid proposal and is evaluated on its newly rerecorded chart.

If

- `Delta < Delta_min`,
- more than `20` invalid proposals occur in one trust iteration,
- or more than `100` invalid proposals occur in the trial solve,

classify

`INNER_MODE_FAIL / TR_INVALID_PROPOSAL_BUDGET`.

### 4.6 Valid proposal ratio and acceptance

For a physically/chart-valid proposal evaluate

`f_trial=0.5 ||r_aug(u_trial)||^2`,

`ared=f_current-f_trial`,

`rho=ared/pred`.

Any NaN/Inf in the residual, objective, `ared`, `pred`, step, or ratio is

`INNER_MODE_FAIL / TR_NUMERIC_FAIL`.

A valid proposal is accepted iff

`ared>0` and `rho>=eta_accept=0.10`.

Radius update is deterministic:

- if `rho<0.25`, set `Delta <- max(Delta_min,0.25 Delta)`;
- else if `rho>0.75` and `||p||_2>=0.90 Delta_old`, set
  `Delta <- min(100,2 Delta_old)`;
- otherwise leave `Delta` unchanged.

A valid rejected proposal leaves `u` unchanged.
A valid proposal evaluation counts as one trust-region iteration and one residual/objective evaluation.

For an accepted proposal, the certified physical tape at that exact proposal may be reused to compute the new current-chart JAX Jacobian; no additional physical rerecord is required solely for that same-point Jacobian.

### 4.7 Convergence and budget semantics

There is exactly one successful inner convergence criterion:

`||J^T r_aug||_inf <= 1e-8`

at a certified current point.

Small radius, small step, small objective change, or a solver library success flag does **not** independently count as convergence.

Budget counts are inclusive. Before an operation that would exceed a frozen budget, stop and classify

`INNER_MODE_FAIL / TR_BUDGET_EXHAUSTED`.

No tolerance relaxation, alternate solver, warm start, continuation, or retry from a second initial point is permitted.

---

## 5. Exact final Hessian and Laplace semantics

After inner stationarity:

1. physically rerecord the final `z_hat=S u_hat`;
2. compute the **exact fixed-chart JAX Hessian**
   `H_z=D_z^2 Phi_r(z_hat;theta_s,lambda)`
   of the original RB-014 trial objective in physical `z` coordinates;
3. define
   `Htilde=S H_z S`.

The exact coordinate identity is

`H_u=S H_z S`

because `z=S u` is linear at fixed `lambda`.

The authoritative Laplace Hessian is `H_z`, not the Gauss-Newton matrix.

Retain the RB-014 Laplace-validity rules exactly:

- final chart derivative-valid;
- no-jitter Cholesky of `H_z` succeeds;
- all eigenvalues of symmetrized `Htilde` are positive;
- `lambda_min(Htilde) > max(1e-12,1e-10 lambda_max(Htilde))`.

Compute

`log det H_z = 2 sum_i log L_ii`

from the no-jitter Cholesky factor.

No diagonal jitter, clipping, pseudodeterminant, Gauss-Newton substitution, or Hessian regularization is allowed.

Failure is

`INNER_HESSIAN_FAIL`.

The trial contribution to the population objective is still exactly

`Phi_r(z_hat;vartheta)+0.5 log det H_z`.

---

## 6. Outer Laplace objective and bounded-Powell semantics

The population objective remains

`L_Lap(vartheta)=sum_r [Phi_r(z_hat_r;vartheta)+0.5 log det H_z,r]`.

### 6.1 Fixed trial order and failed trial semantics

At every complete outer objective evaluation, trials are processed deterministically in order `r=0,...,15`.

Each trial begins at `u=0`; there is no warm start.

If any trial returns `INNER_MODE_FAIL`, `INNER_HESSIAN_FAIL`, or another physical invalidity, the complete outer point is

`L_Lap=+infinity`.

The evaluator may deterministically short-circuit after the first failing trial because the complete result is already `+infinity`; the failing trial ID/subtype must be recorded.

No trial is dropped, downweighted, imputed, or replaced.

### 6.2 Outer scaling, starts, optimizer and budgets

Retain RB-014 outer scaling:

`x_j=2(vartheta_j-l_j)/(u_j-l_j)-1`,

so `x in [-1,1]^5`.

Use deterministic bounded Powell with:

- `xtol=1e-5`;
- `ftol=1e-8`;
- maximum `300` Powell iterations per start;
- maximum `2500` complete outer objective evaluations per start.

Use exactly the three inherited starts:

- S0: `(p,tau_3,sigma_phi,sigma_psi,sigma_q)=(0.00,1.10,sqrt(0.002),sqrt(0.002),sqrt(0.002))`;
- S1: `(-0.10,0.85,0.03,0.06,0.09)`;
- S2: `(0.10,1.35,0.09,0.06,0.03)`.

The truth is not a start.

### 6.3 Prospective non-finite-start clarification

Before invoking bounded Powell from a start, evaluate the complete outer objective once.

- If finite, the start is `FINITE_INITIAL_START` and Powell may begin.
- If non-finite, mark `OUTER_START_NONFINITE`; Powell is not invoked from that start.
- During Powell, any candidate with a failed trial returns `+infinity` unchanged to the objective callback.
- Any optimizer/library exception caused by non-finite objective arithmetic is caught only to classify that start `OUTER_START_EXCEPTION`; it does not trigger a substitute optimizer or a finite penalty replacement.
- A Powell start is successful only if its termination status is successful within both budgets **and** its final point independently rerecords to a finite complete `L_Lap`.
- If all three starts fail, classify the dataset `OUTER_OPT_FAIL`.

This clarification preserves the RB-014 `+infinity` semantics while preventing an implementation exception from becoming an ungoverned rescue path.

Among successful starts choose the smallest `L_Lap`. If two final objectives differ by at most

`1e-10 max(1,abs(L_best))`,

choose the lexicographically smallest scaled five-vector.

No fourth start or alternate outer optimizer is allowed.

### 6.4 New finite-initial-start hard diagnostic

Across the fixed `32 x 3 = 96` confirmatory initial outer starts, the finite-complete-initial-start fraction must be at least

`0.90`.

This threshold is the complement of the existing RB-014 ten-percent method-failure scale; it is not derived from the post-hoc `94/96` development count.

If the fraction is below `0.90`, the v0.27c scientific result is `SCIENTIFIC FAIL` under the hard method/failure criteria.

Transient non-finite Powell candidate points inside an otherwise successful start are logged but do not by themselves count as failed initial starts.

---

## 7. Deterministic TR-27C implementation-validation suite

All seven TR-27C checks below must PASS, including every negative control, before any `2711xxx` RNG object is created.

The old `94/96` development count is not a validation threshold.

### TR-27C-01 — whitening algebra identity

Freeze

`S=diag(0.05,0.05,0.08,0.08,0.12,0.12)`,

`u=(0.2,-0.3,0.4,-0.5,0.6,-0.7)^T`,

`v=(1,-2,1,-1,2,-1)^T`,

`A=diag(1,2,3,4,5,6)+0.05 vv^T`,

`b=(0.3,-0.2,0.1,-0.4,0.2,0.05)^T`.

Let

`z=S u`,
`q(z)=0.5 z^T A z+b^T z`.

References:

- `0.5 z^T Sigma^-1 z = 0.5 u^T u`;
- `g_z=A z+b`;
- `g_u=S g_z`;
- `H_z=A`;
- `H_u=S H_z S`.

PASS requires:

- prior quadratic absolute error `<=1e-14`;
- scalar transformed-objective absolute error `<=1e-13`;
- gradient max-absolute transformation error `<=1e-13`;
- Hessian relative Frobenius transformation error `<=1e-13`.

Negative control: use
`S_bad=diag(0.05,0.05,0.12,0.12,0.08,0.08)`
in the transformed comparator while retaining the correct reference. At least one positive tolerance must fail.

### TR-27C-02 — exact linear-Gaussian mode

Reuse the C2-27-06 deterministic toy:

```text
A = [[1,0,0,0,0,0],
     [0,1,1,0,0,0],
     [0,0,1,1,0,0],
     [0,0,0,1,1,1]]
```

`y-b=(0.20,-0.10,0.30,0.05)`,
`sigma_t=0.20`,
`S=diag(0.3,0.3,0.4,0.4,0.5,0.5)`.

In physical coordinates,

`H_z=A^T A/sigma_t^2+Sigma^-1`,

`z_exact=H_z^-1 A^T(y-b)/sigma_t^2`,

`u_exact=S^-1 z_exact`.

Run the frozen trust-region solver from `u=0`.

PASS requires:

- `||u_hat-u_exact||_inf <=2e-8`;
- final `||g_u||_inf<=1e-8`;
- exact final `H_z` relative Frobenius error `<=1e-12`;
- Cholesky logdet versus analytical `slogdet(H_z)` absolute error `<=1e-12`.

Negative control: flip the sign of one data-Jacobian column while leaving the analytical reference unchanged. At least one positive tolerance must fail.

### TR-27C-03 — actual Lighthouse residual/Jacobian transformation

Use the frozen v0.27 graph at

`(p,tau_3)=(0.05,0.90)`,

full observation, `H=2`, no timing noise and no missingness.

Use

`S_test=diag(0.05,0.05,0.08,0.08,0.12,0.12)`

and evaluate at `u=0`, `z=0`.

Generate the deterministic base labelled times physically. Define the six-row pseudo-observation vector as those base times plus

`(0.01,-0.02,0.015,-0.01,0.005,-0.015)`.

Compute the exact current-chart JAX augmented-residual Jacobian.

Independent reference: physically rerecorded five-point centered finite differences of the full augmented residual with fixed `h_u=1e-5` in each whitened coordinate.

Every perturbed point must retain derivative-valid physical charts; no step reduction is allowed.

Also compute the already defined physical `z`-Jacobian and verify the algebraic transformation

`J_data,u=J_data,z S_test`.

PASS requires:

- AD-vs-five-point-FD relative Frobenius error `<=2e-6`;
- transformed physical-`z` Jacobian relative Frobenius error `<=1e-10`;
- all physical/chart validity conditions PASS.

Negative control: swap the `psi` and `q` scale blocks in the transformation. The positive transformation tolerance must fail.

### TR-27C-04 — invalid-step contraction and stale-chart rejection

Use a deterministic one-dimensional trust-region harness tied to the C2-27-04 collision sentinel.

Current state:

`u=0`,
`r(u)=u-1`,
`J=1`,
`Delta=1`.

Map each proposal to the two-neuron collision coordinate

`delta(u)=0.01(1-u)`.

The physical validator declares `delta=0` exactly
`EVENT_COLLISION / DERIVATIVE_INVALID`.

The first dogleg step is exactly `p=+1`, proposing `u=1`, hence the collision.

PASS requires:

1. the proposal is rejected without changing the current `u=0`;
2. the radius becomes exactly `0.25` within absolute `1e-15`;
3. a new dogleg step is recomputed from the unchanged current model;
4. the next boundary step is `p=0.25`, hence `u=0.25`, `delta=0.0075`, and is physically valid;
5. no derivative token from `u=0` is accepted as the derivative authority at `u=0.25`.

Negative control: deliberately pass the stale `u=0` token to the `u=0.25` derivative sentinel. It must be rejected.

### TR-27C-05 — nonlinear Lighthouse stationarity and objective consistency

Use the frozen physical graph with

`(p,tau_3)=(0.05,0.90)`,
full observation,
`H=2`,
no timing noise/missingness,

and

`S_test=diag(0.05,0.05,0.08,0.08,0.12,0.12)`.

Generate deterministic pseudo-data from

`u_data=(0.50,-0.30,0.25,-0.20,0.15,-0.10)`

using the physical scheduler.

Fit the trial mode from `u=0` with the frozen trust-region solver.

Independent local reference: at the returned physical/chart-valid mode, solve the exact current-chart whitened gradient equation `g_u=0` using deterministic `scipy.optimize.root(method="hybr")`, initialized exactly at the trust-region result, with `xtol=1e-12`. The reference is valid only if it remains on the same physically rerecorded derivative-valid chart.

PASS requires:

- trust-region `||g_u||_inf<=1e-8`;
- `||u_TR-u_ref||_inf<=1e-6`;
- `|f_TR-f_ref|<=1e-10`;
- `|f(u)+0.5 logdet Sigma - Phi(Su)|<=1e-12`;
- transformed exact-gradient relative error `<=1e-10`;
- final exact `H_z` passes the RB-014 no-jitter Laplace-validity rules.

Negative control: omit the prior residual block `u` while retaining the correct reference. At least one mode/objective consistency tolerance must fail.

### TR-27C-06 — frozen RB-015 development regression subset

This is **DEVELOPMENT ONLY** and never enters the v0.27c scientific performance decision.

Regenerate the relevant old `2701xxx` datasets exactly under RB-015 and verify their SHA-256 hashes against the frozen RB-015 ledger before using them.

Use exactly these fourteen exposed trace fixtures:

- `d=0/S0/r1`, `d=0/S1/r0`, `d=0/S2/r0`;
- `d=8/S0/r0`, `d=8/S1/r1`, `d=8/S2/r0`;
- `d=16/S0/r0`, `d=16/S1/r0`, `d=16/S2/r0`;
- `d=24/S0/r1`, `d=24/S1/r0`, `d=24/S2/r0`;
- `d=5/S2/r0`;
- `d=9/S2/r0`.

For each fixture use its inherited RB-014 outer start, observed rows and trial, and start the new inner solver at `u=0`.

PASS requires all 14 fixtures to:

- terminate by the frozen stationarity criterion, not merely a library success flag;
- satisfy `||g_u||_inf<=1e-8`;
- end on a physical/chart-valid point;
- have finite original `Phi_r`;
- pass the exact final RB-014 no-jitter Hessian/logdet validity rules.

Any invalid proposal encountered en route must be handled only by the frozen radius-contraction/retry rule.

The old `94/96` count is not used as a threshold.

Negative control: flip one bit of the stored observation mask before the dataset-hash guard. The fixture must be rejected before solver execution.

### TR-27C-07 — finite outer-start assembly

Use a deterministic 16-trial linear-Gaussian outer-objective fixture made from eight copies each of the two C2-27-08 masked trial structures.

For even trial indices use `A1,B1,y1,mask1`; for odd indices use `A2,B2,y2,mask2` from C2-27-08.

Interpret the two shared coordinates in those matrices as `(p,tau_3)`, and use each of the three inherited physical outer starts S0, S1, S2 including its three scale values.

At each start:

1. solve all 16 whitened trial modes with the frozen trust-region solver;
2. assemble the full Laplace objective;
3. compute the exact linear-Gaussian marginal NLL independently.

Because Laplace is exact for this linear-Gaussian fixture, compare the objective difference relative to S0 so constants cancel.

PASS requires:

- all three inherited starts have finite complete assembled Laplace objectives;
- each objective-difference error versus the exact Gaussian marginal is `<=1e-9`;
- no optimizer/library exception occurs during assembly.

Negative control: force trial 7 to return `CURRENT_POINT_INVALID`. The complete outer point must return typed `+infinity / OUTER_POINT_INVALID / trial=7`, bounded Powell must not be invoked from that non-finite start, and no SciPy exception may be used as the classifier.

### 7.8 Suite rule

`TR-27C PASS` requires all seven positive checks and all seven negative controls to behave exactly as specified.

Any TR-27C failure yields

`IMPLEMENTATION FAIL / BLOCKED`

and **no confirmatory `2711xxx` RNG object may be created**.

No validation tolerance, fixture, trace membership, radius constant, budget, or negative-control rule may be changed after any TR-27C output is inspected.

---

## 8. Confirmatory stochastic dataset boundary

Only after complete TR-27C PASS may the confirmatory RNG be instantiated.

Use NumPy `PCG64DXSM` with exactly 32 replicate triplets, `d=0,...,31`:

`seed_z^c(d)     = 2711000 + 3d`,

`seed_noise^c(d) = 2711001 + 3d`,

`seed_mask^c(d)  = 2711002 + 3d`.

Generation order is inherited unchanged from RB-014:

1. draw all `R x 6` standard-normal preparation coordinates and multiply blockwise by the three truth SDs;
2. physically generate all `R x 12` latent labelled spike times at the frozen truth;
3. draw all `R x 12` iid `N(0,sigma_t^2)` timing errors;
4. draw all `R x 12` iid masks by `U>=pi_miss`;
5. retain observed timestamps only where the mask is one.

No seed may be replaced. No awkward/failed realization may be regenerated.

The old RB-015 `2701xxx` data and every v0.27b diagnostic trace are excluded from the confirmatory scientific decision.

No `2711xxx` RNG object has been created in this contract gate.

---

## 9. Inherited identifiability, Hessian, uncertainty, and scientific thresholds

All RB-014 scientific thresholds remain unchanged except for the prospective finite-initial-start criterion in Section 6.4.

### 9.1 Conservative free-nuisance information

Retain

`R_r=(I-P_Nr)J_s,r`

and

`I_free=sigma_t^-2 sum_r R_r^T R_r`

with the same SVD rank tolerance and shared-column scaling.

Dataset PASS requires

`lambda_min > max(1e-10,1e-8 lambda_max)`

and

`kappa<=1e8`.

Required fraction: at least `0.90`.

### 9.2 Five-dimensional outer Hessian

Retain the fully reoptimized scaled-coordinate central finite-difference Hessian:

- `h_H=1e-3`;
- repeat at `h_H/2`;
- accept the `h_H/2` Hessian iff relative Frobenius difference `<=0.05`;
- no one-sided replacement at a box boundary.

Regularity requires positive definiteness,

`lambda_min > max(1e-10,1e-8 lambda_max)`,

and `kappa<=1e8`.

Required fraction among successful fits: at least `0.90`.

### 9.3 Shared/profile Schur block

Retain

`H_shared=A-B C^-1 B^T`

with no pseudoinverse rescue.

Required regular fraction among five-Hessian-valid fits: at least `0.90`.

### 9.4 Uncertainty

Retain

`Cov_x=H5^-1`

and the RB-014 coordinate transformation, with two-sided 95% Wald intervals using

`1.959963984540054`.

Intervals are not clipped.

At least `26/32` datasets must produce valid five-parameter intervals, and each of the five coordinate coverages among valid intervals must be at least `0.80`.

### 9.5 Recovery thresholds

For `p` and `tau_3`, normalized by full box widths `0.40` and `1.00`:

- absolute normalized signed bias `<=0.05`;
- median normalized absolute error `<=0.10`;
- 90th-percentile normalized absolute error `<=0.25`.

For each `lambda`, normalized by `log(20)`:

- bias `<=0.08`;
- median absolute error `<=0.15`;
- 90th percentile `<=0.35`.

### 9.6 Failure/usable-fit thresholds

Over all 32 immutable confirmatory replicate IDs:

- `INSUFFICIENT_MASK <=0.10`;
- truth physical/chart invalid fraction `<=0.10`;
- dataset-level terminal `INNER_MODE_FAIL` or `INNER_HESSIAN_FAIL` fraction `<=0.10`;
- `OUTER_OPT_FAIL <=0.10`;
- outer-Hessian/uncertainty-invalid fraction `<=0.20`;
- complete usable-fit fraction `>=0.80`;
- finite complete initial outer-start fraction over all 96 starts `>=0.90`.

A transient non-finite candidate encountered inside an otherwise successful bounded-Powell run is logged but is not by itself a dataset-level terminal inner failure. A dataset-level terminal inner-failure flag is set when the dataset has no successful outer fit and its terminal failure provenance includes an inner mode or inner Hessian failure.

Multiple diagnostic flags may coexist and are all reported.

---

## 10. Exact later execution decision hierarchy

The later governed v0.27c execution must use exactly:

1. **IMPLEMENTATION FAIL / BLOCKED** — any TR-27C-01…07 positive check or negative control fails. No `2711xxx` science runs.
2. **SCIENTIFIC FAIL** — TR-27C passes, but any hard identifiability, finite-initial-start, failure-fraction, Hessian/Schur regularity, or usable-fit criterion in Sections 6.4 and 9.1–9.3/9.6 fails.
3. **SCIENTIFIC CONDITIONAL** — all hard criteria pass, but at least one recovery-error or coverage criterion in Sections 9.4–9.5 fails.
4. **SCIENTIFIC PASS** — every frozen v0.27c criterion passes.

A weak, null, fail, or conditional outcome is final for this preregistered confirmatory branch. It may not be rescued by changing the trust-region constants, graph, truth, seed, R, H, noise, missingness, outer starts, optimizer, thresholds, or scientific metrics.

---

## 11. Environment, determinism, and rerun rules

Before TR-27C validation, capture:

- Python version;
- NumPy version;
- SciPy version;
- JAX version;
- jaxlib version;
- exact CPU/backend;
- `jax_enable_x64`;
- relevant XLA/JAX/OMP/MKL environment flags;
- hash of the executable v0.27c implementation and validation fixture definitions.

Requirements:

- CPU backend only;
- `jax_enable_x64=True` before any validation arithmetic;
- deterministic host RNG only through the frozen PCG64DXSM mapping after TR PASS.

If any software version, backend, executable implementation hash, validation-fixture hash, or relevant deterministic runtime configuration changes **after TR-27C PASS but before the first confirmatory RNG object**, rerun TR-27C-01…07 from the beginning.

If such a change occurs after any `2711xxx` RNG object or confirmatory output has been created, preserve all generated data/output, make no replacement, and

`STOP — RETURN TO MASTER`.

No mixed-environment confirmatory result is permitted in the same execution gate without new MASTER authorization.

---

## 12. Software-plumbing correction rule

Before confirmatory RNG creation, a genuine clerical/software-plumbing defect may be corrected only if:

1. the frozen scientific model/design is unchanged;
2. every trust-region constant, tolerance, fixture, budget, seed, metric and threshold remains unchanged;
3. the defect and invalidated prior output are documented;
4. the complete TR-27C suite reruns from the beginning and passes before RNG.

After any confirmatory `2711xxx` RNG object or effect-bearing output is created, an executable-path correction is not self-authorized. Preserve the output and return to MASTER.

Pure result serialization/transcription corrections that do not alter executable computation may be handled under the existing governance audit rule, with the defective serialized output explicitly invalidated.

No post-output tuning is allowed.

---

## 13. Inherited-vs-new contract table

| component | v0.27c status |
|---|---|
| RB-015 original result | inherited immutable SCIENTIFIC FAIL |
| graph/model/truth/boxes | inherited RB-014 unchanged |
| hierarchical Gaussian family | inherited unchanged |
| R/H/noise/missingness | inherited unchanged |
| physical/event/chart semantics | inherited unchanged |
| population unknowns | inherited unchanged |
| Laplace marginal objective | inherited unchanged |
| inner variable | **new numerical parameterization:** whitened `u=S^-1 z` |
| inner objective | exact augmented least squares, algebraically equivalent |
| inner solver | **new:** deterministic dogleg trust-region Gauss-Newton |
| invalid proposal handling | **new explicit rule:** reject + radius contraction/retry |
| final Laplace Hessian | inherited exact original-coordinate Hessian, no jitter |
| outer scaling/Powell/starts | inherited, with prospective non-finite-start wrapper clarification |
| scientific thresholds | inherited unchanged |
| new method threshold | finite complete initial-start fraction `>=0.90` |
| validation | **new:** TR-27C-01…07 mandatory before RNG |
| old 2701xxx data | DEVELOPMENT ONLY |
| confirmatory seeds | **new disjoint namespace:** 2711xxx, still ungenerated |
| RB-019 engineering baseline | acknowledged; not silently imported into CORE execution path |

---

## 14. Anti-cherry-picking freeze table

The following are fixed before any v0.27c validation/scientific output:

- solver family: whitened dogleg trust-region Gauss-Newton only;
- all trust radii, ratio thresholds, update factors and boundary criterion;
- stationarity tolerance;
- all iteration/evaluation/rerecord/invalid-proposal budgets;
- no-ridge/no-LM/no-pseudoinverse rule;
- exact final-Hessian authority;
- outer `+infinity` and exception semantics;
- exact TR-27C-01…07 membership, fixtures, tolerances and negative controls;
- old development trace membership;
- `2711xxx` seed mapping;
- inherited graph/truth/R/H/noise/missingness;
- inherited recovery/identifiability/coverage/failure/usable-fit criteria;
- new finite-initial-start fraction `>=0.90`;
- execution decision hierarchy.

None may be altered after TR-27C or confirmatory output inspection except through a new MASTER-authorized branch preserving the original result.

---

## 15. Explicit exclusions and deferred branches

This contract does not authorize:

- any `2711xxx` RNG creation in the present gate;
- any confirmatory v0.27c execution in the present gate;
- solver-family search or comparison;
- Armijo-BFGS, Strong-Wolfe-BFGS, Levenberg-Marquardt, generic least-squares substitution, EM, VI or MCMC as a rescue;
- change of graph, truth, parameter boxes, `R`, `H`, timing noise, missingness or hierarchical family;
- active pulse/probe design or direct subthreshold sensing;
- unknown topology, unlabelled spike matching, unknown observation noise or population mean;
- promotion of legacy C3 pulse/sensor/subset/gain results;
- relabelling of RB-015;
- v0.28 effect-bearing science;
- APP-1/APP-2/APP-3 performance execution;
- independent novelty positioning;
- manuscript claim freeze.

---

## 16. Gate decision

# PASS — COMPLETE PRE-EXECUTION V0.27C CONTRACT FIXED; NO CONFIRMATORY OUTPUT GENERATED

The v0.27c follow-up now has a finite and reproducible pre-execution contract.

The contract freezes:

1. the exact whitened augmented residual;
2. the deterministic dogleg trust-region step;
3. all radius/acceptance/update constants;
4. invalid-step contraction/retry semantics;
5. stationarity and finite budgets;
6. exact Hessian/logdet authority;
7. deterministic failed-trial and outer-start behavior;
8. TR-27C-01 through TR-27C-07 with fixed fixtures, tolerances and negative controls;
9. the disjoint `2711xxx` seed namespace;
10. all inherited RB-014 scientific constants and thresholds;
11. one new prospective finite-initial-start hard criterion;
12. environment/change-control and anti-cherry-picking rules.

PASS here is only a **pre-execution contract PASS**. It does not establish trust-region implementation correctness, finite confirmatory starts, parameter recovery, identifiability, coverage, or scientific PASS.

No `2711xxx` RNG object was created or inspected.

---

## 17. Proposed MASTER freeze

If MASTER accepts this gate, establish

`CORE v0.27c Whitened Trust-Region Laplace Execution Contract Freeze 0.1`

as the indivisible pre-execution authority for a later governed v0.27c execution.

The freeze should explicitly state that, at freeze time:

- TR-27C-01 through TR-27C-07 are UNEVALUATED;
- all `2711xxx` confirmatory RNG streams are UNGENERATED / UNEVALUATED;
- no redesigned-method confirmatory performance exists;
- RB-015 remains immutable SCIENTIFIC FAIL.

CORE does not self-authorize that freeze and does not self-authorize execution.

## STOP

STOP — RETURN TO MASTER; NO 2711XXX RNG CREATION; NO CONFIRMATORY V0.27C EXECUTION
