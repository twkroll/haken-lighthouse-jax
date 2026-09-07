# CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — PRE-EXECUTION VALIDATION CONTRACT COMPLETE; NO V0.3 VALIDATION EXECUTED

## 1. Git / provenance identity

This gate constructs a finite pre-execution validation contract for the algorithmic / C2 layer implied by `CORE v0.3 Continuation Theory Freeze 0.1` (RB-007).

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `c910856bd4d5125840d4068d4edc3e6b6831a6ab`
- governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `9627005724d961c28e8b63d80c3430a1d0805484`
- MASTER STATUS start blob SHA: `7e733d2eb08ae506aad997061a46759000a5e3ed`
- project status v1.5 blob SHA: `44315d22f2ffe23476d0e75e503f95b37bae9053`
- decision log blob SHA: `3af22e697ab53b6eaff0d6d713b6d8c784851efa`
- authorizing prompt blob SHA: `1d59e8f1fd4abda5f8cbc5d4b88f6878e9fdcb1b`
- RB-004 mathematical freeze blob SHA: `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- RB-005 benchmark-contract freeze blob SHA: `ddf8d56099f392fbadfff30d7c4246831fb5cec7`
- RB-006 v0.2 result-freeze blob SHA: `276c74a74d531a947e50c8661e9a068aca41918c`
- RB-007 v0.3 continuation-theory freeze blob SHA: `9ba55b855b3257d11e9fc741ea19a0e2deacc329`
- RB-007 frozen source blob SHA: `7c04401994b749f7918ff74c8e27339bcaf3d3c7`

Historical candidate input is read-only recovery evidence at commit:

`287eae8a86560b78ed94f30a2786243714c33ac0`

with:

- `docs/core/continuation_contract_v0.3.md`, blob `d3507c7a5e9e44f3c81e5cb61d8ae835448a8235`;
- `docs/core/continuation_bifurcations_v0.3.md`, blob `14a809ee9257a8e1b57a4aa03778eeb0221e0e58`.

Legacy B11–B22 are candidate test ideas only. No legacy v0.3 numerical output, tolerance recommendation, critical point or effect-bearing branch location is accepted as evidence in this contract.

**No validation in this document has been executed.**

---

## 2. Frozen-authority map

| Rollback point | Authority in this contract | Not imported |
|---|---|---|
| RB-004 | baseline Lighthouse equations, alpha kernel, fixed delays, event semantics, registered analytical variants, D1–D18 | downstream continuation / stability claims |
| RB-005 | governance precedent for pre-execution finite cases, frozen tolerances and no post-output repair | BC01–BC10 membership is not reused as v0.3 evidence except where explicitly cited as a regression source |
| RB-006 | governed PASS of BC01–BC10; event / alpha / phase-locking baseline already validated | no v0.3 continuation result |
| RB-007 | normalized coordinates, branch operator, phase Jacobian, fixed-physical-delay period derivative, scalar-parameter derivative, gauge, pseudo-arclength algebra, event/chart taxonomy, exchange-symmetric block structure and corrected negative `B` | no numerical continuation, no Lighthouse fold/pitchfork, no v0.4 Floquet object, no unconditional higher regularity |

RB-004 through RB-007 are unchanged by this gate.

---

## 3. Legacy B11–B22 inclusion / exclusion matrix

| Legacy ID | Topic | Canonical disposition |
|---|---|---|
| B11 | dimensional vs normalized coordinates / gauge | RETAIN / REPAIR as V3C01 |
| B12 | branch Jacobian | RETAIN only at one fixed noncritical smooth-reference state as V3C02 |
| B13 | pseudo-arclength fold traversal | RETAIN synthetic fold only as V3C04; Lighthouse fold part DEFER |
| B14 | two-cell block structure / `B` | RETAIN / REPAIR as V3C05 |
| B15 | pitchfork | RETAIN synthetic algebra only as V3C06; Lighthouse pitchfork DEFER |
| B16 | existence/stability classifier | DEFER to v0.4 because Floquet/multiplier objects are not frozen |
| B17 | transversality scaling | RETAIN elementary event part only as V3C07; saltation/Floquet part DEFER |
| B18 | arrival-aware handling | RETAIN / REPAIR as V3C08 with RB-007 chart qualification |
| B19 | threshold contact | DEFER; frozen baseline response is smooth at threshold |
| B20 | implicit branch sensitivity | RETAIN only on exact regular autapse branch as V3C09 |
| B21 | adaptive-delay commensurability | DEFER |
| B22 | first-hitting admissibility | RETAIN / REPAIR inside V3C07 |

No B11–B22 validation is executed here.

---

## 4. Contract-wide execution conventions

### 4.1 Precision and determinism

All numerical execution must use IEEE-754 binary64 / float64. Randomness is forbidden. No stochastic initialization, optimizer, parameter search, adaptive design or effect-strength selection is permitted.

### 4.2 Periodic alpha waveform

For alpha-kernel tests use

\[
\eta_\alpha(t)=\alpha^2 t e^{-\alpha t}H(t),\qquad \alpha>0.
\]

The periodic comb is evaluated by an exact closed-form / periodic-state representation derived from RB-004. A permitted independent waveform path is the exact periodic `(a,q)` state with

\[
q^+=\frac{\alpha^2}{1-e^{-\alpha T}},\qquad
 a^+=\frac{\alpha^2 T e^{-\alpha T}}{(1-e^{-\alpha T})^2},
\]

followed by exact between-arrival flow. No finite warm-up is allowed.

### 4.3 Arrival-aware integration

Every integral involving `R_T'` or a moving alpha arrival must be split at all analytically known arrival phases inside the integration interval. Direct differentiation through a wrapped `mod` expression is not an accepted reference calculation.

For all contract quadratures, internal absolute and relative stopping tolerances are fixed at

`epsabs = 1e-13`, `epsrel = 1e-13`.

### 4.4 Fixed five-point finite-difference stencil

Whenever this contract requests an independent derivative reference, use exactly

\[
D_h f(x)=\frac{-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}.
\]

No step-size scan or post-output step selection is permitted.

Fixed derivative steps are:

- normalized phase: `h_chi = 1e-5`;
- physical period: `h_T = 1e-4`;
- scalar coupling parameter: `h_p = 1e-5`;
- synthetic/analytic branch weight sensitivity: `h_w = 1e-4`;
- arrival-shift derivative: `h_a = 1e-5`.

### 4.5 Tolerance classes

For a numerical comparison to reference `x_ref`, use

\[
|x-x_{ref}|\le a_{tol}+r_{tol}|x_{ref}|.
\]

Frozen classes for this contract are:

- **E0** — exact symbolic/algebraic equality; no numerical tolerance.
- **V3-N1** — closed-form scalar/vector quantities: `a_tol=1e-12`, `r_tol=1e-10`.
- **V3-N2** — integrated residual / invariant quantity: `a_tol=1e-10`, `r_tol=1e-10`.
- **V3-D1** — analytic derivative versus fixed five-point independent derivative: `a_tol=5e-7`, `r_tol=5e-6`.
- **V3-A1** — synthetic continuation corrector residual: Euclidean residual `<=1e-10`; Newton stopping target `<=1e-12`.
- **L0** — exact Boolean / categorical logic.

No tolerance may be relaxed after output inspection.

### 4.6 PASS / FAIL / INVALID

- `PASS`: every required subcase satisfies its frozen rule.
- `FAIL`: any scientifically valid required case violates its rule.
- `INVALID`: only where this contract explicitly designates a derivative chart as mathematically undefined; INVALID must not hide an ordinary failure.

A failed case may not be dropped, replaced, softened, rerun with new parameters or reclassified after inspection.

### 4.7 Software-plumbing defects

A minimal validation harness may be corrected only for a clerical / software-plumbing defect that leaves every scientific specification above unchanged. The defect, correction and invalidated preliminary output must remain in the audit trail. After such a correction the affected validation family, and any family sharing the defective code path, must be rerun from the beginning under the unchanged frozen contract.

---

## 5. Fixed common Lighthouse reference state R0

V3C01–V3C03 use one predetermined **reference evaluation state**, not a claimed locked branch and not a searched critical point.

Model: RB-004 smooth baseline response and alpha synapses.

\[
r=1,\qquad h=-1,\qquad \alpha=2,
\]

\[
T=\pi,\qquad (\chi_1,\chi_2)=(0,0.23),
\]

\[
W=\begin{pmatrix}0.8&0.35\\0.45&0.75\end{pmatrix},
\qquad
\tau=\begin{pmatrix}0.3&0.7\\1.2&0.9\end{pmatrix}.
\]

External drive is zero.

The corresponding wrapped arrival phases are fixed by RB-007 (V3.25):

- `a11 = 0.3/pi = 0.0954929658551372`;
- `a12 = 0.23 + 0.7/pi = 0.4528169203286535`;
- `a21 = -0.23 + 1.2/pi = 0.1519718634205488`;
- `a22 = 0.9/pi = 0.2864788975654116`.

The minimum distance to a cycle boundary is `0.0954929658551372`; same-receiver arrival separations are `0.3573239544735163` and `0.1345070341448628`. All V3C02/V3C03 finite-difference stencil points must report minimum arrival-chart margin `>=0.05`. Failure of this predeclared margin is a benchmark FAIL, not a reason to select another point.

Because all weights and alpha activity are nonnegative while `h=-1`, the baseline response is on its positive smooth branch for this fixed reference state.

---

## 6. V3C01 — coordinate equivalence and global gauge

**Target:** RB-007 (V3.1)–(V3.9), (V3.21).

Use R0.

### 6.1 Dimensional / normalized equivalence

Construct

\[
\phi_i=T\chi_i,
\]

and evaluate both:

\[
F_i^{(\phi)}=\int_0^T S\!\left(\sum_jw_{ij}R_T(s+\phi_i-\phi_j-\tau_{ij})\right)ds-2\pi,
\]

and

\[
F_i^{(\chi)}=T\int_0^1 S\!\left(\sum_jw_{ij}R_T(T(\sigma+\chi_i-\chi_j)-\tau_{ij})\right)d\sigma-2\pi.
\]

Reference: exact equality by change of variables.

Rule: componentwise V3-N2.

### 6.2 Gauge test

Before gauge fixing, evaluate normalized `F` at `chi=(0,0.23)` and at

\[
\chi+c\mathbf 1,\qquad c=0.37.
\]

Reference: exact equality.

Rule: componentwise V3-N2.

**V3C01 PASS** iff both subtests pass; otherwise FAIL.

---

## 7. V3C02 — phase-Jacobian and gauge-null validation

**Target:** RB-007 (V3.10)–(V3.13).

Use R0 with gauge `chi_1=0`.

### 7.1 Gauge-fixed phase column

Compute the analytic column `partial F / partial chi_2` from (V3.12), using arrival-split integration.

Independent reference: V3 five-point derivative of the full normalized branch operator with `h_chi=1e-5`; every perturbed state must be fully reevaluated and all moving arrival splits recomputed.

Rule: V3-D1 on both vector components.

### 7.2 Ungauged null direction

Temporarily retain both phase coordinates and compute both analytic phase columns. Reference identity:

\[
D_\chi F\,\mathbf1=0.
\]

Rules:

- analytic column sum: componentwise V3-N2 to zero;
- independent five-point numerical columns: their sum must satisfy componentwise `|sum|<=5e-7`;
- the implementation must not obtain the null identity by explicitly zeroing the sum after evaluation.

### 7.3 Chart condition

All stencil points must satisfy the frozen `>=0.05` arrival-chart margin from R0.

**V3C02 PASS** iff all derivative, null and chart conditions pass.

---

## 8. V3C03 — fixed-physical-delay period derivative and scalar parameter derivative

**Target:** RB-007 (V3.14)–(V3.20).

Use R0.

### 8.1 Period derivative

Compute analytic `partial F / partial T` from (V3.15)–(V3.16).

Independent reference: fixed five-point derivative with `h_T=1e-4`.

**Frozen derivative convention:** at all four perturbed `T` values:

- `chi=(0,0.23)` is unchanged;
- `alpha=2` is unchanged;
- every physical delay entry `tau_ij` is unchanged exactly;
- `W,r,h` are unchanged;
- `R_T` and all arrival locations are recomputed for the perturbed physical period.

Rule: V3-D1 componentwise.

L0 negative control: if any harness rescales a delay to keep `tau/T` fixed, V3C03-A is FAIL even if a numerical derivative happens to be close.

### 8.2 Scalar coupling parameter

Define one scalar parameter by

\[
w_{12}(p)=0.35+p,
\qquad p_0=0,
\]

with all other quantities fixed.

Compute analytic `partial F / partial p` from (V3.19)–(V3.20) and compare with the fixed five-point derivative using `h_p=1e-5`.

Rule: V3-D1 componentwise.

All stencil points must retain arrival-chart margin `>=0.05`.

**V3C03 PASS** iff both derivative subtests and the fixed-physical-delay logic pass.

---

## 9. V3C04 — pseudo-arclength machinery on a synthetic fold only

**Target:** RB-007 (V3.22)–(V3.24) as a method definition.

No Lighthouse branch is used.

Synthetic equation:

\[
F_s(x,p)=x^2-p=0.
\]

Start exactly at

\[
(x_0,p_0)=(0.4,0.16).
\]

Initial unit tangent is oriented toward decreasing `x`:

\[
t_0=\frac{(-1,-0.8)}{\sqrt{1+0.8^2}}.
\]

Execution contract:

- fixed arclength step `Delta s=0.05`;
- exactly 20 predictor/corrector steps;
- no adaptive step reduction or enlargement;
- corrector Newton system is exactly the 2x2 augmented system from RB-007;
- Newton stopping target `||G||_2<=1e-12`;
- maximum 12 Newton iterations per step;
- tangent is recomputed from the exact nullspace condition and sign-oriented by positive dot product with the previous tangent.

Exact fold control at `(x,p)=(0,0)`: with fold tangent `(-1,0)`, the augmented Newton matrix is

\[
\begin{pmatrix}0&-1\\-1&0\end{pmatrix},
\]

which is nonsingular. This is an E0 check.

PASS requires:

1. E0 augmented-fold nonsingularity;
2. all 20 corrected points converge within 12 iterations;
3. every corrected point has `|x^2-p|<=1e-10`;
4. the sequence starts with `x>0` and contains at least one later accepted point with `x<0`;
5. no step is discarded or resized.

Failure of any item is V3C04 FAIL. No conclusion about a Lighthouse fold follows from PASS.

---

## 10. V3C05 — exchange-symmetric two-cell parity, block structure and corrected `B`

**Target:** RB-007 (V3.29)–(V3.31).

Use the smooth baseline response and alpha kernel with

\[
r=1,\quad h=-1,\quad \alpha=2,\quad T=\pi,
\]

\[
w_s=0.8,\qquad w_c=0.35,
\qquad \tau_s=0.3,\qquad \tau_c=0.7.
\]

This is a fixed **reference evaluation state**, not a claimed locked solution or pitchfork.

### 10.1 Parity

At `chi_test=0.07`, evaluate `F_+,F_-` at `+chi_test` and `-chi_test`.

References:

\[
F_+(T,-\chi)=F_+(T,\chi),
\qquad
F_-(T,-\chi)=-F_-(T,\chi).
\]

Rule: V3-N2.

### 10.2 Block structure at synchrony

At `chi=0`, evaluate:

- `F_-(T,0)`;
- `partial_chi F_+(T,0)` by fixed five-point stencil with `h_chi=1e-5`;
- `partial_T F_-(T,0)` by fixed five-point stencil with `h_T=1e-4` and physical delays fixed.

References: all three are zero by parity. Rules: V3-N2 for `F_-`; absolute derivative magnitude `<=5e-7` for the two numerical off-diagonal derivatives.

### 10.3 Corrected antisymmetric coefficient

Compute

\[
B_{analytic}=-T^2w_c\int_0^1 S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma,
\]

with arrival-split integration.

Independent reference:

\[
B_{FD}=\partial_\chi F_-(T,0)
\]

from the frozen five-point stencil.

Rule: V3-D1.

E0 sign audit: the symbolic chain rule must retain the **negative** prefactor for `B`. A positive-sign implementation fails the E0 audit even if a special numerical cancellation occurs.

**V3C05 PASS** iff parity, block structure, coefficient comparison and E0 sign audit all pass. No Lighthouse pitchfork claim is made.

---

## 11. V3C06 — synthetic pitchfork algebra only

**Target:** limited synthetic validation of the algebraic parity / square-root structure. It does not validate baseline `C^3` regularity or a Lighthouse pitchfork.

Synthetic system:

\[
F_+(T,\chi,p)=T-1,
\qquad
F_-(T,\chi,p)=\chi(p-\chi^2).
\]

E0 references:

- `F_+` is even in `chi`;
- `F_-` is odd in `chi`;
- synchronous branch `chi=0` exists for all `p`;
- at `p=0`, the antisymmetric linear coefficient vanishes;
- reduced coefficients are `a=1`, `b=-1`;
- nontrivial branches satisfy exactly `chi^2=p` for `p>0`.

Finite numerical cases:

\[
p\in\{10^{-4},10^{-3},10^{-2}\},
\qquad T=1,
\qquad \chi=\pm\sqrt p.
\]

At all six points require both residual components to satisfy V3-N1 to zero and `chi^2-p` to satisfy V3-N1.

**V3C06 PASS** iff all E0 and finite cases pass. Any inference about a Lighthouse pitchfork is forbidden.

---

## 12. V3C07 — first-hitting and transversality regression

**Target:** RB-004 D16–D18 and RB-007 (V3.26)–(V3.27).

Use the isolated smooth-baseline clock already frozen / validated beneath RB-007:

\[
r=1,\qquad h=-1,\qquad \psi=0,
\qquad v=S(0)=e^{-1}.
\]

Positive reference:

\[
T_0=2\pi e.
\]

Required checks:

1. deterministic first-hit calculation on `[0,T_0+1]` returns `T_0` within V3-N1;
2. normalized accumulated phase is `<2pi` for all `0<=sigma<1` by monotonicity and equals `2pi` at `sigma=1` within V3-N1;
3. candidate `T_bad=T_0+1` is rejected by L0 because first hitting occurred earlier.

Transversality negative control:

Set instead

\[
h=0,\qquad r=1,\qquad \psi=0.
\]

Then `S(0)=0`. Required classification is exactly `NON-TRANSVERSAL / NO-EVENT`; no finite derivative or event time may be manufactured.

The negative control is a valid L0 control, not an ordinary numerical failure.

**V3C07 PASS** iff all positive, premature-event and nontransversal controls behave exactly as specified.

---

## 13. V3C08 — arrival-aware integration and chart-boundary qualification

**Target:** RB-007 Section 8, especially (V3.25), and the canonical repair that an alpha arrival-chart change is not automatically an existence singularity.

Use one normalized alpha comb with

\[
\alpha=2,\qquad T=\pi.
\]

For dimensionless unwrapped arrival shift `a`, define

\[
J(a)=\int_0^T R_T(s-aT)ds.
\]

Finite shifts are fixed as

\[
a\in\{-10^{-3},0,+10^{-3},0.4\}.
\]

Reference for every case:

\[
J(a)=1
\]

by unit mass over one period.

Execution rules:

- split quadrature at the wrapped arrival `a mod 1` when it lies inside the open interval;
- record both unwrapped and wrapped arrival coordinates;
- do not infer physical singularity merely because the wrapped representative changes from near `1` to near `0`.

Rules:

1. all four `J(a)` values satisfy V3-N2 to `1`;
2. at `a=-1e-3`, `+1e-3` and `0.4`, evaluate `dJ/da` by the fixed five-point stencil `h_a=1e-5`; reference is zero, absolute error `<=5e-7`;
3. at exactly `a=0`, the pointwise classical `R_T'` at the arrival kink is not a valid single-sided point derivative. A request for that pointwise derivative must return the categorical status `ARRIVAL_CHART_BOUNDARY / DERIVATIVE_INVALID` rather than a fabricated centered point derivative;
4. despite item 3, `J(0)` remains a valid integrated quantity and must pass item 1.

Item 3 is the only case-level INVALID classification in V3C08 and cannot be used to hide a failed integrated check.

**V3C08 PASS** iff all integrated, off-boundary derivative and chart-classification requirements pass.

---

## 14. V3C09 — implicit branch sensitivity at an exact regular autapse branch

**Target:** RB-007 regular-branch IFT / implicit sensitivity logic, without adaptive delays or searched critical points.

Use registered linear analytical response V-S2:

\[
S_L(\psi)=\gamma\psi-\Theta,
\qquad \gamma=\pi,
\qquad \Theta=-1.
\]

One-neuron autapse:

\[
\alpha=2,\qquad w=1,
\qquad \tau=\pi/3,
\qquad T=\pi.
\]

Use exact periodic alpha history. Because the alpha comb has unit mass over a cycle,

\[
F(T,w)=\pi w+T-2\pi.
\]

Thus at the reference point:

\[
F_T=1,
\qquad F_w=\pi,
\qquad \frac{dT_*}{dw}=-\pi.
\]

This is a regular branch because `F_T=1`.

### V3C09-A — weight sensitivity

Compute `-(F_T)^{-1}F_w` from the implementation and compare to `-pi` with V3-N1.

Independent branch reference uses the exact finite pair

\[
w_-=1-10^{-4},\qquad w_+=1+10^{-4},
\]

with

\[
T_*(w)=2\pi-\pi w.
\]

Centered branch slope using `h_w=1e-4` must equal `-pi` within V3-N1.

### V3C09-B — fixed-delay sensitivity

At fixed `w=1`, use

\[
\tau_-=\pi/3-10^{-4},\qquad
\tau_+=\pi/3+10^{-4}.
\]

Reference branch period is `T=pi` for both because a full-period shift preserves comb mass. Therefore

\[
F_\tau=0,
\qquad dT_*/d\tau=0.
\]

Require V3-N2 on `F_tau` and V3-N1 on the centered branch-period sensitivity to zero.

Every subcase must preserve strict positive phase velocity `S_L=pi*psi+1>0`, so first hitting is unique.

**V3C09 PASS** iff both exact regular sensitivities pass.

---

## 15. Symbolic versus numerical / algorithmic separation

| ID | Exact / symbolic component | Later numerical / algorithmic component |
|---|---|---|
| V3C01 | coordinate-map and gauge identities | two equivalent integral implementations |
| V3C02 | analytic Jacobian and gauge null identity | fixed five-point independent derivative |
| V3C03 | derivative conventions | fixed five-point `T` / `p` comparisons |
| V3C04 | fold equation and augmented-fold nonsingularity | fixed-step pseudo-arclength traversal |
| V3C05 | exchange parity and negative `B` formula | parity / derivative / integral comparisons |
| V3C06 | synthetic pitchfork algebra | six fixed residual points |
| V3C07 | isolated-clock / transversality identities | deterministic first-hit / categorical controls |
| V3C08 | periodic mass and chart interpretation | split quadrature / off-boundary derivative checks |
| V3C09 | exact linear autapse branch / IFT derivative | fixed finite branch-sensitivity comparisons |

A correct symbolic identity does not rescue a failed numerical implementation test, and a numerical pass does not broaden RB-007 theory.

---

## 16. Complete suite rule

A later governed execution returns overall `PASS` only if **V3C01 through V3C09 all pass**, including every fixed subcase and negative control.

Any valid failed subcase makes the suite `FAIL`.

`CONDITIONAL` is reserved only for a genuine execution-completeness blocker that prevents a meaningful PASS/FAIL classification without changing this contract.

No case may be dropped or replaced after output inspection.

---

## 17. Deferred-item boundary

The following remain explicitly outside this contract:

- DFR-V3-01: any actual Lighthouse fold parameter/location or branch selected by search;
- DFR-V3-02: any actual Lighthouse pitchfork parameter/location/scaling;
- DFR-V3-03: any v0.4 Floquet multiplier, characteristic root, stability label or B16 classifier;
- DFR-V3-04: saltation-matrix scaling beyond RB-004 elementary event-time identity;
- DFR-V3-05: hard-threshold / Heaviside contact tests and `TH_GRAZE` for the smooth baseline;
- DFR-V3-06: adaptive delays, commensurability and slow-fast branch effects;
- DFR-V3-07: general symmetry/Fourier Floquet sectors;
- DFR-V3-08: production or JAX continuation performance;
- DFR-V3-09: exact-vs-surrogate continuation scientific agreement;
- DFR-V3-10: normal-form fitting or effect-bearing critical coefficients;
- DFR-V3-11: v0.4+ legacy recovery execution;
- DFR-V3-12: inference, observation design, active experiment design, applications, novelty, manuscript claims and v0.27.

No acceptance criterion for any deferred item is defined here.

---

## 18. Gate decision

\[
\boxed{\text{PASS}}
\]

Reason:

1. every retained test is tied directly to RB-004/RB-007 or to a clearly labelled synthetic algorithmic problem;
2. all model variants, graphs, parameters, reference states, derivative conventions, chart margins, finite cases, solver steps, tolerances, negative controls and PASS/FAIL rules are fixed before validation execution;
3. no Lighthouse critical point is searched, imported or selected;
4. the historical B11–B22 registry is repaired rather than copied wholesale;
5. v0.4 stability, hard-threshold, adaptive-delay and downstream effect-bearing work remain deferred;
6. no validation has been executed in this gate.

PASS means only that MASTER may decide whether to establish `CORE v0.3 Continuation Validation Contract Freeze 0.1`.

---

## 19. Proposed contents of `CORE v0.3 Continuation Validation Contract Freeze 0.1`

If MASTER authorizes the freeze, freeze exactly:

1. Sections 4–5 execution conventions and common reference state R0;
2. V3C01–V3C09 in Sections 6–14, including every subcase;
3. all fixed parameters, histories, derivative steps, chart margins and synthetic problems;
4. E0, V3-N1, V3-N2, V3-D1, V3-A1 and L0 tolerance classes;
5. arrival-aware integration and fixed-physical-delay conventions;
6. PASS / FAIL / INVALID semantics and software-plumbing audit rule;
7. the complete-suite rule;
8. DFR-V3-01 through DFR-V3-12 deferred boundary.

The freeze must explicitly state that all V3C01–V3C09 remain **UNEVALUATED** at freeze time.

---

## 20. Exact proposed later execution gate

If and only if MASTER freezes this contract, the proposed next execution gate is exactly:

`CORE v0.3 Continuation Validation Execution Gate 0.1`

Its permitted work would be only the deterministic execution of V3C01–V3C09 under the frozen contract, with a result record and return to MASTER. It must not include Lighthouse continuation search or v0.4 science.

---

## 21. Open questions

1. Whether MASTER accepts the proposed contract without repair and establishes the validation-contract freeze.
2. Whether later v0.3 effect-bearing Lighthouse fold/pitchfork confirmation should receive a separate preregistered contract after this C2 layer is validated.
3. Whether unconditional higher regularity of the exact alpha branch operator should be addressed before any Lighthouse-specific pitchfork normal-form gate.
4. Whether v0.4 stability canonicalization should precede or follow a later Lighthouse-specific continuation experiment; this is a MASTER sequencing decision.

---

## 22. STOP

No validation was executed. No numerical continuation was run. No B11–B22 legacy benchmark was executed. No v0.4+ or active-design work was started.

STOP — RETURN TO MASTER
