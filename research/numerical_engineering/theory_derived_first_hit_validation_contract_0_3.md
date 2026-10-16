# NUM-ENG Theory-Derived First-Hit Certification — FINITE PRE-EXECUTION CONTRACT 0.3

Status: FIXED / NOT YET EXECUTED. Date: 2026-10-16.
Authority: RB-004, RB-019, RB-021, RB-022 (including mandatory structural-zero semantic repair); MASTER Gate 0.3 prompt. Branch: `engineering/numerics-v0.1`.

**This contract is committed before any Gate-0.3 validation outputs. No subsequent fixture/tolerance changes or result-specific reruns. No protected RNG streams.** Outcomes are ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE, never scientific effect claims. The physical authority is unchanged `NUMENG_PULSE_AWARE_REFERENCE_V1`, with RB-021 high-level batch-tape guard overlay.

## Common definitions and finite acceptance rules

Let `S(x;r,h)=0` for `x<=h`, otherwise `exp(-r/(x-h)^2)`; `psi(s)=exp(-alpha*s)*(p0+s*q0)`; `q(s)=exp(-alpha*s)*q0`. Except where explicitly noted, `r=1,h=-1,alpha=1`; float64/CPU; positive weight/delay and structural topology are independent. A structural weight zero retains its edge and labelled arrivals. Histories, arrays and topology are fixed below.

Full interval gain is `G(L)=integral_0^L S(psi(s)) ds`. The finite interval encloser divides a segment at `n in {64,128,256,512,1024,2048}` uniform subintervals and obtains exact scalar min/max of `psi` from endpoints and `s_c=(q0-alpha*p0)/(alpha*q0)` whenever `q0!=0` and `s_c` lies strictly inside. On each subinterval sum `width*S(minpsi)` and `width*S(maxpsi)` as lower/upper gain enclosures, respectively. Use this fixed schedule only; if no strict margin is resolved return `UNCERTIFIED`, not a positive certificate. These are mathematical extrema with float64 roundoff, **not outward-rounded interval arithmetic**, so use only as finite engineering consistency checks.

For a no-hit theorem consistency classification require `upper_gain < gap - 1e-12`; for a bracketed unique regular hit require `upper_gain(left) < gap - 1e-12`, `lower_gain(right) > gap + 1e-12`, and minimum `S` on [left,right] > 1e-10, with supplied physical first-hit inside bracket and maximum 2e-8 time deviation from an independently segmented phase-root reference. Zero/equality margin must return `UNCERTIFIED` (not INVALID). Exact discrete signed-event comparisons require identical signature/token, chart validity and time max discrepancy <=2e-8 unless a distinct outcome is specifically prescribed. For all finite gradient tests use central physically rerecorded epsilon=1e-4, max absolute AD/FD error <=3e-5 and replay/physical time residual <=1e-7. No derivative is attempted after a changed labelled itinerary or an invalid chart. Chart collision threshold is the frozen engineering 1e-8, not a theorem.

Labels: `THEORY-CONSISTENT ENGINEERING VALIDATION`, `UNCERTIFIED`, `ENGINEERING DEFECT`, `THEORY/IMPLEMENTATION CONTRADICTION`, `DEFERRED`. Separate these from the physical record's `chart_valid` and `physical_certification` fields. A physical chart may be valid when a separate strict bound is uncertified.

## TV-01/TV-02: algebraic propagation and extrema

TV-01 triples `(alpha,psi0,q0,L)`: `(1,.4,2,.3)`, `(30,-.2,900,.15)`, `(1000,0,4e6,.005)`, `(1,-.7,0,.5)`; sample at `L*{0,.1,.25,.5,.75,1}`. Compare `q(s)` and `psi(s)` with the exact analytic propagation and `reference.propagate_alpha` (where `a0=psi0`, `q0` as above). Absolute tolerance `3e-10` for narrow large amplitudes, relative `2e-13`; for small amplitudes atol `1e-12`.

TV-02 `(alpha,psi0,q0,[a,b])`: `(1,0,3,[0,2])`, `(1000,0,4e6,[0,.005])`, `(1,-2,0,[0,.5])`, `(1,1,-3,[0,1])`. Finite stationary candidates endpoints and the interior `s_c` only. Compare analytic extrema to dense uniform `s=linspace(a,b,20001)`: numerical sampled extrema must lie inside analytic envelope to 1e-10; extrema discrepancy <=3e-5 absolute for ordinary states, <=50 for the alpha=1000/high-amplitude state (relative <=1e-4). Exact analytic candidates checked by finite-difference derivative sign when an interior critical point exists.

## TV-03/TV-04: gain certificates

TV-03 constant input from `psi0=q0=0`, `alpha=1,r=1,h=-1,L=1`: remaining gap `d=.5` -> `CERTIFIED NO-HIT`; gap `d=exp(-1)` exactly -> `UNCERTIFIED` due equality. TH-FH-02 uses `alpha=.1,r=1,h=-1,psi0=-1.01,q0=0,L=.05,gap=.02` -> `CERTIFIED NO-HIT`, since all `psi<=h`.

TV-04 constant-input unique bracket with `psi0=q0=0`, `r=1,h=-1,L=2`, gap `d=1.5*exp(-1)`, bracket `[1.49,1.51]` -> `CERTIFIED REGULAR HIT` at 1.5. Boundary negative control identical but bracket `[1.5,1.51]` -> `UNCERTIFIED` (no strict lower-side margin). TH-FH-01 uses narrow pulse `alpha=1000, psi0=0,q0=4e6,r=1,h=.1`, arrival-local interval `[0,.04]`, gap `.005`, bracket `[.004,.007]` -> `CERTIFIED REGULAR HIT` (global event at `.5 + local_hit`). Compare to frozen RB-018/RB-019 physical case: `SparseParameters(n=1,target=[0],source=[0],weight=[4],delay=[1.5],alpha=1000,r=1,h=.1);history=[[-1]],initial_theta=[2pi-.005],horizon=20`. Coarse endpoint-only sampler reading S(psi(0)) and S(psi(.04)) is a negative control: never report certified no-hit from it.

## TV-05: response derivatives

`r in {.25,1,4}`, `h=-1`, `x-h = sqrt(r/t)` for `t=linspace(.02,12,2401)`, plus `t1=1.5` and `t2=(9+sqrt(33))/4`. Check `abs(S')<=theorem c1/sqrt(r)+3e-13`, equality at `t1` error <=2e-13, `abs(S'')<=c2/r+2e-12`, equality at `t2` error <=1e-11; `c1=2*(1.5)^1.5*exp(-1.5)`, `c2=abs((4*t2^3-6*t2^2)*exp(-t2))`. On `x<=h` and exactly `x=h`, all displayed derivatives vanish. No general higher-order numerical certification.

## TV-06 / TH-FH-05: exact alpha mass and omitted tails

`(alpha,A)` in `{(1,0),(1,.5),(1,5),(4,.5),(1000,0),(1000,.005)}`; quadrature of `u*exp(-u)` from `alpha*A` to infinity (`epsabs=1e-12, epsrel=1e-11`) vs `exp(-alpha*A)*(1+alpha*A)` with atol 2e-12. Omitted finite pulses at ages `[5,7,9]`, signed weights `[2,-1,.5]`, `alpha=1,L=.7,r=1,h=-1`. Compute full minus omitted-input phase integrated by SciPy `quad`, compare abs phase error to `L_S*sum |w|*(M(age)-M(age+L))`, tolerance 1e-11; check decisive strict margin with `d=baseline_gain + bound + .05` -> NO HIT; `d=baseline_gain + bound` -> UNCERTIFIED. As negative local-finiteness-only example use ages `n>=1` and weights `c_n=exp(n)` (a conceptual countably infinite sequence): each finite time interval contains finitely many events but `sum c_n M(n)=sum(n+1)` diverges. Return `UNCERTIFIED` for infinite-tail theorem use; DO NOT instantiate this as an infinite simulator history or an absolute-tail certificate.

## TV-07/TV-08: positive ordinary charts and event sensitivity

Use the pre-existing RB-019 ordinary 2-neuron fixture from `tests/test_rri_repair_v01.py:ordinary_fixture`: dense W=[[2.2,0],[0,2.5]], adjacency=[[1,0],[1,1]], delays=[[.31,0],[.83,.43]], history=((-3,-.5),(-2.2,)), initial theta=(.3,1.1), horizon=40, alpha=1,r=1,h=-1. Sparse order is lexicographically by `(target,source)`; structural-zero coordinate `(1,0)`.

TV-07 perturbations independently ±`1e-5` and ±`5e-5` of (1) the nonzero edge weight `(0,0)`, (2) delay `(1,1)`, (3) phase neuron 0. Each candidate is rerecorded physically and must have the same labelled tape signature, positive min spike transversality >1e-10, positive event/boundary margins >1e-8, and certified tape. Any chart exit is counted separately (and no gradient used); it is not reclassified as a derivative error.

TV-08 central FD epsilon=1e-4 for five coordinates: nonzero weight `(0,0)`, exactly-zero structural weight `(1,0)`, active delay `(1,1)`, structural-zero delay `(1,0)`, initial theta neuron 0. Require original and both signed candidates regular and same token; physical re-record + `derivative_record_sparse` under the RB-021 batch guard. Check spike-time AD-vs-FD <=3e-5, and arrival-time derivative for historical `(1,0)` arrival at `.33` equals 1 with respect to its delay and its physical spike derivative is zero at exact zero weight within absolute tolerance 3e-5 (other indirect feedback is absent for this edge). Verify the spike formula `dT=-dtheta_fixed(T)/S(psi(T^-))` indirectly via AD/FD when velocity>1e-10; use no off-chart differentiation.

## TV-09 / TH-FH-06: repaired structural zero

Reuse the ordinary fixture; vary structural weight `w(1,0)` at exactly `[-1e-4,0,+1e-4]`, unchanged edges; compare independent omitted-edge graph with adjacency[1,0]=False and weight=0. At exact zero, physical spike-time vectors and final phases match omitted-edge graph within 2e-8; labelled arrival sequences/tokens must differ; original tape has zero edge labelled arrivals. Centered physical FD across ±1e-4 matches JAX weight sensitivity <=3e-5. Vary zero-edge delay from `.83` to `.83±1e-4`: historical source-zero arrival at `.33` shifts exactly by ±1e-4 and physical spike times remain invariant at zero weight (tolerance 2e-8). Removing zero-edge arrivals from a purported original tape must be rejected by the RB-021 high-level physical guard. Negative event collision: use TH-FH-04 exact tie below; requires invalid ordinary chart.

## TV-10: full TH-FH family, precise cases/expected outcomes

TH-FH-01 = TV-04 narrow pulse: `CERTIFIED REGULAR HIT`.
TH-FH-02 = TV-03 negative input: `CERTIFIED NO-HIT`.
TH-FH-03: `alpha=.1,r=.1,h=-1,t*=1,q0=0`, `delta=.2` gives `psi0=(h+delta)*exp(alpha*t*)`; define gap before validation by independent `quad_0^t* S(exp(-alpha*s)*psi0)ds` (constructive exact first-hit definition, no measured output fitting). Expect finite regular first-hit at `t*` with positive velocity `exp(-r/delta²)` and increasing `1/velocity` sensitivity; admissibility tolerance time 2e-8, velocity abs tolerance 1e-11. Control `delta=.01` gives a strictly mathematical but numerically under-resolved event; require `UNCERTIFIED` (not PHYSICALLY INVALID) when velocity <=1e-10.
TH-FH-04: isolated clock neuron r=1,h=-1,theta0=`2pi-1.5*exp(-1)`, structural zero-weight self-edge with historical source event `-1`, delay=`2.5+eps`, eps in `[-1e-3,0,+1e-3]`, horizon=2. Expected two opposite valid labelled event orderings at nonzero eps; exactly zero = `PHYSICALLY VALID BUT ORDINARY-CHART INVALID`.
TH-FH-05 = TV-06 finite history `CERTIFIED NO-HIT`, margin equality and missing summability `UNCERTIFIED`.
TH-FH-06 = TV-09: zero-edge physically equivalent but different tape, ±1e-4 fixed-topology cases valid -> `THEORY-CONSISTENT ENGINEERING VALIDATION`; omitted zero arrival from tape -> invalid guard.
TH-FH-07: isolated clock neuron n=1,E=0, r=1,h=-1,theta0=`2pi-1.5*exp(-1)` and horizon values `[1.5001,1.5,1.4999]`: first strict interior = `CERTIFIED REGULAR HIT`; equality = `PHYSICALLY VALID BUT ORDINARY-CHART INVALID` (boundary); last = `CERTIFIED NO-HIT` within its horizon.
TH-FH-08: N=2, self structural edges `(0,0)` and `(1,1)`, weights `(0.3,0.4)`, delays `(1.7,1.7)`, each source history `(-1,)`, theta0=(0,0), alpha=1,r=1,h=-1,horizon=1. Two labelled arrivals simultaneously at t=.7. Expect physical alpha jump maps to commute in either order but total-order chart `PHYSICALLY VALID BUT ORDINARY-CHART INVALID` (collision).

## TV-11: tape negative controls

Use same ordinary fixture and RB-021 high-level guards; run (a) event timestamps shifted +.02 retaining token, (b) delete a labelled structural-zero arrival, (c) candidate weight of `(1,0)` with sufficient perturbation to change itinerary selected by the *predetermined TH-FH-04 ±.001 cases*, and (d) uncertified physical tape label. Every stale/altered input must reject. Successful regular base derivative remains positive control. Direct low-level JAX replay is not asserted physically certified.

## Classification and halt

Physical/theory contradiction under every explicit theorem hypothesis -> `THEORY/IMPLEMENTATION CONTRADICTION — BLOCKED`. A failing accepted implementation guard -> `ENGINEERING DEFECT` and `BLOCKED` for Freeze 0.3; zero/equality margin -> `UNCERTIFIED`. A deliberately invalid ordinary-chart collision is not physical singularity. Do not alter fixtures/tolerances after test output. Any new non-preregistered diagnostic may be logged separately, never used to rescue a failed test. All raw results and exact command/exit info required. No `2701xxx`/`2711xxx` streams, TR-27C, APP-3, AI tasks, main executable merge or manuscript claims.
