# CORE v0.24 — chart-safe active probe with spike-time readout only

## Scope

CORE v0.22 showed that the six-dimensional inverse problem

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q)
\]

is formally identifiable from twelve labelled spike times but has a severe phase/synapse weak direction,

\[
\sigma_{\min}(J_{\rm unforced})\approx9.13748\times10^{-4}.
\]

CORE v0.23 removed that weakness with one direct projected synaptic-state observation. v0.24 removes the direct state readout again. The only measurements are spike times, but the experiment is actively probed by one known pre-event input.

The goal is to create information transverse to the v0.22 weak direction without approaching an event-order collision.

## Probe semantics

Let

\[
v_1=\frac{1}{\sqrt6}(2,-1,-1),
\qquad
v_2=\frac{1}{\sqrt2}(0,1,-1).
\]

They form an orthonormal basis of the zero-mean spatial subspace. A unit probe direction is

\[
d(\beta)=\cos\beta\,v_1+\sin\beta\,v_2,
\qquad
\mathbf 1^Td=0,
\qquad
\|d\|_2=1.
\]

The control is an instantaneous alpha-like jump of the synaptic auxiliary state,

\[
q(t_p^+)=q(t_p^-)+A\,d(\beta),
\qquad
\psi(t_p^+)=\psi(t_p^-).
\]

It is known, deterministic and independent of the inferred parameters. After the probe, no extra state is observed; the inference data are again only labelled spike times.

The amplitude budget is

\[
0\le A\le A_{\max}=\alpha^2=0.25.
\]

Thus the total probe norm is no larger than one native Lighthouse alpha-synapse q-jump. The reference probe is applied at the beginning of the experiment, before any natural hybrid event,

\[
t_p=0^+.
\]

## Hybrid safety constraint

Active design is not allowed to gain apparent information by pushing the trajectory close to a firing/arrival-order collision. For every candidate probe we evaluate the physical scheduler and require

\[
m_{\rm chart}=\min_k\min_{j\ne\sigma_k}
(t_j-t_{\sigma_k})\ge 0.10.
\]

The unforced v0.22 truth trajectory has

\[
m_{\rm chart}^{(0)}\approx0.07291563284.
\]

Hence the v0.24 reference constraint is stricter than the unforced operating point.

## Budget-constrained reference design

A bounded search over pulse time, amplitude and the two-dimensional zero-mean direction finds that the useful region is at the earliest allowed probe time and at the native-jump amplitude budget. We retain the rounded, margin-robust reference

\[
\boxed{
 t_p=0^+,\qquad A=0.25,\qquad \beta=-0.4.
}
\]

Its direction is

\[
\boxed{
d_*\approx(0.7520431524,-0.6513819268,-0.1006612256)
}
\]

and the actual q jump is

\[
A d_*\approx(0.1880107881,-0.1628454817,-0.0251653064).
\]

The physical pulsed truth chart has

\[
\boxed{m_{\rm chart}^{\rm pulse}\approx0.10172701083},
\]

which is about 1.395 times the unforced minimum margin. The probe therefore makes the reference trajectory *farther* from a hybrid event-order collision.

## Spike-time information gain

Using the twelve labelled firing times over four cycles after the known probe, the six-parameter sensitivity matrix has singular values

\[
\boxed{
(11.44827254,\ 8.03549518,\ 2.68364921,\ 0.89499991,\ 0.36900830,\ 0.09678593).
}
\]

Therefore

\[
\boxed{
\sigma_{\min}(J_{\rm pulse})=0.09678593054
}
\]

and

\[
\boxed{
\frac{\sigma_{\min}(J_{\rm pulse})}
{\sigma_{\min}(J_{\rm unforced})}
\approx105.9219.
}
\]

The condition number falls from approximately 11944 to

\[
\boxed{\kappa_2(J_{\rm pulse})\approx118.2845}.
\]

This does not match the idealized direct-readout rank-one optimum of v0.23, which achieved about 250x, but it obtains an orders-of-magnitude improvement using spike times only.

## Derivative validation

The pulsed fixed-chart JAX Jacobian is checked against central finite differences in which every perturbed parameter point is re-simulated by the physical hybrid scheduler. The relative Frobenius error is

\[
\boxed{
\frac{\|J_{\rm JAX}-J_{\rm FD}\|_F}{\|J_{\rm FD}\|_F}
\approx1.83\times10^{-9}.
}
\]

The perturbed points retain the same event chart. Thus the information gain is not a differentiation artifact.

## Six-spike active design

After fixing the probe, exhaustive E-optimal selection of six spike times gives indices

\[
\boxed{S_{E,6}^{\rm pulse}=(0,1,2,3,10,11)}
\]

with

\[
\boxed{\sigma_{\min}=0.08311918946}.
\]

The corresponding singular values are approximately

\[
(9.05500679,5.58272601,1.50685317,0.77357133,0.27799164,0.08311919).
\]

Thus one known active probe plus only six spike times can support the same six-dimensional inverse block without direct synaptic observation.

For spike-time noise \(\sigma_t=10^{-4}\), the Fisher marginal standard deviations are approximately

\[
(1.1841\times10^{-4},\ 1.5727\times10^{-4},\ 4.5972\times10^{-4},\ 2.4864\times10^{-4},\ 1.0618\times10^{-3},\ 3.9883\times10^{-4}).
\]

Using all twelve pulsed spike times gives approximately

\[
(6.9466\times10^{-5},\ 1.4504\times10^{-4},\ 4.2390\times10^{-4},\ 2.2719\times10^{-4},\ 9.0149\times10^{-4},\ 2.9192\times10^{-4}).
\]

## Direct rejection of the v0.22 weak direction and nonlinear alias

The finite v0.22 weak-direction displacement of amplitude 0.01 remains on the same pulsed event chart, with minimum margin about 0.101005. Yet its complete pulsed spike vector differs from truth by

\[
\frac{\|\Delta Y\|_2}{10^{-4}}\approx28.879.
\]

The exact same-chart nonlinear alias identified in v0.22 is also destroyed by the active experiment. Under the same known pulse it remains on the same event chart, with minimum margin about 0.101173, but

\[
\boxed{
\frac{\|\Delta Y_{\rm alias}\|_2}{10^{-4}}\approx22.978.
}
\]

Hence the pulse converts the previously hidden phase/synapse direction into a large spike-time signature without invoking any event collision.

## Nonlinear recovery

A deterministic twelve-start audit uses the same spread of initial guesses as the previous latent-state tests. Both

- all twelve pulsed spike times, and
- the E-optimal six-spike subset

return the true six-dimensional parameter/state vector in 12/12 starts. Every converged solution is verified by the physical scheduler to lie on the pulsed truth chart.

At \(\sigma_t=10^{-4}\), a 100-realisation direct nonlinear audit is consistent with the local Fisher prediction. For the full twelve-spike experiment the empirical/Fisher marginal-standard-deviation ratios are approximately

\[
(1.053,0.948,1.043,1.036,0.989,0.968),
\]

and for the six-spike design approximately

\[
(1.013,1.117,1.144,1.142,1.117,1.055).
\]

## Interpretation

v0.23 showed that the v0.22 failure was an observation-operator deficiency. v0.24 shows that a direct synaptic-state sensor is not mathematically necessary: a known control input can rotate the subsequent spike-time sensitivity matrix away from the hidden initial-state direction.

The key design rule is

\[
\boxed{
\text{maximize information subject to an explicit hybrid safety margin,}
}
\]

not maximize information without regard to event geometry.

In this benchmark, information and hybrid robustness are not in conflict: the selected pulse increases both \(\sigma_{\min}\) and the minimum event margin.

## Benchmark contract B400--B423

B400. Probe direction is zero mean and unit norm.

B401. Probe is an additive q jump with no direct observation channel.

B402. Amplitude budget is \(A\le\alpha^2=0.25\).

B403. Reference probe is \((t_p,A,\beta)=(0^+,0.25,-0.4)\).

B404. Reference direction equals the stored vector to numerical tolerance.

B405. Pulsed physical chart contains 31 events through four firing cycles.

B406. Pulsed truth spike vector matches the stored reference.

B407. Minimum pulsed chart margin is greater than 0.10.

B408. Pulsed chart margin exceeds the unforced v0.22 truth margin.

B409. Pulsed fixed-chart JAX replay matches the physical truth trajectory.

B410. JAX vs physically rerecorded central-FD Jacobian relative error is below \(10^{-8}\).

B411. Full twelve-spike pulsed sensitivity has rank six.

B412. Full pulsed \(\sigma_{\min}\) exceeds 0.096.

B413. Information gain over unforced v0.22 exceeds 100x.

B414. Pulsed condition number is below 120.

B415. E-optimal six-spike indices are `(0,1,2,3,10,11)`.

B416. E-optimal six-spike \(\sigma_{\min}\) exceeds 0.083.

B417. Stored Fisher marginal standard deviations reproduce from the pulsed Jacobians.

B418. v0.22 finite weak displacement remains on the same pulsed physical chart.

B419. That weak displacement produces total spike residual greater than 28 timing-noise standard deviations.

B420. v0.22 nonlinear alias remains on the same pulsed physical chart.

B421. The nonlinear alias produces total pulsed spike residual greater than 22 timing-noise standard deviations.

B422. Twelve-start noiseless recovery returns truth for both full12 and E-optimal six-spike pulsed designs.

B423. Direct timing-noise audit is consistent with Fisher scale and does not require any direct synaptic-state readout.

## Scope and next step

v0.24 uses an idealized instantaneous q impulse with known amplitude and spatial direction. It does not yet model pulse duration, actuator filtering, uncertain stimulation amplitude/direction, energetic cost beyond the hard native-jump budget, or closed-loop adaptive experiment design.

The next target should replace the ideal impulse by a finite-width actuator model and jointly optimize information, pulse energy and chart safety under actuator uncertainty. Only after that should the project enlarge the latent synaptic subspace or move to unknown spike labels/topology.
