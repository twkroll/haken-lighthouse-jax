# CORE v0.4 Floquet Theory Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — NARROW SPIKE-TIME FLOQUET / SYMMETRY THEORY CANONICALIZED; NO B23–B40 OR LIGHTHOUSE ROOT SEARCH EXECUTED

## 1. Git / provenance identity

This gate audits only the mathematical/source/formulation layer authorised by MASTER.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD at gate start: `a50141a5b6b70cabbeebbbac25eee9f7ab222449`
- governance blob SHA: `7ba28f4c959344930f7b22d10f6f0d5b5163eea9`
- CORE STATUS start blob SHA: `cf8c54b96366eb815b24e15fb32d40f18163699c`
- MASTER STATUS start blob SHA: `6b6d021ae5e2a795b1fd37f44c6788d2d681aefe`
- project status v1.7 blob SHA: `8b613b529e2111e64659d4ae03beae2435860606`
- decision log blob SHA: `0311649a813efc1a5e3264a1019d20628ef6c129`
- authorising prompt blob SHA: `154f2fb9d8e58f7ad808c3d8ec52c958a5234b10`

Frozen scientific authorities:

- RB-004 `CORE Mathematical Freeze 0.1`, blob `d84a2f8c23b0bb0d6be4867a42a6fea235232f20`
- RB-006 `CORE v0.2 Benchmark Result Freeze 0.1`, blob `276c74a74d531a947e50c8661e9a068aca41918c`
- RB-007 `CORE v0.3 Continuation Theory Freeze 0.1`, blob `9ba55b855b3257d11e9fc741ea19a0e2deacc329`
- RB-008 `CORE v0.3 Continuation Validation Contract Freeze 0.1`, blob `911acb4c589735e964f5cd25c7f438bacfa0e6e0`
- RB-009 `CORE v0.3 Continuation Validation Result Freeze 0.1`, blob `88d2a25c9ef489bb4160e7f1211fd9f53b750b6a`

Frozen legacy recovery input is read-only at:

`287eae8a86560b78ed94f30a2786243714c33ac0`

Candidate v0.4 legacy blobs:

- `docs/core/spike_time_floquet_v0.4.md`, blob `d45650432d926b1eb2e9c1700cf61bd47fb6de3b`
- `docs/core/symmetry_reductions_v0.4.md`, blob `5021fc9bf9547b40e1eff9827f9abd5a8c7f3fbd`
- `docs/core/floquet_contract_v0.4.md`, blob `8a11678e746554b7b3de5d8b1d715057225979d8`

No legacy branch was merged or modified. No B23–B40 test, multiplier/root search, stability-boundary search, continuation sweep, v0.5+ calculation or downstream experiment was executed.

---

## 2. Frozen-authority map

| Authority | Used here | Explicitly not imported |
|---|---|---|
| RB-004 | baseline Lighthouse dynamics, alpha kernel, fixed delays, event section, first-hitting/transversality semantics | downstream Floquet or stability claims |
| RB-006 | governed consistency of baseline/event/alpha identities | no v0.4 result |
| RB-007 | phase-locked coordinates, fixed-domain existence operator, existence/event/chart taxonomy | no dynamic multiplier claim |
| RB-008 | governance precedent for finite pre-execution validation contracts | V3C test membership is not reused as v0.4 evidence |
| RB-009 | governed v0.3 validation PASS | no Floquet multiplier or stability boundary |
| legacy v0.4 | candidate mathematical/test inventory only | no legacy COMPLETE/benchmark/result status is accepted |

---

## 3. Source / provenance claim map

### S-V4-1 — Coombes 2025

Stephen Coombes, *Revisiting the Haken Lighthouse model*, European Physical Journal Special Topics, DOI `10.1140/epjs/s11734-025-01841-3`, published online 19 August 2025.

Relevant source support:

- Sect. 3.2 develops linear stability from perturbations of firing times for synchronous graph states;
- its event-time relation and map-based stability construction support the general firing-time viewpoint;
- the paper also uses circulant/Fourier ideas for structured network stability and develops a continuum/Turing stability formulation.

Qualification: Sect. 3.2 explicitly specialises the graph calculation there to a linear `S`. Therefore the nonlinear, heterogeneous phase-locked operator retained below is **not** attributed wholesale to the 2025 paper.

Provenance status: `SOURCE-DERIVED STRUCTURAL SUPPORT` only.

### S-V4-2 — Coombes–Thul–Ruschel–Nicks 2026

Stephen Coombes, Rüdiger Thul, Stefan Ruschel, Rachel Nicks, *Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks*, arXiv:`2606.21508v1`, submitted 19 June 2026.

Relevant source support:

- Sect. 3, especially Eqs. (11)–(14), derives a firing-time linear difference equation and nonlinear spectral matrix for general phase-locked states with fixed delays;
- the source uses the cycle exponent `lambda` with perturbations proportional to `exp(m lambda)`;
- Sect. 6, especially Eqs. (34)–(35), exploits a circulant ring representation to diagonalise stability into spatial Fourier sectors.

The source characteristic form contains a source-aligned diagonal row-sum term. Below this gate independently proves the exact periodicity identity that reduces the source-aligned form to the project multiplier operator `(mu-1)D_nu-H(mu)` under the stated baseline assumptions.

Provenance status: `SOURCE-DERIVED STRUCTURE + DERIVATION HERE`.

### S-V4-3 — baseline provenance

Historical Haken / Lighthouse model provenance and the modern graph/alpha canonical baseline are inherited only through RB-004. No new historical attribution is created in this gate.

### S-V4-4 — standard mathematics

Discrete Fourier diagonalisation of circulant matrices, invariant subspaces of equitable quotients, finite-group isotypic projectors, simple nonlinear-eigenvalue sensitivity and standard map-bifurcation labels are used only where independently stated/derived below. No novelty claim is made.

---

## 4. Canonical assumptions for this v0.4 theory layer

The following assumptions are local to the retained theory and do not broaden RB-004.

- **V4-A1 — regular locked orbit.** A one-spike-per-cycle phase-locked orbit exists with `T>0` and firing times `T_i^m=(m+chi_i)T`.
- **V4-A2 — event validity.** The prescribed event is first hitting and the spike-section velocity satisfies `nu_i>0` for every neuron in the frozen nonnegative baseline response.
- **V4-A3 — itinerary preservation.** Perturbations are small enough not to create/destroy spikes or change the event/arrival chart used by the local linearisation.
- **V4-A4 — differentiability.** `S_i` is `C^1` on the locked input range. The alpha periodic input is continuous and piecewise `C^1` / absolutely continuous; derivative identities are interpreted almost everywhere with split integration at arrivals.
- **V4-A5 — summability/interchange.** Lag sums, differentiation and integration are interchanged only where absolute convergence or an equivalent dominated-convergence argument is established.
- **V4-A6 — multiplier coordinate.** The raw lag generating series is formulated for `mu != 0`; for the alpha tail its absolute-convergence domain is derived explicitly below.
- **V4-A7 — spike-time scope.** The characteristic operator describes the linearised event-time recurrence. Equivalence to a complete full hybrid-state Floquet spectrum, including any auxiliary synaptic-state modes, is not asserted without a separate validation/equivalence gate.
- **V4-A8 — symmetry scope.** Symmetry reduction is applied to the full locked-state characteristic operator in the chosen event-index gauge, not inferred from weights alone.

These assumptions are `ASSUMPTION — PROJECT CANONICALIZATION`, except where inherited directly from RB-004/RB-007.

---

## 5. Base phase-locked orbit and local representation

The frozen locked-state timing form is

\[
\boxed{T_i^m=(m+\chi_i)T.}
\tag{V4.1}
\]

In neuron `i`'s local cycle coordinate

\[
t=T_i^m+s,\qquad 0\le s<T,
\]

define

\[
\boxed{
\Psi_i(s)=\sum_j w_{ij}\sum_{\ell\in\mathbb Z}
\eta\!\left(s+(\ell+\chi_i-\chi_j)T-\tau_{ij}\right).
}
\tag{V4.2}
\]

Reindexing `ell=m-n` makes (V4.2) independent of cycle number `m`.

For the continuous alpha baseline, `Psi_i` is periodic and continuous at the cycle seam. Define the event velocity

\[
\boxed{\nu_i=S_i(\Psi_i(0))=S_i(\Psi_i(T^-)).}
\tag{V4.3}
\]

A regular event requires `nu_i>0` under the frozen nonnegative response.

**Label:** PROPOSITION / PROVED  
**Provenance:** RB-004/RB-007 + DERIVATION HERE

---

## 6. Independent spike-time linearisation

Perturb firing times by

\[
\widetilde T_i^m=T_i^m+\delta T_i^m.
\tag{V4.4}
\]

The exact phase-gain condition is

\[
2\pi=\int_{\widetilde T_i^m}^{\widetilde T_i^{m+1}}
S_i(\widetilde\psi_i(t))\,dt.
\tag{V4.5}
\]

A presynaptic event displacement gives, inside a fixed chart,

\[
\eta(t-T_j^n-\delta T_j^n-\tau_{ij})
=\eta(t-T_j^n-\tau_{ij})
-\eta'(t-T_j^n-\tau_{ij})\delta T_j^n+O(\delta T^2).
\tag{V4.6}
\]

Hence

\[
\delta\psi_i(t)=
-\sum_jw_{ij}\sum_n
\eta'(t-T_j^n-\tau_{ij})\delta T_j^n.
\tag{V4.7}
\]

Applying the Leibniz rule to the moving limits in (V4.5), using equal base endpoint velocities (V4.3), gives

\[
0=\nu_i(\delta T_i^{m+1}-\delta T_i^m)
+\int_{T_i^m}^{T_i^{m+1}}S_i'(\psi_i^*)\delta\psi_i\,dt.
\tag{V4.8}
\]

Define the lag coefficients

\[
\boxed{
K_{ij,\ell}
=\int_0^T S_i'(\Psi_i(s))
\eta'\!\left(s+(\ell+\chi_i-\chi_j)T-\tau_{ij}\right)ds.
}
\tag{V4.9}
\]

Reindexing `n=m-ell` yields

\[
\boxed{
\nu_i(\delta T_i^{m+1}-\delta T_i^m)
=\sum_jw_{ij}\sum_{\ell\in\mathbb Z}
K_{ij,\ell}\,\delta T_j^{m-\ell}.
}
\tag{V4.10}
\]

**Label:** PROPOSITION / PROVED under V4-A1–V4-A5  
**Provenance:** DERIVATION HERE; source structure consistent with Coombes et al. 2026 Sect. 3

### 6.1 Reconciliation with the source-aligned difference form

Changing variables to a coordinate anchored at the *perturbed* lower event produces the source-aligned expression

\[
\nu_i(\delta T_i^{m+1}-\delta T_i^m)
+\sum_jw_{ij}\sum_\ell K_{ij,\ell}
(\delta T_i^m-\delta T_j^{m-\ell})=0.
\tag{V4.11}
\]

Define

\[
A_i:=\sum_jw_{ij}\sum_\ell K_{ij,\ell}.
\tag{V4.12}
\]

Under absolute interchange,

\[
A_i
=\int_0^T S_i'(\Psi_i(s))\Psi_i'(s)ds
=S_i(\Psi_i(T))-S_i(\Psi_i(0))=0.
\tag{V4.13}
\]

For the alpha baseline the composition is absolutely continuous, so the identity remains valid with derivative kinks handled almost everywhere / by split integration.

Therefore (V4.11) reduces exactly to (V4.10).

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

This is an important repair/clarification: the source-aligned diagonal row-sum term is not silently discarded; its exact cancellation is proved.

---

## 7. Nonlinear cycle-multiplier operator

Use the cycle-Floquet ansatz

\[
\delta T_i^m=\xi_i\mu^m,
\qquad \mu\ne0.
\tag{V4.14}
\]

Define

\[
\boxed{
H_{ij}(\mu)=w_{ij}\sum_{\ell\in\mathbb Z}K_{ij,\ell}\mu^{-\ell},
}
\tag{V4.15}
\]

\[
D_\nu=\operatorname{diag}(\nu_1,\ldots,\nu_N),
\]

and

\[
\boxed{
M(\mu)=(\mu-1)D_\nu-H(\mu).
}
\tag{V4.16}
\]

Then the spike-time characteristic problem is

\[
\boxed{M(\mu)\xi=0.}
\tag{V4.17}
\]

For small analytical systems `det M(mu)=0` is equivalent to singularity of `M`, but determinant evaluation is not frozen as a numerical method.

**Label:** PROPOSITION / PROVED on the convergence domain  
**Provenance:** DERIVATION HERE; `mu=e^lambda` reparameterises the source cycle-exponent formulation of Coombes et al. 2026

### 7.1 Convergence domain

For a causal kernel whose derivative obeys a tail bound

\[
|\eta'(t)|\le C(1+t^p)e^{-\beta t}\quad(t\to\infty),
\]

and bounded `S_i'(Psi_i)` on one cycle:

- sufficiently negative lags vanish identically by causality;
- positive-lag coefficients obey `K_{ij,ell}=O(poly(ell)e^{-beta ell T})`.

Hence (V4.15) converges absolutely and locally uniformly at least for

\[
\boxed{|\mu|>e^{-\beta T}.}
\tag{V4.18}
\]

For the alpha kernel, `beta=alpha`, so the raw lag-series domain is

\[
\boxed{|\mu|>r,\qquad r=e^{-\alpha T}.}
\tag{V4.19}
\]

Within that domain `H(mu)` is analytic. The gate does not equate a meromorphic extension outside this domain with an absolutely convergent lag series.

**Label:** LEMMA / PROVED for the stated exponential-tail class  
**Provenance:** DERIVATION HERE

---

## 8. Exact neutral global time-translation mode

A uniform time translation has

\[
\delta T_i^m=c\quad\forall i,m,
\]

hence candidate multiplier/eigenvector

\[
\mu_0=1,\qquad \xi_0=\mathbf1.
\]

Because `1>e^{-alpha T}`, the alpha lag series converges absolutely at `mu=1`. Using (V4.13),

\[
\sum_jH_{ij}(1)=A_i=0.
\tag{V4.20}
\]

Therefore

\[
\boxed{M(1)\mathbf1=0.}
\tag{V4.21}
\]

**Label:** THEOREM / PROVED under V4-A1–V4-A5  
**Provenance:** DERIVATION HERE; source-consistent with the phase-shift zero mode in Coombes et al. 2026

The neutral mode is identified by its physical uniform spike-time vector, not by deleting an arbitrary computed root nearest `1`.

---

## 9. Weighted derivative comb and alpha closed form

Define

\[
\boxed{
Q_\mu(x;T)=\sum_{\ell\in\mathbb Z}
\eta'(x+\ell T)\mu^{-\ell}.
}
\tag{V4.22}
\]

Whenever the lag series is absolutely integrable, Fubini/Tonelli rearrangement gives

\[
\boxed{
H_{ij}(\mu)=w_{ij}\int_0^T S_i'(\Psi_i(s))
Q_\mu(s+(\chi_i-\chi_j)T-\tau_{ij};T)ds.
}
\tag{V4.23}
\]

**Label:** PROPOSITION / PROVED on the absolute-convergence domain  
**Provenance:** DERIVATION HERE

### 9.1 Alpha kernel

For

\[
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\]

write away from an arrival boundary

\[
x=u+qT,\qquad 0<u<T,\qquad q\in\mathbb Z,
\]

and let

\[
r=e^{-\alpha T},\qquad z=r/\mu.
\]

Causality implies that only terms with `n=q+ell>=0` contribute. Thus

\[
Q_\mu
=\mu^q\alpha^2e^{-\alpha u}
\sum_{n=0}^\infty z^n[(1-\alpha u)-\alpha Tn].
\]

For `|z|<1`, geometric summation yields

\[
\boxed{
Q_\mu(x;T)=
\mu^q\alpha^2e^{-\alpha u}
\left[
\frac{1-\alpha u}{1-r/\mu}
-\frac{\alpha T(r/\mu)}{(1-r/\mu)^2}
\right].
}
\tag{V4.24}
\]

Equivalently,

\[
Q_\mu(x;T)=
\alpha^2e^{-\alpha u}\mu^{q+1}
\left[
\frac{1-\alpha u}{\mu-r}
-\frac{\alpha Tr}{(\mu-r)^2}
\right].
\tag{V4.25}
\]

The convergent-series identity is exactly

\[
\boxed{|\mu|>r.}
\tag{V4.26}
\]

The rational expression (V4.25) defines a **meromorphic algebraic continuation** beyond that domain, with a pole at `mu=r` and, depending on integer `q`, possible additional behaviour/poles at `mu=0`. This continuation is not called a convergent lag-sum identity outside (V4.26).

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

### 9.2 Arrival boundary convention

At `u=0`, the classical point derivative of the alpha kernel jumps. Therefore:

- integrated quantities use split integration and are unaffected by the value assigned at one point;
- a pointwise derivative at the kink is one-sided / chart-labelled;
- direct automatic differentiation through `mod`/`floor` is not a canonical reference;
- meromorphic continuation in `mu` does not remove the event-chart qualification in physical time.

This is aligned with RB-007/RB-009 arrival-boundary semantics.

### 9.3 Relation to the frozen alpha state-space representation

RB-004/RB-006 establish the exact periodic alpha state-space representation for the base waveform. Equation (V4.24) is a generating-function identity for the **weighted derivative history**. This gate does not prove that all roots of its meromorphic continuation coincide with every auxiliary full-state Floquet multiplier. That equivalence remains a C2/C5 validation question.

---

## 10. Multiplier and exponent conventions

Coombes et al. 2026 uses a cycle exponent `lambda` via `exp(m lambda)`. The project multiplier is

\[
\boxed{\mu=e^\lambda.}
\tag{V4.27}
\]

For a chosen logarithm branch,

\[
\lambda_k=\Log\mu+2\pi i k,
\qquad
\Lambda_k=\frac{\lambda_k}{T}
\tag{V4.28}
\]

where `Lambda_k` is a physical-time exponent.

Consequences:

- `|mu|<1` is branch-independent and equivalent to `Re Lambda_k<0` for every log branch;
- arguments/frequencies depend on the chosen branch modulo `2pi` per cycle;
- `mu=0` has no finite logarithm and is handled in multiplier space;
- critical classification should therefore be performed primarily in multiplier space.

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE / PROJECT CONVENTION

A complete full-hybrid stability theorem is not asserted in this gate. Conditional statement only: **if** the relevant spike-time spectrum is complete for the perturbation class under study, then all nontrivial multipliers inside the unit disk is the discrete-cycle spectral-stability criterion.

---

## 11. Simple nonlinear-eigenvalue conditioning

Let `mu_*` be a simple root of the nonlinear eigenproblem with

\[
M(\mu_*)\xi=0,
\qquad
y^*M(\mu_*)=0,
\]

and normalise

\[
\|\xi\|_2=\|y\|_2=1.
\]

Define

\[
\boxed{\gamma_*=y^*M'(\mu_*)\xi.}
\tag{V4.29}
\]

For a simple nonlinear eigenvalue one requires

\[
\boxed{\gamma_*\ne0.}
\tag{V4.30}
\]

If the operator depends smoothly on a scalar parameter `p`, first-order differentiation gives

\[
\boxed{
\frac{d\mu_*}{dp}
=-\frac{y^*M_p(\mu_*,p)\xi}
{y^*M_\mu(\mu_*,p)\xi}.
}
\tag{V4.31}
\]

**Label:** PROPOSITION / PROVED for a simple root under the stated differentiability  
**Provenance:** DERIVATION HERE / standard nonlinear-eigenvalue calculus

Canonical repair relative to the legacy wording: the magnitude of `y^*M'xi` is not a scale-invariant conditioning number unless left/right vectors are normalised. This gate freezes the denominator only with an explicit normalisation convention; a production condition number is C2.

---

## 12. Existence / dynamic / event / chart taxonomy

The following remain logically distinct:

1. **existence criticality:** rank loss of the gauge-fixed `D_zF` from RB-007;
2. **dynamic criticality:** a nontrivial spike-time multiplier reaches the unit circle;
3. **event singularity:** transversality `nu_i=0` or loss of first hitting;
4. **arrival/event-chart boundary:** event ordering or an alpha derivative kink changes chart;
5. **representation boundary:** phase wrapping or spike-generation relabelling changes coordinates without changing the physical orbit.

None is identified with another by this gate. Coincidence can be a later bifurcation theorem/validation target but is not assumed.

**Label:** INTERPRETATION / LOGICAL TAXONOMY  
**Provenance:** RB-007 + PROJECT CANONICALIZATION

---

## 13. Event-index relabelling covariance

Spike-generation labels are not physical observables. Relabel neuron `i` by an integer `k_i`:

\[
m'=m+k_i,
\qquad
\chi_i'=\chi_i-k_i.
\tag{V4.32}
\]

Under the multiplier ansatz,

\[
\xi_i'=\mu^{-k_i}\xi_i.
\]

With

\[
D_k(\mu)=\operatorname{diag}(\mu^{-k_1},\ldots,\mu^{-k_N}),
\]

a consistently transformed characteristic matrix satisfies

\[
\boxed{M'(\mu)=D_k(\mu)M(\mu)D_k(\mu)^{-1}.}
\tag{V4.33}
\]

Thus root locations are invariant under consistent integer spike-label gauges, even though individual matrix entries/eigenvector components can change.

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

This qualification is important for twisted/spatiotemporal states and prevents phase wrapping from being mistaken for a change of physical spectrum.

---

## 14. Exchange-symmetric two-cell reduction

Let `P` exchange the two neurons. If the **full** characteristic operator satisfies

\[
PM(\mu)=M(\mu)P
\quad\text{for all }\mu\text{ in the domain},
\tag{V4.34}
\]

then

\[
M(\mu)=
\begin{pmatrix}a(\mu)&b(\mu)\\b(\mu)&a(\mu)\end{pmatrix}.
\]

The invariant vectors

\[
v_+=(1,1)^T,\qquad v_-=(1,-1)^T
\]

yield

\[
\boxed{E_+(\mu)=a(\mu)+b(\mu),\qquad
E_-(\mu)=a(\mu)-b(\mu).}
\tag{V4.35}
\]

For the common-velocity representation `M=(mu-1)nu I-H` with `H=[[h_s,h_c],[h_c,h_s]]`,

\[
E_+(\mu)=\nu(\mu-1)-h_s(\mu)-h_c(\mu),
\]

\[
E_-(\mu)=\nu(\mu-1)-h_s(\mu)+h_c(\mu).
\tag{V4.36}
\]

The global shift lies in the `+` sector and `E_+(1)=0`.

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE; source-supported by the two-node modal split in Coombes et al. 2026

A zero of the v0.3 antisymmetric **existence** coefficient `B` is not identified with `E_-(1)=0` without a separate orbit-bifurcation argument.

---

## 15. Circulant ring / Fourier reduction

### 15.1 Canonical condition

The project does **not** infer a Floquet reduction from a circulant weight matrix alone.

Let `C` be the cyclic node-shift matrix. The sufficient canonical condition is

\[
\boxed{CM(\mu)=M(\mu)C\quad\forall\mu\text{ in the domain}.}
\tag{V4.37}
\]

Equivalently, in the chosen consistent event-index gauge, the full delayed locked-state operator is circulant. This requires the velocity term and delay/phase/gain-weighted coupling to respect the cyclic action.

Coombes et al. 2026 constructs such a circulant representation for distance-structured ring states. In project terms, displacement-only weights/delays and a twisted base are sufficient only after the event-index/spatiotemporal convention is checked consistently; weights alone are never sufficient evidence.

### 15.2 Exact DFT diagonalisation

If

\[
H_{ij}(\mu)=h_{d}(\mu),\qquad d=i-j\pmod N,
\]

and `D_nu=nu I`, define

\[
\kappa_q=2\pi q/N,
\qquad
\xi_i^{(q)}=e^{i\kappa_q i}.
\]

Then

\[
H(\mu)\xi^{(q)}
=\widehat h_q(\mu)\xi^{(q)},
\]

with

\[
\boxed{
\widehat h_q(\mu)=\sum_{d=0}^{N-1}h_d(\mu)e^{-i\kappa_qd}.
}
\tag{V4.38}
\]

Thus

\[
\boxed{E_q(\mu)=\nu(\mu-1)-\widehat h_q(\mu)=0}
\tag{V4.39}
\]

are exactly the `N` scalar sector equations.

**Label:** THEOREM / PROVED conditional on full circulant operator (V4.37)  
**Provenance:** DERIVATION HERE / standard DFT; source-supported by Coombes et al. 2026 Sect. 6

### 15.3 Base twist versus perturbation sector

Use distinct symbols:

- `q0` — base-state winding/twist label;
- `q` — perturbation Fourier sector.

They are not interchangeable. The full coefficients `h_d` may depend parametrically on `q0`, but DFT diagonalisation is performed in perturbation label `q`.

The uniform global time shift is spatially uniform, hence belongs to perturbation sector

\[
\boxed{q=0.}
\tag{V4.40}
\]

Only the uniform eigenvector at `mu=1` is removed as the guaranteed neutral mode; other `q=0` roots remain physical candidates.

### 15.4 Twisted-state indexing qualification

For a twisted state the physical symmetry can be spatiotemporal. Integer event-label changes can introduce `mu`-dependent similarity factors as in (V4.33). Therefore a code/report must either:

1. exhibit a gauge in which (V4.37) holds, or
2. use the corresponding spatiotemporal / gauge-covariant block reduction.

A claim of ordinary DFT diagonalisation is invalid if only `W` is circulant while the actual delayed locked-state `M(mu)` is not.

### 15.5 N=2 consistency

For `N=2`, DFT sectors are exactly

\[
q=0\leftrightarrow(1,1)^T,
\qquad
q=1\leftrightarrow(1,-1)^T.
\]

Whenever the same full operator satisfies both descriptions,

\[
\boxed{E_{q=0}=E_+,\qquad E_{q=1}=E_-.}
\tag{V4.41}
\]

**Label:** LEMMA / PROVED

---

## 16. Equitable cluster quotient and transverse qualification

Partition nodes into clusters `C_1,...,C_C`. Let `R` be the cluster-indicator matrix. Assume:

- `nu_i=nu_a` for all `i in C_a`;
- for every `a,b` and every `i,i' in C_a`,

\[
\boxed{
\sum_{j\in C_b}H_{ij}(\mu)
=\sum_{j\in C_b}H_{i'j}(\mu)
}
\tag{V4.42}
\]

for all `mu` in the domain.

Then the cluster-constant subspace is invariant and

\[
\boxed{M(\mu)R=R M^Q(\mu),}
\tag{V4.43}
\]

with

\[
M^Q_{ab}(\mu)
=\delta_{ab}\nu_a(\mu-1)-H^Q_{ab}(\mu),
\]

\[
H^Q_{ab}(\mu)=\sum_{j\in C_b}H_{ij}(\mu),\quad i\in C_a.
\tag{V4.44}
\]

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

### Canonical repair of the legacy transverse statement

Equitability alone guarantees the **longitudinal quotient subspace**. It does **not**, for a general nonnormal operator, guarantee that the Euclidean zero-sum-within-cluster complement is itself invariant.

Therefore:

- quotient roots describe longitudinal/cluster-constant modes;
- full stability cannot be certified from the quotient alone;
- a clean independent transverse-sector decomposition requires an additional invariant complement, typically supplied by stronger permutation symmetry / commutation or another explicitly proved block structure.

The blanket legacy statement that zero-average perturbations automatically form transverse invariant sectors under equitability alone is **REPAIRED / NOT RETAINED AS STATED**.

---

## 17. General finite permutation symmetry

Let a finite permutation group `G` act with unitary permutation matrices `P_g`. If

\[
\boxed{P_gM(\mu)=M(\mu)P_g\quad\forall g\in G,\ \forall\mu,}
\tag{V4.45}
\]

then every central isotypic projector commutes with `M(mu)`.

For a complex irreducible representation `rho` of dimension `d_rho` and character `chi_rho`, define

\[
\boxed{
\Pi_\rho=\frac{d_\rho}{|G|}
\sum_{g\in G}\chi_\rho(g)^*P_g.
}
\tag{V4.46}
\]

Then

\[
M(\mu)\operatorname{range}\Pi_\rho
\subseteq\operatorname{range}\Pi_\rho.
\tag{V4.47}
\]

**Label:** THEOREM / PROVED conditional on commutation (V4.45)  
**Provenance:** standard finite-group representation theory / DERIVATION CHECKED HERE

Qualifications:

- an isotypic component can contain multiple copies of the same irrep; projection does not imply a scalar sector;
- for real formulations, complex-conjugate irreps may need to be paired into real invariant blocks;
- only the isotropy/spatiotemporal symmetry preserved by the **locked delayed state** may be used, not the full symmetry group of the naked weight graph.

---

## 18. Continuum / large-ring limit

The legacy schematic limit from discrete ring symbols to a continuum Fourier integral is mathematically plausible under a controlled quadrature scaling, regular kernels/delays and a fixed physical wave-number convention, and it is consistent with the continuum stability perspective in Coombes 2025.

This gate does not prove the required uniform convergence of the full nonlinear characteristic/root problem.

Classification:

`OPEN QUESTION / CONDITIONAL ASYMPTOTIC PROGRAM`.

No ring-to-continuum numerical convergence or root convergence is canonicalised here.

---

## 19. Dynamic critical labels

After identifying and excluding only the guaranteed global time-shift eigenpair:

- **unit / steady critical candidate:** an additional nontrivial multiplier at `mu=+1`;
- **period-doubling candidate:** a real nontrivial multiplier at `mu=-1`;
- **Neimark–Sacker candidate:** a nonreal conjugate pair `mu,conj(mu)` with `|mu|=1` and `mu != ±1`.

**Label:** PROJECT DEFINITIONS / standard map terminology.

For an actual local bifurcation theorem one additionally needs the appropriate simplicity, transverse crossing, absence of other unintended critical multipliers and nonlinear nondegeneracy; Neimark–Sacker conclusions also require the relevant resonance/nonlinear hypotheses. Those are not established here.

No actual Lighthouse unit/PD/NS point is classified in this gate.

---

## 20. C1 / C2 / C3 / C5 disposition by claim

| Claim/material | Class | Epistemic disposition |
|---|---|---|
| locked spike-time/local-cycle representation | C1 | PROPOSITION / PROVED |
| moving-limit spike-time linearisation | C1 | PROPOSITION / PROVED under V4 assumptions |
| lag recurrence (V4.10) | C1 | PROPOSITION / PROVED |
| source-aligned difference form and row-sum cancellation | C1 | LEMMA / PROVED |
| nonlinear multiplier operator on convergent lag domain | C1 | PROPOSITION / PROVED |
| alpha lag convergence domain `|mu|>exp(-alpha T)` | C1 | LEMMA / PROVED |
| exact neutral `mu=1`, `xi=1` | C1 | THEOREM / PROVED |
| weighted-comb / lag-sum equivalence in convergence domain | C1 | PROPOSITION / PROVED |
| alpha weighted-comb closed form | C1 | LEMMA / PROVED away from arrivals |
| meromorphic alpha continuation as algebraic function | C1 | PROPOSITION / PROVED algebraically |
| interpreting continuation outside the lag domain as complete physical spectrum | C5/C2 | NOT ESTABLISHED; requires equivalence validation |
| full hybrid-state spectral completeness of spike-time operator | C5/C2 | OPEN / validation required |
| multiplier/exponent conversion | C1 | PROPOSITION / PROVED |
| simple-root sensitivity denominator with normalised vectors | C1 | PROPOSITION / PROVED |
| production nonlinear-root conditioning metric | C2 | later validation/implementation |
| two-cell symmetric/antisymmetric reduction under full exchange symmetry | C1 | PROPOSITION / PROVED |
| DFT ring reduction under full circulant `M(mu)` | C1 | THEOREM / PROVED conditionally |
| automatic circulancy from weights alone | C5 / REJECT | insufficient |
| twisted-state ordinary-circulant gauge without checking event indexing | C5 | must be demonstrated/gauge-qualified |
| N=2 ring/two-cell equivalence | C1 | LEMMA / PROVED when same operator |
| equitable longitudinal quotient | C1 | PROPOSITION / PROVED |
| automatic zero-sum transverse invariant complement from equitability alone | C5 / REJECT AS STATED | needs stronger symmetry/invariant complement |
| finite permutation isotypic reduction | C1 | THEOREM / PROVED conditional on commutation |
| continuum ring limit/root convergence | C5 | OPEN / later asymptotic gate |
| unit/PD/NS terminology | C1 definition | conditional labels only |
| any actual Lighthouse multiplier/stability boundary | C3 | no governed result; preregistered computation required |

---

## 21. Legacy B23–B40 disposition

No legacy tolerance is adopted here and no benchmark is executed.

| Legacy ID | Topic | Canonical disposition for later work |
|---|---|---|
| B23 | neutral time-translation multiplier | ELIGIBLE for later finite pre-execution contract; high-priority exact structural test |
| B24 | recurrence vs direct finite perturbation | REPAIR then eligible: use predetermined regular orbit and fixed perturbation amplitudes; no post-output `eps`/fit-window selection |
| B25 | alpha weighted derivative comb | ELIGIBLE with explicit `|mu|>r` lag-domain cases; meromorphic-continuation cases must be labelled separately |
| B26 | lag-sum vs weighted-comb characteristic matrix | ELIGIBLE only inside common absolute-convergence domain with fixed lag cutoffs/convergence rule fixed before execution |
| B27 | two-cell reduction | ELIGIBLE for operator/block checks; actual root matching deferred to governed root-infrastructure test |
| B28 | ring DFT diagonalisation | ELIGIBLE only after full-operator circulancy/event-index gauge is fixed; weights alone insufficient |
| B29 | dense roots vs Fourier-sector roots | DEFER to governed nonlinear-root infrastructure; C2 |
| B30 | N=2 ring vs two-cell | ELIGIBLE exact structural cross-check |
| B31 | cluster quotient invariance | REPAIR then eligible: test longitudinal quotient only under (V4.42); do not infer automatic transverse complement |
| B32 | transverse cluster instability detection | DEFER/REPAIR: use a predetermined synthetic symmetry block after root infrastructure; no searched Lighthouse effect |
| B33 | multiplier/exponent convention | ELIGIBLE exact finite test with explicit log branches |
| B34 | nonlinear root solver on synthetic matrix functions | ELIGIBLE later C2 infrastructure contract; no Lighthouse roots |
| B35 | nonlinear-eigenvalue conditioning | REPAIR then eligible with fixed left/right normalisation and simple-root cases |
| B36 | event-time vs flow/saltation spectrum | DEFER; full-state/event-time equivalence not frozen and legacy sweep is outside current authority |
| B37 | continuation/Floquet sector alignment at actual symmetry breaking | DEFER; requires governed actual branch/bifurcation result |
| B38 | lag-tail / neutral-residual convergence | ELIGIBLE later with one predetermined case, fixed cutoff ladder and no adaptive result-based truncation |
| B39 | ring-to-continuum dispersion convergence | DEFER to separate continuum/asymptotic layer |
| B40 | mode-selection atlas along branch | DEFER; effect-bearing branch/root/stability atlas work |

---

## 22. Explicit exclusions

This gate does not freeze, validate, execute or infer:

- any B23–B40 output or legacy tolerance;
- any actual Lighthouse multiplier/root;
- any stable/unstable label for a Lighthouse branch;
- any actual unit, period-doubling or Neimark–Sacker point;
- any stability-boundary location or parameter sweep;
- any v0.3 legacy fold/pitchfork location;
- full spike-time / flow-saltation spectral equivalence;
- auxiliary alpha-state Floquet-mode completeness;
- continuum/root convergence;
- production/JAX nonlinear-root solvers;
- v0.5 normal forms or coefficients;
- v0.6+ legacy numerical science;
- adaptive-delay execution;
- inference, observation design, active experiment design, applications, novelty positioning, manuscript claim freeze or v0.27.

The legacy branch remains read-only recovery evidence.

---

## 23. Gate decision

\[
\boxed{\text{PASS}}
\]

Reason:

1. the spike-time recurrence is independently re-derived including moving integration limits;
2. the source-aligned diagonal/difference term is reconciled by an explicit periodic row-sum cancellation proof rather than omitted by convention;
3. the nonlinear characteristic operator is derived with an explicit convergence domain;
4. the exact neutral global shift mode is proved;
5. the alpha weighted derivative comb is independently summed, with the correct `|mu|>exp(-alpha T)` series domain and a strict distinction between convergent identity and meromorphic continuation;
6. arrival-boundary one-sided semantics are aligned with RB-007/RB-009;
7. multiplier/exponent conventions and simple-root conditioning are repaired/qualified;
8. two-cell and DFT reductions are proved only under symmetry of the full characteristic operator;
9. twisted-state/event-index gauge covariance is made explicit;
10. cluster equitability is narrowed to the longitudinal quotient, repairing the legacy overstatement about automatic transverse zero-sum sectors;
11. finite-group isotypic reduction is retained only under full-operator commutation and base-state isotropy;
12. continuum convergence and all effect-bearing root/stability claims remain deferred;
13. no B23–B40 execution or actual multiplier calculation occurred.

PASS means only that MASTER may decide whether to establish a narrow `CORE v0.4 Floquet Theory Freeze 0.1`.

---

## 24. Proposed contents of `CORE v0.4 Floquet Theory Freeze 0.1`

If MASTER authorises a freeze, proposed frozen contents are limited to:

1. assumptions V4-A1–V4-A8;
2. base/local-cycle representation (V4.1)–(V4.3);
3. spike-time perturbation derivation (V4.4)–(V4.10);
4. source-aligned difference form and exact row-sum cancellation (V4.11)–(V4.13);
5. cycle multiplier operator and convergence-domain statements (V4.14)–(V4.19);
6. exact neutral mode (V4.20)–(V4.21);
7. weighted derivative comb and alpha formulas (V4.22)–(V4.26), including the convergent-series/meromorphic-continuation distinction;
8. multiplier/exponent convention (V4.27)–(V4.28);
9. normalised simple-root conditioning/sensitivity statements (V4.29)–(V4.31);
10. existence/dynamic/event/chart taxonomy;
11. event-index relabelling covariance (V4.32)–(V4.33);
12. two-cell reduction (V4.34)–(V4.36);
13. full-operator circulant condition and DFT reduction (V4.37)–(V4.41), with twist/event-index qualification;
14. equitable longitudinal quotient (V4.42)–(V4.44) plus explicit rejection of automatic transverse-complement invariance under equitability alone;
15. finite permutation-symmetry/isotypic reduction (V4.45)–(V4.47) under full-operator commutation;
16. conditional unit/PD/NS terminology and explicit exclusions;
17. C1/C2/C3/C5 classifications and B23–B40 disposition matrix.

Explicitly excluded from the proposed freeze are all actual Lighthouse roots/stability labels, numerical root infrastructure, B23–B40 outputs, full-state spectrum equivalence, continuum convergence and v0.5+ science.

---

## 25. Open questions / proposed MASTER sequencing

1. Whether MASTER accepts this narrowed/repaired theory and establishes `CORE v0.4 Floquet Theory Freeze 0.1`.
2. If frozen, whether the next action should be a finite **v0.4 Floquet Validation Contract Canonicalization Gate** covering only C2-eligible structural/analytic tests (e.g. repaired B23–B35/B38 subset) before any actual Lighthouse stability search.
3. Whether a separate mathematical equivalence gate is needed for spike-time versus full alpha-state/flow-saltation spectra before any statement of complete hybrid-orbit stability.
4. Whether twisted-ring spatiotemporal symmetry should receive a dedicated event-index/gauge theorem before large-ring root computation.
5. Whether continuum/ring convergence should be sequenced after the finite-network Floquet layer rather than folded into v0.4 validation.
6. Any actual Lighthouse stability-boundary experiment should receive a later pre-execution contract with branch points, parameter windows, root-count regions and acceptance criteria fixed before outputs are inspected.

No second gate is started here.

---

## 26. STOP

`CORE v0.4 Floquet Theory Canonicalization Gate 0.1` is complete.

No B23–B40 benchmark was executed. No actual Lighthouse multiplier/root or stability boundary was computed. No v0.5+ or downstream science was started.

STOP — RETURN TO MASTER
