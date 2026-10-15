# CORE v0.23 — transverse observation of the latent synaptic state

## Scope

CORE v0.22 showed that twelve labelled spike times formally identify

\[
\vartheta=(p,\tau_3,\eta_1,\eta_2,\xi_\psi,\xi_q),
\]

but leave one extremely weak phase/synapse direction with

\[
\sigma_{\min}(J_{\rm spike})\approx9.13748\times10^{-4}.
\]

The weak right singular vector is dominated by the initial phase variables and the projected initial synaptic drive \(\xi_\psi\). More spike-time rows barely improve this singular value. v0.23 therefore changes the measurement physics rather than merely extending the spike-time window.

The spatial contrast remains

\[
v=\frac{1}{\sqrt6}(2,-1,-1),
\]

with

\[
\psi_0=\psi_{0,*}+\xi_\psi v,
\qquad
q_0=q_{0,*}+\xi_qv.
\]

## Pre-event projected synaptic measurement

Before the first firing or arrival event the alpha-synapse state evolves exactly as

\[
q(t)=e^{-\alpha t}q_0,
\qquad
\psi(t)=e^{-\alpha t}(\psi_0+tq_0).
\]

Because the reference synchronous components are spatially uniform and \(v^T\mathbf1=0\), the projected subthreshold observable is

\[
\boxed{
z_\psi(t)=v^T\psi(t)=e^{-\alpha t}(\xi_\psi+t\xi_q).
}
\]

Its sensitivity row in the six-dimensional unknown coordinates is

\[
\boxed{
g(t)=e^{-\alpha t}(0,0,0,0,1,t).
}
\]

This measurement is non-perturbing: it does not alter the packet queue, event roots or chart sequence.

## Rank-one information bound

Appending one scalar measurement changes the Gram matrix from

\[
G=J^TJ
\]

to

\[
G_+=J^TJ+g^Tg.
\]

This is a positive rank-one update. Eigenvalue interlacing therefore bounds the new weakest singular value by the old second-weakest one,

\[
\boxed{
\sigma_6([J;g])\le \sigma_5(J).
}
\]

For the v0.22 full twelve-spike Jacobian,

\[
\sigma_6(J)=9.13748422798\times10^{-4},
\qquad
\sigma_5(J)=0.228772004925.
\]

Numerically optimizing the pre-event measurement time gives

\[
\boxed{t_m=0.698919300895.}
\]

The first physical spike occurs only at

\[
t_1=8.15276289049,
\]

so the measurement precedes the first hybrid event by

\[
\boxed{7.45384358959}
\]

time units.

At this time

\[
g(t_m)\approx(0,0,0,0,0.705068970508,0.492786311950)
\]

and

\[
\boxed{
\sigma_{\min}([J;g(t_m)])=0.228772004925.
}
\]

Thus the physically realizable scalar measurement saturates the rank-one interlacing bound to numerical precision. Relative to spike times alone,

\[
\boxed{
\frac{0.228772004925}{9.13748422798\times10^{-4}}
\approx250.3665.
}
\]

The single observation removes the unique information bottleneck without exposing a new weaker direction.

## Why measure \(\psi\), not only \(q\)?

At the chart origin a direct projected \(\psi\) measurement adds the row

\[
(0,0,0,0,1,0)
\]

and raises the weakest singular value to

\[
0.198175101975,
\]

a factor \(216.88\) improvement.

A projected \(q\) measurement adds

\[
(0,0,0,0,0,1)
\]

but reaches only

\[
0.0260855657632,
\]

a factor \(28.55\). This is consistent with the v0.22 weak singular vector, whose \(\xi_\psi\) component has magnitude \(0.78635\) while its \(\xi_q\) component has magnitude only \(0.07659\).

Allowing a short pre-event evolution mixes \(\xi_\psi\) and \(\xi_q\) in exactly the combination needed to attain the rank-one optimum.

## Mixed-noise reference benchmark

Raw singular values mix observation units, so v0.23 also fixes an explicit reference noise model:

\[
\sigma_t=10^{-4}
\]

for each labelled spike time and

\[
\boxed{\sigma_z=2\times10^{-4}}
\]

for the projected synaptic measurement.

After whitening by a common timing-noise scale the augmented Jacobian is

\[
\widetilde J=
\begin{bmatrix}
J\\
(\sigma_t/\sigma_z)g(t_m)
\end{bmatrix}.
\]

Here \(\sigma_t/\sigma_z=1/2\), and the full twelve-spike plus one-sensor system still reaches

\[
\boxed{\sigma_{\min}(\widetilde J)=0.228772004925,}
\]

again saturating the old second-smallest singular value.

The sensor need not be this accurate to remain useful. Holding \(t_m\) fixed, the largest sensor standard deviations that retain prescribed gains over spike-only observation are approximately

\[
\boxed{\sigma_z^{100\times}=5.65422\times10^{-4}},
\]

\[
\boxed{\sigma_z^{200\times}=2.82585\times10^{-4}}.
\]

Thus the two-order-of-magnitude information gain survives sensor noise several times larger than the benchmark spike-time noise.

## Joint spike/sensor experiment design

Once the new measurement is present, fewer spike times are required. Under the reference mixed-noise model, exhaustive E-optimal selection gives

\[
\boxed{S_{5+z}=(0,2,9,10,11)}
\]

for five spike times plus one analog observation, with

\[
\sigma_{\min}\approx0.175067477.
\]

Using six spike times plus the sensor gives

\[
\boxed{S_{6+z}=(0,2,3,9,10,11)}
\]

and

\[
\boxed{\sigma_{\min}\approx0.200974241.}
\]

For \(S_{6+z}\), the Fisher standard deviations under the stated noise model are approximately

\[
\boxed{
(2.46446,3.70010,3.55933,1.81926,3.75369,3.15659)\times10^{-4}.
}
\]

Compared with the old six-spike v0.22 baseline, this reduces the latent phase/synapse uncertainty by factors between roughly \(27\) and \(237\), while also improving \(p\) and \(\tau_3\) by factors about \(2.62\) and \(2.19\).

## Elimination of the v0.22 weak direction and nonlinear alias

For the finite v0.22 weak-direction displacement of amplitude \(0.01\), the new measurement changes by

\[
\boxed{|\Delta z_\psi|\approx0.00516687.}
\]

At the reference sensor noise this is

\[
\boxed{25.83\sigma_z.}
\]

The exact same-chart nonlinear alias found in v0.22 gives

\[
\boxed{|\Delta z_\psi|\approx0.00404477=20.22\sigma_z.}
\]

so the formerly invisible alias is strongly rejected by one scalar measurement.

A deterministic twelve-start noiseless audit confirms the nonlinear result: both the E-optimal five-spike-plus-sensor and six-spike-plus-sensor experiments return the true six-dimensional parameter/state vector from all twelve v0.22 multistart initializations. The corresponding spike-only experiments admitted alternative exact or near-exact fits.

## Direct noise audit

A thirty-realization nonlinear audit for the six-spike-plus-sensor design at

\[
\sigma_t=10^{-4},\qquad \sigma_z=2\times10^{-4}
\]

gives empirical standard deviations

\[
(2.18564,3.50836,3.26468,1.66248,3.58661,2.80282)\times10^{-4},
\]

against Fisher predictions

\[
(2.46446,3.70010,3.55933,1.81926,3.75369,3.15659)\times10^{-4}.
\]

All empirical/Fisher ratios lie between \(0.887\) and \(0.955\), so the augmented experiment has returned the six-dimensional inverse problem to a locally regular small-noise regime at the original \(10^{-4}\) timing-noise scale.

## Hybrid interpretation

The new information is acquired strictly before the first event. Therefore:

- no packet is created or destroyed;
- no firing or arrival root is moved;
- no event-order surface is crossed;
- the physical chart and all one-sided event derivatives remain those of v0.22.

This cleanly separates an observation-design failure from a hybrid-differentiation failure. The v0.22 ambiguity was not caused by event nonsmoothness; it was caused by insufficiently transverse observation physics.

## CORE conclusion

\[
\boxed{
\text{More spike times}\not\Rightarrow\text{resolution of latent synaptic state}.
}
\]

But

\[
\boxed{
\text{one well-placed transverse subthreshold measurement}
\Rightarrow
\text{250-fold recovery of the weakest local information direction}.
}
\]

The v0.23 rule is therefore:

> When a latent direction remains weak under longer observation of the same output channel, change the observation operator before enlarging the latent model further.

## Scope and next step

v0.23 uses an idealized scalar readout of the known spatial projection \(v^T\psi\). It does not yet model a particular experimental sensor, measurement filtering, unknown projection direction, or a perturbative input pulse.

The next CORE stage should test whether the same transverse information can be generated **without direct access to \(\psi\)**, using a small known input pulse and spike times only. That would turn the v0.23 observability result into an active-experiment / system-identification design problem while preserving the chart-aware hybrid machinery.
