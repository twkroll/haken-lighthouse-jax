# NUM-ENG Parametric Compact-Domain RIFC Qualification Gate 0.8

Date: 2026-10-17. Workstream: 20 – NUM-ENG – Numerical Engineering.
Decision: **CANDIDATE PASS — THREE PARAMETRIC COMPACT BOXES QUALIFIED / DEVELOPMENT ENGINEERING EVIDENCE ONLY**.
Status: **RETURN TO MASTER**. No scientific effect or globally qualified parameter domain is claimed.

## 1. Authority, chronology and freeze identities

Current MASTER project v2.19, branch \`engineering/numerics-v0.1\`. Authorizing prompt:
\`research/master/prompts/numerical_engineering_parametric_compact_domain_rifc_qualification_gate_0_8.md\` (Git blob \`4ebfa4b2bfe8336b64a8baa688c40bdef45e0357\`).
Canonical authorities RB-019/RB-021/RB-023/RB-024/RB-025/RB-026/RB-027/RB-028/RB-029/RB-030, with RB-029 Q-RIFC-K the theorem being instantiated. RB-030 RIFC-TAPE and NNE-A is **theory only and not executable in this gate**.

Before any new qualification result and validation, the complete **pre-execution contract** was committed:
\`research/numerical_engineering/rifc_parametric_compact_domain_qualification_contract_0_8.md\`,
commit \`32ec665ffe2ba1d3dae243725aaca9e630e3d0e0\`.

The symbolic derivation was committed separately **before the post-proof tests**:
\`research/numerical_engineering/rifc_parametric_compact_domain_qualification_derivation_0_8.md\`,
commit \`9a15b2ea80c9189cfe3a362549103895584e3d56\`.

All exact parameter ranges, three coordinatewise sample points per box, levels/finite nmax, comparison conditions and negative controls were specified beforehand. No box was narrowed or discarded after output inspection.

The unchanged frozen executable was:
\`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py\` (RB-027), Git blob \`1b94cf36447f428a9968c90ac3c0e74c18494d1c\`, SHA-256 \`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202\`.
Original RB-025 remains immutable: Git blob \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`, SHA-256 \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`.
GNU MPFR 4.2.2 / GMP 6.3.0; Python 3.13.5 x86_64 CPU. Existing physical reference authority \`NUMENG_PULSE_AWARE_REFERENCE_V1\` unchanged.

## 2. Analytical Q-RIFC-K result: three truly parametric boxes

The boxes are closed **positive-width products**, not lists of singleton fixtures. The symbolic estimates cover every exact parameter choice in each box; finite numerical tests only sample specified rational points.

### B1 — uniformly fully subthreshold / no hit

\[
\alpha\in[1,3/2],\ r\in[1,5/4],\ h\in[1,5/4],\
\psi_0,q_0\in[-1/16,0],\ L\in[1/2,1],\ d\in[1/4,1/2].
\]

Since \(\psi(s)=e^{-\alpha s}(\psi_0+s q_0)\in[-1/8,0]\) for every s in the segment while h>=1, the frozen response is exactly zero throughout and the source selects only the zero branch. No active reciprocal occurs. Every admissible trajectory has \(\overline{G}=0<\underline d\), strict margin at least 1/4. The source's directed arithmetic preserves the sign and separation.

**Classification: PARAMETRIC DOMAIN QUALIFIED** (zero response / strict no hit).

### B2 — regular positive-response first-hit family

\[
\alpha\in[1,3/2],\ r\in[1,9/8],\ h\in[-1,-7/8],\
\psi_0,q_0\in[0,1/16],\ L\in[4,5],\ d\in[1/2,3/4].
\]

For all s in the segment, \(0\le\psi(s)\le3/8\), hence the true active gap is >=7/8. Uniformly,
\[
S(\psi(s))\ge\exp(-72/49)>1/5,\qquad
G(L)>4/5>3/4\ge d.
\]
With \(G(0)=0\) and positive response, a unique regular first hit lies strictly in the segment. A separate noncircular source-graph sign/roundoff bound for p>=128 retains the *computed* active gap >1/2 before invoking the coarse whole-expression error constant. All interval division denominators on the positive branch exceed 1/4. The source has no arrival competitor in this fixed-topology family.

**Classification: PARAMETRIC DOMAIN QUALIFIED** (uniform active response / transversal first hit).

### B3 — structurally present weight crossing zero

\[
\alpha\in[1,5/4],\quad w\in[-1/8,1/8],\quad h\in[1,9/8],\quad
\psi_0\in[-1/16,0],
\]
with fixed source-labelled structural edge e0, arrival t=1/2, competitor t=3/4, horizon=1, and r=1,q0=0.

The arrival is strictly separated from the competitor by 1/4 and its edge jump obeys \(|w\alpha^2|\le25/128\). At w=0 the jump is identity, but the **labelled arrival remains present**. The interval \([-1/8,1/8]\) crosses zero without changing topology. A separate prearrival segment is subthreshold/no-hit. Nothing here certifies a postarrival trajectory, a full ordinary event tape or NNE-A.

**Classification: PARAMETRIC DOMAIN QUALIFIED — SINGLE STRUCTURAL ARRIVAL AND PREARRIVAL SEGMENT ONLY**.

## 3. Instantiated RB-029 arithmetic constants and schedule

The analytic derivation gives an independent branchwise semantic hull \(H_K=2^{18}\) and uniformly safe positive-response divisor lower bound 1/4 on active B2 operations. For B1/B3 the reciprocal is inactive. Rational endpoint load into directed MPFR satisfies the <=8u relative error bound for \(u=2^{1-p}\) under the ideal correct-directed model; raw integer numerator/denominator lengths are **not** falsely assumed bounded. The repaired exact MPFR/GMP dyadic export contributes no further roundoff.

The prospectively fixed coarse local arithmetic and endpoint-map bounds are
\[
r_K=2^{24},\quad L_K=2^{80},\quad D_K=512.
\]
For the source's fixed finite cell graph,
\[
2^n\le N_n\le1024\cdot2^n+1024.
\]
Define
\[
\Phi_K=\sum_{j=0}^{512}(2^{80})^j,\quad
C_{\rm cell}=2^{24}\Phi_K,\quad
C_{\rm gain}=C_{\rm cell},\quad
C_{\rm prefix}=C_{\rm gain}+2^{24},\quad
C_{\rm wrap}=C_{\rm cell},\quad
B_K=2\max(C_{\rm cell},C_{\rm prefix},C_{\rm wrap}).
\]

Noncircular compactness is checked using exact response sign, positivity and prefix-addition structure, including *variable non-dyadic* horizons L. Prefixes remain uniformly bounded by 2L (<=10) because \(2^n 2^{1-p_n}\) tends to zero and is uniformly tiny. This is established without using the final B_K.

On each qualified branch, the arithmetic endpoint excess relative to the exact natural interval graph satisfies
\[
E_{\rm arith}(n)\le B_K N_n2^{-p_n},\quad
p_n=128+8n.
\]
With \(\gamma=8>\beta=1\), the bound goes to zero in the **idealized unbounded-precision family**. Natural interval/Darboux range width remains a separate mathematical quantity, not collapsed into the roundoff bound.

These constants are intentionally enormous and are not useful precision recommendations. They were never fitted from the observed validation widths.

## 4. Q6 finite-source correspondence

The idealized member and the finite RB-027 implementation perform the same directed source-level arithmetic, fraction-to-MPFR endpoint loads, exact MPFR/GMP dyadic export, response branch decisions and strict proof inequalities when the finite call remains within all source resource caps. Thus rational parameter points accepted by the finite source have pointwise exact-dyadic output correspondence with their ideal members. The mathematical box proof quantifies over every exact real parameter choice; it does **not** imply that Python's Fraction API consumes arbitrary irrational parameters or directly propagates a full parameter box in one invocation.

Production remains constrained by \(p\le8192\), \`nmax<=16\` and finite exponent/integer/JSON budgets. A resource exit is fail-closed; the idealized asymptotic theorem is **not** a guarantee on finite hardware.

## 5. Q7 post-proof finite validation (all passed)

All **37 precommitted checks passed, clean exit 0** under the captured source/backend; no code modification:
- B1: 9/9 \`CERTIFIED_NO_HIT\` calls + 3 independent 160-digit high-precision phase/inclusion comparisons.
- B2: 9/9 \`CERTIFIED_REGULAR_HIT\` calls + 3 independent 160-digit high-precision integral/inclusion comparisons.
- B3: 9/9 structural/prearrival calls, including singleton w=-1/8, 0, 1/8 and crossing interval [-1/8,1/8], with all positive artifacts independently replayable.
- X1: analytic vanishing active threshold gap rejected as \`THEOREM ASSUMPTION FAILED\`; no false qualified box.
- X2: frozen narrow-pulse case with \`nmax=0\` returned \`RESOURCE_EXHAUSTED\`, never a negative physical conclusion.
- X3: hypothesized deletion of e0 at w=0 classified \`IMPLEMENTATION/GRAPH MISMATCH\`.
- X4: stored prefix mutation correctly rejected by the independent certificate auditor.

Source MPFR/GMP identities checked before tests. Validation checks response/gain/prefix inclusion and independent high-precision point/integral comparators. Where a directly computed *exact natural-graph arithmetic excess* was not independently available, no stronger independent measurement claim is made; the symbolic bound is an analytical result, not a fitted empirical number.

Git raw stdout (37 PASS records):
\`research/numerical_engineering/rifc_parametric_gate_0_8_POST_PROOF_RUN.log\`.
Git symbolic box/result index:
\`research/numerical_engineering/rifc_parametric_compact_domain_constants_results_0_8.json\`.
Full exact original 37-row NDJSON, local runnable validation harness, stdout, environment, certificates, full SHA-256 manifest and immutable read-only source copy: \`NUMENG_Gate_0_8_Parametric_Compact_Domain_Audit.zip\`, SHA256 \`803dd405146685745ee424b28cbfa0306e8451ef322bf8832a6bf632946a58f0\`.
Git provenance:
\`research/numerical_engineering/rifc_parametric_compact_domain_provenance_manifest_0_8.json\`.

## 6. Q8 negative controls / Q9 classification

B1 \`PARAMETRIC DOMAIN QUALIFIED\`.
B2 \`PARAMETRIC DOMAIN QUALIFIED\`.
B3 \`PARAMETRIC DOMAIN QUALIFIED\` **only for the precise structural arrival and separate pre-arrival segment**.
X1 \`THEOREM ASSUMPTION FAILED\` because the source's positive reciprocal endpoint gap can approach zero.
X2 \`RESOURCE-LIMITED / QUALIFIED IDEALLY\` (the finite cap deliberately exhausts).
X3 \`IMPLEMENTATION/GRAPH MISMATCH\` for the *deliberately invalid hypothetical* zero-edge deletion (not a bug in actual RB-027 source).
X4 negative proof-audit corruption rejected.

No observed finite case was dropped, post-hoc retuned or used to select B_K.

## 7. Final decision / MASTER recommendation

**CANDIDATE PASS — Q-RIFC-K COMPACT-BOX ARITHMETIC QUALIFICATION B1–B3 ONLY**. The three required genuinely varying compact parameter families analytically meet RB-029's sufficient arithmetic assumptions, and all prespecified finite consistency checks/negative controls passed.

Recommend MASTER review for a **bounded NUM-ENG Parametric Compact-Domain RIFC Qualification Freeze 0.8** with only these box-specific conclusions. In particular, keep separate:
- idealized arithmetic-rate proof vs finite execution;
- singleton/boxwise endpoint bounds vs an actual all-parameter-box RIFC implementation;
- certified single structural arrival vs full sequential tape;
- theorem's strict regularity conditions vs global model correctness.

RB-025/RB-026/RB-027/RB-028/RB-029/RB-030 and MAIN remain unchanged. No executable source integration, protected \`2701xxx\`/\`2711xxx\` RNG, TR-27C, CORE execution, APP-3, RIFC-TAPE code, NNE-A code, effect tests, performance claims, novelty or manuscript claims.

**STOP — RETURN TO MASTER.**
