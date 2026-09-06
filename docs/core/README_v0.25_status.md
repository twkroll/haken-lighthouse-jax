# CORE v0.25 status

CORE v0.25 extends the latent initial synaptic state from one real q=1 direction to the full real two-dimensional zero-mean q=1 plane in both `psi0` and `q0`.

Unknown block:

`(p, tau3, eta1, eta2, xi_psi1, xi_psi2, xi_q1, xi_q2)`.

Two repeated trials share the same reproducibly prepared but unknown initial state. Both use labelled spike times only and the chart-safe active-pulse family from v0.24.

Pulse 1 is exactly the v0.24 reference:

`P1=(0.05, 0.1, 0.55, -0.1)`.

Rounded Pulse 2:

`P2=(0.05, 0.1, 0.20, 3.02)`.

Key results:
- P1 alone is formally rank 8 but has `sigma_min≈1.86287e-4`, condition number `≈7.38e4`;
- unforced 8-parameter experiment has `sigma_min≈3.24415e-5`;
- duplicating P1 gives only `sigma_min≈2.63450e-4`;
- P1+P2 gives `sigma_min≈0.1468571`, condition number `≈125.33`;
- this is `≈788.34x` P1 alone and `≈557.44x` duplicate-P1 information in the weakest direction;
- P1/P2 physical chart margins are `0.06285675` and `0.06334074`, both above the hard `0.06` floor;
- a refined P2 on the margin boundary reaches `sigma_min≈0.14696444`; the rounded reference loses only `≈0.073%` objective;
- fixed-chart JAX vs physically rerecorded central-FD errors are about `2.55e-9` and `2.23e-9` for P1/P2;
- exact global E-optimal 8-spike subset across 24 candidates is `(1,5,6,7,12,16,21,23)`, four spikes from each trial, with `sigma_min≈0.0936843`;
- deterministic 12-start nonlinear audits recover truth 12/12 for both full24 and E-opt8;
- 50-realisation `sigma_t=1e-4` audits remain on the Fisher scale.

The two pulse reset vectors are nearly opposing rather than orthogonal (`≈159.91 degrees`). The mechanism is therefore a two-sided nonlinear operating-point probe: repeating an identical trial does not change identifiability geometry, whereas a second deliberately different probe does.

Assets:
- `docs/core/full_q1_two_probe_v0.25.md`
- `benchmarks/core_v025_reference.json`
- `reference/core_v025_full_q1_two_probe.py`
- `docs/core/README_v0.25_status.md`
- benchmark contract `B426-B451`

Scientific rule:

> Replication reduces noise; experimental diversity changes the sensitivity nullspace. Practical hybrid identifiability requires both conditioning and chart-safe diversity, not rank alone.

Scope caveat: the same unknown latent initial state must be reproducibly prepared across the two trials. Trial-to-trial state jitter and pulse calibration uncertainty are not yet included.

Next target: CORE v0.26 should introduce trial-specific preparation variability and pulse calibration uncertainty and determine which shared network parameters remain identifiable before any move to unknown labels or topology.
