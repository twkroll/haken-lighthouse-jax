# CORE in-flight conduction semantics v0.13

## Purpose

CORE v0.13 makes adaptive propagation causally explicit.  Previous CORE stages used frozen delays or a slow conduction-speed variable through the kinematic relation

\[
\tau_{ij}=\ell_{ij}/c_{ij}.
\]

That is sufficient for frozen bifurcation theory and for the reduced slow-fast benchmark of v0.12, but it does not by itself specify what happens to a spike that is already travelling when `c_ij(t)` changes.

The 2026 adaptive Lighthouse paper of Coombes, Thul, Ruschel and Nicks motivates activity-dependent conduction speeds and formulates the adaptive problem with `tau_ij(t)=d_ij/c_ij(t)` as a state-dependent delay system.  CORE v0.13 adds a distinct project-level event semantics for discrete spikes in flight.  It is not claimed to reproduce the authors' internal simulation convention.

The core rule is:

> A spike packet carries **remaining anatomical distance**, not a delay timestamp that is frozen at emission.

---

# 1. Packet state

For every emitted spike from node `j` along directed edge `(i,j)` of fixed anatomical length `ell_ij>0`, create a packet `P` with emission time `s_P` and remaining distance

\[
\rho_P(s_P)=\ell_{ij}.
\tag{IF1}
\]

While the packet is in flight,

\[
\boxed{\dot\rho_P(t)=-c_{ij}(t).}
\tag{IF2}
\]

The packet arrives at the first time `a_P>s_P` satisfying

\[
\boxed{\rho_P(a_P)=0,}
\tag{IF3}
\]

or equivalently

\[
\boxed{\int_{s_P}^{a_P}c_{ij}(u)\,du=\ell_{ij}.}
\tag{IF4}
\]

This is the canonical CORE v0.13 in-flight propagation law.

If

\[
c_{ij}(t)\ge c_{\min}>0
\]

and `c_ij` is continuous, then the accumulated distance is strictly increasing and every emitted packet has a unique finite arrival time.  The arrival surface is transversal because

\[
\dot\rho_P(a_P^-)=-c_{ij}(a_P)<0.
\tag{IF5}
\]

Thus state-dependent conduction does not create an ambiguity in the next-arrival event so long as speed remains strictly positive and simultaneous-event ties are handled by an explicit event policy.

---

# 2. Network event semantics

The adaptive event state consists of

1. Lighthouse phase / synaptic states;
2. conduction variables `c_ij`;
3. plasticity/activity variables used to evolve `c_ij`;
4. a finite set of active packets, each storing `(source,target,weight,rho)`.

For an alpha synapse we retain the smooth state-space realization

\[
\dot q_i=-\alpha q_i,
\qquad
\dot\psi_i=-\alpha\psi_i+q_i.
\tag{IF6}
\]

A packet arrival from `j` to `i` with weight `w_ij` produces

\[
q_i^+=q_i^-+w_{ij}\alpha^2.
\tag{IF7}
\]

A firing event at node `j` creates one packet on each outgoing edge.  Conduction speed then continues to evolve while every existing packet's remaining distance is advected by (IF2).

The next hybrid event is the earliest among

- a Lighthouse threshold crossing;
- a packet arrival `rho_P=0`;
- any explicitly modelled discontinuity of the plasticity law.

CORE v0.13 assumes the speed law is continuous, so speed updates do not themselves require jump events.

### Same-edge FIFO property

All packets already present on one edge experience the same instantaneous speed `c_ij(t)`.  Their pairwise remaining-distance differences are therefore constant between emissions and arrivals.  Hence packets emitted in temporal order cannot overtake one another on the same edge.  Arrival re-ordering can occur only between different edges or at simultaneous-event surfaces.

---

# 3. Arrival sensitivities

Define

\[
F(a,s;\xi)
=\int_s^a c(u;\xi)\,du-\ell=0,
\tag{IF8}
\]

where `xi` denotes any parameter or upstream state that affects conduction speed.

Implicit differentiation gives

\[
\boxed{
\frac{\partial a}{\partial s}
=\frac{c(s)}{c(a)}
}
\tag{IF9}
\]

for an externally prescribed speed profile.

More generally,

\[
\boxed{
\delta a
=\frac{c(s)\,\delta s-
\displaystyle\int_s^a\delta c(u)\,du}{c(a)}.
}
\tag{IF10}
\]

Equation (IF10) is the event-time sensitivity needed by an exact adaptive Floquet / return-map implementation.  When `c` is itself a dynamical state, `delta c` is obtained from the variational equation of the plasticity subsystem.

---

# 4. Relation to two simpler delay conventions

Let a packet be emitted at time `s`, let

\[
c_s=c(s),\qquad
\tau_s=\ell/c_s,
\]

and suppose locally

\[
c(s+t)=c_s+\gamma t+O(t^2).
\tag{IF11}
\]

Three distinct conventions are then possible.

## 4.1 Launch-frozen delay

Freeze the speed at emission:

\[
\Delta_{\rm launch}=\tau_s.
\tag{IF12}
\]

## 4.2 Physical in-flight propagation

The path-integral rule gives

\[
\ell=c_s\Delta+\frac12\gamma\Delta^2,
\]

hence

\[
\boxed{
\Delta_{\rm path}
=\frac{2\ell}{c_s+\sqrt{c_s^2+2\gamma\ell}}.
}
\tag{IF13}
\]

For slow adaptation,

\[
\boxed{
\Delta_{\rm path}
=\tau_s-
\frac12\frac{\gamma}{c_s}\tau_s^2
+O(\gamma^2).
}
\tag{IF14}
\]

## 4.3 Instantaneous-delay / DDE sampling convention

If a delayed spike is sampled through

\[
s=a-\ell/c(a),
\]

then `Delta=a-s` obeys

\[
\Delta=\frac{\ell}{c_s+\gamma\Delta},
\]

so

\[
\boxed{
\Delta_{\rm current}
=\frac{2\ell}{c_s+\sqrt{c_s^2+4\gamma\ell}}.
}
\tag{IF15}
\]

and

\[
\boxed{
\Delta_{\rm current}
=\tau_s-
\frac{\gamma}{c_s}\tau_s^2
+O(\gamma^2).
}
\tag{IF16}
\]

Therefore, for increasing speed (`gamma>0`),

\[
\boxed{
\Delta_{\rm current}
<\Delta_{\rm path}
<\Delta_{\rm launch}.
}
\tag{IF17}
\]

To first order the physical path correction is exactly half the instantaneous-current-delay correction.  This provides a simple diagnostic for adaptive-delay implementations.

---

# 5. Controlled propagation benchmark

Use the v0.12 frozen NS speed

\[
\tau_{\rm NS}=7.941411830425917,
\qquad
c_{\rm NS}=1/\tau_{\rm NS}
=0.125922193855846,
\]

with unit path length.  Choose a controlled linear ramp whose fractional speed change over one frozen transit is

\[
\chi=\frac{\gamma\ell}{c_{\rm NS}^2}=10^{-2}.
\tag{IF18}
\]

Then

\[
\gamma=1.5856398905469225\times10^{-4}.
\]

The three transit times are

\[
\boxed{
\Delta_{\rm launch}=7.941411830425917,
}
\tag{IF19}
\]

\[
\boxed{
\Delta_{\rm path}=7.902096946944075,
}
\tag{IF20}
\]

\[
\boxed{
\Delta_{\rm current}=7.863547366887612.
}
\tag{IF21}
\]

Thus the conventions are observably different once adaptation is not asymptotically slow.

At this ramp the emission-time sensitivity of the physical arrival is

\[
\boxed{
\frac{da}{ds}=\frac{c(s)}{c(a)}
\approx0.990147542976674.
}
\tag{IF22}
\]

---

# 6. v0.12 adaptive-scale audit

The v0.12 slow benchmark uses

\[
\frac{dc}{dn}
=\varepsilon[c_0-c+\kappa H(A^2)],
\]

with

\[
\varepsilon=10^{-6},\quad
A=10^{-3},\quad
c_0=0.1259231150089354,\quad
\kappa=2\times10^{-6},\quad
H(u)=\frac{u}{u+9\times10^{-4}}.
\]

Converting cycle index `n` to physical time locally with the frozen period

\[
T_{\rm NS}=16.297496058505022
\]

gives

\[
\dot c(s)
\approx5.66573443\times10^{-14}.
\tag{IF23}
\]

If `A` is frozen during the transit, the speed law is locally an exactly solvable exponential relaxation.  Solving the distance integral gives

\[
\boxed{
\Delta_{\rm path}^{v0.12}
\approx7.941411830411729.
}
\tag{IF24}
\]

Hence the launch-frozen approximation overestimates one transit by only

\[
\boxed{
\Delta_{\rm launch}-\Delta_{\rm path}^{v0.12}
\approx1.4188\times10^{-11}.
}
\tag{IF25}
\]

The exact frozen NS--FIC delay window from v0.12 is

\[
W_\tau=8.09303591698\times10^{-6}.
\]

Therefore

\[
\boxed{
\frac{\Delta_{\rm launch}-\Delta_{\rm path}^{v0.12}}{W_\tau}
\approx1.7531\times10^{-6}.
}
\tag{IF26}
\]

This is the main v0.13 robustness result:

> At the v0.12 test adaptation rate, in-flight propagation changes a single long-edge transit by less than two parts in a million of the already tiny frozen NS--FIC window.

Thus the v0.12 dynamic-bifurcation-skip conclusion is not caused by having ignored within-flight speed evolution.

At the much slower v0.12 90%-tracking threshold the relative correction is smaller still, of order `3e-9` of the frozen NS--FIC window.

---

# 7. What is and is not certified

Certified in v0.13:

- causal remaining-distance packet semantics;
- unique arrival for continuous positive speed;
- exact event-time sensitivity formula;
- same-edge FIFO/no-overtaking property;
- analytical comparison with launch-frozen and instantaneous-current delay conventions;
- exact linear-ramp benchmark;
- quantitative robustness of the v0.12 slow-passage result to in-flight propagation.

Not yet certified:

- a long full-network adaptive Lighthouse trajectory with all packets explicitly queued;
- plasticity driven by the full edge activity functional of the 2026 paper while packets are simultaneously in flight;
- global post-Chenciner switching destination;
- genuine adaptive hysteresis.

Those require the full packet-queue simulator rather than a one-flight propagation audit.

---

# 8. Benchmark contract B167--B182

**B167 — packet state.** Every emitted delayed spike carries remaining distance `rho`, not a precomputed immutable arrival time.

**B168 — propagation ODE.** `rho_dot=-c_ij(t)`.

**B169 — arrival condition.** Arrival is the first zero of `rho`.

**B170 — fixed-speed recovery.** Constant `c` gives `Delta=ell/c` exactly.

**B171 — positivity/transversality.** Require `c>=c_min>0`; then every arrival is causal, unique and transversal.

**B172 — same-edge FIFO.** Packets on one edge cannot overtake under a common positive speed field.

**B173 — emission sensitivity.** For prescribed `c(t)`, `da/ds=c(s)/c(a)`.

**B174 — general sensitivity.** Equation (IF10) must be recovered by the adaptive variational implementation.

**B175 — linear-ramp physical delay.** Equation (IF13) is reproduced.

**B176 — current-delay comparison.** Equation (IF15) is reproduced and, for increasing speed, `Delta_current<Delta_path<Delta_launch`.

**B177 — first-order factor-two rule.** The physical correction is half the instantaneous-current correction at first order in speed drift.

**B178 — controlled numerical ramp.** Equations (IF19)--(IF21) are reproduced to reference tolerance.

**B179 — v0.12 physical drift.** At `epsilon=1e-6`, the one-flight speed derivative is approximately `5.66573443e-14`.

**B180 — v0.12 in-flight correction.** The one-flight transit correction is approximately `1.4188e-11`.

**B181 — dynamic-skip robustness.** The correction/window ratio is below `2e-6`.

**B182 — scope.** v0.13 does not certify the global adaptive attractor; that requires a complete packet-queue simulation.

---

# 9. Next CORE step

CORE v0.14 should implement the full adaptive event engine:

1. continuous Lighthouse/synapse/plasticity flow;
2. threshold-root detection;
3. packet creation at spikes;
4. remaining-distance propagation for every active packet;
5. arrival-root detection and alpha-state jumps;
6. deterministic simultaneous-event semantics;
7. AD/variational propagation through both firing and arrival events;
8. comparison against v0.12 for dynamic skip and against the 2026 adaptive model for branch following and switching.

Only after this event engine is validated should the project claim a full adaptive Lighthouse network rather than a frozen-atlas or reduced slow-fast approximation.
