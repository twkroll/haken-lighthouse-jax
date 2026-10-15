# NUM-ENG Robustness, Scaling & Differentiable Kernel Gate 0.2 — consolidated engineering return

Date: 2026-10-15
Workstream: `20 – NUM-ENG – Numerical Engineering`
Gate decision: **PASS — ENGINEERING ONLY; recommend MASTER review for Numerical Engineering Freeze 0.2**
Evidence class: **DEVELOPMENT EVIDENCE / LOCAL ENGINEERING METRICS ONLY**
Authorized development branch: `engineering/numerics-v0.1`.

## Authority, baseline and chronology

Governance: `PROJECT_GOVERNANCE.md`, `research/master/parallel_engineering_policy_v0_1.md`, MASTER Gate-0.2 prompt, RB-004, RB-019, RB-020 and current MASTER/CORE/NUM-ENG statuses.

Frozen RB-019 physical authority: `NUMENG_PULSE_AWARE_REFERENCE_V1`, from source commit `aa8b4ac234a1c1960a5829fc3d24982e8002105d`, subtree `software/numerical_engineering/reference_repair_v0_1/`. **No RB-019 physical/reference source file was edited or replaced.**

Before numerical Gate-0.2 stress execution, the finite F01–F18 (excluding F14 as a standalone integral-budget control), G01/J01 and S01–S04 matrix and acceptance tolerances were committed at:
`research/numerical_engineering/gate_0_2_frozen_stress_matrix.md`
(commit `a43314a881437bdc05352cb58f357515c5555f89`).

A *separate*, subsequent exploratory diagnostic discovered a high-level JAX batch-guard defect: a physically certified G01 event tape with all event timestamps shifted +0.02 kept the same token and was silently accepted by `guarded_batch_replay`. **This diagnostic was not added retroactively to the frozen matrix.** Its repair and negative/positive software QA were fixed before repair execution in:
`research/numerical_engineering/gate_0_2_batch_guard_diagnostic_addendum.md` (commit `780a38b53bd1864ea514a59db553dc8e132c9532`).

The software patch only strengthens high-level JAX tape authority; it does not change RB-004 equations, the physical reference or any scientific contract. The old frozen source remains accessible under RB-019. The patched code is versioned separately under `software/numerical_engineering/robustness_kernel_gate_0_2/overrides/lighthouse_dev/sparse_replay.py`, Git blob `5606c09aed4dc18202af199f3323062562606d8d`; baseline blob `f41c5529e924c15ac35d61a839ed1dd05e4a62a1`.

## A/B — predetermined physical robustness and chart certificate matrix

The 17 predeclared physical comparison cases F01–F13 and F15–F18 cover alpha 1, 30 and 1000; weak/strong, negative and structural-zero weights; delay and prespike history; valid crossings/noncrossings; near-collision and exact-collision states; horizon/initial-arrival boundaries; no-edge silent case; graph sizes 5,12,24,48 with E=2N.

**17/17 dense-vs-sparse comparisons PASS:** exact labelled signatures/tokens, identical validity classification, max event-time discrepancy `6.661338147750939e-15` and final-phase discrepancy `7.105427357601002e-15`, compared with prospectively fixed `2e-8` and `3e-8` tolerances.

13 cases are certified regular; four are correctly invalid:

| Fixture | Expected fail-closed diagnostic |
|---|---|
| F08 | `EVENT_CHART_COLLISION_NEAR` (two coincident spikes) |
| F11 | `INITIAL_ARRIVAL_CHART_BOUNDARY` |
| F12 | `HORIZON_EVENT_CHART_BOUNDARY` |
| F13 | `EVENT_BUDGET_EXCEEDED` |

F09 with two isolated nearly coincident spikes remains regular at the predetermined offset. F02 is a correctly non-crossing narrow-pulse case. F01 recovers the frozen RB-018 narrow-pulse first hit with absolute deviation `2.220446049250313e-16` from the reference target at 0.505000505363421. F14's deliberately insufficient integration segment budget raises `SEGMENT_BUDGET_EXCEEDED` (not silent partial certification).

## E — first-hit acceleration classification

The prospectively enumerated Gauss, quiet-guard, and phase-bound candidates yield **28/28 finite comparison agreements**, max event-time discrepancy `1.2434497875801753e-14`, max phase discrepancy `1.1546319456101628e-14`, all relative to the unchanged RB-019 physical authority. All emit `UNVERIFIED` rather than a physical certification.

Three additional historical accelerators were inspected *after* the frozen matrix as an explicitly exploratory engineering diagnostic, on F01/F07/F15: `cached_v08`, `v09_newton`, and `v09_bound_only` each agree on all three local runs (9/9), without changing the frozen acceptance record.

**All six acceleration paths are classified `DEVELOPMENT COMPARATOR`**, not `ENGINEERING-APPROVED WITH DOMAIN`: `cached_v08`, `v09_newton`, `v09_bound_only`, `gauss_v09`, `quiet_v010`, `phase_bound_v010`. None has its own fail-closed physical-authority fallback/certification wrapper. They may be compared, but cannot replace the RB-019 authority or supply independent chart certificates. No universal speedup claim is inferred.

## C — gradient robustness and differentiable kernel

Predetermined regular two-neuron G01 has 13 physical events, five spikes, and a certified regular physical tape.

JAX fixed-chart replay vs physical event times: max absolute discrepancy `9.592326932761353e-14`. Central finite differences use `epsilon=1e-4`, physically rerecord both sides, and require unchanged event token:

| Parameter coordinate | Max |AD − physical FD| |
|---|---:|
| structural-zero edge weight | 5.419196202893772e-10 |
| active edge delay | 3.0200619782760896e-10 |
| initial lifted phase | 1.8952128755245212e-10 |

All below the prospective `3e-5` tolerance. No chart exits in G01; chart-change controls are separately treated as INVALID, never differentiated across.

JVP/VJP dot-product identity discrepancy: `8.881784197001252e-16`. JVP vs full Jacobian discrepancy: `9.621904018033915e-16`.

Local CPU `jit` first-call/warmed timing for this *single* event chart: forward first call ~0.265 s vs three warmed calls ~0.108–0.154 ms; Jacobian first call ~1.327 s vs warmed ~2.298–2.887 ms. Compilation and execution times are explicitly separated, not compared to a fair end-to-end alternative model.

### Newly found batch guard defect and confined software repair

Before repair, `guarded_batch_replay` accepted a +0.02-shifted base event tape retaining the same token; `derivative_record_sparse` correctly rejected it. Root cause: candidate rerecords were checked but the supplied *base tape timestamps* were never independently verified.

The versioned v0.2 override introduces a **shared base-tape physical rerecord check** for both high-level derivative and batch routes, verifying physical certification, labelled token and topology, event counts/times (`<=1e-8`), spike/event coherence, initial-arrived edge mapping, finite initial alpha state equality, and final phase consistency. It rejects stale, truncated, uncertified, inconsistent-spike-list and forged-initial-state tapes. The JAX direct fixed-chart primitive remains explicitly unguarded and usable only after high-level physical validation.

Added prospective diagnostic QA: **8/8 tests PASS** (seven malformed tapes + one valid same-chart batch). **The reference integrator and RB-019 source subtree remain unchanged.** This is software hygiene, not new physics.

## D — finite sparse scaling / work counters (CPU only)

Determininistic directed graphs S01–S04 with 2N structural edges, no RNG. Source/target topology and values fixed in the preregistered stress matrix.

| N | E | Events | Alpha state sparse | Alpha state dense | Phase integrals | Adaptive quadratures | Root solves | Median physical rerecord |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 10 | 15 | 160 B | 400 B | 240 | 618 | 10 | 60.16 ms |
| 12 | 24 | 36 | 384 B | 2,304 B | 1,175 | 2,011 | 38 | 209.28 ms |
| 24 | 48 | 72 | 768 B | 9,216 B | 4,291 | 5,829 | 109 | 657.71 ms |
| 48 | 96 | 144 | 1,536 B | 36,864 B | 16,381 | 17,570 | 347 | 1,839.72 ms |

Alpha-state bytes count only two float64 `(a,q)` arrays; they exclude Python/JAX arrays, event queue, histories, and object allocation. The ratio `N²/E` is respectively 2.5, 6, 12, 24 in this fixed graph family. There are three separately rerecorded timing repetitions per N; medians are local engineering walltimes on an AMD EPYC 9V74 virtual CPU, not a general complexity law.

## F — runtime/process controls and full QA record

Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, JAX/JAXLIB 0.9.0.1, pytest 9.0.2, Linux x86_64 CPU. `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `JAX_PLATFORMS=cpu`, `JAX_ENABLE_X64=1`, `XLA_PYTHON_CLIENT_PREALLOCATE=false`. Deterministic fixtures only. No protected RNG namespaces touched.

Chronological reproduction:
1. Frozen 48-test Gate-0.2 suite before extra defect repair: `48 passed in 29.04s`, exit 0; independent repeat `48 passed in 29.35s`, exit 0.
2. Original RB-019 baseline aggregate: `194 passed in 145.05s`, exit 0.
3. Confined batch guard repair: dedicated 8 tests PASS, clean exit.
4. Patched targeted QA: `56 passed in 35.35s`, exit 0.
5. **Patched aggregate RB-019 + Gate-0.2: `250 passed in 177.30s`, clean exit 0.**

Local audit archive: `NUMENG_Gate_0_2_Engineering_Bundle.zip`, SHA-256 `762b4467dc30dbaba5ebf24dd662d66f8c87e8d12c4bb086d73d710891292fc6`; ZIP CRC PASS, contains 20 files. Full archive-content manifest SHA-256 `9062c26caa93853de43001de6d5e51c4bb1a6ba0f48a2ed0ede79755664a9e15`. Representative metric data SHA-256: stress `9f680ef144c408357c0e8c8831aeb1f1001cf37d170192ef034aab78e3f57268`, JAX `85d17777d5379a70aa0b0a2736d997e9eafedf3a0e7dce99a0f9ece055c91f46`. Original raw logs, exact harness/test sources, and environment capture remain in the archive; all four significant source/tests have matching Git blob IDs.

## Component disposition

- `ENGINEERING-APPROVED WITH DOMAIN`: unchanged RB-019 physical reference in the explicit finite stress domain; versioned high-level JAX batch/tape validation override on the tested G01 valid/invalid cases; deterministic test harness and local state-memory accounting.
- `DEVELOPMENT COMPARATOR`: all six accelerated first-hit paths; direct unguarded JAX fixed-chart primitive (only a conditional building block); old v0.9 learning/optimizer smoke and any timing extrapolation.
- `REPAIR-REQUIRED`: no *unresolved* gate acceptance blocker after the confined batch-guard repair; the initial stale-tape bug remains documented in Git history/addendum for future regression.
- `REJECTED`: promotion of unverified accelerated tapes as independently certified physical authority; use of token equality alone as evidence of timestamps/complete base chart; any AI/confirmatory/scaling or manuscript claims inferred from local tests.

## Limitations and recommendation

Finite numerical quality controls under RB-019 do not constitute formal interval-arithmetic certification, global first-hit correctness or a universal chart-validity guarantee. No GPU or independent hardware portability suite was run; end-to-end training speed/AI performance is untested. The stronger batch validation adds a physical rerecord of the base tape and may increase batch overhead; this gate does **not** claim that this change is a speedup. All 250 green QA tests are local/software-only.

**Gate 0.2 recommendation: PASS — ENGINEERING ONLY.** MASTER may review a bounded `Numerical Engineering Freeze 0.2` incorporating the new high-level batch-guard overlay, finite robustness suite, stress matrix and explicit comparator classifications. Do not replace RB-019 physical authority, merge executable code to main, or authorize APP-3/TR-27C by implication.

## STOP

**RETURN TO MASTER.** RB-015 remains immutable SCIENTIFIC FAIL; RB-020 is a frozen contract but TR-27C-01…07 remain UNEVALUATED; the reserved confirmatory `2711xxx` streams remain UNGENERATED / UNEVALUATED. APP-3 is PROTECTED/WAIT and parked. No scientific effect search, training, confirmatory run, v0.28 execution, novelty positioning or manuscript claim has been performed.
