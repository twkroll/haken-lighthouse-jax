# NUM-ENG MPFR Exact-Dyadic Serialization Repair & IR-A4-R Requalification Gate 0.6

Date: 2026-10-16
Workstream: 20 — NUM-ENG — Numerical Engineering
Decision: **SERIALIZATION REPAIR VALIDATED / FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED**
Status: **RETURN TO MASTER** (bounded repair-only outcome, not FULL PASS).
Evidence: ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE ONLY.

## Authority and chronology

MASTER authorization: `research/master/prompts/numerical_engineering_mpfr_exact_dyadic_serialization_repair_ir_a4r_requalification_gate_0_6.md`, project status v2.15; RB-019/RB-021/RB-023/RB-024/RB-025/RB-026. The complete Gate-0.6 contract was committed *before source modification or Gate-0.6 validation outputs*: `779c8f05256406c5684d4dec35ae123a418027fb`.

Baseline RB-025 source unchanged: Git blob `6df6740e86344628a2b9583f0a3f719f9d5817f8`, SHA-256 `0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539`. New source: `software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py`, SHA-256 `a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202`. The new source was created separately on `engineering/numerics-v0.1`; there is no merge of executable source to `main`. Physical authority `NUMENG_PULSE_AWARE_REFERENCE_V1` unchanged.

Fixed backend environment: GNU MPFR 4.2.2 and GNU GMP 6.3.0 on x86_64 Linux, Python 3.13.5. Captured library SHA-256: MPFR `4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c`, GMP `d15e1585c6c267296459570c8ac217ca9123044bcd4e896d2f686b32333445d2`.

## R1 — exact export (SERIALIZATION REPAIR VALIDATED)

The Gate-0.5 `M.val` fixed tiny-value floor was removed **only in the new versioned source**. The new path calls `mpfr_get_z_2exp(z,x)` to extract exact binary integer significand `z` and exponent `e` for an *already correctly directed-rounded finite MPFR value*; GMP's exact integer-to-decimal conversion and integer-only Python parsing produce exactly `Fraction(z)*2**e`. Signed real values are unchanged, zero/negative zero map to the same exact real zero. No Python float, nextafter, libm exponential, decimal roundtrip or artificial floor is used. This is exact representation of the rounded value, not a new mathematical approximation.

The original exp(-10000) negative control now yields positive intervals strictly below `2^-2048` at **all five preregistered p={128,256,512,2048,4096}**, both directly and in `response(x=1/100,r=1,h=0)`. Directed GMP serialization retains the exact MPFR endpoints. Independent high precision validates inclusion; it does not create certificates. The old RB-026 no-go remains true for the old source; it is not reinterpreted as an MPFR bug.

## R2 — resource-safe exact dyadics (REPAIR VALIDATED WITH FINITE DOMAIN)

Finite guards: precision 2..8192 bits, |exponent|<=131072, significand <=p+2 bits, exact Fraction numerator/denominator <=262144 bits; nonfinite/invalid values raise `ArithmeticFailure` and cannot yield a positive certificate. To handle very large dyadic denominators without disabling Python 3.13's 4300-digit global int-to-decimal safety limit, the repaired source serializes/reconstructs exact decimal numerator/denominator strings through bounded 1000-digit integer chunks. Decimal and JSON contents retain mathematically *exact* rational endpoints. A new ~120 KB valid tiny-No-Hit certificate can be serialized and independently audited; corruption of a strict margin is rejected.

Tests cover positive/negative powers through `2^-10000`, signed zeros, non-dyadic fractions, precision-out-of-range, extreme exponent, infinity/NaN, a divisor containing zero, threshold straddling, collision and finite-budget failure.

## R3 — finite-soundness regression (PASS)

- 19/19 new exact-serialization/resource/positive/negative tests PASS, clean process exit.
- 26/26 original Gate-0.4 tests run against `rifc_mpfr_v0_2` PASS, exit 0.
- 26/26 same original tests run against **unchanged** `rifc_mpfr_v0_1` PASS, exit 0.
- Combined RIFC regression: **71/71 PASS**, single process exit 0.
- Frozen physics/RRI/Batch-JAX compatibility subset: **28/28 PASS**, separately, exit 0.
- All six original RB-025 proof-data artifacts replay under the unchanged old auditor without physical simulation. At least six new ordinary positive Gate-0.6 artifacts plus the extended tiny-No-Hit proof also independently replay with the repaired auditor.

The 19 new QA test cases are source-specific and are not confirmatory scientific tests. No protected RNG namespace was generated.

## Q1/Q2/Q3 — arithmetic and expression-graph qualification

The companion `EXACT_DYADIC_AND_IR_A4R_PROOF_0_6.md` records the exact MPFR/GMP export proof and conditional primitive ulp rate; a uniform response lower-bound on the fixed compact above-threshold segment (`psi(s)>1/300`); a threshold-straddling monotone branch; and the alpha-state/cell/prefix operation graph with conservative count `N_n<=1024*2^n+1024`. Interval range/dependency width is explicitly distinguished from rounding excess. The direct serialization adds exactly zero rounding excess.

## Q4/Q5 — full IR-A4-R NOT ESTABLISHED

**The full frozen candidate `B_K=2^8192` whole-expression propagation bound is not analytically proved for the entire source graph.** Moreover the actual repaired source supports only `p<=8192`, and its `certify` API still limits `nmax<=16`; the RB-024 theoretical schedule `p_n=128+8n` exceeds the precision resource cap at n=1009. Hence the current finite-budget code cannot be claimed to execute the unbounded refinement sequence required for an implementation-wide eventual-certification guarantee. Resource guards fail closed, they do not establish convergence.

No new source-level rate floor was found in the supported finite exact-GMP serialization path. This does *not* prove a finite uniform B_K for the full arithmetic graph, nor refute its potential existence under a future unbounded backend. Source/proof correspondence for a full IR-A4-R qualification is therefore incomplete. Full Gate-0.6 PASS is explicitly withheld.

## Q6/Q7 — NOT EXECUTED by contract

Since the prerequisite Q4 analytical qualification is **not established**, no claimed rate-consistency fit/validation and no prospective eventual-certification trial family was executed. A finite tiny no-hit proof and finite-budget negative control were run only as R3 soundness/fail-closed QA, **not** as a replacement for Q6/Q7. No hidden parameter/domain/threshold retuning.

## Component classification

**SERIALIZATION REPAIR VALIDATED:** new versioned exact MPFR/GMP dyadic export under captured finite ABI and resource constraints.

**FINITE SOUNDNESS PRESERVED:** repaired outward interval RIFC and saved proof-data replay under finite tests, original RB-025 baseline untouched.

**IR-A4-R NOT ESTABLISHED / DEFERRED:** unbounded whole-expression B_K derivation and formally unlimited precision/refinement semantics.

**EVENTUAL-CERTIFICATION IMPLEMENTATION VALIDATED:** NO; Q7 not authorized after missing Q4 proof.

**DEFERRED:** sequential complete event tapes, NNE-A, parameter-box chart radius, all AI/APP-3 and TR-27C science.

## MASTER recommendation

Accept only this **bounded serialization-repair result**, not an IR-A4-R/full eventual-certification freeze. Consider a separate, prospectively scoped arithmetic-propagation proof gate with an idealized unbounded precision family and an explicit bounded-resource/execution distinction; alternatively prioritize full finite certificates and treat eventual termination as deferred. RB-025 and RB-026 must both remain historically immutable.

No alteration to RB-004 science, RB-015 SCIENTIFIC FAIL, RB-020 parked trust-region contract, reserved 2711xxx data, APP-3, or canonical main source. All work was on `engineering/numerics-v0.1`.

**STOP — RETURN TO MASTER.**
