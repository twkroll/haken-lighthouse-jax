# NUM-ENG RIFC Source-Graph Arithmetic Propagation & Idealized IR-A4-R Qualification Gate 0.7

Date: 2026-10-16
Workstream: 20 – NUM-ENG – Numerical Engineering
Decision: **PASS — RESTRICTED IDEALIZED IR-A4-R SOURCE-GRAPH QUALIFICATION K01–K06 / FINITE SOURCE CORRESPONDENCE**, ENGINEERING/THEORY-VALIDATION ONLY.
Status: RETURN TO MASTER.

## 1. Exact scope and chronology

Authorizing MASTER prompt:
\`research/master/prompts/numerical_engineering_rifc_source_graph_ir_a4r_qualification_gate_0_7.md\`.
Frozen authorities: RB-004/RB-019/RB-021/RB-023/RB-024/RB-025/RB-026/RB-027 and current MASTER/CORE/NUM-ENG STATUS.

Pre-analysis contract:
\`research/numerical_engineering/rifc_source_graph_ir_a4r_proof_contract_0_7.md\`, **committed before new analytical conclusions and postproof validation**, commit \`d6b76886663a911a85e4b684825b3047e517b754\`.

Canonical repaired source, unchanged:
\`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py\`
Git blob \`1b94cf36447f428a9968c90ac3c0e74c18494d1c\`,
SHA256 \`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202\`.

Original RB-025 remains byte-identical:
Git blob \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`,
SHA256 \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`.

Backend assumptions: correctly directed MPFR 4.2.2, exact GMP 6.3.0 \`mpfr_get_z_2exp\` conversion; Python 3.13.5 x86_64. Existing finite resource guards, source, precision choices and source paths were not edited.

## 2. Analytical derivation — G-PASS on the fixed restricted domain

Companion artifact:
\`research/numerical_engineering/rifc_source_graph_ir_a4r_derivation_0_7.md\`.

The prospectively frozen K01–K06 domain consists of three ordinary first-hit/no-hit arrival-free alpha cases, a fully subthreshold control, below/contact/straddling/above response-interval controls, and one fixed structural arrival. It is a **finite union of compact input families**, not a universal Lighthouse parameter domain. The exact branchwise response arguments for the active above-threshold paths stay at least \(1/300\) above \(h\), except explicitly threshold-safe branches that do not evaluate the reciprocal at/below threshold. Noncircular source-level enclosure estimates for p>=128 ensure actual directed intervals remain >\(1/400\) where a reciprocal is evaluated.

The proof first distinguishes unbounded raw integer numerator/denominator sizes used by rational input conversion from bounded **semantic ratio values**. MPFR integer parse and directed quotient give relative rational-load error <=\(8u\), \(u=2^{1-p}\), independent of integer digit counts in the ideal unbounded family. Exact-dyadic export adds zero error. For scalar interval graph outputs |x|<=H=2^18, local rounded output excess <=\(2^{24}2^{-p}\).

The response branches are threshold-safe. On the explicitly verified bounded divisor region \(|b|>=1/160000\), interval add/sub/mul/div and exp (only on nonpositive arguments) have an endpoint l-infinity Lipschitz majorant \(\Lambda=2^{80}\). The source's finite local cell-DAG dependency depth is less than 512 primitive nodes; the per-cell arithmetic excess is bounded by \(2^{41000}2^{-p}\). Independently, all cell gains are in [0,L/2^n], and the cumulative source prefixes remain in [0,L] for all n because dyadic endpoints and \(kL/2^n\) are exactly representable at \(p_n=128+8n\). No circular use of the coarse total error bound is required to keep source values in the compact hull.

The source has a maximum of 8 directed scalar endpoint evaluations in one interval product/division, each with at most 7 MPFR primitive operations, and less than 700 scalar MPFR primitives per cell. The fixed graph therefore satisfies
\[
2^n\le N_n\le1024\,2^n+1024.
\]
Prefix error accumulates **additively**, not with the coarse cell nonlinearity at every prefix step:
\[
E_{\mathrm{arith}}(n)\le2^{41002}2^n2^{-p_n}.
\]
Using the prospectively frozen \(B_K=2^{65536}\),
\[
\boxed{ E_{\mathrm{arith}}(n)\le B_K N_n 2^{-p_n}, \quad p_n=128+8n }
\]
holds for the idealized graph on K01–K06. Since \(N_n=O(2^n)\), the bound tends to zero at worst as a constant times \(2^{-7n}\). This is a **restricted idealized arithmetic-rate proof**, not global mathematical interval correctness or practical computational cost. The giant constant is intentionally non-sharp and must not be called a usable error tolerance.

Source-proof correspondence:
\`research/numerical_engineering/rifc_source_graph_finite_correspondence_0_7.md\`.
The ideal family changes only finite resource limits; every finite Gate-0.6 computation staying within MPFR precision, exponent, integer/JSON and nmax caps follows the same directed endpoint/comparison DAG and produces the same exact dyadic proof data. A finite cap hit remains UNCERTIFIED/RESOURCE failure, not a mathematical no-hit.

## 3. Prospectively fixed finite postproof QA

The postproof suite was run **only after** the analytical derivation was recorded in Git. Fixed levels \(n=\{0,2,4,6,8\}\), precisions \(\{128,144,160,176,192\}\), and K01–K06 were not modified. Results:

- K01 strict no hit: 5/5 PASS.
- K02 tiny strict no hit: 5/5 PASS.
- K03 unique regular hit: 5/5 PASS, including independent mpmath high-precision integral containment \(4e^{-1}\).
- K04 exact subthreshold: 5/5 PASS.
- K05 four fixed response threshold branches at all five precisions: 5/5 PASS.
- K06 structural-zero/cross-zero retained arrival, labelled collision rejection, insufficient nmax resource exhaustion: 1/1 PASS.
- One additional mutated-prefix negative certificate replay was correctly rejected while the original positive certificate was accepted (clean exit).

All 26 fixed runs returned process exit code 0 in isolated processes. Verified invariants include: stored response intervals in [0,1], gains in [0,Delta], prefixes in [0,kDelta], finite first-hit/no-hit classification, strict event/tape guards, source SHA pinning, and MPFR/GMP version pinning.

The first monolithic validation process exceeded the container walltime limit after completing K01 and the first K02 levels. It is explicitly NOT counted as a passing aggregate test. Fixed numerical tests were rerun process-by-process **without altering fixtures or acceptance thresholds**, and all 26 cleanly exited. Isolating the process is a QA orchestration change, not source/contract retuning. No new broad historical 250-case regression was required or executed because neither RB-027 source nor physical/JAX software changed.

Machine-readable Git summary:
\`research/numerical_engineering/rifc_source_graph_gate_0_7_validation_results.json\`.
Raw local reproducer and log bundle SHA256:
\`c74f6ed3699914aec77196cdc9bd2756fd456a1a67f92c4ed3ccb70d000d6e2f\`,
archive \`NUMENG_Gate_0_7_Source_Graph_Proof_Audit.zip\`.
Byte manifest:
\`research/numerical_engineering/rifc_source_graph_provenance_manifest_0_7.json\`.

### Qualification caveats

The proof concerns **endpoint arithmetic excess** relative to the exact natural interval expression graph. True interval dependency/Darboux cell-width overestimation is a separate term governed by continuity; neither is replaced by an empirical convergence fit. Finite consistency data were not used to choose \(B_K\) or the domain.

IR-A4-R beyond K01–K06, arbitrary parameter families or zero-margin/horizon/collision geometries, full sequential event completeness, NNE-A and full chart radius remain DEFERRED.

The idealized \(p_n\to\infty\) family is *not* the actual production implementation: the latter retains \(p\le8192\), bounded materialized dyadics/exponents, and \`nmax<=16\`. RB-024's eventual strict-margin certification applies only to the idealized family under its other theorem assumptions. Every finite invocation may exhaust its allotted resources and correctly return UNCERTIFIED. No finite-resource guarantee of unconditional termination is made.

## 4. Classification and MASTER recommendation

- **IR-A4-R IDEALIZED FAMILY ESTABLISHED:** on the explicit frozen K01–K06 under correctly-directed ideal MPFR and exact dyadic export assumptions.
- **IDEALIZED SOURCE-GRAPH CORRESPONDENCE ESTABLISHED:** positive-certificate expression graph has no extra finite-source approximation after lifting only resource limits.
- **FINITE EXECUTION CORRESPONDENCE ESTABLISHED:** finite calls within all caps give exactly corresponding ideal finite-member endpoints and classifications.
- **DEFERRED:** whole-model/global IR-A4-R, implementable unlimited refinement, full chart, NNE-A, scientific effect and APP-3.
- **REJECTED:** any claim that a finite p/nmax executable now has an unconditional eventual-certification guarantee.

Recommendation: MASTER may freeze a **strictly bounded idealized source-graph IR-A4-R qualification 0.7**, but must retain RB-025/RB-026/RB-027 unchanged, including historical old-source NO-GO, and keep finite software bounds explicit. No source is merged to main.

All results ENGINEERING VALIDATION / DEVELOPMENT EVIDENCE. No protected \`2701xxx\`/\`2711xxx\` seeds, no TR-27C, no APP-3, no RB-015 revision, no manuscript/novelty and no effect-bearing work.

**STOP — RETURN TO MASTER.**
