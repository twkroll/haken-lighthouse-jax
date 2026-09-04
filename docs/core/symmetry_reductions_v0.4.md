# CORE symmetry and Fourier reductions v0.4

## Purpose

This document reduces the general spike-time characteristic operator of `spike_time_floquet_v0.4.md` whenever the locked state and the delayed network possess symmetry.

The main targets are:

1. circulant rings and rotating/twisted phase-locked states;
2. exchange-symmetric two-cell systems;
3. cluster-synchronous/equitable partitions;
4. general permutation-symmetry sectors.

The 2026 Coombes--Thul--Ruschel--Nicks study explicitly uses circulant symmetry to decompose ring stability into Fourier modes. CORE generalises that organising principle into an implementation contract.

---

# 1. General characteristic operator

For a locked state

\[
T_i^m=(m+\chi_i)T,
\]

v0.4 defines

\[
\mathcal M(\mu)=(\mu-1)D_\nu-\mathcal H(\mu),
\tag{S1}
\]

with

\[
\mathcal H_{ij}(\mu)
=w_{ij}\sum_{\ell\in\mathbb Z}K_{ij,\ell}\mu^{-\ell}.
\tag{S2}
\]

Symmetry reduction is valid only when the **full delayed locked-state operator**, not merely `W`, respects the symmetry.

---

# 2. Circulant ring

Index nodes by

\[
i=0,1,\ldots,N-1
\]

modulo `N`. Let the directed displacement from presynaptic node `j` to postsynaptic node `i` be

\[
d=i-j\pmod N.
\]

Assume

\[
w_{ij}=w_d,
\qquad
\tau_{ij}=\tau_d.
\tag{S3}
\]

A `q_0`-twisted locked state is

\[
\boxed{
\chi_i=\frac{q_0 i}{N}\pmod 1,
}
\tag{S4}
\]

where `q_0` is an integer winding number.

Then

\[
\chi_i-\chi_j=\frac{q_0d}{N}\pmod1.
\]

The base input becomes independent of node index:

\[
\boxed{
\Psi_{q_0}(s)
=
\sum_{d=0}^{N-1}
w_d R_T\!\left(
s+\frac{q_0d}{N}T-\tau_d
\right).
}
\tag{S5}
\]

Hence the spike-section velocities are common:

\[
\nu_i=\nu.
\]

The corresponding lag coefficient depends only on displacement:

\[
K_{d,\ell}^{(q_0)}
=
\int_0^T
S'(\Psi_{q_0}(s))
\eta'\!\left(
s+\left(\ell+\frac{q_0d}{N}\right)T-\tau_d
\right)ds.
\tag{S6}
\]

Define

\[
h_d^{(q_0)}(\mu)
=
w_d\sum_{\ell\in\mathbb Z}
K_{d,\ell}^{(q_0)}\mu^{-\ell}.
\tag{S7}
\]

Then `H(mu)` is circulant.

---

# 3. Exact discrete Fourier diagonalisation

Let

\[
\kappa_q=\frac{2\pi q}{N},
\qquad q=0,\ldots,N-1,
\]

and define the Fourier vector

\[
\xi_i^{(q)}=e^{i\kappa_q i}.
\tag{S8}
\]

Because the operator is circulant,

\[
\mathcal H(\mu)\xi^{(q)}
=
\widehat h_q^{(q_0)}(\mu)\xi^{(q)},
\]

where

\[
\boxed{
\widehat h_q^{(q_0)}(\mu)
=
\sum_{d=0}^{N-1}
h_d^{(q_0)}(\mu)e^{-i\kappa_q d}.
}
\tag{S9}
\]

Therefore the full `N x N` nonlinear eigenproblem reduces exactly to `N` scalar characteristic equations:

\[
\boxed{
E_q^{(q_0)}(\mu)
=
\nu(\mu-1)
-
\widehat h_q^{(q_0)}(\mu)
=0.
}
\tag{S10}
\]

Interpretation:

- `q_0` labels the **base rotating-wave/twist state**;
- `q` labels the **perturbation Fourier mode**.

These two integers must never be conflated in code or plots.

---

# 4. Neutral ring mode

Global time translation is spatially uniform, hence it lies in perturbation sector

\[
q=0.
\]

For every admissible locked ring state,

\[
\boxed{
E_0^{(q_0)}(1)=0.
}
\tag{S11}
\]

The `q=0` sector can also contain additional nontrivial multipliers. Only the eigenpair whose spike-time eigenvector is the uniform global shift is neutral by symmetry.

---

# 5. Reflection symmetry and Fourier degeneracy

If the delayed edge classes are reflection symmetric,

\[
w_d=w_{N-d},
\qquad
\tau_d=\tau_{N-d},
\tag{S12}
\]

and the locked state preserves the corresponding reflection symmetry, then the sectors `q` and `N-q` form the usual real sine/cosine pair.

For real coefficients, roots appear in complex conjugate pairs. CORE should report both the complex Fourier label and, where useful, the equivalent real irreducible subspace.

For a twisted base `q_0 != 0`, reflection may map the base to the opposite twist `-q_0`; it is not automatically an isotropy of a single branch. Degeneracy assumptions must therefore be checked against the actual base state, not inferred from ring geometry alone.

---

# 6. Continuum / large-ring limit

Let node position be

\[
x_i=\frac{iL}{N}.
\]

If

\[
w_d\to \frac{L}{N}w(x),
\qquad
\tau_d\to\tau(x),
\]

then the discrete symbol (S9) approaches a spatial Fourier transform of the delay- and phase-weighted event kernel.

Schematically,

\[
\widehat h(k,\mu)
=
\int_0^L
h(x,\mu)e^{-ikx}dx.
\tag{S13}
\]

The characteristic relation becomes

\[
\boxed{
E(k,\mu)=\nu(\mu-1)-\widehat h(k,\mu)=0.
}
\tag{S14}
\]

This is the event-based counterpart of a neural-field dispersion relation and provides a bridge to the spatial/Turing analysis in the 2025 Lighthouse revisit.

The limit must be demonstrated numerically rather than assumed: discrete spectra should converge to the continuum symbol as `N` grows under a documented weight normalisation.

---

# 7. Exchange-symmetric two-cell system as C2 Fourier theory

The two-cell symmetric/antisymmetric decomposition from v0.2 and v0.3 is simply the `N=2` cyclic Fourier transform:

\[
q=0 \leftrightarrow (1,1)^T,
\]

\[
q=1 \leftrightarrow (1,-1)^T.
\]

Thus

\[
E_+(\mu)=E_{q=0}(\mu),
\qquad
E_-(\mu)=E_{q=1}(\mu).
\tag{S15}
\]

This identity is a useful cross-version benchmark: the generic ring implementation at `N=2` must reproduce the dedicated two-cell formulas exactly.

---

# 8. Cluster-synchronous states

Let the nodes be partitioned into clusters

\[
\mathcal C_1,\ldots,\mathcal C_C.
\]

Suppose all nodes in cluster `a` share the same locked offset and spike-section velocity:

\[
\chi_i=\chi_a,
\qquad
\nu_i=\nu_a,
\qquad i\in\mathcal C_a.
\tag{S16}
\]

The cluster subspace is invariant for stability if the full characteristic coupling is equitable: for every `i,i' in C_a` and every target cluster `b`,

\[
\boxed{
\sum_{j\in\mathcal C_b}\mathcal H_{ij}(\mu)
=
\sum_{j\in\mathcal C_b}\mathcal H_{i'j}(\mu)
}
\tag{S17}
\]

for all `mu` in the domain of interest.

Define the quotient coupling

\[
\mathcal H^Q_{ab}(\mu)
=
\sum_{j\in\mathcal C_b}\mathcal H_{ij}(\mu),
\qquad i\in\mathcal C_a.
\tag{S18}
\]

Then perturbations constant inside each cluster obey

\[
\boxed{
\mathcal M^Q_{ab}(\mu)
=
\delta_{ab}\nu_a(\mu-1)
-
\mathcal H^Q_{ab}(\mu).
}
\tag{S19}
\]

Roots of

\[
\det\mathcal M^Q(\mu)=0
\]

describe **longitudinal / inter-cluster** perturbations.

---

# 9. Transverse cluster stability

The quotient operator is not a complete stability test.

Perturbations whose sum/average vanishes within a cluster can break cluster synchrony while leaving the quotient coordinates unchanged. These form transverse symmetry sectors.

Therefore a cluster branch is stable only if:

1. every nontrivial quotient multiplier is inside the unit circle;
2. every transverse-sector multiplier is inside the unit circle;
3. the neutral global time-shift mode is excluded correctly.

A code path that evaluates only `M^Q` can miss a cluster-splitting instability and fails the CORE contract.

---

# 10. General permutation symmetry

Let a finite permutation group `G` act on node space with permutation matrices `P_g`.

If the complete locked-state characteristic operator satisfies

\[
\boxed{
P_g\mathcal M(\mu)=\mathcal M(\mu)P_g
\quad\forall g\in G,
}
\tag{S20}
\]

then node space decomposes into invariant isotypic components.

For an irreducible representation `rho` of dimension `d_rho` and character `chi_rho(g)`, the standard symmetry projector is

\[
\boxed{
\Pi_\rho
=
\frac{d_\rho}{|G|}
\sum_{g\in G}
\chi_\rho(g)^*P_g.
}
\tag{S21}
\]

After constructing an orthonormal basis for `range(Pi_rho)`, project `M(mu)` into that sector and solve the smaller nonlinear eigenproblem there.

For cyclic groups, (S21) is exactly the discrete Fourier transform. For two-cell exchange symmetry it produces the symmetric and antisymmetric sectors.

---

# 11. Isotropy of the base state matters

A network may possess a large symmetry group while a particular phase-locked state preserves only a subgroup.

Symmetry reduction must use the **isotropy subgroup of the delayed locked state**, including:

- connectivity;
- delay classes;
- response/kernel parameters;
- phase offsets.

Do not block-diagonalise according to symmetries broken by the chosen locked state.

Twisted ring states are the canonical example: translation symmetry survives in a co-rotating phase-difference sense and yields the circulant operator above, while reflection can map one twist branch to another rather than fixing it.

---

# 12. Connection to v0.3 existence sectors

At a symmetric branch point, the continuation Jacobian `D_zF` and the dynamic characteristic operator `M(mu)` are different operators, but both inherit the isotropy of the same base state.

Therefore their critical vectors can be labelled by the same symmetry sectors.

CORE should store, for every detected critical point:

\[
(\text{existence sector},\;\text{dynamic sector},\;\text{admissibility status}).
\]

At a genuine symmetry-breaking periodic-orbit bifurcation one expects a nontrivial dynamic multiplier to approach `mu=+1` in the same sector as the branch-Jacobian nullvector. This is a validation target, not a hard-coded identity.

---

# 13. Ring instability atlas

For a ring branch with base twist `q_0`, define

\[
\rho_q(p)=
\max\{|\mu|:\;E_q^{(q_0)}(\mu;p)=0\},
\]

after neutral-mode exclusion.

The branch can then be labelled by the leading perturbation sector

\[
q_*(p)=\operatorname*{argmax}_q\rho_q(p).
\tag{S22}
\]

This gives a compact mode-selection atlas:

- `q=0`: spatially uniform timing instability;
- low `q`: long-wave modulation;
- intermediate/high `q`: patterned timing instability;
- sector changes: mode competition.

This mode label is the natural discrete precursor of the critical wave number in the continuum neural-field limit.

---

# 14. Implementation outputs [P]

The symmetry layer should expose conceptually:

- `ring_edge_symbol(mu, q0, displacement)`;
- `ring_mode_characteristic(mu, q0, q)`;
- `ring_mode_roots(q0, q)`;
- `cluster_quotient_operator(mu, partition)`;
- `symmetry_projectors(group)`;
- `projected_characteristic(mu, sector)`;
- `leading_sector(branch_point)`.

Every reduced result must be independently comparable to the unreduced dense `M(mu)` on small systems before reduction is trusted at scale.