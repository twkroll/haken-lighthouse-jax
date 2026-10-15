# CORE continuation benchmark contract v0.3

## Scope

This file specifies the reference tests required before continuation or bifurcation results are considered CORE-valid. It extends the v0.2 analytical benchmark suite.

Each benchmark is labelled as one of:

- **EXACT** — equality should converge to numerical precision/tolerance;
- **PIECEWISE-EXACT** — equality is exact inside a fixed event/arrival itinerary;
- **STRUCTURAL** — checks symmetry, invariance, rank, or classification rather than a scalar closed form;
- **ASYMPTOTIC** — checks a controlled limiting law.

The continuation implementation must never silently replace an exact benchmark by a smoothed surrogate.

---

# B11 — dimensional versus normalised phase coordinates

**Class:** EXACT

Use both locked-state conventions

\[
T_i^m=mT+\phi_i
\]

and

\[
T_i^m=(m+\chi_i)T,
\qquad \phi_i=T\chi_i.
\]

For the same physical branch point, evaluate the v0.2 dimensional-offset equations and the v0.3 normalised-offset equations.

Acceptance:

\[
\boxed{\|F^{(\phi)}-F^{(\chi)}\|_\infty<\varepsilon_F.}
\]

Also verify invariance under

\[
\chi_i\mapsto\chi_i+c
\]

before gauge fixing.

Recommended default:

`eps_F <= 1e-10` in float64 for smooth moderate parameter cases.

---

# B12 — branch Jacobian

**Class:** PIECEWISE-EXACT

At a regular point whose arrival ordering and threshold-active intervals are fixed, compare

\[
D_zF
\]

from the analytic/autodiff branch implementation with centered finite differences.

For coordinate `z_k`, use a sequence of step sizes `h_n` and require the error to exhibit the expected convergence before roundoff dominates.

Acceptance should be based on both absolute and relative error:

\[
\boxed{
|J_{ik}^{\rm ref}-J_{ik}^{\rm fd}|
\le
\varepsilon_{\rm abs}
+\varepsilon_{\rm rel}|J_{ik}^{\rm ref}|.
}
\]

The test point must be separated from:

- arrival collisions;
- threshold contacts;
- event grazing;
- wrapped phase chart boundaries.

A direct autodiff-through-`mod` result is not accepted as the reference derivative for the exact alpha kernel.

---

# B13 — pseudo-arclength fold traversal

**Class:** EXACT algorithmic

First validate the continuation engine independently of Lighthouse dynamics on

\[
F(x,p)=x^2-p=0.
\]

Start on either regular branch and continue through the turning point using pseudo-arclength.

Required checks:

1. the solver crosses the point `(x,p)=(0,0)` without parameter-step failure;
2. the augmented Newton matrix remains solvable at the fold;
3. the detected right nullvector of `F_x` agrees with the fold tangent direction;
4. local scaling satisfies

\[
|x|\sim |p|^{1/2}.
\]

Then repeat on at least one Lighthouse branch with an observed fold.

A continuation implementation that only uses parameter stepping fails B13 by definition.

---

# B14 — exchange-symmetric two-cell block diagonalisation

**Class:** STRUCTURAL / PIECEWISE-EXACT

Use

\[
W=\begin{pmatrix}w_s&w_c\\w_c&w_s\end{pmatrix}
\]

with symmetric self/cross delays and common response function.

At synchrony `chi=0`, verify

\[
F_-(T,0)=0,
\]

\[
\partial_\chi F_+(T,0)=0,
\]

\[
\partial_TF_-(T,0)=0.
\]

Hence the transformed Jacobian must satisfy

\[
\boxed{
D(F_+,F_-)
=\begin{pmatrix}A&0\\0&B\end{pmatrix}
}
\]

within numerical tolerance.

Also compare `B` with the explicit integral

\[
\boxed{
B=-T^2w_c\int_0^1
S'(\Psi_0)
R_T'(T\sigma-\tau_c)d\sigma.
}
\]

This is the primary Lighthouse-specific v0.3 Jacobian benchmark.

---

# B15 — pitchfork coefficient and square-root scaling

**Class:** EXACT normal-form / STRUCTURAL Lighthouse

Validate the generic symmetry-breaking machinery first on

\[
F_+(T,\chi,p)=T-T_0,
\]

\[
F_-(T,\chi,p)=\chi(p-\chi^2).
\]

At `p=0`, the code must identify:

- synchronous branch `chi=0`;
- antisymmetric zero mode;
- two broken-symmetry branches for `p>0`;
- scaling

\[
|\chi|=\sqrt p.
\]

For a Lighthouse two-cell pitchfork, compare measured branch direction against

\[
\chi^2\sim-\frac{a}{b}(p-p_*),
\]

with

\[
a=F_{-,\chi p}
-\frac{F_{-,\chi T}F_{+,p}}{F_{+,T}},
\]

\[
b=\frac16F_{-,\chi\chi\chi}
-\frac{F_{-,\chi T}F_{+,\chi\chi}}{2F_{+,T}}.
\]

Acceptance: fitted `chi^2` versus `p-p_*` slope must converge toward `-a/b` as the fit window shrinks.

---

# B16 — existence/stability separation

**Class:** STRUCTURAL

For every continued branch point store independently:

\[
\sigma_{\min}(D_zF)
\]

and the leading nontrivial dynamic multiplier/root.

The implementation must permit all four logical combinations:

1. regular existence + dynamically stable;
2. regular existence + dynamically unstable;
3. singular/near-singular existence + dynamically stable on one side;
4. singular/near-singular existence + dynamically unstable.

No code path may infer stability from the condition number of `D_zF`.

Unit-test the classifier using synthetic multiplier sets containing:

- trivial `mu=1` plus stable roots;
- nontrivial `mu=1`;
- `mu=-1`;
- complex unit pair `exp(+-i Omega)`;
- unstable `|mu|>1`.

Expected labels are respectively:

- stable after neutral-mode exclusion;
- unit/steady critical;
- `PD`;
- `NS`;
- unstable.

---

# B17 — event-transversality singularity

**Class:** ASYMPTOTIC / EXACT scaling

For a controlled event with crossing speed `nu`, event-time sensitivity satisfies

\[
\delta T=-\frac{\delta\theta}{\nu}.
\]

Choose a sequence `nu_n -> 0+` with fixed nonzero `delta theta`.

Acceptance:

\[
\boxed{
|\delta T|\,\nu\to|\delta\theta|.
}
\]

For the alpha-synapse saltation matrix, track an entry proportional to `1/nu` and require the same scaling.

The branch point must be labelled `EV_GRAZE` when the configured transversality tolerance is crossed, regardless of whether the branch Newton residual is small.

---

# B18 — arrival-aware quadrature and derivative jump

**Class:** PIECEWISE-EXACT

For the alpha kernel, construct a locked orbit with known arrival phases

\[
a_{ij}=\left(\chi_j-\chi_i+\frac{\tau_{ij}}{T}\right)\bmod1.
\]

Split quadrature exactly at all unique arrival phases.

Checks:

1. the split integral agrees with a high-resolution independent integral;
2. moving an arrival without changing ordering yields convergent smooth sensitivities;
3. one-sided Jacobians approaching an arrival-order collision converge to their respective limits;
4. the code emits `ARR_COLL` when the ordering margin crosses tolerance.

The test should explicitly demonstrate that `R_T` is continuous while `R_T'` has the expected jump for the alpha kernel.

---

# B19 — threshold-contact detection

**Class:** STRUCTURAL / PIECEWISE-EXACT

For a thresholded response `S`, define

\[
H_i(\sigma)=\Psi_i(\sigma)-h.
\]

Construct cases with:

1. transverse threshold crossing;
2. no threshold crossing;
3. tangential contact satisfying approximately

\[
H_i(\sigma_*)=0,
\qquad
\partial_\sigma H_i(\sigma_*)=0.
\]

The third case must be labelled `TH_GRAZE` and must force the exact continuation layer to rebuild/split its active intervals.

---

# B20 — frozen-branch implicit sensitivity

**Class:** PIECEWISE-EXACT

On a regular delay-continued branch

\[
F(z,\tau)=0,
\]

compute

\[
q=-(D_zF)^{-1}F_\tau.
\]

Compare against centered finite differences of nearby converged branch points:

\[
q_{\rm fd}
=\frac{z_*(\tau+h)-z_*(\tau-h)}{2h}.
\]

Acceptance:

\[
\boxed{
\|q-q_{\rm fd}\|
\to0
}
\]

under step refinement away from folds/hybrid boundaries.

Track simultaneously

\[
\sigma_{\min}(D_zF).
\]

As a fold is approached, large branch sensitivity should correlate with loss of invertibility rather than be silently clipped.

---

# B21 — commensurability crossing

**Class:** EXACT diagnostic

For any continued delay `tau_ij`, calculate

\[
C_{ij}^{(k)}=\tau_{ij}-kT
\]

for a configured integer range `k`.

When a branch crosses `C=0`, locate the crossing by interpolation/root refinement and verify

\[
\boxed{|\tau_{ij}-kT|<\varepsilon_C.}
\]

Store the corresponding phase offsets, stability label, and slow-plasticity drift if an adaptive rule is active.

This benchmark connects the fixed-delay continuation layer to the adaptive-delay research programme.

---

# B22 — first-hitting admissibility

**Class:** EXACT event itinerary

For every candidate one-spike-per-cycle locked solution define

\[
\Theta_i(\sigma)
=T\int_0^\sigma S_i(\Psi_i(\xi))d\xi.
\]

The event itinerary is valid only if the first solution of

\[
\Theta_i(\sigma)=2\pi
\]

occurs at `sigma=1` for every neuron.

Acceptance requires an independent root/event search over the open cycle. A branch point that satisfies the integrated equation `F=0` but fires earlier must be labelled `ADM_FAIL` and excluded from physical branch plots.

---

# Required continuation output schema

Every saved point should expose at least the following numerical fields:

- `parameter`;
- `period`;
- unwrapped normalised phase offsets;
- wrapped display phase offsets;
- `residual_norm`;
- `sigma_min_branch_jacobian`;
- `branch_condition_number`;
- `tangent`;
- `event_transversality_min`;
- `arrival_margin`;
- `threshold_margin`;
- `admissible`;
- `leading_multiplier_real` / `leading_multiplier_imag` or equivalent root data;
- `unstable_mode_count`;
- `critical_labels`;
- `derivative_backend`;
- `exact_or_surrogate`.

For symmetry-reduced problems also store the symmetry sector of every critical eigen/singular mode.

---

# v0.3 acceptance gate

A continuation implementation is **CORE-v0.3 valid** only when:

1. B11-B14 pass;
2. pseudo-arclength crosses the canonical fold B13;
3. existence and stability diagnostics are independent (B16);
4. hybrid event-transversality failure is detected (B17);
5. exact alpha-kernel continuation is arrival-aware (B18);
6. first-hitting admissibility is checked independently (B22).

B15 and B19-B21 become mandatory when the corresponding symmetry, threshold, or adaptive-delay features are used in a scientific result.
