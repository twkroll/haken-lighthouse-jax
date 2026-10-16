# NUM-ENG RIFC-0.1 Outward-Interval Implementation & Validation Gate 0.4

Date: 2026-10-16
Workstream: 20 – NUM-ENG – Numerical Engineering
Decision: **PASS — FINITE CERTIFICATE SOUNDNESS ONLY (ENGINEERING)**
Status: RETURN TO MASTER, conditional on MASTER review.
Scientific classification: **ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE**, not a scientific-effect PASS.

## 1. Governing authority and pre-execution chronology

Authorized MASTER task: \`research/master/prompts/numerical_engineering_rifc_interval_implementation_validation_gate_0_4.md\`. Governing authorities: PROJECT_GOVERNANCE, Parallel Engineering Policy 0.1, RB-004, RB-019, RB-021, RB-022, RB-023 and RB-024 (candidate plus mandatory proof-closure repair). The physical model and authoritative \`NUMENG_PULSE_AWARE_REFERENCE_V1\` were not changed.

Gate start: \`main\` HEAD \`d344504d360d6981e95a52cdcffc5dbede5dae6c\`; engineering branch HEAD \`5dc9b3aed33557fb3749951e87b1e9d4ae7679e7\`.

**The complete finite validation contract was committed BEFORE running new Gate-0.4 fixtures**:
- \`research/numerical_engineering/rifc_interval_implementation_validation_contract_0_4.md\`;
- pre-execution contract commit \`2aa95c77973fe63a82a7cf11472ee92273b5bb7c\`.
- exact inputs, refinement level budgets, arithmetic backend, acceptance/taxonomy rules, classes, negative controls, independently specified comparisons and artifact formats were fixed there.

No preregistered fixture, scientific target, arithmetic threshold, success rule or backend was retuned after seeing results.

## 2. Backend qualification: RI-01–RI-03

- Python 3.13.5 on Linux x86_64 CPU; **GNU MPFR 4.2.2**, shared-object identity \`/lib/x86_64-linux-gnu/libmpfr.so.6\` SHA-256 \`4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c\`.
- \`ctypes\` bindings invoke MPFR directed rounding RNDD/RNDU for finite +, -, multiplication, permitted division, square root, and exponential. Exact rational fixture inputs are loaded by outward rational endpoint enclosure. All serialized endpoints are exact dyadic rationals. Arithmetic errors, unsupported scalar domains, zero-containing denominator, nonfinite operations and oversized representational cases fail closed.
- MPFR's independently specified correctly rounded \`mpfr_exp\` primitive is the **exponential inclusion contract**, not the platform \`exp\` plus an unjustified \`nextafter\`. Finite positive soundness is conditional on MPFR's documented correct-rounding semantics and the platform ABI.
- An explicit outward dyadic serialization floor for extremely tiny exponentials avoids pathological huge-rational output; the floor is a *widening*, never an inward truncation. This is a software-domain guard, not a theorem of convergence.
- RI-01: point/interval +, -, *, /, min/max/hull/intersection, exact Fraction containment PASS.
- RI-02: MPFR directed exp for predetermined scalar/interval fixtures compared with independent 200-digit mpmath point values PASS. The high-precision comparator is only QA, not the proof primitive.
- **RI-03 / IR-A4-R: DEFERRED / NOT ESTABLISHED**. No uniform backend/whole-expression \`B_K N 2^-p\` rate has been independently proven. Therefore no eventual finite-termination theorem is invoked, notwithstanding successful finite calculations.

## 3. Implemented rigorous finite scope

Versioned implementation under \`software/numerical_engineering/rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py\`:

1. finite inclusion-valid interval primitives and exact rational endpoint serialization;
2. arrival-free alpha state/response interval propagation for known singleton scalar inputs;
3. threshold-safe monotone response enclosure with no reciprocal evaluation at the threshold;
4. equally spaced dyadic Darboux gain and complete outward prefix interval tape under \`m_n=2^n\`, \`p_n=128+8n\`;
5. strictly positive margin \`CERTIFIED_NO_HIT\`;
6. strictly bracketed, transversal \`CERTIFIED_REGULAR_HIT\`;
7. structural-zero labelled arrivals, identity jumps and topology-fixed weight-through-zero handling;
8. exact rational competing event-order/horizon/initial tests with strict disjointness, exact ties invalid and interval overlaps inconclusive;
9. finite refinement budgets and full nonpositive taxonomy;
10. JSON serialization plus independent recomputation of every cell, gain/prefix and strict inequality **without the physical simulator**.

A positive regular hit currently certifies an **individual arrival-free segment with known initial alpha state and phase gap**, not an entire automatically generated multi-neuron ordinary event chart. The positive event ordering and structural arrival certificates are separate, exact rational comparison objects. There is **no emitted \`CERTIFIED_ORDINARY_CHART\`**, no solved parameter-box NNE-A and no general source/rate proof for IR-A4-R.

## 4. Preregistered validation results RI-04–RI-14

| ID | Contract family | Result |
|---|---|---|
| RI-04 | Exact alpha-state segment propagation at alpha=1 and alpha=1000 | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-05 | Fully below/at/straddling/above threshold S interval enclosure | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-06 | Dyadic Darboux gain contains 200-digit reference integrals | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-07 | Strict no-hit, zero-margin nonpositive control | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-08 | Strict regular first-hit and transversality, broad and narrow pulse | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-09 | Topology-fixed structural zero, crossing zero, labelled arrival | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-10 | Strict event ordering, overlap, exact collision and initial/horizon | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-11 | Seven implementable negative/fail-closed classes | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-12 | Replayed positive JSON proof, tamper rejection | THEORY-CONSISTENT ENGINEERING VALIDATION |
| RI-13 | Unconditional eventual certification under refinement | **DEFERRED — IR-A4-R not established** |
| RI-14 | Deliberately inadequate finite Nmax | RESOURCE_EXHAUSTED / UNCERTIFIED, as required |

RI-01 and RI-02 PASS, RI-03 DEFERRED (see above).

**TH-FH-01–08 finite checks**:
- TH-FH-01 narrow alpha=1000 input: \`CERTIFIED_REGULAR_HIT\` at local time bracket \`[1/200,1/100]\` = [0.005,0.010], containing pre-existing RB-019 physical offset approximately 0.005000505363421. The earlier physical simulator is only a QA comparator.
- TH-FH-02 subthreshold: \`CERTIFIED_NO_HIT\`.
- TH-FH-03 nearly tangential stress: pointwise small transversality yields \`STRICT_MARGIN_ABSENT\` under fixed demand; **no claim that a complete near-tangent first-hit time was certified**.
- TH-FH-04 strict before/after ordering and exact spike/arrival tie: certified strict orders; exact tie \`ORDINARY_CHART_INVALID\`.
- TH-FH-05 finite, absolutely summable two-pulse omitted-history tail: phase gain bounded in high-precision comparison; infinite locally finite history without absolute summability remains **DEFERRED**.
- TH-FH-06 repaired structural-zero convention: the labelled arrival persists with weight −1/16, 0, +1/16 and a crossing interval; jump identity at zero; omitted-edge tape differs.
- TH-FH-07 exact horizon/initial boundary: \`ORDINARY_CHART_INVALID\`.
- TH-FH-08 distinct-target simultaneous commuting arrivals: state jumps commute, but ordinary total-order chart \`ORDINARY_CHART_INVALID\`.

No theorem contradiction under the inspected RB-024 assumptions was observed in these finite fixtures. A numerical classification \`UNCERTIFIED\` is not physical nonexistence or singularity.

## 5. Reproduction and audit trail

- New suite: **26/26 PASS**, repeat **26/26 PASS**, both exit 0; \`logs/test_final_1.log\`, \`logs/test_final_2.log\`.
- Unchanged reference/JAX compatibility: \`test_reference.py\`, \`test_rri_repair_v01.py\`, \`test_gate02_batch_guard.py\`: **28/28 PASS**, exit 0 with proper \`PYTHONPATH=.\`.
- Independent artifact replay: **6/6 positive JSON certificate objects** checked from stored MPFR enclosures/strict inequalities in a fresh executable process with \`source/audit_saved_certificates.py\`, no physical simulator.
- Six certificates include strict no-hit, broad and narrow regular first hits, a strict event-order proof, exact-zero and cross-zero structural arrival proofs.
- The original failing test log (a wrong max-interval *test assertion*) is retained. A later 24-test extension found one exact-horizon status precedence bug and a huge-denominator serialization resource issue on extremely small exponentials. Both were fixed conservatively without altering the pre-execution fixture set or the MPFR inclusion backend. Interim failing logs and subsequent repeated clean 26-case logs are all retained.
- First compatibility attempt misconfigured Python module resolution; its import errors are retained separately from the successful environment-corrected 28-case regression.
- All protected seed namespaces were left unused. No TR-27C, APP-3, optimization, training, scientific speedup or stochastic task was run.

## 6. Provenance and integrated inventory

- Branch: \`engineering/numerics-v0.1\`; original source-data integration commit \`e5b1c488aa6e03e706171902942377c210979a8f\`.
- Versioned subtree: \`software/numerical_engineering/rifc_interval_gate_0_4/\` with 29 integrated source, proof, log, environment, and SHA256 manifest files; includes unit-test cache as *non-authoritative raw QA metadata*.
- The subsequent exact \`OUTCOME_MATRIX.json\` result-class matrix was integrated in commit \`8b6d8455226d12489b08804d8915b28f2203df9b\`.
- Source \`rifc_mpfr_v0_1.py\` Git blob SHA \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`, source SHA-256 \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`.
- \`source/test_rifc_gate04.py\` SHA-256 \`f951802e4b41b64b1f722a171a97715aa9cb08e5fd292a928c71c0beea1f3ca2\`.
- Complete \`SHA256_MANIFEST.json\` and \`certificates/CERTIFICATE_MANIFEST.json\` permit byte-level identification; certificate auditing recalculates from exact serialized rational inputs and MPFR operations.
- Full downloadable local ZIP is \`NUMENG_RIFC_Gate_0_4_Engineering_Package.zip\`; no executable source merged to \`main\`.

## 7. Final component disposition

- **ENGINEERING-APPROVED FOR FINITE SOUNDNESS ONLY**: MPFR 4.2.2 directed primitive/exp interval backend conditional on its correct-rounding specification; arrival-free interval alpha propagation; threshold-safe response; dyadic gain/prefix; strict no-hit and regular-hit segment certificates; exact rational order/structural-zero arrival certificates; fail-closed finite budget; independently replayable proof artifacts in tested finite input domain.
- **ENGINEERING-APPROVED**: deterministic finite QA harness, exact input/source identities and raw provenance tools.
- **DEFERRED**: IR-A4-R rate and eventual certification; full multi-event tape construction; arbitrary scalar/parameter boxes, general NNE-A full-chart radius; formal interval proof of the MPFR library itself; full near-tangency First-Hit family, unsummable infinite history, global simulator certification, GPU portability, speed/scaling and AI performance.
- **REPAIR-REQUIRED**: none identified in the *approved finite subset* after preserving and correcting interim software test defects.
- **REJECTED**: interval from ordinary \`math.exp\`+nextafter as proof; treating overlapping competitor intervals as collisions or certified ordering; treating token equality as tape authority; claiming full-chart/eventual certification or scientific effects from finite QA.

## 8. Gate decision and STOP

**PASS — ENGINEERING VALIDATION, FINITE CERTIFICATE SOUNDNESS ONLY** under the frozen bounded domain, GNU MPFR correctness contract, exact inputs and strict replayed inequalities.

Recommend MASTER consider \`NUM-ENG RIFC-0.1 Interval Certification Freeze 0.4\` as a **bounded finite-soundness engineering validation layer**, not a global First-Hit theorem or production-wide event-certifier freeze. MASTER should separately decide whether full sequential tape logic and IR-A4-R whole-expression proof need a follow-up gate.

RB-015 immutable SCIENTIFIC FAIL; RB-020/TR-27C remains parked; all reserved confirmatory seeds UNGENERATED/UNEVALUATED; APP-3 PROTECTED/WAIT. No scientific promotion, no \`main\` executable merge, no novelty/manuscript claims.

**STOP — RETURN TO MASTER.**
