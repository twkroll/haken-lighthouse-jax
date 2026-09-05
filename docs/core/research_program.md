# CORE research program

## Mission

CORE is the mathematical source of truth for the Haken Lighthouse JAX project. It separates historical Lighthouse structure, contemporary reconstruction, and project extensions, then converts them into exact analytical benchmarks, continuation problems, stability operators, symmetry reductions, low-dimensional order-parameter equations, invariant-object computations, and causal adaptive-event semantics that can be checked independently of any one numerical implementation.

The governing principle is:

> Every computational claim should be traceable to a mathematical object whose assumptions, invariances, singular limits, event semantics, and validation tests are explicit.

---

# Scientific ordering

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
\text{exact invariant objects}
\to
\text{adaptive event dynamics}
\to
\text{large-scale JAX computation}.
}
\]

This ordering turns JAX into an accelerator and inference engine for a mathematically controlled system rather than into the definition of the model itself.

---

# Completed version ladder

## v0.1 -- canonical hybrid model -- COMPLETE

Graph Lighthouse equations, firing/event convention, exponential and alpha synapses, delayed graph model, synchronous period relation, spike-to-rate and continuum bridge.

## v0.2 -- exact analytical benchmarks -- COMPLETE

Exact periodic alpha comb/state, isolated clock, delayed autapse, phase-locked existence equations, event-time linearisation, exact hybrid flow/saltation and benchmark contract B0--B10.

## v0.3 -- continuation and hybrid admissibility -- COMPLETE

Fixed-domain branch equations, pseudo-arclength continuation, folds, two-cell symmetry breaking, grazing/first-hitting/arrival-order boundaries and B11--B22.

## v0.4 -- general Floquet and symmetry theory -- COMPLETE

General spike-time characteristic operator, gauge-neutral identity, two-cell sectors, circulant/ring Fourier reduction, cluster symmetry and B23--B40.

## v0.5 -- synergetic order parameters / normal forms -- COMPLETE AT THEORY-CONTRACT LEVEL

Gauge-fixed return maps, Haken slaving interpretation, pitchfork/flip/Neimark--Sacker normal forms, ring order parameters, finite cyclic selection rules, adaptive-delay slow-variable template and B41--B58.

Interpretive rule:

> The order parameter is the amplitude of the critical collective mode for the instability under study. Microscopic phase, firing rate, synaptic state, or delay is not promoted to an order parameter without a center/critical-mode argument.

## v0.6 -- first numerical atlas -- COMPLETE

Nonlinear two-cell pitchfork benchmark, branch geometry, multiplier crossing, first numerical synergetic cubic, Coombes Fig.3 reproduction audit and B59--B72.

## v0.7 -- dynamic event normal forms -- COMPLETE

Gauge-fixed exact event-history map, genuine flip plus period-two continuation, genuine ring Neimark--Sacker point, direct cubic coefficient extraction and B73--B90.

## v0.8 -- hybrid codimension-two structure -- COMPLETE

Transversal NS plus response-threshold contact, quadrature audit, hybrid/non-smooth classification and B91--B104.

## v0.9 -- smooth Chenciner point -- COMPLETE

Smooth nondegenerate generalized Neimark--Sacker point with `L1=0`, fifth-order coefficient, nonzero second Lyapunov coefficient, regular two-parameter unfolding, resonance audit and B105--B120.

## v0.10 -- local Chenciner unfolding -- COMPLETE

Physical-to-normal-form map, quintic radial dynamics, invariant-circle roots, FIC condition, stability sectors and B121--B134.

## v0.11 -- exact invariant circles and FIC -- COMPLETE

Smooth alpha state-space exact-event map, JAX AD, Fourier parameterization, exact invariant circles, asymptotic normal-form comparison, direct nondegenerate FIC and B135--B150.

## v0.12 -- adaptive conduction slow--fast benchmark -- COMPLETE

Frozen NS/FIC skeleton, calibrated slow radial envelope, conduction-speed adaptation, dynamic-bifurcation skip, delayed escape, explicit negative result for local sync/circle hysteresis and B151--B166.

## v0.13 -- causal in-flight conduction semantics -- COMPLETE

Remaining-distance packet state, causal arrival root, exact arrival sensitivities, same-edge FIFO property, comparison of launch-frozen / path-integral / instantaneous-current delay conventions, v0.12 one-flight robustness audit and B167--B182.

Primary files:

- `in_flight_delays_v0.13.md`
- `../../benchmarks/core_v013_reference.json`
- `../../reference/core_v013_inflight_delays.py`

---

# Next: v0.14 -- full adaptive event engine

The next stage moves from a one-flight propagation audit to a full event-driven adaptive Lighthouse network.

## WP14.1 -- packet queue and continuous propagation

Implement an event state containing:

- phase and alpha-synapse states;
- conduction/plasticity states;
- active packets with remaining distance;
- deterministic event ordering for threshold and arrival ties.

Every outgoing spike creates packets. Every packet evolves by

\[
\dot\rho=-c(t)
\]

until its first zero. Constant speed must recover the fixed-delay v0.11 event map exactly.

## WP14.2 -- adaptive activity law

Implement both:

1. the simple v0.12 project plasticity rule for regression tests;
2. the activity-window conduction-speed rule of the 2026 adaptive Lighthouse work, with clear separation between the literature model and any CORE-modified fibre-activity definition.

## WP14.3 -- variational event dynamics

Propagate sensitivities through:

- continuous neural/synaptic/plasticity flow;
- firing events;
- packet creation;
- arrival events;
- changes of event order.

The v0.13 identity

\[
\delta a=
\frac{c(s)\delta s-\int_s^a\delta c(u)\,du}{c(a)}
\]

is the first unit test.

## WP14.4 -- reduced-vs-full adaptive validation

Re-run the v0.12 sweep in the full packet simulator and measure:

- actual NS passage;
- amplitude at the static FIC;
- dynamic-skip persistence;
- escape time;
- destination attractor;
- any genuine forward/backward hysteresis.

The full event model should agree with v0.12 in the singular slow limit and quantify the correction at finite adaptation rate.

## WP14.5 -- adaptive switching atlas

After the local ring test is passed, move to parameter regions with multiple frozen attracting branches. Continue the branchwise slow flow and determine when opposing drift directions produce relaxation switching, bottlenecks or stable adaptive fixed points.

---

# Longer-term targets toward CORE v1.0

## Mathematical well-posedness

- existence and uniqueness with state-dependent in-flight propagation;
- simultaneous-event semantics;
- event-order collision surfaces;
- nonsmooth threshold/grazing theory;
- conditions preventing Zeno behaviour.

## Cross-scale theory

- controlled slow-synapse asymptotics;
- event-spectrum to neural-field dispersion convergence;
- continuum amplitude equations near spatial instability;
- finite-size corrections to continuum mode selection.

## Stochastic extensions

- event-time noise and phase diffusion;
- stochastic order-parameter equations near criticality;
- noise-induced switching;
- uncertainty propagation for inferred parameters and conduction states.

## Plasticity / adaptation

- weight plus delay plasticity;
- competing slow variables;
- adaptive critical manifolds;
- codimension-two slow passage and hysteresis;
- distance-heterogeneous and edge-specific conduction dynamics.

## Differentiable-surrogate science

For every exact event benchmark compare a smooth/differentiable JAX surrogate in terms of:

- critical parameter error;
- multiplier error;
- normal-form coefficient error;
- invariant-circle/FIC error;
- adaptive switching-time error.

Normal-form and event-geometry fidelity, not trajectory similarity alone, is the standard for surrogate validation.

## v1.0 mathematical freeze

A v1.0 CORE specification should contain:

1. canonical exact model;
2. dimensionless conventions;
3. event and in-flight propagation semantics;
4. exact benchmark suite;
5. branch continuation specification;
6. spike-time Floquet operator;
7. symmetry and continuum reductions;
8. normal-form/order-parameter theory;
9. validated invariant objects;
10. adaptive conduction semantics and slow-fast tests;
11. exact-vs-surrogate error standards;
12. provenance for every equation family and a reproducible bibliography.
