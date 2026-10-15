# CORE v0.21 — optimal observation design for hybrid Lighthouse inference

## Scope

CORE v0.21 treats the observation set itself as part of the inverse problem. The physical truth and latent-state parameterization remain those of v0.20,

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2),
\qquad
\delta\phi_0=(\eta_1,\eta_2,-\eta_1-\eta_2),
\]

with

\[
\vartheta_*=(-3.267985407948901,8,0,0).
\]

Instead of stopping after two cycles, the truth chart is followed for four firing cycles. This gives twelve candidate labelled spike times

\[
Y=(t_{0,0},t_{1,0},t_{2,0},t_{0,1},\ldots,t_{2,3})
\]

and a fixed-chart sensitivity matrix

\[
J=\frac{\partial Y}{\partial\vartheta}\in\mathbb R^{12\times4}.
\]

The physical truth replay contains 30 hybrid events before all twelve labelled firing observations have occurred. JAX fixed-chart derivatives agree with centered finite differences to the same numerical precision as v0.20.

## Design criteria

For a selected observation index set \(S\), let \(J_S\) be the corresponding rows of \(J\). With independent spike-time noise of variance \(\sigma_t^2\), the local Fisher information is

\[
\mathcal I_S=\sigma_t^{-2}J_S^T J_S.
\]

v0.21 compares three standard local design criteria:

- **E-optimality:** maximize the weakest singular direction,
  \[
  \max_S\sigma_{\min}(J_S).
  \]
- **D-optimality:** maximize information volume,
  \[
  \max_S\log\det(J_S^TJ_S).
  \]
- **A-optimality:** minimize total local parameter variance,
  \[
  \min_S\operatorname{tr}[(J_S^TJ_S)^{-1}].
  \]

All subsets of sizes four, five and six from the twelve candidate spike times are enumerated exactly. This is an experiment-design calculation on a regular physical event chart; no derivative is taken through an event-order `argmin`.

## Baseline: first two cycles

The v0.20 observation set is the first six spike times,

\[
S_{\rm base}=(0,1,2,3,4,5).
\]

Its singular values are

\[
(5.81134164,\;3.26704426,\;0.82982598,\;0.10170598),
\]

so

\[
\boxed{\sigma_{\min}^{\rm base}=0.1017059763}.
\]

At \(\sigma_t=10^{-4}\), its Fisher standard deviations are

\[
\boxed{
(6.2157\!\times10^{-4},\;7.7079\!\times10^{-4},\;2.8460\!\times10^{-5},\;3.4821\!\times10^{-5})
}
\]

for \((p,\tau_3,\eta_1,\eta_2)\).

## E-optimal designs

The best four-observation subset is

\[
\boxed{S_{E,4}=(1,2,9,11)}
\]

corresponding to

\[
\boxed{(t_{1,0},t_{2,0},t_{0,3},t_{2,3})}.
\]

It has

\[
\boxed{\sigma_{\min}=0.2898829236},
\]

which is already 2.85 times the weakest singular value of the six-spike v0.20 baseline, despite using only four observations.

The E-optimal six-observation subset is

\[
\boxed{S_{E,6}=(1,2,3,4,9,11)}
\]

or

\[
\boxed{(t_{1,0},t_{2,0},t_{0,1},t_{1,1},t_{0,3},t_{2,3})}.
\]

Its singular values are

\[
\boxed{(5.87646938,\;3.30080013,\;1.53281984,\;0.30865154)}
\]

and therefore

\[
\boxed{
\frac{\sigma_{\min}^{E,6}}{\sigma_{\min}^{\rm base}}
=3.03474.
}
\]

For \(\sigma_t=10^{-4}\), the corresponding Fisher standard deviations are

\[
\boxed{
(1.9321\!\times10^{-4},\;2.6674\!\times10^{-4},\;3.1963\!\times10^{-5},\;3.0476\!\times10^{-5})
}.
\]

Thus the marginal uncertainty of \(p\) drops by a factor about 3.22 and that of \(\tau_3\) by about 2.89 relative to the v0.20 baseline. The \(p/\tau_3\) correlation drops from about 0.969 to 0.919.

The E-optimal six-spike design captures about 93.1% of the weakest-direction information of all twelve observations, since the full four-cycle matrix has

\[
\sigma_{\min}(J_{12})=0.33164651.
\]

## D- and A-optimal designs

The D-optimal six-observation set is

\[
\boxed{S_{D,6}=(1,2,7,9,10,11)},
\]

or

\[
(t_{1,0},t_{2,0},t_{1,2},t_{0,3},t_{1,3},t_{2,3}).
\]

It gives

\[
\log\det(J_S^TJ_S)=4.9492653347.
\]

The baseline value is 0.9429773208, so the Fisher determinant is increased by

\[
\boxed{\exp(4.9492653-0.9429773)\approx54.94}.
\]

For this benchmark the A-optimal six-observation set coincides with the E-optimal set \(S_{E,6}\).

## Observation horizon is more valuable than dense early sampling

Restricting the candidate pool to the first \(C\) cycles and still allowing at most six observations gives the best E-optimal weakest singular values

\[
\boxed{
\begin{array}{c|ccc}
C&2&3&4\\\hline
\sigma_{\min}^{E}&0.101706&0.204161&0.308652
\end{array}}
\]

Hence spreading observations over later recurrent feedback cycles is substantially more informative than simply measuring all spikes early.

Importantly, the minimum physical truth-chart margin has already reached

\[
\boxed{m_{\min}\approx0.07291563284}
\]

by the second cycle. Extending the observation horizon through the fourth cycle does not reduce this minimum margin at the truth point. In this benchmark the extra information therefore costs observation time but does **not** move the nominal experiment closer to an event-order collision.

## Neuron-selection audit

Four cycles from any one neuron are formally rank four, but practical conditioning is poor. The weakest singular values are approximately

\[
\sigma_{\min}^{(0)}=0.001769,
\quad
\sigma_{\min}^{(1)}=0.026136,
\quad
\sigma_{\min}^{(2)}=0.016628.
\]

Thus structural rank alone is misleading.

Observing two neurons over four cycles is much better. The pair \((0,2)\) gives

\[
\boxed{\sigma_{\min}=0.235165},
\]

while \((1,2)\) gives 0.224444 and \((0,1)\) gives 0.125821. For this truth state, multi-neuron coverage is therefore far more valuable than a single long trace.

## Controlled extension: unknown observation clock offset

The observation design is strong enough to introduce one additional latent nuisance parameter, a global timestamp offset \(\delta t_0\):

\[
Y_{\rm obs}(\vartheta,\delta t_0)=Y(\vartheta)+\delta t_0\mathbf 1.
\]

The five-parameter sensitivity matrix is

\[
J_{\rm clock}=[J\;\mathbf1].
\]

The E-optimal six-observation design becomes

\[
\boxed{S_{E,6}^{\rm clock}=(0,1,2,3,9,11)}
\]

with singular values

\[
\boxed{(6.03223638,\;3.59463517,\;2.05515609,\;1.10308305,\;0.29868343)}.
\]

It is full rank five. At \(\sigma_t=10^{-4}\), Fisher predicts

\[
\boxed{
\operatorname{sd}(p,\tau_3,\eta_1,\eta_2,\delta t_0)
\approx
(1.9323\!\times10^{-4},2.8462\!\times10^{-4},3.2550\!\times10^{-5},3.4655\!\times10^{-5},5.5849\!\times10^{-5}).
}
\]

Thus a properly designed six-spike experiment can absorb an unknown global clock offset while retaining substantially better \(p/\tau_3\) precision than the old six-spike design with a known clock.

This is a local result only. v0.21 does not yet infer latent \((\psi_0,q_0)\), missing spike identities or topology.

## Direct small-noise audit

A deterministic 20-realisation nonlinear fit at \(\sigma_t=10^{-4}\) confirms the design trend. The empirical standard deviations for the original baseline are approximately

\[
(5.60\!\times10^{-4},7.26\!\times10^{-4},2.75\!\times10^{-5},3.07\!\times10^{-5}),
\]

whereas the E-optimal six-spike plan gives approximately

\[
\boxed{(2.14\!\times10^{-4},3.36\!\times10^{-4},2.97\!\times10^{-5},3.41\!\times10^{-5})}.
\]

For the five-parameter clock-offset experiment the direct empirical standard deviations are approximately

\[
(1.65\!\times10^{-4},2.69\!\times10^{-4},4.08\!\times10^{-5},3.77\!\times10^{-5},4.89\!\times10^{-5}).
\]

## Interpretation

v0.21 establishes three design principles for the project:

1. **Rank is not enough.** A measurement set may be structurally identifiable yet practically unusable because \(\sigma_{\min}\) is tiny.
2. **Feedback-separated observations matter.** Later recurrent cycles break the dominant \(p/\tau_3\) tradeoff much more effectively than dense early sampling.
3. **Hybrid robustness and statistical information are separate design axes.** Here the longer optimal plan improves Fisher information without reducing the nominal chart margin, but future designs should explicitly treat both.

## Benchmark contract B329–B350

- **B329** four-cycle truth replay yields twelve labelled spike times through 30 physical events.
- **B330** the 12-by-4 JAX sensitivity agrees with centered finite differences to relative error below \(10^{-8}\).
- **B331** the v0.20 first-six baseline reproduces \(\sigma_{\min}=0.1017059763\).
- **B332** exhaustive subset enumeration is used for observation budgets 4, 5 and 6.
- **B333** E-optimal four-observation set is `(1,2,9,11)`.
- **B334** E-optimal six-observation set is `(1,2,3,4,9,11)`.
- **B335** E-optimal six-spike \(\sigma_{\min}>0.308\).
- **B336** E-optimal improvement over baseline in \(\sigma_{\min}\) exceeds factor 3.
- **B337** D-optimal six-observation set is `(1,2,7,9,10,11)`.
- **B338** D-optimal Fisher determinant improvement over baseline exceeds factor 50.
- **B339** A-optimal six-observation set coincides with the E-optimal set for this benchmark.
- **B340** best E-optimal six-spike values through horizons 2, 3 and 4 are approximately `(0.101706,0.204161,0.308652)`.
- **B341** extending from cycle 2 to cycle 4 does not reduce the minimum nominal chart margin below `0.0729156328`.
- **B342** every one-neuron four-cycle trace is rank four but has \(\sigma_{\min}<0.03\).
- **B343** the two-neuron pair `(0,2)` over four cycles has \(\sigma_{\min}>0.23\).
- **B344** full twelve-observation \(\sigma_{\min}\approx0.33164651\).
- **B345** E-optimal six observations retain more than 93% of full-twelve weakest-direction information.
- **B346** clock-offset augmented design has five columns and remains full rank with six observations.
- **B347** E-optimal clock-offset six-set is `(0,1,2,3,9,11)` with \(\sigma_{\min}>0.298\).
- **B348** clock-offset Fisher standard deviation is below \(6\times10^{-5}\) at \(\sigma_t=10^{-4}\).
- **B349** direct noise audit confirms substantially smaller empirical \(p,\tau_3\) spread for the E-optimal design than for the baseline.
- **B350** observation design remains fixed-chart/chart-aware: no derivative is assigned through event-order selection.

## Next

CORE v0.22 should use these design criteria before enlarging the latent block. The natural next controlled test is latent synaptic state: introduce a low-dimensional gauge-fixed perturbation of \((\psi_0,q_0)\), compare identifiability under the baseline and v0.21-optimal schedules, and determine whether additional cycles or additional neurons are required. Unknown spike labels/topology should remain out of scope until continuous-state identifiability is understood.