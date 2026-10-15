# NUM-ENG Reference/Rerecord Repair & Controlled Integration Gate 0.1

Date: 2026-10-15
Workstream: `20 – NUM-ENG – Numerical Engineering`
Authorized branch: `engineering/numerics-v0.1`
Gate decision: **PASS — ENGINEERING ONLY; RETURN TO MASTER**
Scientific status: **DEVELOPMENT EVIDENCE ONLY**.

## Authority and frozen pre-repair contract

Executed only under `research/master/prompts/numerical_engineering_reference_rerecord_repair_integration_gate_0_1.md`, Parallel Engineering Policy 0.1, RB-004/RB-006/RB-009 mathematical and validation premises, RB-017 intake and RB-018 audit. The engineering action does not alter any frozen scientific equation, scientific threshold or result.

Exactly frozen RB-017 intake: `Lighthouse_Numerik_Starter_v0_10.zip`, SHA-256 `e21202362fc9ead75a3e5d92736d38002eb75d4e4ec5b4dd1cfb3c0a7c88db53`. Its 137 archived regular files and defective original 33-entry manifest remain unmodified.

Before obtaining repaired-output test results, the local `PRE_REPAIR_CONTRACT_0_1.md` was written and SHA-256 frozen as `a0a7742b53159a204e815f72d7d7e53aff293825e5901fcd684b6e98f01188d4`. It prospectively fixes:

1. lifted phase and transverse first-hitting; no physical phase reset;
2. alpha-pulse-aware segmentation using the exact inter-event input shape, local extrema, threshold crossings, and an analytic tail bound;
3. QUADPACK `epsabs=2e-13`, `epsrel=2e-12`, estimated integral error sum <= `max(2e-11, 2e-11*dt)`, tail bound <= `2e-13`;
4. Brent root tolerance `xtol=1e-12`, `rtol=9e-16`, endpoint phase allowance `1e-12`;
5. source-labelled arrival/spike ordering and `1e-8` collision tolerance;
6. at most 512 quadrature segments per integral and 2000 event-loop iterations by default;
7. explicit `PHYSICAL_FIRST_HIT_UNCERTIFIED` invalid status on numerical failure, rather than accepting a partial physical tape;
8. physical certification and rerecorded labelled-token/time guards before JAX differentiation;
9. finite fixture and numeric tolerances: <= `2e-9` for the RB-018 event, <= `2e-8` event-time equivalence, <= `3e-8` final phase, and <= `3e-5` absolute error for the selected regular-chart AD/FD check.

The contract expressly does **not** claim mathematically rigorous interval arithmetic or a universal first-hit proof.

## Repair and authoritative semantics

New `lighthouse_dev/physical_first_hit_repair.py` integrates the RB-004 alpha-state response on arrival-separated intervals. It splits at the pulse's scale, physical input turning point and input-threshold roots, subtracts the exact baseline velocity and bounds the decaying tail analytically. Its finite QUADPACK error/budget checks fail closed. The repaired dense and sparse references share this numerical integration and keep the frozen first-hitting/no-reset and edge-delay semantics.

The `Record`/`SparseRecord` high-level physical authority now labels accepted regular tapes `NUMENG_PULSE_AWARE_REFERENCE_V1`; an invalid or unresolved reference tape is never accepted for high-level differentiation. The sparse/dense derivative wrappers check physical rerecording, certification, complete event signatures and event times before AD. The batch wrapper validates each proposed physical tape. Direct unguarded fixed-chart functions remain **conditional primitives**, not standalone physical certificates.

The conditional JAX quadrature retains the original 64-point rule for ordinary alpha values and clusters quadrature nodes near the beginning of segments for `alpha>=100`. This improves the narrow-pulse replay and is still verified against the repaired physical reference. The original v0.9 Gauss public integrator is routed to the corrected physical routine: no previous speedup timing is transported as an engineering claim. Profiler hooks count QUADPACK calls from the new module.

## Reproduction and RRI matrix

Captured controls: Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0; JAX/JAXLIB 0.9.0.1; pytest 9.0.2; Linux x86_64 CPU; `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `JAX_PLATFORMS=cpu`, `XLA_PYTHON_CLIENT_PREALLOCATE=false`. Exact environment details and raw logs are committed beneath the engineering source path.

The **eleven original RB-017 modules** were rerun separately with PASS and clean exit code 0:

| Module | Cases | Exit |
|---|---:|---:|
| test_chart_guard_v05.py | 13 | 0 |
| test_fast_first_hit_v08.py | 20 | 0 |
| test_irregular_phase_bound_v010.py | 36 | 0 |
| test_numerical_and_learning_v09.py | 45 | 0 |
| test_profiling_v07.py | 10 | 0 |
| test_rechart_v06.py | 15 | 0 |
| test_reference.py | 6 | 0 |
| test_replay.py | 4 | 0 |
| test_sparse_v04.py | 14 | 0 |
| test_structural_graph_v03.py | 8 | 0 |
| test_z_history_multineuron.py | 9 | 0 |
| **Original subtotal** | **180** | **all 0** |

New `tests/test_rri_repair_v01.py` contains **14/14 PASS, clean exit**, including the eight mandatory repair topics:

- **RRI-01 PASS:** frozen RB-018 one-neuron pulse (`alpha=1000,r=1,h=0.1,W=4,delay=1.5,history=-1,theta0=2*pi-0.005,H=20`) now yields one regular spike at `0.5050005053634212`, then its scheduled delayed arrival; independent segmented SciPy agrees within the frozen `2e-9` criterion; no target-time hard-coding.
- **RRI-02 PASS:** original 180 tests, all module exits clean.
- **RRI-03 PASS:** combined `pytest -q tests` reports `194 passed in 141.46s`, clean exit `0`. The previously observed aggregate shutdown issue was not reproduced under this isolated environment; no general portability guarantee is made.
- **RRI-04 PASS (finite suite):** dense/sparse agreement for quiet, prespike history, structural zero, alpha 1/30/1000 and multi-neuron fixtures at frozen event/phase tolerances.
- **RRI-05 PASS:** deterministic unresolved integration, event-budget exhaustion, boundary and simultaneous-spike collision controls result in explicit invalid states.
- **RRI-06 PASS:** incomplete, stale or uncertified input tapes rejected; validated ordinary and narrow regular tapes accepted by guarded replay; finite-difference/AD limited to regular charts.
- **RRI-07 PASS:** dense/sparse first-hit equivalence with a structurally present zero-weight connection.
- **RRI-08 PASS on fixed fixtures, but acceleration status QUALIFIED:** two initial accelerated variants included in the new pytest suite. An additional deterministic check of all six legacy schedulers on the frozen narrow-pulse and ordinary two-cell cases returned 12/12 labelled-event/time comparisons within `2e-8`. All their outputs remain tagged `UNVERIFIED`, so high-level JAX wrappers will not silently accept them as independently certified physical tapes. They remain non-authoritative development comparators, not production physical references.

All post-repair behavior, timing, optimizer and learning-smoke output remains DEVELOPMENT EVIDENCE.

## Provenance / controlled branch integration

Exact source integration commit: `aa8b4ac234a1c1960a5829fc3d24982e8002105d`.

Integrated isolated subtree:

`software/numerical_engineering/reference_repair_v0_1/`

- 19 Python implementation modules under `lighthouse_dev/` (including reference and conditional legacy comparators);
- 12 pytest modules under `tests/` (11 legacy + 1 new);
- 23 documentation/provenance/log files: frozen pre-repair contract, README, changelog, QA matrix, complete original/repaired SHA256 inventories, the original defective manifest preserved unchanged, exact environment identity, all 11 module logs and the combined test log, RRI output.

The exact 139-file repaired working tree comprises the original 137-file RB-017 intake plus two new files: the pulse-aware physical integrator and the 14-case test module. Nine files are added or changed; other intake bytes remain untouched. Complete repaired working-tree SHA-256 inventory SHA-256:

`7dd31eb6add44c719c749421d6261a9df050076b16d44e2030da728336bce71d`.

The 137-entry original-byte manifest from the prior audit is preserved, alongside the defective original 33-entry manifest for audit history. The four inspected key Git source files and the Git manifest were byte-compared against the local tested transfer and matched exactly.

All executable source was integrated **only on** `engineering/numerics-v0.1`. `main`, CORE artifacts, scientific freezes and master decisions were not modified.

## Component disposition

- **ENGINEERING-APPROVED (scoped, finite QA):** repaired sparse/dense physical authority; analytic alpha-state propagation; pulse-window segmentation and bounded/error-controlled adaptive quadrature; chart/tape certification guard in high-level derivative APIs; regular-chart JAX conditional replay under physical residual checks; structural-zero support; original test infrastructure and new RRI fixtures; profiling count fix; complete provenance/manifest/test logs.
- **ENGINEERING-APPROVED AS DEV COMPARATORS ONLY:** retained historical accelerated schedulers, with physical certificate `UNVERIFIED` and no independent production-authority status.
- **DEFERRED:** general correctness outside the explicit numerical budget and fixture envelope; formally rigorous interval enclosures; unconditional direct JAX fixed-chart calls; platform-independent teardown guarantees; performance/scaling/speedup generalizations; scientific interpretation of the pre-existing single-weight learning smoke.
- **REJECTED:** using the old 33-entry manifest as a complete hash authority; calling historic approximate Gauss timings a validated speedup after the repair; promoting local optimizer/AI-smoke data to confirmatory evidence.
- **REPAIR-REQUIRED:** no unresolved defect *within the finitely specified RRI-01..08 engineering acceptance suite*; additional production-hardening is a future scope, not silently declared complete.

## Gate decision and requested MASTER action

**PASS — ENGINEERING ONLY.** Under the pre-repair numerical QA contract, finite repair criteria RRI-01 through RRI-08 are met, and the reviewed development source with complete provenance/tests is on the authorized branch.

Recommendation: MASTER may review and establish a *Numerical Engineering Freeze 0.1* as a narrowly scoped stable **engineering baseline**, with the approved/deferred distinction retained and an explicit future hardening/APP-3 preregistration boundary. This gate itself does NOT freeze or promote any scientific effect or AI-performance claim.

RB-015 remains immutable `SCIENTIFIC FAIL`; protected `2711xxx` RNG objects remain untouched; no v0.27c confirmatory science, APP-3 training/benchmark, v0.28 work, novelty positioning, manuscript claim or executable merge to `main`.

**STOP — RETURN TO MASTER.**
