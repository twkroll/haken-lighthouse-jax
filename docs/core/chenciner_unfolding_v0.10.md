# CORE local Chenciner unfolding v0.10

## Purpose

CORE v0.9 established a smooth nondegenerate generalized Neimark--Sacker / Chenciner point in the `N=3` Lighthouse ring. v0.10 converts that point into a local two-parameter phase diagram.

The goals are:

1. define canonical unfolding coordinates in terms of the physical parameters `(p,tau_3)`;
2. derive the Neimark--Sacker and fold-of-invariant-circles geometry from the quintic radial normal form;
3. classify the stability of the synchronous orbit and the small invariant circles;
4. state the correct numerical validation strategy for the exact event map.

The critical point from v0.9 is

\[
(T_*,p_*,\tau_*,\Omega_*)
=(16.29213672114,-3.26248414452,7.92140373739,0.266095330801),
\]

with

\[
L_2=0.021546133331>0.
\]

---

# 1. Canonical unfolding coordinates

Write

\[
\delta p=p-p_*,
\qquad
\delta\tau=\tau_3-\tau_*.
\]

Use

\[
\boxed{\beta_1=|\mu|-1}
\tag{U101}
\]

for radial linear stability and

\[
\boxed{\beta_2=L_1}
\tag{U102}
\]

for the cubic radial coefficient.

The certified v0.9 derivatives are

\[
\partial_p\beta_1\approx-0.18379443,
\tag{U103}
\]

\[
\left.\frac{dp_{\rm NS}}{d\tau_3}\right|_*
\approx-0.27482160,
\tag{U104}
\]

and

\[
\left.\frac{d\beta_2}{d\tau_3}\right|_{\rm NS}
\approx-0.0092975000.
\tag{U105}
\]

Since `beta_1=0` identically on the NS locus,

\[
\partial_\tau\beta_1
=-\partial_p\beta_1\frac{dp_{\rm NS}}{d\tau_3}
\approx-0.0505106793.
\tag{U106}
\]

A separate exact-event finite-difference audit at fixed `tau_3` gives

\[
\partial_p\beta_2
\approx0.08625,
\tag{U107}
\]

with a spread of order `1e-4` under the tested finite-difference steps. Therefore

\[
\partial_\tau\beta_2
=
\left.\frac{d\beta_2}{d\tau_3}\right|_{\rm NS}
-\partial_p\beta_2\frac{dp_{\rm NS}}{d\tau_3}
\approx0.014405863.
\tag{U108}
\]

Thus the first local physical-to-normal-form map is

\[
\boxed{
\begin{pmatrix}\beta_1\\\beta_2\end{pmatrix}
\approx
\begin{pmatrix}
-0.18379443 & -0.0505106793\\
 0.08625 & 0.014405863
\end{pmatrix}
\begin{pmatrix}\delta p\\\delta\tau\end{pmatrix}.
}
\tag{U109}
\]

Its determinant is

\[
\boxed{\det\approx1.70883\times10^{-3}\ne0,}
\tag{U110}
\]

consistent with the invariant v0.9 transversality test.

The first row and the derivative along the NS locus are certified. The separate entries in the second row are presently reference finite-difference estimates and should later be replaced by automatic differentiation of the full parameterized state-space return map.

---

# 2. Quintic radial normal form

After removing the carrier phase, let `r=|z|`. To the leading order needed for Chenciner geometry,

\[
\boxed{
r_{n+1}-r_n
=r_n\left(\beta_1+\beta_2r_n^2+L_2r_n^4\right)+\cdots .
}
\tag{U111}
\]

With

\[
u=r^2\ge0,
\]

nonzero invariant-circle amplitudes satisfy

\[
\boxed{
L_2u^2+\beta_2u+\beta_1=0.
}
\tag{U112}
\]

Hence

\[
\boxed{
u_{\pm}
=\frac{-\beta_2\pm\sqrt{\beta_2^2-4L_2\beta_1}}{2L_2}.
}
\tag{U113}
\]

Only positive real roots correspond to physical small invariant circles.

---

# 3. Critical curves

## 3.1 Neimark--Sacker curve

The NS curve is

\[
\boxed{\beta_1=0.}
\tag{U114}
\]

In physical coordinates its tangent is

\[
\boxed{
\delta p
=-0.27482160\,\delta\tau+O(\|\delta\|^2).
}
\tag{U115}
\]

Along this curve

\[
\beta_2
\approx-0.0092975000\,\delta\tau.
\tag{U116}
\]

Therefore:

- `delta_tau<0` gives `beta_2>0`: locally subcritical NS;
- `delta_tau>0` gives `beta_2<0`: locally supercritical NS.

The Chenciner point is exactly the transition between the two.

## 3.2 Fold of invariant circles

A double nonzero root of (U112) requires

\[
\boxed{
\beta_2^2-4L_2\beta_1=0,
\qquad
\beta_2<0.
}
\tag{U117}
\]

Thus the fold-of-invariant-circles (FIC) curve is

\[
\boxed{
\beta_1=\frac{\beta_2^2}{4L_2},
\qquad \beta_2<0.
}
\tag{U118}
\]

At the fold,

\[
\boxed{
r_{\rm FIC}^2=-\frac{\beta_2}{2L_2}.}
\tag{U119}
\]

The FIC curve is tangent to the NS curve at the Chenciner point in unfolding coordinates.

If only the linear physical-to-unfolding map (U109) is retained, the physical-plane approximation is

\[
\delta p
\approx
-0.27482160\,\delta\tau
-0.00545721\,\delta\tau^2.
\tag{U120}
\]

The quadratic coefficient in (U120) is **not yet an invariant physical curvature coefficient**: second derivatives of the parameter transformation also contribute at the same order. Equation (U120) is therefore an initialization formula for numerical FIC continuation, not a final measured curve.

---

# 4. Stability sectors for L2 > 0

For the radial map (U111), the synchronous state has radial multiplier larger than one when `beta_1>0` and smaller than one when `beta_1<0`.

For a nonzero root `u`, the leading radial stability sign is controlled by

\[
\beta_2+2L_2u.
\tag{U121}
\]

Consequently:

### Region A: `beta_2>0`, `beta_1<0`

- synchronous orbit stable;
- one positive invariant circle exists;
- that circle is radially unstable;
- this is the subcritical NS side.

### Region B: `beta_2>0`, `beta_1>0`

- synchronous orbit unstable;
- no small invariant circle from the quintic normal form.

### Region C: `beta_2<0`, `beta_1<0`

- synchronous orbit stable;
- one positive outer invariant circle exists;
- the outer circle is radially unstable.

### Region D: `beta_2<0`, `0<beta_1<beta_2^2/(4L_2)`

- synchronous orbit unstable;
- two positive invariant circles exist;
- the smaller circle is radially stable;
- the larger circle is radially unstable.

This is the characteristic Chenciner two-circle wedge.

### Region E: `beta_2<0`, `beta_1=beta_2^2/(4L_2)`

- the two invariant circles coalesce in a fold;
- the radial derivative is neutral to leading order.

### Region F: `beta_2<0`, `beta_1>beta_2^2/(4L_2)`

- synchronous orbit unstable;
- no small invariant circle remains in the local normal form.

---

# 5. Example local amplitudes

For illustration, take

\[
\beta_2=-5\times10^{-4},
\qquad
\beta_1=10^{-6}.
\]

Then

\[
\beta_2^2-4L_2\beta_1>0
\]

and (U113) predicts

\[
\boxed{r_-\approx0.0470,\qquad r_+\approx0.1449.}
\tag{U122}
\]

The inner branch is stable and the outer branch unstable in the reduced radial dynamics.

These amplitudes are coordinates in the v0.9 physical Fourier-history normalization; they are not raw Euclidean norms of the full history vector.

---

# 6. Why brute-force time stepping is not a reference method

A direct exact-event test inside the two-circle wedge showed the main numerical difficulty: sufficiently close to Chenciner the radial linear growth/decay is only of order `1e-5` per cycle, while stable history components decay much faster.

Therefore an initial condition can show a large transient decrease in a naive state norm even when the critical radial multiplier is slightly outside the unit circle. Tens or hundreds of cycles are insufficient to identify the final invariant circle reliably.

CORE therefore adopts the rule:

\[
\boxed{
\text{near Chenciner: do not certify invariant circles from transient simulation alone.}
}
\tag{U123}
\]

The reference computation must use an invariant-object solver.

---

# 7. Exact-event invariant-circle formulation

Let `P_p` be the gauge-fixed Lighthouse event-history map. Seek a parameterization

\[
K:\mathbb T\to\Sigma
\]

and rotation number `omega` satisfying

\[
\boxed{
P_p(K(\varphi))=K(\varphi+\omega).
}
\tag{U124}
\]

Represent

\[
K(\varphi)=\sum_{|k|\le M}K_ke^{ik\varphi}
\tag{U125}
\]

and solve the collocation residual together with a phase condition. The first initialization is supplied by the critical Fourier-history eigenvector and the normal-form radius from (U113).

For a fold of invariant circles, augment (U124) with a neutral radial eigenfunction / singular-Jacobian condition and continue in `(p,tau_3)` by pseudo-arclength.

This solver, rather than long-time simulation, is the next numerical implementation target.

---

# 8. Benchmark contract B121--B134

- **B121** reproduce the matrix (U109) within the stated certified/estimated tolerances.
- **B122** recover a nonzero determinant above `1e-3`.
- **B123** verify the NS tangent (U115).
- **B124** verify `d beta_2/d tau|NS < 0`.
- **B125** verify the Chenciner radial equation (U112) with `L2>0`.
- **B126** recover the FIC discriminant condition (U117).
- **B127** verify two positive roots in Region D.
- **B128** verify the smaller Region-D root has negative radial restoring coefficient.
- **B129** verify the larger Region-D root has positive radial restoring coefficient.
- **B130** recover the example radii (U122) to `1e-3`.
- **B131** use (U120) only as an initializer, not as certified physical FIC curvature.
- **B132** invariant-circle certification must solve (U124), not infer a torus from finite transient duration.
- **B133** collocation amplitudes must be reported in the v0.9 physical Fourier-history normalization.
- **B134** compare exact-event collocation against the quintic prediction as the distance to Chenciner tends to zero.

---

# 9. CORE conclusion

v0.10 turns the isolated Chenciner point into a local organization principle:

\[
\boxed{
\text{subcritical NS}
\longleftrightarrow
\text{Chenciner}
\longleftrightarrow
\text{supercritical NS + two-circle wedge + FIC}.
}
\]

The Lighthouse order parameter is still the same complex `q=1` spike-time Fourier amplitude. What changes across the Chenciner point is the nonlinear radial organization of that order parameter.

The next implementation target is an exact-event Fourier-collocation solver for (U124). Once that is verified, the fast Chenciner normal form can be coupled to the slow adaptive-delay dynamics without relying on ambiguous transient simulations.
