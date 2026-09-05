# Mathematical CORE status pointer

The canonical mathematical source of truth for the project is distributed across the versioned files in this directory.  The detailed original-model reconstruction remains in the historical/core derivation files; later versioned files add project generalisations and verified benchmarks without retroactively changing the historical model.

## Current verified ladder

- v0.1: canonical hybrid Lighthouse graph model and provenance separation;
- v0.2: exact analytical alpha-synapse/event benchmarks;
- v0.3: continuation, folds, symmetry breaking and hybrid admissibility;
- v0.4: general spike-time Floquet operator and symmetry reductions;
- v0.5: synergetic order parameters, slaving and map normal forms;
- v0.6: first numerical pitchfork atlas and reproduction audits;
- v0.7: direct event-map flip and Neimark--Sacker coefficients;
- v0.8: hybrid NS + threshold-contact codimension-two point;
- v0.9: smooth nondegenerate Chenciner point;
- v0.10: quintic local Chenciner unfolding;
- v0.11: exact invariant circles and direct fold of invariant circles;
- v0.12: adaptive conduction-delay slow--fast benchmark and dynamic bifurcation skip;
- v0.13: causal in-flight conduction semantics using remaining-distance packet states.

## Current adaptive event convention

For an edge `(i,j)` of anatomical length `ell_ij`, every emitted spike creates a packet with remaining distance

\[
\rho(s)=\ell_{ij},
\qquad
\dot\rho(t)=-c_{ij}(t).
\]

The packet arrives at the first zero of `rho`, equivalently

\[
\int_s^a c_{ij}(u)\,du=\ell_{ij}.
\]

For continuous strictly positive conduction speed this arrival is unique and transversal.  This is a **project extension** that makes the event semantics of already-emitted spikes explicit; it is distinct from simply evaluating an instantaneous state-dependent delay `tau_ij(t)=ell_ij/c_ij(t)`.

The general first-order arrival sensitivity is

\[
\delta a=
\frac{c(s)\,\delta s-\int_s^a\delta c(u)\,du}{c(a)}.
\]

These equations and their numerical benchmarks are defined in `in_flight_delays_v0.13.md` and contract B167--B182.

## Current scientific ordering

\[
\boxed{
\text{exact model}
\to
\text{exact benchmarks}
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

For the complete roadmap, see `research_program.md`.
