# CORE exact invariant circles and fold v0.11

## Purpose

CORE v0.11 closes the main numerical gap left by v0.10: the invariant circles predicted by the quintic Chenciner normal form are now solved directly in the exact Lighthouse event dynamics.

The main results are:

1. a smooth state-space event map that avoids differentiating the periodic-comb `mod`/Heaviside representation;
2. a symmetry-adapted Fourier parameterization solver for
   \[
   \mathscr P(K(\varphi))=K(\varphi+\omega);
   \]
3. a verified local invariant-circle branch emerging from the v0.9 Neimark--Sacker locus with the expected quadratic parameter scaling;
4. asymptotic convergence of the exact branch coefficient to the v0.10 quintic prediction;
5. direct continuation through a nondegenerate fold of invariant circles (FIC).

The model remains

\[
S(x)=\exp[-1/(x+1)^2]H(x+1),
\qquad
\eta(t)=\alpha^2te^{-\alpha t}H(t),
\qquad \alpha=0.5,
\]

on the `N=3` circulant family

\[
w_d=[1,p,-p],
\qquad
\tau_d=[0,2,\tau_3].
\]

The Chenciner point from v0.9 is

\[
\tau_{3,*}=7.92140373739,
\quad
T_*=16.29213672114,
\quad
p_*=-3.26248414452,
\quad
\Omega_*=0.266095330801.
\]

---

# 1. Why the old history-map differentiation is not used

The v0.7 map writes activity as an exact periodic comb plus finite perturbation corrections. That form is excellent for values and first derivatives, but high-order finite differences must repeatedly split pairs of almost coincident base/perturbed arrival boundaries. Near the Chenciner point this creates a severe cancellation/quadrature artifact.

For v0.11 the event map is therefore evaluated in the finite-dimensional alpha-synapse state variables

\[
\dot q=-\alpha q,
\qquad
\dot\psi=-\alpha\psi+q.
\tag{V111}
\]

Between arrivals over an interval `Delta`,

\[
q^+=e^{-\alpha\Delta}q,
\tag{V112}
\]

\[
\psi^+=e^{-\alpha\Delta}(\psi+q\Delta).
\tag{V113}
\]

An arrival with weight `w` gives

\[
q^+\leftarrow q^+ + w\alpha^2.
\tag{V114}
\]

The phase gain on each smooth interval is evaluated by fixed Gauss quadrature. Because v0.11 stays inside the fixed itinerary

\[
0<2<\tau_3<T,
\]

the complete map is smooth with respect to spike times and parameters.

---

# 2. Exact initial synaptic state from finite spike history

Let

\[
x_{rj}=\delta T_j^{-r},
\qquad r=0,\ldots,L-1,
\]

and let neuron `i` start its phase integration at

\[
a_i=x_{0i}.
\]

Recent past spikes `r=1,...,L-1` are inserted explicitly. For edge displacement `d`, weight `w_d` and delay `tau_d`, their ages at `a_i` are

\[
A_{r,ij}=a_i+rT-x_{rj}-\tau_d.
\tag{V115}
\]

The unperturbed tail older than `L` cycles is summed analytically. With

\[
\rho=e^{-\alpha T},
\qquad
A_L=a_i+LT-\tau_d,
\]

the tail contribution is

\[
q_{\rm tail}
=w_d\alpha^2\frac{e^{-\alpha A_L}}{1-\rho},
\tag{V116}
\]

\[
\psi_{\rm tail}
=w_d\alpha^2e^{-\alpha A_L}
\left[
\frac{A_L}{1-\rho}
+
\frac{T\rho}{(1-\rho)^2}
\right].
\tag{V117}
\]

The current self-arrival at delay zero is included in the initial `q` state. The two current cross-arrivals occur at

\[
x_{0,i-1}+2,
\qquad
x_{0,i-2}+\tau_3,
\tag{V118}
\]

and are propagated explicitly in this order.

The next spike deviation `delta_i` is the root of

\[
\int_{x_{0i}}^{T+\delta_i}S(\psi_i(t))dt=2\pi.
\tag{V119}
\]

Newton iteration uses the exact endpoint derivative

\[
\partial_{\delta_i}
\int^{T+\delta_i}S(\psi_i(t))dt
=
S(\psi_i(T+\delta_i)).
\tag{V1110}
\]

and is differentiated by automatic differentiation.

The usual gauge removal gives the return map

\[
g=\frac13\sum_i\delta_i,
\]

\[
\mathscr P(x)_{0i}=\delta_i-g,
\qquad
\mathscr P(x)_{ri}=x_{r-1,i}-g,
\quad r\ge1.
\tag{V1111}
\]

At the synchronous orbit the Jacobian eigenpair agrees with the infinite-history characteristic equation to approximately `1e-10` in the physical critical mode.

---

# 3. Symmetry-adapted circle parameterization

For the `q=1` ring mode use

\[
K_{r,i}(\varphi)
=f_r(\varphi+2\pi i/3).
\tag{V1112}
\]

A subtle gauge consequence is essential:

- for the current block `r=0`, the spatial mean is removed pointwise, therefore temporal Fourier harmonics `n == 0 mod 3` are absent;
- for history blocks `r>=1`, the gauge shift `-g` generates spatially uniform components, therefore harmonics `n == 0 mod 3` and the temporal mean must be retained.

Omitting these older-history uniform components produces a false low-residual branch with incorrect `O(|A|)` parameter scaling.

Use real Fourier series

\[
f_r(\varphi)
=a_{r0}
+
\sum_{n=1}^{M}
[a_{rn}\cos(n\varphi)+b_{rn}\sin(n\varphi)].
\tag{V1113}
\]

The physical critical-amplitude and phase gauge are fixed by

\[
a_{0,1}=2A,
\qquad
b_{0,1}=0.
\tag{V1114}
\]

Thus `A` is the same physical complex Fourier amplitude used in v0.9--v0.10.

At collocation phases `varphi_j`, solve

\[
\boxed{
\mathscr P(K(\varphi_j))-K(\varphi_j+\omega)=0
}
\tag{V1115}
\]

together with synchronous-period consistency. The unknowns are the remaining Fourier coefficients, `(T,p,omega)`.

---

# 4. Local benchmark plane

Choose

\[
\boxed{
\tau_3=\tau_{3,*}+0.02
=7.94140373739.
}
\tag{V1116}
\]

The exact `q=1` NS orbit at this delay is

\[
\boxed{
T_{\rm NS}=16.29749389161298,
}
\tag{V1117}
\]

\[
\boxed{
p_{\rm NS}=-3.26798318225628,}
\tag{V1118}
\]

\[
\boxed{\Omega_{\rm NS}=0.26566907110085.}
\tag{V1119}
\]

The NS residual is below `5e-15` in the reference calculation.

---

# 5. Exact local invariant-circle branch

Starting from the NS orbit and continuing in `A` gives:

| `A` | `T` | `p` | `omega` | `p-p_NS` |
|---:|---:|---:|---:|---:|
| 0.003 | 16.297493894277835 | -3.2679831907823336 | 0.2656686925728281 | -8.52605408497e-9 |
| 0.006 | 16.297493902821014 | -3.2679832181927604 | 0.2656675578704931 | -3.59364809022e-8 |
| 0.009 | 16.297493916941058 | -3.2679832634963060 | 0.2656656666159935 | -8.12400267058e-8 |
| 0.012 | 16.297493936461260 | -3.2679833261260460 | 0.2656630186837619 | -1.43869766323e-7 |
| 0.015 | 16.297493961133515 | -3.2679834052859147 | 0.2656596138978083 | -2.23029635205e-7 |

For these points the collocation RMS residual is between approximately `1e-15` and `5e-14`.

At `A=0.012`, evaluation of the solved Fourier series on an independent phase grid gives a full-state invariance residual below `3e-14`. The discrete `n=1` Fourier residual projected onto the critical left Floquet vector satisfies

\[
\boxed{
|p^*\widehat R_{n=1}|\approx1.6\times10^{-16}.
}
\tag{V1120}
\]

Thus the small global residual is not hiding an error in the weak critical radial direction.

---

# 6. Quadratic branch scaling and comparison with v0.10

Fit the exact branch as

\[
p(A)-p_{\rm NS}
=c_2A^2+c_4A^4+\cdots.
\tag{V1121}
\]

The exact-event fit gives

\[
\boxed{
c_2^{\rm exact}\approx-0.00100847923835,
}
\tag{V1122}
\]

\[
 c_4^{\rm exact}\approx0.07499553762.
\tag{V1123}
\]

The v0.10 linearized Chenciner unfolding predicts

\[
\beta_2
\approx
\left.\frac{dL_1}{d\tau_3}\right|_{\rm NS}
\delta\tau
=
-0.0092975(0.02),
\]

and, using

\[
\partial_p|\mu|\approx-0.18379443,
\]

\[
\boxed{
c_2^{\rm NF}\approx-0.00101172815738.}
\tag{V1124}
\]

Hence the relative leading-order error is

\[
\boxed{
\frac{|c_2^{\rm exact}-c_2^{\rm NF}|}{|c_2^{\rm NF}|}
\approx3.21\times10^{-3},
}
\tag{V1125}
\]

or about `0.32%`.

The expected asymptotic trend is observed when the delay offset is varied:

- `delta tau = 0.02`: leading coefficient error about `0.32%`;
- `delta tau = 0.05`: error about `1.6%`;
- `delta tau = 0.20`: error about `8%`.

Thus the exact-event circle branch converges to the v0.10 quintic prediction as the Chenciner point is approached.

---

# 7. Direct fold of invariant circles

Continue the exact circle family in amplitude at fixed (V1116). The physical parameter reaches a nondegenerate minimum near

\[
\boxed{
A_{\rm FIC}^{\rm exact}\approx0.0660575,
}
\tag{V1126}
\]

with

\[
\boxed{
T_{\rm FIC}\approx16.297494585315,
}
\tag{V1127}
\]

\[
\boxed{
p_{\rm FIC}\approx-3.267985407948901,}
\tag{V1128}
\]

\[
\boxed{
\omega_{\rm FIC}\approx0.26548519956913.
}
\tag{V1129}
\]

Therefore

\[
\boxed{
p_{\rm FIC}-p_{\rm NS}
\approx-2.22569262\times10^{-6}.}
\tag{V1130}
\]

Implicit differentiation of the collocation equations gives

\[
\boxed{
\left.\frac{dp}{dA}\right|_{\rm FIC}
\approx2.7\times10^{-10},
}
\tag{V1131}
\]

and a local polynomial/continuation estimate gives

\[
\boxed{
\left.\frac{d^2p}{dA^2}\right|_{\rm FIC}
\approx4.08\times10^{-3}>0.
}
\tag{V1132}
\]

so the fold is nondegenerate.

The v0.10 quintic normal form predicts

\[
A_{\rm FIC}^{\rm NF}
=\sqrt{-\beta_2/(2L_2)}
\approx0.06568987297,
\tag{V1133}
\]

and

\[
p_{\rm FIC}^{\rm NF}-p_{\rm NS}
\approx-2.18288414\times10^{-6}.
\tag{V1134}
\]

The exact-vs-normal-form discrepancies are therefore approximately

\[
\boxed{0.56\%\ \text{in fold amplitude}}
\]

and

\[
\boxed{1.96\%\ \text{in fold parameter location}.}
\]

---

# 8. Spectral and history checks

At the fold, a Fourier solve with `M=5` and a refinement with `M=7` agree in `p` to approximately `1e-14`.

For `M=7`, 22 collocation phases give

\[
\mathrm{RMS}(R)\approx2.5\times10^{-13},
\qquad
\|R\|_\infty\approx7.3\times10^{-13}.
\tag{V1135}
\]

The old unperturbed alpha tail is represented analytically, while perturbation history uses `L=4`. At the present periods, omitted perturbation-tail effects are exponentially smaller than the reported circle/FIC errors.

---

# 9. Numerical design rules established by v0.11

1. Do not certify near-Chenciner circles from transient simulation alone.
2. Do not differentiate high-order normal-form data through paired periodic-comb/Heaviside corrections.
3. Use the smooth alpha state-space event itinerary for Newton/AD.
4. Retain gauge-generated spatially uniform harmonics in older history blocks.
5. Start circle continuation at the NS locus with `A -> 0`; jumping directly to a finite target amplitude can converge to a distant near-invariant loop.
6. Monitor the critical Fourier residual projection, not only the global norm.
7. Require quadratic `p-p_NS = O(A^2)` scaling before assigning local-NS branch status.
8. Use amplitude continuation to traverse the FIC; `p` itself is singular as a continuation parameter at the fold.

---

# 10. Benchmark contract B135--B150

- **B135**: the smooth state-space map reproduces the synchronous fixed point to `<1e-9`.
- **B136**: its critical Jacobian eigenvector agrees with `q_r=mu^{-r} exp(2 pi i i/3)` to relative residual `<1e-8`.
- **B137**: solve the NS orbit (V1117)--(V1119) with residual `<1e-10`.
- **B138**: retain `n == 0 mod 3` harmonics for history blocks `r>=1` and omit them for current block `r=0`.
- **B139**: obtain an exact circle at `A=0.012` with dense-grid max invariance residual `<1e-10`.
- **B140**: require critical projected residual `|p^* Rhat_1|<1e-10`.
- **B141**: verify `p(A)-p_NS=O(A^2)` as `A -> 0`.
- **B142**: recover `c2_exact approx -0.00100847924` at `delta tau=0.02`.
- **B143**: compare with `c2_NF approx -0.00101172816`; require relative discrepancy `<1%`.
- **B144**: verify that the leading coefficient discrepancy decreases as `delta tau -> 0`.
- **B145**: continue the circle family through the parameter minimum near `A=0.06606`.
- **B146**: recover `p_FIC-p_NS approx -2.22569e-6`.
- **B147**: require `|dp/dA|<1e-7` at the stored FIC point.
- **B148**: require `d2p/dA2>1e-3` at the FIC.
- **B149**: require exact-vs-quintic fold errors `<2%` in amplitude and `<5%` in parameter location.
- **B150**: require `M=5` / `M=7` fold-parameter agreement `<1e-9` and `M=7` max collocation residual `<1e-9`.

---

# 11. Consequence

CORE now closes the complete local Chenciner chain

\[
\boxed{
\text{exact Lighthouse events}
\to
\text{NS pair}
\to
L_1=0,\ L_2\ne0
\to
\text{quintic unfolding}
\to
\text{exact invariant circles}
\to
\text{exact FIC}.
}
\]

The next mathematical step should be adaptive-delay coupling. The fast subsystem now has a quantitatively verified local organizer, including the stable/unstable circle geometry and its fold. Slow conduction-delay dynamics can therefore be coupled to the verified Chenciner coordinates without relying on an unvalidated reduced-model branch.