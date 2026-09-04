# Mathematical Core v0.1

## 0. Purpose and provenance

This document defines the mathematical source of truth for the project. Every equation is assigned one of three provenance classes:

- **[H] Historical**: directly traceable to Haken's Lighthouse model or an equivalent reformulation.
- **[C] Contemporary reconstruction**: a modern formulation supported by Coombes' 2025/2026 revisit.
- **[P] Project extension**: a proposed canonicalization or extension introduced for this project.

The goal is to preserve the analytically tractable hybrid structure of the Lighthouse model while making the state, events, delays, synapses, and limiting reductions explicit enough for modern numerical work and JAX implementations.

---

## 1. Historical / contemporary graph model

Let nodes be indexed by `i = 1, ..., N`. Associate to each node a lifted phase/state variable

\[
\theta_i(t) \in \mathbb{R},
\]

and a total synaptic input

\[
\psi_i(t) \in \mathbb{R}.
\]

A compact graph formulation is

\[
\dot\theta_i(t)=S(\psi_i(t)),
\tag{1}
\]

\[
\psi_i(t)=\sum_{j=1}^N w_{ij}\,a_j(t-\tau_{ij}) + I_i(t),
\tag{2}
\]

\[
a_i(t)=\sum_{m\in\mathbb Z}\eta(t-T_i^m).
\tag{3}
\]

Here:

- `w_ij` is the directed coupling from node `j` to node `i`;
- `tau_ij >= 0` is the axonal / communication delay;
- `eta(t)` is a causal post-synaptic response kernel;
- `I_i(t)` is an optional external input, included explicitly in this project notation;
- `T_i^m` is the `m`th firing time of node `i`.

The firing times satisfy the phase-crossing condition

\[
\theta_i(T_i^m)=2\pi m
\tag{4}
\]

for the lifted representation. Equivalently, a wrapped phase fires whenever `theta_i mod 2 pi` reaches the firing section.

**Provenance:** (1)–(3) are [H/C]; the explicit additive `I_i` is [P] but is consistent with Haken's use of external drive. The lifted event convention (4) is [P] notation equivalent to the standard Lighthouse firing condition.

### 1.1 Two reset conventions

Haken discussed two variants:

1. the phase/state is forced back to zero when the input falls below threshold;
2. the phase is not reset by a drop below threshold.

The contemporary Coombes analysis uses the second convention. The project will make this a model option rather than silently mixing the two systems.

---

## 2. Firing-rate / phase-velocity nonlinearity

The function

\[
S:\mathbb{R}\rightarrow\mathbb{R}_{\ge 0}
\]

maps synaptic input to phase velocity. Haken required a thresholded response: zero below a threshold, increasing above threshold, with saturation in the full nonlinear model.

The project treats `S` as an explicit interchangeable component.

### 2.1 Smooth threshold family [C]

A convenient smooth-above-threshold choice used in the modern revisit is

\[
S(x)=\exp\!\left[-\frac{r}{(x-h)^2}\right]H(x-h),\qquad r>0,
\tag{5}
\]

where `H` is the Heaviside step function and `h` is the input threshold.

### 2.2 Linear mid-range model [H/C]

For analytical work,

\[
S_L(x)=\gamma x-\Theta.
\tag{6}
\]

This linear model is particularly useful for exact period relations and stability calculations.

### 2.3 Project response-function contract [P]

A response family should expose at least

\[
S(x),\qquad S'(x),
\]

where the derivative may be classical, piecewise, distributional, or replaced by a documented smooth surrogate for differentiable computation.

We should never conflate a smooth surrogate used for automatic differentiation with the exact nonsmooth model.

---

## 3. Synaptic kernels

Assume throughout that

\[
\eta(t)=0 \quad (t<0),
\]

and, unless otherwise stated,

\[
\int_0^\infty \eta(t)\,dt=1.
\tag{7}
\]

### 3.1 Exponential synapse [H]

Haken used

\[
\eta_{\exp}(t)=\alpha e^{-\alpha t}H(t).
\tag{8}
\]

For a spike train

\[
y_i(t)=\sum_m\delta(t-T_i^m),
\tag{9}
\]

the filtered activity satisfies the event-driven ODE

\[
\dot a_i=-\alpha a_i
\]

between spikes, with jump

\[
a_i(T_i^{m+})=a_i(T_i^{m-})+\alpha.
\tag{10}
\]

This is exactly equivalent to convolution with (8).

### 3.2 Alpha-function synapse [C]

The continuous alpha kernel is

\[
\eta_{\alpha}(t)=\alpha^2 t e^{-\alpha t}H(t),
\tag{11}
\]

with transform

\[
\widehat\eta(\omega)=\frac{1}{(1+i\omega/\alpha)^2}.
\tag{12}
\]

A JAX-friendly hybrid state-space realization is [P]

\[
\dot q_i=-\alpha q_i,
\qquad
\dot a_i=-\alpha a_i+q_i
\tag{13}
\]

between spikes, with event jump

\[
q_i(T_i^{m+})=q_i(T_i^{m-})+\alpha^2,
\qquad
a_i(T_i^{m+})=a_i(T_i^{m-}).
\tag{14}
\]

The resulting transfer from the spike train to `a_i` is exactly `alpha^2/(s+alpha)^2`, hence (11).

This realization is important because it replaces explicit convolution by a small hybrid state per node whenever delays are absent or separately represented.

---

## 4. Canonical project model [P]

We define the **Lighthouse Hybrid Graph System (LHGS)** as

\[
\dot\theta_i=S_i(\psi_i;\vartheta_i),
\tag{15}
\]

\[
\psi_i(t)=I_i(t)+\sum_j w_{ij}\,a_j(t-\tau_{ij}),
\tag{16}
\]

with synaptic state dynamics chosen from a documented kernel realization and spike events generated by

\[
g_i(\theta_i,n_i)=\theta_i-2\pi(n_i+1)=0.
\tag{17}
\]

On an event, the spike counter changes as

\[
n_i^+=n_i^-+1,
\tag{18}
\]

and the outgoing synaptic state receives the kernel-specific jump.

This separates four mathematical objects that must remain distinct in code:

1. **flow** between events;
2. **event surface**;
3. **jump map**;
4. **delay operator**.

That separation will be the basis for exact event-driven simulation, fixed-step approximations, and differentiable surrogate simulation.

---

## 5. Synchronous solutions and exact self-consistency

Assume:

- a common delay `tau_ij = tau`;
- a row-sum constraint

\[
\sum_j w_{ij}=\Gamma
\tag{19}
\]

for every node;
- a synchronous spike train with period `T`, `T_i^m=mT`.

Define the periodic synaptic waveform

\[
P_T(t)=\sum_{m\in\mathbb Z}\eta(t-\tau-mT).
\tag{20}
\]

Then

\[
\psi_i(t)=\Gamma P_T(t)
\]

for every node, and the emergent period obeys the scalar self-consistency condition

\[
2\pi=\int_0^T S\!\left(\Gamma P_T(s)\right)ds.
\tag{21}
\]

Equation (21) is one of the most important benchmark relations in the project: numerical implementations should recover it before any large-network claims are trusted.

For the linear response `S_L(x)=gamma x-Theta`, normalization of the kernel gives

\[
T=\frac{\gamma\Gamma-2\pi}{\Theta},
\tag{22}
\]

when the sign constraints produce `T>0`. In a balanced network (`Gamma=0`) and `Theta<0`,

\[
T=\frac{2\pi}{|\Theta|}.
\tag{23}
\]

---

## 6. Linear stability around synchrony

Perturb firing times as

\[
\widetilde T_i^m=mT+\delta T_i^m.
\]

For small perturbations, the phase and time deviations are related by

\[
\delta T_i^m=-\frac{\delta\theta_i(mT)}{\dot\theta(T)}.
\tag{24}
\]

For a diagonalizable connectivity matrix with eigenvalues `w_hat_mu`, the modern Lighthouse analysis reduces stability to scalar characteristic functions, one per network eigenmode. The neutral eigenvalue associated with global time translation must be separated from true instabilities.

**CORE requirement:** implement two independent stability routes:

1. a spike-time / event-map formulation;
2. a flow-and-saltation / master-stability formulation for finite-dimensional synaptic states.

Agreement between the two routes is a high-value validation target.

---

## 7. Slow-synapse reduction: bridge to neural mass / neural field models

For a spatial continuum `x in R`, the Lighthouse system generalizes to

\[
\partial_t\theta(x,t)=S(\psi(x,t)),
\tag{25}
\]

\[
\psi(x,t)=\int_{\mathbb R}w(x,y)a(y,t-\tau(x,y))\,dy.
\tag{26}
\]

If `eta` is the Green function of a linear temporal operator `Q`, then

\[
Q\psi(x,t)=\int_{\mathbb R}w(x,y)\sum_m
\delta\!\left(t-T^m(y)-\tau(x,y)\right)dy.
\tag{27}
\]

Under slow synaptic processing and short-time averaging, the spike train is approximated by a firing rate. Using

\[
R(x,t)\approx\frac{\dot\theta(x,t)}{2\pi}
=\frac{S(\psi(x,t))}{2\pi},
\tag{28}
\]

yields

\[
Q\psi(x,t)\approx\frac{1}{2\pi}
\int_{\mathbb R}w(x,y)
S\!\left(\psi(y,t-\tau(x,y))\right)dy.
\tag{29}
\]

Thus the Lighthouse model provides a mathematically explicit bridge from spike timing to Wilson–Cowan / neural-field style rate dynamics.

This reduction is central to the project because it gives a hierarchy:

`spike/event model -> temporally averaged rate model -> continuum field model`.

---

## 8. Spatial patterns and waves

For translation-invariant coupling `w(x,y)=w(|x-y|)` and distance-dependent conduction delay

\[
\tau(x,y)=\frac{|x-y|}{v},
\tag{30}
\]

periodic travelling waves can be sought using spike times

\[
T^m(x)=mT+\rho x.
\tag{31}
\]

The physical wave speed is `c=1/rho` when `rho != 0` under this convention. The resulting self-consistency problem defines a dispersion relation between `T` and `rho`.

CORE should treat synchrony, travelling waves, clusters, bumps, and oscillator death as solution families of one hybrid framework rather than as separate models.

---

## 9. Modern extension frontier

The 2026 work of Coombes, Thul, Ruschel, and Nicks introduces activity-dependent conduction delays through myelination / conduction-speed adaptation. This motivates a project-level slow-fast extension

\[
\dot\theta_i=S(\psi_i),
\]

\[
\psi_i(t)=\sum_j w_{ij}a_j(t-\tau_{ij}(t)),
\]

\[
\varepsilon\dot\tau_{ij}=F_{ij}(\text{activity},\tau_{ij}),
\qquad 0<\varepsilon\ll1.
\tag{32}
\]

This is **not** part of the historical core. It belongs to the modern extension layer.

Additional project extensions to study later:

- heterogeneous thresholds and response curves;
- additive and multiplicative synaptic noise;
- plastic weights `w_ij(t)`;
- adaptive delays `tau_ij(t)`;
- multiple synaptic time scales / E-I populations;
- graph limits and neural fields in 1D/2D;
- differentiable event surrogates for parameter inference;
- stochastic event timing and uncertainty quantification.

---

## 10. Dimensionless formulation

Hidden unit choices are a common source of irreproducibility. Let `alpha_*` be a reference inverse synaptic time and set

\[
s=\alpha_* t,
\qquad
\bar\tau_{ij}=\alpha_*\tau_{ij}.
\tag{33}
\]

Then

\[
\frac{d\theta_i}{ds}=\bar S(\psi_i),
\qquad
\bar S=\frac{S}{\alpha_*}.
\tag{34}
\]

All benchmark cases should specify whether parameters are dimensional or nondimensional. The implementation must never infer this silently.

---

## 11. Mathematical validation ladder

A numerical implementation is considered CORE-valid only after passing, in order:

### Level 0 — single node

- exact exponential-kernel decay;
- exact alpha-kernel impulse response;
- phase monotonicity when `S >= 0`;
- correct spike count and event times.

### Level 1 — synchronous graph

- row-sum synchrony;
- recovery of (21);
- recovery of the exact linear period (22);
- balanced-network special case (23).

### Level 2 — perturbation theory

- numerical Floquet / event-map multipliers;
- neutral time-translation mode;
- agreement with analytical stability boundaries.

### Level 3 — structured networks

- clusters and phase locking;
- heterogeneous graph spectra;
- delay-induced instabilities.

### Level 4 — continuum / limits

- convergence toward neural-field reduction for slow synapses;
- travelling-wave dispersion;
- Turing-type instability and localized bumps.

---

## 12. Initial research hypotheses

### H1 — hybrid formulation is the correct computational primitive

The most faithful modern implementation is likely a hybrid dynamical system rather than a generic tiny-step ODE solver over approximate delta pulses.

### H2 — exact event and smooth surrogate models should coexist

Use exact events for reference science and a documented smooth surrogate only when gradients are required. Quantify the surrogate error against event time, frequency, and stability observables.

### H3 — the slow-synapse limit is a key cross-scale validation

The same codebase should numerically demonstrate convergence from spiking Lighthouse dynamics to a rate / neural-field description as synaptic time scales become slow.

### H4 — graph spectrum is a natural organizing variable

For synchronous states, stability should be organized by connectivity eigenmodes and master-stability ideas, permitting comparison across network topologies.

### H5 — adaptive delays create a synergetic slow-fast extension

Treat conduction delay as a slowly evolving order/control variable and study branch following, mode selection, and switching between phase-locked states.

---

## 13. Open mathematical questions for CORE

1. Under what minimal regularity assumptions on `S` and `eta` does the hybrid system possess unique forward solutions?
2. How should simultaneous spikes be defined for zero-delay recurrent graphs without introducing update-order artifacts?
3. Which reset convention is structurally stable under perturbations and biologically interpretable?
4. Can the event-map and saltation-matrix stability theories be unified into one computational API?
5. What is the asymptotic error of the slow-synapse rate reduction as a function of synaptic time scale?
6. Which smooth event surrogate preserves bifurcation boundaries best while remaining differentiable in JAX?
7. How do heterogeneous thresholds, weights, and delays alter the row-sum synchrony condition?
8. Which classes of adaptive delay rules admit Lyapunov, contraction, or averaging analyses?
9. Can continuum limits be derived from graph sequences rather than introduced phenomenologically?
10. Which macroscopic quantities should be interpreted as synergetic order parameters: population rate, phase coherence, wave number, bump position, or a learned low-dimensional collective coordinate?

---

## 14. Reference baseline

Primary / near-primary sources used for v0.1:

1. H. Haken, "Quasi-discrete dynamics of a neural net: The Lighthouse model", *Discrete Dynamics in Nature and Society* 4 (2000), 187–200. DOI: `10.1155/S1026022600000182`.
2. H. Haken, "Phase Locking in the Lighthouse Model of a Neural Net with Several Delay Times", *Progress of Theoretical Physics Supplement* 139 (2000), 96–111. DOI: `10.1143/PTPS.139.96`.
3. H. Haken, *Brain Dynamics: Synchronization and Activity Patterns in Pulse-Coupled Neural Nets with Delays and Noise*, Springer (2002).
4. S. Coombes, "Revisiting the Haken Lighthouse model", *European Physical Journal Special Topics* 235 (2026), 4571–4593; version of record 19 Aug 2025. DOI: `10.1140/epjs/s11734-025-01841-3`.
5. S. Coombes, R. Thul, S. Ruschel, R. Nicks, "Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks", arXiv:`2606.21508` (2026).

---

## 15. CORE next milestone

Version v0.2 should add fully derived benchmark cases rather than more prose:

- exact single-neuron impulse-response solution;
- two-neuron phase-locked self-consistency equations;
- synchronous `N`-node period derivation;
- event-time linearization;
- saltation matrix for the finite-dimensional alpha-synapse state;
- nondimensional parameter table;
- testable numerical invariants for implementation.
