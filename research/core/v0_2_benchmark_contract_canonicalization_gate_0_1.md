# CORE v0.2 Benchmark Contract Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — PRE-EXECUTION BENCHMARK CONTRACT COMPLETE; NO BENCHMARK EXECUTED

## 1. Input / provenance identity

This gate constructs a governed benchmark contract under the frozen mathematical baseline:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `401e329e187e3e2631a69e55d2fa8b77c0080307`
- canonical mathematical freeze: `research/core/mathematical_freeze_0_1.md`
- mathematical freeze status: `FROZEN / STABLE`, rollback point `RB-004`
- frozen scope source: `research/core/mathematical_scope_canonicalization_gate_0_1.md`
- frozen legacy recovery input inspected only as historical design input: commit `287eae8a86560b78ed94f30a2786243714c33ac0`
- legacy v0.2 candidate derivations: `docs/core/derivations_v0.2.md`
- legacy v0.2 candidate benchmark contract: `docs/core/benchmark_contract_v0.2.md`

The legacy branch is used only to recover candidate benchmark ideas. No legacy numerical output is treated as evidence. No benchmark was executed in this gate.

The authoritative mathematical targets are only frozen baseline equations C1–C11, assumptions A1–A13, registered analytical variants, and elementary identities D1–D18 contained in RB-004.

---

## 2. Legacy v0.2 asset inventory

At the frozen recovery snapshot the relevant v0.2 assets are:

1. `docs/core/derivations_v0.2.md`
   - analytical formulas for the periodic kernel comb, alpha state, isolated clock, autapse, phase locking, linear row-sum reduction, event-time perturbation and additional later stability material;
2. `docs/core/benchmark_contract_v0.2.md`
   - legacy benchmark definitions B0–B10;
3. no standalone committed v0.2 reference script;
4. no standalone committed v0.2 benchmark JSON.

Therefore there is **no exact-replay object for v0.2**. This gate creates a new pre-execution contract from the frozen mathematics; it does not replay a missing legacy executable.

### Relationship among the assets

- `derivations_v0.2.md` supplied candidate mathematical targets during recovery.
- The mathematical-scope canonicalization gate independently re-derived and froze only the C1-eligible subset as D1–D18.
- `benchmark_contract_v0.2.md` supplied historical test-design ideas, but its acceptance rules are not canonical merely because they were committed.
- This document is the first governance-compliant pre-execution benchmark contract tied directly to RB-004.

---

## 3. Legacy benchmark inclusion / exclusion matrix

| Legacy ID | Legacy topic | Relation to RB-004 | Decision | Reason |
|---|---|---|---|---|
| B0 | isolated linear Lighthouse neuron | D6–D7; V-S2 | **RETAIN / REPAIR** | valid frozen analytical variant, but canonical contract also adds a baseline-response isolated clock |
| B1 | alpha-kernel impulse response | C3, C6–C7; D1-equivalent state realization | **RETAIN / TRANSLATE** | legacy used `u`; freeze uses project state `q=alpha u` |
| B2 | periodic alpha-kernel orbit | D1–D5 | **RETAIN** | directly frozen elementary identity family |
| B3 | unbalanced synchronous linear period | D13–D14 | **RETAIN / REFRAME** | retain as row-sum benchmark with explicit admissibility/history rules; no open-ended sweep |
| B4 | balanced synchronous network | D13–D15 | **RETAIN** | exact frozen special case |
| B5 | two-cell mode decomposition | not D1–D18 | **DEFER** | eigenmode/stability structure is not part of RB-004 benchmark freeze target |
| B6 | modal flow matrix | not D1–D18 | **DEFER** | downstream flow/Floquet structure is outside current freeze |
| B7 | saltation matrix | not D1–D18 | **DEFER** | generic saltation matrix was not frozen; only elementary event-time identity D18 is frozen |
| B8 | event-time sensitivity | D18, C10 | **RETAIN / REPAIR** | retain only elementary transversal event-time identity; no downstream Floquet interpretation |
| B9 | slow-synapse modal roots | explicitly future target only | **DEFER** | asymptotic stability theory is outside RB-004 |
| B10 | delay-induced imaginary-axis algebra | explicitly future target only | **DEFER** | derived from the unfrozen slow-synapse characteristic equation |

No B5–B7 or B9–B10 acceptance value may enter the first benchmark freeze.

---

## 4. Contract-wide execution conventions

These rules are part of the proposed benchmark contract and must be fixed before any execution.

### 4.1 Precision

All future numerical checks in this contract use IEEE-754 binary64 / float64 arithmetic. A lower-precision implementation requires a separately authorized tolerance contract and cannot silently weaken these thresholds.

### 4.2 Error metric

Unless a benchmark states otherwise, a scalar or pointwise numerical comparison passes when

\[
|x-x_{ref}| \le a_{tol}+r_{tol}|x_{ref}|.
\]

Canonical tolerance classes are:

- **E0 — exact symbolic/algebraic:** equality must follow exactly from algebra / symbolic simplification; no numerical tolerance.
- **N1 — closed-form pointwise or event quantity:** `a_tol = 1e-12`, `r_tol = 1e-10`.
- **N2 — integrated residual / periodic closure:** `a_tol = 1e-10`, `r_tol = 1e-10`.
- **L0 — logical admissibility:** exact Boolean pass/fail; no tolerance except where a numerical comparison uses N1/N2 internally.

No tolerance may be changed after observing benchmark errors.

### 4.3 Numerical method classes

The later execution gate may use only the following method classes for this contract:

1. exact algebra / symbolic evaluation;
2. closed-form analytical evaluation;
3. deterministic float64 quadrature for a pre-specified finite interval;
4. deterministic event/root solver used only to locate a first hitting time;
5. deterministic evaluation of the frozen alpha state-space flow.

No optimizer, continuation routine, parameter search, adaptive-design routine, inference routine or v0.3+ solver is needed or authorized by this contract.

### 4.4 Histories for delayed periodic tests

A delayed periodic benchmark must start from the **exact periodic spike/history state implied by the reference solution**, not from a transient warm-up chosen after inspecting convergence. The history interval must cover `[-tau_max,0]` and be generated analytically from the prescribed periodic spike train.

### 4.5 No hidden scans

Finite test sets listed below are fixed benchmark cases, not searches. They must be executed exactly as written. No extra parameter point may be added to improve or rescue a failed result inside the same execution gate.

---

## 5. Fully pre-specified proposed benchmark contract

### BC01 — alpha-kernel normalization

**Frozen target:** C3 and Section 9.1 of the frozen scope source.  
**Classification:** E0 exact symbolic/algebraic.  
**Epistemic target:** LEMMA / PROVED, SOURCE-DERIVED + DERIVATION HERE.

**Model / variant**

Baseline alpha kernel

\[
\eta_\alpha(t)=\alpha^2 t e^{-\alpha t}H(t),\qquad \alpha>0.
\]

**Parameter domain**

Symbolic `alpha>0`; no fitted or scanned value.

**Initial/history conditions**

Not applicable.

**Observable**

\[
I(\alpha)=\int_0^\infty\eta_\alpha(t)\,dt.
\]

**Independent reference**

\[
I(\alpha)=1.
\]

**Method class**

Exact integration / symbolic algebra.

**Domain / resolution**

Exact improper integral on `[0,infinity)`; no discretization.

**Tolerance**

E0: exact equality.

**Pass rule**

PASS iff the symbolic result simplifies to `1` under `alpha>0`.

**Admissibility requirements**

`alpha>0`.

**Expected failure mode**

If `alpha<=0`, causality/decay/normalization assumptions fail and the benchmark is invalid rather than numerically failed.

---

### BC02 — impulse / state-space equivalence

**Frozen target:** C3, C6–C7 and Section 9.2.  
**Classification:** E0 derivation + N1 future numerical cross-formulation test.  
**Epistemic target:** PROPOSITION / PROVED.

**Model / variant**

Baseline alpha synapse using project state `(a,q)`.

**Parameters**

\[
\alpha=2.
\]

**Initial/event conditions**

Immediately before a single spike at `t=0`:

\[
a(0^-)=0,\qquad q(0^-)=0.
\]

Apply the frozen jump

\[
q(0^+)=4,\qquad a(0^+)=0.
\]

**Observable**

`q(t)` and `a(t)` for `0<=t<=2`.

**Independent reference**

\[
q_{ref}(t)=4e^{-2t},
\qquad
 a_{ref}(t)=4te^{-2t}.
\]

**Method class**

Frozen state-space flow compared with the closed-form kernel response.

**Horizon / resolution**

257 equally spaced points on `[0,2]`, including both endpoints.

**Tolerance**

N1 pointwise for both states at every sample point.

**Pass rule**

PASS iff every sampled `a,q` value meets N1, `a(0^+)=0` meets N1, and the jump `q(0^+)-q(0^-)=4` meets N1.

**Admissibility requirements**

One and only one spike at `t=0`; no additional input.

**Expected failure modes**

Wrong jump normalization (`alpha` instead of `alpha^2`), state-variable scaling confusion between `u` and `q`, or discontinuously jumping `a`.

---

### BC03 — periodic alpha comb and unit-mass identity

**Frozen target:** D1–D3.  
**Classification:** E0 identity + N1/N2 future analytical-numerical cross-check.  
**Epistemic target:** LEMMA / PROPOSITION, PROVED.

**Model / variant**

Baseline alpha kernel.

**Parameters**

\[
\alpha=2,\qquad T=\pi,\qquad \rho=e^{-2\pi}.
\]

**Initial/history conditions**

Infinite periodic spike train `T^m=mT`, represented analytically; no finite warm-up.

**Observable**

The periodic comb on one fundamental interval,

\[
R_T(t)=\sum_{m\in\mathbb Z}\eta_\alpha(t-mT),\qquad 0\le t<T,
\]

and its one-period mass.

**Independent reference**

For `u=t mod T`,

\[
R_{ref}(t)=4e^{-2u}
\left[
\frac{u}{1-\rho}+\frac{\pi\rho}{(1-\rho)^2}
\right],
\]

and

\[
\int_0^T R_T(s)ds=1.
\]

**Method class**

Closed-form reference versus independently evaluated periodic activation; deterministic float64 quadrature for the period integral.

**Horizon / resolution**

513 equally spaced phase points on `[0,T)`. The unit-mass integral is evaluated over `[0,T]` by deterministic adaptive quadrature whose absolute and relative stopping tolerances are both set to `1e-13` before execution.

**Tolerance**

N1 for pointwise comb values; N2 for the integrated mass.

**Pass rule**

PASS iff all pointwise values meet N1 and the integral equals `1` within N2.

**Admissibility requirements**

Exact periodic history and `alpha,T>0`.

**Expected failure modes**

Finite-history startup contamination, wrong causal index convention, missing previous-cycle pulses, or incorrect kernel normalization.

---

### BC04 — periodic hybrid alpha state / periodic closure

**Frozen target:** D4–D5 and equivalence to D3.  
**Classification:** E0 + N1/N2.  
**Epistemic target:** PROPOSITION / PROVED.

**Model / variant**

Baseline alpha state `(a,q)` with `q=alpha u`.

**Parameters**

\[
\alpha=2,\qquad T=\pi,\qquad \rho=e^{-2\pi}.
\]

**Initial/post-spike state**

\[
q^+=\frac{4}{1-\rho},
\qquad
 a^+=\frac{4\pi\rho}{(1-\rho)^2}.
\]

**Observable**

Flow over one cycle, pre-event state at `T^-`, post-jump state at `T^+`, and `a(t)` over the cycle.

**Independent reference**

\[
q(t)=q^+e^{-2t},
\qquad
 a(t)=e^{-2t}(a^+ + q^+ t),
\qquad 0\le t<T,
\]

with jump `q^+=q^-+4`, continuous `a`, and periodic closure after the jump.

**Method class**

Deterministic alpha state-space flow; compare against closed form.

**Horizon / resolution**

One period; 257 equally spaced points on `[0,T)` plus explicit evaluation of `T^-` and the post-jump state.

**Tolerance**

N1 pointwise; N2 for the full-state periodic closure norm.

**Pass rule**

PASS iff pointwise states meet N1, `a(T^+)=a(T^-)` meets N1, `q(T^+)-q(T^-)=4` meets N1, and the post-jump state equals the prescribed initial post-spike state within N2.

**Admissibility requirements**

Exactly one spike per period with the prescribed periodic state.

**Expected failure modes**

Incorrect jump order, wrong rescaling from `u` to `q`, or using transient rather than periodic initial conditions.

---

### BC05 — isolated-clock identity

**Frozen target:** D6–D7.  
**Classification:** E0 + N1 exact-event test.  
**Epistemic target:** PROPOSITION / PROVED.

#### BC05-A — frozen baseline response

**Model**

One isolated neuron, no recurrent input, baseline response C2.

**Parameters**

\[
r=1,\qquad h=-1,\qquad \theta(0)=0.
\]

Then

\[
S(0)=e^{-1}.
\]

**Reference**

\[
\theta(t)=e^{-1}t,
\qquad
T_0=2\pi e.
\]

**Observable**

First hitting of `theta=2*pi`.

**Method class**

Closed-form flow and deterministic first-hit event/root calculation.

**Horizon / resolution**

Search interval fixed to `[0, 2*pi*e + 1]`; no timestep scan.

**Tolerance**

N1 on first event time.

**Pass rule**

First event must equal `2*pi*e` within N1 and no earlier crossing may exist.

**Expected failure modes**

Wrong threshold branch, wrapped-phase reset changing elapsed time, or event not treated as first hitting.

#### BC05-B — registered linear analytical variant

Use V-S2 with

\[
\gamma=1,\qquad \Theta=-1,\qquad \psi=0,\qquad \theta(0)=0.
\]

Reference:

\[
\theta(t)=t,\qquad T_0=2\pi.
\]

Use the same N1 event-time rule.

---

### BC06 — delayed-autapse period identity

**Frozen target:** D8–D9.  
**Classification:** E0 identity + N2 residual/event check.  
**Epistemic target:** PROPOSITION / PROVED under stated assumptions.

**Model / variant**

One-neuron delayed autapse with normalized alpha kernel and registered linear response V-S2.

**Fixed parameters**

\[
w=1,\qquad \gamma=\pi,\qquad \Theta=-1.
\]

Therefore

\[
T_{ref}=\pi.
\]

The exact predetermined finite cases are

\[
\alpha\in\{0.2,2,20\},
\qquad
\tau\in\{0,\pi/3,3\pi/2\}.
\]

All nine Cartesian-product cases are part of the contract; none may be dropped after execution.

**Initial/history conditions**

Exact periodic spike history `T^m=m*pi` for all times needed to cover the largest delay; phase is set to `0` at the reference spike at `t=0`.

**Observables**

1. period residual
\[
F=\int_0^\pi S_L(R_\pi(s-\tau))ds-2\pi;
\]
2. next first-hitting time.

**Independent reference**

\[
F=0,
\qquad T=\pi.
\]

**Method class**

Closed-form periodic comb plus deterministic quadrature for the residual; deterministic event/root calculation for first hitting.

**Horizon / resolution**

One cycle `[0,pi]`; quadrature stopping tolerances fixed at `1e-13` absolute and relative.

**Tolerance**

N2 for `F`; N1 for event time.

**Pass rule**

All nine cases must satisfy both tolerances. A subset pass is a benchmark FAIL.

**Admissibility / transversality**

For these parameters the comb is nonnegative and

\[
S_L(x)=\pi x+1>0,
\]

so accumulated phase is strictly increasing and first hitting is unique/transversal.

**Expected failure modes**

Delay applied with the wrong sign, insufficient prespike history, kernel area not equal to one, or spurious alpha/delay dependence in the linear existence period.

---

### BC07 — phase-locked self-consistency and global gauge

**Frozen target:** D10–D12.  
**Classification:** E0 structural identity + N2 residual/gauge check.  
**Epistemic target:** PROPOSITION / PROVED.

**Model / variant**

Two-neuron fixed-delay graph with alpha synapses and linear response V-S2.

**Parameters**

\[
W=
\begin{pmatrix}
0.7&0.3\\
0.4&0.6
\end{pmatrix},
\qquad
\gamma=\pi,
\qquad
\Theta=-1,
\qquad
\alpha=2,
\qquad
T=\pi.
\]

Offsets:

\[
\phi_1=0,
\qquad
\phi_2=\pi/4.
\]

Fixed delays:

\[
(\tau_{ij})=
\begin{pmatrix}
0&\pi/6\\
\pi/3&\pi/5
\end{pmatrix}.
\]

Gauge-shift test value:

\[
c=0.37\pi.
\]

**Initial/history conditions**

Exact periodic spike trains `T_i^m=mT+phi_i` and the corresponding analytical alpha history.

**Observable**

For each neuron,

\[
R_i=\int_0^T S_L\!\left(\sum_jw_{ij}R_T(s+\phi_i-\phi_j-\tau_{ij})\right)ds-2\pi.
\]

Evaluate once at `(phi_1,phi_2)` and once at `(phi_1+c,phi_2+c)`.

**Independent reference**

Because both row sums equal one and D2 holds,

\[
R_1=R_2=0,
\]

and the residual vector is exactly gauge invariant.

**Method class**

Closed-form periodic comb and deterministic quadrature.

**Horizon / resolution**

One cycle `[0,pi]`; quadrature stopping tolerances `1e-13` absolute and relative.

**Tolerance**

N2 for each residual; absolute difference between unshifted and shifted residual vectors `<=1e-11` componentwise.

**Pass rule**

Both residuals must meet N2 before and after the gauge shift, and the residual vectors must meet the gauge-difference threshold.

**Admissibility / transversality**

All weights are positive and `S_L=pi*psi+1>0`, so the reference cycle is strictly increasing in phase.

**Expected failure modes**

Wrong sign in `phi_i-phi_j`, wrong delay sign, failure to impose periodic history, or gauge-dependent implementation of the existence equations.

---

### BC08 — linear row-sum identity: unbalanced and balanced cases

**Frozen target:** D13–D15.  
**Classification:** E0 + N1/N2.  
**Epistemic target:** PROPOSITION / PROVED under V-S2 assumptions.

#### BC08-A — unbalanced row sum

Use

\[
W=
\begin{pmatrix}
0.7&0.3\\
0.4&0.6
\end{pmatrix},
\qquad \Gamma=1,
\qquad \gamma=\pi,
\qquad \Theta=-1.
\]

Reference:

\[
T=\pi.
\]

#### BC08-B — balanced row sum

Use

\[
W=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix},
\qquad \Gamma=0,
\qquad \gamma=1,
\qquad \Theta=-1.
\]

Reference:

\[
\psi_i(t)=0,
\qquad T=2\pi.
\]

For each subcase execute the following fixed dimensionless alpha/delay pairs:

1. `alpha*T = 0.5`, `tau/T = 0`;
2. `alpha*T = 2*pi`, `tau/T = 0.5`;
3. `alpha*T = 20`, `tau/T = 1.5`.

Here `alpha` and `tau` are derived from the subcase reference `T`; these are three fixed regression cases, not a scan.

**Initial/history conditions**

Exact synchronous periodic spike history and corresponding alpha state.

**Observables**

One-cycle phase increment, first-hitting period, and in BC08-B the synchronous input cancellation residual.

**Independent references**

D14 for BC08-A, D15 for BC08-B, and exact cancellation in the balanced synchronous geometry.

**Method class**

Closed-form periodic alpha history plus deterministic phase integration / first-hit calculation.

**Horizon / resolution**

One reference period per case.

**Tolerance**

N1 on period; N2 on phase-increment residual and balanced input cancellation.

**Pass rule**

All six fixed cases must pass. No claim of general stability is made.

**Admissibility requirements**

The unbalanced positive-row-sum case uses positive input and positive `S_L`; the balanced synchronous case has `S_L(0)=1`; both are transversal.

**Expected failure modes**

Row/column convention reversal, nonperiodic delay initialization, failure of exact cancellation, or unintended dependence of the linear existence period on alpha/delay.

---

### BC09 — first-hitting / admissibility condition

**Frozen target:** C8 and D16–D17.  
**Classification:** E0 + L0 logical event test.  
**Epistemic target:** LEMMA / PROVED.

**Model**

Same baseline isolated clock as BC05-A:

\[
r=1,\qquad h=-1,\qquad \psi=0,
\qquad S(0)=e^{-1}.
\]

**Positive reference**

\[
A(t)=e^{-1}t,
\qquad T=2\pi e.
\]

**Positive pass condition**

The implementation must establish

\[
A(T)=2\pi
\]

within N1 and must return no crossing on the open interval `(0,T)`.

**Negative control**

Present the candidate period

\[
T_{bad}=2\pi e+1.
\]

Since the first crossing already occurred at `2*pi*e`, `T_bad` must be rejected as an admissible next-event period even though a later phase section may exist.

**Method class**

Closed-form accumulated phase plus first-hit logic.

**Horizon / resolution**

`[0,T_bad]`.

**Tolerance**

N1 on the equality at the true hit; L0 on accepting/rejecting candidate periods.

**Pass rule**

PASS iff the true period is accepted and the negative-control candidate is rejected specifically because first hitting occurred earlier.

**Expected failure modes**

Treating any section crossing as the designated next event, checking only the endpoint equality, or ignoring the first-hitting convention.

---

### BC10 — elementary event-time perturbation under transversality

**Frozen target:** C10 and D18.  
**Classification:** E0 + N1 exact-event sensitivity test.  
**Epistemic target:** LEMMA / PROVED.

**Model**

Baseline isolated clock from BC05-A with constant velocity

\[
v=S(0)=e^{-1}>0.
\]

**Reference event**

At unperturbed initial phase `theta(0)=0`,

\[
T=2\pi e.
\]

**Perturbations**

Use exactly

\[
\varepsilon\in\{+10^{-4},-10^{-4}\}
\]

as initial phase perturbations, with no other state change.

**Independent reference**

The event time is exactly

\[
T(\varepsilon)=\frac{2\pi-\varepsilon}{v},
\]

so

\[
\delta T=-\frac{\varepsilon}{v}=-e\varepsilon.
\]

In this constant-velocity case the frozen first-order identity is exact for the chosen perturbation.

**Observable**

Next first-hitting time for both perturbation signs.

**Method class**

Deterministic event/root calculation compared with the exact closed form.

**Horizon / resolution**

Search interval `[0,2*pi*e+1]`.

**Tolerance**

N1 on both perturbed event times and on `delta T`.

**Pass rule**

Both signs must pass N1 and preserve the same regular event section.

**Transversality negative control**

Set instead `h=0`, `r=1`, `psi=0`. Then `S(0)=0`; the isolated neuron has no finite next event and D18 is undefined because the denominator vanishes. The implementation must return an explicit non-transversal/no-event status and must **not** divide by zero or manufacture a derivative.

**Expected failure modes**

Sign error in D18, differentiating a non-transversal event, or silently returning finite sensitivity when `dot(theta)=0`.

---

## 6. Tolerance rationale table

| Class | Values | Applies to | Rationale fixed before execution |
|---|---|---|---|
| E0 | exact | symbolic/algebraic identities | these are mathematical identities, not numerical estimates |
| N1 | `atol=1e-12`, `rtol=1e-10` | closed-form states, event times, scalar reference quantities | safely above binary64 rounding while still far below scientific scales in the fixed cases; consistent with the legacy order-of-magnitude target without inheriting legacy PASS status |
| N2 | `atol=1e-10`, `rtol=1e-10` | quadrature residuals, periodic closure, cancellation residuals | allows deterministic quadrature/root accumulation while remaining stringent relative to order-one/`2*pi` references |
| L0 | exact Boolean | first-hitting, admissibility, transversality rejection | event semantics are categorical; they must not be softened post hoc |

Quadrature internal stopping tolerances are fixed at `1e-13` absolute and relative where specified. These are **method tolerances**, not acceptance tolerances.

A benchmark failure must not be repaired by loosening N1/N2 in the same gate. Any tolerance change requires a new authorized contract revision with rationale independent of the failed output.

---

## 7. Symbolic vs numerical classification

| Benchmark | Symbolic/algebraic component | Future numerical component |
|---|---|---|
| BC01 | primary | none required |
| BC02 | closed-form derivation | pointwise state comparison |
| BC03 | comb formula and unit mass | pointwise comb + quadrature |
| BC04 | periodic-state formulas | one-cycle flow/closure |
| BC05 | isolated-clock formula | first-event location |
| BC06 | autapse period identity | nine fixed residual/event cases |
| BC07 | phase-locked/gauge identity | fixed residual/gauge case |
| BC08 | row-sum formulas | six fixed synchronous cases |
| BC09 | first-hitting logic | positive + negative-control event test |
| BC10 | D18 formula | two perturbations + transversality negative control |

The symbolic result and the numerical implementation test are logically distinct. A symbolic identity may be correct even if a future implementation benchmark fails.

---

## 8. Admissibility / transversality requirements

The following rules are global to the contract:

1. A period residual is not sufficient by itself; any benchmark claiming a next event must also satisfy first hitting D16–D17.
2. Any event-time derivative test requires C10 / D18 transversality.
3. A non-transversal or no-event case is **not** repaired by regularization inside this benchmark layer; it must be reported as outside the derivative chart.
4. Delayed tests require exact periodic prespike history over the full delay window.
5. Gauge tests alter all phase offsets by the same constant and must not alter the phase-locked residual.
6. Linear-response benchmarks are explicitly V-S2 analytical-variant tests, not silent replacements of the frozen baseline response C2.
7. The benchmark contract tests existence/event semantics only where stated; it makes no stability claim.

---

## 9. Deferred legacy items

The following recovered v0.2 items are intentionally not canonicalized in this benchmark contract:

### DFR-01 — legacy B5 two-cell mode decomposition

Reason: not among frozen D1–D18 benchmark identities. It belongs with later stability/Floquet canonicalization.

### DFR-02 — legacy B6 modal flow matrix

Reason: modal variational flow is outside RB-004.

### DFR-03 — legacy B7 saltation matrix

Reason: the generic saltation matrix is not frozen. Only the elementary event-time perturbation identity D18 is currently canonical.

### DFR-04 — legacy B9 slow-synapse modal roots

Reason: slow-synapse stability asymptotics are explicitly listed only as future source-supported targets.

### DFR-05 — legacy B10 delay-induced imaginary-axis algebra

Reason: depends on the unfrozen slow-synapse characteristic equation.

### DFR-06 — legacy open-ended parameter sweeps

Any wording such as “arbitrary alpha/delay” or “random positive parameters” is replaced by symbolic domains or fixed finite regression cases. No benchmark may choose points after inspecting effects.

### DFR-07 — implementation-specific surrogate tolerances

Fixed-step, low-precision, smooth-surrogate or JAX-specific tolerances are not part of this first exact analytical contract. They require their own later implementation contract.

---

## 10. Gate decision

\[
\boxed{\text{PASS}}
\]

Reason:

1. every retained benchmark is traceable to RB-004 baseline definitions or D1–D18;
2. all parameter values, finite test sets, histories, observables, references, method classes and acceptance thresholds are fixed before execution;
3. exact symbolic checks are separated from future numerical checks;
4. first-hitting and transversality requirements are explicit;
5. legacy stability/saltation/slow-synapse material outside the freeze is deferred rather than silently promoted;
6. no benchmark has been executed and no legacy output was used as validation evidence.

PASS means only that MASTER can decide whether to freeze this contract.

---

## 11. Proposed contents for `CORE Benchmark Contract Freeze 0.1`

If MASTER accepts this gate, the proposed freeze should contain exactly:

1. contract-wide execution conventions in Section 4;
2. benchmark definitions BC01–BC10 in Section 5;
3. tolerance classes E0, N1, N2 and L0 in Section 6;
4. symbolic-vs-numerical separation in Section 7;
5. admissibility/transversality rules in Section 8;
6. deferred-item boundary DFR-01 through DFR-07 in Section 9.

The freeze must explicitly state that **no benchmark has yet passed**, because no benchmark execution has occurred.

---

## 12. Exact next permissible execution gate after MASTER freeze

If and only if MASTER establishes `CORE Benchmark Contract Freeze 0.1`, the exact next scientific execution gate proposed is:

`CORE v0.2 Benchmark Execution Gate 0.1`

Its sole purpose would be to execute BC01–BC10 exactly as frozen, without changing parameters, histories, grids, quadrature tolerances, acceptance tolerances or pass/fail rules.

That gate is **not executed here** and is not automatically authorized by this PASS.

---

## 13. STOP

No benchmark was executed. No v0.3+ theory, implementation, active design, inference, optimization or v0.27 work was started.

STOP — RETURN TO MASTER
