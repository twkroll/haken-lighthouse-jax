# CORE v0.23 status

CORE v0.23 adds a single non-perturbing pre-event measurement transverse to the v0.22 phase/synapse weak direction.

Unknown block remains

`(p, tau3, eta1, eta2, xi_psi, xi_q)`.

With `v=(2,-1,-1)/sqrt(6)`, before the first hybrid event

`z_psi(t)=v^T psi(t)=exp(-alpha*t)*(xi_psi+t*xi_q)`.

Key results:
- spike-only full-12 `sigma_min = 9.13748e-4`;
- the optimal pre-event measurement time is `t_m = 0.698919300895`, more than `7.45` time units before the first firing;
- one scalar measurement raises `sigma_min` to `0.228772004925`, a `250.37x` gain;
- this equals the old second-smallest singular value and therefore saturates the rank-one interlacing upper bound;
- direct `psi0` measurement gives `216.88x`, direct `q0` only `28.55x`;
- with reference noises `sigma_t=1e-4`, `sigma_z=2e-4`, the full augmented system still reaches the same weakest singular value;
- sensor noise may rise to about `5.65e-4` while retaining a `100x` information gain;
- an E-optimal six-spike-plus-sensor plan uses spike indices `(0,2,3,9,10,11)` and has whitened `sigma_min≈0.200974`;
- the finite v0.22 weak displacement and exact nonlinear alias are rejected by the sensor at about `25.83 sigma_z` and `20.22 sigma_z` respectively;
- deterministic twelve-start noiseless audits return truth for both five-spike-plus-sensor and six-spike-plus-sensor designs;
- a thirty-realization mixed-noise audit agrees with Fisher predictions within roughly 5–12% in marginal standard deviations.

Assets:
- `docs/core/transverse_observation_v0.23.md`
- `benchmarks/core_v023_reference.json`
- `reference/core_v023_transverse_observation.py`
- `docs/core/README_v0.23_status.md`
- benchmark contract `B378-B399`

Scientific rule:

> When extending the observation horizon does not lift a weak latent direction, change the observation operator before adding more hidden-state dimensions.

Next target: generate comparable transverse information using a small known input pulse and spike times only, so direct synaptic-state readout is no longer required.
