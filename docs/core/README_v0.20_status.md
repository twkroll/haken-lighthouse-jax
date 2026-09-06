# CORE v0.20 status

CORE v0.20 extends the chart-aware inverse problem to the four-dimensional unknown block

`(p, tau3, eta1, eta2)`

where `(eta1, eta2)` are gauge-fixed latent relative initial phases.

Key results:
- six spike times give a rank-four sensitivity matrix with singular values `(5.81134, 3.26704, 0.829826, 0.101706)` and condition number `57.14`;
- latent phases increase marginal `p/tau3` uncertainty by only about 45%;
- the first three spikes identify latent phase only, while delayed feedback is required to identify `p,tau3`;
- one optimization path exhibits two distinct sequential chart crossings, first at event indices `0/1` and later at `9/10`;
- a vector of event margins is required for robust boundary prediction; the scalar minimum-margin gradient can miss the next active surface;
- the two-boundary start `(-3.2,7.7,-0.07,-0.12)` converges in five iterations with exactly two physical chart rerecordings.

Assets:
- `docs/core/latent_state_inference_v0.20.md`
- `benchmarks/core_v020_reference.json`
- `reference/core_v020_latent_state_inference.py`
- benchmark contract `B309-B328`

Next: extend the latent block to synaptic state and/or unknown clock offset, and study observation design / identifiability before attempting unknown topology.
