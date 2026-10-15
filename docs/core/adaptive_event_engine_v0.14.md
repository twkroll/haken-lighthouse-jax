# CORE full adaptive packet-queue event engine and global bistability v0.14

## Purpose

CORE v0.14 closes the value-dynamics gap left by v0.13. The project now has a full event-driven three-cell Lighthouse reference in which neural phase and alpha-synapse states evolve continuously, emitted delayed spikes are explicit packets carrying remaining distance, conduction speed evolves while packets are in flight, and the next event is selected from firing and packet-arrival roots.

The benchmark also answers a question that v0.12 deliberately left open. The local Chenciner chart contains no stable-synchrony/stable-small-circle coexistence, but the full global event dynamics contains a much larger timing-modulated attractor that coexists with stable synchrony. Thus CORE now separates local slow-passage delay from genuine global hysteretic memory.

The model family remains

\[
S(x)=\exp[-1/(x+1)^2]H(x+1),\qquad \alpha=0.5,
\]

with three-cell circulant weights

\[
w_d=[1,p,-p],\qquad p=-3.267985407948901.
\]

The frozen references inherited from v0.11/v0.12 are

\[
T_{\rm NS}=16.297496058505022,
\qquad
\tau_{\rm NS}=7.941411830425917,
\]

and

\[
\tau_{\rm FIC}=7.94140373739,
\qquad
A_{\rm FIC}=0.0660575.
\]

### Provenance

- **[H/C]** Lighthouse phase dynamics and delayed alpha-synapse interactions.
- **[C]** Adaptive conduction-speed / state-dependent-delay motivation from Coombes, Thul, Ruschel and Nicks (2026), arXiv:2606.21508.
- **[P]** Remaining-distance packet semantics from v0.13 and the present packet-queue engine.
- **[P]** The simple activity gate used for regression remains a project benchmark and is not claimed to duplicate the paper's microscopic activity functional.

---

# 1. Full adaptive state

For neuron `i`, use

\[
(\phi_i,\psi_i,q_i),
\]

with

\[
\dot q_i=-\alpha q_i,
\qquad
\dot\psi_i=-\alpha\psi_i+q_i,
\qquad
\dot\phi_i=S(\psi_i).
\tag{AE1}
\]

The ring displacement convention is

\[
d=0:\quad w_0=1,\quad \tau_0=0,
\]

\[
d=1:\quad w_1=p,\quad \ell_1=1,\quad c_1=1/2,
\]

\[
d=2:\quad w_2=-p,\quad \ell_2=1,\quad c_2=c(t).
\tag{AE2}
\]

Every delayed emitted spike creates a packet

\[
P=(j,i,w,\rho,\text{edge type})
\]

with `rho=1`. For the long adaptive edge

\[
\boxed{\dot\rho=-c(t),}
\tag{AE3}
\]

whereas the short edge has `rho_dot=-1/2`. The zero-delay self-edge is applied directly as an alpha-state jump.

---

# 2. Continuous conduction and alpha flow

To reproduce the v0.12 cycle-scale law locally in physical time, define

\[
\lambda=\varepsilon/T_{\rm NS}
\]

and, while the held cycle activity `A_h` is fixed,

\[
\dot c=\lambda[c_{\rm eq}(A_h)-c],
\tag{AE4}
\]

with

\[
c_{\rm eq}(A_h)=c_0+\kappa H(A_h^2),
\qquad
H(u)=\frac{u}{u+0.03^2}.
\tag{AE5}
\]

Hence between hybrid events

\[
\boxed{c(t+\Delta)=c_{\rm eq}+(c(t)-c_{\rm eq})e^{-\lambda\Delta}.}
\tag{AE6}
\]

A long packet travels the exact distance

\[
\boxed{
D_c(\Delta)=c_{\rm eq}\Delta+(c-c_{\rm eq})\frac{1-e^{-\lambda\Delta}}{\lambda}.
}
\tag{AE7}
\]

Its arrival root solves `D_c(Delta)=rho`. At `lambda=0`, this reduces exactly to `Delta=rho/c`.

The alpha flow is also exact between events:

\[
q_i(t+\Delta)=e^{-\alpha\Delta}q_i(t),
\]

\[
\psi_i(t+\Delta)=e^{-\alpha\Delta}[\psi_i(t)+q_i(t)\Delta].
\tag{AE8}
\]

Only the phase gain

\[
\Delta\phi_i=\int_0^\Delta S\!\left(e^{-\alpha s}[\psi_i+q_is]\right)ds
\tag{AE9}
\]

is quadrature-evaluated. The reference uses 20-point Gauss--Legendre quadrature.

---

# 3. Global event scheduler

At every state compute all active packet arrival times and the earliest firing root that occurs before the next arrival. The global next event is

\[
\boxed{\Delta_*=\min\{\Delta_{\rm arrival},\Delta_{\rm firing}\}.}
\tag{AE10}
\]

A firing root is the first solution of

\[
\phi_i+\int_0^\Delta S(\psi_i(s))ds=2\pi.
\tag{AE11}
\]

The complete continuous state and every packet are advanced once to the common event time.

## Arrival batch

Every packet with `rho=0` is removed and produces

\[
q_i^+=q_i^-+w\alpha^2.
\tag{AE12}
\]

## Firing batch

Every neuron already on its firing surface at that same time obeys

\[
\phi_i^+=\phi_i^- -2\pi,
\tag{AE13}
\]

followed by the zero-delay self jump

\[
q_i^+=q_i^-+\alpha^2,
\tag{AE14}
\]

and creation of one short and one long packet.

The reference processes arrivals before firing. For the present Lighthouse jumps, the value result is order-independent at an exact tie: both jumps are additive in `q`, while neither changes `phi` instantaneously.

Same-edge FIFO follows from v0.13 because all packets on one edge share the same instantaneous speed.

---

# 4. Variational structure and simultaneous-event scope

Between generic non-simultaneous events,

\[
\delta\dot q=-\alpha\delta q,
\qquad
\delta\dot\psi=-\alpha\delta\psi+\delta q,
\qquad
\delta\dot\phi=S'(\psi)\delta\psi.
\tag{AE15}
\]

For the no-feedback conduction test,

\[
\delta\dot c=-\lambda\delta c,
\qquad
\delta\dot\rho=-\delta c.
\tag{AE16}
\]

For a smooth event surface `h(x)=0` with reset `R`, the generic saltation matrix is

\[
\boxed{
K=DR+\frac{f^+-DRf^-}{\nabla h^\top f^-}\nabla h^\top.
}
\tag{AE17}
\]

At packet arrival, `h=rho` and the denominator is `-c(a)<0`; the v0.13 identity

\[
\delta a=\frac{c(s)\delta s-\int_s^a\delta c(u)du}{c(a)}
\tag{AE18}
\]

is recovered. At firing, `h_i=phi_i-2pi` and the normal velocity is `S(psi_i)>0` for a regular crossing.

Packet creation/removal changes queue dimension. Differentiation can therefore use a fixed-capacity slot chart or a fixed-itinerary local chart. v0.14 documents the generic-event rule but does not yet claim a production global JAX tangent engine.

The primary `kappa=0` simultaneous batches have commuting resets and unchanged companion event surfaces/normal velocities. With the cycle-held activity statistic used for the project feedback regression, the speed remains continuous but the right-hand side changes at cycle completion. Value dynamics is certified; global AD through that feedback tie is deferred.

---

# 5. Frozen-delay recovery

Set

\[
\varepsilon=0,\qquad c=1/\tau_{\rm NS}.
\]

After synchronous alpha transients relax, the full packet engine gives

\[
\boxed{T_{\rm full}=16.297496054831527.}
\tag{AE19}
\]

Against the v0.12 reference,

\[
|T_{\rm full}-T_{\rm NS}|=3.6734953\times10^{-9},
\]

or `2.2540e-10` relative error. The last ten synchronous firing batches have zero measured inter-neuron spread at floating-point resolution.

Thus the new packet queue recovers the fixed-delay Lighthouse orbit in the frozen limit.

---

# 6. Critical-mode preparation

A direct phase perturbation contains stable history components as well as the critical `q=1` mode. v0.14 therefore prepares the center direction before adaptation.

At the frozen NS orbit prescribe

\[
\delta T_i=2A_0\cos(2\pi i/3),\qquad A_0=10^{-3},
\tag{AE20}
\]

and initialize

\[
\delta\phi_i=-\nu\delta T_i,
\qquad \nu=S(\psi_{\rm spike}).
\tag{AE21}
\]

After 20 frozen cycles the measured physical Fourier amplitude is

\[
\boxed{A_{\rm prep}=0.0010023850212674303.}
\tag{AE22}
\]

Adaptation begins only after this preparation.

---

# 7. Full event engine versus v0.12 slow envelope

The reduced model and the full packet engine start from the same measured `A_prep`.

| epsilon | full cycles to FIC | A_full at FIC | reduced n | A_red | relative amplitude difference |
|---:|---:|---:|---:|---:|---:|
| 1e-3 | 150 | 0.00100239957178 | 150.0217693 | 0.00100241651234 | -1.69e-5 |
| 3e-4 | 500 | 0.00100226543723 | 500.0725451 | 0.00100248999531 | -2.24e-4 |
| 1e-4 | 1500 | 0.00100250843898 | 1500.2176666 | 0.00100269997641 | -1.91e-4 |
| 1e-5 | 15002 | 0.00100586082225 | 15002.1768231 | 0.00100553902479 | +3.20e-4 |

Across the direct full-engine tests,

\[
\boxed{\frac{|A_{\rm full}-A_{\rm red}|}{A_{\rm red}}<3.3\times10^{-4}.}
\tag{AE23}
\]

The `1e-5` run is a separate slower reference invocation. At that rate,

\[
\boxed{\frac{A_{\rm full}(\tau_{\rm FIC})}{A_{\rm FIC}}=0.01522705.}
\tag{AE24}
\]

Only about 1.52% of the frozen fold amplitude has developed. The full packet network therefore directly exhibits the dynamic bifurcation skip.

v0.14 does not spend default reference runtime on a direct `1e-6` full-packet run. That point remains certified by v0.12 at reduced level; v0.13 independently showed that the physical within-flight correction there is only about `1.75e-6` of the frozen NS--FIC window. v0.14 now pushes the direct queue validation down to `1e-5`.

## Activity-feedback regression

For the project gate with `kappa=2e-6` and `epsilon=1e-4`, the full packet engine reaches the FIC after 1496 completed cycles with

\[
A_{\rm full}=0.0010027502580810417.
\]

The reduced benchmark gives `n=1496.3080138847185` and

\[
A_{\rm red}=0.0010026991354429421,
\]

so the relative amplitude discrepancy is only

\[
\boxed{5.10\times10^{-5}.}
\tag{AE25}
\]

---

# 8. Global timing-modulated attractor

v0.12 established a negative local statement: the quintic Chenciner chart has no interval in which stable synchrony and the stable **small** invariant circle coexist. That does not exclude a distant nonlinear attractor.

The full event engine reveals one.

At frozen

\[
\boxed{\tau_3=7.8}
\]

a small `q=1` seed leaves synchrony and approaches a bounded timing-modulated state. Over the final 500 cycles,

\[
\boxed{\langle A\rangle=0.8236549539772645,}
\tag{AE26}
\]

with standard deviation `0.067899049194926` and amplitude range approximately `0.71018` to `0.90067`.

v0.14 deliberately calls this a **large timing-modulated attractor**. It is not yet classified as a smooth invariant circle, a high-period orbit, or a chaotic set.

---

# 9. Genuine global bistability at tau3=8.0

Take the large state from `tau3=7.8`, set

\[
\boxed{\tau_3=8.0}
\]

and evolve another 2500 frozen cycles. The state remains strongly modulated:

\[
\boxed{\langle A\rangle_{\rm large}=0.7181453200202882,}
\tag{AE27}
\]

with standard deviation `0.04917740433409652` and amplitude range approximately `0.64435` to `0.78554`. Its mean cycle period is

\[
\boxed{\langle T\rangle_{\rm large}=16.223012090039237}
\tag{AE28}
\]

with standard deviation `0.01461101168239618`.

Now initialize the same frozen parameter value from synchrony with a `1e-3` `q=1` seed. After 2200 cycles, the final-200-cycle amplitude is

\[
\boxed{\langle A\rangle_{\rm sync\ basin}=2.1157\times10^{-6},}
\tag{AE29}
\]

with maximum `2.7941e-6`.

Therefore at exactly

\[
\boxed{p=-3.267985407948901,\qquad \tau_3=8.0}
\]

the full event system has both a stable/attracting synchronous state and a numerically attracting large timing-modulated state.

Since

\[
8.0-\tau_{\rm NS}=0.0585881695740831,
\]

this coexistence lies far outside the `8.1e-6`-wide local NS--small-FIC wedge. This is global frozen bistability, not slow-passage ambiguity.

## Hysteretic memory protocol

The same point `tau3=8.0` can be reached in two ways:

1. initialize near synchrony at 8.0 -> synchrony;
2. pass through the unstable regime at 7.8, acquire the large timing state, then return to 8.0 -> large timing state.

The final state depends on parameter history. CORE therefore permits the term

\[
\boxed{\text{global hysteretic memory}}
\]

for this protocol. This does not change the v0.12 local result: there is still no local synchrony/small-circle hysteresis in the quintic Chenciner chart.

---

# 10. Smoothness and queue audit of the large state

A 300-cycle exact interval audit at the large `tau3=8.0` state gives

\[
\psi_{\min}\approx-0.5344786744,
\qquad
\psi_{\max}\approx0.5730224021.
\]

The response threshold is `h=-1`, hence

\[
\boxed{\min(\psi+1)\approx0.4655213256>0.}
\tag{AE30}
\]

The benchmark therefore remains inside the smooth response region. The maximum number of active packets observed is six. The minimum event spacing in this audit is `3.78e-4`, so no Zeno-like clustering is observed.

---

# 11. Empirical upper persistence bracket

Starting from the established large `tau3=8.0` state:

- at `tau3=8.0073`, after 3000 cycles, `mean(A)=0.684803688`;
- at `tau3=8.0075`, after 6000 cycles, `mean(A)=1.7495e-4`, with final-window maximum below `3.58e-4`.

Thus the current finite-time continuation protocol gives

\[
\boxed{8.0073\lesssim\tau_{\rm loss}\lesssim8.0075.}
\tag{AE31}
\]

This is **not** a bifurcation classification. The boundary could be a fold of a large invariant circle, a basin-boundary collision, a crisis, or another global event. v0.14 stores only an empirical persistence bracket.

---

# 12. Relation to the adaptive Lighthouse literature

Coombes, Thul, Ruschel and Nicks (2026) show that activity-dependent conduction speed can reshape the attractor structure of Lighthouse networks and generate long-time switching between phase-locked patterns. CORE v0.14 is consistent with that organizing picture but remains distinct: already-emitted spikes use the explicit remaining-distance law of v0.13, and the simple `H(A^2)` feedback is a project regression law rather than a reproduction of the paper's detailed white-matter activity functional.

The main project result is therefore not attributed to the paper:

> In the present CORE ring slice, a globally large timing-modulated attractor coexists with stable synchrony well beyond the local Chenciner wedge.

---

# 13. What is and is not certified

Certified in v0.14:

- a complete imperative packet-queue Lighthouse value simulator;
- exact alpha and conduction flow between events;
- firing/arrival root scheduling and deterministic simultaneous batches;
- frozen v0.12 period recovery;
- direct full-vs-reduced slow-passage agreement;
- dynamic skip in the full packet engine down to `epsilon=1e-5`;
- project activity-feedback regression;
- global frozen bistability at `tau3=8.0`;
- parameter-history-dependent global hysteretic memory;
- smooth-response and finite-event-spacing audit of the large benchmark state;
- an empirical upper persistence bracket.

Not yet certified:

- a direct full-packet `epsilon=1e-6` run as a default reference;
- the dynamical type of the large timing attractor;
- the bifurcation type at its upper persistence boundary;
- a production JAX fixed-capacity packet queue;
- globally differentiable tangent propagation through cycle-held feedback ties;
- the exact adaptive activity functional used in the 2026 paper.

---

# 14. Benchmark contract B183--B204

**B183 -- full state.** The adaptive event state contains neural alpha/phase variables, conduction state and active remaining-distance packets.

**B184 -- alpha flow.** Equation (AE8) is reproduced between events.

**B185 -- conduction flow.** Equations (AE6)--(AE7) are reproduced for the long edge.

**B186 -- fixed-delay recovery.** At `epsilon=0`, long packets arrive after `1/c`.

**B187 -- next-event rule.** The global next event is the earliest firing or packet-arrival root.

**B188 -- tie semantics.** Exact ties are processed as one deterministic additive arrival/firing batch.

**B189 -- same-edge FIFO.** Packet ordering on a common edge is preserved.

**B190 -- frozen NS period.** Equation (AE19) agrees with the v0.12 reference to better than `1e-6` absolute error.

**B191 -- synchronous batch.** Frozen synchronous firing spread is below `1e-12` in the reference audit.

**B192 -- center-mode preparation.** Equation (AE22) is reproduced.

**B193 -- full/reduced slow passage.** For the `1e-3` to `1e-4` default table, relative amplitude discrepancy is below `1e-3`.

**B194 -- extended 1e-5 check.** The separate slow invocation reproduces the `1e-5` row with relative amplitude discrepancy below `1e-3`.

**B195 -- full dynamic skip.** At `1e-5`, `A(tau_FIC)/A_FIC < 0.02`.

**B196 -- activity-feedback regression.** At `epsilon=1e-4`, `kappa=2e-6`, full/reduced relative amplitude discrepancy is below `1e-3`.

**B197 -- large state at 7.8.** A small `q=1` seed reaches a bounded state with final-window mean amplitude above `0.7`.

**B198 -- large state persists at 8.0.** The history-prepared large state has final-window mean amplitude above `0.6`.

**B199 -- synchrony basin at 8.0.** An independent `1e-3` seed about synchrony decays to final-window mean amplitude below `1e-5`.

**B200 -- global bistability.** B198 and B199 must hold at the same frozen `(p,tau3)`.

**B201 -- smoothness audit.** The large 8.0 benchmark retains response-threshold margin above `0.4`, maximum active packet count at most six, and positive finite event spacing.

**B202 -- upper persistence protocol.** At 8.0073 the large-state mean remains above `0.5` after 3000 cycles; at 8.0075 the mean is below `5e-4` after 6000 cycles.

**B203 -- boundary scope.** B202 is an empirical finite-time bracket and must not be labelled a fold/crisis without invariant-object continuation.

**B204 -- variational scope.** Generic single-event saltation and v0.13 arrival sensitivity are part of the mathematical contract; full AD through the cycle-held feedback tie is deferred.

---

# 15. Next CORE step

CORE v0.15 should classify the newly discovered global object rather than add another local normal-form coefficient.

Priority sequence:

1. build a fixed-`p` invariant-object solver that can continue the large timing state from `tau3=7.8` through the coexistence interval;
2. determine whether it is an invariant circle, high-period orbit or more complicated attractor;
3. compute its transverse stability;
4. replace the empirical 8.0073--8.0075 loss bracket by a genuine bifurcation condition if possible;
5. perform a slow adaptive forward/backward sweep through the certified global bistability region;
6. implement a fixed-capacity JAX packet queue and tangent/saltation map for the same benchmark.

The distinction to preserve is

\[
\boxed{\text{local Chenciner geometry}\ne\text{global attractor geometry}\ne\text{slow adaptive selection}.}
\]

v0.14 is the first CORE stage in which all three are visible in one full event-driven Lighthouse network.
