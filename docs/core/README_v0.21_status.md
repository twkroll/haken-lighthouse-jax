# CORE v0.21 status

CORE v0.21 promotes observation design to a first-class part of the chart-aware Lighthouse inverse problem.

Unknown block:

`(p, tau3, eta1, eta2)`

with twelve candidate labelled spike times spanning four firing cycles.

Key results:
- the v0.20 first-six baseline has `sigma_min = 0.1017059763`;
- exhaustive E-optimal selection of six observations gives indices `(1,2,3,4,9,11)` and `sigma_min = 0.3086515413`, a factor `3.0347` improvement;
- the corresponding Fisher standard deviations of `p` and `tau3` fall to about `1.93e-4` and `2.67e-4` at spike-time noise `1e-4`;
- four well-placed observations `(1,2,9,11)` already give `sigma_min = 0.2898829236`, larger than the old six-spike baseline;
- the D-optimal six-set `(1,2,7,9,10,11)` improves the Fisher determinant by a factor about `54.94` over baseline;
- extending the candidate horizon from two to three to four cycles raises the best six-spike `sigma_min` approximately `0.1017 -> 0.2042 -> 0.3087` without decreasing the nominal truth-chart minimum margin below `0.07291563`;
- one-neuron four-cycle traces are formally full rank but poorly conditioned, while two-neuron coverage is substantially stronger;
- a controlled fifth unknown, a global observation clock offset, remains locally identifiable with six designed spike observations; its E-optimal six-set has `sigma_min = 0.29868343`.

Assets:
- `docs/core/observation_design_v0.21.md`
- `benchmarks/core_v021_reference.json`
- `reference/core_v021_observation_design.py`
- benchmark contract B329–B350

Scientific rule introduced by v0.21:

**design statistical information and hybrid chart robustness separately.**

The design layer selects rows of a valid one-sided fixed-chart sensitivity matrix. It never differentiates through event-order selection.

Next target: CORE v0.22 should introduce a low-dimensional latent synaptic-state block only after comparing baseline and v0.21-optimal observation schedules, so any loss of identifiability can be attributed to the new latent physics rather than poor measurement choice.
