# CORE v0.18 status

CORE v0.18 adds the first chart-aware inverse-problem benchmark.

At the verified N=3 ring truth `(p,tau3)=(-3.267985407948901,8)`, six labelled spike times from a known hybrid start state locally identify both continuous parameters. The fixed-chart spike-time Jacobian has singular values approximately `(0.83330,0.14773)`, condition number `5.64`, and agrees with a central finite-difference audit to relative error `3.76e-9`.

Three noiseless starts converge to the truth in five function evaluations. A `sigma_t=1e-4` noise audit gives parameter dispersion consistent with the local Fisher prediction.

The same benchmark carries an explicit hybrid chart sentinel. On the `tau3=8` slice the recorded event order loses validity near `p=-3.78713044385`; the chart margin changes sign across that point. A nonpositive margin invalidates the current JAX gradient and requires the physical scheduler to record a new chart.

Assets:

- `docs/core/inverse_problem_v0.18.md`
- `benchmarks/core_v018_reference.json`
- `reference/core_v018_inverse_problem.py`
- benchmark contract `B269-B288`

Next: a hybrid trust-region / multi-chart optimizer that can approach an event-order boundary, shorten the current step, rerecord the physical chart after an intentional crossing, and resume differentiation on the new side.
