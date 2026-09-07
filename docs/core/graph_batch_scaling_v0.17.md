# CORE sparse graph tensors, batching, and scaling v0.17

## Purpose

CORE v0.17 removes the last hard-coded three-cell topology from the JAX value kernel while preserving the exact hybrid semantics certified in v0.13--v0.16. The result is a sparse directed graph representation with fixed-capacity packet state, `vmap`-compatible state batches, and equal-shape graph-parameter batches.

The acceptance rule is deliberately conservative:

> The graph engine is accepted only after its `N=3` specialization reproduces the v0.16 oracle before any large-network result is interpreted.

No globally smoothed event model is introduced.

---

## 1. Sparse directed graph

Let

\[
G=(V,E), \qquad |V|=N, \quad |E|=E.
\]

Each directed edge stores

\[
\boxed{e=(s_e,t_e,w_e,\ell_e,m_e,v_e)},
\tag{GB1}
\]

where `s_e,t_e` are source/target labels, `w_e` is synaptic weight, `ell_e` is anatomical path length, `m_e` is the discrete propagation mode, and `v_e` is the fixed speed when applicable.

The three propagation modes are

\[
m_e=0:\ \text{zero-delay jump},
\]

\[
m_e=1:\ \dot\rho=-v_e,
\]

\[
m_e=2:\ \dot\rho=-c(t).
\tag{GB2}
\]

Topology labels `(source,target,mode)` are discrete chart data. Continuous edge arrays `(weight,length,fixed_speed)` remain ordinary JAX arrays and can participate in fixed-chart differentiation.

A delayed packet no longer repeats source, target, weight, and mode. It stores only

\[
\boxed{P_k=(m_k,e_k,\rho_k)},
\tag{GB3}
\]

with active mask `m_k`, edge index `e_k`, and remaining distance `rho_k`. The static graph tensors supply the remaining packet metadata.

---

## 2. Emission and arrival semantics

When neuron `i` fires, every zero-delay edge with `s_e=i` contributes the additive alpha jump

\[
q_{t_e}^+=q_{t_e}^-+w_e\alpha^2.
\tag{GB4}
\]

Every delayed edge emits one packet with

\[
e_k=e,\qquad \rho_k=\ell_e.
\tag{GB5}
\]

Insertion uses the first free queue slot in deterministic edge-list order. Queue order is bookkeeping only: arrival selection uses physical arrival times, and simultaneous arrivals are accumulated additively.

Consequently a permutation of the edge list may change slot IDs but must not change the physical trajectory. This is tested directly in v0.17.

---

## 3. Exact specialization to the v0.16 ring

For the benchmark ring, every source has three outgoing graph edges:

\[
(s,s,1,0,m=0),
\]

\[
(s,s+1,p,1,m=1,v=1/2),
\]

\[
(s,s+2,-p,1,m=2).
\tag{GB6}
\]

At `N=3` this is exactly the v0.16 model.

The graph engine recovers

\[
\boxed{T=16.29749605483085},
\tag{GB7}
\]

with absolute error about `3.67e-9` from the independent frozen reference.

After the standard center-mode preparation,

\[
\boxed{A_0=0.0010023850245501774}.
\tag{GB8}
\]

For `epsilon=1e-5`, the graph engine reaches the static FIC after

\[
\boxed{15002\ \text{completed cycles}}
\tag{GB9}
\]

with

\[
\boxed{A_{\rm FIC}^{graph}=0.0010058631750129}.
\tag{GB10}
\]

Thus

\[
A_{\rm FIC}^{graph}/A_{\rm FIC}^{frozen}
\approx0.0152271,
\tag{GB11}
\]

and the v0.14--v0.16 dynamic-bifurcation skip is unchanged by the graph abstraction.

---

## 4. Queue-capacity semantics

The `N=3` graph emits six delayed packets in the simultaneous firing batch. Hence capacity five must hard-overflow, while capacity six is sufficient for the initial batch. The production-style reference uses twelve slots.

For the synchronous sparse ring family used in the scaling audit, every neuron fires once per cycle and both delayed paths are shorter than the period. Therefore there is at most one in-flight packet per delayed outgoing edge on the synchronous branch. The predicted maximum is

\[
\boxed{Q_{active,max}=2N.}
\tag{GB12}
\]

The scaling reference uses

\[
\boxed{Q_{max}=4N},
\tag{GB13}
\]

a factor-two capacity margin.

---

## 5. Edge-order invariance

A random permutation of all nine `N=3` edge records was applied before a 200-cycle warm/perturbed trajectory. Queue slot identities changed, but all compared physical observables agreed exactly in the test arithmetic:

\[
\boxed{\max |x_{permuted}-x_{canonical}|=0.}
\tag{GB14}
\]

The compared variables included time, neural/synaptic state, spike counts, last spike times, order-parameter amplitude, and period.

This is an important invariant: graph storage order cannot become a hidden physical parameter.

---

## 6. State batching and graph-parameter batching

For a shared graph, independent states are stacked as a PyTree and advanced with

\[
\operatorname{vmap}(\mathcal P_G).
\tag{GB15}
\]

Four center-mode seeds `(0,5e-4,1e-3,2e-3)` were evolved for thirty cycles. The maximum discrepancy between one `vmap` call and four separate calls was

\[
\boxed{6.82\times10^{-13}}.
\tag{GB16}
\]

A second batching mode stacks equal-shape graph tensors as well as states. Four different continuous `p` values were advanced simultaneously. The batched and separate physical states agreed to the test arithmetic exactly:

\[
\boxed{\max |x_{batched\ graph}-x_{single}|=0.}
\tag{GB17}
\]

This is the representation needed for parameter sweeps, ensembles, and future inverse problems. It does **not** imply differentiability with respect to integer topology labels.

---

## 7. Continuous graph-parameter derivative

At a fixed arrival chart,

\[
q_{t_e}^+=q_{t_e}^-+w_e\alpha^2.
\]

Therefore

\[
\boxed{\frac{\partial q_{t_e}^+}{\partial w_e}=\alpha^2.}
\tag{GB18}
\]

With `alpha=0.5`, JAX returns

\[
\boxed{0.25}
\tag{GB19}
\]

exactly. This is the first v0.17 check that the graph representation preserves a differentiable continuous edge parameter while keeping topology discrete.

---

## 8. Sparse large-N structural audit

The scaling family keeps three edges per neuron,

\[
E=3N,
\tag{GB20}
\]

and queue capacity `4N`.

On the synchronous branch every neuron receives one self edge, one `p` edge delayed by two, and one `-p` adaptive edge. Thus its synaptic drive is independent of network size:

\[
\Psi_{sync}(t)
=R_T(t)+pR_T(t-2)-pR_T(t-\tau_3).
\tag{GB21}
\]

The exact same period is therefore a structural prediction, not merely a performance test.

Direct JAX runs give:

| N | E | Qmax | period | max active |
|---:|---:|---:|---:|---:|
| 3 | 9 | 12 | 16.29749605483083 | 6 |
| 8 | 24 | 32 | 16.29749605483085 | 16 |
| 16 | 48 | 64 | 16.29749605483085 | 32 |
| 32 | 96 | 128 | 16.29749605483085 | 64 |
| 64 | 192 | 256 | 16.29749605483085 | 128 |
| 128 | 384 | 512 | 16.29749605483085 | 256 |
| 256 | 768 | 1024 | 16.29749605483085 | 512 |

No overflow occurred.

Single-machine CPU timings observed during development were roughly linear after compilation, but timing numbers are intentionally **not** part of the scientific benchmark contract. Accelerator scaling has not yet been certified.

---

## 9. Differentiability scope

The v0.16 rule remains unchanged.

Continuous arrays such as

\[
w_e,\ell_e,v_e,c
\]

may be differentiated inside one fixed event chart. Integer arrays

\[
s_e,t_e,m_e,e_k
\]

are structural labels. Event-order changes and topology changes remain hybrid/discrete boundaries.

Batching many parameter sets does not turn those boundaries into smooth objects.

---

## 10. Benchmark contract B247--B268

- **B247** graph state uses sparse edge tensors `(source,target,weight,length,mode,fixed_speed)`.
- **B248** zero-delay graph edges produce direct additive alpha-state jumps.
- **B249** delayed queue slots store only active mask, `edge_id`, and remaining distance.
- **B250** delayed emission uses deterministic first-free-slot allocation.
- **B251** insufficient queue capacity produces a hard overflow flag; `Q=5` overflows the initial N=3 batch and `Q=6` does not.
- **B252** N=3 graph specialization recovers `T=16.29749605483085`.
- **B253** N=3 specialization observes maximum active queue occupancy six.
- **B254** prepared N=3 center amplitude is `0.0010023850245501774`.
- **B255** the `epsilon=1e-5` graph run reaches the FIC after 15002 cycles.
- **B256** the graph FIC-crossing amplitude is `0.0010058631750129` and remains below 2% of the static FIC amplitude.
- **B257** random edge-list permutation leaves all audited physical observables invariant to `1e-12`.
- **B258** shared-graph `vmap` agrees with separate state runs to `1e-10`.
- **B259** equal-shape graph-parameter batching agrees with separate graph runs to `1e-10`.
- **B260** fixed-arrival edge-weight derivative is `dq_target/dw=alpha^2=0.25`.
- **B261** N=8 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B262** N=16 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B263** N=32 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B264** N=64 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B265** N=128 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B266** N=256 sparse ring recovers the N=3 synchronous period to `5e-10`.
- **B267** with `Qmax=4N`, synchronous scaling runs through N=256 have `max_active=2N` and no overflow.
- **B268** CPU timing is observational only; topology/event-order labels remain nondifferentiable chart data.

---

## 11. Next

CORE v0.18 should use the v0.17 graph tensors for a controlled inverse problem: infer continuous edge weights and/or conduction parameters from synthetic spike-time observations while remaining inside known event charts. The first acceptance test should recover the N=3 benchmark parameters from exact synthetic data and detect, rather than smooth through, any event-order boundary crossed by the optimizer.
