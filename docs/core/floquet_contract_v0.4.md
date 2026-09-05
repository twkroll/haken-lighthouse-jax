# CORE Floquet and symmetry benchmark contract v0.4

## Scope

This file extends the CORE benchmark suite from B0--B22 to the general phase-locked spike-time/Floquet operator and symmetry reductions introduced in v0.4.

Benchmark classes:

- **EXACT** — equality should converge to numerical precision/tolerance;
- **PIECEWISE-EXACT** — exact within a fixed arrival/event itinerary;
- **STRUCTURAL** — tests invariance, symmetry, nullspaces or classification;
- **CONVERGENCE** — requires controlled convergence with lag/window/grid size;
- **CROSS-FORMULATION** — two mathematically independent formulations must agree.

The exact event formulation remains the reference. Smooth surrogate models may be compared against it but cannot replace these tests.

---

# B23 — exact neutral time-translation multiplier

**Class:** EXACT / STRUCTURAL

For any regular phase-locked state, construct

\[
\mathcal M(\mu)=(\mu-1)D_\nu-\mathcal H(\mu).
\]

Verify

\[
\boxed{\mathcal M(1)\mathbf1=0.}
\]

Acceptance:

\[
\frac{\|\mathcal M(1)\mathbf1\|_\infty}
{1+\|\mathcal H(1)\|_\infty}
<\varepsilon_{neutral}.
\]

Recommended float64 target for smooth moderate cases:

`eps_neutral <= 1e-10` after lag/quadrature convergence.

Also verify that adding a common constant to every spike time produces no first-order change in the one-cycle phase-gain residual.

Failure of this identity is a red flag for lag indexing, delay sign, arrival convention, or quadrature splitting.

---

# B24 — spike-time recurrence versus direct finite perturbation

**Class:** PIECEWISE-EXACT / CROSS-FORMULATION

Choose a regular locked state away from:

- event grazing;
- arrival collisions;
- threshold contacts;
- first-hitting boundaries.

Apply a small finite set of spike-time perturbations `delta T_j^n`, evaluate the exact one-cycle phase-gain residual by direct recomputation, and compare its first-order variation with

\[
\nu_i(\delta T_i^{m+1}-\delta T_i^m)
-
\sum_jw_{ij}\sum_\ell K_{ij,\ell}\delta T_j^{m-\ell}.
\]

As perturbation amplitude `eps -> 0`, the difference must scale as

\[
O(\varepsilon^2).
\]

A log-log fit should approach slope two before roundoff dominates.

---

# B25 — alpha weighted derivative comb

**Class:** PIECEWISE-EXACT / CONVERGENCE

For

\[
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\]

compare the direct truncated sum

\[
\sum_\ell\eta'(x+\ell T)\mu^{-\ell}
\]

with the closed form

\[
\mathcal Q_\mu(x;T)
=
\mu^q\alpha^2e^{-\alpha u}
\left[
\frac{1-\alpha u}{1-r/\mu}
-
\frac{\alpha T(r/\mu)}{(1-r/\mu)^2}
\right],
\]

where `x=u+qT`, `0<u<T`, `r=exp(-alpha*T)`.

Test real and complex `mu` values inside the absolute-convergence domain first. Then test meromorphic continuation against a finite-dimensional/state-space calculation where available.

Do not evaluate exactly at an arrival boundary without a documented one-sided convention.

---

# B26 — characteristic matrix: lag sum versus weighted comb

**Class:** CROSS-FORMULATION

For the same locked state and complex `mu`, evaluate `H_ij(mu)` by:

1. explicit lag coefficients `K_ijell` plus a converged lag sum;
2. direct quadrature of the weighted derivative comb `Q_mu`.

Require

\[
\boxed{
\|\mathcal M_{lag}(\mu)-\mathcal M_{comb}(\mu)\|_
\le
\varepsilon_{abs}+\varepsilon_{rel}\|\mathcal M_{comb}(\mu)\|.
}
\]

Run the comparison over a set of complex points both inside and near the unit circle, excluding poles/singular arrival configurations.

---

# B27 — two-cell symmetric/antisymmetric Floquet reduction

**Class:** EXACT / STRUCTURAL

For an exchange-symmetric synchronous two-cell state, compute the dense matrix `M(mu)` and transform it with

\[
U=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\1&-1
\end{pmatrix}.
\]

Require

\[
\boxed{
U^*\mathcal M(\mu)U
=
\operatorname{diag}(E_+(\mu),E_-(\mu))
}
\]

for arbitrary test values of `mu`.

Also require

\[
E_+(1)=0.
\]

The antisymmetric roots from `E_-` must agree with roots of the full dense nonlinear eigenproblem in that sector.

---

# B28 — ring DFT diagonalisation

**Class:** EXACT / STRUCTURAL

Construct a circulant ring locked state satisfying the v0.4 symmetry assumptions. Let `F_N` be the unitary DFT matrix.

For arbitrary complex `mu`, verify

\[
\boxed{
F_N^*\mathcal M(\mu)F_N
=
\operatorname{diag}
\left(E_0^{(q_0)}(\mu),\ldots,E_{N-1}^{(q_0)}(\mu)\right).
}
\]

Acceptance is based on the norm of all off-diagonal entries after transformation.

This test must pass for:

- synchrony `q_0=0`;
- at least one nonzero twisted state `q_0`.

---

# B29 — ring dense roots versus Fourier-sector roots

**Class:** CROSS-FORMULATION

For small `N`, compute the characteristic roots/multipliers in a prescribed region using:

1. the dense nonlinear matrix `M(mu)`;
2. all scalar Fourier functions `E_q(mu)`.

The union of sector roots, including multiplicities and the neutral root, must match the dense root set within tolerance.

Store the Fourier sector `q` on every matched root.

---

# B30 — N=2 ring equals dedicated two-cell theory

**Class:** EXACT

Instantiate the generic ring implementation with `N=2` and symmetric edge classes.

Require exact numerical equality between:

- ring `q=0` and dedicated symmetric `E_+`;
- ring `q=1` and dedicated antisymmetric `E_-`.

This benchmark prevents drift between specialised and general symmetry code paths.

---

# B31 — cluster quotient invariance

**Class:** STRUCTURAL / EXACT

Choose a network with an equitable cluster partition. For each cluster pair `(a,b)` verify that

\[
\sum_{j\in C_b}\mathcal H_{ij}(\mu)
\]

is independent of the representative `i in C_a`.

Construct the quotient operator `M^Q(mu)` and compare its roots with the roots of the full operator restricted to perturbations constant on each cluster.

Use at least one nontrivial partition with unequal cluster sizes.

---

# B32 — transverse cluster instability detection

**Class:** STRUCTURAL

Use or construct a cluster state where the quotient modes are stable but a transverse within-cluster mode is unstable.

The full stability classifier must return `unstable`, while a deliberately quotient-only diagnostic returns `longitudinally stable`.

This benchmark exists to ensure the production code never mistakes quotient stability for full cluster stability.

---

# B33 — multiplier/exponent convention

**Class:** EXACT

For selected complex multipliers away from the logarithm branch cut, verify

\[
\lambda=\log\mu,
\qquad
\Lambda=\lambda/T,
\qquad
\mu=e^{\Lambda T}.
\]

Classification must be performed primarily in multiplier space:

- stable: `|mu|<1`;
- unit: `mu=+1`;
- PD: `mu=-1`;
- NS: conjugate pair on `|mu|=1` away from `+-1`.

Changing the branch of `log(mu)` must not change the multiplier-based classification.

---

# B34 — nonlinear root solver on synthetic matrix functions

**Class:** EXACT algorithmic

Validate the nonlinear eigenvalue/root infrastructure before applying it to Lighthouse dynamics.

Use matrix functions with known roots, for example

\[
M(\mu)=
\begin{pmatrix}
\mu-a&0\\0&(\mu-b)(\mu-c)
\end{pmatrix}.
\]

Require:

1. correct root locations;
2. correct algebraic multiplicities where the method supports them;
3. correct contour root count under the argument principle;
4. stable refinement from nearby initial guesses;
5. no use of determinant magnitude as the sole convergence criterion.

Repeat with a mildly nonnormal matrix similarity transform.

---

# B35 — nonlinear eigenvalue conditioning

**Class:** EXACT / STRUCTURAL

At a simple root `mu_*`, compute right and left nullvectors `xi`, `y` and evaluate

\[
\gamma_*=y^*M'(\mu_*)\xi.
\]

Compare the predicted first-order root sensitivity under a small controlled perturbation of a scalar parameter with the measured root shift.

The implementation should flag near-multiple/ill-conditioned roots when

\[
|\gamma_*|
\]

is small relative to the chosen normalisation.

This benchmark protects against overconfident stability labels near defective multipliers.

---

# B36 — event-time versus flow/saltation spectrum

**Class:** CROSS-FORMULATION

In a case where a finite-dimensional hybrid flow/saltation formulation from v0.2 is available, compute nontrivial Floquet multipliers by both:

1. the v0.4 spike-time characteristic operator;
2. the independent flow-plus-saltation monodromy matrix.

Match the physical multiplier sets after accounting for any auxiliary synaptic-state modes represented differently by the two formulations.

At minimum include:

- a synchronous two-cell alpha-synapse case without ambiguous simultaneous-update ordering;
- one parameter sweep crossing a known stability boundary.

Agreement of the crossing location is required even if auxiliary stable modes differ in representation.

---

# B37 — continuation/Floquet symmetry-sector alignment

**Class:** STRUCTURAL / CROSS-FORMULATION

At a v0.3 exchange-symmetry-breaking branch point:

1. compute the nullvector of the existence Jacobian `D_zF`;
2. label its symmetry sector;
3. track dynamic multipliers toward `mu=+1`;
4. label the corresponding Floquet eigenvector sector.

For a genuine regular pitchfork of periodic orbits, require the critical nontrivial dynamic sector to match the existence sector.

If they do not match, the software must report a diagnostic mismatch rather than forcing a pitchfork label.

---

# B38 — lag-tail convergence and neutral-residual convergence

**Class:** CONVERGENCE

For exponentially decaying kernels, compute the characteristic operator with increasing historical lag cutoff `L`.

Track simultaneously:

\[
\|M_L(\mu)-M_{L+\Delta L}(\mu)\|,
\]

leading multiplier error, and

\[
\|M_L(1)\mathbf1\|.
\]

All three must converge consistently with the expected kernel-tail decay.

A stability result is not considered converged if the leading multiplier appears stable while the neutral residual remains dominated by lag-truncation error.

---

# B39 — ring-to-continuum dispersion convergence

**Class:** CONVERGENCE / ASYMPTOTIC

Choose a smooth periodic spatial kernel and delay profile with a documented `1/N` quadrature normalisation. Compute ring symbols for increasing `N` and compare them with the corresponding continuum Fourier integral.

For fixed physical wave number `k`, require

\[
E_q^{(N)}(\mu)\to E(k,\mu)
\]

and convergence of the leading multiplier/root.

This is the v0.4 bridge from discrete spiking rings to the continuum dispersion framework.

---

# B40 — mode-selection atlas consistency

**Class:** STRUCTURAL

Along a continued ring branch, compute the leading nontrivial spectral radius in every Fourier sector:

\[
\rho_q(p)=\max |\mu_q(p)|.
\]

Require the reported global leading multiplier to satisfy

\[
\rho_*(p)=\max_q\rho_q(p).
\]

When the leading sector changes from `q_a` to `q_b`, store the crossing and verify it against the dense small-`N` operator where feasible.

This benchmark validates mode competition and the instability atlas used for scientific interpretation.

---

# Required branch-point stability record

After v0.4, every scientifically reported locked branch point should be able to carry the following fields conceptually:

- existence residual `||F||`;
- `sigma_min(D_zF)`;
- event-transversality margin `min_i |nu_i|`;
- first-hitting/admissibility status;
- leading nontrivial multiplier `mu_*`;
- spectral radius `rho_*`;
- symmetry/Fourier sector;
- nonlinear eigenvalue conditioning;
- neutral residual `||M(1)1||`;
- root-search/contour completeness metadata.

A branch diagram that colours points as stable/unstable without enough information to reproduce these labels is not CORE-valid.