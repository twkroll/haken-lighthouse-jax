# CORE v0.3 Continuation Theory Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — NARROW CONTINUATION THEORY CANONICALIZED; NO NUMERICAL CONTINUATION OR B11+ EXECUTION

## 1. Provenance / input identity

This gate audits only the mathematically recoverable v0.3 continuation layer under the canonical frozen baseline and governed v0.2 validation result.

Canonical inputs:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `6150f512ad11c3e2bd2d7fb8093969f79fafc1c7`
- governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `7a769380440d2bf21ee6322cb8e3605d80b04b74`
- MASTER STATUS start blob SHA: `9cee2ff293423fe0d7b90df97d14b0f20662348e`
- project status v1.4 blob SHA: `84ad420478d4eb437bb8dbfd346918c3d9e4d245`
- decision log blob SHA: `fb9b3671eac397c76bdc55e0c377451287e5cec3`
- authorizing prompt blob SHA: `45db766111269f6bc7903385e608a4fb99af1801`
- `CORE Mathematical Freeze 0.1` / RB-004 blob SHA: `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- `CORE v0.2 Benchmark Result Freeze 0.1` / RB-006 blob SHA: `276c74a74d531a947e50c8661e9a068aca41918c`

Frozen legacy recovery input:

- exact recovery commit: `287eae8a86560b78ed94f30a2786243714c33ac0`
- legacy theory file blob SHA: `14a809ee9257a8e1b57a4aa03778eeb0221e0e58` — `docs/core/continuation_bifurcations_v0.3.md`
- legacy benchmark-registry blob SHA: `d3507c7a5e9e44f3c81e5cb61d8ae835448a8235` — `docs/core/continuation_contract_v0.3.md`

The frozen legacy tree contains the two v0.3 documents above but no standalone v0.3 reference script and no v0.3 benchmark JSON. Reference scripts / machine-readable benchmark outputs begin only at later versions. Thus there is no v0.3 executable object that can legitimately be called an exact replay target.

Legacy history also records an explicit erratum, commit `c2caf6e441b7d3b09f5243bcd96e9a13731ab0ff`, `CORE erratum: correct sign of two-cell B coefficient`, followed by a restore commit after a failed in-place edit. The recovery-snapshot formula is therefore treated as a candidate that requires independent derivation, not as self-authenticating evidence.

No numerical continuation, benchmark, fold/pitchfork search, multiplier computation, parameter scan or v0.4+ calculation was performed in this gate.

---

## 2. Legacy v0.3 claim inventory and audit disposition

| Legacy material | Audit disposition |
|---|---|
| normalized offsets `chi_i`, `phi_i=T chi_i` | retained and re-derived |
| gauge `chi_1=0`, unwrapped internal phases | retained and re-derived |
| normalized branch equations | retained, with baseline external drive set to zero |
| phase-coordinate branch Jacobian | retained and independently derived |
| period derivative | retained with explicit fixed-physical-delay convention and coordinate caveat |
| parameter derivative | retained in baseline-compatible form |
| comb period derivative | retained locally / almost-everywhere under stated convergence and arrival regularity |
| second/higher derivatives | conditional only; not blanket-frozen for the alpha branch operator |
| pseudo-arclength equations | retained as algebraic continuation definition; not executed |
| generic fold conditions | retained only as conditional standard local theory requiring sufficient smoothness |
| exchange-symmetric two-cell block structure | retained and independently derived |
| two-cell antisymmetric coefficient `B` | retained; corrected negative sign independently confirmed |
| pitchfork coefficients/scaling | algebraically correct under a `C^3` branch-operator assumption; baseline applicability deferred pending regularity/validation |
| existence-vs-dynamical-stability separation | retained as a strict conceptual rule; no v0.4 stability result imported |
| event transversality / first hitting | retained; consistent with RB-004 D16–D18 |
| threshold-contact nonsmoothness | qualified: not a nonsmooth boundary for frozen baseline response C2, which is smooth through threshold |
| arrival-order collision | qualified: an event-chart / representation boundary; not automatically an existence singularity of the integrated operator |
| adaptive-delay slow flow / commensurability | deferred; adaptive delay is outside RB-004 baseline |
| general group/Fourier symmetry, Floquet labels, surrogate continuation | deferred to v0.4+ / implementation gates |
| B11–B22 | registry only; no execution and no acceptance threshold adopted here |

---

## 3. Canonical notation and coordinate map

### 3.1 Dimensional v0.2 offsets

RB-004 freezes the one-spike-per-cycle phase-locked ansatz in dimensional offsets as

\[
T_i^m=mT+\phi_i,
\]

with input in neuron `i`'s local cycle coordinate `s in [0,T)`

\[
\Psi_i^{(\phi)}(s)=\sum_j w_{ij}
R_T(s+\phi_i-\phi_j-\tau_{ij}).
\]

The existence condition is

\[
2\pi=\int_0^T S\!\left(\Psi_i^{(\phi)}(s)\right)\,ds.
\]

### 3.2 Normalized coordinates

Define

\[
\boxed{\chi_i=\phi_i/T,\qquad \phi_i=T\chi_i,}
\tag{V3.1}
\]

and firing times

\[
\boxed{T_i^m=(m+\chi_i)T.}
\tag{V3.2}
\]

The physical phase offsets are defined modulo one cycle, but continuation coordinates are represented on the universal cover:

\[
\boxed{\chi_i\in\mathbb R\text{ internally; }\chi_i\bmod1\text{ only for display}.}
\tag{V3.3}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE / PROJECT CANONICALIZATION

The map (V3.1) is bijective for any fixed `T>0` between dimensional offsets modulo `T` and normalized offsets modulo `1`.

### 3.3 Gauge fixing

Uniform time translation acts by

\[
\chi_i\mapsto\chi_i+c\quad\forall i.
\]

Only differences `chi_i-chi_j` enter the branch equations below. Therefore one redundant coordinate is removed by

\[
\boxed{\chi_1=0.}
\tag{V3.4}
\]

and the canonical branch unknown is

\[
\boxed{z=(T,\chi_2,\ldots,\chi_N)\in(0,\infty)\times\mathbb R^{N-1}.}
\tag{V3.5}
\]

No dynamic Floquet claim is implied by this gauge fixing; it is only an existence-coordinate reduction.

---

## 4. Independent derivation of the normalized branch equations

Set

\[
s=T\sigma,\qquad 0\le\sigma<1,
\]

and substitute `phi_i=T chi_i` in the frozen v0.2 input. Define

\[
\boxed{
X_{ij}(\sigma;z,p)
=T(\sigma+\chi_i-\chi_j)-\tau_{ij}(p),
}
\tag{V3.6}
\]

and, for the RB-004 baseline with no external drive,

\[
\boxed{
\Psi_i(\sigma;z,p)=
\sum_j w_{ij}(p)R_T(X_{ij}(\sigma;z,p);p).
}
\tag{V3.7}
\]

Here `p` may parameterize frozen-baseline quantities or registered analytical variants, but an external-drive term is **not** part of the baseline branch operator. Any `I_i` term in the legacy v0.3 document belongs to the registered external-drive variant and is deferred unless separately authorized.

Changing variables in the v0.2 integral gives

\[
\int_0^T S(\Psi_i^{(\phi)}(s))ds
=
T\int_0^1 S(\Psi_i(\sigma))d\sigma.
\]

Hence the canonical normalized branch operator is

\[
\boxed{
F_i(z,p)=
T\int_0^1 S_i(\Psi_i(\sigma;z,p);p)d\sigma-2\pi,
\qquad i=1,\ldots,N,
}
\tag{V3.8}
\]

and phase-locked existence means

\[
\boxed{F(z,p)=0.}
\tag{V3.9}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED STRUCTURE via RB-004 + DERIVATION HERE

This is exactly the frozen dimensional-offset existence equation written in fixed-domain coordinates. It introduces no new dynamics.

---

## 5. Independent branch-Jacobian derivation

All derivatives in this section are local derivatives of (V3.8). Assume the required derivatives of `S`, `R_T`, weights and delay parameterization exist in the sense specified in Section 8.

### 5.1 Phase columns

For `k>=2`,

\[
\partial_{\chi_k}X_{ij}
=T(\delta_{ik}-\delta_{jk}).
\tag{V3.10}
\]

Therefore

\[
\begin{aligned}
\partial_{\chi_k}\Psi_i
&=\sum_jw_{ij}R_T'(X_{ij})T(\delta_{ik}-\delta_{jk})\\
&=T\left[
\delta_{ik}\sum_jw_{ij}R_T'(X_{ij})
-w_{ik}R_T'(X_{ik})
\right].
\end{aligned}
\tag{V3.11}
\]

Differentiating (V3.8) yields

\[
\boxed{
\partial_{\chi_k}F_i
=T^2\int_0^1 S_i'(\Psi_i)
\left[
\delta_{ik}\sum_jw_{ij}R_T'(X_{ij})
-w_{ik}R_T'(X_{ik})
\right]d\sigma.
}
\tag{V3.12}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

Self-coupling is handled correctly: when `i=k=j`, the two Kronecker contributions cancel because a uniform shift of a neuron relative to itself cannot alter its self-delay argument.

### 5.2 Gauge identity before fixing

If all `N` phase coordinates are temporarily retained,

\[
\sum_{k=1}^N \partial_{\chi_k}X_{ij}=0.
\]

Thus

\[
\boxed{D_\chi F\,\mathbf1=0}
\tag{V3.13}
\]

before gauge fixing. This is the differential form of global translation invariance.

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

---

## 6. Period-derivative audit

This derivative is subtle because `T` occurs in four distinct ways:

1. the prefactor `T` in (V3.8);
2. the physical argument `X_ij`;
3. the periodic comb `R_T` itself;
4. the dimensional offsets `phi_i=T chi_i`, because the chosen partial derivative holds normalized `chi` fixed.

### 6.1 Fixed physical delays

The canonical `D_zF` period column is defined at fixed `(sigma,chi,p)` with **physical delays `tau_ij` held fixed**. Then

\[
\boxed{
\partial_T X_{ij}=\sigma+\chi_i-\chi_j.
}
\tag{V3.14}
\]

This is not the derivative at fixed dimensional offsets `phi_i`; holding `chi_i` fixed deliberately lets `phi_i=T chi_i` vary with `T`.

At fixed argument `x`, write the explicit period derivative of the comb as

\[
(\partial_T R_T)(x).
\]

Then

\[
\boxed{
\partial_T\Psi_i
=
\sum_jw_{ij}
\left[
(\partial_TR_T)(X_{ij})
+R_T'(X_{ij})(\sigma+\chi_i-\chi_j)
\right].
}
\tag{V3.15}
\]

Finally,

\[
\boxed{
\partial_TF_i
=
\int_0^1S_i(\Psi_i)d\sigma
+T\int_0^1S_i'(\Psi_i)\,\partial_T\Psi_i\,d\sigma.
}
\tag{V3.16}
\]

On a solution of `F_i=0`,

\[
\boxed{
\partial_TF_i
=\frac{2\pi}{T}
+T\int_0^1S_i'(\Psi_i)\,\partial_T\Psi_i\,d\sigma.
}
\tag{V3.17}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

### 6.2 Explicit comb-period derivative

For

\[
R_T(x)=\sum_{m\in\mathbb Z}\eta(x-mT),
\]

termwise differentiation at fixed `x`, wherever justified, gives

\[
\boxed{
(\partial_TR_T)(x)
=-\sum_{m\in\mathbb Z}m\,\eta'(x-mT).
}
\tag{V3.18}
\]

For the exponentially decaying alpha kernel the weighted tail is summable away from its pointwise derivative kinks, so (V3.18) is valid locally / almost everywhere and one-sided at an arrival kink. It must not be implemented by blindly differentiating a wrapped `mod` expression.

**Label:** LEMMA / PROVED LOCALLY UNDER STATED REGULARITY  
**Provenance:** DERIVATION HERE

### 6.3 Other delay conventions are different derivatives

If instead a dimensionless delay ratio `d_ij=tau_ij/T` is held fixed, then `tau_ij=T d_ij` and

\[
\partial_TX_{ij}=\sigma+\chi_i-\chi_j-d_{ij}.
\]

More generally, if `tau_ij=tau_ij(T)`,

\[
\partial_TX_{ij}=\sigma+\chi_i-\chi_j-\frac{d\tau_{ij}}{dT}.
\]

These are different parameterizations and must never be substituted silently for the fixed-physical-delay derivative (V3.14).

### 6.4 General scalar parameter derivative

At fixed `z`, a parameter `p` gives

\[
\boxed{
\partial_pF_i
=T\int_0^1
\left[S_i'(\Psi_i)\partial_p\Psi_i
+(\partial_pS_i)(\Psi_i;p)\right]d\sigma,
}
\tag{V3.19}
\]

with

\[
\boxed{
\partial_p\Psi_i
=
\sum_j\left[
(\partial_pw_{ij})R_T(X_{ij})
+w_{ij}(\partial_pR_T)(X_{ij})
-w_{ij}R_T'(X_{ij})\partial_p\tau_{ij}
\right].
}
\tag{V3.20}
\]

`partial_p R_T` here means explicit kernel/periodic-waveform dependence on `p` at fixed `T` and fixed argument. External-drive derivatives are not part of the baseline operator.

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

---

## 7. Gauge / invariance audit and continuation coordinates

### 7.1 Exact invariance

Because every `X_ij` depends on `chi_i-chi_j`,

\[
F(T,\chi+c\mathbf1,p)=F(T,\chi,p).
\tag{V3.21}
\]

Gauge fixing one phase therefore removes exactly one coordinate redundancy from the existence system.

### 7.2 Unwrapped coordinates

The quotient `chi_i mod 1` is physical display information. Using wrapped coordinates internally creates discontinuities when a representative crosses an integer even though the physical orbit changes continuously. The canonical continuation coordinate is therefore the unwrapped lift (V3.3).

A crossing of a wrapped display boundary is a **coordinate-chart boundary, not a physical branch singularity**.

### 7.3 Pseudo-arclength algebra

**Project continuation definition — not executed in this gate.**

For a scalar continuation parameter `p`, a known solution `(z_0,p_0)` and unit tangent `t_0=(t_z,t_p)`, define predictor

\[
(z_{pred},p_{pred})=(z_0,p_0)+\Delta s\,t_0.
\]

The pseudo-arclength corrector is

\[
F(z,p)=0,
\]

\[
\boxed{
t_0^T\begin{pmatrix}z-z_{pred}\\p-p_{pred}\end{pmatrix}=0,
}
\tag{V3.22}
\]

with augmented Newton matrix

\[
\boxed{
\begin{pmatrix}
D_zF&F_p\\
t_z^T&t_p
\end{pmatrix}.
}
\tag{V3.23}
\]

A regular branch tangent satisfies

\[
\boxed{[D_zF\;F_p]\begin{pmatrix}t_z\\t_p\end{pmatrix}=0,
\qquad \|t\|_2=1.}
\tag{V3.24}
\]

**Label:** PROJECT INTERPRETATION / DEFINITION  
**Provenance:** standard continuation structure adopted by the project; no implementation-performance claim

---

## 8. Smooth-chart assumptions and hybrid / representation boundaries

The first-derivative formulas above are not unconditional pointwise identities for every representation of the hybrid problem.

### 8.1 Baseline response threshold

The frozen baseline response is

\[
S_{r,h}(x)=0\ (x\le h),\qquad
S_{r,h}(x)=e^{-r/(x-h)^2}\ (x>h).
\]

This function extends **smoothly through `x=h`**; all one-sided derivatives from above vanish at the threshold. Therefore a crossing `Psi_i=h` is **not by itself a nonsmooth branch boundary for the frozen baseline response**.

Legacy v0.3 statements about threshold-contact nonsmoothness apply only to registered hard-threshold / Heaviside / piecewise response variants. For such variants, active intervals can change and smooth Jacobian formulas require piecewise / one-sided treatment.

**Baseline correction:** threshold contact must not be labelled `TH_GRAZE` merely because `Psi=h` under C2. If it also makes the spike crossing speed vanish, it is captured by event transversality instead.

### 8.2 Alpha-kernel arrival points

The alpha kernel is continuous at zero but its first derivative jumps there. Hence the periodic comb `R_T` is continuous and periodic, but `R_T'` is piecewise smooth with jumps at spike-arrival phases.

Consequences:

1. classical pointwise `R_T'` is undefined at the isolated kink itself;
2. the branch integral and first derivative can still be interpreted almost everywhere / by split integration because isolated arrival points have measure zero and `R_T` is Lipschitz;
3. naive autodifferentiation through `mod` is not a reference derivative;
4. event-itinerary implementations must update their chart when arrival ordering changes;
5. an arrival collision is **not automatically** a rank singularity of `F` or `D_zF`.

Thus the legacy statement that the branch Jacobian necessarily changes discontinuously at every arrival collision is too strong for the integrated alpha-kernel existence operator and is **not canonicalized** here. Higher derivatives and event-map derivatives can require one-sided / distributional boundary terms and remain a separate regularity question.

### 8.3 Arrival phase registry

For edge `j->i`, the wrapped arrival phase is

\[
\boxed{
a_{ij}=\left(\chi_j-\chi_i+\frac{\tau_{ij}}{T}\right)\bmod1.}
\tag{V3.25}
\]

Coincidences `a_ij=a_ik mod 1` or `a_ij=0 mod 1` mark a change of a wrapped arrival-order chart. Exact future validation should use unwrapped arrival coordinates or split quadrature and preserve one-sided chart provenance.

**Label:** PROPOSITION / PROVED as a timing identity  
**Provenance:** DERIVATION HERE

### 8.4 Event transversality

At the prescribed spike section,

\[
\nu_i=S_i(\Psi_i(1^-)).
\]

A regular event requires

\[
\boxed{\nu_i>0}
\tag{V3.26}
\]

for the nonnegative baseline response. If `nu_i=0`, the RB-004 event-time formula D18 is undefined and the locked-event chart is singular.

**Label:** LEMMA / PROVED  
**Provenance:** RB-004 + DERIVATION HERE

### 8.5 First-hitting admissibility

Define normalized accumulated phase

\[
\Theta_i(\sigma)=T\int_0^\sigma S_i(\Psi_i(\xi))d\xi.
\]

A candidate one-spike-per-cycle orbit is physically admissible only if

\[
\boxed{
\Theta_i(1)=2\pi,
\qquad
\Theta_i(\sigma)<2\pi\quad\forall\,0<\sigma<1.
}
\tag{V3.27}
\]

This is logically independent of solving the endpoint integral equation.

**Label:** LEMMA / PROVED  
**Provenance:** RB-004 D16–D17 + DERIVATION HERE

---

## 9. Existence vs stability vs hybrid-singularity taxonomy

These categories are canonicalized as distinct logical questions.

### 9.1 Existence regularity / singularity

After gauge fixing, a regular branch point has

\[
\det D_zF\ne0
\]

for a fixed parameter. Then the implicit-function theorem gives a locally unique branch graph `z=z(p)`.

An **existence singularity** is indicated by rank loss of the gauge-fixed `D_zF`. A small singular value is a diagnostic, not by itself a complete nonlinear bifurcation classification.

**Label:** THEOREM / PROVED for the regular-point implicit-function statement; PROPOSITION for the rank-loss diagnostic  
**Provenance:** standard mathematical result + PROJECT INTERPRETATION

### 9.2 Conditional generic fold theorem

If `F` is `C^2` in a neighborhood, `rank D_zF=N-1`, right/left nullvectors satisfy `D_zF r=0`, `ell^T D_zF=0`, `ell^T r=1`, and

\[
\ell^TF_p\ne0,
\qquad
\ell^TD_z^2F[r,r]\ne0,
\]

then Lyapunov–Schmidt reduction gives the generic local fold form

\[
0=a\,\delta p+b\,\xi^2+\cdots.
\]

**Label:** PROPOSITION / PROVED CONDITIONALLY ON `C^2` REGULARITY  
**Provenance:** standard local bifurcation structure / DERIVATION CHECKED HERE

This gate does **not** prove that the exact alpha-kernel branch operator is `C^2` across every moving arrival configuration. Therefore no Lighthouse fold location or blanket higher-derivative claim is frozen by this statement.

### 9.3 Dynamical stability

Dynamical stability concerns the event/spike-time return operator or characteristic spectrum. It is not determined by `D_zF`.

Canonical rule:

\[
\boxed{\text{existence Jacobian regularity }\not\Rightarrow\text{ dynamical stability}.}
\tag{V3.28}
\]

and conversely an existence singularity does not determine a Floquet multiplier configuration.

**Label:** INTERPRETATION / LOGICAL SEPARATION  
**Provenance:** PROJECT INTERPRETATION consistent with hybrid dynamical-systems structure

No v0.4 Floquet formula, multiplier value or stability boundary is imported here.

### 9.4 Hybrid/event-chart singularity

Hybrid validity is lost or its local derivative chart fails when, for example:

- spike transversality fails (`nu_i=0`);
- the assumed spike at `sigma=1` is not first hitting;
- simultaneous event ordering makes a chart-specific event map ambiguous;
- a nonsmooth registered response variant changes active branch pieces.

These conditions can occur while `D_zF` remains nonsingular.

### 9.5 Representation/chart boundaries

Wrapped phase crossings and alpha-arrival ordering changes can require a change of coordinates or event itinerary without being physical singularities of the phase-locked orbit. They must therefore be recorded separately from genuine existence and transversality singularities.

---

## 10. Exchange-symmetric two-cell audit

Consider

\[
W=\begin{pmatrix}w_s&w_c\\w_c&w_s\end{pmatrix},
\]

common response, self-delay `tau_s`, cross-delay `tau_c`, and gauge-fixed relative phase `chi=chi_2-chi_1`.

Then

\[
\Psi_1=w_sR_T(T\sigma-\tau_s)
+w_cR_T(T(\sigma-\chi)-\tau_c),
\]

\[
\Psi_2=w_cR_T(T(\sigma+\chi)-\tau_c)
+w_sR_T(T\sigma-\tau_s).
\]

Define

\[
F_+=(F_1+F_2)/2,
\qquad
F_-=(F_1-F_2)/2.
\]

Exchange of the two cells sends `chi -> -chi`, so

\[
\boxed{F_+(T,-\chi)=F_+(T,\chi),
\qquad F_-(T,-\chi)=-F_-(T,\chi).}
\tag{V3.29}
\]

At synchrony `chi=0`, parity gives

\[
F_-(T,0)=0,
\qquad
\partial_\chi F_+(T,0)=0,
\qquad
\partial_TF_-(T,0)=0.
\]

Thus

\[
\boxed{
D_{(T,\chi)}(F_+,F_-)\big|_{\chi=0}
=
\begin{pmatrix}A&0\\0&B\end{pmatrix}.}
\tag{V3.30}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

For

\[
\Psi_0=w_sR_T(T\sigma-\tau_s)+w_cR_T(T\sigma-\tau_c),
\]

the antisymmetric existence coefficient is obtained directly from the phase derivative:

\[
\partial_\chi F_1|_0
=-T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma,
\]

\[
\partial_\chi F_2|_0
=+T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma.
\]

Therefore

\[
\boxed{
B=\partial_\chi F_-|_0
=-T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma.}
\tag{V3.31}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

This independently confirms the **negative sign** in the recovery snapshot and resolves the historical sign erratum at the mathematical level.

A zero `B` is an antisymmetric existence-Jacobian degeneracy. It is not sufficient on its own to declare a generic pitchfork; nonlinear nondegeneracy and regularity conditions are additionally required.

### 10.1 Legacy pitchfork coefficients

The algebraic elimination formulas

\[
T=T_s(p)-\frac{F_{+,\chi\chi}}{2F_{+,T}}\chi^2+O(\chi^4)
\]

and the corresponding `a,b` coefficients in the legacy document are algebraically correct **if `F` is `C^3` locally and the stated denominators/nondegeneracies hold**.

However, because the alpha-kernel existence operator contains moving derivative kinks and this gate has not established blanket `C^3` regularity across all arrival configurations, these formulas are classified as:

`C1 algebra under an explicit C^3 assumption / C5 for unconditional baseline applicability`.

They are not part of the proposed narrow freeze below.

---

## 11. C1–C5 classification of recovered v0.3 material

Classification semantics follow the recovery gate:

- **C1** — directly recoverable mathematical material after independent audit;
- **C2** — computational / algorithmic claim suitable for a governed replay or validation contract;
- **C3** — effect-bearing claim requiring a preregistered rerun if used as frozen evidence;
- **C4** — exploratory / historical material retained only for provenance;
- **C5** — unresolved, insufficiently sourced, or requiring an additional proof/regularity layer.

| v0.3 claim/material | Class | Epistemic status |
|---|---|---|
| `phi_i=T chi_i`, normalized firing times | C1 | PROPOSITION / PROVED — DERIVATION HERE |
| fixed-domain branch operator (V3.8) | C1 | PROPOSITION / PROVED — RB-004 + DERIVATION HERE |
| uniform gauge and `chi_1=0` | C1 | LEMMA / PROVED — DERIVATION HERE |
| unwrapped internal phase coordinates | C1 | PROJECT INTERPRETATION / coordinate rule |
| phase Jacobian (V3.12) | C1 | PROPOSITION / PROVED — DERIVATION HERE |
| fixed-physical-delay period derivative (V3.14–V3.18) | C1 | PROPOSITION / LEMMA — PROVED under stated regularity |
| general parameter derivative | C1 | PROPOSITION / PROVED under stated differentiability |
| pseudo-arclength augmented equations | C1 | PROJECT DEFINITION; no execution claim |
| regular-branch IFT statement | C1 | THEOREM / PROVED |
| generic fold conditions | C1 conditional | PROPOSITION / PROVED if local `C^2` regularity holds |
| any actual Lighthouse fold location/branch | C3 | no governed numerical result yet |
| exchange parity/block diagonalization | C1 | PROPOSITION / PROVED |
| corrected antisymmetric coefficient `B` | C1 | PROPOSITION / PROVED |
| generic pitchfork elimination formulas | C1 conditional / C5 baseline-wide | algebra checked; unconditional alpha-operator `C^3` regularity not established |
| any actual Lighthouse pitchfork location/scaling | C3 | preregistered numerical validation required |
| existence/stability/hybrid separation | C1 | PROJECT INTERPRETATION / logical taxonomy |
| actual Floquet/multiplier claims | C5 here | v0.4+ gate required |
| transversality and first hitting | C1 | already supported by RB-004; normalized restatement proved |
| baseline threshold as nonsmooth boundary | C5 / REJECT AS STATED | frozen C2 response is smooth at threshold |
| hard-threshold variant contact theory | C1 conditional | applies only to separately selected nonsmooth variants |
| arrival phase formula | C1 | PROPOSITION / PROVED |
| claim that every arrival collision makes `D_zF` discontinuous | C5 / NOT ESTABLISHED | too strong for integrated continuous alpha comb |
| exact arrival-aware implementation behavior | C2 | requires future validation contract |
| adaptive-delay implicit sensitivity algebra | C1 candidate but deferred | variant outside RB-004 baseline |
| adaptive switching / commensurability effects | C3 | effect-bearing later program |
| general symmetry/Fourier-sector continuation | C5 here | overlaps v0.4+ symmetry layer |
| exact-vs-surrogate scientific agreement | C2/C3 | requires implementation + pre-execution contract |

No legacy `COMPLETE`, `VERIFIED` or `CERTIFIED` label changes these classifications.

---

## 12. Deferred numerical / benchmark registry

The legacy `continuation_contract_v0.3.md` is retained only as a registry of future validation ideas. No B11–B22 test was executed and no legacy recommended tolerance is adopted as canonical by this gate.

| Legacy benchmark | Future disposition |
|---|---|
| B11 coordinate equivalence/gauge | suitable for a new pre-execution C2 validation contract |
| B12 branch Jacobian | suitable for C2 contract on predetermined smooth-chart cases |
| B13 pseudo-arclength synthetic fold | C2 algorithmic validation; Lighthouse-fold part must be separately preregistered |
| B14 two-cell block diagonalization / `B` integral | high-priority C2 validation target |
| B15 pitchfork | synthetic algebraic test C2; Lighthouse pitchfork C3 and regularity-dependent |
| B16 existence/stability classifier | deferred until v0.4 stability objects are canonical |
| B17 event-transversality scaling | elementary part can become C2; saltation part is outside current freeze |
| B18 arrival-aware quadrature | C2 after a refined contract distinguishing a.e. first derivatives from chart changes |
| B19 threshold contact | only for an explicitly authorized nonsmooth response variant |
| B20 implicit branch sensitivity | C2 after fixed parameterization and predetermined branch test point |
| B21 commensurability | adaptive-delay branch; deferred |
| B22 first-hitting admissibility | C2 and directly traceable to RB-004 |

A future contract must fix model variant, parameter values, histories, chart margins, finite test points, derivative convention, tolerances and pass/fail rules **before** any v0.3 numerical output is observed.

---

## 13. Explicit exclusions

This gate does not canonicalize, execute or validate:

- any numerical continuation branch;
- any Lighthouse fold or pitchfork parameter/location;
- any B11–B22 benchmark output;
- any continuation tolerance or step-size policy;
- any v0.4 Floquet spectrum, multiplier or stability boundary;
- any normal-form coefficient obtained numerically;
- any v0.5+ theory or v0.6+ numerical atlas result;
- blanket `C^2/C^3` regularity of the exact alpha branch operator across arrival collisions;
- hard-threshold contact theory as a property of the frozen smooth baseline response;
- adaptive-delay dynamics, commensurability effects or slow switching;
- JAX or production implementation;
- surrogate-continuation error claims;
- inference / observation design / active experiment design;
- v0.27;
- application, novelty or manuscript claims.

The legacy branch remains read-only recovery evidence and is not merged.

---

## 14. Gate decision

\[
\boxed{\text{PASS}}
\]

Reason:

1. the normalized coordinate map is exactly derivable from RB-004 v0.2 phase-locking mathematics;
2. the fixed-domain branch equation is an exact change of variables, not a new numerical claim;
3. global gauge invariance and unwrapped continuation coordinates are mathematically consistent;
4. the normalized phase Jacobian is independently re-derived;
5. the period derivative has been independently audited with all explicit / implicit `T` dependence and fixed-physical-delay semantics stated;
6. the two-cell exchange-symmetry block structure and corrected negative sign of `B` are independently verified;
7. first-hitting and transversality conditions are consistent with RB-004;
8. existence, dynamical stability and hybrid/chart singularities are separated without importing v0.4 science;
9. two legacy overstatements are repaired rather than silently promoted: baseline threshold contact is not generally nonsmooth, and arrival collision is not automatically an existence-Jacobian singularity;
10. no numerical continuation, benchmark execution or downstream effect inspection occurred.

PASS means only that MASTER may decide whether to establish a narrow `CORE v0.3 Continuation Theory Freeze 0.1`.

---

## 15. Proposed contents of `CORE v0.3 Continuation Theory Freeze 0.1`

If MASTER authorizes a freeze, the proposed frozen contents are limited to:

1. normalized coordinate map (V3.1)–(V3.5);
2. baseline normalized branch operator (V3.6)–(V3.9), with no external drive;
3. phase-Jacobian and gauge identities (V3.10)–(V3.13);
4. fixed-physical-delay period derivative and comb-period derivative (V3.14)–(V3.18) under the stated regularity assumptions;
5. general parameter derivative (V3.19)–(V3.20);
6. exact gauge invariance (V3.21) and unwrapped-coordinate rule;
7. pseudo-arclength algebra (V3.22)–(V3.24) as a method definition only;
8. smooth-chart / arrival / wrapped-coordinate qualifications in Section 8;
9. event transversality and first-hitting conditions (V3.26)–(V3.27);
10. existence-vs-stability-vs-hybrid taxonomy and regular-branch IFT statement;
11. generic fold theorem only conditionally on local `C^2` regularity, with no numerical fold claim;
12. exchange-symmetric two-cell parity, block diagonalization and corrected coefficient (V3.29)–(V3.31);
13. C1–C5 classification and explicit exclusions.

Explicitly excluded from the proposed freeze are all numerical continuation results, actual fold/pitchfork claims, v0.4 stability objects, unconditional higher-derivative alpha-kernel claims, adaptive delays and B11–B22 outputs.

---

## 16. Open questions

1. **OPEN QUESTION — alpha-operator higher regularity.** What is the sharp `C^k` regularity of the integrated phase-locked operator with a continuous alpha kernel and moving arrival kinks, especially at coincident arrivals? This must be resolved before unconditional baseline-specific second/third derivative bifurcation coefficients are frozen.
2. **OPEN QUESTION — simultaneous arrivals.** Under which coupling/jump structures do simultaneous arrivals merely change event-chart representation versus create a genuine nonsmooth event-map derivative?
3. **OPEN QUESTION — threshold variants.** If a hard cutoff or Heaviside response is later selected, a separate piecewise continuation theorem / contract is required; the smooth baseline C2 does not supply it.
4. **OPEN QUESTION — first v0.3 numerical contract.** MASTER must decide which finite, pre-specified cases are sufficient to validate normalized coordinates, Jacobians, pseudo-arclength and two-cell symmetry without selecting Lighthouse critical points post hoc.
5. **OPEN QUESTION — stability interface.** The exact interface between the v0.3 existence operator and a later canonical v0.4 spike-time/Floquet operator remains deferred.

---

## 17. STOP

No v0.3 numerical continuation or B11+ benchmark was executed. No v0.4+ work was started.

STOP — RETURN TO MASTER
