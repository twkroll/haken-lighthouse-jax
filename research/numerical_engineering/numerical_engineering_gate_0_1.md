# NUM-ENG Numerical Engineering Gate 0.1 — consolidated return

Date: 2026-10-15
Workstream: 20 – NUM-ENG – Numerical Engineering
Gate decision: **CONDITIONAL / BLOCKED — NOT PASS**
Evidence status: **DEVELOPMENT EVIDENCE ONLY**
Authorized branch: `engineering/numerics-v0.1`

## Authorities and intake

This execution follows `research/master/prompts/numerical_engineering_gate_0_1.md`, `research/master/parallel_engineering_policy_v0_1.md`, RB-017, and RB-004/RB-006/RB-009 semantic references. Current project status is MASTER v2.4. Git before return: `aeacf0f40c21799225e7177139de56928fa7a3da`. The older `5c02ccd` appears *inside the archived software package* and is not the current project HEAD.

Exactly frozen RB-017 original input: `Lighthouse_Numerik_Starter_v0_10.zip`, SHA-256 `e21202362fc9ead75a3e5d92736d38002eb75d4e4ec5b4dd1cfb3c0a7c88db53`. ZIP CRC integrity PASS; 137 archived regular files, 47 Python files, 11 pytest modules. Archived contents were extracted into an isolated working directory; original ZIP and files were not modified.

The original 33-line `FILE_SHA256_MANIFEST.txt` had 31 matching checksums and **two mismatches**:
- `README.md`: actual `735da0e6fb0fa2bd00070921ed06c9b870b0321a45cf33c23fb4a21c4e757c73`;
- `lighthouse_dev/sparse_replay.py`: actual `641e4e9e289820d93cc9dbfe777814348f289b1a10ceccd963c3ab1cd86cc826`.

Both old entries are preserved unmodified in the RB-017 archive. A new **complete 137-file** original-byte hash/size/CRC32 manifest has been generated as `RB017_ORIGINAL_COMPLETE_SHA256.tsv` (SHA-256 `52b429d3c4784341b8615228896756295ad8a901317256d385d82b9e3c54268a`) alongside the local audit bundle. No retroactive modification of the RB-017 intake is claimed.

## Environment

Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0; JAX/JAXLIB 0.9.0.1; pytest 9.0.2; Matplotlib 3.10.8; Linux x86_64 CPU backend. Exact environment and CPU metadata are captured separately.

Reproduction controls: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `XLA_PYTHON_CLIENT_PREALLOCATE=false`, `JAX_PLATFORMS=cpu`.

## Complete reproduction

**All 180 reported cases are independently reproduced.** All eleven supplied test modules independently returned PASS with clean process exit code 0:

| Module | Passed | Exit |
|---|---:|---:|
| test_chart_guard_v05 | 13 | 0 |
| test_fast_first_hit_v08 | 20 | 0 |
| test_irregular_phase_bound_v010 | 36 | 0 |
| test_numerical_and_learning_v09 | 45 | 0 |
| test_profiling_v07 | 10 | 0 |
| test_rechart_v06 | 15 | 0 |
| test_reference | 6 | 0 |
| test_replay | 4 | 0 |
| test_sparse_v04 | 14 | 0 |
| test_structural_graph_v03 | 8 | 0 |
| test_z_history_multineuron | 9 | 0 |
| **TOTAL** | **180** | **all 0** |

A separate single-process aggregate run also produced **180 passed in 72.90s, exit 0**. The earlier aggregate teardown/hang phenomenon was not reproduced under this CPU/plugin isolation. Its original root cause is not established, and an unconditional portability claim is not authorized. Raw per-module and aggregate logs are retained in the local audit bundle.

## Mathematical/semantic audit and decisive new negative control

The source uses lifted phases with no physical reset, first-hitting spike convention, alpha-state propagation, fixed edge delays, labelled event tape, prespike histories, zero-weight structural edges, and JAX fixed-chart replay. Existing test fixtures cover regular-chart comparisons and negative controls, but they do not prove universal first-hit correctness.

**One original physical rerecord path silently misses a true spike.**

Deterministic one-cell fixture: `alpha=1000, r=1, h=0.1, weight=4, delay=1.5`, historical emission `-1` (arrival `t=0.5`), initial phase `2*pi - 0.005`, horizon `20`.

- `physical_rerecord_sparse`: only arrival at `t=0.5`, **0 spikes**, `chart_valid=True`, no warning.
- `physical_rerecord_gauss` and `physical_rerecord_quiet`: exactly 1 first hit at `0.5050005053634209`, then delayed arrival at `2.005000505363421`.
- Independently segmented SciPy quadrature plus a root solve gives first hit `0.505000505363421`, matching the pulse-aware solver to `1.11e-16`.
- `derivative_record_sparse` **accepts the incomplete reference tape** and returns an empty spike vector. Thus nominal physical rerecording does not always fail closed when the underlying reference quadrature misses a narrow pulse.

The discrepancy violates the engineering-gate criterion that accepted first-hit charts and their JAX guards be reliably fail-closed. It is an engineering defect, **not** a change to the frozen RB-004 model or a new scientific result. The audit provides a deterministic executable negative-control script; no RNG is used.

## QA matrix and classification

The 180 green tests support, on their predetermined cases: event/token equivalence; dense-vs-sparse comparison; regular-chart JAX Jacobian against physical finite differences; collision/history/horizon negative controls; first-hit acceleration comparisons; quiet-guard controls; deterministic profiler/work counters; O(E) alpha-state storage accounting; and isolated/aggregate test process controls. The new narrow-pulse negative control shows these cases do **not** suffice to certify the raw physical reference.

Component disposition (one classification per scope):
- **ENGINEERING-APPROVED:** exact source identity and regenerated complete original-byte manifest; reproduced test/fixture infrastructure; explicit zero-weight structural-coordinate representation in tested cases; deterministic environment/log protocol. Approval is strictly scoped, not a production numerical freeze.
- **REPAIR-REQUIRED:** obsolete/inaccurate original SHA manifest as a checksum authority; unsegmented first-hit quadrature in reference/sparse physical rerecorders; chart guards/JAX derivative wrappers that trust this incomplete rerecord without an independent physical-first-hit check.
- **DEFERRED:** alternate pulse-aware integrators as global production default until reference-contract QA closure; performance/scaling speedup generalization; fixed-chart JAX support outside validated regular charts; synthetic one-weight optimizer smoke as scientific evidence; global applicability of optional bounds.
- **REJECTED:** claiming the original 33-line manifest is complete/accurate; promoting local speedup or learning-smoke data to confirmatory APP-3 evidence.

## Integration disposition and next repair gate

The local audit bundle records complete SHA-256 inventory, test matrix, exact environment, raw test logs, independent counterexample and detailed component inventory. The old package remains untouched.

**Only this gate report and NUM-ENG STATUS are written to the authorized development branch in this return. No executable software is integrated as production-authoritative while the failed first-hit reference remains unresolved.** This is a conditional engineering audit, not a source integration PASS.

Proposed MASTER-authorized repair gate: freeze pulse-aware physical reference requirements and explicit quadrature/first-hit tolerances, make chart guards reject incomplete tapes, add the deterministic alpha=1000 regression and relevant JAX negative controls, rerun the full 180-case suite plus new cases, publish a complete repaired-source manifest and integrate reviewed sources into the development branch. Do not merge to main or reclassify old outcomes.

## STOP

Decision: **CONDITIONAL / BLOCKED. No Numerical Engineering Freeze 0.1 is recommended yet. Return to MASTER for an explicit repair-gate authorization.**

All numerical, timing, scaling, optimizer and learning-smoke outputs remain **DEVELOPMENT EVIDENCE**. RB-015 remains immutable SCIENTIFIC FAIL; no `2711xxx` RNG generation/evaluation, no v0.27c confirmatory execution, no APP-3 training or benchmark, no v0.28 science, novelty positioning, manuscript claim, or edit to RB-004–RB-017.

**STOP — RETURN TO MASTER.**
