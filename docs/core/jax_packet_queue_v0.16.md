# CORE fixed-capacity JAX packet queue and event tangents v0.16

## Purpose

CORE v0.16 converts the imperative scientific oracle of v0.14/v0.15 into a shape-static JAX event engine without changing the mathematical model. The target is not generic differentiability through event-order changes. The target is stricter and more useful:

1. exact-value agreement with the causal packet semantics already certified by CORE;
2. a fixed-capacity queue suitable for `jit`, `lax.while_loop`, `vmap`, and accelerator execution;
3. explicit event charts whose continuous tangent maps are differentiable inside one fixed event itinerary;
4. quantitative reproduction of the v0.14 dynamic-skip benchmark and the v0.15 global invariant-circle multipliers/fold.

The central implementation rule is

> discrete event labels define a local chart; JAX differentiates the continuous state inside that chart, not across an event-order switching surface.

This keeps exact hybrid science separate from any future globally smoothed surrogate.

### Provenance

- **[H/C]** Lighthouse phase dynamics and delayed alpha-synapse interactions.
- **[C]** adaptive conduction-speed motivation.
- **[P]** remaining-distance packet semantics from v0.13.
- **[P]** full imperative packet scheduler from v0.14.
- **[P]** global hybrid invariant-circle fold from v0.15.
- **[P]** fixed-capacity JAX queue, masked event charts, and chart-tangent implementation introduced here.

---

# 1. Shape-static packet state

For the three-cell benchmark choose a compile-time queue capacity

\[
\boxed{Q_{\max}=12.}
\tag{JQ1}
\]

The v0.14 large-circle audit observed at most six packets simultaneously, so the reference has a factor-two capacity margin.

Every slot `k=1,...,Qmax` stores

\[
(m_k,s_k,t_k,w_k,\rho_k,\kappa_k),
\tag{JQ2}
\]

where

- `m_k` is an active mask;
- `s_k,t_k` are source/target integer labels;
- `w_k` is the packet weight;
- `rho_k` is remaining anatomical distance;
- `kappa_k` selects the short fixed-speed or long adaptive edge.

The full continuous vector used for differentiation is

\[
\boxed{
x=(\phi_1,\ldots,\phi_N,\psi_1,\ldots,\psi_N,
q_1,\ldots,q_N,c,\rho_1,\ldots,\rho_{Q_{\max}}).
}
\tag{JQ3}
\]

Masks and integer packet labels are **chart data**, not differentiable variables.

A queue insertion uses the first free slot in deterministic source order. If no slot is free, the reference raises a hard overflow flag; it never silently overwrites a live packet.

---

# 2. Continuous exact flow

The neural/synaptic flow remains

\[
\dot\phi_i=S(\psi_i),
\qquad
\dot\psi_i=-\alpha\psi_i+q_i,
\qquad
\dot q_i=-\alpha q_i,
\tag{JQ4}
\]

with `alpha=0.5`. The alpha-state flow is exact,

\[
q_i(t+\Delta)=e^{-\alpha\Delta}q_i(t),
\tag{JQ5}
\]

\[
\psi_i(t+\Delta)=e^{-\alpha\Delta}[\psi_i(t)+q_i(t)\Delta].
\tag{JQ6}
\]

The phase gain is evaluated with the same 20-point Gauss rule used by the v0.14 oracle. Thus numerical differences between v0.14 and v0.16 measure queue/scheduler implementation error rather than a change of quadrature model.

For the project slow conduction law,

\[
\dot c=\lambda[c_{\rm eq}(A_h)-c],
\qquad
\lambda=\varepsilon/T_{\rm NS},
\tag{JQ7}
\]

and fixed held cycle activity `Ah`, the speed flow and travelled distance are evaluated analytically. Long packets therefore obey exactly

\[
\rho(t+\Delta)=\rho(t)-\int_t^{t+\Delta}c(u)\,du.
\tag{JQ8}
\]

---

# 3. Global value scheduler

For every active queue slot the arrival time is computed from its local packet chart. A short packet has

\[
\Delta_a=\rho/(1/2).
\tag{JQ9}
\]

For a long adaptive packet the unique root satisfies

\[
\int_0^{\Delta_a}c(t+s)\,ds=\rho.
\tag{JQ10}
\]

The value kernel uses a fixed-iteration Newton solve on the exact distance integral; positivity of speed gives the same unique causal root as v0.13.

For each neuron, a firing root solves

\[
\phi_i+\int_0^{\Delta_f}S(\psi_i(s))\,ds=2\pi.
\tag{JQ11}
\]

A 58-step bisection is used for the value scheduler. The next global event is

\[
\boxed{\Delta=\min(\Delta_a,\Delta_f).}
\tag{JQ12}
\]

All arrivals at that time are applied additively, followed by every firing surface already reached at the same time. This reproduces the deterministic batch policy of v0.14.

The entire event loop can be executed inside `jax.lax.while_loop`. No Python packet objects or dynamically resized arrays are required.

---

# 4. Differentiable event roots

A raw bisection has a correct root value but an unusable automatic derivative because its branch decisions are discrete. CORE therefore separates **value root** and **chart derivative**.

For firing, the robust bisection root is used as a stop-gradient initializer and then refined by differentiable Newton iterations. If

\[
G_i(\Delta;x)=
\phi_i+\int_0^\Delta S(\psi_i(s;x))ds-2\pi=0,
\tag{JQ13}
\]

then

\[
\frac{\partial G_i}{\partial\Delta}
=S(\psi_i(\Delta)).
\tag{JQ14}
\]

Implicit differentiation gives, in particular,

\[
\boxed{
\frac{\partial\Delta_f}{\partial\phi_i}
=-\frac{1}{S(\psi_i(\Delta_f))}.
}
\tag{JQ15}
\]

In the direct v0.16 chart test,

\[
\frac{\partial\Delta_f}{\partial\phi_i}
=-2.288917537509386,
\]

while the independent endpoint-velocity expression gives

\[
-2.288917546306807.
\]

The absolute discrepancy is below `9e-9`.

For a frozen long packet,

\[
\Delta_a=\rho/c,
\]

so

\[
\boxed{
\frac{\partial\Delta_a}{\partial\rho}=\frac1c,
\qquad
\frac{\partial\Delta_a}{\partial c}=-\frac{\rho}{c^2}.
}
\tag{JQ16}
\]

At the direct chart test with `c=1/8`, JAX returns

\[
\boxed{
\partial_\rho\Delta_a=8,
\qquad
\partial_c\Delta_a=-47.87198569561542,
}
\tag{JQ17}
\]

exactly matching the analytical values.

For genuinely evolving speed, the derivative reduces to the v0.13 identity

\[
\delta a=
\frac{c(s)\delta s-\int_s^a\delta c(u)du}{c(a)}.
\tag{JQ18}
\]

---

# 5. Event-chart tangent and saltation

Let `sigma` denote a fixed event chart: the next event type/index, the arrival batch, the firing batch, and the queue slots assigned to any newly emitted packets are held fixed. Define

\[
\mathcal P_\sigma(x)
=R_\sigma\!\left(\Phi_{\tau_\sigma(x)}(x)\right).
\tag{JQ19}
\]

If `h_sigma=0` is the selected event surface, then

\[
D\tau_\sigma
=-\frac{Dh_\sigma\,D_x\Phi_\tau}
{Dh_\sigma\,f^-}.
\tag{JQ20}
\]

The event-section tangent is

\[
\boxed{
D\mathcal P_\sigma
=DR_\sigma
\left[D_x\Phi_\tau+f^-\otimes D\tau_\sigma\right].
}
\tag{JQ21}
\]

For continuous-time perturbations synchronized at the same physical time, the corresponding standard saltation matrix is

\[
\boxed{
\mathcal S_\sigma
=DR_\sigma+
\frac{(f^+-DR_\sigma f^-)n^T}{n^Tf^-}.
}
\tag{JQ22}
\]

CORE keeps (JQ21) and (JQ22) conceptually distinct. The reference code differentiates the event-section chart directly with JAX; the same chart data can also be used to assemble explicit saltation matrices.

### Direct derivative audit

For a generic single-firing chart, a random JAX JVP differs from a central finite-difference directional derivative by

\[
\boxed{9.96\times10^{-10}\ \text{relative}.}
\tag{JQ23}
\]

For a generic single adaptive-arrival chart, the corresponding error is

\[
\boxed{1.59\times10^{-10}\ \text{relative}.}
\tag{JQ24}
\]

Thus the fixed-chart tangent implementation is numerically closed well below the tolerances relevant to the later Floquet and circle benchmarks.

---

# 6. Frozen-value recovery

At the exact v0.12/v0.14 NS delay,

\[
\tau_{\rm NS}=7.941411830425917,
\]

the JAX packet engine gives

\[
\boxed{T_{\rm JAX}=16.297496054830845.}
\tag{JQ25}
\]

Against

\[
T_{\rm ref}=16.297496058505022,
\]

the absolute period error is

\[
\boxed{3.67418\times10^{-9}.}
\tag{JQ26}
\]

This is essentially identical to the imperative v0.14 recovery error.

---

# 7. Full JAX dynamic-skip reproduction

Prepare the same physical q=1 center seed as v0.14. The compiled JAX system obtains

\[
A_0=0.0010023850245501774.
\tag{JQ27}
\]

For

\[
\varepsilon=10^{-5},\qquad \kappa=0,
\]

the exact packet scheduler requires `15002` completed spike cycles to cross the static FIC delay. At crossing,

\[
\boxed{A_{\rm FIC}^{\rm JAX}=0.001005850800989724.}
\tag{JQ28}
\]

The v0.14 imperative oracle gave approximately

\[
A_{\rm FIC}^{\rm imp}=0.00100586082225.
\]

Hence

\[
\boxed{
\frac{A_{\rm JAX}-A_{\rm imp}}{A_{\rm imp}}
\approx-9.96\times10^{-6}.
}
\tag{JQ29}
\]

And relative to the static frozen fold amplitude,

\[
\boxed{
A_{\rm FIC}^{\rm JAX}/0.0660575
=0.01522689779.
}
\tag{JQ30}
\]

Thus the dynamic bifurcation skip survives the transition from an imperative variable-length packet list to a fully shape-static JAX queue.

---

# 8. Global-circle normal multipliers in JAX

The v0.15 large hybrid circle crosses an arrival-order switching surface, so its normal stability is again measured directly from the piecewise-smooth packet dynamics rather than from one globally fixed itinerary.

The v0.16 JAX values are

| `tau3` | v0.15 oracle | v0.16 JAX |
|---:|---:|---:|
| 8.00400 | 0.78431228 | 0.78525152 |
| 8.00600 | 0.86499368 | 0.86727584 |
| 8.00700 | 0.93581548 | 0.93574062 |
| 8.00720 | 0.96123381 | 0.96125129 |
| 8.00725 | 0.97179225 | 0.97111484 |

The maximum absolute discrepancy is

\[
\boxed{2.2822\times10^{-3}.}
\tag{JQ31}
\]

Close to the fold the agreement is much tighter; at `tau3=8.0072` the difference is about `1.75e-5`.

Fitting the JAX multipliers to

\[
1-\mu_{\perp,s}
=K\sqrt{\tau_F-\tau_3}
\tag{JQ32}
\]

gives, from all five points,

\[
K=3.7128212721,
\qquad
\tau_F^{(5),\rm JAX}=8.0073083884,
\tag{JQ33}
\]

and from the three closest points,

\[
\boxed{
K=3.6307003884,
\qquad
\tau_F^{(3),\rm JAX}=8.0073134826.
}
\tag{JQ34}
\]

The latter differs from the v0.15 multiplier fit by only about `2.8e-6` and from the independent escape-ghost value by about `3.1e-6`.

---

# 9. Repelling basin-edge circle

Using the same deterministic JAX large-circle state at `tau3=8.0072`, two radial impulses separated by only

\[
2.3193\times10^{-7}
\]

can be chosen on opposite sides of the basin boundary. Their phase-section separation grows with the direct JAX estimate

\[
\boxed{
\mu_{\perp,u,\rm rot}^{\rm JAX}\approx1.03831.
}
\tag{JQ35}
\]

The v0.15 imperative value was

\[
1.04004099.
\]

Thus JAX independently preserves

\[
\boxed{
\mu_{\perp,s}<1<\mu_{\perp,u}
}
\tag{JQ36}
\]

on the two global circle branches.

---

# 10. What JAX differentiation means at an event-order switch

The fixed-capacity representation removes dynamic memory shape, but it does **not** make hybrid dynamics globally smooth.

At a surface where two candidate events exchange order, the chart label `sigma` changes. Therefore

\[
D\mathcal P_{\sigma_-}
\neq
D\mathcal P_{\sigma_+}
\]

in general. A naive gradient through `argmin` or through a hard mask has no invariant mathematical meaning exactly on the switching surface.

CORE v0.16 therefore certifies:

- exact values across chart switches;
- one-sided continuous-state derivatives inside each regular chart;
- direct trajectory-based normal multipliers for the global hybrid circle;
- explicit event-time derivatives and fixed-chart tangent maps.

It does **not** claim one globally smooth gradient through arrival-order collision surfaces.

Likewise, additive simultaneous-event batches are value-commutative in the present benchmark, but a fully general tangent theory for arbitrary simultaneous surfaces requires a generalized/multi-surface saltation construction. That remains separate from the regular single-chart tests above.

---

# 11. Benchmark contract B225--B246

**B225 — fixed queue capacity.** The JAX reference uses compile-time `Qmax=12`.

**B226 — mask semantics.** Active status and integer packet labels are discrete chart data; only continuous neural/conduction/distance variables are differentiated.

**B227 — deterministic allocation.** Packet creation uses first-free slot allocation in deterministic source order.

**B228 — overflow semantics.** Queue exhaustion is a hard benchmark failure; no live packet may be overwritten.

**B229 — causal propagation.** Active long packets satisfy the exact v0.13 remaining-distance integral.

**B230 — fixed-speed recovery.** `epsilon=0` gives `Delta=rho/c` exactly on adaptive slots.

**B231 — value firing root.** The global value scheduler uses a robust bisection root for firing events.

**B232 — differentiable firing root.** Fixed-chart differentiation uses stop-gradient value initialization followed by Newton refinement, recovering the implicit event derivative.

**B233 — firing-time derivative.** Equation (JQ15) is reproduced to `2e-7` absolute tolerance or better.

**B234 — arrival-time derivatives.** Equation (JQ16) is reproduced to numerical precision in the frozen benchmark.

**B235 — firing chart JVP.** A generic firing-chart JVP agrees with central finite differences to relative error below `2e-7`.

**B236 — arrival chart JVP.** A generic adaptive-arrival-chart JVP agrees with central finite differences to relative error below `2e-7`.

**B237 — frozen period.** The JAX period at `tau_NS` agrees with the exact reference within `1e-6`.

**B238 — queue margin.** No overflow occurs in the certified three-cell trajectories; the inherited observed active-packet maximum is six, below `Qmax=12`.

**B239 — center seed.** The JAX center preparation returns `A0≈0.0010023850`.

**B240 — dynamic skip.** At `epsilon=1e-5`, the JAX packet network reaches the static FIC with less than `2%` of the frozen fold amplitude.

**B241 — imperative/JAX skip agreement.** The FIC-crossing amplitude differs from the v0.14 oracle by less than `3e-5` relative.

**B242 — stable circle multiplier.** At `tau3=8.0072`, direct JAX reconstruction gives `mu_perp,s,rot≈0.96125`, within `8e-4` of v0.15.

**B243 — stable multiplier table.** The stored five-point JAX table differs from the v0.15 oracle by less than `3e-3` in absolute multiplier value.

**B244 — global fold location.** The three-point JAX multiplier fit gives `tau_F` within `5e-6` of both the v0.15 multiplier and ghost-escape estimates.

**B245 — unstable basin-edge circle.** Direct JAX edge tracking at `tau3=8.0072` gives a full-rotation factor between `1.02` and `1.06` and remains consistent with the v0.15 value `1.04004`.

**B246 — hybrid derivative scope.** No globally smooth derivative is claimed on event-order switching surfaces or generic simultaneous-event intersections; gradients are chartwise/one-sided there.

---

# 12. Next CORE step

The main mathematical architecture is now sufficient for large-scale implementation. CORE v0.17 should move from the three-cell reference to a **batched graph kernel**:

1. edge-indexed fixed-capacity packet tensors for arbitrary sparse graphs;
2. vectorized packet propagation and masked reductions;
3. graph-level overflow/capacity bounds;
4. batched event-chart tangent propagation;
5. exact-vs-JAX tests on rings with increasing `N`;
6. first gradient-based parameter inference benchmark using event times, while explicitly avoiding chart-switch singularities.

The acceptance criterion remains normal-form/event-geometry fidelity, not trajectory similarity alone.
