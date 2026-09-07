# CORE Mathematical Scope Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — ORIGINAL SCOPE GATE RECONSTRUCTED; PROPOSED FREEZE ONLY

## 1. Scope and recovery provenance

This gate reconstructs the originally missing `CORE Mathematical Scope Gate 0.1` from the frozen legacy recovery input at commit

`287eae8a86560b78ed94f30a2786243714c33ac0`

and from independently checked primary / authoritative mathematical sources.

Authoritative governance inputs:

- `PROJECT_GOVERNANCE.md`
- `research/master/core_legacy_recovery_snapshot_0_1.md`
- `research/core/recovery_canonicalization_gate_0_1.md`
- `research/master/prompts/core_mathematical_scope_gate_0_1.md`
- `research/master/prompts/core_mathematical_scope_canonicalization_gate_0_1.md`

Frozen legacy foundational inputs used only as recovery candidates:

- `docs/core/mathematical_core.md`
- `docs/core/derivations_v0.2.md`
- `docs/core/research_program.md` only for historical scope / variant / open-question identification

No v0.3–v0.26 numerical result, implementation result, benchmark label, continuation result, active-design result, inference result, or branch-local `COMPLETE / VERIFIED / CERTIFIED` label is used as evidence in this gate.

The result of this gate is one proposed deterministic mathematical baseline and a set of independently re-derived elementary analytical identities. `PASS` here means only that MASTER has enough source-audited material to decide whether to authorize `CORE Mathematical Freeze 0.1`.

---

## 2. Precise primary-source map

### S1 — Haken original model article

H. Haken, **“Quasi-Discrete Dynamics of a Neural Net: The Lighthouse Model,”** *Discrete Dynamics in Nature and Society* 4 (2000), 187–200. DOI: `10.1155/S1026022600000182`.

Primary-source locators:

- Section 1, **“THE MODEL”**, pp. 187–190.
- Eq. (1): dendritic-current dynamics driven by delayed axonal pulses, with damping and noise.
- Eqs. (2)–(5): axonal pulse represented through a periodic sharply peaked function of a phase.
- Eq. (6): phase velocity driven by a nonlinear response function `S`.
- Eq. (7): neuronal input assembled from coupled dendritic currents, explicit delays, and external input.
- The paper then develops phase locking and perturbation dynamics for two and many neurons.

Use in this gate: **original Lighthouse architecture**, pulse/phase/dendritic-current separation, delay concept, thresholded response concept, and historical phase-locking provenance.

### S2 — Haken original delayed phase-locking paper

H. Haken, **“Phase Locking in the Lighthouse Model of a Neural Net with Several Delay Times,”** *Progress of Theoretical Physics Supplement* 139 (2000), 96–111. DOI: `10.1143/PTPS.139.96`.

Primary-source locator: pp. 96–111; the paper explicitly treats an `N`-neuron pulse-coupled Lighthouse network with general coupling and several delays, including exact phase-locked states and their stability.

Use in this gate: **primary provenance for fixed communication delays and phase-locked Lighthouse states**. No stability formula from this source is frozen here.

### S3 — Haken monograph consolidation

H. Haken, **Brain Dynamics: Synchronization and Activity Patterns in Pulse-Coupled Neural Nets with Delays and Noise**, Springer, 2002. DOI: `10.1007/978-3-540-46284-2`.

Primary-source locators:

- Chapter 5, **“The Lighthouse Model. Two Coupled Neurons,”** pp. 77–101.
  - Eq. (5.6): spike-train representation by phase crossings / delta peaks.
  - Eq. (5.7): Naka–Rushton response.
  - Eqs. (5.8)–(5.9): phase-rate formulation.
  - Eq. (5.10): coupled dendritic input with delays and external drive.
- Chapter 6, **“The Lighthouse Model. Many Coupled Neurons,”** pp. 103–139.
  - Eq. (6.2): general synaptic-kernel relation.
  - Eq. (6.3): many-neuron phase dynamics with coupling, delay, threshold / response, external drive and noise.

Use in this gate: **primary consolidation of the Lighthouse equations and response / input conventions**.

### S4 — authoritative later Lighthouse reformulation

C. C. Chow and S. Coombes, **“Existence and Wandering of Bumps in a Spiking Neural Network Model,”** *SIAM Journal on Applied Dynamical Systems* 5(4) (2006), 552–574. DOI: `10.1137/060654347`.

Locator: Section 2, especially Eqs. (2.1)–(2.2).

This paper reformulates the Lighthouse model as a pulse-coupled phase system with causal normalized synaptic kernel and explicitly distinguishes the two historical reset conventions: immediate reset when input falls below threshold versus no such reset.

Use in this gate: **later mathematical reconstruction and reset-variant clarification**.

### S5 — contemporary graph / alpha-kernel reformulation

S. Coombes, **“Revisiting the Haken Lighthouse model,”** *European Physical Journal Special Topics* 235 (2026), 4571–4593; online publication 19 August 2025. DOI: `10.1140/epjs/s11734-025-01841-3`.

Precise locators:

- Section 2, Eq. (1): graph Lighthouse model
  `dot(theta_i)=S(psi_i)`, `psi_i=sum_j w_ij a_j(t-tau_ij)`, `a_i=sum_m eta(t-T_i^m)`.
- Section 2, Eq. (2): firing-section definition using lifted / modulo phase.
- Section 2, Eq. (3): smooth threshold response used in the revisit.
- Section 2, Eq. (4): normalized continuous alpha kernel `alpha^2 t exp(-alpha t) H(t)`.
- Section 3.1, Eqs. (5)–(8): periodic synaptic waveform, Fourier representation, alpha-kernel transform, and period integral.
- Section 3.1, Eqs. (9)–(11): balanced and linear-response period relations.
- Section 3.3, Eqs. (31)–(32) and following jump rule: equivalent alpha-kernel state-space representation with state `(theta,a,u)` and firing jump `u -> u+alpha`.

Use in this gate: **authoritative contemporary graph reconstruction**, exact event convention, the no-reset-below-threshold version used in the revisit, continuous alpha kernel, and its exact state-space realization.

### S6 — adaptive-delay work, registry only

S. Coombes, R. Thul, S. Ruschel, R. Nicks, **“Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks,”** arXiv:2606.21508 (2026).

Use in this gate: **variant registry only**. No adaptive-delay equation or result is part of the proposed baseline freeze.

### Source-discipline conclusion

The structural lineage is therefore:

`Haken original pulse / dendrite / phase architecture [S1,S2,S3]`

`-> later explicit normalized-kernel / reset reconstruction [S4]`

`-> modern delayed graph and alpha-kernel reformulation [S5]`

`-> project canonicalization below`.

No equivalence is inferred merely from notation. Where the project changes variables or chooses one historical / modern variant, the change is explicitly proved or labelled as a project choice.

---

## 3. Original vs reformulation vs project distinction

| Item | Haken original | Later reformulation | Project canonicalization in this gate |
|---|---|---|---|
| neuron state | phase `phi` | lifted / angular `theta_i` | lifted `theta_i in R` |
| spike representation | phase-generated pulse / delta train | firing times `T_i^m` | first hitting of `theta_i=2 pi m` |
| response | thresholded quasi-linear saturating; Naka–Rushton used | smooth threshold `S` or Heaviside / linear variants | smooth Coombes response is baseline |
| synapse | dendritic-current ODE; exponential response historically | general causal normalized kernel; alpha kernel in modern revisit | alpha kernel is baseline |
| delay | explicit fixed transmission delays | edgewise fixed `tau_ij` | edgewise fixed `tau_ij >= 0` |
| reset below threshold | historical variants exist | both variants made explicit | **no reset below threshold** |
| firing reset | phase / pulse convention | lifted-angle representation | no reset of lifted `theta`; wrapped subtraction by `2 pi` is coordinate-only |
| external drive | allowed in Haken equations | may be added | excluded from baseline; registered variant |
| noise | present in Haken treatments | optional | excluded from baseline |
| alpha state | not Haken original | `(a,u)`, `u+=u+alpha` in S5 | rescaled `q=alpha u`; exact equivalence proved below |
| adaptive delay | not baseline Haken model | later extension | deferred variant only |

The canonical choices above are not selected because of any downstream v0.3–v0.26 effect size. They are selected because they give one explicit deterministic version already supported by the authoritative modern reformulation [S5], while preserving a transparent map back to the Haken architecture.

---

## 4. Proposed canonical baseline equations and notation

### 4.1 Graph objects

Let

`G=(V,E)`, `V={1,...,N}`,

be a finite directed graph. For every ordered pair `(j -> i)` let

- `w_ij in R` be the fixed coupling weight from neuron `j` to neuron `i`;
- `tau_ij >= 0` be its fixed communication delay.

Self-edges are permitted unless a later experiment explicitly excludes them.

### 4.2 Lifted phase and synaptic input

For each neuron `i`,

\[
\theta_i(t)\in\mathbb R
\]

is a lifted angular phase and

\[
\psi_i(t)\in\mathbb R
\]

is its total synaptic input.

The baseline flow is

\[
\boxed{\dot\theta_i(t)=S_{r,h}(\psi_i(t))}
\tag{C1}
\]

with

\[
\boxed{
S_{r,h}(x)=
\begin{cases}
0,&x\le h,\\
\exp[-r/(x-h)^2],&x>h,
\end{cases}
\qquad r>0 .}
\tag{C2}
\]

Thus `0 <= S < 1`, `S` is thresholded, monotone above threshold, smooth through the threshold when extended by zero, and saturates to one in the chosen nondimensionalization.

### 4.3 Baseline alpha synapse

Choose one global synaptic rate

\[
\alpha>0.
\]

The normalized causal alpha kernel is

\[
\boxed{
\eta_\alpha(t)=\alpha^2 t e^{-\alpha t}H(t),
\qquad
\int_0^\infty\eta_\alpha(t)\,dt=1 .}
\tag{C3}
\]

For firing times `T_j^m`, define the presynaptic activation

\[
\boxed{
a_j(t)=\sum_m\eta_\alpha(t-T_j^m).}
\tag{C4}
\]

The network input is

\[
\boxed{
\psi_i(t)=\sum_{j=1}^N w_{ij}\,a_j(t-\tau_{ij}).}
\tag{C5}
\]

Equivalently, each spike of neuron `j` contributes the alpha waveform on edge `j -> i` starting at arrival time `T_j^m+tau_ij`.

### 4.4 Exact local state-space realization of the kernel

For each presynaptic neuron, define project variable

\[
q_j=\alpha u_j,
\]

where `u` is the contemporary S5 variable. Between spikes,

\[
\boxed{
\dot q_j=-\alpha q_j,
\qquad
\dot a_j=-\alpha a_j+q_j .}
\tag{C6}
\]

At a spike of neuron `j`,

\[
\boxed{
q_j^+=q_j^-+\alpha^2,
\qquad
a_j^+=a_j^- .}
\tag{C7}
\]

Section 9 proves that (C6)–(C7) are exactly equivalent to convolution with (C3).

### 4.5 Nondimensionalization

The baseline is nondimensional except for the explicit bookkeeping of the numerical time coordinate.

- `theta` is an angle measured in radians and is dimensionless.
- The chosen time unit makes the saturation value of `S` equal to one radian per time unit.
- `alpha` has inverse-time units relative to this time coordinate.
- `tau_ij` has time units.
- `eta` is normalized to unit area; if physical input units are later restored, the weight scale absorbs the corresponding kernel/time normalization.

No physical biophysical calibration is frozen in Scope 0.1.

---

## 5. Event / spike / reset convention

Let `n_i` be the integer spike counter and suppose the current target section is `2 pi (n_i+1)`.

A spike is the **first hitting time**

\[
\boxed{
T_i^{n_i+1}
=
\inf\{t>T_i^{n_i}:\theta_i(t)=2\pi(n_i+1)\}.}
\tag{C8}
\]

At a regular event:

\[
\boxed{n_i^+=n_i^-+1,}
\tag{C9}
\]

and the outgoing synaptic state receives (C7).

The lifted phase itself is **not reset**:

\[
\theta_i^+=\theta_i^-.
\]

A wrapped implementation may replace `theta_i` by `theta_i-2 pi` at a spike; this is only a coordinate representation of the same lifted trajectory.

The baseline specifically excludes the historical variant in which the phase is reset to zero whenever the input drops below threshold. That convention remains in the variant registry.

A regular firing event must satisfy transversality

\[
\boxed{
\dot\theta_i(T_i^m^-)=S_{r,h}(\psi_i(T_i^m^-))>0 .}
\tag{C10}
\]

For differentiable event-time calculations, simultaneous event collisions are not part of the regular-event chart.

---

## 6. Synaptic and fixed-delay definitions

The baseline delay semantics are strictly fixed and emission-independent:

\[
\boxed{
(j\to i)\text{ spike emitted at }T_j^m
\quad\Rightarrow\quad
\text{edge contribution }w_{ij}\eta_\alpha(t-T_j^m-\tau_{ij}).}
\tag{C11}
\]

Thus propagation changes only the argument of the fixed kernel. `tau_ij` is not updated while a spike is in flight, does not depend on activity, and has no plasticity state in this freeze.

For delayed equations, the initial data must contain a locally finite prespike history sufficient to evaluate all delayed activations over `[-tau_max,0]`, or an exactly equivalent history representation.

---

## 7. Baseline assumptions table

| ID | Assumption | Status / provenance |
|---|---|---|
| A1 | finite directed graph with fixed `N` | PROJECT ASSUMPTION |
| A2 | fixed real weights `w_ij`; signs may be excitatory or inhibitory | SOURCE-DERIVED / PROJECT CANONICALIZATION |
| A3 | fixed edge delays `tau_ij>=0` | SOURCE-DERIVED |
| A4 | deterministic baseline: no stochastic forcing | PROJECT ASSUMPTION / EXCLUSION |
| A5 | no external drive in the baseline | PROJECT ASSUMPTION / EXCLUSION |
| A6 | no reset when input falls below threshold | SOURCE-SUPPORTED VARIANT CHOICE |
| A7 | response is exactly (C2) with `r>0` | CONTEMPORARY REFORMULATION / PROJECT CHOICE |
| A8 | synapse is exactly normalized alpha kernel (C3) with one `alpha>0` | CONTEMPORARY REFORMULATION / PROJECT CHOICE |
| A9 | spike history before initial time is locally finite | PROJECT WELL-POSEDNESS ASSUMPTION |
| A10 | regular-event analysis uses first hitting and transversality (C10) | DERIVATION HERE / STANDARD HYBRID ASSUMPTION |
| A11 | simultaneous-event collisions are excluded from local derivative formulae | PROJECT ASSUMPTION |
| A12 | all numerical time / input scales are nondimensional until separately calibrated | PROJECT NORMALIZATION |
| A13 | row-sum balance, synchrony, autapses, rings, etc. are **not** global baseline assumptions; they are special validation geometries | PROJECT SCOPE BOUNDARY |

Because (C2) satisfies `0<=S<1`, each neuron needs at least `2 pi` time units to accumulate another `2 pi` of phase. For a finite graph and locally finite prehistory this rules out spike-time Zeno accumulation in the baseline model.

---

## 8. Formal variant registry

| Variant ID | Component | Variant | Relation to baseline | Status |
|---|---|---|---|---|
| V-R0 | reset | immediate reset to zero whenever input is below / falls below threshold | historical alternative | deferred |
| V-R1 | reset | no reset below threshold; lifted phase | **baseline** | selected |
| V-S0 | response | Haken Naka–Rushton / Hill-with-cutoff response | original response family | retained variant |
| V-S1 | response | smooth threshold response (C2) | **baseline** | selected |
| V-S2 | response | linear mid-range `S_L(x)=gamma x-Theta` | exact analytical benchmark variant | retained |
| V-S3 | response | Heaviside response | later mathematical simplification | retained variant |
| V-K0 | synapse | exponential `alpha exp(-alpha t) H(t)` | Haken historical kernel | retained variant |
| V-K1 | synapse | alpha kernel (C3) | **baseline** | selected |
| V-K2 | synapse | general causal normalized kernel with Fourier transform | umbrella mathematical class | deferred generalization |
| V-D0 | delays | zero delay | special case | retained |
| V-D1 | delays | one common fixed delay | special case / validation geometry | retained |
| V-D2 | delays | edgewise fixed delays (C11) | **baseline** | selected |
| V-D3 | delays | activity-dependent / adaptive conduction delay | later extension [S6] | explicitly deferred |
| V-D4 | delays | causal in-flight state-dependent propagation semantics | recovered project extension | v0.13+ legacy; explicitly deferred |
| V-I0 | drive | no external drive | **baseline** | selected |
| V-I1 | drive | additive deterministic external drive | Haken-supported / project extension | retained variant |
| V-N0 | noise | deterministic | **baseline** | selected |
| V-N1 | noise | additive / multiplicative noise | Haken-studied extension | deferred |
| V-C0 | geometry | finite graph | **baseline** | selected |
| V-C1 | geometry | continuum / neural field | modern extension | deferred |
| V-P0 | plasticity | fixed weights and delays | **baseline** | selected |
| V-P1 | plasticity | STDP / weight plasticity / myelination | later extension | deferred |

No variant is selected here on the basis of a downstream numerical effect size.

---

## 9. Independently verified C1 derivations

All results in this section were re-derived for this gate. Branch-local `COMPLETE` labels are not used as proof.

### 9.1 Alpha-kernel normalization

**Label:** LEMMA / PROVED  
**Provenance:** SOURCE-DERIVED + DERIVATION HERE

For `alpha>0`,

\[
\int_0^\infty \alpha^2 t e^{-\alpha t}\,dt
=\alpha^2\frac{1}{\alpha^2}=1.
\]

Hence (C3) is normalized.

### 9.2 Alpha-kernel state-space equivalence and jump normalization

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED + DERIVATION HERE; `q=alpha u` is PROJECT CANONICALIZATION

Start from zero state and apply one spike at `t=0`. From (C6)–(C7),

\[
q(0^+)=\alpha^2,
\qquad
q(t)=\alpha^2 e^{-\alpha t},\quad t>0.
\]

The second state obeys

\[
\dot a+\alpha a=q,
\qquad a(0^+)=0.
\]

Multiplying by `e^{alpha t}` gives

\[
\frac{d}{dt}(e^{\alpha t}a)=\alpha^2,
\]

so

\[
a(t)=\alpha^2 t e^{-\alpha t}=\eta_\alpha(t).
\]

By linear superposition, a spike train produces

\[
a(t)=\sum_m\eta_\alpha(t-T^m).
\]

Thus (C6)–(C7) are exactly equivalent to convolution with (C3), not an approximation.

The S5 variables satisfy

\[
\dot a=-\alpha a+\alpha u,
\qquad
\dot u=-\alpha u,
\qquad
u^+=u^-+\alpha.
\]

Setting `q=alpha u` yields precisely (C6)–(C7). Therefore the project state is a proved rescaling of the contemporary state-space realization.

### 9.3 Periodic kernel-comb unit-mass identity

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

For period `T>0`, define

\[
R_T(t)=\sum_{m\in\mathbb Z}\eta(t-mT).
\tag{D1}
\]

Index shifting gives `R_T(t+T)=R_T(t)`. For the nonnegative normalized baseline kernel, Tonelli's theorem permits

\[
\begin{aligned}
\int_0^T R_T(s)\,ds
&=\sum_m\int_0^T\eta(s-mT)\,ds\\
&=\sum_m\int_{-mT}^{(1-m)T}\eta(u)\,du\\
&=\int_{-\infty}^{\infty}\eta(u)\,du\\
&=1.
\end{aligned}
\tag{D2}
\]

This identity is independent of the detailed waveform.

### 9.4 Exact periodic alpha-kernel comb

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

Let

\[
u=t\bmod T\in[0,T),
\qquad
\rho=e^{-\alpha T}.
\]

Causality gives

\[
R_T(t)
=\alpha^2 e^{-\alpha u}
\sum_{n=0}^\infty (u+nT)\rho^n.
\]

Using

\[
\sum_{n=0}^\infty\rho^n=\frac1{1-\rho},
\qquad
\sum_{n=0}^\infty n\rho^n=\frac{\rho}{(1-\rho)^2},
\]

we obtain

\[
\boxed{
R_T(t)=\alpha^2e^{-\alpha u}
\left[
\frac{u}{1-\rho}+
\frac{T\rho}{(1-\rho)^2}
\right].}
\tag{D3}
\]

### 9.5 Exact periodic hybrid alpha state

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED + DERIVATION HERE

Use the S5 `u`-state. Immediately after a spike, periodicity requires

\[
u^+=e^{-\alpha T}u^++\alpha.
\]

Hence

\[
\boxed{u^+=\frac{\alpha}{1-\rho}.}
\tag{D4}
\]

Between spikes,

\[
u(t)=u^+e^{-\alpha t}.
\]

Solving `dot a=-alpha a+alpha u` gives

\[
a(t)=e^{-\alpha t}[a^++\alpha u^+t].
\]

Continuity plus periodicity requires

\[
a^+=e^{-\alpha T}[a^++\alpha u^+T],
\]

thus

\[
\boxed{a^+=\frac{\alpha^2T\rho}{(1-\rho)^2}.}
\tag{D5}
\]

Substitution gives exactly (D3). With `q=alpha u`,

\[
q^+=\frac{\alpha^2}{1-\rho}.
\]

### 9.6 Isolated Lighthouse clock

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED STRUCTURE + DERIVATION HERE

With no recurrent input, `psi=0`, so

\[
\dot\theta=S(0).
\]

If `S(0)>0`, the time required for a `2 pi` phase increment is

\[
\boxed{T_0=\frac{2\pi}{S(0)}.}
\tag{D6}
\]

If `S(0)=0`, the deterministic no-reset-below-threshold isolated neuron is quiescent.

For the linear benchmark response

\[
S_L(x)=\gamma x-\Theta,
\]

with `-Theta>0`,

\[
\boxed{T_0=-\frac{2\pi}{\Theta}.}
\tag{D7}
\]

### 9.7 Delayed autapse period relation

**Label:** PROPOSITION / PROVED  
**Provenance:** DERIVATION HERE

For one neuron with self-weight `w`, fixed delay `tau`, and periodic firing period `T`,

\[
\psi(t)=wR_T(t-\tau).
\]

The phase must advance by `2 pi` in one cycle:

\[
\boxed{
2\pi=\int_0^T S(wR_T(s-\tau))\,ds.}
\tag{D8}
\]

Because the integrand is `T`-periodic, the full-period integral is invariant under the shift `tau`. Therefore delay does not alter this scalar existence integral. It may still alter first-hitting admissibility and stability, so no stronger statement is frozen.

For `S_L(x)=gamma x-Theta`, (D2) gives

\[
2\pi=\gamma w-\Theta T,
\]

hence

\[
\boxed{T=\frac{\gamma w-2\pi}{\Theta},}
\tag{D9}
\]

provided `T>0`, the assumed linear operating range is valid, and first hitting holds.

### 9.8 General one-spike-per-cycle phase-locked self-consistency

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED CONCEPT + DERIVATION HERE

Assume

\[
T_i^m=mT+\phi_i.
\tag{D10}
\]

In neuron `i`'s local cycle coordinate `t=mT+phi_i+s`, `0<=s<T`, the activation arriving from neuron `j` is

\[
R_T(s+\phi_i-\phi_j-\tau_{ij}).
\]

Therefore

\[
\psi_i^{PL}(s)
=\sum_jw_{ij}R_T(s+\phi_i-\phi_j-\tau_{ij}).
\tag{D11}
\]

Integrating the phase equation over one firing cycle gives

\[
\boxed{
2\pi=
\int_0^T
S\!\left(
\sum_jw_{ij}R_T(s+\phi_i-\phi_j-\tau_{ij})
\right)ds,
\quad i=1,\ldots,N.}
\tag{D12}
\]

Only relative offsets matter. The transformation

\[
\phi_i\mapsto\phi_i+c
\]

leaves every equation invariant, so one offset must be fixed to remove the global time-translation gauge.

### 9.9 Linear-response row-sum identity

**Label:** PROPOSITION / PROVED  
**Provenance:** SOURCE-DERIVED STRUCTURE + DERIVATION HERE

For the linear benchmark response, (D12) and (D2) yield

\[
2\pi
=\gamma\sum_jw_{ij}-\Theta T.
\tag{D13}
\]

Hence a common period requires equal relevant row sums. If

\[
\sum_jw_{ij}=\Gamma
\quad\forall i,
\]

then

\[
\boxed{T=\frac{\gamma\Gamma-2\pi}{\Theta}.}
\tag{D14}
\]

For `Gamma=0`, `Theta<0`,

\[
\boxed{T=\frac{2\pi}{|\Theta|}.}
\tag{D15}
\]

Offsets and fixed delays drop out of the **linear existence integral**; they are not thereby irrelevant to admissibility or stability.

### 9.10 First-hitting / admissibility condition

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

For a candidate interspike interval `T`, define accumulated phase

\[
A(t)=\int_0^t S(\psi(s))\,ds.
\]

The prescribed firing at `T` is the next event iff

\[
\boxed{A(T)=2\pi}
\tag{D16}
\]

and

\[
\boxed{A(t)<2\pi\quad\text{for every }0<t<T.}
\tag{D17}
\]

This is simply the definition of first hitting. If `S(psi(t))>0` throughout the cycle, strict monotonicity makes (D17) automatic once (D16) holds. Threshold plateaus require the explicit check.

### 9.11 Elementary event-time perturbation formula

**Label:** LEMMA / PROVED  
**Provenance:** DERIVATION HERE

Let a regular reference event occur at `T`, with

\[
\theta(T)=2\pi m,
\qquad
\dot\theta(T)\ne0.
\]

Perturb the trajectory by `delta theta` and the event time by `delta T`. Expanding the perturbed event condition gives

\[
0
=\delta\theta(T)+\dot\theta(T)\,\delta T+o(\|\delta\|).
\]

Therefore

\[
\boxed{
\delta T=-\frac{\delta\theta(T)}{\dot\theta(T)}.}
\tag{D18}
\]

Equivalently, for an event function `g(t,p)=0`,

\[
\partial_pT=-\frac{\partial_pg}{\partial_tg}
\]

whenever `partial_t g != 0`. No v0.3+ Floquet or numerical result is needed for this elementary identity.

---

## 10. Analytical validation targets

The following are targets that a future implementation / replay gate may test. They are **not** executed here.

1. **Kernel impulse target:** one spike under (C6)–(C7) must produce (C3) exactly.
2. **Kernel area target:** numerical / symbolic integration should recover unit area.
3. **Periodic-comb target:** a periodic spike train should reproduce (D3) and the unit-mass identity (D2).
4. **Periodic-state target:** post-spike alpha states must match (D4)–(D5).
5. **Isolated-clock target:** conditional period (D6).
6. **Autapse target:** periodic existence relation (D8), and (D9) in the linear benchmark regime.
7. **Synchronous row-sum target:** (D14)–(D15) where the special assumptions apply.
8. **Phase-locked residual target:** candidate `(T,phi)` must satisfy every equation (D12), after one gauge condition is imposed.
9. **First-hit target:** every accepted event cycle must satisfy (D16)–(D17).
10. **Transversality target:** local event-time derivatives are valid only when (C10) holds.
11. **Gauge target:** global translation of all phase offsets must leave the phase-locked equations invariant.
12. **Future source-supported targets only:** synchronization stability, delay-induced stability changes, travelling waves, bumps, continuum reductions, and slow-synapse limits may be addressed in later gates. No legacy v0.3+ value is accepted here as validation evidence.

---

## 11. Explicit exclusions

The proposed Scope 0.1 baseline excludes:

- branch-local v0.3–v0.26 scientific results;
- all legacy numerical continuation and bifurcation claims;
- Floquet-spectrum values and numerical stability boundaries;
- normal forms, Chenciner / invariant-circle results, and order-parameter coefficient claims;
- adaptive conduction, state-dependent delays and in-flight packet semantics;
- STDP, weight plasticity, myelination and other adaptation;
- stochastic forcing / noise;
- deterministic external drive from the baseline equations;
- the historical immediate-reset-below-threshold convention from the baseline;
- exponential synapses from the baseline (retained as a historical variant);
- linear / Heaviside response laws from the baseline (retained as analytical variants);
- continuum / neural-field equations;
- JAX or any other implementation contract;
- parameter fitting, optimization, scans or effect-size selection;
- inference, observation design, pulse design or active experiments;
- v0.27 / hierarchical repeated-trial work;
- application claims;
- novelty claims;
- manuscript claim freeze.

---

## 12. Original Scope Gate coverage matrix

| Original requirement | Coverage here | Decision |
|---|---|---|
| Scope | Sections 1, 11 | SATISFIED |
| Source map | Section 2 | SATISFIED |
| Canonical equations and notation | Section 4 | SATISFIED |
| Event / spike definition | Section 5 | SATISFIED |
| Synaptic and delay definitions | Sections 4.3–4.4, 6 | SATISFIED |
| Baseline assumptions | Section 7 | SATISFIED |
| Variant registry | Section 8 | SATISFIED |
| Analytical validation targets | Section 10 | SATISFIED |
| Explicit exclusions | Section 11 | SATISFIED |
| Gate decision | Section 14 | SATISFIED |
| Proposed CORE Mathematical Freeze 0.1 contents | Section 15 | SATISFIED |
| Open questions | Section 16 | SATISFIED |
| STOP | Section 18 | SATISFIED |

The original Scope Gate is therefore now complete in substance and governance form. This statement does not retroactively change the legacy branch's historical status.

---

## 13. Deferred legacy material

Everything requiring downstream theory, computation, implementation or effect inspection remains deferred, including all v0.3–v0.26 work.

In particular:

- v0.3 continuation / hybrid-boundary work;
- v0.4 Floquet / symmetry work;
- v0.5 normal-form / order-parameter work;
- v0.6–v0.15 numerical atlas / bifurcation / invariant-object work;
- v0.16–v0.17 JAX / scaling work;
- v0.18–v0.23 inverse / observation-design work;
- v0.24 active-pulse design;
- v0.25 two-probe design;
- v0.26 nuisance / calibration theory.

These artifacts remain `NON-CANONICAL LEGACY CORE WORKING STATE` unless a later MASTER-authorized gate separately replays, preregisters, re-derives or classifies them.

---

## 14. Gate decision

\[
\boxed{\text{PASS}}
\]

Reason:

1. the baseline has been reconstructed as one explicit deterministic model;
2. primary Haken sources are separated from later reformulations and project choices;
3. every baseline component has a source / provenance classification;
4. alpha-kernel, periodic-comb, isolated-clock, autapse, phase-locking, first-hit and elementary event-time identities were independently re-derived;
5. assumptions, variants, validation targets and exclusions are explicit;
6. no downstream legacy result was promoted, replayed or used to select the baseline.

`PASS` does **not** itself create `CORE Mathematical Freeze 0.1`.

---

## 15. Proposed `CORE Mathematical Freeze 0.1` contents if MASTER approves

A minimal freeze should contain exactly:

1. the source map S1–S6, with S6 registry-only;
2. canonical baseline equations (C1)–(C11);
3. the no-reset-below-threshold lifted-phase event convention;
4. the normalized alpha-kernel and proved `(a,q)` state-space equivalence;
5. fixed edge-delay semantics;
6. assumptions A1–A13;
7. variant registry V-R0 through V-P1;
8. independently proved elementary identities (D1)–(D18);
9. validation-target list in Section 10;
10. exclusions in Section 11;
11. explicit statement that no v0.3–v0.26 numerical / implementation / inference / active-design claim is frozen.

Recommended freeze semantics:

`RB-004 / CORE Mathematical Freeze 0.1 — BASELINE DEFINITIONS AND ELEMENTARY C1 DERIVATIONS ONLY`

The exact rollback identifier remains a MASTER governance decision.

---

## 16. Open questions

1. Should a future freeze also require the Haken Naka–Rushton response as a mandatory historical reference implementation, even though (C2) is the canonical baseline response?
2. Should the first implementation-grade baseline permit neuron-specific or edge-specific alpha rates, or keep one global `alpha` until a later variant gate?
3. What exact simultaneous firing / arrival tie convention should be frozen before an event engine is authorized?
4. What canonical representation of delayed prehistory should be used for reproducible simulations: explicit spike history, delay buffers, or an equivalent hybrid history object?
5. Should deterministic external drive receive a separate early variant freeze because it appears already in Haken's primary equations?
6. Which v0.2 reference scripts / benchmark JSON assets are sufficiently specified for an exact replay-only canonicalization gate?
7. Which later mathematical results are C1 re-derivable without numerical dependence, and which must wait for preregistered reruns?

---

## 17. Proposed next MASTER decisions — not executed

MASTER may now choose among:

1. **Authorize `CORE Mathematical Freeze 0.1`** using Section 15, or return this gate for source / notation repair.
2. After a freeze, authorize a **separate v0.2 exact benchmark replay / canonicalization gate** limited to committed C2-eligible reference assets and the analytical targets in Section 10.
3. Only after baseline + elementary benchmarks are frozen, decide whether any v0.3+ legacy line should be recovered by fresh derivation, exact replay, or preregistered rerun according to the prior C1–C5 classification.

No such next step is performed here.

---

## 18. STOP

`CORE Mathematical Scope Canonicalization Gate 0.1` is complete.

No replay was run. No implementation was written. No v0.3+ science was executed. No active experiment design was performed. No v0.27 work was started.

**STOP — RETURN TO MASTER**
