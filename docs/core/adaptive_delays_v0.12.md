# CORE adaptive conduction-delay dynamics v0.12

## Purpose

CORE v0.12 is the first slow--fast benchmark built on the exact frozen-delay atlas established in v0.9--v0.11.

The aim is deliberately narrower than a full biological white-matter model. We ask a local mathematical question:

> If the conduction delay is allowed to adapt slowly, does the fast Lighthouse order parameter adiabatically follow the frozen Neimark--Sacker / invariant-circle / fold-of-invariant-circles skeleton, or can slow passage cause the system to skip that entire local attractor window?

The answer for the verified `N=3` ring is unexpectedly sharp: the frozen NS--FIC window in the physical delay is so narrow and the radial growth so weak that a slowly adapting system can pass through the whole window without acquiring the frozen invariant-circle amplitude. Activity-dependent speed-up makes this dynamic skip stronger.

Provenance:

- **[C26]** Coombes, Thul, Ruschel and Nicks (2026) introduce activity-dependent conduction-speed plasticity in the Haken Lighthouse model and organize the resulting slow--fast dynamics by frozen locked branches.
- **[P]** the particular order-parameter-level plasticity law, parameter choices, dynamic-passage calculation and numerical benchmark values below are project definitions.
- **[E]** frozen NS/FIC data come from the exact event and invariant-circle calculations of CORE v0.11.

The central CORE interpretation remains unchanged: the complex `q=1` spike-time Fourier amplitude is the fast synergetic order parameter. The conduction delay is a slow structural state variable, not an order parameter by default.

---

# 1. Frozen exact skeleton at fixed coupling

Use the v0.11 ring

\[
w_d=[1,p,-p],\qquad \tau_d=[0,2,\tau_3],
\]

and fix the coupling at the exact v0.11 FIC value

\[
\boxed{p_{\rm ad}=-3.267985407948901.}
\tag{V121}
\]

At

\[
\boxed{\tau_{\rm FIC}=7.94140373739}
\tag{V122}
\]

the exact Fourier-collocation calculation gives the nondegenerate fold of invariant circles

\[
\boxed{A_{\rm FIC}^{\rm exact}=0.0660575.}
\tag{V123}
\]

Keeping `p=p_ad` fixed and solving the independent spike-time characteristic equations gives the corresponding frozen Neimark--Sacker point

\[
\boxed{T_{\rm NS}=16.297496058505022,}
\tag{V124}
\]

\[
\boxed{\tau_{\rm NS}=7.941411830425917,}
\tag{V125}
\]

\[
\boxed{\Omega_{\rm NS}=0.265668898005473.}
\tag{V126}
\]

Therefore the entire frozen stable-circle window in the physical delay has width

\[
\boxed{
W_\tau
=\tau_{\rm NS}-\tau_{\rm FIC}
=8.09303591698\times10^{-6}.
}
\tag{V127}
\]

This width is the first key number of v0.12.

The frozen critical multiplier crosses the unit circle with

\[
\boxed{
 s_\tau
 =\left.\frac{\partial(|\mu|-1)}{\partial\tau_3}\right|_{\rm NS,p=p_{\rm ad}}
 \approx-0.05053354353.
}
\tag{V128}
\]

Thus decreasing `tau_3` through `tau_NS` makes synchrony radially unstable.

---

# 2. Frozen radial normal form calibrated by exact NS and FIC data

Let

\[
A\ge0
\]

denote the physical `q=1` Fourier amplitude used in v0.9--v0.11. On the fixed-`p` slice define

\[
\beta_1(\tau_3)
=s_\tau(\tau_3-\tau_{\rm NS}).
\tag{V129}
\]

Use the v0.9 second Lyapunov coefficient

\[
\boxed{L_2=0.021546133331>0.}
\tag{V1210}
\]

For the v0.12 one-dimensional slow passage we calibrate one effective cubic radial coefficient from the **exact** NS--FIC separation. At the fold,

\[
\beta_{1,{\rm FIC}}
=s_\tau(\tau_{\rm FIC}-\tau_{\rm NS})
\approx4.08969782780\times10^{-7}.
\tag{V1211}
\]

The quintic fold relation

\[
\beta_1=\frac{\beta_2^2}{4L_2},\qquad \beta_2<0
\]

then gives

\[
\boxed{
\beta_{2,{\rm eff}}
=-\sqrt{4L_2\beta_{1,{\rm FIC}}}
=-1.87741497471\times10^{-4}.
}
\tag{V1212}
\]

The frozen radial equation used for the adaptive benchmark is

\[
\boxed{
\frac{dA}{dn}
=A\left[
\beta_1(\tau_3)
+\beta_{2,{\rm eff}}A^2
+L_2A^4
\right].
}
\tag{V1213}
\]

Here `n` is cycle count. The differential form is the slow-envelope limit of the v0.10 cycle map and is used because the adaptive time scale will be orders of magnitude slower than one spike cycle.

The calibration itself predicts

\[
A_{\rm FIC}^{\rm cal}
=\sqrt{-\frac{\beta_{2,{\rm eff}}}{2L_2}}
=0.066005552315,
\tag{V1214}
\]

which differs from the exact v0.11 value by only

\[
\boxed{7.86\times10^{-4}\ \text{relative} \;(0.079\%).}
\tag{V1215}
\]

This supplies an internal static check before any slow dynamics is introduced.

---

# 3. Project plasticity law in conduction-speed coordinates

The current adaptive Lighthouse literature motivates evolving conduction speed rather than delay directly. Let the normalized path length be

\[
\ell=1,
\qquad
\tau_3=\frac{1}{c}.
\tag{V1216}
\]

CORE v0.12 uses the cycle-scale phenomenological law

\[
\boxed{
\frac{dc}{dn}
=\varepsilon
\left[
c_0-c+\kappa H(A^2)
\right],
}
\tag{V1217}
\]

with saturating activity proxy

\[
\boxed{
H(u)=\frac{u}{u+u_s}.
}
\tag{V1218}
\]

This is a project reduced law in the same slow-speed-plasticity spirit as the 2026 adaptive Lighthouse work. It is **not** claimed to be the exact microscopic axonal activity functional used there.

Benchmark values are

\[
\tau_{\rm target}=\tau_{\rm FIC}-5\times10^{-5}
=7.94135373739,
\]

\[
\boxed{c_0=1/\tau_{\rm target}=0.1259231150089354,}
\tag{V1219}
\]

\[
\boxed{u_s=0.03^2=9\times10^{-4},}
\tag{V1220}
\]

and for the activity-dependent case

\[
\boxed{\kappa=2\times10^{-6}.}
\tag{V1221}
\]

The canonical perturbation seed at the frozen NS crossing is

\[
\boxed{A_0=10^{-3}.}
\tag{V1222}
\]

---

# 4. Linear slow-passage estimate

First set `kappa=0`. Near the NS crossing and while `A` is small,

\[
\frac{d\tau_3}{dn}
\approx
-\varepsilon\tau_{\rm NS}^2(c_0-c_{\rm NS}).
\]

Define the positive delay sweep speed

\[
v_\tau=-\frac{d\tau_3}{dn}.
\]

At the NS point,

\[
\boxed{
\frac{v_\tau}{\varepsilon}
=\tau_{\rm NS}^2(c_0-c_{\rm NS})
=5.80934608827\times10^{-5}.
}
\tag{V1223}
\]

Approximating

\[
\tau_3(n)=\tau_{\rm NS}-v_\tau n,
\]

gives

\[
\beta_1(n)\approx |s_\tau|v_\tau n.
\]

Hence the linearized envelope amplification accumulated before the frozen FIC is

\[
\boxed{
G_{\rm NS\to FIC}
=\log\frac{A(\tau_{\rm FIC})}{A_0}
\approx
\frac{|s_\tau|W_\tau^2}{2v_\tau}.
}
\tag{V1224}
\]

Equating this optimistic linear gain to

\[
\log(A_{\rm FIC}^{\rm exact}/A_0)
\]

gives

\[
\boxed{
\varepsilon_{\rm lin}
\approx6.7979341\times10^{-9}.
}
\tag{V1225}
\]

Thus even the **optimistic linear** estimate says that adaptation must occur on a scale of order

\[
1/\varepsilon\sim10^8
\]

cycles before the fast mode has enough residence time inside the local NS--FIC window to grow from `10^-3` to the fold amplitude.

Because the cubic term slows radial growth as the stable circle is approached, (V1225) is an upper bound on the actual tracking rate.

---

# 5. Nonlinear delayed passage and dynamic FIC skip

Integrate the coupled reduced system (V1213), (V1217) from

\[
\tau_3(0)=\tau_{\rm NS},
\qquad
A(0)=10^{-3}.
\]

Define `90% tracking` by

\[
A(\tau_{\rm FIC})=0.9A_{\rm FIC}^{\rm exact}.
\tag{V1226}
\]

Without activity feedback,

\[
\boxed{
\varepsilon_{90}^{(\kappa=0)}
\approx1.730295\times10^{-9}.
}
\tag{V1227}
\]

With `kappa=2e-6`,

\[
\boxed{
\varepsilon_{90}^{(\kappa>0)}
\approx5.82640\times10^{-10}.
}
\tag{V1228}
\]

So the activity-dependent speed-up requires adaptation to be approximately

\[
\boxed{2.97\times}
\]

slower to achieve the same 90% adiabatic tracking criterion.

For the representative still-slow value

\[
\varepsilon=10^{-6},
\]

the no-feedback system reaches the static FIC after about

\[
1.50022\times10^5
\]

cycles with

\[
\boxed{A_{\rm FIC,dyn}\approx0.001031914.}
\tag{V1229}
\]

The activity-feedback case gives

\[
\boxed{A_{\rm FIC,dyn}\approx0.001031825.}
\tag{V1230}
\]

Both are only about

\[
\boxed{1.56\%}
\]

of the frozen fold amplitude.

Therefore the adaptive trajectory has crossed the entire static stable-circle window while remaining essentially near the synchronous state. This is the first CORE example of a **dynamic bifurcation skip** caused by slow passage.

---

# 6. Activity-dependent myelination accelerates the escape trigger

At the frozen fold amplitude,

\[
H(A_{\rm FIC}^2)\approx0.8290141.
\]

Relative to the no-activity speed drift at the NS point, the plasticity term increases the instantaneous conduction-speed drive by

\[
\boxed{
\frac{c_0-c_{\rm NS}+\kappa H(A_{\rm FIC}^2)}
{c_0-c_{\rm NS}}
\approx2.79995.
}
\tag{V1231}
\]

To quantify the post-FIC local escape, define the boundary of validity of the small-amplitude chart by

\[
A_{\rm esc}=0.1.
\tag{V1232}
\]

For `epsilon=1e-6`, after the static FIC is crossed, the reduced model reaches `A=0.1` after approximately

\[
\boxed{2.39940\times10^6\ \text{cycles}}
\]

without feedback, versus

\[
\boxed{2.16462\times10^6\ \text{cycles}}
\]

with activity-dependent speed-up.

The feedback therefore shortens the post-FIC escape lag by approximately

\[
\boxed{9.78\%.}
\tag{V1233}
\]

The corresponding delays at the escape threshold are approximately

\[
\tau_{\rm esc}^{(\kappa=0)}=7.94135827600,
\]

\[
\tau_{\rm esc}^{(\kappa>0)}=7.94132289898.
\tag{V1234}
\]

The second trajectory is driven much deeper beyond the frozen FIC because activity increases conduction speed.

CORE does not identify the attractor reached after `A=0.1`; that requires a global adaptive-event calculation. v0.12 certifies only the local escape trigger.

---

# 7. Important negative result: no local sync/circle hysteresis

The local quintic Chenciner geometry with `L2>0` has the following stable objects on the fixed-`p` slice:

- `tau_3 > tau_NS`: stable synchrony;
- `tau_FIC < tau_3 < tau_NS`: unstable synchrony plus a stable inner invariant circle and an unstable outer circle;
- `tau_3 < tau_FIC`: no small invariant circle and unstable synchrony.

There is therefore **no interval in the local v0.12 chart in which stable synchrony and the stable small invariant circle coexist**.

Consequently,

\[
\boxed{\text{local Chenciner geometry alone does not provide stable sync/circle hysteresis.}}
\tag{V1235}
\]

Any hysteresis or relaxation switching seen in a full adaptive Lighthouse network must involve at least one of:

1. a more global phase-locked or modulated branch outside this local chart;
2. a second slow variable or a more structured plasticity law;
3. another mode or event itinerary;
4. a genuinely global return mechanism.

This negative result prevents CORE from incorrectly labeling delayed passage as hysteresis.

---

# 8. Synergetic interpretation

The reduced adaptive system is

\[
\boxed{
\frac{dA}{dn}
=A[\beta_1(c)+\beta_2A^2+L_2A^4],
\qquad
\frac{dc}{dn}
=\varepsilon[c_0-c+\kappa H(A^2)].
}
\tag{V1236}
\]

The roles are distinct:

- `A` is the fast collective timing order parameter;
- `c` or `tau_3=1/c` is a slow structural state;
- the frozen exact Lighthouse bifurcation atlas is the fast skeleton;
- slow passage determines whether the system can actually realize the frozen attractors.

This is a concrete refinement of the slaving picture: a frozen attracting branch need not be dynamically observable under slow adaptation if its basin is entered too late or its residence window is too short compared with the critical-mode growth time.

---

# 9. Benchmark contract B151--B166

- **B151**: fix `p=-3.267985407948901` and retain the exact v0.11 FIC at `tau_FIC=7.94140373739`.
- **B152**: recover the frozen NS point at the same `p` within documented tolerances.
- **B153**: recover `W_tau=8.09303591698e-6`.
- **B154**: recover `d(|mu|-1)/d tau approx -0.05053354353` at fixed `p`.
- **B155**: recover `beta2_eff approx -1.87741497471e-4` from exact NS--FIC calibration.
- **B156**: recover `A_FIC_cal approx 0.066005552315` and relative error `<1e-3` against the exact fold amplitude.
- **B157**: implement the speed-state convention `tau_3=1/c` and saturating activity proxy `H(u)=u/(u+u_s)`.
- **B158**: recover the no-activity sweep factor `v_tau/epsilon approx 5.80934608827e-5`.
- **B159**: recover the optimistic linear capture estimate `epsilon_lin approx 6.797934e-9` for `A0=1e-3`.
- **B160**: recover the nonlinear 90% tracking threshold `epsilon90 approx 1.7303e-9` without activity feedback.
- **B161**: recover the 90% threshold `epsilon90 approx 5.8264e-10` for `kappa=2e-6`.
- **B162**: at `epsilon=1e-6`, verify `A(tau_FIC)/A_FIC <0.02`.
- **B163**: at `epsilon=1e-6`, verify activity feedback shortens the post-FIC escape lag to `A=0.1`.
- **B164**: recover the local activity-driven speed-up factor near the fold, approximately `2.79995`.
- **B165**: do not call the local NS/FIC transition hysteretic unless two stable frozen attractors coexist over a common parameter interval.
- **B166**: do not interpret `A>0.1` with the local quintic chart; transition destination must be established by a broader exact adaptive-event model.

---

# 10. Next step

v0.12 closes the reduced slow--fast part of WP6.4 but not the full adaptive-event validation.

The next CORE target should be **state-dependent-delay event dynamics** with actual spikes in flight while conduction speed changes. The exact v0.11 frozen state-space map provides the local fast component, but a correct adaptive simulator must also specify how changes in `c(t)` alter the arrival time of a spike already propagating on an axon.

Only after that semantic issue is fixed can CORE compare

\[
\text{full adaptive event network}
\quad\text{vs}\quad
\text{v0.12 slow--fast reduction}
\]

for dynamic skip, delayed onset, global switching and genuine hysteresis.

## Reference

S. Coombes, R. Thul, S. Ruschel, R. Nicks, *Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks*, arXiv:2606.21508 (2026).
