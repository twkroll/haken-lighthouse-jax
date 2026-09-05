# CORE continuation and bifurcations v0.3

## Purpose

This document extends the v0.2 phase-locked self-consistency equations into a continuation and bifurcation framework. The central goal is to separate three mathematically distinct objects:

1. **existence singularities** of the phase-locked branch equations;
2. **dynamical stability changes** of the event/spike-time dynamics;
3. **hybrid singularities** where event transversality or event ordering fails.

These classes must not be conflated in analysis or code.

Provenance tags follow the project convention:

- **[H]** historical Haken structure/result;
- **[C]** contemporary Lighthouse reconstruction/extensions, especially Coombes et al.;
- **[P]** project derivation/canonicalisation.

The contemporary 2026 adaptive-delay work explicitly uses frozen fixed-delay phase-locked branches to organise the slow adaptive dynamics. That makes robust branch continuation a first-class CORE requirement.

---

# 1. Normalised phase-locked coordinates

The v0.2 document used dimensional time offsets `phi_i`. For continuation it is cleaner to introduce **normalised phase offsets**

\[
\chi_i\in\mathbb R/\mathbb Z,
\]

with firing times

\[
T_i^m=(m+\chi_i)T.
\tag{C1}
\]

The two conventions are related by

\[
\phi_i=T\chi_i.
\tag{C2}
\]

Fix the global time-translation gauge by

\[
\chi_1=0.
\tag{C3}
\]

Then the branch unknown is

\[
z=(T,\chi_2,\ldots,\chi_N)\in\mathbb R^N.
\tag{C4}
\]

For the local phase coordinate of neuron `i`, write

\[
t=(m+\chi_i+\sigma)T,\qquad 0\le \sigma<1.
\tag{C5}
\]

Define

\[
X_{ij}(\sigma;z,p)
=T(\sigma+\chi_i-\chi_j)-\tau_{ij}(p),
\tag{C6}
\]

and

\[
\Psi_i(\sigma;z,p)
=I_i(\sigma;z,p)+
\sum_j w_{ij}(p)R_T\!\left(X_{ij}(\sigma;z,p);p\right).
\tag{C7}
\]

Here `p` denotes one or more continuation parameters, for example a delay, coupling strength, threshold, synaptic time scale, or external drive.

The phase-locked branch equations are

\[
\boxed{
F_i(z,p)
=
T\int_0^1 S_i\!\left(\Psi_i(\sigma;z,p);p\right)d\sigma
-2\pi
=0,
}
\tag{C8}
\]

for `i=1,...,N`.

Thus

\[
\boxed{F(z,p)=0,\qquad F:\mathbb R^N\times\mathbb R^q\to\mathbb R^N.}
\tag{C9}
\]

Using `chi_i` rather than dimensional offsets has three practical advantages:

- phases remain on a fixed unit circle as `T` changes;
- the integration domain is fixed (`sigma in [0,1]`);
- the branch Jacobian has no moving-boundary term from the integral limit.

For numerical continuation, use **unwrapped** `chi_i` internally and reduce modulo one only for display. Direct continuation on a wrapped coordinate introduces artificial discontinuities at `chi_i=0/1`.

---

# 2. Exact branch Jacobian

Assume for this section that the active branch lies in a smooth region of `S` and of the periodic kernel. Nonsmooth arrival and threshold boundaries are treated separately in Sections 8 and 9.

Write

\[
S_i'=\partial_xS_i(\Psi_i;p).
\]

For a phase variable `chi_k`, `k>=2`,

\[
\partial_{\chi_k}X_{ij}
=T(\delta_{ik}-\delta_{jk}).
\tag{C10}
\]

Therefore

\[
\partial_{\chi_k}\Psi_i
=T\left[
\delta_{ik}\sum_jw_{ij}R_T'(X_{ij})
-w_{ik}R_T'(X_{ik})
\right]
+\partial_{\chi_k}I_i.
\tag{C11}
\]

The phase columns of the branch Jacobian are

\[
\boxed{
\partial_{\chi_k}F_i
=T\int_0^1S_i'\,\partial_{\chi_k}\Psi_i\,d\sigma.
}
\tag{C12}
\]

When `I_i` is phase independent,

\[
\boxed{
\partial_{\chi_k}F_i
=T^2\int_0^1S_i'
\left[
\delta_{ik}\sum_jw_{ij}R_T'(X_{ij})
-w_{ik}R_T'(X_{ik})
\right]d\sigma.
}
\tag{C13}
\]

## 2.1 Period derivative

At fixed `(sigma,chi)` and fixed physical delays,

\[
\partial_TX_{ij}=\sigma+\chi_i-\chi_j.
\tag{C14}
\]

Hence

\[
\partial_T\Psi_i
=
\sum_jw_{ij}
\left[
\partial_TR_T(X_{ij})
+R_T'(X_{ij})(\sigma+\chi_i-\chi_j)
\right]
+\partial_TI_i,
\tag{C15}
\]

where `partial_T R_T(x)` means derivative with respect to the period at fixed argument `x`.

The first Jacobian column is

\[
\boxed{
\partial_TF_i
=
\int_0^1S_i(\Psi_i;p)d\sigma
+T\int_0^1S_i'\,\partial_T\Psi_i\,d\sigma.
}
\tag{C16}
\]

On a solution branch the first integral equals `2*pi/T`, so equivalently

\[
\boxed{
\partial_TF_i
=
\frac{2\pi}{T}
+T\int_0^1S_i'\,\partial_T\Psi_i\,d\sigma.
}
\tag{C17}
\]

This identity is useful as an implementation cross-check.

## 2.2 Parameter derivative

For a scalar continuation parameter `p`,

\[
\boxed{
\partial_pF_i
=T\int_0^1
\left[
S_i'\,\partial_p\Psi_i
+\partial_pS_i
\right]d\sigma.
}
\tag{C18}
\]

A general input derivative is

\[
\partial_p\Psi_i
=
\partial_pI_i
+\sum_j
\left[
(\partial_pw_{ij})R_T(X_{ij})
+w_{ij}\,\partial_pR_T(X_{ij})
-w_{ij}R_T'(X_{ij})\partial_p\tau_{ij}
\right].
\tag{C19}
\]

Equation (C19) deliberately separates weight, kernel, and delay sensitivities.

## 2.3 Kernel-period derivative from the spike comb

For

\[
R_T(x)=\sum_{m\in\mathbb Z}\eta(x-mT),
\tag{C20}
\]

formal differentiation gives, away from nonsmooth kernel points and under sufficient convergence,

\[
\boxed{
\partial_TR_T(x)
=-\sum_{m\in\mathbb Z}m\,\eta'(x-mT).
}
\tag{C21}
\]

This representation is often safer analytically than differentiating a `mod` implementation.

For the alpha kernel, `R_T` is continuous but its first derivative is only piecewise smooth at spike-arrival phases. Exact continuation must therefore be arrival-aware; see Section 9.

---

# 3. Hessian structure and second derivatives

For fold and symmetry-breaking nondegeneracy tests we need second and, in symmetric problems, third derivatives.

Let `z_a,z_b` be branch coordinates. Then

\[
\boxed{
\partial_{z_az_b}^2F_i
=
\partial_{z_b}\left(\partial_{z_a}F_i\right),
}
\]

with the generic integral structure

\[
\partial_{z_az_b}^2F_i
=
\text{boundary/prefactor terms}
+T\int_0^1
\left[
S_i''(\partial_{z_a}\Psi_i)(\partial_{z_b}\Psi_i)
+S_i'\partial_{z_az_b}^2\Psi_i
\right]d\sigma.
\tag{C22}
\]

For two phase coordinates, with phase-independent external drive,

\[
\partial_{\chi_k\chi_l}^2\Psi_i
=T^2\left[
\delta_{ik}\delta_{il}\sum_jw_{ij}R_T''(X_{ij})
-\delta_{ik}w_{il}R_T''(X_{il})
-\delta_{il}w_{ik}R_T''(X_{ik})
+\delta_{kl}w_{ik}R_T''(X_{ik})
\right].
\tag{C23}
\]

CORE code should obtain higher derivatives in two independent ways where feasible:

1. automatic differentiation of a smooth branch evaluator;
2. finite-difference or symbolic checks on controlled benchmark cases.

For exact alpha-kernel continuation across arrival phases, automatic differentiation through `mod` is not accepted as a reference calculation.

---

# 4. Pseudo-arclength continuation

Simple parameter stepping fails at folds. The canonical continuation problem is pseudo-arclength continuation.

Suppose `(z_0,p_0)` is a known solution and

\[
t_0=(t_z,t_p)
\]

is a unit branch tangent. A predictor is

\[
(z_{\rm pred},p_{\rm pred})=(z_0,p_0)+\Delta s\,t_0.
\tag{C24}
\]

The corrector solves

\[
F(z,p)=0
\tag{C25}
\]

plus the arclength condition

\[
\boxed{
t_0^T
\begin{pmatrix}
z-z_{\rm pred}\\
p-p_{\rm pred}
\end{pmatrix}=0.
}
\tag{C26}
\]

The Newton matrix is

\[
\boxed{
\begin{pmatrix}
D_zF & F_p\\
t_z^T & t_p
\end{pmatrix}.
}
\tag{C27}
\]

The tangent at a regular point satisfies

\[
\boxed{
\begin{pmatrix}D_zF & F_p\end{pmatrix}
\begin{pmatrix}t_z\\t_p\end{pmatrix}=0,
\qquad
\|t\|_2=1.
}
\tag{C28}
\]

The sign of the new tangent is chosen so that its dot product with the previous tangent is positive.

## 4.1 Conditioning diagnostics

Record at every continuation point:

- smallest singular value `sigma_min(D_zF)`;
- condition number of the corrector matrix;
- Newton residual norm;
- Newton correction norm;
- arclength step size;
- event-transversality margin;
- minimum distance to threshold-switching and arrival-collision surfaces;
- leading nontrivial Floquet/spike-time multiplier.

No branch diagram should be trusted without these diagnostics.

---

# 5. Generic fold of phase-locked solutions

At a regular branch point, `D_zF` is nonsingular and the implicit-function theorem gives a locally unique graph `z(p)`.

A generic fold occurs when

\[
\operatorname{rank}D_zF=N-1.
\tag{C29}
\]

Let right and left nullvectors satisfy

\[
D_zF\,r=0,
\qquad
\ell^TD_zF=0,
\qquad
\ell^Tr=1.
\tag{C30}
\]

The generic fold nondegeneracy conditions are

\[
\boxed{\ell^TF_p\ne0}
\tag{C31}
\]

and

\[
\boxed{
\ell^T D_z^2F[r,r]\ne0.
}
\tag{C32}
\]

The reduced local normal form is

\[
0=a\,\delta p+b\,\xi^2+\cdots,
\tag{C33}
\]

where

\[
a=\ell^TF_p,
\qquad
b=\frac12\ell^TD_z^2F[r,r].
\tag{C34}
\]

A vanishing smallest singular value alone is therefore **not sufficient** to declare a fold; (C31) and (C32) must also be checked.

---

# 6. Exchange-symmetric two-cell network

Consider

\[
W=
\begin{pmatrix}
w_s&w_c\\w_c&w_s
\end{pmatrix}
\tag{C35}
\]

with symmetric self-delay `tau_s`, cross-delay `tau_c`, common response function, and normalised phase difference

\[
\chi=\chi_2-\chi_1.
\]

Fix `chi_1=0`, so the branch variables are `(T,chi)`.

The two inputs are

\[
\Psi_1(\sigma)
=w_sR_T(T\sigma-\tau_s)
+w_cR_T(T(\sigma-\chi)-\tau_c),
\tag{C36}
\]

\[
\Psi_2(\sigma)
=w_cR_T(T(\sigma+\chi)-\tau_c)
+w_sR_T(T\sigma-\tau_s).
\tag{C37}
\]

Define

\[
F_+=\frac{F_1+F_2}{2},
\qquad
F_-=\frac{F_1-F_2}{2}.
\tag{C38}
\]

Exchange symmetry acts as

\[
\chi\mapsto-\chi,
\qquad
F_+(T,-\chi)=F_+(T,\chi),
\qquad
F_-(T,-\chi)=-F_-(T,\chi).
\tag{C39}
\]

Hence synchrony `chi=0` automatically satisfies

\[
F_-(T,0)=0.
\tag{C40}
\]

At synchrony,

\[
\partial_\chi F_+(T,0)=0,
\qquad
\partial_TF_-(T,0)=0.
\tag{C41}
\]

Therefore the Jacobian in `(F_+,F_-)` coordinates is diagonal:

\[
\boxed{
D_{(T,\chi)}(F_+,F_-)|_{\chi=0}
=
\begin{pmatrix}
A&0\\0&B
\end{pmatrix},
}
\tag{C42}
\]

with

\[
A=\partial_TF_+(T,0),
\qquad
B=\partial_\chi F_-(T,0).
\tag{C43}
\]

This separates the two principal existence singularities:

- `A=0`, `B!=0`: fold of the synchronous period branch;
- `B=0`, `A!=0`: symmetry-breaking of the relative phase.

## 6.1 Explicit symmetry-breaking coefficient

At synchrony define

\[
\Psi_0(\sigma)=
 w_sR_T(T\sigma-\tau_s)
+w_cR_T(T\sigma-\tau_c).
\tag{C44}
\]

Then

\[
\boxed{
B
=-T^2w_c
\int_0^1
S'(\Psi_0)
R_T'(T\sigma-\tau_c)
\,d\sigma.
}
\tag{C45}
\]

Equation (C45) is an important v0.3 benchmark.

If there is only one shifted input waveform and no nonlinear waveform overlap, the full-period shift invariance can force this coefficient to vanish identically. Thus a zero value of `B` must be interpreted structurally before it is labelled as an isolated pitchfork.

## 6.2 Generic pitchfork reduction

Assume `A!=0` and `B=0` at `(T_*,p_*)`. Since `F_+` is even in `chi`, solve it locally as

\[
T=T_s(p)+c\chi^2+O(\chi^4),
\tag{C46}
\]

where

\[
\boxed{
c=-\frac{F_{+,\chi\chi}}{2F_{+,T}}}
\tag{C47}
\]

at the bifurcation point.

Because `F_-` is odd,

\[
F_-=\chi\left[a\,\delta p+b\chi^2+\cdots\right].
\tag{C48}
\]

Along the synchronous branch,

\[
T_s'(p)=-\frac{F_{+,p}}{F_{+,T}},
\tag{C49}
\]

so the unfolding coefficient is

\[
\boxed{
a
=F_{-,\chi p}
-\frac{F_{-,\chi T}F_{+,p}}{F_{+,T}}.
}
\tag{C50}
\]

The cubic coefficient after eliminating `T` is

\[
\boxed{
b
=\frac16F_{-,\chi\chi\chi}
-\frac{F_{-,\chi T}F_{+,\chi\chi}}{2F_{+,T}}.
}
\tag{C51}
\]

A generic exchange-symmetry pitchfork requires

\[
\boxed{a\ne0,\qquad b\ne0.}
\tag{C52}
\]

The nontrivial branches satisfy to leading order

\[
\boxed{
\chi^2\sim-\frac{a}{b}(p-p_*).
}
\tag{C53}
\]

This provides a quantitative branch-direction test for numerical continuation.

---

# 7. Existence bifurcation versus dynamical stability bifurcation

The branch equation `F(z,p)=0` answers whether a phase-locked orbit exists and how its period/phase offsets vary. It does **not** by itself determine whether that orbit attracts perturbations.

Let the spike-time/event linearisation produce a characteristic matrix

\[
\mathcal E(\lambda;z,p),
\tag{C54}
\]

or an equivalent monodromy/event map with multipliers `mu`.

With the per-cycle ansatz used in v0.2,

\[
\mu=e^\lambda.
\tag{C55}
\]

The orbit is linearly stable when all nontrivial roots satisfy

\[
\Re\lambda<0
\tag{C56}
\]

or equivalently all nontrivial multipliers satisfy

\[
|\mu|<1.
\tag{C57}
\]

The global time-translation mode gives the neutral root

\[
\lambda=0
\qquad\Longleftrightarrow\qquad
\mu=1,
\tag{C58}
\]

and must be excluded from the stability decision.

For a gauge-fixed event map the neutral direction may be removed explicitly.

## 7.1 Dynamic critical cases

CORE classifies multiplier crossings as follows:

### Real unit crossing

\[
\mu=+1
\tag{C59}
\]

apart from the trivial translation multiplier. This can signal a steady phase mode, branch exchange, or a cycle fold/pitchfork depending on symmetry and nonlinear terms.

### Flip / period-doubling

\[
\boxed{\mu=-1}
\tag{C60}
\]

corresponding to a period-two modulation of the event sequence.

### Oscillatory / torus instability

\[
\boxed{\mu_{1,2}=e^{\pm i\Omega},\qquad 0<\Omega<\pi.}
\tag{C61}
\]

For a Poincare/event map this is a Neimark-Sacker crossing. In delay-equation language the same phenomenon is often described as a Hopf-type oscillatory instability because the associated characteristic roots cross the imaginary axis.

The project should report both the multiplier and characteristic-root language to avoid ambiguity.

## 7.2 Delay-induced instability

A delay parameter enters the characteristic equations through phase factors or delayed spike-index couplings. A branch may therefore remain perfectly regular in `D_zF` while a nontrivial multiplier crosses the unit circle.

Thus

\[
\boxed{
\det D_zF\ne0
\quad\text{does not imply dynamical stability.}
}
\tag{C62}
\]

Likewise a fold of the branch equations does not automatically specify the Floquet spectrum.

---

# 8. Hybrid singularity: loss of spike-event transversality

Let the spike event surface be

\[
g_i(\theta_i,m)=\theta_i-2\pi m=0.
\tag{C63}
\]

Its crossing speed is

\[
\nu_i
=\nabla g_i\cdot f
=\dot\theta_i
=S_i(\Psi_i).
\tag{C64}
\]

A regular event requires

\[
\boxed{\nu_i\ne0.}
\tag{C65}
\]

The v0.2 event-time sensitivity

\[
\delta T_i=-\frac{\delta\theta_i}{\nu_i}
\tag{C66}
\]

and the saltation matrix both contain `1/nu_i`. Therefore

\[
\boxed{\nu_i\to0}
\tag{C67}
\]

is an intrinsic singular limit of the event description.

We call this **event grazing / loss of transversality**.

It is not detected reliably by `det(D_zF)`.

At every branch point define the event-transversality diagnostic

\[
\boxed{
\nu_{\min}=\min_i S_i(\Psi_i(1^-)).
}
\tag{C68}
\]

for the chosen firing convention. A branch approaching `nu_min=0` must be flagged even if continuation Newton iterations remain well conditioned.

## 8.1 Premature-event admissibility

The one-spike-per-period ansatz also requires that the assumed endpoint is the first hitting time of the firing section. Define accumulated phase

\[
\Theta_i(\sigma)
=T\int_0^\sigma S_i(\Psi_i(\xi))d\xi.
\tag{C69}
\]

A valid locked orbit requires

\[
\boxed{
\Theta_i(\sigma)<2\pi
\quad\text{for all }0\le\sigma<1,
\qquad
\Theta_i(1)=2\pi.
}
\tag{C70}
\]

Violation of (C70) is an admissibility failure of the assumed event itinerary, not merely a small numerical error.

---

# 9. Threshold and arrival-order nonsmoothness

The exact Lighthouse model may contain nonsmooth response thresholds and causal kernels. Two additional codimension-one surfaces matter.

## 9.1 Response-threshold contact

If `S` contains a switching threshold `h`, define

\[
H_i(\sigma)=\Psi_i(\sigma)-h.
\tag{C71}
\]

When the orbit changes the set of intervals on which `H_i>0`, the branch equations become only piecewise smooth. A tangential threshold contact satisfies

\[
\boxed{
H_i(\sigma_*)=0,
\qquad
\partial_\sigma H_i(\sigma_*)=0.
}
\tag{C72}
\]

This is a switching/grazing boundary and must not be passed using a naive smooth Newton Jacobian.

## 9.2 Arrival-phase collision

For a causal kernel, an incoming spike from `j` reaches `i` at a phase determined by

\[
a_{ij}
=\left(\chi_j-\chi_i+\frac{\tau_{ij}}{T}\right)\bmod1.
\tag{C73}
\]

A change in ordering occurs when two arrival phases coincide or an arrival crosses the cycle boundary:

\[
\boxed{a_{ij}=a_{ik}\pmod1}
\tag{C74}
\]

or

\[
\boxed{a_{ij}=0\pmod1.}
\tag{C75}
\]

For the alpha kernel, `R_T` is continuous at an arrival but `R_T'` has a jump. Therefore the branch itself may remain continuous while its Jacobian changes piecewise.

**Reference implementation rule:** exact quadrature should split the cycle at all arrival phases. Differentiating directly through `mod` is permitted only for explicitly labelled smooth-surrogate calculations.

---

# 10. Slow-fast adaptive delays and frozen branches

The 2026 adaptive-delay Lighthouse framework motivates

\[
F(z,\tau,p)=0
\tag{C76}
\]

for the fast locked state, coupled to slow delay dynamics

\[
\dot\tau=\varepsilon G(z,\tau,p),
\qquad 0<\varepsilon\ll1.
\tag{C77}
\]

Away from folds and hybrid singularities, the implicit-function theorem gives a frozen branch

\[
z=z_*(\tau,p).
\tag{C78}
\]

Its sensitivity is

\[
\boxed{
\frac{dz_*}{d\tau}
=-(D_zF)^{-1}F_\tau.
}
\tag{C79}
\]

The reduced slow flow is therefore

\[
\boxed{
\dot\tau
=\varepsilon G(z_*(\tau,p),\tau,p).
}
\tag{C80}
\]

Equation (C79) shows why folds are dynamically important for adaptive conduction: as the smallest singular value of `D_zF` approaches zero, frozen-branch sensitivity can become large and normal hyperbolicity is lost.

This provides a clean mathematical mechanism for slow drift followed by fast switching between phase-locked states.

## 10.1 Commensurability surfaces

Adaptive-delay work highlights delay-period relationships of the form

\[
\tau_{ij}\approx k_{ij}T
\tag{C81}
\]

or, more generally, fixed arrival phases. Define the commensurability residual

\[
\boxed{
C_{ij}^{(k)}=\tau_{ij}-kT.
}
\tag{C82}
\]

Tracking zero sets of (C82) along frozen branches allows direct comparison between branch geometry and delay-plasticity fixed points.

---

# 11. Symmetry and graph representations

For networks equivariant under a symmetry group `G`, the branch operator satisfies

\[
F(gz,p)=gF(z,p),
\qquad g\in G.
\tag{C83}
\]

At a symmetric locked state, `D_zF` commutes with the isotropy representation and can be block-diagonalised into symmetry sectors.

This generalises the two-cell decomposition into symmetric and antisymmetric modes.

A **symmetry-breaking existence bifurcation** occurs when a zero singular/eigenmode appears in a nontrivial symmetry sector while the tangent mode inside the symmetric fixed-point subspace remains regular.

For circulant rings, the natural sectors are discrete Fourier modes. This aligns with the contemporary Lighthouse stability analysis in which spatially structured rings decompose into Fourier modes.

CORE should use symmetry-adapted coordinates whenever available rather than treating all `N` phase variables as an undifferentiated dense system.

---

# 12. Branch labelling protocol

Every stored continuation point should contain at least:

\[
(T,\chi_2,\ldots,\chi_N,p),
\]

plus the following labels/diagnostics:

1. residual `||F||`;
2. `sigma_min(D_zF)`;
3. branch tangent;
4. event-transversality margin `nu_min`;
5. admissibility status from first-hitting tests;
6. threshold-contact distance;
7. arrival-collision distance;
8. leading nontrivial multiplier/root;
9. number of unstable multipliers/roots;
10. symmetry/isotropy label;
11. commensurability residuals if delays are continued;
12. provenance of derivative evaluation: exact piecewise, analytic, autodiff surrogate, or finite difference.

Suggested critical-point labels:

- `REG` regular;
- `FOLD` branch fold;
- `SB` symmetry breaking;
- `PD` period doubling / flip;
- `NS` Neimark-Sacker / oscillatory delay instability;
- `EV_GRAZE` spike-event loss of transversality;
- `TH_GRAZE` threshold switching contact;
- `ARR_COLL` arrival-order collision;
- `ADM_FAIL` invalid one-spike itinerary.

A point may carry more than one label in codimension-two situations.

---

# 13. Codimension-two targets

After one-parameter continuation is reliable, CORE should search for intersections of critical conditions, including

\[
\text{FOLD}+\text{NS},
\qquad
\text{SB}+\text{NS},
\qquad
\text{FOLD}+\text{EV_GRAZE},
\qquad
\text{SB}+\text{ARR_COLL}.
\tag{C84}
\]

These points are likely to organise complex switching and multistability more strongly than generic regular branch segments.

For adaptive delays, a particularly important case is a slow-flow fixed point approaching a fold or symmetry-breaking point of the frozen fast subsystem.

---

# 14. Exact versus surrogate continuation

The project will maintain two continuation layers.

## 14.1 Exact/reference layer

- exact event itinerary;
- exact causal kernel or exact finite-dimensional hybrid state;
- arrival-aware quadrature;
- explicit threshold intervals for nonsmooth `S`;
- exact or independently validated Jacobians;
- event-time stability calculation.

## 14.2 Differentiable surrogate layer

- smoothed threshold;
- smoothed/wrapped periodic kernel if needed;
- standard JAX automatic differentiation;
- gradients suitable for fitting and optimisation.

The surrogate branch must be compared against the exact branch in

\[
T,
\quad
\chi_i,
\quad
p_{\rm crit},
\quad
\mu_{\rm lead},
\tag{C85}
\]

before surrogate-derived scientific claims are accepted.

---

# 15. Minimal v0.3 theorems / propositions to test numerically

## Proposition P1 — gauge invariance

Uniform phase translation leaves the dimensional locked state invariant. Gauge fixing `chi_1=0` removes exactly one neutral coordinate from the branch equations.

## Proposition P2 — normalised Jacobian

Equations (C13), (C16), and (C18) reproduce finite-difference sensitivities at regular smooth branch points.

## Proposition P3 — exchange-symmetry block diagonalisation

For the symmetric two-cell network, the existence Jacobian at synchrony is diagonal in `(F_+,F_-)` coordinates, equation (C42).

## Proposition P4 — symmetry-breaking coefficient

Equation (C45) equals the antisymmetric Jacobian eigenvalue of the two-cell existence problem at synchrony.

## Proposition P5 — generic fold scaling

Near a nondegenerate fold, branch displacement scales as

\[
|z-z_*|=O(|p-p_*|^{1/2}).
\tag{C86}
\]

## Proposition P6 — generic pitchfork scaling

Near a nondegenerate exchange-symmetry pitchfork,

\[
|\chi|=O(|p-p_*|^{1/2}),
\tag{C87}
\]

with coefficient predicted by (C53).

## Proposition P7 — transversality singularity

Event-time and saltation sensitivities diverge like `1/nu_i` as `nu_i -> 0`, unless a problem-specific numerator vanishes simultaneously.

## Proposition P8 — frozen-branch sensitivity

Away from singular points, finite differences along a delay-continued branch agree with

\[
-(D_zF)^{-1}F_\tau.
\]

---

# 16. CORE v0.3 conclusions

The central mathematical object is now

\[
\boxed{F(z,p)=0}
\]

augmented by two independent structures:

\[
\boxed{\text{event/Floquet stability}}
\]

and

\[
\boxed{\text{hybrid admissibility/transversality}}.
\]

The project therefore adopts the following hierarchy:

\[
\text{branch existence}
\;\to\;
\text{branch singularity}
\;\to\;
\text{dynamic stability}
\;\to\;
\text{hybrid validity}.
\]

For adaptive delays this becomes

\[
\boxed{
\text{frozen Lighthouse branches}
\;\to\;
\text{slow drift}
\;\to\;
\text{loss of normal hyperbolicity / stability}
\;\to\;
\text{fast switching}.
}
\]

This is the mathematical bridge from the historical phase-locking problem to a modern synergetic slow-fast theory of mode selection.