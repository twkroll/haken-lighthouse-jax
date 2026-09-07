# CORE Legacy Verification Sweep 0.1

Date: 2026-09-07
Status: PASS — FULL V0.4–V0.26 LEGACY CORPUS CLASSIFIED; NO LEGACY C3 EFFECT PROMOTED

## 1. Git / provenance identity

This sweep was executed under the MASTER-authorized `VERIFY-LEGACY` command and the verification-first command protocol v0.2.

Canonical identity at sweep start and immediately before the sweep result write:

- repository: `twkroll/haken-lighthouse-jax`
- canonical branch: `main`
- `main` HEAD: `c2dce18e3bc7ce0eab0a0fe9ab84beae1c73f0c4`
- command protocol: `research/master/command_protocol_v0_2.md`
- authorizing prompt: `research/master/prompts/core_legacy_verification_sweep_0_1.md`
- frozen recovery input: `287eae8a86560b78ed94f30a2786243714c33ac0`
- legacy recovery branch is read-only verification input and was not merged, rebased, rewritten or continued.

The complete recursive tree at the recovery SHA was inspected with `truncated=false` before version-by-version classification.

## 2. Freeze-chain reuse

The following canonical layers are premises and were not redundantly re-proved unless a concrete legacy contradiction required an audit:

- RB-004 — `CORE Mathematical Freeze 0.1`: canonical deterministic baseline, alpha kernel, event/delay semantics, assumptions and elementary D1–D18 identities.
- RB-005 — `CORE Benchmark Contract Freeze 0.1`.
- RB-006 — governed v0.2 result: `BC01–BC10 ALL PASS UNDER RB-005`.
- RB-007 — `CORE v0.3 Continuation Theory Freeze 0.1`, including fixed-domain branch mathematics, event/chart taxonomy and canonical two-cell coefficient
  
  `B = -T^2 w_c ∫ S'(Psi_0) R_T'(T sigma - tau_c) d sigma`.
- RB-008 — v0.3 continuation validation contract.
- RB-009 — governed v0.3 result: `V3C01–V3C09 ALL PASS UNDER RB-008`.
- RB-010 — `CORE v0.4 Floquet Theory Freeze 0.1`, including the spike-time recurrence, `M(mu)=(mu-1)D_nu-H(mu)`, the neutral multiplier, alpha lag-series convergence qualification and full-operator symmetry conditions.

No legacy `COMPLETE`, `VERIFIED`, `CERTIFIED` or benchmark status was allowed to override these canonical freezes.

## 3. Full legacy artifact inventory v0.4–v0.26

All hashes below refer to the frozen recovery SHA.

| Version | Primary document(s), blob SHA | Reference implementation | Stored benchmark/status closure |
|---|---|---|---|
| v0.4 | `spike_time_floquet_v0.4.md` `d4565043…`; `symmetry_reductions_v0.4.md` `5021fc9b…`; `floquet_contract_v0.4.md` `8a11678e…` | none | no v0.4 benchmark JSON |
| v0.5 | `order_parameter_normal_forms_v0.5.md` `551bfb16…`; `normal_form_contract_v0.5.md` `ea8b6b3e…` | none | no v0.5 benchmark JSON |
| v0.6 | `numerical_atlas_v0.6.md` `bbb1aa38…` | `core_v06_two_cell_pitchfork.py` `8e771dec…` | JSON `3395337d…` |
| v0.7 | `event_normal_forms_v0.7.md` `239b5db9…` | `core_v07_event_normal_forms.py` `a7a897e5…` | JSON `ef32a892…` |
| v0.8 | `codimension_two_v0.8.md` `84496aa0…` | `core_v08_codimension_two.py` `9264897d…` | JSON `68fc13f0…` |
| v0.9 | `chenciner_v0.9.md` `814425e7…` | `core_v09_chenciner.py` `5a35a0c7…` | JSON `0cd320bc…` |
| v0.10 | `chenciner_unfolding_v0.10.md` `46f6996d…` | `core_v010_chenciner_unfolding.py` `784ae6ea…` | JSON `069f5e3d…` |
| v0.11 | `invariant_circles_v0.11.md` `09ea3810…` | `core_v011_invariant_circles.py` `7d40957d…` | JSON `5e316183…` |
| v0.12 | `adaptive_delays_v0.12.md` `eafcf433…` | `core_v012_adaptive_delays.py` `f41dfe16…` | JSON `f9d3e294…` |
| v0.13 | `in_flight_delays_v0.13.md` `5626b1d4…` | `core_v013_inflight_delays.py` `8bc8467f…` | JSON `7004bfe0…`; status `fb8626aa…` |
| v0.14 | `adaptive_event_engine_v0.14.md` `af06d87c…` | `core_v014_adaptive_event_engine.py` `4be544d7…` | JSON `88079199…`; status `9aacaa31…` |
| v0.15 | `global_invariant_circle_fold_v0.15.md` `4507d2b5…` | `core_v015_global_circle_fold.py` `4a899e7a…` | JSON `96ba0c39…`; status `13456f85…` |
| v0.16 | `jax_packet_queue_v0.16.md` `8c818ae5…` | packet/value/tangent scripts `64e5448d…`, `3d3fcac5…`, `c5ac5637…` | JSON `5517c54d…`; status `183dc079…` |
| v0.17 | `graph_batch_scaling_v0.17.md` `498752cc…` | graph/scaling scripts `12e01bad…`, `f1ba0f54…` | JSON `5fefea57…`; status `d33f9929…` |
| v0.18 | `inverse_problem_v0.18.md` `c3ef76ec…` | `core_v018_inverse_problem.py` `5dd8ad75…` | JSON `3a27ba54…`; status `8889af5a…` |
| v0.19 | `hybrid_multichart_optimizer_v0.19.md` `d3ff48e0…` | `core_v019_multichart_optimizer.py` `12ee4b40…` | JSON `1e6791b7…`; status `a2ae4ee5…` |
| v0.20 | `latent_state_inference_v0.20.md` `e6a74cef…` | `core_v020_latent_state_inference.py` `80324614…` | JSON `2573a2da…`; status `6c43051c…` |
| v0.21 | `observation_design_v0.21.md` `dcd815da…` | `core_v021_observation_design.py` `b69eda92…` | JSON `49cdfcb4…`; status `b27e66b6…` |
| v0.22 | `latent_synaptic_state_v0.22.md` `77181b6c…` | `core_v022_latent_synaptic_state.py` `1f455e6d…` | JSON `aaed682d…`; status `8afefa89…` |
| v0.23 | `transverse_observation_v0.23.md` `1fdbc03b…` | `core_v023_transverse_observation.py` `854b48a7…` | JSON `63f991de…`; status `bafbbbb1…` |
| v0.24 | `active_pulse_design_v0.24.md` `56d03e98…` | `core_v024_active_pulse_design.py` `dd036c3c…` | JSON `94894856…`; status `c1c9a153…`; superseded prototypes exist in history |
| v0.25 | `full_q1_two_probe_v0.25.md` `e253afe2…` | `core_v025_full_q1_two_probe.py` `38989174…` | JSON `a4e31596…`; status `8f71739d…` |
| v0.26 | `trial_nuisance_calibration_v0.26.md` `1566cc8d…` | `core_v026_trial_nuisance_calibration.py` `14c14602…` | **no benchmark JSON and no v0.26 status summary** |

The absence of v0.26 JSON/status closure is a real artifact gap, not inferred completion.

## 4. Consolidated verification matrix

| Version / material | Type | Relation to freezes / verification route | Sweep result class | Recovery class | Freeze eligibility / rerun rule |
|---|---|---|---|---|---|
| v0.4 spike-time Floquet/symmetry theory | mathematical theory | already independently canonicalized as RB-010 | `ALREADY CANONICAL` | C1 | already frozen; no new action |
| v0.4 B23–B40 | candidate validation inventory | audited against RB-010; no execution | mixed: useful C2 inventory / repair / defer | C2/C3/C5 | requires new pre-execution contract before numerical use |
| v0.5 smooth-map fold/pitchfork/flip/NS algebra | conditional math | independently checked as abstract map algebra | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 conditional | possible narrow theory freeze after explicit regularity/scope gate |
| v0.5 claim that v0.4 event-time spectrum is the complete nontrivial hybrid return-map spectrum | mathematical equivalence claim | stronger than RB-010 | `DEFER / OPEN QUESTION` | C5 | needs separate equivalence proof/validation |
| v0.6 two-cell pitchfork script/JSON arithmetic | implementation/numerics | script convention inspected; stored values recomputed consistently | `STATICALLY CONSISTENT` | C2 mechanics / C3 effect | effect requires preregistered rerun |
| v0.6 claim that RB-007 negative B sign was an erratum | interpretation | v0.6 uses globally opposite existence residual convention | `SUPERSEDED / REJECT` | C4/C5 | canonical RB-007 sign retained |
| v0.6 actual Lighthouse pitchfork / scaling / multiplier relation | numerical effect | exploratory downstream result | `PREREGISTERED RERUN REQUIRED` | C3 | new frozen contract required |
| v0.7 event-map implementation and history-convergence machinery | algorithm | finite perturbation history, exact base tail | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C2 | faithful replay contract if needed |
| v0.7 actual flip/NS locations and normal-form coefficients | numerical effects | exploratory numerical branch | `PREREGISTERED RERUN REQUIRED` | C3 | preregister before use |
| v0.8 corrected contact coordinates | numerical geometry | corrected legacy artifact internally consistent | `STATICALLY CONSISTENT` | C3 | rerun only if scientifically prioritized |
| v0.8 label “hybrid codimension-two” from smooth baseline threshold contact | interpretation | conflicts with RB-007 smooth-threshold repair | `SUPERSEDED / REJECT` | C4/C5 | do not promote |
| v0.9 Chenciner local algebra | conditional math | standard generalized-NS structure consistent | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 conditional | separate normal-form theory gate possible |
| v0.9 Chenciner point / L1 zero / numerical transversalities | numerical effect | effect-bearing legacy search | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.9 independently generated fifth-order b2/L2 | higher-order numerical derivation | reference script consumes stored fifth-order values; generator absent | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C5/C3 | recover generator or rederive under new contract |
| v0.10 radial Chenciner/FIC polynomial algebra | conditional math | independently checked conditional on coefficients | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 conditional | freeze candidate only as abstract algebra |
| v0.10 numerical wedge/radii/FIC predictions | numerical effects | inherit exploratory v0.9 coefficients | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.11 Fourier/collocation invariant-circle machinery | algorithm | finite L, finite Fourier/collocation representation | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C2 | replay contract needed |
| v0.11 claim wording “exact invariant circles” | epistemic wording | numerically high-accuracy but finite representation | `SOURCE/PROVENANCE REPAIR REQUIRED` | C5 | qualify before reuse |
| v0.11 actual small circle/FIC results | numerical effects | exploratory | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.12 slow-fast radial/conduction envelope equations | project model/algebra | internally coherent conditional reduced model | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 conditional | may be frozen only as project reduced-model mathematics |
| v0.12 epsilon thresholds, dynamic skip and effect percentages | effects | exploratory | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.13 in-flight packet remaining-distance semantics, existence/FIFO/sensitivity | mathematical project theory | independently derived | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | **high-value narrow freeze candidate** |
| v0.13 numerical robustness comparisons | effect/benchmark | depend on exploratory v0.12 slice | `PREREGISTERED RERUN REQUIRED` | C3 | preregister if used |
| v0.14 queue event-engine semantics | algorithm | static audit consistent | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C2 | replay contract before canonical implementation claim |
| v0.14 large timing attractor / coexistence / “global hysteretic memory” | numerical effects | discovered in exploratory lineage | `PREREGISTERED RERUN REQUIRED` | C3 | high-value hypothesis only |
| v0.15 global quasiperiodic circle / unstable boundary circle / fold near tau_F≈8.00731 | numerical global effects | finite numerical classification, exploratory | `PREREGISTERED RERUN REQUIRED` | C3 | high-value preregistered global-dynamics test if prioritized |
| v0.15 rigorous invariant-circle/fold existence | theorem-level claim | not supplied by finite trajectory/Fourier/ghost evidence | `DEFER / OPEN QUESTION` | C5 | separate proof layer if needed |
| v0.16 fixed-capacity queue/chart/tangent design | implementation/method | formulas and chart policy consistent | `MATHEMATICALLY VERIFIED IN SWEEP` for local derivative formulas; replay pending for implementation | C1/C2 | theory pieces may freeze; code claims need replay |
| v0.16 JAX equivalence / derivative errors / fold replay | implementation results | exact script closure not executed in this sweep | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C2; inherited effect C3 | replay contract; do not promote fold effect |
| v0.17 sparse graph/batch/edge-order design | method | structural representation consistent | `MATHEMATICALLY VERIFIED IN SWEEP` for invariance/weight-jump algebra; replay pending for software | C1/C2 | code validation later |
| v0.17 N=3 equality, batches, N=256 scaling | implementation | stored benchmark only | `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` | C2 | exact replay if production path selected |
| v0.18 chart-aware inverse-problem mechanics | method/implementation | fixed-chart derivative principle consistent with canonical event semantics | `STATICALLY CONSISTENT`; replay pending | C2 | implementation replay possible |
| v0.18 recovery/conditioning/noise performance | scientific benchmark effect | inherited exploratory truth/chart | `PREREGISTERED RERUN REQUIRED` if promoted | C3 | preregister |
| v0.19 multichart rerecording / boundary predictor concept | method | differentiates only within charts, rerecords across switch | `MATHEMATICALLY VERIFIED IN SWEEP` for local predictor principle; replay pending for optimizer | C1/C2 | code replay if needed |
| v0.19 optimizer paths/iterations/crossing success | performance | numerical benchmark | `PREREGISTERED RERUN REQUIRED` for performance claim | C3 | preregister if scientific evidence |
| v0.20 gauge-fixed latent relative-phase model and margin-vector concept | method | structurally coherent | `STATICALLY CONSISTENT`; replay pending | C1/C2 | theory/method candidate; performance requires contract |
| v0.20 rank/singular values/Fisher/optimizer crossings | numerical effect | exploratory | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.21 E/D/A design definitions | mathematics | standard local Fisher design algebra | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | reusable definition |
| v0.21 optimized observation subsets and gains | optimized effect | explicit exhaustive post-effect selection | `PREREGISTERED RERUN REQUIRED` | C3 | must pre-fix candidate pool/objective before confirmatory rerun |
| v0.22 local conditioning vs nonlinear uniqueness distinction | interpretation/method | logically valid distinction | `MATHEMATICALLY VERIFIED IN SWEEP` / interpretation | C1 interpretation | reusable principle |
| v0.22 near-null direction, aliases, schedule results | numerical effects | selected in response to observed inference geometry | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.23 pre-event alpha projected observation formula and rank-one bound | mathematical observation theory | independently derived and checked | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | **high-value narrow freeze candidate** |
| v0.23 optimized sensor time, bound saturation and ≈250.37× gain | optimized effect | designed after v0.22 weak direction | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.24 pulse family/chart-safety method | experiment-method definition | final form static-consistent but arose after superseded designs | C2 method / `STATICALLY CONSISTENT` | C2/C4 history | new confirmatory contract must define it before output |
| v0.24 reference pulse, ≈87.07× gain, subsets/noise | optimized active-design effects | clearly post-hoc lineage | `PREREGISTERED RERUN REQUIRED` | C3 | preregister; prototypes remain C4 |
| v0.25 duplicate-trial sqrt(2) information scaling | linear algebra | independently verified | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | reusable |
| v0.25 P1+P2 ≈788× / ≈557× gains, P2 and E-opt8 | optimized active-design effects | P2 designed after P1 geometry | `PREREGISTERED RERUN REQUIRED` | C3 | preregister |
| v0.26 nuisance-profile algebra `R_r=(I-P_Nr)J_sr` | local inference mathematics | independently derived from profiled least squares/Fisher information | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | **high-value narrow freeze candidate** |
| v0.26 structural A/beta/gamma self-calibration ambiguity | proposition under explicit pre-event/free-state assumptions | independently proved by invertibility + nuisance-state absorption | `MATHEMATICALLY VERIFIED IN SWEEP` | C1 | **high-value narrow freeze candidate** |
| v0.26 pulse-time nuisance | claim/number | not structurally absorbed by same argument; legacy only finds a weak residual direction | `STATICALLY CONSISTENT` / `DEFER` | C3/C5 | numerical rerun before promotion |
| v0.26 numerical profiled singular values/stds/noise/multistart | numerical effects | no JSON/status closure; exploratory nuisance choices | `PREREGISTERED RERUN REQUIRED` plus replay gap | C3/C5 | fresh contract required |
| v0.27 hierarchical repeated-trial direction | future idea | no execution and not authorized | `DEFER / OPEN QUESTION` | C5 | MASTER decision only |

No item in the sweep received `EXACT REPLAY PASS` or `EXACT REPLAY FAIL`; see Section 5.

## 5. Exact replay attempts and execution-environment limitations

### 5.1 Environment

Available deterministic numerical environment during the sweep:

- Python `3.13.5`
- NumPy `2.3.5`
- SciPy `1.17.0`
- Linux `6.18.35`, x86_64, glibc 2.41.

The frozen recovery tree gave exact blob identities for all listed reference scripts, JSON files and status notes.

### 5.2 Faithful-replay rule applied conservatively

The sweep did not label a run `EXACT REPLAY PASS` unless the exact committed artifact could be materialized and executed with its dependency chain unchanged. The connected GitHub interface allowed complete source/static inspection but did not provide a faithful local recovery checkout for the entire import-linked reference tree. Reconstructing scripts manually from displayed source would violate the command's instruction not to call an approximate reconstruction an exact replay.

Therefore v0.7–v0.26 implementation executions are classified `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` where replay matters.

### 5.3 v0.6 numerical recomputation

The deterministic equations and constants in `core_v06_two_cell_pitchfork.py` were independently recomputed in the available SciPy environment without altering model, parameters or tolerances. The recomputed values agree with the stored JSON, including approximately:

- `T*=13.4306902002865`
- `p*=6.7153451001432`
- `chi^2/Delta p=2.0256177404`
- `sigma=-0.01840410444`
- `c_chi=0.00908567499`.

Because this was not execution of the materialized exact legacy blob in its original checkout/import environment, the result is deliberately called `STATICALLY CONSISTENT / independent numerical recomputation`, not `EXACT REPLAY PASS`.

### 5.4 v0.9 fifth-order gap

The v0.9 reference script does not itself generate the fifth-order coefficient set used for `b2/L2`; it consumes stored fifth-order numbers and checks downstream algebra. The generating AD artifact is absent from the recovery snapshot. Independent fifth-order replay therefore remains `REPLAY PENDING — ENVIRONMENT/ARTIFACT GAP` even if the stored arithmetic is internally consistent.

### 5.5 v0.26 closure gap

The recovery snapshot contains the v0.26 document and script, but no `core_v026_reference.json` and no `README_v0.26_status.md`. This is a genuine closure gap. The script can be a future replay source; the numerical v0.26 result is not treated as a closed legacy benchmark.

## 6. Contradictions and canonical repairs

### 6.1 v0.6 B-sign wording

RB-007 independently froze

`B = -T^2 w_c ∫ S'(Psi_0)R_T'(...) d sigma`

for the canonical residual `F = integral - 2pi`.

v0.6 calls the negative sign a historical error and uses a positive `B`, but its script simultaneously defines the entire existence residual with the opposite sign, `F_legacy = 2pi - integral = -F_canonical`. Consequently every residual derivative, including `B`, changes sign. The branch equation, `B=0` locus and branch geometry are invariant under this global residual sign change.

**Repair:** the canonical negative RB-007 coefficient is retained. The v0.6 sentence declaring it an erratum is `SUPERSEDED / REJECT`; v0.6 numerical branch geometry is not rejected merely because of the convention change.

### 6.2 v0.8 threshold-contact label

RB-007 freezes that the smooth baseline response is flat/smooth through its threshold and that `Psi=h` is not by itself a nonsmooth hybrid boundary. Therefore the v0.8 terminology “hybrid codimension-two” for an NS/threshold-contact intersection is too strong under the frozen baseline.

**Repair:** retain, at most, an exploratory geometric intersection of an NS condition with a threshold level set; reject the claim that the threshold level alone constitutes a hybrid singularity for the baseline.

### 6.3 v0.7/v0.11 “exact” wording

The legacy event/invariant-circle chain combines exact alpha/base-state formulas with finite history cutoffs, numerical root solving, quadrature and finite Fourier/collocation representations.

**Repair:** reserve “exact” for the analytic alpha flow, event equations and exact fixed-chart identities. Numerical invariant objects are high-accuracy reference calculations, not rigorous infinite-dimensional existence proofs.

### 6.4 v0.5 full-spectrum equivalence

RB-010 explicitly does not freeze equivalence between the spike-time characteristic spectrum and every auxiliary full hybrid-state Floquet mode. Any v0.5 normal-form argument that assumes that complete equivalence must state it as an extra assumption or await an equivalence gate.

### 6.5 v0.9 fifth-order provenance

The stored fifth-order Chenciner coefficient is not independently generated by the committed reference script. It must not be described as independently replayed from the recovered artifact set.

## 7. Independent mathematical verifications added by this sweep

### 7.1 v0.13 causal in-flight propagation

Let a packet launched at `s` carry remaining path distance `rho` and satisfy

`rho_dot(t)=-c(t)`, `rho(s)=L>0`.

If `c` is continuous and `c(t)>=c_min>0`, then `rho` is strictly decreasing and reaches zero exactly once in finite time. Packets on the same edge obey the same scalar travel integral, so launch order is preserved (FIFO) while the speed law is common.

For the arrival `a` defined by

`∫_s^a c(u)du=L`,

variation gives

`c(a) delta a - c(s) delta s + ∫_s^a delta c(u)du = 0`,

hence

`delta a = [c(s)delta s - ∫_s^a delta c(u)du]/c(a)`.

In particular, `da/ds=c(s)/c(a)` when only launch time varies.

**Label:** PROPOSITION / PROVED under `c>=c_min>0`.
**Provenance:** DERIVATION HERE / PROJECT in-flight semantics.

### 7.2 v0.23 projected pre-event alpha observation

Before any event,

`q(t)=e^{-alpha t}q_0`,

`psi(t)=e^{-alpha t}(psi_0+t q_0)`.

For the unit zero-mean spatial contrast `v` and latent coefficients `xi_psi,xi_q`, the projected observation is

`z_psi(t)=e^{-alpha t}(xi_psi+t xi_q)`

with sensitivity row

`g(t)=e^{-alpha t}(0,0,0,0,1,t)`.

Appending one scalar row gives the Gram update

`J_+^T J_+ = J^T J + g^T g`.

Cauchy interlacing for a rank-one positive update implies that the new smallest singular value cannot exceed the old second-smallest singular value:

`sigma_min([J;g]) <= sigma_{n-1}(J)` for an `n`-column full-rank `J`.

**Label:** LEMMA / PROVED.
**Provenance:** DERIVATION HERE.

The optimized legacy `t_m` and 250× effect do not follow as a theorem and remain C3.

### 7.3 v0.25 duplicate-trial information scaling

For exactly duplicated trial Jacobians,

`J_dup=[J;J]`, so `J_dup^T J_dup=2 J^T J`.

Every singular value is therefore multiplied by `sqrt(2)` and the singular-vector geometry is unchanged. Replication reduces independent measurement noise but cannot rotate a near-null sensitivity direction.

**Label:** LEMMA / PROVED.
**Provenance:** DERIVATION HERE.

### 7.4 v0.26 nuisance profiling

For one trial with local model

`delta y = J_s delta theta_s + N delta z + epsilon`,

and homoscedastic independent Gaussian noise, minimizing least squares over the nuisance coordinate `delta z` projects the shared-parameter signal onto the orthogonal complement of `col(N)`:

`R=(I-P_N)J_s`.

The profiled local Fisher information is

`I_profile = sigma_t^{-2} R^T R`.

For independent trials, stack the residualized matrices before forming `R^T R`. If `N` is rank deficient, `P_N` means the orthogonal projector onto `col(N)`, equivalently defined by the Moore–Penrose pseudoinverse.

**Label:** PROPOSITION / PROVED.
**Provenance:** DERIVATION HERE / standard linear-Gaussian profiling.

### 7.5 v0.26 structural pulse self-calibration ambiguity

Assume:

1. the pulse occurs at a fixed time `t_p` before the first physical event;
2. the full real `q=1` initial synaptic subspace is free in both `(psi_0,q_0)`;
3. the two independent relative `q=1` phase coordinates are free;
4. the pulse reset is restricted to the same real `q=1` synaptic subspace;
5. the event chart is regular and labelled spike times are the downstream observations.

The pre-pulse alpha flow in the `q=1` synaptic subspace is

`(psi_0,q_0) -> e^{-alpha t_p}(psi_0+t_p q_0, q_0)`.

Its block-triangular linear map is invertible. Any infinitesimal change in pulse amplitude/direction coordinates `(A,beta,gamma)` changes only the `q=1` synaptic reset vector. Because the pre-pulse synaptic state is freely adjustable through the invertible initial-state map, an equal and opposite pre-reset state variation can cancel the pulse-reset variation exactly. The resulting pre-pulse relative phase variation can simultaneously be cancelled using the two free relative phase coordinates. The post-pulse relative state is therefore unchanged to first order, and every subsequent fixed-chart labelled spike time is unchanged to first order.

Thus the `(A,beta,gamma)` calibration sensitivity columns lie in the trial-state nuisance span under these assumptions.

**Label:** PROPOSITION / PROVED UNDER STATED ASSUMPTIONS.
**Provenance:** DERIVATION HERE.

This proof does **not** automatically absorb a perturbation of `t_p`, because changing pulse time changes both the flow duration and the time at which the reset is applied. The legacy weak-but-nonzero pulse-time residual is therefore not contradicted.

## 8. C1–C5 disposition summary

### C1 — recoverable mathematics

High-confidence C1 candidates now include:

- v0.5 abstract smooth-map normal-form algebra, conditionally on smoothness/nonresonance and without full hybrid-spectrum equivalence;
- v0.9/v0.10 abstract generalized-NS radial algebra, conditionally on valid coefficients;
- v0.13 in-flight packet arrival/FIFO/sensitivity theory;
- v0.16 local fixed-chart event/root derivative formulas;
- v0.17 edge-order invariance and continuous weight-jump derivative logic;
- v0.19 first-order chart-boundary predictor principle;
- v0.21 E/D/A local design definitions;
- v0.23 pre-event projected alpha observation and rank-one information bound;
- v0.25 duplicate-trial `sqrt(2)` scaling;
- v0.26 nuisance profiling and the structural `(A,beta,gamma)` self-calibration ambiguity theorem under explicit assumptions.

### C2 — algorithmic / implementation layer

v0.6–v0.20 contain substantial deterministic reference machinery, especially event maps, invariant-circle solvers, packet queues, graph batching and chart-aware differentiation. The code is valuable, but canonical software claims need faithful replay or a new frozen validation contract. Static audit alone is not a production validation.

### C3 — effect-bearing legacy results

All actual Lighthouse bifurcation/global-object effects from v0.6–v0.15 and optimized/effect-selected inference/design findings from v0.21–v0.26 remain C3. Reproducing their old output exactly would establish reproducibility of the exploratory lineage, not convert it into confirmatory evidence.

### C4 — exploratory/historical only

Superseded v0.24 pulse prototypes, deleted/replaced design notes, historical `COMPLETE/VERIFIED/CERTIFIED` labels and interpretation statements contradicted by later freezes remain provenance only.

### C5 — unresolved/gap

Key C5 items are full spike-time-vs-full-hybrid spectral equivalence, unconditional high-order smoothness of the alpha event operator across all moving arrivals, rigorous existence of the global invariant circles/folds claimed numerically, v0.9 fifth-order generator closure, continuum limits requiring proof, and v0.26 numerical closure without JSON/status.

## 9. Items effectively closed by existing canonical work

No further scientific gate is needed merely to rediscover:

1. baseline Lighthouse/alpha/event/delay mathematics — RB-004/RB-006;
2. normalized continuation/gauge/first-hit/two-cell branch mathematics — RB-007/RB-009;
3. narrow spike-time Floquet operator, neutral mode, alpha lag convergence and full-operator symmetry qualifications — RB-010;
4. the historical v0.6 apparent `B`-sign conflict — resolved here as a residual-convention issue while retaining RB-007;
5. the invalid interpretation of smooth baseline threshold contact as automatically hybrid/nonsmooth — already repaired by RB-007 and confirmed in this sweep;
6. the elementary in-flight propagation identities in Section 7.1 — mathematically closed enough for a narrow future freeze decision;
7. the v0.23 observation formula/rank-one bound — mathematically closed enough for a narrow future freeze decision;
8. the v0.25 duplicate-trial information scaling — mathematically closed;
9. the v0.26 nuisance-profiling and fixed-time `(A,beta,gamma)` self-calibration propositions — mathematically closed under their stated assumptions.

## 10. Genuinely unresolved mathematical claims

1. **Full spectral equivalence:** when and in what exact state space does the spike-time characteristic spectrum represent all nontrivial Floquet modes of the full hybrid alpha-synapse system?
2. **Higher regularity:** sufficient conditions for `C^2/C^3/C^5` smoothness of the exact event/return operator across moving alpha-arrival configurations; this controls rigorous baseline pitchfork/Chenciner applicability.
3. **Rigorous invariant objects:** theorem-level existence/uniqueness of the numerical invariant circles, basin-boundary circles and global invariant-circle fold observed in v0.11/v0.15.
4. **v0.9 fifth-order generation:** exact provenance/reproduction of the fifth-order coefficient generator underlying stored `b2/L2`.
5. **General cluster transverse decomposition:** equitability guarantees a quotient but not, by itself, the complete transverse invariant decomposition of a general nonnormal characteristic operator; extra symmetry/invariance assumptions remain necessary.
6. **Discrete-to-continuum limit:** a rigorous/asymptotic convergence theorem for event-based ring symbols under explicit normalization.
7. **Pulse-time nuisance:** a structural classification of the residual pulse-time calibration direction beyond the numerical v0.26 example.

These are the mathematical issues that could justify new proof work; the rest of the unresolved queue is implementation replay or confirmatory rerun rather than theory rediscovery.

## 11. Exact-replay-needed implementation claims

If the corresponding project direction is selected, faithful recovery-environment replay is still useful for:

- v0.7 event-map lag-history convergence and finite-difference normal-form plumbing;
- v0.9–v0.11 AD/Fourier/collocation code paths, with the v0.9 fifth-order generator gap explicitly resolved first;
- v0.13–v0.15 packet/adaptive-event reference engines as software objects, separate from C3 effects;
- v0.16 fixed-capacity JAX packet queue, tangent and dynamic-chart value equivalence;
- v0.17 graph/batch/edge-order implementation and scaling correctness;
- v0.18 fixed-chart inverse Jacobian plumbing;
- v0.19 multichart rerecording optimizer mechanics;
- v0.20 latent-phase fixed-chart derivatives;
- v0.21–v0.23 exhaustive subset/sensor code only if these are needed as reusable tooling;
- v0.24/v0.25 active-pulse machinery as implementation, not as confirmatory effect evidence;
- v0.26 script execution, especially because no benchmark JSON/status artifact closes that version.

A single consolidated implementation replay contract is preferable to reopening one micro-gate per legacy version, provided it fixes the exact recovery SHA, environment, permitted methods and failure rules in advance.

## 12. C3 scientific effects requiring preregistered rerun

### Bifurcation / dynamics block v0.6–v0.15

- two-cell pitchfork location/scaling and associated dynamic multiplier behavior;
- genuine flip and ring NS critical points and normal-form coefficients;
- v0.8 NS/threshold-level intersection geometry if still scientifically desired, but without the rejected baseline “hybrid” label;
- Chenciner point, `L1=0`, fifth-order `L2`, unfolding wedge and FIC predictions;
- small/large invariant-circle branches and folds;
- adaptive-delay slow-passage/dynamic-skip effects;
- global timing-modulated attractor/coexistence/hysteresis;
- global invariant-circle fold near legacy `tau_F≈8.00731` and its basin-boundary classification.

### Inference / design block v0.18–v0.26

If used as scientific evidence rather than software examples, preregister:

- inverse recovery/noise performance and chart crossing results v0.18–v0.20;
- v0.21 optimized observation schedules and gains;
- v0.22 magnitude/direction of the latent-state information bottleneck and nonlinear aliases;
- v0.23 optimized measurement time and information gain;
- v0.24 pulse family/bounds/margin rule, reference pulse, 87× gain and selected spike subset;
- v0.25 complementary second probe, 788×/557× gains and E-optimal eight-row design;
- v0.26 preparation-jitter amplitudes, calibration uncertainty model, numerical profiled information, nonlinear recovery and noise performance.

For active-design confirmation, the preregistration must freeze **before output inspection** at least: pulse family, amplitude/time/direction bounds, observation horizon/candidate pool, chart-safety rule, noise model, objective, optimization/search procedure, finite validation set and acceptance/robustness rules.

## 13. Rejected, superseded and deferred material

### Rejected / superseded

- the v0.6 prose claim that the canonical RB-007 negative `B` sign is itself an error;
- the v0.8 interpretation of smooth baseline threshold contact as automatically a hybrid/nonsmooth codimension-two event;
- any unqualified “exact/certified” wording for finite-history/Fourier/collocation invariant objects;
- any unnormalized use of `|y^*M'(mu)xi|` as a scale-independent condition number;
- the superseded/deleted v0.24 aggressive and simplified pulse-design prototypes as scientific evidence.

### Deferred / open

- full hybrid spectral equivalence;
- rigorous global invariant-object proofs;
- continuum convergence;
- missing/unlabelled spikes and unknown topology;
- hierarchical repeated-trial population model proposed after v0.26;
- all v0.27 work.

## 14. Minimal recommended next-work queue

This ordering removes the largest amount of uncertainty per new gate while respecting dependencies.

### Q1 — Consolidated C1 theory promotion gate — highest leverage

MASTER should consider one narrow mathematical gate that canonicalizes only the strongest newly verified C1 material:

1. v0.13 in-flight packet arrival/FIFO/sensitivity theory;
2. v0.23 pre-event projected alpha observation and rank-one information bound;
3. v0.25 duplicate-trial information scaling;
4. v0.26 nuisance profiling and fixed-time `(A,beta,gamma)` self-calibration ambiguity under explicit assumptions.

This requires no effect search and would convert several repeatedly reused legacy formulas into canonical premises.

### Q2 — Consolidated C2 implementation replay contract

If near-term work needs differentiable simulation/inference infrastructure, freeze one deterministic replay contract around v0.16–v0.20 first: queue value/tangents, sparse graph/batch, fixed-chart inverse Jacobian and multichart rerecording. These are dependencies for later active-design validation and have higher implementation leverage than replaying every old bifurcation script.

### Q3 — Choose one preregistered dynamics target, not the whole atlas

If nonlinear dynamics is a priority, select **before rerun** one high-value hypothesis, preferably the v0.15 global invariant-circle fold/coexistence story because it integrates the earlier local theory and has a strong falsifiable structure. Freeze model, parameter path, continuation algorithm, invariant-object diagnostics, chart rules and success/failure criteria before recomputation.

Do not rerun v0.6→v0.15 serially merely because the versions exist.

### Q4 — Separate passive observability, intervention and nuisance confirmation

If inference/experiment design is the priority, use separate preregistered gates:

1. passive latent-state information limit (v0.22 hypothesis);
2. transverse observation/intervention comparison (v0.23/v0.24 hypothesis);
3. multi-probe diversity and trial nuisance/calibration (v0.25/v0.26 hypothesis).

Do not reuse the legacy optimized pulse/subset as if it were preregistered unless it is explicitly frozen as a fixed confirmatory test candidate before rerun.

### Q5 — v0.27 only after MASTER sequencing

The hierarchical many-trial extension remains scientifically natural but unauthorized. It should begin only after MASTER decides which v0.26 pieces are canonical premises and which numerical effects have earned confirmation.

## 15. Proposed freeze candidates — no automatic promotion

The sweep proposes, for MASTER review only, the following narrow candidate package:

1. **In-flight propagation proposition:** `rho_dot=-c(t)`, unique transversal arrival for `c>=c_min>0`, same-edge FIFO and arrival sensitivity formula.
2. **Pre-event observation lemma:** alpha-flow projected observable `z_psi(t)=e^{-alpha t}(xi_psi+t xi_q)` and rank-one singular-value interlacing bound.
3. **Duplicate-trial information lemma:** duplicated Jacobian scales singular values by `sqrt(2)` without changing sensitivity directions.
4. **Nuisance-profile proposition:** `R=(I-P_N)J_s` and profiled local Fisher information.
5. **Pulse self-calibration proposition:** at fixed pre-event pulse time, free full-real-q1 synaptic state plus relative phase freedom absorbs infinitesimal `(A,beta,gamma)` calibration changes under the stated regular-chart assumptions.

Not proposed for freeze by this sweep:

- any optimized measurement time, pulse or observation subset;
- any legacy effect size;
- any actual bifurcation/global invariant-object location;
- any implementation-performance/scaling result without replay;
- the v0.9 fifth-order coefficient set;
- any v0.26 numerical uncertainty value;
- v0.27.

## 16. Overall sweep decision

\[
\boxed{\text{PASS}}
\]

**PASS — FULL V0.4–V0.26 LEGACY CORPUS CLASSIFIED; NO LEGACY C3 EFFECT PROMOTED.**

Rationale:

1. every legacy version v0.4 through v0.26 was inventoried at the exact recovery SHA;
2. claims were checked against the complete RB-004–RB-010 canonical freeze chain;
3. concrete contradictions were resolved without rewriting frozen science;
4. several C1 statements were independently verified where doing so materially reduced ambiguity;
5. replay gaps were preserved rather than disguised as approximate exact replays;
6. exploratory/effect-selected C3 results remain preregistration-dependent despite strong static artifact consistency;
7. missing v0.26 benchmark/status closure is explicitly recorded;
8. the remaining work has been reduced to a small dependency-ordered queue rather than one gate per historical version.

PASS is a decision about **completion of this verification sweep**, not a statement that every legacy result is true, reproduced or canonical.

No new scientific effect was searched. No parameter, tolerance, objective, observation horizon, pulse family, geometry or success criterion was retuned. No v0.27, application, novelty or manuscript work was started.

## 17. STOP

The authorized `VERIFY-LEGACY` batch sweep is complete.

CORE must return to MASTER for review of the proposed freeze candidates and next-work queue.

STOP — RETURN TO MASTER
