# CORE Recovery & Canonicalization Gate 0.1

Date: 2026-09-07
Status: PASS — RECOVERY COMPLETE; NO LEGACY SCIENCE PROMOTED OR FROZEN

## 1. Recovery input identity and hashes

This gate audits only the frozen legacy recovery input established by MASTER in `research/master/core_legacy_recovery_snapshot_0_1.md`.

- Repository: `twkroll/haken-lighthouse-jax`
- Canonical branch: `main`
- `main` HEAD at gate execution start: `7890f7db610c3f6eddf019c66812d11bdb7d8028`
- Recovery branch name: `core/theory-v0.1`
- Exact recovery HEAD: `287eae8a86560b78ed94f30a2786243714c33ac0`
- Recovery HEAD message: `CORE v0.26: document trial nuisance and calibration theory`
- Merge base: `948dedbc5294fbe864b940060ee6b2053020347f`
- Branch comparison at recovery: `diverged`; recovery branch 133 commits ahead and 34 commits behind the then-canonical `main`.
- MASTER recovery snapshot blob SHA: `eb7e2c3532f7b0d8f30595e3325aecd788ad0ecb`
- Recovery-gate prompt blob SHA: `7993c8b8165f7f6ea0867c6d9f8361389aab8c36`

Classification throughout this document:

`NON-CANONICAL LEGACY CORE WORKING STATE`

No commit, document, reference script, benchmark JSON, status pointer, numerical value, interpretation, or branch-local label such as COMPLETE / VERIFIED / CERTIFIED is promoted to canonical scientific status by this recovery gate.

## 2. Commit/version lineage

The immutable recovered lineage is the 133-commit segment after merge base `948dedbc5294fbe864b940060ee6b2053020347f` through `287eae8a86560b78ed94f30a2786243714c33ac0`.

The recovered scientific version ladder is:

| Version | Recovered working topic | Branch-local status evidence |
|---|---|---|
| v0.1 | canonical hybrid Lighthouse model | called COMPLETE in legacy research program |
| v0.2 | exact analytical benchmarks and derivations | COMPLETE |
| v0.3 | continuation and hybrid admissibility | COMPLETE |
| v0.4 | spike-time Floquet and symmetry theory | COMPLETE |
| v0.5 | synergetic order parameters and normal forms | COMPLETE AT THEORY-CONTRACT LEVEL |
| v0.6 | first numerical atlas | COMPLETE |
| v0.7 | dynamic event normal forms | COMPLETE |
| v0.8 | hybrid codimension-two structure | COMPLETE |
| v0.9 | smooth Chenciner point | COMPLETE |
| v0.10 | local Chenciner unfolding | COMPLETE |
| v0.11 | exact invariant circles and FIC | COMPLETE |
| v0.12 | adaptive-conduction slow-fast benchmark | COMPLETE |
| v0.13 | causal in-flight conduction semantics | COMPLETE |
| v0.14 | full adaptive packet-queue event engine | COMPLETE |
| v0.15 | global hybrid invariant-circle fold | VERIFIED / COMPLETE in legacy summaries |
| v0.16 | fixed-capacity JAX packet queue | legacy-certified implementation layer |
| v0.17 | sparse graph / batch scaling | completed working layer |
| v0.18 | chart-aware inverse problem | completed benchmark |
| v0.19 | hybrid multi-chart optimizer | completed benchmark |
| v0.20 | latent relative-phase inference | completed benchmark |
| v0.21 | optimal observation design | completed benchmark |
| v0.22 | latent synaptic-state information limit | completed benchmark |
| v0.23 | transverse subthreshold observation | completed benchmark |
| v0.24 | chart-safe active pulse experiment design | completed benchmark after superseded prototypes |
| v0.25 | full real q=1 two-probe experiment | completed benchmark |
| v0.26 | trial-specific preparation and pulse-calibration nuisance | latest recovered working version |

This ladder is scientific working evidence only. The canonical governance lineage did not advance with it: at recovery HEAD, legacy `research/core/STATUS.md` still said `CORE Mathematical Scope Gate 0.1`, `READY`, latest canonical file `none yet`; the legacy MASTER status likewise still waited for that gate.

### 2.1 Superseded / deleted lineage evidence

The recovered history contains explicit iterative replacement, not a single preregistered immutable scientific sequence. A concrete late example is CORE v0.24:

- `9ec3f6224304420c0292581dac32ac7661342c34` — `CORE v0.24: add active pulse reference solver` introduced an aggressive prototype with `A_MAX=0.12`, `MARGIN_MIN=0.05`, and a stored reference pulse with amplitude `0.12` and pulse time approximately `0.01741`.
- `3e6eb643de6ab01d6333a77972030d96bf41eb20` — `CORE v0.24: remove superseded aggressive pulse prototype` deleted that implementation.
- `c8a88e731e0942435762ef1785bd258c606e0e91` — `CORE v0.24: document chart-safe active experiment design` documented a simplified design with `A<=0.1`, chart margin floor `0.05`, and a three-coordinate pulse parameterization.
- `c0016d5d08cc9dda250cc2039c4321de4bb5b505` — `CORE v0.24: remove superseded simplified active-experiment note` deleted that note.
- The recovery snapshot finally contains `docs/core/active_pulse_design_v0.24.md` and `reference/core_v024_active_pulse_design.py` with the later chart-safe four-coordinate pulse family and hard margin floor `0.06`.

This is not evidence of misconduct. It is evidence that v0.24 was iterative/exploratory and that the final optimized numerical design cannot be treated as a preregistered confirmatory result.

## 3. Artifact manifest

### 3.1 Foundational / unversioned CORE documents

- `docs/core/mathematical_core.md` — long-form mathematical core, internally labelled Mathematical Core v0.5.
- `docs/core/research_program.md` — recovered version ladder and historical next-step program.
- `docs/core/benchmark_contract_v0.2.md` — benchmark contract foundation.

### 3.2 Versioned mathematical / scientific documents

Recovered documents include:

- `derivations_v0.2.md`
- `continuation_bifurcations_v0.3.md`
- `continuation_contract_v0.3.md`
- `spike_time_floquet_v0.4.md`
- `floquet_contract_v0.4.md`
- `symmetry_reductions_v0.4.md`
- `order_parameter_normal_forms_v0.5.md`
- `normal_form_contract_v0.5.md`
- `numerical_atlas_v0.6.md`
- `event_normal_forms_v0.7.md`
- `codimension_two_v0.8.md`
- `chenciner_v0.9.md`
- `chenciner_unfolding_v0.10.md`
- `invariant_circles_v0.11.md`
- `adaptive_delays_v0.12.md`
- `in_flight_delays_v0.13.md`
- `adaptive_event_engine_v0.14.md`
- `global_invariant_circle_fold_v0.15.md`
- `jax_packet_queue_v0.16.md`
- `graph_batch_scaling_v0.17.md`
- `inverse_problem_v0.18.md`
- `hybrid_multichart_optimizer_v0.19.md`
- `latent_state_inference_v0.20.md`
- `observation_design_v0.21.md`
- `latent_synaptic_state_v0.22.md`
- `transverse_observation_v0.23.md`
- `active_pulse_design_v0.24.md`
- `full_q1_two_probe_v0.25.md`
- `trial_nuisance_calibration_v0.26.md`

### 3.3 Status summaries

Versioned status summaries are present from `README_v0.13_status.md` through `README_v0.25_status.md`. No `README_v0.26_status.md` is present at the frozen recovery snapshot.

### 3.4 Reference implementations

The snapshot contains reference scripts from v0.6 through v0.26, including special multiple-script implementations for v0.16 and v0.17. Representative late files are:

- `reference/core_v018_inverse_problem.py`
- `reference/core_v019_multichart_optimizer.py`
- `reference/core_v020_latent_state_inference.py`
- `reference/core_v021_observation_design.py`
- `reference/core_v022_latent_synaptic_state.py`
- `reference/core_v023_transverse_observation.py`
- `reference/core_v024_active_pulse_design.py`
- `reference/core_v025_full_q1_two_probe.py`
- `reference/core_v026_trial_nuisance_calibration.py`

### 3.5 Benchmark JSON

Machine-readable benchmark JSON exists from v0.6 through v0.25. No `benchmarks/core_v026_reference.json` is present at recovery HEAD. Thus v0.26 has a scientific document and reference script but lacks the same benchmark/status closure pattern as v0.25 and earlier late versions.

### 3.6 Relationship among artifact types

The recovered pattern is generally:

`scientific/theory document -> reference script -> benchmark JSON -> status summary -> benchmark-contract additions`

but it is not perfectly uniform. Early versions rely more heavily on foundational documents/contracts; v0.13 onward gains explicit status pointers; v0.26 is incomplete relative to the late-version pattern because the benchmark JSON and status pointer are absent.

## 4. Original Scope Gate 0.1 substantive-coverage matrix

| Original required item | Recovered coverage | Recovery assessment |
|---|---|---|
| Scope | `mathematical_core.md` defines a project mathematical core and separates historical, contemporary, and project material | SUFFICIENT IN SUBSTANCE, but not written as the required gate deliverable |
| Source map | `[H]`, `[C]`, `[P]` provenance tags distinguish historical Haken, contemporary reconstruction, and project extension | REQUIRES REPAIR: no sufficiently precise bibliographic source map / primary-source equation mapping was found in the foundational file |
| Canonical equations and notation | graph phase equation, synaptic input, spike train, LHGS project canonicalization, phase-locked and synchronous forms | STRONG SUBSTANTIVE COVERAGE |
| Event / spike definition | lifted phase crossing, event surface, spike counter, reset/jump separation, transversality/admissibility | STRONG SUBSTANTIVE COVERAGE |
| Synaptic and delay definitions | exponential and alpha kernels, state-space realizations, fixed edge delays, later in-flight semantics | STRONG SUBSTANTIVE COVERAGE; later adaptive semantics exceed baseline scope |
| Baseline assumptions | causality, kernel normalization, row-sum/synchrony conditions, reset-convention distinction, regular-event assumptions | SUBSTANTIAL but dispersed; requires a single canonical assumptions table |
| Variant registry | reset conventions, response families, exponential/alpha kernels, external drive, adaptive delays and later extensions appear across documents | SUBSTANTIAL but not a formal frozen variant registry; requires repair |
| Analytical validation targets | synchrony, phase locking, delay effects, stability/Floquet, continuum/symmetry, waves/pattern-related structures and later invariant objects | EXCEEDS MINIMUM IN SUBSTANCE |
| Explicit exclusions | limitations and scope statements exist locally | INSUFFICIENT AS ORIGINAL GATE ARTIFACT: no single pre-execution exclusion freeze satisfying the original gate |
| Gate decision material | branch-local version status exists | FORMALLY ABSENT for Scope Gate 0.1 |
| Proposed freeze contents | `mathematical_core.md` behaves like a proposed mathematical specification | SUBSTANTIVE CANDIDATE, but no MASTER-authorized proposed freeze package was submitted through the required gate |
| Open questions | many later documents and research program contain explicit next questions | STRONG BUT DISPERSED |

### Scope-Gate recovery conclusion

`CORE Mathematical Scope Gate 0.1` was **satisfied in substantial mathematical content**, especially by `docs/core/mathematical_core.md` plus `docs/core/derivations_v0.2.md`, but it was **not completed as a governed gate**. The most important repairs are:

1. primary-source / equation-level source map;
2. explicit baseline assumption and variant registry;
3. pre-execution exclusions;
4. formal gate decision and proposed freeze package;
5. CORE STATUS / STOP transition.

This recovery gate therefore does not retroactively declare Scope Gate 0.1 PASS.

## 5. Mathematical/source-derived claim inventory

### 5.1 SOURCE-DERIVED candidates

The legacy `[H]` / `[C]` material includes candidates such as:

- Lighthouse phase evolution `dot(theta_i)=S(psi_i)` and spike-driven synaptic input structure;
- firing by phase-section crossing;
- Haken reset-convention variants;
- thresholded/saturating response-function structure;
- exponential synaptic kernel;
- contemporary smooth threshold response and alpha-kernel formulation;
- later modern adaptive-delay structures where explicitly attributed.

Epistemic status in this recovery report: **SOURCE-DERIVED CANDIDATE**, not THEOREM / PROVED by this project. Exact primary-source citations must be verified before canonical adoption.

### 5.2 DERIVATION HERE candidates

The recovered project derivations include:

- alpha-kernel state-space equivalence and jump normalization;
- exact periodic alpha-kernel comb;
- isolated-clock and autapse period relations;
- general phase-locked self-consistency equations;
- first-hitting / admissibility conditions;
- event-time perturbation formula under transversality;
- spike-time Floquet operators and symmetry-sector reductions;
- center-manifold / order-parameter normal-form contracts;
- later nuisance-profile projection formulas for inference.

Recovery epistemic classification: mostly **LEMMA / PROPOSITION CANDIDATE — DERIVATION HERE**. None is upgraded to `THEOREM / PROVED` without a dedicated mathematical verification pass.

### 5.3 PROJECT ASSUMPTION / INTERPRETATION candidates

Examples include:

- explicit additive external-input notation;
- LHGS naming/canonicalization;
- choice of response/kernel families for project baselines;
- chart-safety margins and benchmark tolerances;
- identification of critical Floquet-mode amplitude as project order parameter;
- scientific rules such as separating event-chart validity from smooth fixed-chart differentiation;
- nuisance-profile interpretation in v0.26.

These remain **ASSUMPTION / INTERPRETATION** unless separately proved or source-supported.

## 6. Numerical / implementation / benchmark inventory

### v0.6–v0.15

Contains numerical bifurcation atlas work, event normal forms, codimension-two and Chenciner searches, invariant circles/FIC, adaptive slow-fast experiments, causal in-flight delay tests, full adaptive event simulation, and global invariant-circle-fold classification.

Classification: `NUMERICAL RESULT`, `BENCHMARK / REFERENCE OUTPUT`, and in several versions `MATHEMATICAL CLAIM` supported numerically.

### v0.16–v0.17

Contains fixed-capacity JAX packet-queue implementation and sparse graph/batch scaling.

Classification: `IMPLEMENTATION ARTIFACT`, `BENCHMARK / REFERENCE OUTPUT`, plus numerical validation claims.

### v0.18–v0.20

Contains chart-aware inverse inference, a hybrid multi-chart optimizer, and latent phase inference.

Classification: `INFERENCE RESULT`, `IMPLEMENTATION ARTIFACT`, `BENCHMARK / REFERENCE OUTPUT`, `INTERPRETATION`.

### v0.21–v0.25

Contains optimal observation design, latent-state identifiability analysis, transverse observation design, active pulse design, and a two-probe active experiment.

Classification: `EXPERIMENT-DESIGN RESULT`, `INFERENCE RESULT`, `NUMERICAL RESULT`, `BENCHMARK / REFERENCE OUTPUT`, `INTERPRETATION`.

### v0.26

Contains trial-specific nuisance profiling and pulse-calibration analysis. It has a reference script but no matching benchmark JSON/status pointer at the frozen recovery snapshot.

Classification: `INFERENCE RESULT`, `MATHEMATICAL CLAIM`, `NUMERICAL RESULT`, `INTERPRETATION`, with weaker artifact closure than v0.25.

## 7. Governance provenance audit

The canonical authorization that remained in force while the legacy branch was produced was still `CORE Mathematical Scope Gate 0.1`. Legacy `research/core/STATUS.md` never advanced beyond READY, and legacy MASTER governance explicitly stated that no implementation, parameter tuning, benchmarking, learning experiment, or application execution should precede completion of that gate.

Accordingly:

| Legacy layer | Compatibility with then-canonical authorization |
|---|---|
| v0.1 baseline definitions / source separation | broadly within substantive Scope Gate intent, but required gate file/status transition omitted |
| v0.2 analytical baseline derivations | partly within analytical-validation scope; already extends beyond a minimal scope-only deliverable |
| v0.3–v0.5 continuation/Floquet/normal-form theory | beyond the formally authorized first gate |
| v0.6–v0.15 numerical scientific execution | outside formal authorization |
| v0.16–v0.17 JAX implementation/scaling | explicitly outside formal authorization |
| v0.18–v0.20 inference/optimization | outside formal authorization |
| v0.21–v0.25 observation/active experiment design | outside formal authorization |
| v0.26 nuisance/calibration experiment | outside formal authorization |

Required STOP transitions were therefore not performed. This is a governance provenance defect, not by itself a statement that the mathematics or numerical outputs are false.

## 8. Exact-replay audit and limitations

The recovery prompt authorized exact replay but forbade scientific repair, retuning, rescanning, or new experimentation.

### 8.1 Full executable replay

A full committed-script replay was **not completed in this gate**. The available connector exposed repository files and history for audit but did not provide an executable checkout of the legacy snapshot into the scientific runtime. Reconstructing/refactoring the multi-version dependency tree manually would itself risk altering the committed execution environment and is therefore not treated as an exact replay.

Result classification: `EXACT COMMITTED REPLAY — NOT PERFORMED; ENVIRONMENT / CHECKOUT LIMITATION`.

No scientific result is accepted on the basis of this limitation.

### 8.2 Static committed-output consistency checks

Independent arithmetic checks of stored summary numbers were performed without changing parameters or objectives:

- v0.23: `0.228772004925 / 9.13748e-4 = 250.3666`, consistent with recorded `250.37x`.
- v0.24: `0.07955699 / 9.13748e-4 = 87.0667`, consistent with recorded `87.07x`.
- v0.24 unsafe-vs-reference objective difference is approximately `0.08134%`, consistent with the stated `<0.1%` safety cost comparison.
- v0.25: `0.1468571 / 1.86287e-4 = 788.3379`, consistent with `788.34x` P1-alone gain.
- v0.25: `0.1468571 / 2.63450e-4 = 557.4382`, consistent with `557.44x` duplicate-P1 gain.
- v0.25 rounded-vs-refined objective loss is approximately `0.07304%`, consistent with the stated `~0.073%`.

These are only internal consistency checks of committed values, not reproduction of dynamics, Jacobians, optimization, noise audits, or benchmark tolerances.

### 8.3 Replay priority for future MASTER-authorized work

If MASTER chooses to re-verify legacy science, exact replay should begin with:

1. foundational deterministic analytical benchmarks v0.2;
2. a small canonical event/Floquet benchmark before importing later code;
3. v0.16/v0.17 implementation-equivalence tests only after the model/event semantics are frozen;
4. separately preregistered reruns, not mere replays, for effect-selected/optimized late experiments.

## 9. Anti-cherry-picking / design-provenance audit

The recovery snapshot does not support a blanket claim that all numerical objectives, geometries, horizons, parameter choices, constraints, and success criteria were fixed before effect inspection.

No misconduct is inferred from missing or evolving records. The classifications below concern confirmatory provenance only.

| Version range | Design provenance classification | Reason |
|---|---|---|
| v0.1–v0.2 | PRE-SPECIFIED / TRACEABLE for definitions and explicit derivations; source provenance incomplete | primarily mathematical construction rather than effect search |
| v0.3–v0.5 | PARTIALLY TRACEABLE | theory program evolves through successive continuation/stability/normal-form targets |
| v0.6–v0.15 | PARTIALLY TRACEABLE to CLEARLY POST-HOC / EXPLORATORY for discovered numerical structures | successive searches and newly discovered bifurcation/global objects feed the next target |
| v0.16–v0.20 | PARTIALLY TRACEABLE | implementation/inference targets inherit selected prior benchmark points and charts |
| v0.21 | CLEARLY EXPLORATORY as an optimization result | observation subsets are explicitly searched and optimized |
| v0.22–v0.23 | PARTIALLY TRACEABLE / EXPLORATORY | latent block and sensor design are chosen in response to observed weak directions |
| v0.24 | CLEARLY POST-HOC / EXPLORATORY | committed lineage contains superseded pulse prototypes and changed amplitude/margin/parameterization choices |
| v0.25 | PARTIALLY TRACEABLE / EXPLORATORY | second probe is designed after inspecting v0.24/P1 sensitivity geometry; rounded/refined designs are compared |
| v0.26 | PARTIALLY TRACEABLE / EXPLORATORY | nuisance amplitudes, calibration uncertainties, and target profiling extend the observed v0.25 limitations |

Consequence: late numerical results remain valuable hypothesis-generating and method-development evidence, but optimized effect sizes/designs cannot be frozen as confirmatory results without a fresh MASTER-authorized preregistration and rerun.

## 10. Detailed treatment of v0.24, v0.25, v0.26

### 10.1 CORE v0.24 — active hybrid experiment design

Recovered scientific question: whether a known pre-event pulse can remove the v0.22 spike-time weak direction while retaining labelled spike-time-only observation.

Final recovery-snapshot pulse family:

`d(gamma)=cos(gamma)*v1+sin(gamma)*v2`,

`psi^+ = psi^- + A*cos(beta)*d(gamma)`,

`q^+ = q^- + A*sin(beta)*d(gamma)`,

with a hard event-chart safety constraint and E-optimal smallest-singular-value objective.

Recovered reference values include `t_p=0.05`, `A=0.1`, `beta=0.55`, `gamma=-0.1`, chart margin approximately `0.06285675`, pulsed `sigma_min≈0.07955699`, and an approximately `87.07x` ratio relative to the stored no-pulse weakest singular value. A nearby lower-margin pulse had only about a `0.081%` objective advantage, motivating the legacy hybrid-safety interpretation.

Meaning of `active hybrid experiment design`:

- **active**: a known intervention deforms the trajectory to generate transverse spike-time sensitivity instead of adding a direct hidden-state sensor;
- **hybrid**: candidate interventions must be evaluated on a physically recorded event chart, with continuous derivatives used only inside the valid chart and event-order collision proximity treated as an admissibility constraint.

Recovery classification:

- mathematical pulse/reset family and fixed-chart design principle: `MATHEMATICAL CLAIM / PROJECT INTERPRETATION`, proposed C1 after canonical model semantics are fixed;
- specific optimized pulse, effect size, selected spike subset and noise-recovery results: `EXPERIMENT-DESIGN RESULT / NUMERICAL RESULT`, C3;
- superseded aggressive/simplified prototypes: C4.

### 10.2 CORE v0.25 — two complementary chart-safe probes

Recovered unknown block expands to eight coordinates representing `(p,tau3)`, relative phase, and full real two-dimensional q=1 latent components in both initial `psi` and `q`.

Two trials share the same unknown preparation but use different known pulses. Stored summaries report that one probe alone is formally full rank but poorly conditioned, duplicate P1 barely helps, while complementary P1+P2 strongly improves the weakest sensitivity direction. Stored values include `sigma_min≈0.1468571` for P1+P2 and both chart margins above the hard `0.06` floor.

Legacy interpretation: replication reduces noise, while diverse interventions rotate/change the sensitivity nullspace.

Recovery classification:

- stacked-trial sensitivity formulation: C1/C2 mathematical-computational candidate;
- optimized P2, numerical gains, exact E-optimal subset and noise audit: C3;
- branch-local claim of practical identifiability: INTERPRETATION pending preregistered rerun.

### 10.3 CORE v0.26 — trial nuisance and pulse calibration

v0.26 removes the v0.25 reproducible-preparation assumption. Shared scientific parameters are `(p,tau3)` while each trial has latent preparation nuisance; pulse calibration also receives trial-specific nuisance coordinates.

The key mathematical object is nuisance-profiled shared sensitivity:

`R_r=(I-P_{N_r}) J_{s,r}`,

stacked across trials. Stored numerical results report singular values approximately `(1.11043772,0.32439413)` and shared-parameter standard deviations on the `1e-4` scale under the stored noise model.

The document also argues that several pulse-calibration directions lie in the trial-state sensitivity span to numerical precision, leading to the interpretation that spike times alone cannot self-calibrate the corresponding pulse decomposition when the initial q=1 preparation is unknown. External calibration information is therefore introduced.

Recovery classification:

- nuisance projection algebra: PROPOSITION / DERIVATION-HERE candidate, C1 after mathematical audit;
- structural self-calibration impossibility: PROPOSITION candidate requiring a dedicated proof/review of assumptions, C1/C5 until verified;
- stored nuisance examples, calibration scales, Fisher/noise values and multistart behavior: C3;
- artifact closure is weaker than v0.25 because no matching v0.26 benchmark JSON/status pointer exists at recovery HEAD.

The stated next direction — a hierarchical many-trial preparation model with missing/noisy spikes — is only an `OPEN QUESTION / FORMER NEXT WORKING STEP`. It is not authorized or executed here.

## 11. Canonicalization recommendation classes C1–C5

| Material | Recommendation | Rationale |
|---|---|---|
| Baseline notation, event convention, kernel definitions, explicit project-vs-source separation in v0.1 | C1 — DIRECTLY RECOVERABLE, subject to citation/source-map repair | can be audited without new scientific execution |
| Elementary v0.2 exact derivations (kernel comb, state-space equivalence, basic period/self-consistency identities) | C1 — DIRECTLY RECOVERABLE after mathematical line-by-line check | derivations can be re-established analytically |
| Source-derived `[H]/[C]` attributions without precise bibliographic mapping | C5 until source map repaired; then C1 | provenance is too coarse for canonical source claims |
| v0.3–v0.5 theory contracts | C1/C2 by claim | useful theory, but beyond minimal Scope Gate and needs dedicated verification |
| v0.6–v0.15 selected numerical bifurcation/invariant-object results | C3 — REQUIRES PREREGISTERED RERUN if used as frozen scientific evidence | exploratory search lineage and governance overreach |
| v0.16–v0.17 implementation equivalence/scaling artifacts | C2 — REPLAY-VERIFIABLE | software/reference claims can be tested after model freeze |
| v0.18–v0.20 benchmark inference/optimizer outputs | C2 for implementation mechanics; C3 for scientific performance/effect claims | chart method can be replayed, benchmark success claims need preregistered confirmation if frozen |
| v0.21 optimized observation schedules | C3 | explicit post hoc combinatorial design optimization |
| v0.22 weak-direction numerical effect | C3 | valuable hypothesis-generating result, but design/horizon provenance not confirmatory |
| v0.23 optimized transverse sensor result | C3 | sensor time/operator chosen in response to observed weak direction |
| v0.24 final active pulse numerical result | C3 | iterative/superseded design lineage clearly demonstrates exploratory optimization |
| v0.24 superseded prototypes/notes | C4 — LEGACY EXPLORATORY | retain only as provenance/history |
| v0.25 optimized complementary two-probe result | C3 | designed from v0.24 sensitivity geometry; confirmatory rerun required |
| v0.26 nuisance projection algebra | C1 candidate | mathematical structure can be independently audited |
| v0.26 numerical nuisance/calibration results | C3, with some C5 replay gaps | no matching benchmark JSON/status closure and exploratory nuisance choices |
| former v0.27 hierarchical direction | OPEN QUESTION only | not executed and not authorized |

## 12. Proposed minimal canonicalization sequence

1. **MASTER opens a narrow Scope-Gate Canonicalization / Mathematical Freeze preparation gate.** Use recovered v0.1–v0.2 material as input, not as already frozen truth.
2. **Repair the source map first.** For every `[H]` / `[C]` equation or historical statement, attach precise primary/authoritative source location and separate later reformulations from Haken originals.
3. **Produce the originally missing Scope Gate 0.1 deliverable** with one canonical baseline, assumptions, variant registry, validation targets, exclusions, open questions, and proposed freeze contents.
4. **Mathematically re-check C1 derivations** before MASTER accepts a CORE Mathematical Freeze.
5. **Only after the mathematical baseline is frozen**, authorize exact replay gates for implementation/reference layers that do not require effect-selection decisions.
6. **For exploratory numerical discoveries intended as evidence**, create new preregistered validation gates with fixed model, parameters, geometry, objective, horizon, resolution, tolerances and success criteria before rerun.
7. **Treat v0.24–v0.26 as hypothesis/design generators.** Freeze a fresh active-design protocol before re-evaluating their effect sizes or optimized pulses.
8. **Continue beyond v0.26 only after MASTER has integrated recovered results and explicitly opened the next scientific branch.**

No wholesale merge of `core/theory-v0.1` is recommended.

## 13. Items that must be freshly preregistered / rerun

If MASTER wishes to use them as frozen scientific evidence, at minimum:

- v0.6–v0.15 numerical bifurcation locations, global-object classifications, hysteresis/dynamic-skip effect claims;
- selected reference parameter points used downstream as scientific truth;
- v0.18–v0.20 inverse-recovery performance and optimizer crossing-success claims;
- v0.21 observation-schedule optimality/performance;
- v0.22 magnitude of latent-state sloppiness and nonlinear-alias behavior;
- v0.23 optimized measurement time and reported information gains;
- v0.24 pulse family constraints, chart-margin floor, design box, objective, stored pulse and information gains;
- v0.25 second-probe design, eight-parameter identifiability and noise performance;
- v0.26 nuisance amplitudes/distributions, calibration uncertainty model, shared-parameter performance and nonlinear recovery.

For active-design reruns, preregistration must fix before effect inspection: pulse family, amplitude/time/direction bounds, event-chart margin rule, observation set/horizon, noise model, objective, optimizer/search protocol, acceptance criterion and robustness criterion.

## 14. Items retained only as legacy exploratory evidence

- deleted/superseded v0.24 aggressive pulse prototype;
- deleted/superseded simplified v0.24 active-experiment note;
- exploratory optimization/search paths whose choices were later changed in response to observed behavior;
- branch-local COMPLETE / VERIFIED / CERTIFIED labels as historical metadata;
- former next-step directives in legacy documents, including the hierarchical v0.27 direction;
- any result lacking enough source/configuration information for either mathematical audit or exact replay.

These items remain useful for provenance, hypothesis generation, regression targets and future protocol design but cannot themselves be result freezes.

## 15. Open questions

### Source/provenance

1. Exact primary-source equation mapping for all `[H]` and `[C]` claims remains to be built.
2. Which Haken reset convention should form the future project baseline, and which belongs only in the variant registry?
3. Which contemporary reformulations are mathematically equivalent versus merely compatible project extensions?

### Mathematical verification

4. Which v0.3–v0.5 claims can be promoted to PROPOSITION / LEMMA / THEOREM after independent proof audit?
5. Does the v0.26 calibration non-identifiability statement admit a clean structural theorem with explicit rank/gauge assumptions?

### Reproducibility

6. Which committed reference scripts execute unchanged in a frozen dependency environment?
7. Why does v0.26 lack the benchmark JSON/status closure pattern present through v0.25, and can exact reconstruction be performed without scientific repair?
8. Which benchmark tolerances were fixed before their generating effect was inspected?

### Governance / future work

9. Which legacy numerical results are important enough to justify expensive preregistered reruns?
10. Should v0.24–v0.26 be validated as one preregistered sequence or separated into observation, intervention and nuisance gates?
11. The hierarchical repeated-trial direction remains scientifically interesting but is not authorized until canonicalization and validation priorities are decided by MASTER.

## 16. Gate decision

# PASS

Meaning of PASS here is exactly the recovery-gate meaning: the legacy working state has been sufficiently reconstructed and classified for MASTER to make an informed canonicalization decision.

PASS does **not** mean:

- original Scope Gate 0.1 is retroactively PASS;
- v0.2–v0.26 claims are accepted;
- any benchmark is reproduced;
- any legacy result is frozen;
- the legacy branch may be merged;
- v0.27 or hierarchical experimentation may begin.

Recovered Scope-Gate material is assessed as **substantially sufficient but requiring formal/source repair** before canonical acceptance.

## 17. Proposed next MASTER decisions

CORE proposes that MASTER choose exactly one next global step from the recovery, preferably:

1. open a narrow **CORE Mathematical Scope Canonicalization Gate** that rebuilds the required Scope Gate 0.1 deliverable from C1-eligible v0.1–v0.2 material with primary-source verification; or
2. if MASTER judges the provenance repair insufficiently scoped, open a targeted source/provenance gate first.

MASTER should preserve `RB-002 CORE Legacy Recovery Input Snapshot 0.1` and keep `core/theory-v0.1` read-only as legacy recovery evidence.

No new scientific execution is recommended before MASTER makes that decision.

## 18. STOP

CORE Recovery & Canonicalization Gate 0.1 is complete.

`STOP — RETURN TO MASTER`
