# CORE event-map normal forms v0.7

## Purpose

CORE v0.7 converts the v0.5 normal-form theory and v0.6 numerical atlas into direct calculations on a gauge-fixed Lighthouse spike-history return map. The goals are:

1. extract a cubic coefficient directly from the exact event dynamics rather than infer it only from branch geometry;
2. exhibit a generic flip bifurcation with a continued period-two spike pattern;
3. exhibit a generic Neimark--Sacker bifurcation in the first nonlinear finite-ring benchmark and compute its first Lyapunov coefficient;
4. quantify convergence with respect to spike-history truncation.

All numerical benchmarks use the smooth-above-threshold Lighthouse response

\[
S(x)=\exp[-1/(x+1)^2]H(x+1)
\]

and the alpha kernel

\[
\eta(t)=\alpha^2t e^{-\alpha t}H(t),\qquad \alpha=0.5.
\]

The critical orbits reported below stay strictly above the response threshold and have positive event velocity, so the return maps are evaluated inside one fixed smooth event/arrival itinerary.

---

# 1. Gauge-fixed spike-history return map

Let the current cycle be labelled `m=0`. Store the last `L` spike-time deviations

\[
x_{rj}=\delta T_j^{-r},\qquad r=0,\ldots,L-1.
\tag{V71}
\]

The perturbed presynaptic activity can be evaluated as the exact periodic base comb plus a finite correction:

\[
a_j(t)
=R_T(t)
+\sum_{r=0}^{L-1}
\left[
\eta(t+rT-x_{rj})-\eta(t+rT)
\right].
\tag{V72}
\]

For edge delay `tau_ij`, replace `t` by `t-tau_ij`. The unperturbed tail older than `L` cycles is retained exactly by `R_T`; only the perturbation tail is truncated. For the present alpha-kernel benchmarks, `alpha*T` is large enough that `L=4` and `L=5` already agree to much better precision than required by the benchmark contract.

For neuron `i`, solve the first-hitting equation

\[
2\pi
=\int_{x_{0i}}^{T+\delta T_i^{1}}
S\!\left(\psi_i(t;x)\right)dt
\tag{V73}
\]

for the next spike deviation `delta T_i^1`.

Remove global time translation by

\[
g=\frac1N\sum_i\delta T_i^1
\tag{V74}
\]

and define the gauge-fixed return map

\[
\boxed{
\mathscr P_L(x)_{0i}=\delta T_i^1-g,
\qquad
\mathscr P_L(x)_{ri}=x_{r-1,i}-g,
\quad r\ge1.
}
\tag{V75}
\]

The Jacobian

\[
L=D\mathscr P_L(0)
\tag{V76}
\]

is the finite-history approximation to the gauge-fixed event return operator. Unlike the raw lifted-phase flow-plus-saltation matrix, (V75) removes the global time-shift mode explicitly.

---

# 2. Direct multilinear derivatives

Use the Taylor convention

\[
\mathscr P(x)=Lx+\frac12B(x,x)+\frac16C(x,x,x)+\cdots.
\tag{V77}
\]

The reference implementation evaluates `B` and `C` by symmetric directional differences of the exact event map, not by differentiating a smoothed surrogate.

For a real direction `q`,

\[
B(q,q)
=\lim_{h\to0}
\frac{\mathscr P(hq)-2\mathscr P(0)+\mathscr P(-hq)}{h^2},
\tag{V78}
\]

and

\[
C(q,q,q)
=\lim_{h\to0}
\frac{
\mathscr P(2hq)-2\mathscr P(hq)+2\mathscr P(-hq)-\mathscr P(-2hq)
}{2h^3}.
\tag{V79}
\]

Mixed derivatives use the corresponding central polarization formulas.

---

# 3. Generic two-cell flip benchmark

Consider the exchange-symmetric two-cell network

\[
W=\begin{pmatrix}w_s&w_c\\w_c&w_s\end{pmatrix},
\qquad
w_s+w_c=\Gamma=1,
\tag{V710}
\]

with

\[
\tau_s=0,
\qquad
\tau_c=2.
\tag{V711}
\]

Use the transverse eigenvalue

\[
\widehat w=w_s-w_c
\tag{V712}
\]

as the continuation parameter, so

\[
w_s=\frac{1+\widehat w}{2},
\qquad
w_c=\frac{1-\widehat w}{2}.
\tag{V713}
\]

Solving the synchronous existence equation together with the antisymmetric flip condition

\[
E_-(-1)=0
\tag{V714}
\]

gives

\[
\boxed{
\widehat w_*=10.508451441614785,
\qquad
T_*=16.81736224376564.
}
\tag{V715}
\]

Thus

\[
w_s=5.754225720807392,
\qquad
w_c=-4.754225720807392.
\tag{V716}
\]

This is a generic flip rather than a hidden unit-multiplier degeneracy:

\[
\boxed{E_-(1)=0.7423135516929733\ne0.}
\tag{V717}
\]

At the firing section,

\[
\nu_*=0.3639833534456731>0,
\tag{V718}
\]

and over the full cycle `S(psi)` remains positive (`min S approx 0.1950`).

## 3.1 Critical event-history mode

In physical spike-time normalisation, the flip eigenvector is

\[
\boxed{
q_F^{(r)}=(-1)^r(1,-1)^T,
\qquad r=0,\ldots,L-1.
}
\tag{V719}
\]

and

\[
Lq_F=-q_F.
\tag{V720}
\]

Let `p_F` be the left eigenvector normalised by

\[
p_F^Tq_F=1.
\tag{V721}
\]

The direct map coefficient is

\[
\boxed{
c_f
=\frac16p_F^TC(q_F,q_F,q_F)
+\frac12p_F^TB\!\left(q_F,(I-L)^{-1}B(q_F,q_F)\right).
}
\tag{V722}
\]

Numerically,

\[
\boxed{c_f^{\rm map}=0.5502495\ \text{(L=4)},}
\]

\[
\boxed{c_f^{\rm map}=0.5502496\ \text{(L=5)}.}
\tag{V723}
\]

The difference is below `2e-7` at the quoted finite-difference step.

## 3.2 Crossing speed

Along the synchronous branch,

\[
\left.\frac{d\mu_-}{d\widehat w}\right|_*
=-0.295658029254714.
\tag{V724}
\]

With the v0.5 convention

\[
A_{n+1}=-(1+\sigma\varepsilon)A_n+c_fA_n^3+\cdots,
\qquad
\varepsilon=\widehat w-\widehat w_*,
\]

this gives

\[
\boxed{\sigma=0.295658029254714.}
\tag{V725}
\]

---

# 4. Exact period-two spike branch

The period-doubled antisymmetric spike pattern can be parameterised by

\[
T_1^m=mT+A(-1)^m,
\qquad
T_2^m=mT-A(-1)^m.
\tag{V726}
\]

Over the doubled period `2T`, neuron 1 fires at `A` and `T-A`, while neuron 2 fires at `-A` and `T+A`. Construct the exact `2T`-periodic alpha-kernel comb from these four spike phases and impose phase gain `2pi` on the two alternating interspike intervals of neuron 1. Exchange/cycle symmetry supplies the neuron-2 equations.

The nontrivial branch exists for

\[
\varepsilon=\widehat w-\widehat w_*>0
\]

and satisfies

\[
\boxed{
A^2
=0.5373149\,\varepsilon+o(\varepsilon),
}
\tag{V727}
\]

\[
\boxed{
T-T_*
=0.1154757\,\varepsilon+o(\varepsilon).
}
\tag{V728}
\]

The normal form predicts

\[
A^2\sim\frac{\sigma}{c_f}\varepsilon.
\tag{V729}
\]

Using the continued period-two branch gives

\[
\boxed{c_f^{\rm branch}=0.55025094,}
\tag{V730}
\]

which agrees with the direct return-map value (V723) to a few parts in `10^6`.

This is the first CORE coefficient independently determined by:

1. third-order derivatives of the exact gauge-fixed event map;
2. a separately continued nonlinear period-two spike orbit.

---

# 5. v0.6 pitchfork consistency identity

For the v0.6 two-cell pitchfork, the existence cubic coefficient `b`, period `T`, and dynamic mass `E_mu=partial_mu E_-(1)` satisfy in the documented `A=chi` normalisation

\[
\boxed{
c_\chi=-\frac{2b}{T E_\mu}.}
\tag{V731}
\]

Using

\[
b=-0.02718724838,
\quad
T=13.4306902003,
\quad
E_\mu=0.445594394
\]

gives

\[
\boxed{c_\chi=0.00908567506,}
\tag{V732}
\]

independently reproducing the v0.6 value inferred from branch slope and multiplier slope. Equation (V731) makes explicit why replacing the event-history dynamic mass by the endpoint velocity `nu` gives the wrong cubic coefficient.

---

# 6. First nonlinear ring Neimark--Sacker benchmark

Take `N=3` and index ring edges by displacement `d=0,1,2`. Let

\[
\boxed{
w_d=[1,p,-p],}
\tag{V733}
\]

so the row sum is identically one, and choose

\[
\boxed{\tau_d=[0,2,5].}
\tag{V734}
\]

The critical parameter is

\[
\boxed{p_*=-2.6069763661290217,}
\tag{V735}
\]

with synchronous period

\[
\boxed{T_*=15.565320495514536.}
\tag{V736}
\]

The critical Fourier sector is `q=1` (with its real conjugate sector `q=2`). Its multiplier is

\[
\boxed{
\mu_*=0.96331925+0.26835800i,
}
\tag{V737}
\]

with

\[
|\mu_*|=1+O(10^{-9}),
\qquad
\boxed{\Omega=0.271688105857\ldots}.
\tag{V738}
\]

The remaining computed gauge-fixed history multipliers are strictly inside the unit circle. Event transversality is regular:

\[
\nu_*=0.3871891405609047,
\qquad
\min_t S(\psi_*(t))\approx0.09715>0.
\tag{V739}
\]

## 6.1 Physical Fourier-amplitude normalisation

Use

\[
\xi_i=e^{2\pi i i/3},
\qquad i=0,1,2,
\tag{V740}
\]

and define the history eigenvector by

\[
\boxed{
q_{NS}^{(r)}=\mu_*^{-r}\xi,
\qquad r=0,\ldots,L-1.
}
\tag{V741}
\]

This fixes the otherwise arbitrary eigenvector scale: the order parameter is the physical complex spike-time Fourier amplitude in the current cycle.

Let `p_NS` satisfy

\[
p_{NS}^*q_{NS}=1.
\tag{V742}
\]

With the v0.5 homological equations

\[
h_{20}=(\mu_*^2I-L)^{-1}B(q,q),
\]

\[
h_{11}=(I-L)^{-1}B(q,\bar q),
\]

and

\[
G_{21}=p^*\left[
C(q,q,\bar q)+B(\bar q,h_{20})+2B(q,h_{11})
\right],
\]

the first Lyapunov coefficient is

\[
\ell_1=\frac12\operatorname{Re}(e^{-i\Omega}G_{21}).
\tag{V743}
\]

Direct event-map differentiation gives

\[
\boxed{
\ell_1=0.0051638971\quad(L=4),
}
\]

\[
\boxed{
\ell_1=0.0051638857\quad(L=5).
}
\tag{V744}
\]

The history-truncation difference is approximately `1.1e-8`.

## 6.2 Crossing speed and classification

Along the synchronous branch,

\[
\boxed{
\frac{d|\mu|}{dp}\bigg|_*=-0.1093172533,
}
\tag{V745}
\]

and

\[
\frac{d\arg\mu}{dp}\bigg|_*
=-0.1739045745.
\tag{V746}
\]

Because the radial crossing speed is negative while `ell_1>0`, the local Neimark--Sacker bifurcation is **subcritical** in this convention. The small invariant circle lies on the side `p>p_*`, where the synchronous fixed point is already linearly stable, and is radially unstable.

The local amplitude prediction is

\[
\boxed{
|A|^2
\sim
21.16955\,(p-p_*).
}
\tag{V747}
\]

for the physical Fourier amplitude (V741).

This is the first nonlinear Lighthouse ring benchmark in CORE: a spatial Fourier mode is simultaneously the critical spike-time mode and the synergetic order parameter.

---

# 7. Benchmark contract B73--B90

**B73** Gauge-fixed zero state: `||P_L(0)||` is below numerical tolerance.

**B74** Flip critical residual: synchronous existence residual and `E_-(-1)` vanish at (V715).

**B75** Flip genericity: `|E_-(1)| > 0.7` at the critical point.

**B76** Flip eigenvector: `||L q_F + q_F||` converges with finite-difference refinement.

**B77** Flip coefficient/history convergence: `c_f(L=4)` and `c_f(L=5)` agree within `5e-6`.

**B78** Flip branch scaling: `A^2/epsilon -> 0.537315`.

**B79** Flip period scaling: `(T-T*)/epsilon -> 0.115476`.

**B80** Independent flip coefficient: direct-map and branch-derived `c_f` agree within `1e-4`.

**B81** v0.6 pitchfork mass identity: (V731) reproduces `c_chi` within `1e-7`.

**B82** NS critical residual: `E_1(mu*)` and synchronous existence residual vanish.

**B83** NS unit modulus: `||mu*|-1| < 1e-6`.

**B84** NS angle: computed map eigenvalue angle agrees with (V738).

**B85** NS physical eigenvector: `||L q_NS-mu*q_NS||/||q_NS|| < 1e-6`.

**B86** NS history convergence: `ell_1(L=4)` and `ell_1(L=5)` agree within `5e-6`.

**B87** NS nondegeneracy: `|d|mu|/dp| > 0.1` and `ell_1 != 0`.

**B88** NS resonance guard: report distances of `k*Omega` from `2pi Z` for low orders before applying the generic normal form.

**B89** NS classification: signs of radial crossing speed and `ell_1` imply the same subcritical label in both code and documentation.

**B90** Exact/surrogate future contract: a JAX surrogate is not accepted until it reproduces the flip critical parameter, `c_f`, NS critical parameter, critical complex multiplier, and `ell_1` within declared tolerances.

---

# 8. Consequences for CORE

v0.7 closes an important methodological loop:

\[
\boxed{
\text{exact spike events}
\to
\text{gauge-fixed return map}
\to
\text{Floquet mode}
\to
\text{direct }B,C
\to
\text{normal-form coefficient}
\to
\text{independent nonlinear branch check}.
}
\]

The order parameter is no longer only a conceptual label. For the flip it is the physical alternating antisymmetric spike-time amplitude; for the ring NS point it is the physical complex Fourier spike-time amplitude.

The next CORE step should move from isolated codimension-one examples to a two-parameter atlas: continue the flip and NS loci, locate their interactions with unit-multiplier, grazing, and arrival-collision curves, and then couple the verified fast normal forms to slowly adaptive delays.