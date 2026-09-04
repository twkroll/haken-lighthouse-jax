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

## Rollback points

- RB-001: Governance Initialization 0.1 — STABLE
