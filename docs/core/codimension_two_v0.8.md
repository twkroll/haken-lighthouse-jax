# CORE codimension-two atlas v0.8 — corrected reference

## Status and numerical erratum

CORE v0.8 introduced the first hybrid codimension-two Lighthouse benchmark: a transverse intersection of a smooth Neimark--Sacker (NS) locus with a tangential response-threshold contact locus in a three-node ring.

A v0.9 reproducibility audit found that the originally stored coordinates corresponded to a 48-point Gauss rule, while the committed v0.8 reference script imported the 32-point quadrature from v0.7. The original script therefore did **not** reproduce its own asserted coordinates. The audit also showed that the previously reported event-map value `ell1 ~= -14.5006` at the threshold contact is strongly quadrature/finite-difference sensitive and must not be treated as a certified normal-form coefficient.

This document supersedes the original v0.8 numerical values. The hybrid codimension-two intersection itself is retained; its coordinates below are converged with 96/128-point Gauss quadrature. The nonlinear NS coefficient at the threshold boundary is deliberately left **uncertified**. The smooth generalized-NS/Chenciner calculation is moved to v0.9, away from the threshold boundary.

Provenance classes follow the CORE convention: **[H]** historical Haken structure, **[C]** contemporary Lighthouse structure, **[P]** project derivation/reference calculation.

---

# 1. Two-parameter ring family

Use the synchronous `N=3` circulant ring

\[
w_d=[1,p,-p],
\qquad
\tau_d=[0,2,\tau_3],
\tag{V81}
\]

with

\[
S(x)=\exp[-1/(x+1)^2]H(x+1),
\qquad
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\qquad \alpha=0.5.
\tag{V82}
\]

The row sum is one for all `(p,tau_3)`. Define

\[
\Psi(s)=R_T(s)+pR_T(s-2)-pR_T(s-\tau_3).
\tag{V83}
\]

Synchronous existence requires

\[
F_{\rm sync}(T,p,\tau_3)
=2\pi-\int_0^T S(\Psi(s))ds=0.
\tag{V84}
\]

The `q=1` NS locus is defined by

\[
F_{\rm sync}=0,
\qquad
E_1(e^{i\Omega};T,p,\tau_3)=0,
\qquad 0<\Omega<\pi.
\tag{V85}
\]

A tangential threshold contact is defined by

\[
\Psi(s_*)=-1,
\qquad
\Psi'(s_*)=0,
\qquad
\Psi''(s_*)>0.
\tag{V86}
\]

---

# 2. Converged hybrid codimension-two point

Solving the five equations

\[
F_{\rm sync}=0,
\quad
\Re E_1(e^{i\Omega})=0,
\quad
\Im E_1(e^{i\Omega})=0,
\quad
\Psi(s_*)+1=0,
\quad
\Psi'(s_*)=0
\tag{V87}
\]

with 96- and 128-point Gauss rules gives the converged reference

\[
\boxed{T_*=17.6950650237,}
\tag{V88}
\]

\[
\boxed{p_*=-7.2156404007,}
\tag{V89}
\]

\[
\boxed{\tau_{3,*}=13.1402482105,}
\tag{V810}
\]

\[
\boxed{\Omega_*=0.4610342074,}
\tag{V811}
\]

\[
\boxed{s_*=4.3807078863.}
\tag{V812}
\]

The corresponding critical multiplier is

\[
\boxed{
\mu_*=0.89559288398+0.44487457352i,
\qquad |\mu_*|=1.
}
\tag{V813}
\]

The 96- and 128-point coordinate differences are below approximately `1.4e-7`, while the 32-point rule is visibly unconverged at this threshold-sensitive point. Thus v0.8 adopts the 128-point coordinates above.

---

# 3. Threshold and event diagnostics

At the converged point,

\[
\Psi(s_*)=-1,
\qquad
\Psi'(s_*)=0,
\tag{V814}
\]

and

\[
\boxed{\Psi''(s_*)\approx0.24999998>0.}
\tag{V815}
\]

Hence the contact is an isolated tangential minimum.

At the firing section,

\[
\Psi(0)\approx0.8327593022,
\tag{V816}
\]

so

\[
\boxed{\nu_*=S(\Psi(0))\approx0.7425188207>0.}
\tag{V817}
\]

Spike-event transversality therefore remains regular. The second codimension is a response-threshold/activity-set boundary, not spike grazing.

Because the zero extension of this particular response is infinitely flat at `x=-1`, the threshold contact is not a classical derivative discontinuity. It is nevertheless a structural boundary of the active response set and is kept as a hybrid/structural CORE diagnostic.

---

# 4. Transverse intersection of critical loci

Using `tau_3` as local continuation parameter gives

\[
\boxed{
\frac{dp_{\rm NS}}{d\tau_3}\approx-2.27233144,
}
\tag{V818}
\]

and

\[
\boxed{
\frac{dp_{\rm TH}}{d\tau_3}\approx-0.29182573.
}
\tag{V819}
\]

Thus

\[
\boxed{
\frac{dp_{\rm NS}}{d\tau_3}
-
\frac{dp_{\rm TH}}{d\tau_3}
\approx-1.98050571\ne0.
}
\tag{V820}
\]

The acute angle between the two parameter-plane tangents is approximately

\[
\boxed{49.9782^\circ.}
\tag{V821}
\]

The intersection is therefore transverse and genuinely codimension two in `(p,tau_3)`.

---

# 5. Linear NS transversality

At fixed `tau_3=tau_{3,*}`, independent characteristic-root continuation in `p` gives

\[
\boxed{
\frac{d|\mu|}{dp}\approx-0.019617079,
}
\tag{V822}
\]

and

\[
\boxed{
\frac{d\arg\mu}{dp}\approx-0.071526814.
}
\tag{V823}
\]

Hence the complex pair crosses the unit circle transversely.

---

# 6. Nonlinear coefficient at the threshold boundary — not certified

The original v0.8 record reported

\[
\ell_1\approx-14.5006066.
\]

The v0.9 audit showed that this value is tied to the legacy 48-point quadrature and is not stable under simultaneous quadrature refinement and finite-difference-step refinement of the threshold-contact event map. For example, moving from 48 to 64/96-point quadrature changes the computed cubic coefficient by order unity rather than by the benchmark tolerance.

Therefore:

\[
\boxed{
\text{v0.8 does not certify }\ell_1
\text{ or an NS criticality label at the threshold contact.}
}
\tag{V824}
\]

This does **not** invalidate the hybrid codimension-two intersection: its defining conditions are existence, unit-circle NS criticality, threshold contact, and transverse intersection of the two loci, all of which are independently converged above.

The smooth nonlinear NS analysis is instead performed in v0.9 at a point where

\[
\min_s(\Psi(s)+1)>0,
\]

so the entire orbit remains uniformly away from the response threshold.

---

# 7. Negative result retained

The regular two-cell flip family examined in v0.8 did not produce a verified simultaneous nontrivial `mu=-1` and `mu=+1` point. CORE therefore retains the negative result:

- no flip+unit codimension-two label is assigned unless both conditions are solved on the same regular orbit;
- failed or ill-conditioned searches are not promoted to bifurcation claims.

---

# 8. Corrected benchmark contract B91--B104

- **B91**: solve (V87) with residual norm `<1e-9` using at least 96-point quadrature.
- **B92**: reproduce the 128-point coordinates (V88)--(V812) within documented convergence tolerance.
- **B93**: verify `|Psi(s_*)+1|<1e-8`.
- **B94**: verify `|Psi'(s_*)|<1e-8`.
- **B95**: verify `Psi''(s_*)>0` and approximately `0.25`.
- **B96**: verify `nu_*>0.7`.
- **B97**: verify `||mu_*|-1|<1e-8` in the characteristic calculation.
- **B98**: recover `dp_NS/dtau_3 approx -2.27233144`.
- **B99**: recover `dp_TH/dtau_3 approx -0.29182573`.
- **B100**: verify the slope-difference magnitude exceeds one.
- **B101**: recover `d|mu|/dp approx -0.019617079` at fixed `tau_3`.
- **B102**: perform a quadrature convergence audit; do **not** certify the legacy `ell1` value.
- **B103**: any future threshold-boundary nonlinear coefficient must include both quadrature and derivative-step convergence.
- **B104**: do not label a two-cell flip+unit codimension-two point without simultaneous solved critical conditions.

---

# 9. v0.8 conclusion

The corrected v0.8 result is

\[
\boxed{
\text{smooth NS critical mode}
+
\text{tangential response-threshold boundary}
\Longrightarrow
\text{transverse hybrid codimension-two intersection}.
}
\]

The threshold-boundary cubic coefficient is intentionally not part of the certified result. v0.9 moves to a uniformly smooth part of the NS locus and computes the generalized-NS/Chenciner normal form through fifth order.