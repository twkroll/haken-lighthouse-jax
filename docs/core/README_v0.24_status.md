# CORE v0.24 status

CORE v0.24 replaces the idealized direct synaptic-state readout of v0.23 by one known pre-event pulse and returns to spike-time-only observation.

Unknown block remains

`(p, tau3, eta1, eta2, xi_psi, xi_q)`.

Pulse family:

`d(gamma)=cos(gamma)*v1+sin(gamma)*v2`

`psi += A*cos(beta)*d`

`q += A*sin(beta)*d`

with `v1=(2,-1,-1)/sqrt(6)` and `v2=(0,1,-1)/sqrt(2)`.

Reference design:
- `t_p=0.05`
- `A=0.1`
- `beta=0.55`
- `gamma=-0.1`
- physical truth-chart margin `0.06285675 > 0.06`
- first firing after pulse `7.84778792`

Key results:
- no-pulse full-12 `sigma_min = 9.13748e-4`;
- pulsed full-12 `sigma_min = 0.07955699`;
- information gain `87.07x`;
- condition number drops from about `1.19e4` to about `1.30e2`;
- JAX fixed-chart Jacobian agrees with centered finite differences at about `3.0e-9` relative error;
- E-optimal six-spike pulsed schedule is `(0,1,2,3,10,11)` with `sigma_min≈0.0748375`;
- v0.22 finite weak displacement becomes a `20.65 sigma_t` full-12 spike-time discrepancy;
- v0.22 exact same-chart nonlinear alias becomes a `16.15 sigma_t` discrepancy;
- deterministic 12-start noiseless audits return truth for both the six-spike and full-12 pulsed designs;
- 30-realization `sigma_t=1e-4` audits remain on the Fisher scale.

Hybrid-safety result:
- a nearby less-safe pulse has `sigma_min≈0.0796217` but chart margin only `0.0304037`;
- enforcing the `0.06` margin costs less than `0.1%` of the E-optimal objective.

Assets:
- `docs/core/active_pulse_design_v0.24.md`
- `benchmarks/core_v024_reference.json`
- `reference/core_v024_active_pulse_design.py`
- `docs/core/README_v0.24_status.md`
- benchmark contract `B400-B425`

Scientific rule:

> In active hybrid experiment design, event-chart safety is a hard admissibility constraint; information gains obtained only by approaching an event-order collision are not accepted.

Next target: use one or two independently designed chart-safe pulse experiments to identify the full real two-dimensional q=1 synaptic subspace in both initial `psi` and `q` before attempting unknown labels or topology.
