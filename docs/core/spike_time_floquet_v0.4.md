# CORE spike-time Floquet theory v0.4

## Purpose

This document derives the general linear stability operator for an arbitrary phase-locked Haken Lighthouse network with heterogeneous weights, delays and phase offsets. It extends the synchronous/eigenmode calculations of v0.2 and the branch-continuation framework of v0.3.

The central object is a nonlinear matrix-valued characteristic operator in the cycle multiplier `mu`. The formulation is event based: it acts directly on perturbations of spike times rather than on a time-discretised phase trajectory.

Provenance tags:

- **[H]** historical Lighthouse structure;
- **[C]** contemporary structure supported by Coombes (2025/2026);
- **[P]** project derivation/canonicalisation.

The 2026 Coombes--Thul--Ruschel--Nicks work explicitly develops spike-time stability for fixed-delay phase-locked Lighthouse states and applies circulant/Fourier reduction on rings. The formulas below are derived independently as the CORE reference rather than copied from a secondary representation.

---

# 1. Base phase-locked orbit

Let

\[
\dot\theta_i(t)=S_i(\psi_i(t)),
\]

\[
\psi_i(t)=\sum_{j=1}^N w_{ij}\sum_{n\in\mathbb Z}
\eta\!\left(t-T_j^n-\tau_{ij}\right).
\tag{F1}
\]

A phase-locked solution has common period `T` and normalised offsets `chi_i`:

\[
T_i^m=(m+\chi_i)T,
\qquad \chi_i\in\mathbb R/\mathbb Z.
\tag{F2}
\]

Fix the gauge `chi_1=0` when solving the existence problem, but do **not** remove global physical time translation from the stability problem.

In the local cycle coordinate of neuron `i`,

\[
t=T_i^m+s,\qquad 0\le s<T,
\]

the periodic input is

\[
\Psi_i(s)=\sum_jw_{ij}\sum_{n\in\mathbb Z}
\eta\!\left(
 s+(m-n+\chi_i-\chi_j)T-\tau_{ij}
\right).
\tag{F3}
\]

After reindexing the integer lag, `Psi_i` is independent of `m`.

Define the spike-section velocity

\[
\boxed{
\nu_i=S_i(\Psi_i(0))=S_i(\Psi_i(T^-)).
}
\tag{F4}
\]

Regular event transversality requires `nu_i != 0`.

---

# 2. Perturb the spike times

Perturb every firing time:

\[
\widetilde T_i^m=T_i^m+\delta T_i^m.
\tag{F5}
\]

The phase-gain condition over one interspike interval is

\[
2\pi=\int_{T_i^m}^{T_i^{m+1}}S_i(\psi_i(t))dt.
\tag{F6}
\]

A presynaptic spike-time perturbation changes its kernel contribution according to

\[
\eta(t-T_j^n-\delta T_j^n-\tau_{ij})
=
\eta(t-T_j^n-\tau_{ij})
-
\eta'(t-T_j^n-\tau_{ij})\delta T_j^n
+O(\delta T^2).
\tag{F7}
\]

Therefore

\[
\delta\psi_i(t)=
-\sum_jw_{ij}\sum_n
\eta'(t-T_j^n-\tau_{ij})\delta T_j^n.
\tag{F8}
\]

Linearising (F6), including the moving integration limits, gives

\[
0=
\nu_i(\delta T_i^{m+1}-\delta T_i^m)
+
\int_{T_i^m}^{T_i^{m+1}}
S_i'(\psi_i^*(t))\delta\psi_i(t)dt.
\tag{F9}
\]

Substituting (F8) and using `s=t-T_i^m` yields the general spike-time recurrence

\[
\boxed{
\nu_i(\delta T_i^{m+1}-\delta T_i^m)
=
\sum_jw_{ij}\sum_{\ell\in\mathbb Z}
K_{ij,\ell}\,\delta T_j^{m-\ell}.
}
\tag{F10}
\]

Here

\[
\boxed{
K_{ij,\ell}
=
\int_0^T
S_i'(\Psi_i(s))
\eta'\!\left(
 s+(\ell+\chi_i-\chi_j)T-\tau_{ij}
\right)ds.
}
\tag{F11}
\]

Equation (F10) is the CORE v0.4 reference recurrence. It is valid inside a fixed event/arrival itinerary and away from threshold/grazing nonsmooth boundaries.

---

# 3. Nonlinear Floquet eigenproblem

Use the cycle-Floquet ansatz

\[
\delta T_i^m=\xi_i\mu^m.
\tag{F12}
\]

Then

\[
\delta T_j^{m-\ell}=\xi_j\mu^m\mu^{-\ell},
\]

and (F10) becomes

\[
\nu_i(\mu-1)\xi_i
=
\sum_j\mathcal H_{ij}(\mu)\xi_j,
\tag{F13}
\]

where

\[
\boxed{
\mathcal H_{ij}(\mu)
=w_{ij}\sum_{\ell\in\mathbb Z}
K_{ij,\ell}\mu^{-\ell}.
}
\tag{F14}
\]

Define

\[
D_\nu=\operatorname{diag}(\nu_1,\ldots,\nu_N)
\]

and the matrix-valued characteristic operator

\[
\boxed{
\mathcal M(\mu)
=(\mu-1)D_\nu-\mathcal H(\mu).
}
\tag{F15}
\]

The nontrivial Floquet multipliers satisfy

\[
\boxed{
\det\mathcal M(\mu)=0.
}
\tag{F16}
\]

For numerical work, CORE should solve the nonlinear eigenproblem

\[
\mathcal M(\mu)\xi=0
\tag{F17}
\]

directly and should not rely on the determinant except for small analytical examples.

The locked orbit is linearly asymptotically stable when every nontrivial multiplier satisfies

\[
\boxed{|\mu|<1.}
\tag{F18}
\]

The dimensionless cycle exponent is

\[
\lambda=\log\mu,
\]

while the physical-time exponent is

\[
\Lambda=\frac{1}{T}\log\mu.
\tag{F19}
\]

Multiplier space is preferred computationally because it avoids branch ambiguity in the complex logarithm.

---

# 4. Exact neutral time-translation mode

Every autonomous phase-locked orbit has the global time-shift perturbation

\[
\delta T_i^m=c
\quad\text{for all }i,m.
\tag{F20}
\]

Thus

\[
\boxed{\mu_0=1,\qquad \xi_0=\mathbf 1}
\tag{F21}
\]

must be an exact neutral mode.

This identity follows directly from (F11). At `mu=1`,

\[
\sum_j\mathcal H_{ij}(1)
=
\int_0^T
S_i'(\Psi_i(s))\Psi_i'(s)ds
\]

and therefore

\[
\sum_j\mathcal H_{ij}(1)
=
S_i(\Psi_i(T))-S_i(\Psi_i(0))=0.
\tag{F22}
\]

Hence

\[
\boxed{
\mathcal M(1)\mathbf 1=0.
}
\tag{F23}
\]

This is one of the strongest exact implementation tests in the project. A discretisation or lag truncation that destroys (F23) beyond its documented approximation error has not converged.

The neutral multiplier must be identified by its eigenvector overlap with global time translation, not merely by deleting whichever computed multiplier happens to lie closest to one.

---

# 5. Weighted derivative-comb representation

Define the Floquet-weighted derivative comb

\[
\mathcal Q_\mu(x;T)
=
\sum_{\ell\in\mathbb Z}
\eta'(x+\ell T)\mu^{-\ell}.
\tag{F24}
\]

Then

\[
\boxed{
\mathcal H_{ij}(\mu)
=
w_{ij}\int_0^T
S_i'(\Psi_i(s))
\mathcal Q_\mu\!\left(
 s+(\chi_i-\chi_j)T-\tau_{ij};T
\right)ds.
}
\tag{F25}
\]

This form avoids explicitly storing a very large number of lag coefficients.

For the alpha kernel

\[
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\]

write

\[
x=u+qT,
\qquad 0\le u<T,
\qquad q\in\mathbb Z,
\]

and

\[
r=e^{-\alpha T},\qquad z=\frac{r}{\mu}.
\]

Away from the arrival boundary `u=0`, direct geometric summation gives

\[
\boxed{
\mathcal Q_\mu(x;T)
=
\mu^q\alpha^2e^{-\alpha u}
\left[
\frac{1-\alpha u}{1-z}
-
\frac{\alpha Tz}{(1-z)^2}
\right].
}
\tag{F26}
\]

The series derivation converges for `|z|<1`; the rational expression supplies its meromorphic continuation elsewhere. Arrival boundaries must be handled with the same one-sided convention used by the event solver.

For exact-alpha calculations, CORE should split quadrature intervals at every point where `u=0` rather than autodifferentiating through `mod`/`floor`.

---

# 6. Relation to the v0.2 synchronous master-stability form

Suppose the base state is synchronous and homogeneous so that

- `chi_i=0`;
- `nu_i=nu`;
- all edges of a given class have the same delay/kernel factor;
- the stability kernel factors as

\[
\mathcal H(\mu)=g(\mu)W.
\tag{F27}
\]

If

\[
Wv_\rho=\widehat w_\rho v_\rho,
\]

then (F17) reduces to

\[
\boxed{
E_\rho(\mu)
=
\nu(\mu-1)-\widehat w_\rho g(\mu)=0.
}
\tag{F28}
\]

Thus the v0.2 graph-eigenmode/master-stability result is a special case of the full v0.4 operator.

For heterogeneous phase-locked states, `W` alone is generally **not** the correct stability operator: weights, delays, offsets and the postsynaptic gain `S_i'(Psi_i)` are entangled inside `H(mu)`.

---

# 7. Two-cell reduction

For an exchange-symmetric synchronous two-cell system,

\[
\mathcal H(\mu)=
\begin{pmatrix}
h_s(\mu)&h_c(\mu)\\
h_c(\mu)&h_s(\mu)
\end{pmatrix},
\qquad D_\nu=\nu I.
\tag{F29}
\]

The symmetric and antisymmetric modes

\[
v_+=(1,1)^T,
\qquad
v_-=(1,-1)^T
\]

give scalar characteristic functions

\[
\boxed{
E_+(\mu)=\nu(\mu-1)-h_s(\mu)-h_c(\mu),
}
\tag{F30}
\]

\[
\boxed{
E_-(\mu)=\nu(\mu-1)-h_s(\mu)+h_c(\mu).
}
\tag{F31}
\]

`E_+(1)=0` is the global time-translation mode. `E_-` controls relative timing and is the natural dynamic sector to compare with the antisymmetric existence mode `B` from v0.3.

The two objects must be stored separately: `B=0` is an existence-Jacobian statement; `E_-(1)=0` is a dynamic unit-multiplier statement. Their coincidence is a high-value orbit-bifurcation diagnostic, not an identity to assume blindly.

---

# 8. Dynamic bifurcation labels

After removal of the trivial global shift mode:

- **unit / steady critical:** a nontrivial multiplier crosses `mu=+1`;
- **period doubling:** a real multiplier crosses `mu=-1`;
- **Neimark--Sacker:** a complex-conjugate pair crosses `|mu|=1` away from `+-1`;
- **strong instability:** one or more multipliers satisfy `|mu|>1`.

For delayed systems there can be many multipliers. Reporting only the single largest real part from one local root search is not a sufficient stability certificate.

Each branch point should store at least:

\[
\rho_* = \max_{\mu\ne\mu_0}|\mu|,
\]

the corresponding multiplier(s), right/left eigenvectors where available, and a symmetry-sector label.

---

# 9. Nonnormality and eigenvalue conditioning

The general `M(mu)` is nonnormal. Near a simple nonlinear eigenpair `(mu_*,xi_*)`, let `y_*` be a left nullvector:

\[
y_*^*\mathcal M(\mu_*)=0,
\qquad
\mathcal M(\mu_*)\xi_*=0.
\]

A natural nonlinear eigenvalue conditioning denominator is

\[
\boxed{
\kappa_\mu^{-1}
=
\left|
y_*^*\mathcal M'(\mu_*)\xi_*
\right|.
}
\tag{F32}
\]

Small values signal a poorly conditioned or nearly multiple multiplier. CORE should therefore record both spectral radius and conditioning; a multiplier slightly inside the unit circle can still be highly sensitive.

---

# 10. Numerical root strategy [P]

For small systems, roots can be tracked by complex continuation in `(Re mu, Im mu)` using

\[
\mathcal M(\mu)\xi=0
\]

plus a normalisation condition on `xi`.

For larger systems:

1. use smallest singular value `sigma_min(M(mu))` for localisation rather than `det M`;
2. use an argument-principle contour count when a complete count inside a region is needed;
3. refine individual roots with a nonlinear eigenvalue Newton/secant method;
4. continue multipliers along a branch using the previous branch point as the initial guess;
5. run independent contour checks near suspected crossings.

For alpha kernels, compare two independent implementations:

- lag-sum / truncated-history form (F14);
- weighted-comb form (F25)--(F26).

Their convergence agreement is part of the v0.4 benchmark contract.

---

# 11. Connection to continuation geometry

At each v0.3 branch point `z_*(p)`, v0.4 attaches the dynamic operator

\[
\mathcal M(\mu;z_*(p),p).
\tag{F33}
\]

This produces a labelled branch object

\[
\boxed{
\mathcal B(p)=
\bigl[z_*(p),\;D_zF,\;\mathcal M(\cdot),\;\text{admissibility}\bigr].
}
\tag{F34}
\]

The three CORE checks remain independent:

1. `F=0` and continuation regularity;
2. Floquet/spike-time stability;
3. event admissibility/transversality.

Near a symmetry-breaking point, compare the symmetry sector of the nullvector of `D_zF` with the sector of any nontrivial multiplier approaching `+1`. Agreement supports the interpretation as a genuine periodic-orbit bifurcation; disagreement is diagnostic and must not be hidden.

---

# 12. Scope limits

The derivation assumes:

- a regular one-spike-per-node-per-cycle phase-locked itinerary;
- fixed edge delays during the fast stability calculation;
- differentiability of `S` and piecewise differentiability of `eta` on the current itinerary;
- no simultaneous event ambiguity that changes the jump/update convention.

At threshold contact, arrival collision, first-hitting failure or `nu_i -> 0`, switch to the nonsmooth/hybrid diagnostics of v0.3 rather than extrapolating (F10) through the singularity.

---

# 13. CORE v0.4 outputs

The implementation layer should expose conceptually:

- `lag_kernel(i,j,ell, locked_state)` -> `K_ijell`;
- `characteristic_matrix(mu, locked_state)` -> `M(mu)`;
- `neutral_residual(locked_state)` -> `||M(1) 1||`;
- `floquet_roots(locked_state, region)`;
- `leading_nontrivial_multiplier(locked_state)`;
- `mode_conditioning(mu, xi, y)`;
- symmetry-sector projections defined in the companion symmetry document.

Exact event science and smooth differentiable surrogates must remain separate implementations with explicit cross-validation.