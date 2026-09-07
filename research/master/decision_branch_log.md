# Decision & Branch Log

## DEC-001
Governance prompt adopted as project operating procedure.
Status: STABLE
Date: 2026-09-04

## DEC-002
Git repository `twkroll/haken-lighthouse-jax` is the single source of truth for canonical project state, prompts, freezes, and results.
Status: STABLE
Date: 2026-09-04

## DEC-003
Initial workstream structure authorized:
- 00 MASTER
- 10 CORE
- 50 APP-1 Computational Neuroscience
- 60 APP-2 Neuromorphic Computing
- 70 APP-3 Differentiable Inference / Temporal Learning
- 80 LIT
- 90 MANUSCRIPT
Status: STABLE
Date: 2026-09-04

## DEC-004
Application workstreams are created only as PROTECTED / WAIT. They may not execute until MASTER opens an explicit gate.
Status: FROZEN
Date: 2026-09-04

## DEC-005
The first scientific task is `CORE Mathematical Scope Gate 0.1`. No implementation, parameter tuning, benchmarking, learning experiment, or application execution precedes this gate.
Status: ACTIVE
Date: 2026-09-04

## DEC-006
MASTER Status Audit 0.2 confirms that `CORE Mathematical Scope Gate 0.1` has not yet been executed in the Git single source of truth. `research/core/STATUS.md` remains READY and no gate result file exists. The later README-only commit `948dedbc5294fbe864b940060ee6b2053020347f` was inspected and does not constitute scientific execution or a freeze violation. No application, literature, or manuscript branch is authorized to proceed.
Status: STABLE
Date: 2026-09-04

## DEC-007
MASTER PDF Snapshot v0.1 was generated from canonical project status v0.2 and the current branch-status files. Its canonical LaTeX source is stored at `research/master/reports/haken_lighthouse_jax_master_report_v0_1.tex`, with `research/master/reports/CURRENT.md` pointing to the current version. The report introduces no new scientific result and leaves all scientific freeze states unchanged.
Status: STABLE
Date: 2026-09-04

## DEC-008
MASTER Status Audit 0.3 confirms that the CORE gate still has not been executed: `research/core/STATUS.md` remains READY and `research/core/mathematical_scope_gate_0_1.md` is absent. Commits since Status Audit 0.2 are restricted to the MASTER report, report pointer, decision log, and MASTER status bookkeeping. No scientific freeze violation, unauthorized branch execution, post-hoc retuning, or application/literature/manuscript execution is detected. The single authorized next scientific action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-009
MASTER PDF Snapshot v0.2 was generated from canonical project status v0.3 and Decision Log through DEC-008. Canonical report source is stored at `research/master/reports/haken_lighthouse_jax_master_report_v0_2.md`; `research/master/reports/CURRENT.md` points to v0.2. The versioned and current PDFs are byte-identical with SHA-256 `556c401d6014a7c4bfd1bcee509183a3fe3cbaa8c558af108d6b109534402a20` and were visually verified after rendering 9 A4 pages. The report is administrative only and leaves the scientific freeze state unchanged.
Status: STABLE
Date: 2026-09-04

## DEC-010
MASTER Status Audit 0.4 confirms again that `CORE Mathematical Scope Gate 0.1` is still unexecuted: `research/core/STATUS.md` remains READY and `research/core/mathematical_scope_gate_0_1.md` is absent. APP-1, APP-2, and APP-3 remain PROTECTED / WAIT; LIT and MANUSCRIPT remain WAIT. No commits occurred after the MASTER report v0.2 bookkeeping commit before this audit. No freeze violation, unauthorized branching, retuning, result inspection, or scientific execution is detected. The single authorized next scientific action remains the existing CORE gate.
Status: STABLE
Date: 2026-09-04

## DEC-011
MASTER Status Audit 0.5 reconfirms that `CORE Mathematical Scope Gate 0.1` remains unexecuted. `research/core/STATUS.md` is still READY and `research/core/mathematical_scope_gate_0_1.md` is absent. Direct branch checks confirm APP-1, APP-2 and APP-3 remain PROTECTED / WAIT; LIT and MANUSCRIPT remain WAIT. No repository commits occurred after Status Audit 0.4 before this audit. No freeze violation, unauthorized branching, effect inspection, retuning, scientific execution, or result manipulation is detected. The single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-012
MASTER generated two communication-only PDF briefings at the user's request: a current pre-manuscript snapshot and a detailed colleague-facing technical derivation note. Both are explicitly NON-CANONICAL / PRE-CORE and are recorded under `research/master/briefings/README.md` with hashes and page counts. The detailed note uses source-derived Lighthouse equations and transparent elementary derivations, but it does not constitute a CORE Mathematical Freeze, scientific execution, a MANUSCRIPT Claim Freeze, or a novelty claim. `research/manuscript/STATUS.md` remains WAIT and the single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-013
MASTER Status Audit 0.6 confirms that the communication-only briefings created under DEC-012 did not alter any scientific freeze or branch authorization. `research/core/STATUS.md` remains READY and `research/core/mathematical_scope_gate_0_1.md` is still absent. APP-1, APP-2 and APP-3 remain PROTECTED / WAIT; LIT and MANUSCRIPT remain WAIT. The only commits since Status Audit 0.5 before this audit are `c25b2e5631f206096fc51730498a3c956f6d73de` and `b3c4a5bbea68a936ac6d20f83cbd5a4257521c9d`, both limited to documenting the non-canonical briefings. No effect inspection, retuning, unauthorized scientific execution, manuscript claim freeze, or novelty positioning is detected. The single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-014
MASTER Status Audit 0.7 confirms no change in scientific state since Status Audit 0.6. No repository commits occurred between the audit-0.6 status commit `3ca67f2782bf45b271204774dbe5e8d209b4eb50` and the start of this audit. `research/core/STATUS.md` remains READY and `research/core/mathematical_scope_gate_0_1.md` remains absent. All application, literature, and manuscript authorizations therefore remain unchanged. No freeze violation, unauthorized branching, effect inspection, retuning, novelty positioning, or scientific execution is detected. The single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-015
MASTER Status Audit 0.8 confirms no scientific or branch-state change since Status Audit 0.7. No repository commits occurred after the audit-0.7 status commit `39ebd7c4186d893a816efea7a68ee3cae4feba2c` before this audit. Direct checks confirm `research/core/STATUS.md` remains READY, `research/core/mathematical_scope_gate_0_1.md` is absent, APP-1/APP-2/APP-3 remain PROTECTED / WAIT, and LIT plus MANUSCRIPT remain WAIT. No freeze violation, unauthorized branching, effect inspection, retuning, novelty positioning, manuscript claim freeze, or scientific execution is detected. The single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-016
MASTER Status Audit 0.9 confirms no scientific or branch-state change since Status Audit 0.8. The repository HEAD at the start of this audit was the audit-0.8 status commit `f9c27449fdee3fd5823e66658f2439939d643825`; no commits occurred after it before this audit. Direct checks confirm `research/core/STATUS.md` remains READY, `research/core/mathematical_scope_gate_0_1.md` is absent, APP-1/APP-2/APP-3 remain PROTECTED / WAIT, and LIT plus MANUSCRIPT remain WAIT. No freeze violation, unauthorized branching, effect inspection, retuning, novelty positioning, manuscript claim freeze, or scientific execution is detected. The single authorized scientific next action remains `CORE Mathematical Scope Gate 0.1`.
Status: STABLE
Date: 2026-09-04

## DEC-017
MASTER repository-wide recovery audit discovers the previously unintegrated branch `core/theory-v0.1`. At discovery its head is `287eae8a86560b78ed94f30a2786243714c33ac0` with message `CORE v0.26: document trial nuisance and calibration theory`; its merge base with `main` is `948dedbc5294fbe864b940060ee6b2053020347f`, and it is 133 commits ahead / 34 commits behind `main`. The branch contains extensive CORE work through v0.26, including mathematical analysis, numerical continuation/bifurcation work, inference, active experiment design, JAX/reference code, and benchmarks. However, on that same branch `research/core/STATUS.md` still says `CORE Mathematical Scope Gate 0.1 / READY`, while its MASTER status still waits for that gate and forbids downstream implementation/scientific execution. Therefore the branch cannot be silently merged or treated as a canonical result lineage. Previous audit statements of 'no unauthorized scientific branch execution detected' are henceforth understood as conclusions about the audited canonical `main` state, not a complete repository-wide historical finding. MASTER freezes the exact legacy head only as administrative recovery input in `research/master/core_legacy_recovery_snapshot_0_1.md`, establishes RB-002, PARKS direct execution of the original Scope Gate pending recovery, and authorizes `CORE Recovery & Canonicalization Gate 0.1`. Recovery may inventory, source-audit, classify, and exactly replay committed artifacts without tuning or new scientific design. No v0.27, direct merge, legacy continuation, application execution, novelty claim, or scientific freeze is authorized until recovery returns to MASTER.
Status: STABLE
Date: 2026-09-07

## DEC-018
`CORE Recovery & Canonicalization Gate 0.1` returns PASS at `research/core/recovery_canonicalization_gate_0_1.md`. PASS means the legacy branch through v0.26 has been sufficiently reconstructed and classified for MASTER decision-making; it does not validate, reproduce, promote, merge, or freeze any legacy scientific result. The recovery establishes that the original Scope Gate was substantially satisfied in mathematical content by recovered v0.1–v0.2 foundational material but was not completed as a governed gate. Required repairs are precise primary-source/equation mapping, one explicit baseline assumptions table, a formal variant registry, explicit exclusions, a formal gate decision/proposed freeze package, and independent checks of C1-eligible derivations. MASTER accepts the recovery classification as stable administrative/audit evidence and establishes RB-003. MASTER does not authorize replay, active-design rerun, v0.27, or downstream legacy continuation at this point. The single next scientific action is `CORE Mathematical Scope Canonicalization Gate 0.1`, which must reconstruct the missing governed Scope Gate deliverable from C1-eligible v0.1–v0.2 material with primary-source verification and independent mathematical checking. v0.3–v0.26 remain recovery evidence only.
Status: STABLE
Date: 2026-09-07

## DEC-019
`CORE Mathematical Scope Canonicalization Gate 0.1` returns PASS at `research/core/mathematical_scope_canonicalization_gate_0_1.md`. MASTER reviews the source map, baseline equations C1–C11, assumptions A1–A13, formal variant registry, exclusions and independently re-derived elementary identities D1–D18 and finds no blocker to a narrow mathematical baseline freeze. MASTER therefore establishes `CORE Mathematical Freeze 0.1` in `research/core/mathematical_freeze_0_1.md` and rollback point RB-004. RB-004 freezes baseline definitions and elementary C1 derivations only; no v0.3–v0.26 numerical, implementation, inference or active-design claim is promoted. Inspection of the frozen legacy tree confirms that v0.2 has `docs/core/derivations_v0.2.md` and `docs/core/benchmark_contract_v0.2.md` but no standalone v0.2 reference script or benchmark JSON. MASTER therefore does not authorize a misleading exact replay. The single next scientific action is `CORE v0.2 Benchmark Contract Canonicalization Gate 0.1`, which must pre-specify benchmark inputs, observables, tolerances and pass/fail rules before any execution.
Status: STABLE
Date: 2026-09-07

## DEC-020
`CORE v0.2 Benchmark Contract Canonicalization Gate 0.1` returns PASS at `research/core/v0_2_benchmark_contract_canonicalization_gate_0_1.md`. MASTER reviews BC01–BC10 and finds the contract suitable for pre-execution freeze: all benchmark membership, fixed parameter/test sets, histories, observables, references, horizons, grids/resolutions, permitted method classes, quadrature stopping tolerances, acceptance tolerances, admissibility/transversality rules, negative controls, and pass/fail criteria are specified before execution. Symbolic and numerical checks are explicitly separated; legacy B5–B7 and B9–B10 plus open-ended sweeps and implementation-specific tolerances remain deferred. No benchmark has been executed and PASS of the contract gate is not a benchmark PASS. MASTER establishes `CORE Benchmark Contract Freeze 0.1` in `research/core/benchmark_contract_freeze_0_1.md` as RB-005. The single next scientific action is `CORE v0.2 Benchmark Execution Gate 0.1`, which must execute BC01–BC10 exactly under RB-005 without changing scientific specification after observing results. Any scientifically valid failure must be preserved and returned to MASTER.
Status: STABLE
Date: 2026-09-07

## DEC-021
`CORE v0.2 Benchmark Execution Gate 0.1` returns PASS at `research/core/v0_2_benchmark_execution_gate_0_1.md`. Every required BC01–BC10 benchmark, fixed subcase and required negative control passes under RB-005. No scientifically valid benchmark failure occurs. The execution record contains one documented software-plumbing correction in the first-hit harness: adaptive quadrature embedded directly in an endpoint-bracketed root solver was replaced by the exact primitive of the already frozen periodic alpha comb. MASTER accepts the correction because no model, parameter, finite case, history, horizon, grid, method class, observable, reference, quadrature tolerance, acceptance tolerance, pass/fail rule or negative control changed, and the aborted output was not used as evidence. MASTER establishes `CORE v0.2 Benchmark Result Freeze 0.1` / RB-006. Recovery classifies v0.3–v0.5 theory contracts C1/C2 by claim and requires dedicated verification. Therefore the single next scientific action is `CORE v0.3 Continuation Theory Canonicalization Gate 0.1`, restricted to mathematical claim audit/re-derivation of normalized phase-locked coordinates, gauge structure, branch equations/Jacobians, period derivatives and singularity taxonomy. No numerical continuation, B11+ execution, bifurcation search, v0.4+ science, implementation continuation or active experiment design is authorized.
Status: STABLE
Date: 2026-09-07

## DEC-022
`CORE v0.3 Continuation Theory Canonicalization Gate 0.1` returns PASS at `research/core/v0_3_continuation_theory_canonicalization_gate_0_1.md`. MASTER accepts the independently re-derived normalized phase-coordinate map, fixed-domain branch operator, phase Jacobian, fixed-physical-delay period derivative, parameter derivative, gauge structure, pseudo-arclength algebra as a method definition, event/admissibility qualifications, existence-vs-stability-vs-hybrid taxonomy, and exchange-symmetric two-cell block structure with corrected negative antisymmetric coefficient `B`. MASTER also accepts the gate's two explicit repairs to legacy v0.3: threshold contact is not automatically nonsmooth for the frozen smooth baseline response C2, and alpha-arrival collisions are not automatically existence-Jacobian singularities. Conditional fold theory is frozen only under stated local `C^2` assumptions; unconditional higher-derivative/pitchfork applicability is not promoted. MASTER establishes `CORE v0.3 Continuation Theory Freeze 0.1` / RB-007. No numerical continuation, actual Lighthouse fold/pitchfork result, B11–B22 output, v0.4 stability result or downstream effect is promoted. The single next scientific action is `CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1`, which must pre-specify finite cases, derivative conventions, chart conditions, tolerances and PASS/FAIL rules before any v0.3 validation execution.
Status: STABLE
Date: 2026-09-07

## DEC-023
`CORE v0.3 Continuation Validation Contract Canonicalization Gate 0.1` returns PASS at `research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`. MASTER accepts the finite pre-execution V3C01–V3C09 contract because model choices, common reference state R0, parameters, derivative conventions, fixed five-point derivative steps, chart margins, arrival-aware integration, solver steps, tolerances, negative controls, PASS/FAIL/INVALID rules, software-plumbing audit rule and deferred boundary are all fixed before validation execution. Legacy B11–B22 are repaired into a narrower canonical suite rather than imported wholesale; no Lighthouse critical point or v0.4 stability object is selected or executed. MASTER establishes `CORE v0.3 Continuation Validation Contract Freeze 0.1` / RB-008. At freeze time V3C01–V3C09 are UNEVALUATED. The single next scientific action is `CORE v0.3 Continuation Validation Execution Gate 0.1`, which must execute V3C01–V3C09 exactly under RB-008 and preserve any scientifically valid failure. No Lighthouse continuation search, fold/pitchfork search, v0.4+ recovery science, production implementation continuation or active experiment design is authorized.
Status: STABLE
Date: 2026-09-07

## DEC-024
`CORE v0.3 Continuation Validation Execution Gate 0.1` returns PASS in the corrected governed record `research/core/v0_3_continuation_validation_execution_gate_0_1.md`: V3C01–V3C09 all pass under RB-008, with no scientifically valid failure and no execution blocker. MASTER accepts the post-write V3C04 correction as a clerical/result-serialization defect under the already frozen RB-008 software-plumbing rule: the affected V3C04 family was rerun from the beginning under the unchanged contract, remained PASS, and the incorrect preliminary table is preserved in Git history but invalidated as evidence. No scientific model, parameter, reference state, derivative step, chart margin, solver step, tolerance, benchmark membership, negative control or success rule changed. MASTER establishes `CORE v0.3 Continuation Validation Result Freeze 0.1` / RB-009. RB-009 validates only the deterministic v0.3 C2 layer and promotes no actual Lighthouse continuation branch, fold/pitchfork, Floquet multiplier, stability boundary or downstream effect. Recovery classifies v0.3–v0.5 theory contracts C1/C2 by claim; legacy v0.4 contains spike-time Floquet and symmetry mathematics plus a separate B23–B40 benchmark contract. The single next scientific action is therefore `CORE v0.4 Floquet Theory Canonicalization Gate 0.1`, restricted to source/claim audit and independent derivation of the spike-time recurrence, nonlinear characteristic operator, neutral mode, weighted alpha derivative comb, multiplier conventions and symmetry/Fourier/cluster reductions. No B23–B40 execution, actual Lighthouse multiplier/root search, stability-boundary search, v0.5+ science, production implementation continuation or active experiment design is authorized.
Status: STABLE
Date: 2026-09-07

## DEC-025
`CORE v0.4 Floquet Theory Canonicalization Gate 0.1` returns PASS at `research/core/v0_4_floquet_theory_canonicalization_gate_0_1.md`. MASTER accepts the narrow independently re-derived spike-time Floquet/symmetry layer, including the regular spike-time recurrence, proved periodic row-sum cancellation, nonlinear characteristic operator `M(mu)=(mu-1)D_nu-H(mu)`, alpha lag-series convergence qualification, exact neutral global time-shift mode, derivative-comb representation, multiplier/exponent convention, normalized simple-root sensitivity, event-index relabelling covariance, and two-cell/Fourier/cluster symmetry reductions conditional on symmetry of the full delayed locked-state characteristic operator. MASTER retains the gate's repairs: source-aligned diagonal cancellation is proved rather than silently dropped; meromorphic alpha continuation is distinguished from the convergent lag series; weights alone do not justify Fourier reduction; and no complete full-hybrid-spectrum equivalence is asserted. MASTER establishes `CORE v0.4 Floquet Theory Freeze 0.1` / RB-010. No B23–B40 output, actual Lighthouse multiplier/root/stability boundary, v0.5 normal form, or downstream numerical effect is promoted. To eliminate unnecessary serial rediscovery of the already-existing legacy corpus, MASTER adopts `research/master/command_protocol_v0_2.md` and amends `PROJECT_GOVERNANCE.md` with the frozen-work reuse rule `Reconstruct state, not frozen science`, plus commands `RESUME` and `VERIFY-LEGACY`. MASTER authorizes exactly one consolidated next scientific action: `CORE Legacy Verification Sweep 0.1`, covering legacy v0.4–v0.26 in one CORE session without returning to MASTER between versions. The sweep may audit, classify, mathematically cross-check and faithfully exact-replay committed deterministic artifacts where closure permits, but it may not promote exploratory C3 effects without preregistered rerun, tune after effect inspection, invent missing replay artifacts, or start v0.27.
Status: STABLE
Date: 2026-09-07

## Rollback points

- RB-001: Governance Initialization 0.1 — STABLE
- RB-002: CORE Legacy Recovery Input Snapshot 0.1 at `287eae8a86560b78ed94f30a2786243714c33ac0` — STABLE ADMINISTRATIVE / NON-CANONICAL SCIENCE
- RB-003: CORE Recovery Classification 0.1 — STABLE ADMINISTRATIVE / NO SCIENTIFIC FREEZE
- RB-004: CORE Mathematical Freeze 0.1 — FROZEN / STABLE SCIENTIFIC BASELINE
- RB-005: CORE Benchmark Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-006: CORE v0.2 Benchmark Result Freeze 0.1 — FROZEN / STABLE RESULT
- RB-007: CORE v0.3 Continuation Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY
- RB-008: CORE v0.3 Continuation Validation Contract Freeze 0.1 — FROZEN / STABLE PRE-EXECUTION CONTRACT
- RB-009: CORE v0.3 Continuation Validation Result Freeze 0.1 — FROZEN / STABLE RESULT
- RB-010: CORE v0.4 Floquet Theory Freeze 0.1 — FROZEN / STABLE SCIENTIFIC THEORY