# CORE Research Program

## Objective

Develop a mathematically rigorous, provenance-aware theory stack for the Haken Lighthouse model that supports exact analysis, numerical validation, and a modern JAX implementation.

The program is organized so that every computational feature has an analytical benchmark wherever possible.

## WP1 — Historical reconstruction

**Goal:** Reconstruct the original Lighthouse model without importing later assumptions.

Tasks:

- recover Haken's phase, dendritic-current, spike-train, delay, and noise equations;
- document both reset conventions;
- identify the response functions and approximations used in different Haken publications;
- produce a notation concordance: Haken 2000 / Haken 2002 / Coombes 2025–2026 / project notation.

Deliverable: `historical_reconstruction.md`.

## WP2 — Hybrid dynamical-system formulation

**Goal:** Define the model as flow + event surface + jump map + delay operator.

Tasks:

- prove / state conditions for forward well-posedness;
- define simultaneous events and zero-delay recurrent coupling;
- derive finite-dimensional state realizations for exponential and alpha synapses;
- formalize exact event-driven and wrapped-phase representations.

Deliverable: canonical mathematical specification v1.0.

## WP3 — Exact benchmark solutions

**Goal:** Build an analytical validation suite.

Tasks:

- single-neuron response to impulses and constant drive;
- two-neuron phase locking;
- synchronous N-node solution under row-sum constraint;
- exact period relation for linear response;
- balanced-network special cases.

Deliverable: closed-form / implicit benchmark catalogue.

## WP4 — Stability and bifurcation theory

**Goal:** Characterize loss of synchrony and emergence of collective states.

Tasks:

- event-time perturbation map;
- saltation matrices;
- Floquet multipliers;
- master stability functions;
- delay-induced Hopf / relaxation instabilities;
- static bifurcations, oscillator death, clusters.

Deliverable: stability atlas for canonical network families.

## WP5 — Spike-to-rate asymptotics

**Goal:** Quantify the bridge from Lighthouse spikes to neural mass / neural field equations.

Tasks:

- derive slow-synapse averaging carefully;
- estimate approximation error;
- identify dimensionless small parameters;
- compare against Wilson–Cowan / Amari limits;
- determine where the rate reduction fails.

Deliverable: asymptotic reduction note + numerical convergence tests.

## WP6 — Spatial continuum and pattern formation

**Goal:** Treat space, waves, and localized activity within one theory.

Tasks:

- graph-to-continuum formulation;
- distance-dependent conduction delays;
- travelling-wave dispersion relations;
- Turing-type instability;
- bumps and wandering states;
- 1D and 2D kernels.

Deliverable: continuum theory module.

## WP7 — Modern synergetic extensions

**Goal:** Extend the Lighthouse model while preserving analytical structure.

Priority extensions:

- heterogeneous thresholds and time scales;
- E/I node classes;
- stochastic synaptic transmission;
- adaptive weights;
- adaptive conduction delays / myelination;
- slow-fast order/control variables;
- data-driven low-dimensional order-parameter discovery.

Deliverable: extension taxonomy with explicit provenance labels.

## WP8 — Differentiable mathematics for JAX

**Goal:** Determine which approximations are acceptable for gradient-based inference and learning.

Tasks:

- exact event gradients where possible;
- saltation-aware sensitivities;
- smooth spike/event surrogate families;
- bias/error analysis of surrogate gradients;
- differentiable delays;
- parameter identifiability and inverse problems.

Deliverable: differentiability specification consumed by the implementation workstream.

## Milestones

### M0 — Core v0.1

Canonical equations, provenance scheme, synaptic state realizations, synchrony relation, slow-synapse bridge, research questions.

### M1 — Core v0.2

Fully derived single-node, two-node, and synchronous-network benchmarks plus nondimensional parameter table.

### M2 — Core v0.3

Event-time and saltation stability theory with numerical invariants.

### M3 — Core v0.4

Slow-synapse asymptotics and continuum reduction.

### M4 — Core v0.5

Travelling waves, Turing instabilities, bumps, and graph/continuum correspondence.

### M5 — Core v1.0

Stable mathematical specification supporting exact, approximate, stochastic, adaptive, and differentiable implementations.

## Definition of done for CORE v1.0

The mathematical core is considered mature when:

1. historical statements are traceable to sources;
2. every implementation state variable has a mathematical definition;
3. event semantics are unambiguous;
4. at least one exact benchmark exists for every major solver mode;
5. stability results can be reproduced numerically;
6. the spike-to-rate limit is demonstrated quantitatively;
7. project extensions are clearly separated from Haken's original model;
8. differentiable approximations carry explicit approximation/error statements.
