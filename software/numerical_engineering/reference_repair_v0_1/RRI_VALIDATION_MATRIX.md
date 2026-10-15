# RRI-01..RRI-08 QA matrix (LOCAL ENGINEERING ONLY)

| Control | Observed result | Status |
|---|---|---|
| RRI-01 Frozen alpha=1000 narrow-pulse | one spike 0.5050005053634212; independent segmented SciPy match | PASS |
| RRI-02 Original 11 modules/180 cases | 11 modules, individually exit 0 | PASS |
| RRI-03 Aggregate process | 194 pass in 141.46 s, exit 0 | PASS |
| RRI-04 Reference-family fixtures | dense/sparse tokens and event times agree; alpha=1/30/1000, silent/zero/history | PASS finite suite |
| RRI-05 Fail-closed invalid cases | budget, unresolved quadrature (injected), endpoint and collision invalid | PASS |
| RRI-06 Chart/JAX guard | reject incomplete, stale and uncertified; valid ordinary and narrow with checked residual; regular FD | PASS finite suite |
| RRI-07 Dense/sparse with zero structural weight | identical event signatures and phases | PASS |
| RRI-08 Alternate first hit | gauss and quiet schedulers agree on finite regular fixture; broader accelerators are not certified as production defaults | PASS qualified; DEFERRED for unqualified accelerators |

## Limitation

The label physical_certification describes a finite numerical quality protocol, not an interval-arithmetic mathematical proof. Known limits include extreme parameter conditions that exceed the explicit integration budget. Outside those conditions the simulator returns an invalid chart, not a silently trusted event tape. Direct unguarded JAX fixed-chart primitives do not independently establish physical chart completeness.
