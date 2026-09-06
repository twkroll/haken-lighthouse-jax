# CORE v0.24 — active hybrid experiment design with spike-time readout only

## Scope

CORE v0.22 exposed a severe phase/synapse weak direction in the six-unknown inverse problem

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q),
\]

with twelve spike times but

\[
\sigma_{\min}(J_{\rm passive})\approx9.13748\times10^{-4}.
\]

CORE v0.23 removed this weakness by adding a direct projected synaptic-state measurement. v0.24 removes that direct sensor again and asks whether a known pre-event intervention can transfer the hidden synaptic information into subsequent spike times.

The only measured outputs in v0.24 are labelled spike times.

## Probe pulse semantics

The external probe is represented as a known alpha-synaptic kick at a prescribed time \(t_p\):

\[
q(t_p^+)=q(t_p^-)+A d,\qquad \psi(t_p^+)=\psi(t_p^-).
\]

This is the same state jump produced by an ordinary alpha-synapse arrival, except that the probe amplitude, direction, and time are externally prescribed and are not inferred.

The zero-mean q=1 plane is spanned by

\[
v=\frac{1}{\sqrt6}(2,-1,-1),\qquad
 e_2=\frac{1}{\sqrt2}(0,1,-1).
\]

A general unit probe direction can be written

\[
d(\gamma)=\cos\gamma\,v+\sin\gamma\,e_2.
\]

The reference intervention deliberately uses the exact symmetry direction \(d=v\).

## Design constraints

Active experiment design is constrained independently of the information objective.

The reference admissible class imposes

\[
t_p\ge0.1,
\qquad |A|\le0.3,
\qquad m_{\rm chart}\ge0.075,
\]

where \(m_{\rm chart}\) is the minimum time gap between the realized event and its nearest competitor over the four-cycle observation window.

The lower time bound prevents the pulse from becoming merely a redefinition of the unknown initial state. The amplitude bound is an explicit intervention budget. The chart-margin floor prevents information from being purchased by driving the trajectory arbitrarily close to an event-order collision.

## Reference safe pulse

The symmetry-exact reference is

\[
\boxed{t_p=0.1,\qquad A=0.3,\qquad d=v.}
\]

At the truth parameter/state vector, the first firing occurs at

\[
t_1\approx7.35719995237,
\]

so the pulse precedes the first firing by about \(7.25720\) time units.

The minimum physical event-chart margin is

\[
\boxed{m_{\rm chart}\approx0.09631568>0.075.}
\]

The resulting twelve-spike sensitivity singular values are approximately

\[
(13.54949,\ 8.29220,\ 2.61166,\ 0.925263,\ 0.421831,\ 0.09406042).
\]

Thus

\[
\boxed{\sigma_{\min}^{\rm active}\approx0.09406042}
\]

and

\[
\boxed{
\frac{\sigma_{\min}^{\rm active}}
{\sigma_{\min}^{\rm passive}}
\approx102.94.
}
\]

A constrained angular audit at the same \((t_p,A)\) places the highest-information direction allowed exactly at the margin floor near \(\gamma\approx-0.01279\) rad, with \(\sigma_{\min}\approx0.09505\). The exact symmetry direction \(v\) loses only about one percent in \(\sigma_{\min}\) while increasing the minimum margin to \(0.0963\), so it is used as the reproducible reference.

## Differentiation audit

The probe is a fixed known reset. Once the physical post-probe event chart is recorded, the one-sided fixed-chart JAX Jacobian is obtained by differentiating the same hybrid replay used in v0.22.

At the reference pulse,

\[
\frac{\|J_{\rm JAX}-J_{\rm FD}\|_F}{\|J_{\rm FD}\|_F}
\approx1.97\times10^{-9}.
\]

The active intervention therefore does not require a new differentiation convention.

## Weak-direction and alias rejection using spike times only

Let \(r_{\min}\) denote the v0.22 weak right singular vector. For the finite displacement

\[
\vartheta_w=\vartheta_*+0.01r_{\min},
\]

the active-probe spike-time residual satisfies

\[
\frac{\|Y_{\rm active}(\vartheta_w)-Y_{\rm active}(\vartheta_*)\|_2}
{10^{-4}}
\approx34.54.
\]

The same physical event chart is retained and the minimum margin remains about \(0.09577\).

For the exact same-chart nonlinear alias identified in v0.22,

\[
\frac{\|Y_{\rm active}(\vartheta_{\rm alias})-Y_{\rm active}(\vartheta_*)\|_2}
{10^{-4}}
\approx27.52,
\]

again without changing the event chart.

Thus the probe converts the previously almost invisible phase/synapse direction into a strongly observable spike-time signature.

## Observation reduction

Exhaustive E-optimal selection among the twelve post-probe spike times gives the six-row schedule

\[
\boxed{S_{E,6}=(0,1,2,3,4,11)}
\]

with

\[
\sigma_{\min}\approx0.08862936.
\]

A deterministic twelve-start noiseless audit converges to the true six-dimensional state/parameter vector for all twelve starts using either all twelve spike times or this six-spike schedule.

## Noise audit

For labelled spike-time noise

\[
\sigma_t=10^{-4},
\]

the full twelve-spike Fisher standard deviations at the reference pulse are approximately

\[
(7.28\!\times\!10^{-5},\ 1.51\!\times\!10^{-4},\ 3.92\!\times\!10^{-4},\ 2.03\!\times\!10^{-4},\ 9.37\!\times\!10^{-4},\ 3.14\!\times\!10^{-4}).
\]

A deterministic thirty-realization nonlinear audit gives empirical/Fisher marginal-standard-deviation ratios between approximately \(0.857\) and \(1.053\).

Therefore the active probe restores a regime in which the local Fisher approximation is quantitatively useful at the original \(10^{-4}\) timing-noise scale, despite using spike times only.

## Scientific interpretation

v0.22 showed that passive spike-time observation could not separate initial phase from a projected initial synaptic state. v0.23 fixed this with a new measurement operator. v0.24 shows that the same missing information can instead be generated dynamically:

\[
\boxed{
\text{known probe}\to
\text{state-dependent transient}\to
\text{transverse spike-time sensitivity}.
}
\]

The gain is smaller than the ideal direct sensor of v0.23, but it exceeds two orders of magnitude and requires no direct synaptic-state readout.

The important design rule is

> Active hybrid experiment design must optimize information and chart safety as separate constraints. A pulse is not accepted merely because it increases a singular value; the physical event-order margin must remain explicitly bounded away from zero.

## Benchmark contract B400–B423

- B400: external probe is a known q-state jump and not an inferred parameter.
- B401: probe direction has zero spatial mean and unit norm.
- B402: reference probe uses the q=1 symmetry direction v.
- B403: reference probe time is 0.1.
- B404: reference probe amplitude is 0.3.
- B405: actuation deadtime is at least 0.1.
- B406: intervention amplitude budget is at most 0.3.
- B407: physical minimum chart margin exceeds 0.075.
- B408: probe precedes the first firing by more than 7.2 time units.
- B409: active full-12 sigma_min exceeds 0.094.
- B410: active/passive sigma_min gain exceeds 100.
- B411: fixed-chart JAX/FD Jacobian relative error is below 1e-8.
- B412: the v0.22 finite weak displacement stays on the same active event chart.
- B413: weak-displacement spike residual exceeds 34 timing-noise standard deviations.
- B414: the v0.22 nonlinear alias stays on the same active event chart.
- B415: alias spike residual exceeds 27 timing-noise standard deviations.
- B416: E-optimal six-spike active design is (0,1,2,3,4,11).
- B417: E-optimal six-spike sigma_min exceeds 0.088.
- B418: twelve-start all-spike noiseless recovery returns truth 12/12.
- B419: twelve-start six-spike noiseless recovery returns truth 12/12.
- B420: thirty-realization timing-noise audit uses sigma_t=1e-4.
- B421: empirical/Fisher marginal std ratios remain between 0.80 and 1.10.
- B422: no direct psi/q measurement is used in the v0.24 inverse problem.
- B423: information objective and chart-safety constraint are reported separately.

## Next

CORE v0.25 should replace the ideal instantaneous known q-kick by a finite-duration input waveform with uncertain actuator gain and timing. The key question is whether the information gain survives realistic actuation nuisance parameters without reintroducing the v0.22 weak direction. Only after that should the full q=1 synaptic latent subspace or missing spike labels be added.
