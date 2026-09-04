# CORE codimension-two atlas v0.8

## Purpose

CORE v0.8 continues the verified v0.7 nonlinear bifurcation benchmarks in two parameters and adds the first codimension-two point.

The main result is a **hybrid codimension-two intersection** between

1. a smooth Neimark--Sacker (NS) locus of the synchronous `N=3` Lighthouse ring, and
2. a tangential response-threshold contact locus.

The calculation deliberately distinguishes this from a smooth two-eigenmode codimension-two bifurcation: only one Floquet pair is critical. The second codimension comes from a hybrid/structural boundary of the orbit.

The response and synapse are unchanged from v0.7:

\[
S(x)=\exp[-1/(x+1)^2]H(x+1),
\qquad
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\qquad \alpha=0.5.
\]

For this particular `S`, the threshold extension by zero is infinitely flat at `x=-1`; therefore the threshold contact is not a classical derivative discontinuity. It is nevertheless a structural activity-set boundary and remains a first-class CORE diagnostic.

---

# 1. Two-parameter ring family

Use a three-node circulant ring with displacement weights

\[
\boxed{w_d=[1,p,-p]}
\tag{V81}
\]

and delays

\[
\boxed{\tau_d=[0,2,\tau_3].}
\tag{V82}
\]

The row sum is exactly one for all `(p,tau_3)`.

For the synchronous orbit define

\[
\Psi(s;T,p,\tau_3)
=
R_T(s)+pR_T(s-2)-pR_T(s-\tau_3).
\tag{V83}
\]

Existence requires

\[
\boxed{
F_{\rm sync}(T,p,\tau_3)
=2\pi-\int_0^T S(\Psi(s))ds=0.
}
\tag{V84}
\]

The `q=1` Fourier characteristic equation is

\[
E_1(\mu;T,p,\tau_3)=0.
\tag{V85}
\]

An NS point satisfies

\[
\mu=e^{i\Omega},
\qquad 0<\Omega<\pi,
\tag{V86}
\]

and

\[
\boxed{
F_{\rm sync}=0,
\quad
\Re E_1(e^{i\Omega})=0,
\quad
\Im E_1(e^{i\Omega})=0.
}
\tag{V87}
\]

---

# 2. Threshold-contact locus

The active response threshold is

\[
\Psi=-1.
\]

A tangential contact at phase `s_*` satisfies

\[
\boxed{
\Psi(s_*)=-1,
\qquad
\partial_s\Psi(s_*)=0.
}
\tag{V88}
\]

To select a genuine local minimum require

\[
\boxed{
\partial_s^2\Psi(s_*)>0.
}
\tag{V89}
\]

The threshold-contact locus in `(p,tau_3)` is obtained from

\[
F_{\rm sync}=0,
\qquad
\Psi(s_*)+1=0,
\qquad
\partial_s\Psi(s_*)=0.
\tag{V810}
\]

---

# 3. First codimension-two point

Solve the five equations

\[
F_{\rm sync}=0,
\]

\[
\Re E_1(e^{i\Omega})=0,
\qquad
\Im E_1(e^{i\Omega})=0,
\]

\[
\Psi(s_*)+1=0,
\qquad
\partial_s\Psi(s_*)=0
\tag{V811}
\]

for `(T,p,Omega,tau_3,s_*)`.

The reference solution is

\[
\boxed{T_*=17.69540826,}
\tag{V812}
\]

\[
\boxed{p_*=-7.21591135,}
\tag{V813}
\]

\[
\boxed{\tau_{3,*}=13.14117538,}
\tag{V814}
\]

\[
\boxed{\Omega_*=0.46104577,}
\tag{V815}
\]

\[
\boxed{s_*=4.38076296.}
\tag{V816}
\]

The simultaneous residual norm is approximately

\[
1.2\times10^{-13}.
\tag{V817}
\]

The critical multiplier is

\[
\boxed{
\mu_*=e^{i\Omega_*}
\approx
0.8955877392+0.4448849305i.
}
\tag{V818}
\]

At the threshold contact,

\[
\Psi(s_*)+1\approx0,
\qquad
\Psi'(s_*)\approx0,
\]

and symmetric finite differences give

\[
\boxed{\Psi''(s_*)\approx0.25>0.}
\tag{V819}
\]

Thus the threshold contact is an isolated tangential minimum rather than an extended plateau.

The firing-section input is

\[
\Psi(0)\approx0.832930173,
\]

hence

\[
\boxed{\nu_*=S(\Psi(0))\approx0.742560034>0.}
\tag{V820}
\]

so spike-event transversality is still regular at the codimension-two point.

---

# 4. Transversality of the two critical loci

Continue each locus locally with `tau_3` as parameter.

For the NS curve,

\[
\boxed{
\left.\frac{dp_{\rm NS}}{d\tau_3}\right|_*
\approx-2.26337357.
}
\tag{V821}
\]

For the threshold-contact curve,

\[
\boxed{
\left.\frac{dp_{\rm TH}}{d\tau_3}\right|_*
\approx-0.29189680.
}
\tag{V822}
\]

Their slope difference is

\[
\boxed{-1.97147677\ne0,}
\tag{V823}
\]

and the acute angle between the parameter-plane tangents is approximately

\[
\boxed{49.89^\circ.}
\tag{V824}
\]

Therefore the intersection is transverse and genuinely codimension two in the `(p,tau_3)` plane.

---

# 5. NS dynamics at the hybrid intersection

At fixed `tau_3=tau_{3,*}`, characteristic-root continuation in `p` gives

\[
\boxed{
\left.\frac{d|\mu|}{dp}\right|_*
\approx-0.01969526,
}
\tag{V825}
\]

and

\[
\boxed{
\left.\frac{d\arg\mu}{dp}\right|_*
\approx-0.07158686.
}
\tag{V826}
\]

Thus the NS pair crosses the unit circle transversely.

Using the same physical Fourier-history normalization as v0.7,

\[
q^{(r)}=\mu_*^{-r}
\begin{pmatrix}
1 & e^{2\pi i/3} & e^{4\pi i/3}
\end{pmatrix}^T,
\tag{V827}
\]

the gauge-fixed event-history map gives

\[
\boxed{\ell_1(L=4)\approx-14.50060663,}
\tag{V828}
\]

\[
\boxed{\ell_1(L=5)\approx-14.50060668.}
\tag{V829}
\]

The history-length discrepancy is about `5e-8`.

The sign change relative to the v0.7 NS benchmark (`ell_1>0` there) is scientifically important: the nonlinear character of the oscillatory timing instability changes somewhere along the NS locus between those benchmark locations. CORE does **not** infer a generalized-Hopf point from this sign change alone; locating `ell_1=0` is a separate v0.9 target.

Because

\[
\ell_1<0
\]

while `d|mu|/dp<0`, the local NS normal form at fixed `tau_3=tau_{3,*}` is supercritical under the v0.5/v0.7 coefficient convention.

---

# 6. Local codimension-two interpretation

Introduce parameter offsets

\[
\delta p=p-p_*,
\qquad
\delta\tau=\tau_3-\tau_{3,*}.
\]

A natural local description has two independent scalar unfolding coordinates:

1. an NS radial distance

\[
\lambda_{\rm NS}
=a_p\delta p+a_\tau\delta\tau+\cdots,
\]

2. a threshold-distance coordinate

\[
\lambda_{\rm TH}
=b_p\delta p+b_\tau\delta\tau+\cdots.
\]

The slope inequality (V823) implies these two linear forms are independent.

The critical complex timing amplitude `A` obeys locally

\[
A_{n+1}
=e^{i\Omega_*}
\left[
(1+\lambda_{\rm NS})A_n
+gA_n|A_n|^2+\cdots
\right].
\tag{V830}
\]

The threshold-contact surface is

\[
\lambda_{\rm TH}=0.
\tag{V831}
\]

Thus v0.8 supplies the first explicit Lighthouse example where a synergetic order parameter becomes critical exactly on a structural boundary of the microscopic pulse itinerary.

---

# 7. Negative result: no forced flip + unit codimension-two point

The v0.7 two-cell flip family was continued in `(tau_c,w_hat)` around the verified flip point. Along the regular branch segment examined, the antisymmetric unit diagnostic `E_-(1)` remains strictly positive and does not cross zero.

CORE therefore records **no verified flip+pitchfork codimension-two point** for that family. This negative result is intentional: codimension-two labels are not introduced from proximity or failed root searches.

---

# 8. Benchmark contract B91--B104

### B91 -- codimension-two residual
Solve (V811); require the full residual norm `< 1e-9`.

### B92 -- critical coordinates
Recover `(T_*,p_*,tau_3*,Omega_*,s_*)` within documented tolerances.

### B93 -- threshold value
Verify `|Psi(s_*)+1| < 1e-8`.

### B94 -- tangency
Verify `|Psi'(s_*)| < 1e-8`.

### B95 -- minimum curvature
Verify `Psi''(s_*) > 0` and approximately `0.25`.

### B96 -- event transversality
Verify `nu_* > 0.7`.

### B97 -- NS unit circle
Verify `||mu_*|-1| < 1e-7` in the characteristic calculation.

### B98 -- NS-locus slope
Recover `dp_NS/dtau_3 approx -2.26337357`.

### B99 -- threshold-locus slope
Recover `dp_TH/dtau_3 approx -0.29189680`.

### B100 -- codimension-two transversality
Verify the slope difference has magnitude `> 1`.

### B101 -- radial crossing
Recover `d|mu|/dp approx -0.01969526` at fixed `tau_3=tau_3*`.

### B102 -- event-map Lyapunov coefficient
Recover `ell1 approx -14.5006066` in the physical Fourier-history normalization.

### B103 -- history convergence
Require `|ell1(L=4)-ell1(L=5)| < 1e-5`.

### B104 -- negative flip/unit audit
Do not label a two-cell flip+unit codimension-two point unless `E_-(-1)=0` and a nontrivial `E_-(1)=0` are both solved at the same regular synchronous orbit.

---

# 9. v0.8 conclusions

CORE now contains one verified example of each of the following:

- unit-multiplier symmetry breaking;
- flip / period doubling;
- Neimark--Sacker instability;
- a nonlinear finite-ring timing mode;
- a hybrid codimension-two intersection.

The new organizing picture is

\[
\boxed{
\text{critical timing mode}
+\text{structural event boundary}
\Longrightarrow
\text{hybrid synergetic codimension-two dynamics}.
}
\]

The next mathematical target should not be another arbitrary special case. v0.9 should continue the NS cubic coefficient `ell_1` along the two-parameter NS locus and locate a genuine `ell_1=0` generalized-Hopf/Chenciner point if one exists, while separately continuing arrival-collision boundaries relevant to adaptive delays.
