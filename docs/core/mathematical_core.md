# Mathematical Core v0.5

## 0. Purpose and provenance

This document defines the mathematical source of truth for the project. Every equation is assigned one of three provenance classes:

- **[H] Historical**: directly traceable to Haken's Lighthouse model or an equivalent reformulation.
- **[C] Contemporary reconstruction**: a modern formulation supported by Coombes' 2025/2026 revisit and adaptive-delay work.
- **[P] Project extension**: a proposed canonicalisation or extension introduced for this project.

The goal is to preserve the analytically tractable hybrid structure of the Lighthouse model while making the state, events, delays, synapses, limiting reductions, stability operators, and critical collective modes explicit enough for modern numerical work and JAX implementations.

The detailed derivations are versioned in companion documents. As of v0.5:

- `derivations_v0.2.md`: exact analytical reference cases;
- `continuation_bifurcations_v0.3.md`: branch continuation, folds, pitchforks, hybrid singularities;
- `spike_time_floquet_v0.4.md`: general spike-time Floquet operator;
- `symmetry_reductions_v0.4.md`: ring, cluster, and permutation-symmetry sectors;
- `order_parameter_normal_forms_v0.5.md`: center-manifold/slaving and nonlinear order-parameter equations.

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

**Provenance:** (1)--(3) are [H/C]; the explicit additive `I_i` is [P] but is consistent with Haken's use of external drive. The lifted event convention (4) is [P] notation equivalent to the standard Lighthouse firing condition.

### 1.1 Two reset conventions

Haken discussed two variants:

1. the phase/state is forced back to zero when the input falls below threshold;
2. the phase is not reset by a drop below threshold.

The contemporary Coombes analysis uses the second convention. The project makes this a model option rather than silently mixing the two systems.

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

and, for v0.5 normal-form work where smoothness permits,

\[
S''(x),\qquad S'''(x).
\]

The derivative may be classical, piecewise, distributional, or replaced by a documented smooth surrogate for differentiable computation. We never conflate a smooth surrogate used for automatic differentiation with the exact nonsmooth model.

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

A JAX-friendly hybrid state-space realisation is [P]

\[
\dot q_i=-\alpha q_i,
\qquad
\dot a_i=-\alpha a_i+q_i
\tag{13}
\]

between spikes, with event jump

\[
q_i(T_i^{m+})=q_i(T_i^{m-})+\alpha^2,
\qquad a_i(T_i^{m+})=a_i(T_i^{m-}).
\tag{14}
\]

The resulting transfer from the spike train to `a_i` is exactly `alpha^2/(s+alpha)^2`, hence (11).

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

with synaptic state dynamics chosen from a documented kernel realisation and spike events generated by

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

That separation is the basis for exact event-driven simulation, fixed-step approximations, and differentiable surrogate simulation.

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

For the linear response `S_L(x)=gamma x-Theta`, kernel normalisation gives

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

## 6. General phase-locked states

A one-spike-per-node-per-cycle phase-locked state is written

\[
\boxed{T_i^m=(m+\chi_i)T,\qquad \chi_i\in\mathbb R/\mathbb Z.}
\tag{24}
\]

Fix one `chi_i` to remove the global phase gauge in the existence calculation. The detailed self-consistency equations are defined in `derivations_v0.2.md` and the fixed-domain continuation operator in `continuation_bifurcations_v0.3.md`.

CORE treats three properties as logically independent:

1. **existence/continuation** of the phase-locked branch;
2. **dynamical stability** of the orbit;
3. **hybrid admissibility**, including first hitting, transversality, and arrival ordering.

No stable/unstable branch label is complete without the third layer.

---

## 7. Spike-time Floquet operator [C/P]

For a regular phase-locked orbit, define its spike-section velocity

\[
\nu_i=S_i(\Psi_i(0)).
\tag{25}
\]

Transversality requires

\[
\nu_i\ne0.
\tag{26}
\]

Perturb spike times and use the cycle multiplier ansatz

\[
\delta T_i^m=\xi_i\mu^m.
\tag{27}
\]

The general v0.4 characteristic operator is

\[
\boxed{
\mathcal M(\mu)=(\mu-1)D_\nu-\mathcal H(\mu),
}
\tag{28}
\]

where

\[
D_\nu=\operatorname{diag}(\nu_1,\ldots,\nu_N)
\]

and `H(mu)` combines weights, delays, phase offsets, kernel derivatives, and postsynaptic gain along the locked orbit.

Nontrivial Floquet multipliers solve

\[
\boxed{\mathcal M(\mu)\xi=0.}
\tag{29}
\]

The exact global time-translation identity is

\[
\boxed{\mathcal M(1)\mathbf1=0.}
\tag{30}
\]

The neutral mode must be identified by its overlap with uniform spike-time translation. It is not valid to discard whichever numerical root happens to be closest to one.

A regular locked orbit is linearly asymptotically stable if all nontrivial multipliers satisfy

\[
|\mu|<1.
\tag{31}
\]

---

## 8. Symmetry sectors and collective modes [P/C]

Whenever the complete delayed locked-state operator respects a symmetry, decompose (28) into invariant sectors rather than relying only on the eigenvectors of the static weight matrix.

For a circulant ring with base twist `q_0`, the perturbation sectors are labelled by

\[
\kappa_q=\frac{2\pi q}{N},
\qquad q=0,\ldots,N-1,
\tag{32}
\]

and the characteristic equation reduces to scalar sector equations

\[
\boxed{E_q^{(q_0)}(\mu)=0.}
\tag{33}
\]

Always distinguish:

- `q_0`: winding number of the base locked state;
- `q`: perturbation/Floquet sector.

Cluster states require both quotient/longitudinal and transverse cluster-breaking sectors. A quotient-only stability test is incomplete.

---

## 9. Synergetic order parameters and slaving [H/P]

This layer is introduced explicitly in v0.5.

Let `Sigma` be a gauge-fixed event/Poincare section and

\[
y_{n+1}=\mathscr P_p(y_n)
\tag{34}
\]

the one-cycle return map. Let a finite set of nontrivial multipliers approach the unit circle while the remaining spectrum is separated by a stable gap.

If `V_c` contains the critical collective modes and `A` their amplitudes, local center-manifold/slaving theory gives

\[
\boxed{
y-y_*=V_cA+h(A,\bar A,p-p_*),}
\tag{35}
\]

where the stable components satisfy

\[
h=O(\|A\|^2+|p-p_*|\|A\|).
\tag{36}
\]

### CORE definition of the local order parameter

\[
\boxed{
\text{order parameter} = \text{amplitude of the critical collective spike-time/Floquet mode(s)}.
}
\tag{37}
\]

This is the project-level bridge to Haken's slaving principle. It prevents a loose use of “order parameter” for any macroscopic variable that happens to be convenient to plot.

Examples:

- antisymmetric two-cell timing mode -> real amplitude `A`;
- ring pattern instability in sector `q` -> complex Fourier amplitude `A_q`;
- Neimark--Sacker timing modulation -> complex envelope `Z`;
- simultaneous critical sectors -> vector of amplitudes.

Stable modes are slaved only when the corresponding homological inverses are well conditioned. Weakly stable or nearly defective modes must be promoted into the critical set.

---

## 10. Canonical codimension-one normal forms [C/P]

On the gauge-fixed event return map, the principal local forms are:

### 10.1 Simple nontrivial `+1` multiplier

\[
\boxed{
\Delta A=a\varepsilon+bA^2+\cdots
}
\tag{38}
\]

for a generic cycle fold.

### 10.2 `Z_2` symmetry-breaking `+1` multiplier

\[
\boxed{
\Delta A=\sigma\varepsilon A+cA^3+\cdots
}
\tag{39}
\]

with

\[
A^2\sim-\frac{\sigma}{c}\varepsilon.
\tag{40}
\]

### 10.3 Flip

\[
\boxed{
A_{n+1}=-(1+\sigma\varepsilon)A_n+c_fA_n^3+\cdots.
}
\tag{41}
\]

### 10.4 Neimark--Sacker

For critical multipliers `e^{+-i Omega}`, a complex amplitude obeys

\[
\boxed{
Z_{n+1}=e^{i\Omega}
\left[(1+\sigma\varepsilon)Z_n+gZ_n|Z_n|^2+\cdots\right].
}
\tag{42}
\]

Strong low-order resonances require separate resonant normal forms.

The coefficient definitions and homological equations are fixed in `order_parameter_normal_forms_v0.5.md`.

---

## 11. Finite-ring anisotropy and continuum limit [P]

For a critical ring sector `q`, define the representation order

\[
\boxed{m_q=\frac{N}{\gcd(N,q)}.}
\tag{43}
\]

Under one-node rotation,

\[
A_q\mapsto e^{i2\pi q/N}A_q.
\tag{44}
\]

A monomial `A^r bar(A)^s` is symmetry-allowed in the amplitude equation only when

\[
\boxed{r-s\equiv1\pmod{m_q}.}
\tag{45}
\]

Thus the first cyclic anisotropy is generically of order `m_q-1`.

Consequences:

- `m_q=2`: real `Z_2` sector;
- `m_q=3`: quadratic anisotropy can occur;
- `m_q=4`: cubic anisotropy competes with the isotropic cubic;
- `m_q>=5`: the cubic amplitude equation is effectively continuous-phase/O(2)-like, with discrete phase pinning entering at higher order.

This gives a quantitative finite-size bridge from discrete Lighthouse rings to continuum neural-field pattern-selection theory.

---

## 12. Slow adaptive delays [C/P]

The 2026 adaptive-delay work motivates slow structural dynamics. Near a frozen critical branch, CORE writes

\[
\boxed{
A_{n+1}-A_n=f(A,\bar A;d_n,p),
}
\tag{46}
\]

\[
\boxed{
d_{n+1}-d_n=\varepsilon G(A,\bar A,d_n,p),
\qquad0<\varepsilon\ll1.
}
\tag{47}
\]

Here:

- `A` is the fast critical collective order parameter;
- `d` is a slowly adapting delay/control/state variable;
- frozen phase-locked branches organise the slow motion while they remain normally hyperbolic;
- loss of frozen stability or hybrid admissibility can trigger switching.

Delay variables become part of the order-parameter/center set only if their own dynamics is critical at the same asymptotic scale.

---

## 13. Slow-synapse reduction: bridge to neural mass / neural field models

For a spatial continuum `x in R`, the Lighthouse system generalises to

\[
\partial_t\theta(x,t)=S(\psi(x,t)),
\tag{48}
\]

\[
\psi(x,t)=\int_{\mathbb R}w(x,y)a(y,t-\tau(x,y))\,dy.
\tag{49}
\]

If `eta` is the Green function of a linear temporal operator `Q`, then under slow synaptic processing and short-time averaging,

\[
R(x,t)\approx\frac{\dot\theta(x,t)}{2\pi}
=\frac{S(\psi(x,t))}{2\pi}
\tag{50}
\]

yields

\[
\boxed{
Q\psi(x,t)\approx\frac{1}{2\pi}
\int_{\mathbb R}w(x,y)
S\!\left(\psi(y,t-\tau(x,y))\right)dy.
}
\tag{51}
\]

Thus the model hierarchy is

\[
\boxed{
\text{spike/event model}
\to
\text{rate model}
\to
\text{continuum field model}.
}
\tag{52}
\]

A future CORE target is to derive how the v0.5 event-mode amplitude equations converge to neural-field amplitude equations near spatial criticality.

---

## 14. Dimensionless formulation

Let `alpha_*` be a reference inverse synaptic time and set

\[
s=\alpha_* t,
\qquad
\bar\tau_{ij}=\alpha_*\tau_{ij}.
\tag{53}
\]

Then

\[
\frac{d\theta_i}{ds}=\bar S(\psi_i),
\qquad
\bar S=\frac{S}{\alpha_*}.
\tag{54}
\]

All benchmark and normal-form coefficients must specify whether cycle time, physical time, or nondimensional time is being used. A coefficient without its amplitude normalisation and time convention is not comparable across implementations.

---

## 15. Mathematical validation ladder

### Level 0 — single node and synapse

- exact constant-drive event time;
- exact exponential/alpha impulse response;
- exact periodic alpha comb;
- correct spike count and first-hitting semantics.

### Level 1 — synchronous / phase-locked existence

- row-sum synchrony;
- exact linear period;
- general phase-locked self-consistency;
- pseudo-arclength branch continuation;
- branch Jacobian and singularity tests.

### Level 2 — stability

- event-time Floquet multipliers;
- exact global time-translation identity;
- symmetry-sector decomposition;
- dense-vs-reduced agreement;
- root-count and conditioning diagnostics.

### Level 3 — nonlinear critical dynamics

- center/slaving reconstruction;
- fold, pitchfork, flip, and Neimark--Sacker coefficients;
- branch-amplitude scaling;
- finite-ring equivariant selection rules;
- codimension-two mode interactions.

### Level 4 — slow/large-scale reductions

- adaptive-delay reduced systems;
- exact-vs-surrogate normal-form fidelity;
- discrete-ring to continuum mode convergence;
- spike-event to neural-field amplitude-equation convergence.

---

## 16. Core scientific hypotheses

### H1 — hybrid formulation is the correct computational primitive

The faithful reference implementation is a hybrid dynamical system rather than a generic tiny-step ODE solver over approximate delta pulses.

### H2 — exact event and smooth surrogate models should coexist

Use exact events for reference science and a documented smooth surrogate only where gradients are required. Quantify surrogate error in event times, periods, multipliers, and normal-form coefficients.

### H3 — slow-synapse reduction is a key cross-scale validation

The same model hierarchy should demonstrate convergence from Lighthouse spiking dynamics to rate/neural-field dynamics as synaptic time scales become slow.

### H4 — delayed graph symmetry organises stability

For locked states, the relevant operator is the full delayed event characteristic operator. Static graph eigenmodes are sufficient only in factorisable special cases.

### H5 — critical spike-time modes are synergetic order parameters

Near a regular instability, a small set of critical event/Floquet mode amplitudes should parameterise the emerging collective timing dynamics while stable modes are slaved.

### H6 — adaptive delays create a slow-fast synergetic extension

Frozen locked branches and their critical modes should organise slow adaptive-delay trajectories, switching, and hysteresis.

### H7 — finite network symmetry leaves controlled corrections to continuum theory

Cyclic representation order predicts the order at which finite-size phase pinning enters the amplitude dynamics, allowing a quantitative discrete-to-continuum comparison.

---

## 17. Open mathematical questions for CORE

1. Under what minimal regularity assumptions on `S` and `eta` does the hybrid delayed system possess unique forward solutions?
2. How should simultaneous spikes be defined for zero-delay recurrent graphs without update-order artefacts?
3. Which reset convention is structurally stable under perturbations and biologically interpretable?
4. Can the nonlinear spike-time characteristic operator be connected rigorously to a gauge-fixed Poincare return operator on history space?
5. What is the most robust argument-principle/Evans-function strategy for complete Floquet root counts?
6. How do exact hybrid normal-form coefficients behave near arrival collisions and threshold contacts?
7. Can event-map coefficient formulas be written directly in terms of spike-time residual derivatives without constructing the full history return map?
8. Which codimension-two mode interactions occur first in biologically plausible ring and graph parameter families?
9. How do finite-ring equivariant normal forms converge to continuum/O(2) neural-field amplitude equations?
10. Under what conditions can adaptive delay variables be rigorously reduced together with critical spike-time amplitudes?
11. How accurately can a differentiable JAX surrogate reproduce exact-event cubic coefficients and bifurcation type?
12. Can noise be projected systematically onto the v0.5 order parameters to obtain stochastic amplitude equations for switching and phase diffusion?

---

## 18. Project rule for mathematical claims

Every scientific result should identify its layer:

\[
\boxed{
\text{model}
\to
\text{existence}
\to
\text{stability}
\to
\text{admissibility}
\to
\text{nonlinear critical dynamics}
\to
\text{reduction/approximation}.
}
\]

A result at one layer must not be silently promoted to another. In particular:

- existence does not imply stability;
- stability does not imply hybrid admissibility;
- a critical multiplier does not by itself determine nonlinear branch selection;
- a convenient macroscopic observable is not automatically an order parameter;
- a smooth differentiable surrogate is not the exact event model.
