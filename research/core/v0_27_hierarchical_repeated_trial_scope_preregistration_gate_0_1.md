# CORE v0.27 Hierarchical Repeated-Trial Scope & Preregistration Gate 0.1

Date: 2026-09-07
Status: PASS — NARROW HIERARCHICAL REPEATED-TRIAL TARGET PREREGISTERED IN SCOPE; NO V0.27 NUMERICAL EXECUTION

## 1. Authority, Git identity, and provenance boundary

This gate executes the MASTER-authorized prompt

`research/master/prompts/core_v0_27_hierarchical_repeated_trial_scope_preregistration_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `e599afe71c5892dd2c0a45c1febc396d7bcdf7fe`
- CORE STATUS at gate start: `CORE v0.27 Hierarchical Repeated-Trial Scope & Preregistration Gate 0.1 / READY`
- MASTER project status: v1.9
- frozen legacy recovery SHA: `287eae8a86560b78ed94f30a2786243714c33ac0`

Frozen scientific/audit premises reused here:

- RB-004 — `CORE Mathematical Freeze 0.1`;
- RB-006 — governed v0.2 analytical validation PASS;
- RB-007 — v0.3 continuation theory;
- RB-009 — governed v0.3 continuation validation PASS;
- RB-010 — v0.4 spike-time Floquet/symmetry theory;
- RB-011 — `CORE Legacy Verification Sweep Freeze 0.1`;
- RB-012 — `CORE Consolidated C1 Theory Freeze 0.1`.

No frozen premise is re-derived merely to rebuild context. The legacy recovery branch is used only as provenance/hypothesis input. In particular, no legacy v0.21–v0.26 optimized design, uncertainty, gain, pulse, subset, preparation amplitude, noise result, or multistart success rate is treated as established scientific evidence.

No v0.27 simulation, inference run, parameter scan, numerical optimization, benchmark, or effect inspection was performed in this gate.

---

## 2. First v0.27 scientific target — one branch only

The first v0.27 target is:

> **Hierarchical recovery of two shared Lighthouse network parameters from repeated, independently prepared trials with low-dimensional trial-to-trial q=1 preparation variability, Gaussian spike-time noise, and observed missing labelled spike slots, using no active pulse in the first execution.**

This is deliberately narrower than a realistic full-data problem. It does not add unknown topology, unlabelled spikes, pulse-calibration inference, multiple missing-data mechanisms, unknown preparation mean, or large networks.

The purpose of the first execution will be to test whether the shared network block and the three preparation-variability scales are locally/statistically recoverable under one fixed preregistered synthetic design. PASS of this scope gate does **not** assert that they are recoverable.

**Epistemic status:** PROJECT ASSUMPTION / OPEN SCIENTIFIC QUESTION.

---

## 3. Deterministic Lighthouse model and shared scientific block

### 3.1 Base dynamics

The physical dynamics are exactly the deterministic finite-graph, fixed-delay, smooth-response, alpha-synapse Lighthouse baseline frozen in RB-004. Event generation uses first hitting and the frozen delay/event semantics.

The first v0.27 execution uses `N=3` and a known directed graph topology. The graph is not inferred.

### 3.2 Shared scientific parameters

The shared scientific parameter block is

\[
\boxed{\theta_s=(p,\tau_3)\in\Theta\subset\mathbb R^2.}
\]

The notation is retained from the legacy inverse-problem example only to keep lineage readable; no legacy numerical performance is imported.

The physical graph family is required to have the fixed affine form

\[
W(p)=W^{(0)}+pB,
\]

and the fixed delay family

\[
\Tau(\tau_3)=\Tau^{(0)}+\tau_3 C,
\]

where `W^(0)`, `B`, `Tau^(0)` and selector matrix `C` are known design constants, and `C` has support only on the predeclared edge/edge-orbit whose delay coordinate is called `tau_3`.

The later execution contract must freeze the complete numerical matrices, parameter box `Theta`, truth `theta_s^*`, alpha/response parameters, and all other fixed graph constants before any v0.27 output is generated. They may not be chosen by searching for favorable identifiability.

No deviation from the two-dimensional shared block is allowed in the first execution. Additional weights, delays, topology variables, or global observation-clock nuisance are deferred.

**Epistemic status:** PROJECT ASSUMPTION / DESIGN DEFINITION.

---

## 4. Trial-specific latent preparation and gauge convention

Let

\[
v_1=\frac1{\sqrt6}(2,-1,-1)^T,
\qquad
v_2=\frac1{\sqrt2}(0,1,-1)^T,
\]

and define

\[
V=[v_1\;v_2],
\qquad V^T V=I_2,
\qquad V^T\mathbf 1=0.
\]

The global phase/time-translation direction is not duplicated. Trial `r` has six preparation coordinates

\[
\boxed{z_r=(\eta_r,\xi_{\psi,r},\xi_{q,r})\in\mathbb R^6,}
\]

with each sub-block in `R^2`:

\[
\eta_r=(\eta_{1r},\eta_{2r}),\quad
\xi_{\psi,r}=(\xi_{\psi1,r},\xi_{\psi2,r}),\quad
\xi_{q,r}=(\xi_{q1,r},\xi_{q2,r}).
\]

Relative phase and alpha-synapse preparation are

\[
\phi_{0,r}=\bar\phi_0+V\eta_r,
\]

\[
\psi_{0,r}=\bar\psi_0+V\xi_{\psi,r},
\qquad
q_{0,r}=\bar q_0+V\xi_{q,r}.
\]

The nominal means `bar(phi)_0`, `bar(psi)_0`, and `bar(q)_0` are known fixed design states in the first v0.27 target. An unknown population mean is deferred.

The two-dimensional phase perturbation is therefore explicitly gauge-fixed in `1^perp`, and the initial synaptic variability spans the full real q=1/zero-mean subspace in both `psi` and `q`, consistent with the free-state assumptions underlying RB-012 C1-5.

**Epistemic status:** PROJECT ASSUMPTION, structurally compatible with RB-012.

---

## 5. Hierarchical preparation law

The first hierarchical law is an i.i.d. zero-mean Gaussian random-effects model

\[
\boxed{z_r\mid\lambda\overset{iid}{\sim}\mathcal N(0,\Sigma_z(\lambda)),}
\]

with

\[
\boxed{
\Sigma_z(\lambda)=
\operatorname{diag}
\bigl(
\sigma_\phi^2 I_2,
\sigma_\psi^2 I_2,
\sigma_q^2 I_2
\bigr),
}
\]

and log-scale hyperparameters

\[
\boxed{\lambda=(\lambda_\phi,\lambda_\psi,\lambda_q),\qquad
\sigma_a=e^{\lambda_a}>0.}
\]

The population-level unknown block is therefore

\[
\boxed{\vartheta=(p,\tau_3,\lambda_\phi,\lambda_\psi,\lambda_q)\in\mathbb R^5.}
\]

### 5.1 Why this is the first law

The zero mean is a first-scope identifiability constraint relative to the known nominal preparation. Isotropy inside each two-dimensional q=1 subspace avoids introducing basis-dependent covariance angles, and three scale parameters are the smallest model that distinguishes phase, synaptic-drive and synaptic-derivative preparation variability.

The first target does **not** estimate:

- a six-dimensional preparation mean;
- cross-covariances between phase, `psi`, and `q`;
- anisotropy within a q=1 pair;
- mixture distributions, heavy tails, trial clusters, or temporal drift.

Those are deferred unless the first model fails in a scientifically informative way and MASTER later opens a new branch.

**Epistemic status:** PROJECT ASSUMPTION. Gaussianity is not claimed to be source-derived or biologically universal.

---

## 6. Observation model: labelled timing noise plus observed missing slots

For a fixed observation horizon of `H` firing cycles, let

\[
F_H(\theta_s,z_r)\in\mathbb R^K,
\qquad K=3H,
\]

be the vector of physical labelled spike times produced by the event scheduler, indexed by a predeclared pair `(neuron, ordinal spike number within the observation window)`.

The first imperfection model has two components only.

### 6.1 Timing noise

For an observed slot `k`,

\[
y_{rk}=F_{H,k}(\theta_s,z_r)+\epsilon_{rk},
\qquad
\epsilon_{rk}\overset{iid}{\sim}\mathcal N(0,\sigma_t^2).
\]

The timing-noise scale `sigma_t` is a known acquisition/design parameter in the first execution; it is not estimated.

### 6.2 Missing labelled spike slots

Each candidate slot has an observed mask

\[
m_{rk}\in\{0,1\},
\]

with

\[
\boxed{m_{rk}\overset{iid}{\sim}\operatorname{Bernoulli}(1-\pi_{miss})}
\]

independently of `z_r`, `theta_s`, and `epsilon_r` in the first target.

The mask is observed. A missing spike therefore means that the timestamp for a known `(neuron, ordinal)` slot is absent; it does **not** create an unlabelled sequence-matching problem. The physical spike still occurs in the latent trajectory and can affect later dynamics.

`pi_miss` is known and fixed by the later execution contract. Since the mask law is independent of the model unknowns, its likelihood is constant with respect to `vartheta` and may be omitted from the optimization after conditioning on the observed masks.

A stochastic validation replicate whose mask is too sparse for a preregistered minimal-data rule must be counted according to the predeclared failure/insufficient-data rule; it must not be silently regenerated after seeing the mask.

**Epistemic status:** PROJECT ASSUMPTION / first missingness model (MCAR).

---

## 7. Calibration treatment: no active pulse in v0.27 first execution

The first v0.27 target uses **no active input pulse**.

Reasons:

1. RB-012 proves that, under its stated free-state assumptions, fixed-time `(A,beta,gamma)` calibration directions are structurally absorbed by trial-state nuisance.
2. Legacy optimized pulse and two-probe choices are C3 and may not be imported as confirmatory design.
3. Removing active intervention gives the smallest hierarchical repeated-trial test and isolates what repeated preparation variability plus incomplete spike observation does to shared-parameter inference.

Therefore pulse amplitude, direction, timing, pulse calibration, direct subthreshold sensing, and all active-design optimization are explicitly excluded from the first v0.27 execution.

This is an experimental-scope choice, not a claim that passive trials are sufficient.

---

## 8. Primary inference route: Laplace-approximated marginal maximum likelihood

The primary route is fixed now and is not interchangeable after outputs are seen.

Let `M_r` denote the row-selection operator induced by the observed mask. Define the conditional residual

\[
r_r(z;\theta_s)=M_r\bigl(y_r-F_H(\theta_s,z)\bigr).
\]

For known `sigma_t`, define the per-trial negative joint log-density, up to constants independent of the unknowns,

\[
\boxed{
\Phi_r(z;\theta_s,\lambda)
=
\frac{1}{2\sigma_t^2}\|r_r(z;\theta_s)\|_2^2
+\frac12 z^T\Sigma_z(\lambda)^{-1}z
+\frac12\log\det\Sigma_z(\lambda).
}
\]

For fixed population parameters, the trial mode is

\[
\boxed{\hat z_r(\theta_s,\lambda)=\arg\min_z\Phi_r(z;\theta_s,\lambda).}
\]

Let

\[
H_r=\nabla_z^2\Phi_r(\hat z_r;\theta_s,\lambda).
\]

When `H_r` is positive definite, the Laplace-approximated marginal negative log-likelihood is

\[
\boxed{
\mathcal L_{Lap}(\theta_s,\lambda)
=
\sum_{r=1}^{R}
\left[
\Phi_r(\hat z_r;\theta_s,\lambda)
+\frac12\log\det H_r
\right]
+\text{constant}.
}
\]

The first execution will estimate

\[
\boxed{\hat\vartheta=\arg\min_{(\theta_s,\lambda)\in\Theta\times\Lambda}\mathcal L_{Lap}.}
\]

The compact domains `Theta` and `Lambda`, inner/outer optimization method, derivative method, stopping rules, initialisation policy, maximum evaluations, chart handling and failure rules must all be frozen in the later execution contract.

If a trial mode is not isolated or `H_r` is not positive definite under the preregistered numerical rule, that is a recorded Laplace/inference failure; the method may not be swapped post hoc for EM, variational inference, MCMC, a different prior, or a different objective within the same branch.

**Epistemic status:** PROJECT METHOD DEFINITION / ASSUMPTION. No performance claim is made.

---

## 9. Local/structural identifiability questions

The first execution has two distinct identifiability audits. They must not be conflated.

### 9.1 Conservative free-nuisance shared-parameter audit

For trial `r`, using only observed rows at a regular physical chart, define

\[
J_{s,r}=D_{\theta_s}\,M_rF_H(\theta_s,z_r),
\qquad
N_r=D_z\,M_rF_H(\theta_s,z_r).
\]

Using RB-012 C1-4,

\[
\boxed{R_r=(I-P_{N_r})J_{s,r}.}
\]

For independent trials the conservative profiled information diagnostic is

\[
\boxed{
\mathcal I_{free}
=\sigma_t^{-2}\sum_{r=1}^{R}R_r^TR_r.
}
\]

Primary question Q1:

> Is `rank(I_free)=2` under the preregistered truth, trial count, preparation law, masks and horizon?

This treats every trial preparation as locally free and therefore does not credit the Gaussian hierarchy with extra regularization. Failure of this audit is a scientifically valid negative result, not a trigger to redesign the experiment.

### 9.2 Hierarchical population-parameter audit

Let

\[
\vartheta=(p,\tau_3,\lambda_\phi,\lambda_\psi,\lambda_q).
\]

Primary question Q2:

> Is the observed/expected local information or Hessian of the preregistered Laplace objective with respect to `vartheta` full rank five and numerically regular under the predeclared rank/conditioning rule?

Primary question Q3:

> Are the two shared scientific directions distinguishable from the three preparation-scale directions, as quantified by the appropriate Schur-complement/profile block of the five-dimensional local information matrix?

Primary question Q4:

> Does observed missingness produce a predeclared fraction of information/admissibility failures, and are those failures compatible with the preregistered success criterion without changing the mask model or horizon?

No claim of global identifiability is part of v0.27 first scope.

---

## 10. Synthetic-data generator skeleton for the later execution contract

The first governed execution must generate synthetic datasets only from the following skeleton.

For each stochastic dataset replicate:

1. use the fixed `N=3` graph family `W(p)`, `Tau(tau_3)` and the frozen baseline dynamics;
2. set one preregistered truth `theta_s^*=(p^*,tau_3^*)`;
3. set one preregistered population scale vector `lambda^*`;
4. for `r=1,...,R`, draw one `z_r` from the zero-mean Gaussian law in Section 5 using the frozen RNG scheme;
5. construct the trial initial state from the known nominal state plus `V`-projected preparation coordinates;
6. run the physical event scheduler until the fixed horizon `H` produces `K=3H` labelled spike slots, or trigger the preregistered physical/admissibility failure rule;
7. draw the observed MCAR mask with fixed `pi_miss` and frozen RNG scheme;
8. add Gaussian timing noise with fixed `sigma_t` to observed slots only;
9. fit only by the Laplace-marginal route of Section 8 using the frozen initialization/optimizer/chart rules;
10. retain the latent truth and masked true spike times only for post-fit evaluation metrics, never as fit inputs.

The execution contract must predefine all numerical values, all RNG seeds or a deterministic seed-generation rule, the number of dataset replicates, and the rule for handling generator/inference failures before the first dataset is generated.

No value may be chosen by looking for a favorable result.

---

## 11. Predeclared success/failure observables

The later execution contract must attach numerical PASS/FAIL thresholds to the following finite metric set before execution.

### Primary scientific metrics

1. **Shared-parameter error:** separate signed bias and absolute/normalized error for `p` and `tau_3` over the preregistered replicate set.
2. **Preparation-scale error:** bias/error for `lambda_phi`, `lambda_psi`, and `lambda_q` (or equivalently the three SDs, with the reporting parameterization frozen in advance).
3. **Conservative shared information:** rank, smallest eigenvalue/singular value, and condition number of `I_free` under the frozen numerical rank convention.
4. **Hierarchical information:** rank and conditioning of the five-dimensional Laplace observed-information/Hessian matrix and the shared-parameter Schur/profile block.
5. **Uncertainty calibration:** empirical coverage of preregistered nominal intervals for the two shared parameters and, if retained by the execution contract, for the three log-scale hyperparameters.

### Missing-data metrics

6. **Masked-slot predictive error:** RMSE and maximum absolute error of fitted/posterior-mode predictions at synthetic spike slots that were masked from inference. These true masked times are evaluation-only.
7. **Mask insufficiency rate:** fraction of replicates/trials hitting the preregistered insufficient-observation rule.

### Hybrid/numerical validity metrics

8. **Physical admissibility failure rate:** fraction of trials/replicates that fail first-hitting/transversality/horizon requirements under the frozen rule.
9. **Chart diagnostics:** number/fraction of optimization steps requiring physical chart rerecording, plus final-chart validity; chart switching is a diagnostic and is not automatically a scientific failure unless the contract says so.
10. **Laplace validity/convergence rate:** fraction of fits with valid isolated inner modes, positive-definite `H_r` under the frozen tolerance, and successful outer convergence.

No unlisted metric may replace a failed primary metric after outputs are inspected. Additional exploratory diagnostics may be reported only if explicitly labelled exploratory and cannot change the frozen decision.

---

## 12. Required C2 implementation dependencies — minimal set only

The first v0.27 execution requires only the following implementation capabilities:

1. **Physical fixed-delay alpha event scheduler** for the RB-004 baseline with labelled spikes, delayed arrivals, first-hit/transversality checks and deterministic event ordering.
2. **Fixed-chart differentiable replay/Jacobians** with respect to `(p,tau_3,z_r)` for observed spike rows.
3. **Chart-validity sentinel and physical rerecording** if an inner or outer optimization step crosses an event-order boundary; derivatives remain one-sided within a recorded physical chart.
4. **Hierarchical/Laplace layer introduced in v0.27:** Gaussian random-effects penalty, trial-mode solve, Hessian/log-determinant calculation, missing-row selection, and outer five-parameter objective.

Legacy v0.18–v0.20 contains C2 candidate machinery relevant to items 1–3, but RB-011 does not freeze it as production-valid. Before effect-bearing v0.27 execution, the later contract must either:

- exact-replay and validate the exact required committed C2 path under a frozen replay sub-contract, or
- implement a fresh minimal path and validate it against predeclared deterministic equivalence/finite-difference tests.

The execution does **not** require:

- v0.6–v0.15 bifurcation/invariant-circle machinery;
- v0.16/v0.17 large-N scaling claims as scientific premises;
- adaptive or in-flight delays;
- active-pulse v0.24/v0.25 code;
- optimized observation subsets;
- direct synaptic sensors;
- application code.

---

## 13. Required comparison with legacy v0.26

| v0.26 element | status after RB-011/RB-012 | reused in v0.27? | reason | new assumption/change |
|---|---|---|---|---|
| Shared parameter example `(p,tau3)` | legacy numerical performance C3; the two-coordinate choice itself is not a frozen performance result | **Yes, as a fresh v0.27 design definition** | smallest lineage-compatible scientific block | fixed affine graph/delay parameterization must be frozen before execution; no legacy truth/performance imported |
| Per-trial six-dimensional q=1 preparation | free-state structure compatible with RB-012 C1-5; legacy amplitudes/results C3 | **Yes** | exactly the nuisance space needed for the narrow repeated-trial extension | coordinates expressed in an explicit orthonormal zero-mean basis; nominal mean fixed |
| Nuisance projector/profiled sensitivity `R=(I-P_N)J_s` | **RB-012 FROZEN / STABLE C1** | **Yes** | provides conservative many-trial shared-information audit | observed-row masks are applied before residualization; hierarchical audit added separately |
| Fixed-time `(A,beta,gamma)` pulse calibration ambiguity | **RB-012 FROZEN / STABLE C1 under assumptions** | **Yes, only as exclusion logic** | prevents importing an ill-posed self-calibration target | first v0.27 execution has no active pulse |
| v0.26 profiled singular values / shared uncertainty values | C3 / not frozen | **No** | effect-bearing numerical output | no acceptance threshold may be based on these values |
| v0.26 preparation-jitter amplitudes | C3 exploratory design choices | **No** | not preregistered evidence | new population scales must be fixed independently in the execution contract |
| v0.26 calibration uncertainty values | C3 exploratory | **No** | active calibration excluded | no calibration prior in first target |
| v0.26 noise and multistart results | C3 exploratory | **No** | cannot establish expected recovery | new noise level, replicate count and initialization policy must be frozen before output |
| v0.24/v0.25 pulse/P2/subset designs inherited by v0.26 lineage | C3 optimized/effect-selected | **No** | would violate anti-cherry-picking boundary | passive full predeclared labelled-slot horizon only |

---

## 14. Anti-cherry-picking freeze list for the later execution contract

Before **any** v0.27 numerical output, the next governed contract must freeze at minimum:

### Physical model

1. complete `W^(0)`, `B`, `Tau^(0)`, `C` matrices and topology;
2. alpha and response parameters and all other baseline constants;
3. nominal initial state `(bar(phi)_0,bar(psi)_0,bar(q)_0)` and gauge convention;
4. truth `(p^*,tau_3^*)` and admissible parameter box `Theta`.

### Hierarchy

5. exact Gaussian law and truth `(lambda_phi^*,lambda_psi^*,lambda_q^*)`;
6. admissible hyperparameter box `Lambda`;
7. number of trials `R`;
8. whether the same nominal preparation is used for every trial.

### Observation generator

9. observation horizon `H` and exact labelled-slot ordering;
10. timing-noise scale `sigma_t`;
11. missingness probability `pi_miss` and MCAR rule;
12. stochastic replicate count and all RNG seeds/seed-generation rules;
13. insufficient-mask handling rule.

### Inference

14. Laplace objective exactly as used in code;
15. inner trial-mode optimizer, outer optimizer, derivatives and linear algebra method;
16. initialization policy, including every multistart if multistart is permitted;
17. maximum evaluations/iterations, step/trust rules and stopping tolerances;
18. parameter transformations/bounds;
19. Hessian positive-definiteness and rank tolerances;
20. chart sentinel, chart rerecording rules, event tie tolerance and admissibility rules;
21. C2 validation/equivalence tests required before the scientific dataset is evaluated.

### Decision

22. exact primary metrics from Section 11;
23. numerical PASS/FAIL thresholds for every primary metric;
24. coverage confidence level and exact acceptance interval if coverage is a primary criterion;
25. aggregate decision rule across stochastic replicates and any allowed partial-failure category;
26. software-plumbing correction rule specifying what may be repaired without changing science;
27. explicit rule that failed/weak/null outcomes are preserved and not followed by same-branch retuning.

No quantity in this list may be altered after output inspection except through a new MASTER-authorized branch with a new provenance record.

---

## 15. Explicit exclusions and deferred branches

The first v0.27 target excludes:

- active pulses or direct subthreshold sensors;
- pulse calibration inference;
- unknown topology;
- unknown spike identity / sequence matching;
- false-positive extra observed spikes;
- unknown missingness mechanism or MNAR/MAR dependence on state;
- unknown observation clock offset;
- unknown population preparation mean;
- full 6x6 preparation covariance or mixture laws;
- non-Gaussian preparation distributions;
- adaptive/in-flight delays;
- unlabelled/missed-event data association;
- large-N scaling as a scientific target;
- v0.6–v0.15 bifurcation/global-object validation;
- reuse of legacy optimized sensor/pulse/subset choices;
- applications;
- novelty positioning;
- manuscript claim freeze.

A failure of the first target does not automatically authorize any deferred extension.

---

## 16. Novelty / provenance labels for v0.27

No novelty claim is made.

- Shared two-parameter hierarchical target: **PROJECT ASSUMPTION / NEW PROJECT SCOPE**.
- Gaussian zero-mean three-scale preparation law: **PROJECT ASSUMPTION**.
- MCAR labelled-slot missingness model: **PROJECT ASSUMPTION**.
- Laplace-marginal inference route: **PROJECT METHOD DEFINITION**.
- Many-trial free-nuisance residualization formula: **RB-012-DERIVED PREMISE + PROJECT APPLICATION**.
- Whether the five population parameters are identifiable/recoverable: **OPEN QUESTION**.
- Whether missing labelled spikes can be predicted accurately: **OPEN QUESTION**.
- Any later performance/effect size: **UNEVALUATED** until governed execution.

Independent literature/novelty audit remains a separate MASTER-authorized LIT task.

---

## 17. Proposed contents of the next governed execution contract

A later `CORE v0.27 Hierarchical Repeated-Trial Execution Contract 0.1` should contain, before execution:

1. immutable Git/freeze identity and this scope artifact as authority;
2. all numerical physical-model constants and truth values;
3. exact trial count, hierarchy scales and seed schedule;
4. exact horizon, timing-noise and missingness configuration;
5. deterministic reference/sanity cases for the physical scheduler;
6. fixed-chart Jacobian vs finite-difference validation cases;
7. chart-sentinel/rerecord validation cases if the chosen optimizer can cross charts;
8. exact Laplace objective, Hessian construction and log-determinant convention;
9. inner/outer optimizer and initialization policy;
10. rank/conditioning conventions;
11. stochastic replicate count;
12. masked-slot evaluation protocol;
13. uncertainty/coverage construction;
14. all metric thresholds and aggregate PASS/FAIL logic;
15. software-plumbing correction rule;
16. explicit `FAILED/WEAK/NULL` preservation rule;
17. an execution STOP boundary forbidding retuning after first scientific output.

The contract must separate pre-scientific C2 implementation validation from the effect-bearing hierarchical result, even if both are executed in one governed workflow.

---

## 18. Gate decision

# PASS

`CORE v0.27 Hierarchical Repeated-Trial Scope & Preregistration Gate 0.1` passes.

PASS means only that one first v0.27 target is now sufficiently narrow, mathematically coherent, traceable to RB-004/RB-011/RB-012, and capable of being converted into a fully numerical pre-execution contract without inspecting v0.27 effects.

PASS does **not** mean:

- `(p,tau_3)` are identifiable;
- the preparation scales are identifiable;
- the Laplace approximation is adequate;
- passive repeated trials outperform any legacy design;
- missing spikes can be recovered accurately;
- the implementation is validated;
- any numerical success criterion has been met;
- any novelty has been established.

No v0.27 numerical execution has occurred.

## 19. STOP

Deliverable complete. CORE must return to MASTER for review and possible authorization of a separate numerical execution-contract gate.

STOP — RETURN TO MASTER
