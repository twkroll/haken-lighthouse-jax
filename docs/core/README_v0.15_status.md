# CORE v0.15 status

CORE is verified through **v0.15** on branch `core/theory-v0.1`.

## New v0.15 closure

The large timing-modulated attractor found by the full packet-queue engine in v0.14 is now classified as a **quasiperiodic hybrid invariant circle**.  It is hybrid because its trajectory crosses a short-arrival event-order switching surface, so a single smooth fixed-itinerary return map is not globally valid.

At fixed

\[
p=-3.267985407948901,
\]

the upper loss boundary is

\[
\boxed{\tau_F\simeq8.00731}
\]

and is classified numerically as a **hybrid saddle-node/fold of invariant circles**.

The closure uses three independent diagnostics:

1. stable/unstable normal full-rotation multipliers approaching `+1` from opposite sides;
2. square-root separation of the two circles below the fold;
3. inverse-square-root ghost escape time above the fold.

Near `tau3=8.0072`,

\[
\mu_{\perp,s}\approx0.96123,
\qquad
\mu_{\perp,u}\approx1.04004.
\]

A near-fold multiplier fit gives

\[
\tau_F\approx8.00731073,
\]

while the independent escape-time fit gives

\[
\tau_F\approx8.00731041.
\]

## Global hysteresis mechanism

The verified global organization is now

\[
\text{stable synchrony}
+\text{ stable large hybrid circle}
+\text{ unstable basin-boundary circle}
+\text{ global circle fold}.
\]

This is distinct from the local Chenciner small-circle wedge, which has no stable-synchrony/stable-small-circle coexistence.

## Assets

- `global_invariant_circle_fold_v0.15.md`
- `../../benchmarks/core_v015_reference.json`
- `../../reference/core_v015_global_circle_fold.py`

Benchmark contract: **B205--B224**.

## Next

CORE v0.16 should replace the imperative scientific oracle by a fixed-capacity JAX packet queue with explicit masks, event charts and tangent/saltation propagation, and reproduce the v0.14 dynamic-skip and v0.15 global-circle-fold multipliers before any large-network scaling or gradient-based inference.
