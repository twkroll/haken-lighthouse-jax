# CORE research program

## Mission

CORE is the mathematical source of truth for the Haken Lighthouse JAX project. It separates historical Lighthouse structure, contemporary reconstruction, and project extensions, then converts them into exact analytical benchmarks, continuation problems, stability operators, symmetry reductions, and low-dimensional order-parameter equations that can be checked independently of any one numerical implementation.

The governing principle is:

> Every computational claim should be traceable to a mathematical object whose assumptions, invariances, singular limits, and validation tests are explicit.

---

# Version ladder

## v0.1 — Canonical hybrid model — COMPLETE

Deliverables:

- graph Lighthouse equations;
- lifted firing/event convention;
- reset-convention separation;
- exponential and alpha synapses;
- flow / event / jump / delay decomposition;
- synchronous period relation;
- spike -> rate -> neural-field reduction;
- spatial and adaptive-delay extension frontier.

Primary files:

- `mathematical_core.md`
- `research_program.md`

---

## v0.2 — Exact analytical benchmarks — COMPLETE

Deliverables:

- exact alpha periodic kernel comb;
- exact hybrid alpha state;
- isolated-neuron clock and constant-drive solution;
- delayed autapse;
- general phase-locked existence equations;
- symmetric two-cell problem;
- synchronous N-node period relation;
- event-time linearisation;
- exact modal flow and saltation benchmarks;
- slow-synapse characteristic equation;
- implementation benchmark contract B0--B10.

Primary files:

- `derivations_v0.2.md`
- `benchmark_contract_v0.2.md`

---

## v0.3 — Continuation, folds, symmetry breaking, hybrid admissibility — COMPLETE

Deliverables:

- fixed-domain branch operator `F(z,p)=0`;
- exact Jacobian and parameter sensitivities;
- pseudo-arclength continuation;
- generic fold conditions;
- exchange-symmetric two-cell decomposition;
- pitchfork reduction and square-root scaling;
- strict separation of existence and dynamical stability;
- event grazing / loss of transversality;
- first-hitting and arrival-order boundaries;
- continuation benchmark contract B11--B22.

Primary files:

- `continuation_bifurcations_v0.3.md`
- `continuation_contract_v0.3.md`

---

## v0.4 — General spike-time Floquet and symmetry theory — COMPLETE

Deliverables:

- arbitrary phase-locked spike-time recurrence for heterogeneous weights, delays, and offsets;
- nonlinear characteristic matrix

\[
\mathcal M(\mu)=(\mu-1)D_\nu-\mathcal H(\mu);
\]

- exact neutral identity

\[
\mathcal M(1)\mathbf 1=0;
\]

- nonlinear-eigenvalue conditioning;
- alpha-kernel Floquet-weighted derivative comb;
- recovery of synchronous master-stability reduction;
- two-cell symmetric/antisymmetric dynamic sectors;
- circulant ring / twisted-state Fourier reduction;
- cluster quotient and transverse stability;
- general permutation-symmetry projectors;
- discrete-to-continuum dispersion bridge;
- benchmark contract B23--B40.

Primary files:

- `spike_time_floquet_v0.4.md`
- `symmetry_reductions_v0.4.md`
- `floquet_contract_v0.4.md`

---

## v0.5 — Synergetic order parameters and nonlinear normal forms — COMPLETE AT THEORY-CONTRACT LEVEL

Deliverables:

- gauge-fixed event/Poincare-map formulation;
- identification of critical spike-time/Floquet amplitudes as local synergetic order parameters;
- center-manifold/slaving representation;
- map normal forms for:
  - simple nontrivial `+1` multiplier / fold of cycles;
  - exchange-symmetric `+1` / dynamic pitchfork;
  - `-1` / flip;
  - complex unit pair / Neimark--Sacker;
- explicit coefficient conventions through third order;
- ring Fourier amplitudes as order parameters;
- cyclic selection rule

\[
r-s\equiv1\pmod{m_q},
\qquad
m_q=\frac{N}{\gcd(N,q)};
\]

- finite-ring anisotropy hierarchy;
- two-mode competition/coexistence equations;
- steady--oscillatory and oscillatory--oscillatory codimension-two templates;
- slow adaptive delays coupled to fast critical amplitudes;
- exact-event / implicit / fitted coefficient extraction routes;
- normal-form benchmark contract B41--B58.

Primary files:

- `order_parameter_normal_forms_v0.5.md`
- `normal_form_contract_v0.5.md`

Interpretive rule introduced at v0.5:

> The order parameter is the amplitude of the critical collective mode for the instability under study. Microscopic phase, firing rate, synaptic state, or delay may correlate with it, but are not promoted to order parameters without a center/critical-mode argument.

---

# Next: v0.6 — quantitative bifurcation atlas and coefficient computation

The next stage should move from formal normal-form structure to computed Lighthouse coefficients and reproducible atlases.

## WP6.1 — exact small-system return maps

Construct gauge-fixed event return maps for:

1. delayed autapse;
2. exchange-symmetric two-cell network;
3. small circulant rings.

Compute first, second, and third derivatives including event-time sensitivity.

## WP6.2 — first numerical normal-form coefficients

Produce concrete values and parameter maps for:

- two-cell pitchfork cubic coefficient;
- first flip benchmark;
- first Neimark--Sacker Lyapunov coefficient;
- one codimension-two interaction.

Cross-validate explicit return-map derivatives against an independent spike-time/Lyapunov--Schmidt or local-identification route.

## WP6.3 — ring mode-selection atlas

For selected `N`, coupling kernels, and delay profiles:

- continue base twists `q0`;
- locate critical perturbation sectors `q`;
- calculate cubic/isotropy coefficients;
- classify pure and mixed timing patterns;
- test the predicted `m_q` anisotropy hierarchy;
- study convergence to the continuum limit.

## WP6.4 — adaptive-delay reduced dynamics

Along frozen-delay branches, tabulate:

\[
\sigma(d),\quad c(d),\quad \ell_1(d),\quad q_*(d)
\]

as appropriate and construct low-dimensional slow-fast models. Compare their branch following, switching, and hysteresis against the full adaptive event network.

## WP6.5 — differentiable-surrogate science

For each exact event critical point, compare a differentiable JAX surrogate in terms of:

- critical parameter error;
- multiplier error;
- normal-form coefficient error;
- branch-amplitude prediction error.

Normal-form fidelity, not only trajectory similarity, becomes the standard for surrogate validation.

---

# Longer-term v0.7--v1.0 targets

## Mathematical well-posedness

- existence and uniqueness under documented regularity assumptions;
- simultaneous-event semantics;
- state-dependent-delay well-posedness;
- nonsmooth threshold and grazing theory.

## Cross-scale theory

- controlled slow-synapse asymptotics;
- event-spectrum to neural-field dispersion convergence;
- continuum amplitude equations near spatial instability;
- finite-size corrections to continuum mode selection.

## Stochastic extensions

- event-time noise and phase diffusion;
- stochastic order-parameter equations near criticality;
- noise-induced switching between phase-locked states;
- uncertainty propagation for inferred parameters.

## Plasticity / adaptation

- weight plasticity plus delay plasticity;
- competing slow variables;
- adaptive critical manifolds;
- codimension-two slow passage and hysteresis.

## v1.0 mathematical freeze

A v1.0 CORE specification should contain:

1. canonical exact model;
2. dimensionless conventions;
3. event semantics and admissibility;
4. exact benchmark suite;
5. branch continuation specification;
6. spike-time Floquet operator;
7. symmetry and continuum reductions;
8. normal-form/order-parameter theory;
9. validated coefficient examples;
10. exact-vs-surrogate error standards;
11. provenance for every equation family;
12. a reproducible reference bibliography.

---

# Scientific strategy

The project should avoid a common failure mode: implementing a large differentiable simulator first and only afterwards asking what its output means.

The preferred order is

\[
\boxed{
\text{exact model}
\to
\text{exact small benchmarks}
\to
\text{branches}
\to
\text{Floquet modes}
\to
\text{normal forms/order parameters}
\to
\text{large-scale JAX computation}.
}
\]

This ordering turns JAX into an accelerator and inference engine for a mathematically controlled system rather than into the definition of the model itself.
