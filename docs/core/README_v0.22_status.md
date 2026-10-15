# CORE v0.22 status

CORE v0.22 extends the inverse problem to

`(p, tau3, eta1, eta2, xi_psi, xi_q)`

with a minimal unit zero-mean q=1 latent synaptic contrast in the initial `(psi,q)` state.

Key results:
- the full 12x6 spike-time Jacobian is rank six but has `sigma_min≈9.14e-4` and condition number about `1.19e4`;
- the weakest direction mixes initial phase and synaptic state, especially `xi_psi`, and a finite displacement along it remains almost invisible in spike times while staying on the same hybrid chart;
- the v0.21 four-unknown E-optimal schedule becomes substantially worse after the nuisance block is enlarged;
- re-optimized D-optimal six-spike design `(0,1,2,9,10,11)` strongly improves `p/tau3` while preserving latent-state uncertainty, but cannot remove the near-null direction;
- square six-to-eight observation systems exhibit nonlinear aliases in a deterministic multistart audit, whereas an E-optimal nine-row plan and the full twelve-row plan return truth for all audited starts;
- therefore local conditioning and nonlinear uniqueness are distinct experiment-design objectives.

Assets:
- `docs/core/latent_synaptic_state_v0.22.md`
- `benchmarks/core_v022_reference.json`
- `reference/core_v022_latent_synaptic_state.py`
- `docs/core/README_v0.22_status.md`

Benchmark contract: B351-B377.
