# CORE normal-form benchmark contract v0.5

## Purpose

This contract turns `order_parameter_normal_forms_v0.5.md` into falsifiable numerical and symbolic tests. A v0.5 implementation is not considered CORE-valid because it produces plausible bifurcation diagrams. It must reproduce symmetry, scaling, coefficient, slaving, and full-vs-reduced dynamics checks.

The contract continues the benchmark numbering used by v0.2--v0.4.

---

# B41 — Critical-mode/order-parameter identification

For a branch point with one simple nontrivial critical multiplier `mu_c`, verify that the perturbation of the exact event dynamics projects predominantly onto the corresponding right mode `q` over the linear regime.

Required outputs:

- `mu_c`;
- right/left modes `q,p` with `p^* q = 1`;
- global-shift overlap diagnostic;
- symmetry/Fourier sector;
- nonlinear-eigenvalue conditioning;
- stable spectral gap estimate.

Pass condition:

The identified order-parameter amplitude

\[
A=p^*(y-y_*)
\]

predicts the leading perturbation evolution to first order, and the residual after reconstructing `A q` is asymptotically smaller than the perturbation norm.

---

# B42 — Slaving reconstruction

At a simple unit-mode problem away from nonsmooth boundaries, compute the quadratic stable correction

\[
h_2=(I-L_s)^{-1}\frac12Q_sB(q,q).
\]

Compare the full event-state perturbation with

\[
y-y_*=Aq+h_2A^2.
\]

Pass condition:

For a sequence `A -> 0`, the reconstruction residual scales at least cubically,

\[
\|y-y_*-Aq-h_2A^2\|=O(|A|^3),
\]

within numerical differentiation/event-location error.

---

# B43 — Dynamic pitchfork parity and square-root scaling

Use an exchange-symmetric two-cell or equivalent `Z_2` benchmark with an antisymmetric nontrivial unit multiplier.

Verify numerically that the reduced center increment is odd:

\[
\Delta A(-A,\varepsilon)
=-\Delta A(A,\varepsilon)
+o(\text{fitted order}).
\]

Fit or derive

\[
\Delta A=\sigma\varepsilon A+cA^3+\cdots.
\]

Pass conditions:

1. even center terms vanish at the expected convergence rate;
2. `sigma != 0`, `c != 0` for the chosen generic benchmark;
3. continued broken branches satisfy

\[
A^2\sim-\frac{\sigma}{c}\varepsilon;
\]

4. the critical dynamic sector agrees with the antisymmetric existence sector at the periodic-orbit pitchfork.

---

# B44 — Existence-pitchfork versus return-map pitchfork

At the same `Z_2` critical point, compare:

- v0.3 branch-residual coefficients `(a,b)`;
- v0.5 return-map coefficients `(sigma,c)`.

They need not be numerically identical because of coordinate conventions.

Pass condition:

After converting to the same branch parameter and order-parameter normalisation, both descriptions predict:

- the same critical parameter;
- the same side of branch emergence;
- the same square-root exponent;
- the same symmetry sector.

A disagreement is a failed cross-layer validation, not a harmless convention difference.

---

# B45 — Flip coefficient and period-two branch

Choose a benchmark with a simple nontrivial multiplier crossing `mu=-1` and no simultaneous `+1` criticality.

Compute

\[
c_f
=\frac16p^*C(q,q,q)
+\frac12p^*B\!\left(q,(I-L)^{-1}B(q,q)\right).
\]

Continue the period-two event orbit born at the flip.

Pass conditions:

1. the event perturbation alternates sign according to the critical mode;
2. the period-two amplitude has square-root onset;
3. the branch side and local stability agree with the reduced second-iterate prediction;
4. the coefficient converges under derivative/event-tolerance refinement.

---

# B46 — Neimark--Sacker coefficient

Choose a benchmark with a simple nonresonant pair

\[
\mu_{1,2}=e^{\pm i\Omega}.
\]

Compute

\[
h_{20}=(e^{2i\Omega}I-L)^{-1}B(q,q),
\]

\[
h_{11}=(I-L)^{-1}B(q,\bar q),
\]

\[
G_{21}=p^*[C(q,q,\bar q)+B(\bar q,h_{20})+2B(q,h_{11})],
\]

\[
\ell_1=\frac12\operatorname{Re}(e^{-i\Omega}G_{21}).
\]

Required outputs:

- `Omega`;
- `d|mu|/dp`;
- `ell_1`;
- distance to the nearest low-order resonance;
- critical symmetry sector.

Pass condition:

The invariant-circle/modulation amplitude close to onset agrees with the radial normal-form scaling and branch direction after accounting for the measured crossing orientation.

---

# B47 — Strong-resonance guard

For every Neimark--Sacker candidate, compute at least

\[
d_k=|e^{ik\Omega}-1|,
\qquad k=1,2,3,4.
\]

Pass condition:

A generic NS coefficient is not reported as sufficient when any `d_k` lies below the configured resonance tolerance. The point must be relabelled for resonant analysis.

---

# B48 — Ring-mode reconstruction

For a critical ring sector `q`, reconstruct the physical timing perturbation from

\[
\delta T_i^m
\approx
A_q\mu^m e^{i2\pi qi/N}
+\bar A_q\bar\mu^m e^{-i2\pi qi/N}.
\]

Pass conditions:

1. the dense v0.4 eigenvector agrees with the Fourier reconstruction;
2. rotation by one node changes the amplitude by the predicted representation phase;
3. if reflection belongs to the base-state isotropy, reflection maps `A_q` to its conjugate within numerical tolerance.

---

# B49 — Cyclic anisotropy selection rule

For

\[
m_q=\frac{N}{\gcd(N,q)},
\]
verify the monomial selection rule

\[
r-s\equiv1\pmod{m_q}
\]

for the fitted/derived amplitude map.

Minimum test cases:

- `m_q=2`: real `Z_2` sector;
- `m_q=3`: allowed quadratic anisotropy `\bar A^2`;
- `m_q=4`: allowed cubic anisotropy `\bar A^3`;
- `m_q>=5`: no discrete anisotropy through cubic order.

Pass condition:

Forbidden coefficients converge to zero under refinement while symmetry-allowed coefficients remain invariant under the cyclic group action.

---

# B50 — Finite-ring to continuum normal-form limit

Construct a sequence of rings with increasing `N` under a documented continuum weight/delay normalisation. Track a fixed physical wave number represented by discrete sectors `q_N`.

Pass conditions:

1. the critical multiplier and onset parameter converge;
2. the cubic isotropic coefficient `A|A|^2` converges;
3. when `m_q -> infinity`, low-order discrete anisotropy disappears consistently with the v0.5 symmetry rule;
4. the limit agrees with the v0.4 continuum dispersion relation at linear order.

---

# B51 — Two-mode competition

Choose or construct a codimension-two benchmark with two real critical symmetry sectors.

Fit/derive

\[
\Delta A=A(\mu_1+a_{11}A^2+a_{12}B^2),
\]

\[
\Delta B=B(\mu_2+a_{21}A^2+a_{22}B^2).
\]

Pass conditions:

- pure-mode branch directions agree with `a_11,a_22`;
- mixed-mode existence agrees with the linear system for `(A^2,B^2)`;
- the interaction determinant

\[
\Delta_c=a_{11}a_{22}-a_{12}a_{21}
\]

correctly predicts local uniqueness/degeneracy of the cubic mixed solution;
- full-event simulations/continuation distinguish competition, coexistence, or bistability as predicted locally.

---

# B52 — Codimension-two sector bookkeeping

At any candidate codimension-two point, store both critical modes with:

- multiplier;
- right/left vector;
- symmetry/Fourier sector;
- eigenvalue conditioning;
- parameter crossing directions.

Pass condition:

A repeated or nearly repeated multiplier is not labelled as two-mode interaction until the geometric/sector structure shows two independent critical directions.

---

# B53 — Adaptive-delay frozen-branch reduction

For a slow adaptive-delay example, first freeze the delay `d` and compute the locked branch and normal-form coefficients as functions of `d`.

Construct

\[
\Delta A=f(A;d),
\qquad
\Delta d=\epsilon G(A,d).
\]

Pass conditions as `epsilon -> 0`:

1. the full adaptive trajectory remains close to attracting frozen branches away from loss of normal hyperbolicity;
2. the reduced model predicts the direction of slow drift;
3. transitions occur near the appropriate frozen stability/admissibility boundary, with the expected finite-`epsilon` delay;
4. reducing `epsilon` improves agreement on the slow time scale.

---

# B54 — Order parameter versus slow control variable

In an adaptive-delay benchmark, separately compute the critical fast mode amplitude `A` and the delay variable `d`.

Pass condition:

Documentation and APIs do not conflate them. `d` may only be promoted into the critical/order-parameter set when its own slow dynamics becomes nonhyperbolic or participates in a center manifold at the same asymptotic order.

---

# B55 — Independent coefficient routes

For at least one example in each implemented class (`+1`, flip, NS), compute coefficients by two independent methods selected from:

1. explicit event-return-map derivatives;
2. implicit spike-time/Lyapunov--Schmidt reduction;
3. symmetry-constrained local identification from exact-event data.

Pass condition:

Coefficient disagreement decreases under tolerance/refinement and is smaller than the documented target error before the coefficient is used scientifically.

---

# B56 — Exact-event versus differentiable-surrogate normal form

For any smooth JAX surrogate used for differentiation, compute the same critical parameter and normal-form coefficients in both:

- the exact hybrid/event model;
- the smooth surrogate.

Report

\[
\Delta p_c,
\qquad
\Delta\mu_c,
\qquad
\Delta c,
\qquad
\Delta\ell_1
\]

as applicable.

Pass condition:

The surrogate is not called quantitatively faithful merely because time traces look similar. A documented tolerance must be satisfied for the bifurcation observables actually used in inference or optimisation.

---

# B57 — Smooth-normal-form validity guard

At every coefficient evaluation, store:

\[
\nu_{\min},
\]

the minimum distance to an arrival collision, threshold switching surface, simultaneous-event ambiguity, and the stable spectral gap/conditioning.

Pass condition:

The smooth normal form is automatically flagged invalid or provisional if:

- `nu_min` is below transversality tolerance;
- an arrival/event itinerary changes inside the differentiation stencil;
- an additional multiplier enters the center tolerance;
- a required homological inverse is ill-conditioned;
- a strong temporal/spatial resonance invalidates the generic coefficient formula.

---

# B58 — Reduced/full prediction horizon

For each normal form, compare full event dynamics with reduced amplitude dynamics for initial amplitudes `A_0 -> 0` and parameters `epsilon -> 0`.

Required measurements:

- amplitude error per cycle;
- phase error for complex modes;
- reconstruction error in spike times;
- horizon over which a fixed relative error tolerance is maintained.

Pass condition:

The agreement horizon increases as the asymptotic regime is approached. This test prevents a locally correct coefficient from being overinterpreted far from onset.

---

# Minimum v0.5 acceptance set

A code release may claim **CORE-normal-form-v0.5** only after passing at least:

- B41 critical mode;
- B42 slaving;
- B43 pitchfork;
- B45 flip;
- B46 and B47 Neimark--Sacker;
- B48 and B49 ring symmetry;
- B55 independent coefficient routes;
- B57 validity guard.

Adaptive-delay claims additionally require B53 and B54.

Codimension-two/mode-selection claims additionally require B51 and B52.

Surrogate-gradient claims additionally require B56.

---

# Data record schema

Every stored normal-form result should contain conceptually:

```text
branch_id
parameter_point
locked_state_id
event_itinerary_id
critical_multipliers
critical_right_modes
critical_left_modes
symmetry_sectors
neutral_mode_residual
conditioning
stable_spectral_gap
transversality_margin
arrival_margin
resonance_margins
coefficient_convention
derivative_method
derivative_tolerances
normal_form_coefficients
cross_validation_error
full_vs_reduced_error
validity_flags
```

The purpose of this record is reproducibility: a coefficient without its event itinerary, mode normalisation, derivative convention, and conditioning is not a reusable scientific result.
