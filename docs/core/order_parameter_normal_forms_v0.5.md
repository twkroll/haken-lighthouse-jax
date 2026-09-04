# CORE order-parameter and normal-form theory v0.5

## Purpose

CORE v0.1--v0.4 established the hybrid Lighthouse graph model, phase-locked branch equations, spike-time Floquet operator, and symmetry reductions. v0.5 answers the next question:

> What is the reduced nonlinear dynamics when one or a few nontrivial spike-time/Floquet modes become critical?

This is the natural point at which the Lighthouse model reconnects explicitly to Haken's synergetics.

The central project interpretation is:

- the **critical spike-time/Floquet mode amplitude** is the local order parameter;
- strongly stable spike-time and synaptic/history directions are slaved to that amplitude;
- adaptive delays are, in general, **slow state/control variables**, not automatically order parameters;
- when several multipliers are simultaneously weak, all corresponding amplitudes belong to the order-parameter set.

Provenance tags:

- **[H]** synergetic order-parameter/slaving structure attributable to Haken;
- **[C]** standard center-manifold/normal-form theory for maps and the current Lighthouse literature;
- **[P]** project canonicalisation that connects those ideas to the v0.4 spike-time characteristic operator.

The theory is local. It assumes a fixed event/arrival itinerary, regular spike crossings, and sufficient smoothness of the corresponding return map. Grazing, threshold switching, arrival collisions, and itinerary changes require the nonsmooth diagnostics of v0.3 rather than the smooth normal forms below.

---

# 1. Gauge-fixed event return map

Let `Sigma` be a local event/Poincare section in which global time translation has been fixed. Denote its state or history coordinate by `y`. For a parameter `p`, define the one-cycle return map

\[
\boxed{
y_{n+1}=\mathscr P_p(y_n).
}
\tag{N1}
\]

A phase-locked Lighthouse orbit corresponds to a fixed point

\[
\boxed{y_*(p)=\mathscr P_p(y_*(p)).}
\tag{N2}
\]

Its linearisation is

\[
L(p)=D_y\mathscr P_p(y_*(p)).
\tag{N3}
\]

For delayed networks `L` acts on a history space and need not be a finite matrix. The nontrivial point spectrum relevant to the phase-locked event dynamics is the same spectrum represented implicitly by the v0.4 nonlinear characteristic equation

\[
\mathcal M(\mu)\xi=0.
\tag{N4}
\]

The exact neutral global time-shift multiplier has already been removed by the gauge choice defining `Sigma`. No subsequent normal-form calculation may simply delete an arbitrary multiplier closest to one.

---

# 2. Critical subspace and the slaving principle

Suppose at `(y_*,p_*)` the spectrum splits into a finite critical set and a stable complement,

\[
\sigma(L)=\sigma_c\cup\sigma_s,
\]

with

\[
|\mu|\le 1-\delta
\qquad(\mu\in\sigma_s)
\tag{N5}
\]

for some spectral gap `delta>0`, while the multipliers in `sigma_c` lie on or near the unit circle.

Let `V_c` collect critical right eigenvectors and let `A` denote their amplitude coordinates. Locally, center-manifold/slaving theory gives

\[
\boxed{
y-y_*=V_cA+h(A,\bar A,\varepsilon),}
\tag{N6}
\]

where

\[
\varepsilon=p-p_*,
\qquad
h=O(\|A\|^2+|\varepsilon|\|A\|).
\tag{N7}
\]

Thus the high-dimensional event/history state is locally parametrised by a few amplitudes. This is the precise CORE meaning of Haken's slaving principle in the Lighthouse setting.

### CORE terminology

The order parameter is **not** automatically:

- the microscopic phase `theta_i`;
- the mean firing rate;
- the synaptic variable;
- the conduction delay.

Near a given instability it is the amplitude of the critical collective mode, for example

\[
A_q\quad\text{for a critical ring Fourier sector }q.
\]

Different bifurcations can therefore have different order parameters.

### Nonnormality warning

A spectral gap based only on eigenvalue moduli can be misleading for a highly nonnormal event operator. The v0.4 conditioning quantity

\[
\kappa_\mu^{-1}
=|y^*\mathcal M'(\mu)\xi|
\tag{N8}
\]

and singular-value diagnostics should be recorded together with the nominal gap. Nearly defective or highly sensitive modes must not be slaved merely because their computed multiplier is slightly inside the unit circle.

---

# 3. Taylor convention for a smooth return map

For coefficient formulas below, translate the critical fixed point to the origin and write

\[
\mathscr P(x)
=Lx+\frac12B(x,x)+\frac16C(x,x,x)+O(\|x\|^4),
\tag{N9}
\]

where

- `B=D^2\mathscr P(0)` is the symmetric bilinear second derivative;
- `C=D^3\mathscr P(0)` is the symmetric trilinear third derivative.

Right and left critical eigenvectors are normalised by

\[
Lq=\mu_c q,
\qquad
p^*L=\mu_c p^*,
\qquad
p^*q=1.
\tag{N10}
\]

For a real unit or flip multiplier, real vectors can be used. For a complex pair, `p^*q=1` denotes the Hermitian pairing.

The formulas below define the project coefficient convention. If another software package uses a different factorial convention for `B` or `C`, its coefficients must be converted before comparison.

---

# 4. Simple nontrivial unit multiplier: fold of cycles

Assume a **nontrivial** simple multiplier reaches

\[
\mu_c=+1
\]

with no symmetry forcing the amplitude to change sign. The scalar center map has the form

\[
\boxed{
A_{n+1}-A_n
=a\varepsilon+bA_n^2
+O(|A|^3+|\varepsilon A|+\varepsilon^2).
}
\tag{N11}
\]

The leading coefficients can be written

\[
\boxed{a=p^*\mathscr P_p,}
\tag{N12}
\]

\[
\boxed{b=\frac12p^*B(q,q),}
\tag{N13}
\]

when the coordinate origin is chosen at the critical fixed point and `p` is varied transversely to the cycle fold.

The genericity conditions are

\[
\boxed{a\ne0,\qquad b\ne0.}
\tag{N14}
\]

Fixed points of the reduced map satisfy

\[
A^2\sim-\frac{a}{b}\varepsilon.
\tag{N15}
\]

This is the dynamical-return-map counterpart of the v0.3 Lyapunov--Schmidt fold equation. When both are applied to the same cycle and parameterisation, branch direction and square-root scaling must agree.

---

# 5. Exchange symmetry and the dynamic pitchfork

Consider an exchange-symmetric branch whose critical timing mode is antisymmetric. Let the symmetry act as

\[
A\mapsto-A.
\tag{N16}
\]

Equivariance forces the scalar center map to be odd. Near a nontrivial unit-multiplier crossing,

\[
\boxed{
A_{n+1}-A_n
=\sigma\varepsilon A_n+cA_n^3
+O(|A|^5+|\varepsilon|A^3+\varepsilon^2|A|).
}
\tag{N17}
\]

The multiplier transversality coefficient is most robustly defined as

\[
\boxed{
\sigma=\left.\frac{d\mu_c}{dp}\right|_{p_*}
=p^*\dot L\,q,
}
\tag{N18}
\]

where `dot L` is the derivative of the return-map linearisation **along the symmetric base branch**.

Let `Q_s` denote projection onto the stable complement and `L_s` the restricted stable operator. The quadratic slaved correction is

\[
\boxed{
h_2
=(I-L_s)^{-1}\frac12Q_sB(q,q).
}
\tag{N19}
\]

With the Taylor convention (N9), the cubic coefficient is

\[
\boxed{
c
=p^*B(q,h_2)
+\frac16p^*C(q,q,q).
}
\tag{N20}
\]

A generic dynamic pitchfork requires

\[
\boxed{\sigma\ne0,\qquad c\ne0.}
\tag{N21}
\]

The symmetry-broken fixed points obey

\[
\boxed{
A^2\sim-\frac{\sigma}{c}\varepsilon.
}
\tag{N22}
\]

The derivative of the reduced map on the broken branch is

\[
D_A\mathscr P_{\rm red}
=1+\sigma\varepsilon+3cA^2+\cdots
=1-2\sigma\varepsilon+\cdots.
\tag{N23}
\]

Therefore the sign of `sigma*epsilon`, together with `c`, determines which side contains the small broken branches and their local center-direction stability.

### Two-cell interpretation

For the symmetric two-cell system of v0.3/v0.4,

\[
q\propto(1,-1)^T
\]

is the natural antisymmetric spike-time mode. Its amplitude `A` is the local synergetic order parameter for symmetry breaking.

The v0.3 existence pitchfork coefficient and the v0.5 dynamic coefficient are related diagnostics but are not identical by definition: one comes from the branch residual, the other from the return map. At a genuine periodic-orbit pitchfork they must predict the same branch geometry and critical symmetry sector.

---

# 6. Flip / period-doubling mode

Assume a simple real critical multiplier

\[
\mu_c=-1.
\]

After the standard removal of nonresonant quadratic terms, the scalar center map can be written

\[
\boxed{
A_{n+1}=-(1+\sigma\varepsilon)A_n+c_fA_n^3
+O(|A|^4+|\varepsilon|A^2).
}
\tag{N24}
\]

With convention (N9), a standard cubic coefficient is

\[
\boxed{
c_f
=\frac16p^*C(q,q,q)
+\frac12p^*B\!\left(q,(I-L)^{-1}B(q,q)\right).
}
\tag{N25}
\]

The inverse exists at a generic flip because `+1` is not a nontrivial multiplier of the gauge-fixed map at the same point.

A sign-alternating physical perturbation is

\[
\delta y_n\sim(-1)^nA_nq.
\tag{N26}
\]

Equivalently, the second iterate has a near-unit multiplier and a slowly varying envelope. The newly born period-two event pattern has the usual square-root amplitude scaling. CORE should compare the coefficient prediction against a directly continued period-two branch, not merely against transient simulations.

If another nontrivial `+1` multiplier is simultaneously present, `(I-L)^{-1}` becomes singular and the codimension-two fold/flip or pitchfork/flip normal form must be used instead.

---

# 7. Neimark--Sacker / oscillatory timing mode

Assume a simple complex-conjugate pair

\[
\mu_{1,2}=e^{\pm i\Omega},
\qquad 0<\Omega<\pi,
\tag{N27}
\]

crosses the unit circle and is away from low-order strong resonance.

Let

\[
Lq=e^{i\Omega}q,
\qquad
p^*L=e^{i\Omega}p^*,
\qquad p^*q=1.
\tag{N28}
\]

Define the slaved second-order corrections

\[
\boxed{
h_{20}
=(e^{2i\Omega}I-L)^{-1}B(q,q),}
\tag{N29}
\]

\[
\boxed{
h_{11}
=(I-L)^{-1}B(q,\bar q).}
\tag{N30}
\]

Then

\[
\boxed{
G_{21}
=p^*\left[
C(q,q,\bar q)
+B(\bar q,h_{20})
+2B(q,h_{11})
\right].
}
\tag{N31}
\]

The first Lyapunov coefficient in this convention is

\[
\boxed{
\ell_1
=\frac12\operatorname{Re}\!\left(e^{-i\Omega}G_{21}\right).
}
\tag{N32}
\]

A local complex-amplitude form is

\[
Z_{n+1}
=e^{i\Omega}
\left[(1+\sigma\varepsilon)Z_n
+gZ_n|Z_n|^2+\cdots\right],
\tag{N33}
\]

with radial cubic part determined by `ell_1` after the chosen normalisation.

The rotating-carrier representation

\[
Z_n=e^{in\Omega}A_n
\tag{N34}
\]

reveals a slowly varying envelope `A_n` near onset. This complex envelope is the synergetic order parameter for an oscillatory modulation of spike timing.

### Reporting rule

Do not label a Neimark--Sacker branch merely from the sign of `ell_1`. Report together:

1. the radial crossing speed `d|mu|/dp`;
2. `ell_1` and its coefficient convention;
3. the critical angle `Omega`;
4. distance to strong resonances;
5. the symmetry/Fourier sector of `q`.

Strong resonances such as `e^{ik Omega}=1` at low order require resonant normal forms rather than (N29)--(N33).

---

# 8. Ring Fourier modes as synergetic order parameters

For a ring, v0.4 gives perturbation sectors

\[
\xi_i^{(q)}=e^{i\kappa_q i},
\qquad
\kappa_q=\frac{2\pi q}{N}.
\tag{N35}
\]

If sector `q` is critical, the leading spike-time perturbation is

\[
\boxed{
\delta T_i^m
\approx
A_q\mu^m e^{i\kappa_q i}
+\bar A_q\bar\mu^m e^{-i\kappa_q i}.
}
\tag{N36}
\]

For a steady/unit crossing `mu=1`, this reduces to the real spatial timing pattern

\[
\delta T_i
\approx2\operatorname{Re}\!\left(A_qe^{i\kappa_q i}\right).
\tag{N37}
\]

Thus `A_q` is a direct order parameter for the emergence of a timing pattern with wave number `q`.

## 8.1 Action of cyclic symmetry

Under a one-node rotation,

\[
\boxed{A_q\mapsto e^{i\kappa_q}A_q.}
\tag{N38}
\]

If reflection belongs to the isotropy of the actual delayed locked state, it acts as

\[
\boxed{A_q\mapsto\bar A_q.}
\tag{N39}
\]

Let

\[
\boxed{m_q=\frac{N}{\gcd(N,q)}}
\tag{N40}
\]

be the order of the cyclic representation generated by sector `q`.

Cyclic equivariance constrains monomials in the amplitude equation. A monomial `A^r \bar A^s` is allowed in the `A` equation only if

\[
r-s\equiv1\pmod{m_q}.
\tag{N41}
\]

Consequently, the lowest discrete anisotropy term is generically

\[
\bar A^{m_q-1}.
\]

A schematic steady-mode amplitude equation is therefore

\[
\boxed{
\Delta A
=\sigma\varepsilon A
+cA|A|^2
+d\bar A^{m_q-1}
+\cdots,
}
\tag{N42}
\]

with only terms of the appropriate asymptotic order retained.

This yields a useful classification:

- `m_q=2`: the representation is real and the problem reduces to a `Z_2` pitchfork-type scalar amplitude;
- `m_q=3`: quadratic anisotropy `\bar A^2` is allowed;
- `m_q=4`: cubic anisotropy `\bar A^3` competes directly with `A|A|^2`;
- `m_q>=5`: the cubic truncation is effectively continuous-phase (`O(2)`-like); discrete phase selection first enters at order `m_q-1>=4`.

This is a concrete mode-selection prediction that can be tested on finite Lighthouse rings.

For a twisted base state, continue to distinguish

- `q_0`: base-state winding;
- `q`: perturbation/order-parameter sector.

The relevant symmetry action is that of the isotropy/co-rotating symmetry of the chosen `q_0` branch, not automatically the full symmetry of the underlying ring graph.

---

# 9. Two real critical modes: competition and coexistence

Suppose two independent real unit modes become weak at the same parameter point. After symmetry reduction, let their amplitudes be `A` and `B` and assume independent sign symmetries exclude quadratic terms.

On the slow cycle scale, the generic cubic amplitude system is

\[
\boxed{
\Delta A
=A\left(\mu_1+a_{11}A^2+a_{12}B^2\right)+\cdots,
}
\tag{N43}
\]

\[
\boxed{
\Delta B
=B\left(\mu_2+a_{21}A^2+a_{22}B^2\right)+\cdots.
}
\tag{N44}
\]

The reduced equilibria are:

1. trivial: `A=B=0`;
2. pure `A`: `A^2=-mu_1/a_11`, `B=0`;
3. pure `B`: `B^2=-mu_2/a_22`, `A=0`;
4. mixed mode: solve

\[
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}A^2\\B^2\end{pmatrix}
=-
\begin{pmatrix}\mu_1\\\mu_2\end{pmatrix}.
\tag{N45}
\]

The interaction determinant

\[
\boxed{\Delta_c=a_{11}a_{22}-a_{12}a_{21}}
\tag{N46}
\]

controls whether the cubic truncation admits a locally unique mixed branch. The cross-couplings distinguish competitive mode exclusion from coexistence.

For rings, `A` and `B` can be amplitudes of two different Fourier sectors. A switch in the v0.4 leading sector `q_*(p)` is therefore only the linear precursor; v0.5 coefficients determine whether the nonlinear outcome is winner-take-all, bistability, or a mixed timing pattern.

---

# 10. Steady--oscillatory and oscillatory--oscillatory interactions

## 10.1 Real unit mode plus Neimark--Sacker pair

Let `A` be a real steady order parameter and `Z` a complex oscillatory amplitude. Away from resonances and with `A -> -A` symmetry, a generic slow normal form is

\[
\boxed{
\Delta A
=A\left(\mu_A+aA^2+b|Z|^2\right)+\cdots,
}
\tag{N47}
\]

\[
\boxed{
\Delta Z
=Z\left[(\mu_Z+i\omega_1)+c|Z|^2+dA^2\right]+\cdots.
}
\tag{N48}
\]

This is the event-map analogue of a steady/Hopf or Turing/Hopf interaction: a static timing pattern and an oscillatory timing modulation compete or coexist.

## 10.2 Two oscillatory modes

For two nonresonant complex amplitudes,

\[
\boxed{
\Delta Z_1
=Z_1\left[(\mu_1+i\omega_1)
+a_{11}|Z_1|^2+a_{12}|Z_2|^2\right]+\cdots,
}
\tag{N49}
\]

\[
\boxed{
\Delta Z_2
=Z_2\left[(\mu_2+i\omega_2)
+a_{21}|Z_1|^2+a_{22}|Z_2|^2\right]+\cdots.
}
\tag{N50}
\]

Additional resonant terms must be included whenever temporal frequencies and spatial representation phases satisfy low-order selection rules.

---

# 11. Codimension-two detection rules

CORE v0.5 recognises at least the following candidate codimension-two points after removal of the global shift mode:

- `+1 / +1`: two independent nontrivial unit modes;
- `+1 / -1`: fold/flip or symmetry-breaking/flip;
- `+1 / NS`: steady--oscillatory interaction;
- `-1 / NS`: flip--oscillatory interaction;
- `NS / NS`: two critical complex pairs;
- spatial mode degeneracy: two different symmetry/Fourier sectors critical together.

A codimension-two label requires more than two numerically nearby multipliers. Store:

\[
(\mu_1,\mu_2,\text{right/left modes},\text{sector labels},
\text{conditioning},\text{parameter transversality}).
\tag{N51}
\]

For rings, mode labels are part of the bifurcation type. `q=1`/`q=2` competition is not equivalent to a repeated eigenvalue inside one irreducible sector.

---

# 12. Adaptive delays as slow variables

The 2026 adaptive-delay Lighthouse work motivates a slow--fast extension. Let `d` denote one or several conduction-delay variables and let `epsilon << 1` be the adaptation/time-scale ratio.

Near a frozen critical branch, the reduced cycle dynamics has the canonical form

\[
\boxed{
A_{n+1}-A_n=f(A,\bar A;d_n,p)+\cdots,
}
\tag{N52}
\]

\[
\boxed{
d_{n+1}-d_n
=\epsilon G(A,\bar A,d_n,p)+\cdots.
}
\tag{N53}
\]

The coefficients of `f` are the frozen-delay normal-form coefficients from the preceding sections and therefore vary with `d`.

For a simple symmetry-breaking mode, a minimal slow-fast model is

\[
\boxed{
\Delta A
=\sigma(d-d_c)A-cA^3+\cdots,
}
\tag{N54}
\]

\[
\boxed{
\Delta d
=\epsilon G(A,d)+\cdots.
}
\tag{N55}
\]

Interpretation:

- `A` is the fast critical collective order parameter;
- `d` is a slowly adapting structural variable/control parameter;
- stable frozen phase-locked branches define slow manifolds followed by the adaptive system;
- loss of frozen stability or admissibility can trigger jumps to another branch;
- branch hysteresis plus slow delay drift can generate long-time switching.

This supplies a direct synergetic interpretation of the frozen-branch organisation observed in adaptive-delay Lighthouse networks.

A delay variable may itself become part of the center/critical set if its evolution loses hyperbolicity. CORE will not label delays as order parameters by default.

---

# 13. Coefficient extraction for a hybrid Lighthouse system

Normal-form coefficients must include event-time sensitivities. Three routes are admissible.

## Route A — explicit gauge-fixed return map

Construct `P_p` by exact event integration on a fixed itinerary. Differentiate the complete event map, including event-time dependence and jump/saltation terms.

This is the preferred small-system reference.

## Route B — implicit spike-time / Lyapunov--Schmidt reduction

Work directly with an event-time residual over one or several cycles and eliminate stable directions using left/right nullvectors and homological equations.

This avoids constructing a large history-space return matrix and is attractive for delayed networks.

## Route C — constrained local identification

Fit the normal-form coefficients from carefully designed perturbations of the exact event simulator while enforcing the known symmetry and resonance structure.

Route C is a validation/estimation method, not the sole mathematical source of truth.

### Cross-validation requirement

At least one benchmark in every codimension-one class should compare two independent coefficient routes. Agreement must improve under step-size/event-tolerance refinement.

### Forbidden shortcut

For the exact alpha/event model, automatic differentiation through `mod`, `floor`, unsplit arrival boundaries, or a smoothed spike surrogate does not constitute an exact hybrid derivative. Smooth surrogates may be studied separately, with quantified coefficient error relative to the exact-event reference.

---

# 14. Validity boundaries

The smooth normal forms above are not valid without modification when any of the following occurs at the same asymptotic scale:

1. event transversality is lost: `nu_min -> 0`;
2. a delayed arrival collides with an event boundary and changes the itinerary;
3. the response function crosses a nonsmooth threshold surface;
4. simultaneous spikes require a different jump ordering convention;
5. there is no spectral gap between the chosen center set and additional weak modes;
6. a Neimark--Sacker pair approaches a strong low-order resonance;
7. a nonlinear eigenvalue is nearly multiple/defective and conditioning diverges.

In those cases enlarge the critical set or use nonsmooth/hybrid bifurcation theory rather than forcing a low-dimensional smooth amplitude equation.

---

# 15. CORE v0.5 implementation objects

The mathematical layer should expose conceptually:

- `critical_modes(locked_state, parameters)`;
- `return_map_derivatives(order=3, itinerary=...)`;
- `center_projectors(critical_modes)`;
- `slaving_coefficients(...)`;
- `fold_normal_form(...)`;
- `pitchfork_normal_form(...)`;
- `flip_normal_form(...)`;
- `neimark_sacker_normal_form(...)`;
- `ring_equivariant_normal_form(q0, q, ...)`;
- `codim2_mode_interaction(...)`;
- `adaptive_reduced_system(...)`;
- `normal_form_vs_full_error(...)`.

Every coefficient record should include:

- branch point and parameter values;
- critical multiplier(s);
- left/right critical vectors;
- symmetry/Fourier sector;
- coefficient convention;
- event itinerary identifier;
- transversality/admissibility margins;
- spectral gap and conditioning;
- derivative method and numerical tolerances.

---

# 16. Main hypotheses opened by v0.5

### H5.1 — Lighthouse critical modes are explicit synergetic order parameters

The amplitude of a critical spike-time mode should quantitatively organise the emerging collective timing pattern near instability, with stable microscopic timing/history directions slaved to it.

### H5.2 — Fourier-mode competition predicts network pattern selection

For rings and other symmetric graphs, linear Floquet sectors identify candidate patterns while cubic cross-couplings decide selection, coexistence, and bistability.

### H5.3 — discrete ring symmetry leaves measurable anisotropy fingerprints

The representation order `m_q=N/gcd(N,q)` predicts the first symmetry-allowed phase-pinning term and therefore finite-size deviations from the continuum/O(2)-like amplitude equation.

### H5.4 — adaptive delay dynamics can be reduced to slow drift of normal-form coefficients

When adaptation is slow and frozen branches are normally hyperbolic, a low-dimensional fast-order-parameter/slow-delay system should reproduce branch following and switching seen in the full adaptive Lighthouse network.

### H5.5 — event-derived and smooth-surrogate normal forms need not agree automatically

A differentiable JAX surrogate may shift critical parameters and cubic coefficients even if trajectories look similar. Normal-form coefficients provide a sensitive quantitative measure of surrogate fidelity.

---

# 17. References

1. H. Haken, *Slaving principle revisited*, Physica D 97 (1996), 95--103, DOI: 10.1016/0167-2789(96)00080-2.
2. H. Haken, *Brain Dynamics: Synchronization and Activity Patterns in Pulse-Coupled Neural Nets with Delays and Noise*, Springer, 2002.
3. Yu. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer. Standard center-manifold and normal-form conventions for maps, including flip and Neimark--Sacker bifurcations.
4. S. Coombes, *Revisiting the Haken Lighthouse model*, European Physical Journal Special Topics 235 (2026), 4571--4593, DOI: 10.1140/epjs/s11734-025-01841-3.
5. S. Coombes, R. Thul, S. Ruschel, R. Nicks, *Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks*, arXiv:2606.21508 (2026).

The formulas in this document define the CORE project convention and should be validated independently on benchmark maps and exact event simulations before v1.0 freeze.
