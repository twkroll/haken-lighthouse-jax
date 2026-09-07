# CORE numerical bifurcation atlas v0.6

## Purpose

CORE v0.6 is the first version whose primary output is numerical rather than structural. It turns the v0.1--v0.5 theory into reproducible reference points for independent implementations.

The goals are:

1. attach concrete numbers to exact Lighthouse formulas;
2. expose convention/gauge errors before they enter JAX code;
3. provide a nonlinear two-cell pitchfork with an explicit order-parameter reduction;
4. distinguish quantities computed directly from the event/spike-time problem from quantities inferred by local normal-form matching.

All numbers below use double precision and arrival-aware quadrature. They are intended as reference values with documented tolerances, not as claims of arbitrary-precision constants.

---

# 1. Erratum to v0.3: sign of the two-cell symmetry-breaking coefficient

In `continuation_bifurcations_v0.3.md` the convention is

\[
F_- = \frac{F_1-F_2}{2},\qquad \chi=\chi_2-\chi_1,
\]

with

\[
\Psi_1(\sigma)=w_sR_T(T\sigma-\tau_s)
+w_cR_T(T(\sigma-\chi)-\tau_c),
\]

\[
\Psi_2(\sigma)=w_cR_T(T(\sigma+\chi)-\tau_c)
+w_sR_T(T\sigma-\tau_s).
\]

Differentiating at `chi=0` gives

\[
\partial_\chi F_1
=+T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma,
\]

\[
\partial_\chi F_2
=-T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma.
\]

Therefore the correct coefficient is

\[
\boxed{
B=\partial_\chi F_-(T,0)
=+T^2w_c\int_0^1S'(\Psi_0)R_T'(T\sigma-\tau_c)d\sigma.
}
\tag{V6.1}
\]

The minus sign printed in v0.3 Eq. (C45) is a project erratum. The generic formulas (C46)--(C53) are unchanged; only the explicit evaluation of `B` and derivatives taken from that explicit formula must use (V6.1).

This correction is benchmark B59.

---

# 2. Exact linear reference: Coombes Fig. 3 parameter set

The 2025/2026 revisit uses the globally coupled matrix

\[
w_{ij}=(\Gamma+1)\delta_{ij}-N^{-1}
\]

with

\[
\Gamma=1,\qquad \gamma=\pi,\qquad \Theta=-1,\qquad \tau=0.
\]

The synchronous eigenvalue is `Gamma=1`; every transverse vector with zero node sum has

\[
\widehat w_\perp=\Gamma+1=2.
\]

For the linear response

\[
S_L(x)=\gamma x-\Theta
\]

the period is exactly

\[
\boxed{T=\pi.}
\tag{V6.2}
\]

## 2.1 Exact transverse characteristic polynomial

For an alpha synapse

\[
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\qquad r=e^{-\alpha T},
\]

the zero-delay synchronous spike-time characteristic equation factors as

\[
(\mu-1)\left[
\nu-\gamma\widehat w_\perp
\sum_{k\ge1}\eta(kT)\mu^{-k}
\right]=0,
\]

where

\[
\nu=\dot\theta(T)
=\gamma\Gamma P(0)-\Theta,
\]

and

\[
P(0)=\frac{\alpha^2Tr}{(1-r)^2}.
\]

Using

\[
\sum_{k\ge1}kz^k=\frac{z}{(1-z)^2},
\]

the two non-gauge multipliers are the roots of the exact quadratic

\[
\boxed{
\nu(\mu-r)^2
-\gamma\widehat w_\perp\alpha^2Tr\,\mu=0.
}
\tag{V6.3}
\]

The additional factor `mu-1` is the unwrapped-phase/gauge direction discussed in v0.4. The same factor appears in the raw 3 x 3 saltation monodromy matrix. Therefore an MSF implementation must remove the physical/gauge unit direction by a documented rule; taking the largest raw eigenvalue without gauge handling gives a zero exponent identically.

## 2.2 Numerical values

For `alpha=2`:

\[
r=1.867442731707989\times10^{-3},
\]

\[
P(0)=2.355487006563863\times10^{-2},
\]

\[
\nu=1.073999806754473,
\]

and

\[
\boxed{
\mu_1=1.409982290992954\times10^{-1},\qquad
\mu_2=2.473323515115286\times10^{-5}.
}
\tag{V6.4}
\]

For `alpha=5`:

\[
r=1.507017275390065\times10^{-7},
\]

\[
P(0)=1.183608957043386\times10^{-5},
\]

\[
\nu=1.000037184172042,
\]

and

\[
\boxed{
\mu_1=7.466665573660435\times10^{-5},\qquad
\mu_2=3.041653661757237\times10^{-10}.
}
\tag{V6.5}
\]

Thus the local transverse spike-time multipliers in this linear, zero-delay calculation are inside the unit circle at both values, and much more strongly damped at `alpha=5`.

### Interpretation rule

This does **not** prove that oscillator-death trajectories reported for the same nominal parameter list are impossible. It does show that such a trajectory cannot be labelled a local transverse instability of the synchronous orbit under the exact conventions leading to (V6.3) without an additional explanation (different response convention, basin/global mechanism, reset rule, initialisation, or another modelling detail).

This is intentionally retained as a reproduction question rather than silently tuned away.

---

# 3. Nonlinear two-cell benchmark with a generic symmetry-breaking point

The first nonlinear v0.6 benchmark uses the full smooth-above-threshold Lighthouse response

\[
\boxed{
S(x)=\exp\left[-\frac{1}{(x+1)^2}\right]H(x+1),
}
\tag{V6.6}
\]

and alpha synapses with

\[
\boxed{\alpha=0.5.}
\tag{V6.7}
\]

Use the exchange-symmetric two-cell network

\[
W=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

with

\[
\tau_s=0,
\qquad p\equiv\tau_c
\]

as the continuation parameter. The synchronous input is

\[
\Psi_0(s)=R_T(s)+R_T(s-p).
\]

Both inputs are positive for the critical orbit below, so the threshold at `x=-1` is separated by a large margin and the smooth normal-form calculation is legitimate.

## 3.1 Critical synchronous orbit

Solve simultaneously

\[
F_+(T,0,p)=0,
\qquad
B(T,p)=\partial_\chi F_-(T,0,p)=0.
\]

The first positive nontrivial solution found from the half-period sector is

\[
\boxed{
T_*=13.43069020,
\qquad
p_*=\tau_{c,*}=6.71534510=\frac{T_*}{2}.
}
\tag{V6.8}
\]

More digits should not be treated as certified until an arbitrary-precision reference is added.

On this orbit the periodic input satisfies approximately

\[
0.062744\lesssim\Psi_0(s)\lesssim0.215113,
\]

and hence

\[
0.412547\lesssim\dot\theta(s)\lesssim0.507998.
\]

The spike-section velocity is

\[
\boxed{\nu_*\approx0.41254621>0,}
\tag{V6.9}
\]

so the event is safely transversal.

---

# 4. Existence normal form at the two-cell critical point

With `p=tau_c` and all derivatives evaluated at `(T_*,chi=0,p_*)`, arrival-aware finite differences and direct integral formulas give

\[
F_{+,T}\approx-0.3745575465,
\tag{V6.10}
\]

\[
F_{+,p}=0
\quad\text{(half-period symmetry)},
\tag{V6.11}
\]

\[
F_{+,\chi\chi}\approx0.73964113,
\tag{V6.12}
\]

\[
F_{-,\chi p}\approx+0.05507097235,
\tag{V6.13}
\]

\[
F_{-,\chi T}\approx-0.02753548616.
\tag{V6.14}
\]

At fixed `(T_*,p_*)`, `F_-(chi)` vanishes to numerical precision through the directly sampled cubic term because of the additional half-period interchange symmetry. The generic cubic term of the reduced problem is generated after slaving the period through `F_+=0`.

The period correction is

\[
T=T_s(p)+c_T\chi^2+O(\chi^4),
\]

with

\[
\boxed{
c_T=-\frac{F_{+,\chi\chi}}{2F_{+,T}}
\approx0.98735313.
}
\tag{V6.15}
\]

The v0.3 Lyapunov--Schmidt coefficients are therefore

\[
\boxed{a\approx0.05507097235,}
\tag{V6.16}
\]

\[
\boxed{b\approx-0.02718724838.}
\tag{V6.17}
\]

The nontrivial phase-locked branches satisfy

\[
\boxed{
\chi^2
\sim
-\frac{a}{b}(p-p_*)
\approx2.02561773\,(p-p_*).
}
\tag{V6.18}
\]

Combining (V6.15) and (V6.18),

\[
\boxed{
T-T_*\sim2.00000000\,(p-p_*).
}
\tag{V6.19}
\]

The factor `2` is a useful high-sensitivity cross-check because it results from cancellation between independently computed derivatives.

## 4.1 Direct branch checks

For

\[
p-p_*=10^{-4},
\]

the leading-order prediction is

\[
|\chi|\approx0.01423241.
\]

Direct solution of `(F_+,F_-)=0` gives approximately

\[
\boxed{
T=13.43089020,
\qquad |\chi|=0.01423174.
}
\tag{V6.20}
\]

For

\[
p-p_*=10^{-2},
\]

the leading prediction is `|chi|=0.1423241`, while direct continuation gives

\[
\boxed{
T=13.45069020,
\qquad |\chi|=0.1417599.
}
\tag{V6.21}
\]

The square-root law is therefore already quantitatively useful one hundredth of a time unit from the critical delay.

---

# 5. Dynamic unit multiplier and equality with the existence critical point

For the exchange-symmetric synchronous state, write the two scalar v0.4 characteristic sectors as

\[
E_+(\mu)=\nu(\mu-1)-h_s(\mu)-h_c(\mu),
\]

\[
E_-(\mu)=\nu(\mu-1)-h_s(\mu)+h_c(\mu).
\]

At `mu=1`, periodicity implies

\[
h_s(1)+h_c(1)=0.
\]

Using the corrected sign convention (V6.1),

\[
B=T\,h_c(1),
\]

so

\[
\boxed{
E_-(1)=\frac{2B}{T}.
}
\tag{V6.22}
\]

Therefore, for this two-cell symmetry class,

\[
\boxed{B=0\quad\Longleftrightarrow\quad E_-(1)=0.}
\tag{V6.23}
\]

This is not a generic identity between all existence and stability singularities. It is a symmetry-specific identity at the synchronous two-cell branch and is exactly the kind of cross-layer relation CORE should exploit as a benchmark.

At the v0.6 critical point,

\[
\partial_\mu E_-(1)\approx0.445594394.
\tag{V6.24}
\]

Since along the synchronous branch `T_s'(p_*)=0`, Eq. (V6.22) gives

\[
\partial_pE_-(1)
=\frac{2a}{T_*}
\approx8.20080\times10^{-3}.
\tag{V6.25}
\]

The critical multiplier therefore crosses according to

\[
\boxed{
\mu_-(p)
=1+\sigma(p-p_*)+\cdots,
\qquad
\sigma\approx-0.01840410.
}
\tag{V6.26}
\]

Direct nonlinear-eigenvalue solves at `p-p_*=+-0.01` give slopes consistent with `-1.84e-2`.

---

# 6. Order-parameter cubic coefficient in the chi normalisation

Use the normalised relative firing offset itself as the local scalar order-parameter coordinate,

\[
A\equiv\chi.
\]

The dynamic pitchfork map is written

\[
A_{n+1}-A_n
=\sigma\varepsilon A_n+c_\chi A_n^3+\cdots,
\qquad
\varepsilon=p-p_*.
\tag{V6.27}
\]

The fixed-point branch of this map obeys

\[
A^2\sim-\frac{\sigma}{c_\chi}\varepsilon.
\]

Matching the independently computed multiplier slope (V6.26) to the independently continued branch scaling (V6.18) gives

\[
\boxed{
c_\chi\approx9.08568\times10^{-3}.}
\tag{V6.28}
\]

This coefficient is **coordinate dependent**: it belongs specifically to the `A=chi` normalisation. It must not be compared numerically with a biorthogonally normalised coefficient `p^*q=1` until the amplitude-coordinate conversion is applied.

Because

\[
\sigma<0,
\qquad c_\chi>0,
\]

the small symmetry-broken branches exist for

\[
p>p_*,
\]

where the synchronous critical multiplier has moved inside the unit circle. The reduced center multiplier on the broken branches is

\[
1-2\sigma\varepsilon>1
\]

for small positive `epsilon`. Thus the local pitchfork is

\[
\boxed{\text{subcritical in the dynamic center direction}.}
\tag{V6.29}
\]

A direct third-order derivative of the full gauge-fixed event return map remains a v0.6/v0.7 cross-validation task. Equation (V6.28) is a constrained extraction from two independent observables: branch geometry and multiplier slope.

---

# 7. Benchmark contract B59--B72

## B59 — v0.3 sign erratum

Using the project definitions of `F_-` and `chi`, numerical differentiation of `F_-` must agree with the **positive-sign** formula (V6.1).

## B60 — exact Fig. 3 period

For `Gamma=1`, `gamma=pi`, `Theta=-1`, recover `T=pi` to machine precision.

## B61 — exact alpha periodic state

For the same linear benchmark, recover `P(0)=alpha^2*T*r/(1-r)^2` independently from the hybrid `(a,u)` orbit.

## B62 — linear transverse multipliers, alpha=2

Recover (V6.4) from both the quadratic spike-time equation and the non-gauge eigenvalues of the 3 x 3 flow-plus-saltation matrix.

## B63 — linear transverse multipliers, alpha=5

Recover (V6.5) by the same two routes.

## B64 — gauge unit multiplier

Verify that the raw unwrapped 3 x 3 monodromy has an exact/near-exact unit eigenvalue and that the stability API does not report it as a transverse instability or as the leading nontrivial multiplier.

## B65 — nonlinear critical point

For (V6.6)--(V6.7), recover `(T_*,p_*)` in (V6.8) with absolute errors below `2e-6`.

## B66 — transversality

Verify `nu_*>0.412` and minimum input `Psi_0>-0.9`, comfortably away from both grazing and the threshold `h=-1`.

## B67 — existence derivatives

Recover (V6.10)--(V6.14) within `5e-5` using a derivative route independent of the one used to locate the critical point.

## B68 — branch scaling

For `p-p_*=1e-4`, recover the nontrivial branch with `|chi|-0.01423174` within `2e-5`.

## B69 — existence/dynamic identity

Check numerically that

\[
E_-(1)-2B/T=0
\]

within quadrature tolerance along several synchronous branch points near `p_*`.

## B70 — multiplier slope

Recover `d mu_-/dp approximately -0.0184041` either by implicit differentiation of `E_-` or by symmetric root continuation.

## B71 — cubic coefficient in chi normalisation

Using independently measured branch slope and multiplier slope, recover

\[
c_\chi\approx0.00908568.
\]

## B72 — classification

The implementation must label the local branch as: nontrivial `+1` crossing, antisymmetric/exchange sector, smooth/transversal, broken branches on `p>p_*`, synchronous branch linearly stabilised in the critical direction for increasing `p`, broken branches center-unstable to leading order, hence subcritical.

---

# 8. What v0.6 establishes

CORE now contains a complete chain for one nonlinear critical point:

\[
\boxed{
\text{model parameters}
\to
\text{locked orbit}
\to
\text{existence singularity}
\to
\text{dynamic unit multiplier}
\to
\text{critical order parameter}
\to
\text{cubic branch classification}.
}
\]

This is the minimum standard future JAX bifurcation calculations should meet.

The next numerical theory targets are deliberately narrower than another general theory layer:

1. direct event-return extraction of `c_chi` and conversion to the `p^*q=1` v0.5 convention;
2. one genuine flip point with a continued period-two spike pattern;
3. one genuine Neimark--Sacker point with `ell_1` computed by two independent routes;
4. a small ring in which a specific Fourier sector `q` is the first unstable mode and the v0.5 cyclic selection rule predicts the nonlinear branch symmetry;
5. a frozen-delay/adaptive-delay example in which the slow dynamics crosses one of these measured fast bifurcations.
