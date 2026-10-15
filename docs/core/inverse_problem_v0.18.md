# CORE chart-aware inverse problem v0.18

## Purpose

CORE v0.18 is the first controlled system-identification benchmark built on the sparse JAX graph/event machinery of v0.17. The goal is deliberately narrower than generic black-box fitting: infer continuous Lighthouse parameters from labelled spike times **inside one certified hybrid event chart**, quantify local identifiability, and stop the gradient when the event order ceases to be valid.

The benchmark therefore separates three objects:

1. the physical value dynamics;
2. the differentiable fixed-chart observation map;
3. the chart-validity sentinel.

This is the correct hybrid analogue of ordinary smooth parameter estimation.

### Provenance

- **[H/C]** Lighthouse phase dynamics with delayed alpha-synapse coupling;
- **[P]** exact event and packet semantics from CORE v0.13--v0.17;
- **[P]** sparse graph continuous edge parameters from v0.17;
- **[P]** fixed-chart spike-time inverse problem, identifiability audit, noise audit and chart-boundary guard introduced here.

---

## 1. Conditional inverse problem

Use the verified three-cell ring and infer

\[
\boxed{\theta=(p,\tau_3)}.
\tag{I1}
\]

The topology is known. The hybrid state at the observation start is also treated as known. This is intentional: v0.18 isolates parameter identifiability before latent initial-state inference is introduced.

The truth is

\[
\boxed{p_*=-3.267985407948901,\qquad \tau_{3,*}=8.0.}
\tag{I2}
\]

The known start state is taken after the two initial symmetric arrival batches,

\[
\psi_i=-0.207423841618632,
\qquad
q_i=0.780899408476725,
\tag{I3}
\]

with

\[
\phi=(1.838519273976891,\ 1.488519273976891,\ 1.658519273976891).
\tag{I4}
\]

The queue is empty at this observation origin.

The data vector contains the next six labelled firing times,

\[
\boxed{
Y_*= (
8.152762890488507,
8.566089299061751,
8.964878908823215,
24.62568933324277,
24.69860496608047,
25.36630107670213
).
}
\tag{I5}
\]

The first three firings occur before any new delayed packet arrives and therefore have zero first-order sensitivity to `(p,tau3)`. The second triplet supplies the local information needed for identification.

---

## 2. Fixed-chart observation map

Let `sigma=(sigma_0,...,sigma_K)` be the event itinerary recorded at the truth. For a fixed chart define

\[
\boxed{Y_\sigma(\theta)=\text{labelled spike times obtained by replaying exactly }\sigma.}
\tag{I6}
\]

At firing event `i`, the event time solves

\[
G_i(\Delta;\theta)=
\phi_i+\int_0^\Delta S(\psi_i(s;\theta))\,ds-2\pi=0.
\tag{I7}
\]

A stored chart event time is used only as a `stop_gradient` Newton initializer. The converged root remains differentiable through the implicit equation, so JAX differentiates the physical event time rather than the discrete root-bracketing logic.

For a frozen long packet,

\[
\Delta_a=\rho\tau_3,
\tag{I8}
\]

and an arrival applies

\[
q_{t_e}^{+}=q_{t_e}^{-}+w_e\alpha^2.
\tag{I9}
\]

Thus `p` enters through graph weights and `tau3` through long-edge flight times.

---

## 3. Chart-validity sentinel

A derivative of `Y_sigma` is scientifically meaningful only while `sigma` remains the physical event order. Before every event define the chart margin

\[
\boxed{
m_k(\theta)
=
\min_{j\ne\sigma_k}
\left[t_j(\theta)-t_{\sigma_k}(\theta)\right].
}
\tag{I10}
\]

The chart is regular when

\[
\boxed{m(\theta)=\min_k m_k(\theta)>0.}
\tag{I11}
\]

At `m=0`, two event surfaces are reached simultaneously. Beyond that point a different itinerary is physical and the old chart derivative is rejected.

For the present inference slice at `tau3=8`, the first recorded-chart collision occurs at

\[
\boxed{p_{\rm chart}=-3.7871304438487.}
\tag{I12}
\]

It is a firing-order collision between neurons 0 and 2. Numerically,

\[
m(-3.7870)=+1.90358\times10^{-5},
\tag{I13}
\]

whereas

\[
m(-3.7872)=-1.01505\times10^{-5}.
\tag{I14}
\]

So the reference event order is valid on the first side and invalid on the second. v0.18 therefore treats `m<=0` as a **gradient stop / chart rerecord condition**, not as an invitation to differentiate through `argmin`.

---

## 4. Local identifiability

At the truth,

\[
J
=\frac{\partial Y_\sigma}{\partial(p,\tau_3)}
\in\mathbb R^{6\times2}
\tag{I15}
\]

is

\[
J\approx
\begin{pmatrix}
0&0\\
0&0\\
0&0\\
-0.3761171863&0.3208059661\\
-0.2422300227&0.3280063905\\
-0.4885778472&0.2585715365
\end{pmatrix}.
\tag{I16}
\]

Its singular values are

\[
\boxed{\sigma_1=0.8332999615,\qquad \sigma_2=0.1477257872,}
\tag{I17}
\]

hence

\[
\boxed{\kappa_2(J)=5.6408564632.}
\tag{I18}
\]

The two continuous parameters are therefore locally identifiable from this short spike-time window.

A central finite-difference audit gives

\[
\boxed{
\frac{\|J_{\rm JAX}-J_{\rm FD}\|_F}{\|J_{\rm FD}\|_F}
=3.76\times10^{-9}.
}
\tag{I19}
\]

---

## 5. Noiseless recovery

Use nonlinear least squares

\[
\mathcal L(\theta)
=\frac12\|Y_\sigma(\theta)-Y_*\|_2^2.
\tag{I20}
\]

Three deliberately separated starts were tested:

\[
(-3.0,7.7),\qquad(-3.5,8.2),\qquad(-2.9,8.15).
\tag{I21}
\]

All remain inside the same regular chart and converge in five function evaluations to

\[
\boxed{
(p,\tau_3)=(-3.2679854079489,\ 8.0000000000000)
}
\tag{I22}
\]

within floating-point tolerance.

This is not a claim of global identifiability. It is a certified local inverse problem in one hybrid chart.

---

## 6. Small-noise audit

For independent spike-time noise

\[
\epsilon_k\sim N(0,\sigma_t^2),
\qquad
\sigma_t=10^{-4},
\tag{I23}
\]

the linear covariance prediction is

\[
\operatorname{Cov}(\hat\theta)
\approx
\sigma_t^2(J^TJ)^{-1}.
\tag{I24}
\]

This gives predicted standard deviations

\[
\boxed{
\operatorname{sd}(p)\approx4.27826\times10^{-4},
\qquad
\operatorname{sd}(\tau_3)\approx5.38145\times10^{-4}.
}
\tag{I25}
\]

A deterministic 20-realization synthetic-noise audit gives

\[
\boxed{
\operatorname{sd}_{\rm MC}(p)\approx4.93374\times10^{-4},
\qquad
\operatorname{sd}_{\rm MC}(\tau_3)\approx5.68116\times10^{-4}.
}
\tag{I26}
\]

with sample mean

\[
(-3.2679370290,\ 8.0000696265).
\tag{I27}
\]

The empirical dispersion is consistent with the local Fisher prediction at this deliberately tiny sample size.

---

## 7. What v0.18 certifies

CORE v0.18 certifies:

- continuous-parameter recovery from labelled Lighthouse spike times;
- full-rank local sensitivity of `(p,tau3)` in a short observation window;
- JAX/finite-difference agreement for the fixed-chart spike-time Jacobian;
- noiseless multi-start recovery;
- a small-noise uncertainty sanity check;
- an explicit event-order margin and chart-boundary location;
- refusal to reuse a smooth gradient after the chart becomes invalid.

It does **not** yet certify:

- unknown topology;
- latent initial-state inference;
- automatic optimization across multiple event charts;
- gradients exactly on simultaneous-event surfaces;
- robustness to missed or mislabelled spikes;
- large-N statistical identifiability.

---

## 8. Benchmark contract B269--B288

- **B269** truth is `(p,tau3)=(-3.267985407948901,8)`.
- **B270** known start state equals (I3)--(I4) and has an empty queue.
- **B271** truth replay reproduces all six stored labelled spike times to `1e-12`.
- **B272** first three spike-time sensitivity rows are numerically zero.
- **B273** `sigma_min(J)>0.14`.
- **B274** `cond_2(J)<6`.
- **B275** JAX/central-FD Jacobian relative error is below `1e-7`.
- **B276** each of the three stored initial guesses converges to truth within `5e-12` max parameter error.
- **B277** each noiseless fit requires at most six function evaluations.
- **B278** noise level is `sigma_t=1e-4`.
- **B279** Fisher-predicted `sd(p)` is approximately `4.27826e-4`.
- **B280** Fisher-predicted `sd(tau3)` is approximately `5.38145e-4`.
- **B281** stored 20-run empirical `sd(p)` is approximately `4.93374e-4`.
- **B282** stored 20-run empirical `sd(tau3)` is approximately `5.68116e-4`.
- **B283** the first chart collision on the `tau3=8` slice is near `p=-3.78713044385`.
- **B284** chart margin at `p=-3.7870` is positive.
- **B285** chart margin at `p=-3.7872` is negative.
- **B286** a nonpositive chart margin invalidates the fixed-chart gradient.
- **B287** topology remains discrete and is not differentiated.
- **B288** chart-aware multi-chart continuation is deferred to the next CORE stage.

---

## 9. Next

CORE v0.19 should turn the v0.18 sentinel into an actual **hybrid trust-region optimizer**:

1. optimize inside the current regular chart;
2. predict distance to the nearest event-order surface;
3. shorten a step before the guard is violated;
4. if crossing is required, evaluate the physical value scheduler, record the new chart, and restart differentiation there;
5. extend the inverse state to include selected edge-specific weights/delays and, only after that is stable, latent initial-state variables.

That will be the first optimizer in the project that can move through a piecewise-smooth event landscape without pretending it is globally smooth.
