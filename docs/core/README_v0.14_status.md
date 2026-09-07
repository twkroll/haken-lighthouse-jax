# CORE status through v0.14

The long-form `mathematical_core.md` remains the historical/core source and is not rewritten by this status file.

## Verified ladder

- v0.1--v0.5: canonical Lighthouse model, exact benchmarks, continuation, Floquet/symmetry theory, synergetic order parameters and normal forms.
- v0.6--v0.8: first numerical atlas, direct event normal forms and hybrid codimension-two structure.
- v0.9--v0.11: smooth Chenciner point, quintic unfolding, exact invariant circles and direct fold of invariant circles.
- v0.12: reduced adaptive conduction benchmark and dynamic bifurcation skip.
- v0.13: causal remaining-distance semantics for spikes already in flight.
- v0.14: full adaptive packet-queue event engine, direct reduced-vs-full slow-passage validation, and first global frozen bistability / hysteretic-memory benchmark.

## Current main result

At `p=-3.267985407948901` and frozen `tau3=8.0`, the full event engine supports both a synchrony basin and a large timing-modulated attractor. The latter is obtained by passing through the unstable regime near `tau3=7.8` and then returning to `tau3=8.0`. This coexistence is far outside the local Chenciner NS--small-FIC wedge and therefore represents global rather than local hysteresis structure.

## Reproducibility assets

- `adaptive_event_engine_v0.14.md`
- `../../benchmarks/core_v014_reference.json`
- `../../reference/core_v014_adaptive_event_engine.py`

The default reference invocation checks frozen recovery, full-vs-reduced slow passage, project activity feedback and bistability. `--slow-passage-only` checks the `epsilon=1e-5` packet run. `--upper-only` checks the empirical large-state persistence bracket between `tau3=8.0073` and `tau3=8.0075`.

## Next

CORE v0.15 should classify the large timing-modulated object and the mechanism at its upper loss boundary. A fixed-`p` invariant-object continuation should replace the current finite-time persistence bracket before the project assigns a fold/crisis label. In parallel, the packet queue should be moved to a fixed-capacity JAX representation with event tangent/saltation support.
