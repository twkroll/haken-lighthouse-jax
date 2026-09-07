# CORE Consolidated C1 Theory Freeze 0.1

Date: 2026-09-07
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-012

## Authority and provenance

MASTER reviews the governed `CORE Legacy Verification Sweep 0.1` and accepts only the sweep's strongest explicitly proved C1 candidates as canonical premises.

Frozen verification source:

- `research/core/legacy_verification_sweep_0_1.md`
- blob SHA `853b22a0c630b4ed2d94835b1d4aa95243f38f2f`
- sweep PASS commit `336db6b07610cda320bf481becca9320831249bc`
- audit freeze RB-011

Legacy source material remains read-only at recovery SHA `287eae8a86560b78ed94f30a2786243714c33ac0`.

This freeze does not promote any legacy C3 effect, optimized design, numerical performance result or implementation benchmark.

## C1-1 — In-flight propagation proposition

Let a packet launched at time `s` on an edge of path length `L>0` have remaining distance `rho` governed by

`rho_dot(t) = -c(t)`, `rho(s)=L`.

If `c` is continuous and `c(t)>=c_min>0`, then `rho` is strictly decreasing and reaches zero exactly once in finite time. Packets on the same edge using the same speed law preserve launch order (FIFO).

For the unique arrival time `a` satisfying

`integral_s^a c(u) du = L`,

first-order perturbation gives

`delta a = [c(s) delta s - integral_s^a delta c(u) du] / c(a)`.

In particular, if only launch time varies,

`da/ds = c(s)/c(a)`.

Label: PROPOSITION / PROVED under `c>=c_min>0`.

## C1-2 — Pre-event projected alpha observation and rank-one bound

Before any event under the frozen alpha state-space flow,

`q(t)=exp(-alpha t) q_0`,

and for a projected perturbation direction the observable sensitivity has the form

`z_psi(t)=exp(-alpha t) (xi_psi + t xi_q)`.

Appending one scalar observation row `g` to an `n`-column full-rank Jacobian `J` gives

`J_+^T J_+ = J^T J + g^T g`.

By rank-one positive-update interlacing,

`sigma_min([J;g]) <= sigma_{n-1}(J)`.

This is a structural bound only. No optimized measurement time, saturation claim or legacy information-gain value is frozen.

Label: LEMMA / PROVED.

## C1-3 — Duplicate-trial information scaling

For an exactly duplicated trial Jacobian

`J_dup = [J; J]`,

one has

`J_dup^T J_dup = 2 J^T J`.

Hence every singular value of the stacked duplicated Jacobian is multiplied by `sqrt(2)` while its right-singular directions are unchanged.

Replication therefore scales information/noise averaging but does not rotate a sensitivity nullspace.

Label: LEMMA / PROVED.

## C1-4 — Nuisance-profile proposition

For a local trial Jacobian partitioned as

`J=[J_s  N]`,

where `J_s` contains scientific/shared directions and `N` nuisance directions, let `P_N` be the orthogonal projector onto `col(N)`; if `N` is rank deficient, use the Moore-Penrose definition of that projector.

The nuisance-profiled scientific sensitivity is

`R=(I-P_N) J_s`.

Under the local linear-Gaussian least-squares/Fisher approximation, the profiled local Fisher information is proportional to

`R^T R`.

For independent trials, residualize each trial against its nuisance span and stack the resulting `R_r` before forming the shared information matrix.

Label: PROPOSITION / PROVED.

## C1-5 — Structural fixed-time pulse self-calibration ambiguity

Assume all of the following:

1. the pulse occurs at a fixed time `t_p` before the first physical event;
2. the full real `q=1` initial synaptic subspace is free in both `(psi_0,q_0)`;
3. the two independent relative `q=1` phase coordinates are free;
4. the pulse reset is restricted to the same real `q=1` synaptic subspace;
5. the event chart is regular and labelled spike times are the downstream observations.

The pre-pulse alpha flow in that subspace is

`(psi_0,q_0) -> exp(-alpha t_p) (psi_0+t_p q_0, q_0)`,

which is invertible. Infinitesimal calibration changes in `(A,beta,gamma)` modify only the pulse-reset vector in the same synaptic subspace. A compensating initial-state variation can cancel that reset variation exactly, and the free relative phase coordinates can cancel the corresponding relative-phase variation. The post-pulse relative state is therefore unchanged to first order, so subsequent fixed-chart labelled spike times are unchanged to first order.

Thus the `(A,beta,gamma)` calibration sensitivity columns lie in the trial-state nuisance span under these assumptions.

This proposition does not cover pulse-time nuisance `delta t_p` and does not freeze any numerical calibration uncertainty or Fisher value.

Label: PROPOSITION / PROVED UNDER STATED ASSUMPTIONS.

## Explicit exclusions

RB-012 does not freeze:

- any optimized measurement time, pulse, second probe or spike subset;
- the legacy 250x, 87x, 788x or 557x information-gain values;
- any v0.26 profiled singular value, uncertainty, noise or multistart result;
- pulse-time self-calibration claims;
- any v0.6–v0.15 bifurcation/global-object effect;
- any implementation-performance/scaling claim;
- any v0.27 result.

## Change control

Any extension or weakening of the assumptions above requires a new MASTER-authorized gate and a new versioned freeze.

## STOP

`CORE Consolidated C1 Theory Freeze 0.1` is established.

STOP — FROZEN
