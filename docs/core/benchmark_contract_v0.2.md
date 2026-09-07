# CORE analytical benchmark contract v0.2

This file specifies numerical targets that later implementations must reproduce. It intentionally separates **exact** identities from **asymptotic** slow-synapse checks.

All tolerances below are targets for double precision unless an implementation explicitly documents a different precision policy.

---

## B0 — isolated linear Lighthouse neuron [exact]

Model:

\[
S_L(x)=\gamma x-\Theta,
\qquad \psi=0.
\]

Parameters:

- `gamma = 1`
- `Theta = -1`
- `theta(0)=0`

Reference:

\[
\theta(t)=t,
\qquad
T=2\pi.
\]

Required checks:

- first event time: `2*pi`;
- event `m` occurs at `2*pi*m`;
- phase error between events agrees with `theta=t` up to solver tolerance.

Suggested tolerance:

- relative event-time error `< 1e-10` for an exact/event-driven reference path;
- looser tolerances must be justified for fixed-step surrogate paths.

---

## B1 — alpha-kernel impulse response [exact]

Parameters:

- `alpha = 2`
- one spike at `t=0`
- pre-spike states `a=0`, `u=0`
- event jump `u += alpha`

Reference for `t>=0`:

\[
u(t)=\alpha e^{-\alpha t},
\]

\[
a(t)=\alpha^2 t e^{-\alpha t}.
\]

Integral check:

\[
\int_0^\infty a(t)dt=1.
\]

Required checks:

- state-space realization equals the kernel formula pointwise;
- `a(0)=0` and `a` is continuous through the event;
- `u` jumps by exactly `alpha`.

---

## B2 — periodic alpha-kernel orbit [exact]

Choose any positive `alpha,T`; canonical values:

- `alpha = 2`
- `T = pi`

Set

\[
r=e^{-\alpha T}.
\]

Immediately after a spike:

\[
u^+=\frac{\alpha}{1-r},
\qquad
a^+=\frac{\alpha^2Tr}{(1-r)^2}.
\]

For `0<=t<T`:

\[
u(t)=\frac{\alpha e^{-\alpha t}}{1-r},
\]

\[
a(t)=\alpha^2e^{-\alpha t}
\left[
\frac{t}{1-r}+\frac{Tr}{(1-r)^2}
\right].
\]

Required checks:

- flow from post-event state to `T^-`, followed by `u += alpha`, returns to the post-event state;
- `a(t)` equals the direct periodic comb sum;
- numerical integral over one period equals `1`.

Suggested relative tolerance: `<1e-10`.

---

## B3 — exact synchronous period in an unbalanced network [exact]

Take a matrix with constant row sum

\[
\Gamma=1.
\]

Use

- `gamma = pi`
- `Theta = -1`
- arbitrary `alpha > 0`
- arbitrary common `tau >= 0`

Then

\[
T=\frac{\gamma\Gamma-2\pi}{\Theta}=\pi.
\]

Required parameter sweep:

- at least three `alpha` values spanning two orders of magnitude;
- at least three common delays, including zero and a value larger than `T`.

Required checks:

- synchronous event period remains `pi`;
- period is invariant to `alpha` and common `tau` in the linear model;
- the generated waveform may change, but its integral over a cycle remains one.

This benchmark catches accidental dependence of the linear period on timestep, delay-buffer representation, or kernel discretisation.

---

## B4 — balanced synchronous network [exact]

Choose any row-balanced matrix

\[
W\mathbf1=0.
\]

Canonical 2-cell example:

\[
W=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

Use

- `Theta=-1`
- any `gamma`
- any `alpha`
- common `tau`

Then on the synchronous orbit

\[
\psi_i(t)=0,
\qquad
\dot\theta_i=1,
\qquad
T=2\pi.
\]

Required checks:

- period exactly `2*pi` within solver tolerance;
- synchronous input cancels numerically;
- changing `alpha`, `gamma`, or common delay does not change the synchronous period.

---

## B5 — two-cell mode decomposition [exact algebra]

Use

\[
W=\begin{pmatrix}w_s&w_c\\w_c&w_s\end{pmatrix}.
\]

Reference eigenpairs:

\[
v_+=(1,1)^T,\qquad \widehat w_+=w_s+w_c,
\]

\[
v_-=(1,-1)^T,\qquad \widehat w_-=w_s-w_c.
\]

Required checks:

- numerical eigenvalues match these values;
- the synchronous mode is parallel to the all-ones vector;
- relative phase perturbations project onto `v_-`.

Canonical cross-coupled case:

\[
W=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

so

\[
\widehat w_+=1,\qquad \widehat w_-=-1.
\]

---

## B6 — closed-form modal flow matrix [exact]

For a network eigenmode `w_hat` define

\[
\beta=\gamma\widehat w,
\qquad r=e^{-\alpha T}.
\]

Reference:

\[
E_\beta(T)=
\begin{pmatrix}
1 & \dfrac{\beta(1-r)}{\alpha} &
\dfrac{\beta[1-r(1+\alpha T)]}{\alpha}\\
0&r&\alpha T r\\
0&0&r
\end{pmatrix}.
\]

Required checks:

- compare against the implementation's matrix exponential of `A + beta*DF`;
- use random positive `alpha,T` and positive/negative/zero `beta`;
- maximum absolute element error `<1e-11` in float64.

This test does not require simulation.

---

## B7 — saltation matrix [exact]

Reference:

\[
K(T)=
\begin{pmatrix}
1&0&0\\
\alpha^2/\dot\theta(T)&1&0\\
-\alpha^2/\dot\theta(T)&0&1
\end{pmatrix}.
\]

Required checks:

1. construct `K` from the generic saltation formula;
2. construct `K` from the closed form above;
3. require agreement `<1e-12` in float64.

The test must reject or explicitly flag the grazing case `dot_theta(T)=0` rather than divide silently.

---

## B8 — event-time sensitivity [first order]

Reference relation:

\[
\delta T=-\frac{\delta\theta(T)}{\dot\theta(T)}.
\]

Procedure:

- choose a transversal periodic orbit;
- perturb the state phase by small amplitudes `eps` of both signs;
- measure the next event-time displacement;
- verify first-order convergence to the reference formula as `eps -> 0`.

Acceptance criterion:

- log-log slope of the residual after subtracting the linear prediction should approach 2 for a smooth transversal event implementation.

---

## B9 — slow-synapse modal roots at zero delay [asymptotic]

This is **not** an exact finite-alpha benchmark. It verifies convergence to the slow-synapse reduction.

Reference equation:

\[
\left(1+\frac{\lambda}{\alpha T}\right)^2
=
\frac{\gamma\widehat w}{2\pi}
\]

for `tau=0`, so

\[
\lambda_\pm
=\alpha T
\left[-1\pm\sqrt{\frac{\gamma\widehat w}{2\pi}}\right].
\]

Canonical two-cell transverse mode:

- `W=[[0,1],[1,0]]`, hence `w_hat_minus=-1`;
- `gamma=pi`;
- `Theta=-1`, `Gamma=1`, hence `T=pi`;
- use a sequence `alpha*T/(2*pi) -> 0`.

Then

\[
\frac{\gamma\widehat w_-}{2\pi}=-\frac12,
\]

and

\[
\lambda_\pm
=\alpha T\left(-1\pm\frac{i}{\sqrt2}\right).
\]

Required check:

- roots from the full characteristic calculation converge to these asymptotic values as `alpha*T/(2*pi)` decreases.

Do not enforce a fixed absolute tolerance independent of `alpha`; test convergence rate/trend instead.

---

## B10 — delay-induced imaginary-axis algebra [exact consequence of reduced equation]

Let

\[
c=\frac{\gamma\widehat w}{2\pi},\quad
x=\frac{\omega}{\alpha T},\quad
y=\frac{\omega\tau}{T}.
\]

At an imaginary-axis root of the slow-synapse characteristic equation,

\[
1-x^2=c\cos y,
\qquad
2x=-c\sin y.
\]

Required checks:

- substitute any numerical root of the reduced complex equation and verify both real equations;
- verify `(1+x^2)^2=c^2`;
- explicitly use `c=gamma*w_hat/(2*pi)`.

This benchmark is intentionally written to guard against the normalization inconsistency in the displayed Eq. (29) of the current Coombes PDF.

---

# Test classes

The later codebase should label tests as one of:

- `exact_algebra`
- `exact_event`
- `exact_kernel`
- `exact_period`
- `cross_formulation`
- `asymptotic_limit`

A test derived from a slow-synapse approximation must never be reported as an exact full-model identity.

---

# Minimum CORE acceptance gate

Before large-network experiments are scientifically trusted, the implementation should pass at least:

`B0, B1, B2, B3, B4, B6, B7, B8`.

Before stability diagrams are trusted, additionally pass:

`B5, B9, B10`

and demonstrate agreement between event-map and flow/saltation spectra in a documented overlap case.
