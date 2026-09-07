# CORE generalized Neimark--Sacker / Chenciner benchmark v0.9

## Purpose

CORE v0.9 closes the smooth nonlinear codimension-two problem left open by v0.8.

The v0.8 audit showed that the NS cubic coefficient at the response-threshold contact is not a numerically robust normal-form benchmark. v0.9 therefore continues the same `q=1` NS locus to a region where the whole synchronous orbit remains uniformly above threshold and solves

\[
\ell_1=0
\]

on the NS locus. It then computes the fifth-order resonant coefficient and verifies the second Lyapunov coefficient `L2 != 0`.

The result is the first **smooth, nondegenerate generalized Neimark--Sacker / Chenciner point** in the Lighthouse CORE atlas.

Provenance:

- **[C]** standard center-manifold/normal-form theory for maps;
- **[P]** Lighthouse event-map construction, numerical continuation, coefficient normalization and benchmark values.

---

# 1. Ring family and NS locus

Use the same `N=3` circulant family as v0.8,

\[
w_d=[1,p,-p],
\qquad
\tau_d=[0,2,\tau_3],
\tag{V91}
\]

with

\[
S(x)=\exp[-1/(x+1)^2]H(x+1),
\qquad
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\qquad
\alpha=0.5.
\tag{V92}
\]

The synchronous input is

\[
\Psi(s)=R_T(s)+pR_T(s-2)-pR_T(s-\tau_3).
\tag{V93}
\]

The `q=1` NS locus is defined by

\[
F_{\rm sync}(T,p,\tau_3)=0,
\tag{V94}
\]

\[
E_1(e^{i\Omega};T,p,\tau_3)=0,
\qquad 0<\Omega<\pi.
\tag{V95}
\]

---

# 2. Fifth-order map normal form

On the gauge-fixed event/Poincare section, let the critical complex amplitude be `z`. After center-manifold reduction and nonresonant coordinate elimination, use

\[
\boxed{
 z_{n+1}
 =
 \mu z_n
 +c_1z_n^2\bar z_n
 +c_2z_n^3\bar z_n^2
 +O(|z|^6),
}
\tag{V96}
\]

where

\[
\mu=e^{i\Omega}.
\]

Define the phase-removed coefficients

\[
 b_1=e^{-i\Omega}c_1,
 \qquad
 b_2=e^{-i\Omega}c_2.
\tag{V97}
\]

The project first Lyapunov coefficient is

\[
\boxed{L_1=\Re b_1.}
\tag{V98}
\]

At a generalized NS point, `L1=0`. Under the standard Chenciner normalization, the second Lyapunov coefficient at unit modulus is

\[
\boxed{
L_2
=\frac12\left[(\Im b_1)^2+2\Re b_2\right].
}
\tag{V99}
\]

A nondegenerate Chenciner point requires, in addition to the simple unit-circle pair and parameter transversality,

\[
L_1=0,
\qquad
L_2\ne0,
\tag{V910}
\]

and exclusion of low-order strong resonances.

---

# 3. Smooth state-space event map

For the alpha synapse, v0.9 uses its exact finite-dimensional hybrid realization rather than differentiating the periodic `mod` representation.

For each postsynaptic node,

\[
\dot q=-\alpha q,
\qquad
\dot\psi=-\alpha\psi+q,
\tag{V911}
\]

and an arrival from edge `(i,j)` produces

\[
q^+=q^-+w_{ij}\alpha^2,
\qquad
\psi^+=\psi^-.
\tag{V912}
\]

Between arrivals,

\[
q(t+\Delta)=q(t)e^{-\alpha\Delta},
\tag{V913}
\]

\[
\psi(t+\Delta)
=e^{-\alpha\Delta}
\left[\psi(t)+q(t)\Delta\right].
\tag{V914}
\]

The phase gain on each smooth arrival interval is integrated with Gauss quadrature, the next spike is found by Newton iteration, and global time translation is removed after every cycle exactly as in v0.7.

This state-space formulation has two advantages for fifth-order work:

1. arrival times enter smoothly inside a fixed event itinerary;
2. no differentiation through `mod`, `floor`, or a shifted Heaviside kernel is required.

The fifth-order coefficients are obtained by automatic differentiation of this gauge-fixed map and recursive homological equations degree by degree. The calculation is separate from the characteristic-equation continuation used to locate the NS orbit.

---

# 4. Chenciner point

Solving the NS locus together with

\[
\boxed{L_1=0}
\tag{V915}
\]

gives

\[
\boxed{\tau_{3,*}=7.92140373739,}
\tag{V916}
\]

\[
\boxed{T_*=16.29213672114,}
\tag{V917}
\]

\[
\boxed{p_*=-3.26248414452,}
\tag{V918}
\]

\[
\boxed{\Omega_*=0.266095330801.}
\tag{V919}
\]

The critical multiplier is

\[
\boxed{
\mu_*
=0.964805044716+0.262966206367i,
\qquad |\mu_*|=1.
}
\tag{V920}
\]

The characteristic-equation residual is below `5e-16` in the 48-point reference calculation.

---

# 5. Uniform smoothness and admissibility margins

Unlike the v0.8 threshold-contact point, the v0.9 orbit is uniformly separated from the response threshold:

\[
\min_s\Psi(s)\approx-0.45167232,
\tag{V921}
\]

so

\[
\boxed{
\min_s(\Psi(s)+1)\approx0.54832768>0.
}
\tag{V922}
\]

The maximum input is approximately

\[
\max_s\Psi(s)\approx0.50082721.
\tag{V923}
\]

At the firing section,

\[
\boxed{\nu_*=S(\Psi(0))\approx0.43494412>0.}
\tag{V924}
\]

Thus the event is transverse and the full orbit remains inside one smooth response regime.

The arrival classes remain separated:

\[
0<2<\tau_{3,*}<T_*,
\]

with a minimum nominal arrival/cycle separation of `2`. No arrival collision participates in this codimension-two point.

---

# 6. Cubic degeneracy

In the physical Fourier-history normalization

\[
q_i^{(r)}
=\mu_*^{-r}e^{2\pi i i/3},
\tag{V925}
\]

and with the biorthogonal normalization

\[
p^*q=1,
\tag{V926}
\]

the phase-removed cubic coefficient is

\[
\boxed{
 b_1
 \approx
 -0.04254970545\,i,
}
\tag{V927}
\]

with

\[
\boxed{|\Re b_1|<5\times10^{-13}.}
\tag{V928}
\]

Hence

\[
\boxed{L_1=0}
\]

to numerical precision.

The `L=4` and `L=5` history calculations agree in `L1` to substantially better than `1e-12` at the stored critical point.

---

# 7. Fifth-order coefficient and second Lyapunov coefficient

The resonant fifth-order coefficient is

\[
\boxed{
 b_2
 \approx
 0.020640894614
 +0.003792391324\,i.
}
\tag{V929}
\]

Therefore

\[
L_2
=\frac12
\left[
(0.04254970545)^2
+2(0.020640894614)
\right],
\]

which gives

\[
\boxed{
L_2\approx0.021546133331>0.
}
\tag{V930}
\]

History convergence is exceptionally strong:

\[
L_2(L=4)=0.0215461333307,
\tag{V931}
\]

\[
L_2(L=5)=0.0215461333315.
\tag{V932}
\]

The difference is below `1e-12`.

A separate 32-versus-48-point Gauss audit at the same rounded critical point changes `L2` only at approximately the `1e-12` level. Thus the fifth-order coefficient is not showing the threshold-boundary sensitivity found in v0.8.

---

# 8. Parameter transversality

Two independent unfolding coordinates are required. Use

\[
\beta_1=|\mu|-1,
\qquad
\beta_2=L_1.
\tag{V933}
\]

At fixed `tau_3`, characteristic-root continuation gives

\[
\boxed{
\frac{\partial |\mu|}{\partial p}
\approx-0.18379443.
}
\tag{V934}
\]

Along the NS locus,

\[
\boxed{
\frac{dL_1}{d\tau_3}\Big|_{\rm NS}
\approx-0.0092975000.
}
\tag{V935}
\]

The NS-locus tangent itself is

\[
\boxed{
\frac{dp_{\rm NS}}{d\tau_3}
\approx-0.27482160.
}
\tag{V936}
\]

Using the fact that `beta_1=0` on the NS locus, the determinant of the local parameter transformation `(p,tau_3) -> (beta_1,beta_2)` can be evaluated as

\[
\det D(\beta_1,\beta_2)
=
\frac{\partial|\mu|}{\partial p}
\frac{dL_1}{d\tau_3}\Big|_{\rm NS},
\tag{V937}
\]

so

\[
\boxed{
\det D(\beta_1,\beta_2)
\approx1.70883\times10^{-3}\ne0.
}
\tag{V938}
\]

The two unfolding directions are therefore independent.

---

# 9. Strong-resonance audit

For `k=1,...,6`, compute

\[
d_k=|e^{ik\Omega_*}-1|.
\tag{V939}
\]

The smallest value is

\[
\boxed{
\min_{1\le k\le6}d_k
\approx0.26531.
}
\tag{V940}
\]

Thus the point is safely away from the low-order strong resonances excluded by the standard Chenciner normal form.

---

# 10. CORE classification

The v0.9 point satisfies all project requirements for a smooth nondegenerate generalized NS point:

1. a simple complex-conjugate unit-circle pair;
2. event transversality and a fixed smooth response/arrival itinerary;
3. no low-order strong resonance;
4. `L1=0`;
5. `L2 != 0`;
6. a nonsingular two-parameter unfolding map.

Therefore CORE classifies it as

\[
\boxed{
\text{nondegenerate Chenciner / generalized Neimark--Sacker point}.
}
\tag{V941}
\]

The synergetic order parameter remains the critical complex `q=1` spike-time Fourier amplitude. At v0.9 its cubic saturation vanishes, so quintic order becomes the leading nonlinear radial organizer.

---

# 11. Benchmark contract B105--B120

- **B105**: solve the `q=1` NS locus at `tau_3=tau_{3,*}` with characteristic residual `<1e-10`.
- **B106**: reproduce `(T_*,p_*,tau_3*,Omega_*)` within documented tolerances.
- **B107**: verify `||mu_*|-1|<1e-8`.
- **B108**: verify `min(Psi+1)>0.5`.
- **B109**: verify `nu_*>0.4`.
- **B110**: verify the fixed arrival ordering `0<2<tau_3<T`.
- **B111**: use physical Fourier-history normalization (V925) and `p^*q=1`.
- **B112**: recover `|L1|<1e-8` from the AD state-space event map.
- **B113**: recover `Im(b1) approx -0.04254970545`.
- **B114**: recover `Re(b2) approx 0.020640894614`.
- **B115**: recover `L2 approx 0.021546133331`.
- **B116**: require `|L2(L4)-L2(L5)|<1e-9`.
- **B117**: require a 32/48-point quadrature check for the fifth-order coefficient.
- **B118**: recover `dL1/dtau_3|NS approx -0.00929750`.
- **B119**: recover `partial_p |mu| approx -0.18379443` and a nonzero unfolding determinant.
- **B120**: verify `min_{k=1..6}|exp(i k Omega)-1|>0.2`.

---

# 12. Consequence for the research program

CORE now has two fundamentally different codimension-two benchmarks in the same Lighthouse ring family:

\[
\boxed{
\text{v0.8: smooth NS mode + structural threshold boundary}
}
\]

and

\[
\boxed{
\text{v0.9: smooth NS mode + vanishing cubic saturation}
}
\]

The second case is the direct synergetic scenario: the same complex order parameter remains critical, but the cubic amplitude equation loses its organizing power and the quintic term becomes leading.

The next CORE step should unfold the invariant-circle branches around the Chenciner point and then couple the verified fast amplitude dynamics to slowly adaptive conduction delays. Arrival-collision loci should be retained as separate hybrid boundaries rather than folded into the smooth Chenciner normal form.

## References

The coefficient convention follows standard map normal-form theory for generalized Neimark--Sacker/Chenciner bifurcations, in particular the fifth-order Poincare normal form and nondegeneracy conditions described by Kuznetsov and subsequent Chenciner analyses.