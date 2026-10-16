# NUM-ENG Gate 0.7 — prospectively frozen source-graph IR-A4-R proof contract

Date: 2026-10-16. Status: FROZEN BEFORE NEW GATE-0.7 ANALYTICAL RESULTS / VALIDATION.
Scope: analytical arithmetic-graph qualification of RB-027, **without changing any executable source**. All outputs DEVELOPMENT/ENGINEERING EVIDENCE, not scientific effect claims.

## Exact frozen identities

Gate prompt \`research/master/prompts/numerical_engineering_rifc_source_graph_ir_a4r_qualification_gate_0_7.md\` (Git blob aa84a026a94f5a55e5a59deca58d9cf943cce54b). Main HEAD at intake 3d7d4c703c783c219e83a5b86e066d4e409be9c6; branch HEAD at intake 2b4e12054665411bf1c5b238331b6ace1f1cb721.
Repaired RB-027 executable \`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py\`: SHA256 a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202, Git blob 1b94cf36447f428a9968c90ac3c0e74c18494d1c. Original RB-025: SHA256 0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539, Git blob 6df6740e86344628a2b9583f0a3f719f9d5817f8. MPFR 4.2.2 / GMP 6.3.0 with correctly directed rounding and exact mpfr_get_z_2exp dyadic conversion; no ordinary libm or nextafter-based certification. Frozen RB-019 physical authority NUMENG_PULSE_AWARE_REFERENCE_V1 unchanged. All RB-004…RB-027 authoritative outcomes retained.

## One idealized source-family definition

\`RIFC_infty\` is identical to the positive-certificate expression graph of v0.2, including fraction-to-MPFR input loads, RNDD/RNDU endpoint arithmetic/exp/sqrt (where invoked), exact MPFR integer+dyadic export, comparison branches, dyadic Darboux cells, exact stored prefix and strict hit/no-hit inequalities; **only finite resource caps are lifted** (p<=8192, exponent and GMP-integer size and nmax<=16). For every finite computation under all existing v0.2 resource guards, the ideal family uses the exact same rounding directions, endpoints, branches and certificate comparisons, and hence must return bit-exact same arithmetic endpoints and classifications. Resource failures are outside the subset of positive finite correspondence, not assumed away in source.

Schedule \`p_n=128+8n\`, \`m_n=2^n\`, unbounded mathematical n. This ideal family is a mathematical abstraction, NOT the production runtime.

## Frozen compact domain and fixed branches

Finite union of the following exact singleton/interval fixtures (closed bounded union; no parameter search):
- K01: alpha=1, r=1, h=0, psi0=1/100, q0=0, L=1, gap 1/4; includes direct S(1/100)=exp(-10000) at s=0.
- K02: same, gap 2^-2049 (strict tiny positive no-hit).
- K03: alpha=1, r=1, h=-1, psi0=q0=0, L=4, gap=1 (strict regular hit, S=exp(-1)).
- K04: alpha=1, r=1, h=1, psi0=q0=0, L=1, gap=1/4 (fully subthreshold).
- K05: direct response below: x=[-1/100,-1/200], r=1,h=0; threshold contact x=[0,0]; straddling: x=[-1/100,1/100], r=1,h=0; above: x=[1/100,1/50], r=1,h=0.
- K06: exact labelled structural arrival edge e0 at t=1/2 with weight interval [-1/16,1/16] and alpha=1; competing event disjoint at t=3/4 and interval-overlap negative control. No full ordinary-chart assertion.

Compact semantic scalar bounds for intermediate **real interval endpoints after ideal operations**, NOT raw numerator/denominator integers fed to the rational parser: absolute value <= H=2^18. The transient exact rational numerators and denominators can grow with precision, so source-level fraction loading must be analyzed using **relative** integer MPFR rounding and quotient conditioning, not a false uniform absolute bound on those raw integers. On above-threshold response branches, the intended exact input gap is >=1/300 on K01/K02, exactly 1 on K03 and >=1/100 on K05's positive/straddling top endpoint. The proof must show that directed interval-computed gap endpoints also remain >=delta=1/400 for p_n>=128; **do not assume this as an unproved fact**. Every division entering a positive certificate must have a bounded-away-from-zero real divisor (response reciprocal-square denominator >=1/160000, and positive rational input denominators). Exact source endpoint/exponent ranges in these fixtures lie in [-100000,100000], and finite arithmetic endpoint hull [-2^18,2^18] is a prospective overbound to be proved, not post hoc fitted. In active exp calls, arguments are nonpositive, so exp derivative <=1. For sqrt if reached through permitted aux function, require its argument>=1/160000; no positive first-hit certificate in these fixtures calls sqrt.

Domain includes finite negative/zero responses and strict positive response cases; no arbitrary parameter boxes and no near-threshold *above* inputs with vanishing gap. No compact-domain narrowing after seeing the output.

## Exact primitive model, excess definition and nodewise strategy

Let u=2^(1-p). For finite nonzero normal MPFR rounds, directed endpoint relative error <=u (under the ideal unbounded-exponent family), including exp of finite argument and integer parsing. Exact dyadic export has **zero** additional error. Correctly rounded rational load \`a/b\` must be shown to obey a bounded **relative ratio** error (aim <=8u for p>=128), independently of enormous integer numerator/denominator sizes, assuming nonzero positive denominator and no exponent limits. For scalar inputs |x|<=H this yields an absolute loading bound <=8uH. Interval time cells are exact real interval data, not arithmetic excess.

For an exact natural interval-extension graph using exact +,-,*,/,exp, endpoint comparison and the same branch decisions, define \`E_arith\` as **maximum absolute outward endpoint displacement** from that exact natural interval graph due solely to MPFR rounding/loading, at each cell/prefix (not the full Darboux width caused by interval time dependency). If branch decisions differ because an interval exactly touches h, prove outward containment and choose the comparison graph with branchwise monotone hull; do not falsely claim identical branch if not justified. Use endpoint l-infinity norm (max of absolute endpoint perturbations).

Freeze prospective primitive absolute roundoff bound r_p=2^24*2^-p for all bounded real scalar endpoint operands; for endpoint maps use a safe per-operation Lipschitz overbound L0=2^80 on the interval hull, provided the gap/divisor and active exponent restrictions above have been established. A source endpoint-graph local depth bound D<=512 must be shown from actual code; if false, the proof target fails rather than redefining D. The desired cell bound via the recurrence e_{j+1}<=L0 e_j +r_p is <=2^41000*2^-p under the stated bounds. The target global propagation constant is prospectively fixed B_K=2^65536, with a source-graph primitive-work count overbound N_n<=1024*2^n+1024. Prefix arithmetic errors accumulate additively (no multiplication-by-L0 amplification across prefix cells), and cell gain widths Δ=L/2^n<=4. Prove a finite E_arith(n)<=B_K N_n 2^-p_n or report NOT ESTABLISHED; no fitting of B from observed results.

**Crucial non-circularity:** validate the compact hull/divisor margin for the computed endpoint graph using explicit, sharper branchwise stability bounds for p>=128 before invoking the coarse L0 recurrence. A bound of size 2^41000*2^-128 would NOT establish safety of the hull, and cannot be used circularly for stability. Distinguish exact range width, arithmetic excess, and the precision-independent data-radius issue.

## Correspondence and outcome rules

Finite-executable correspondence is exact **only** for supported p/exponents/integer lengths/nmax when real backend versions and rounding agree. No claim of automatic actual infinity on a finite machine.

G-PASS: complete noncircular hull/divisor branch proof; primitive and source-node rate; explicit N_n/B_K; exact source correspondence; E_arith(n)->0; then (and only then) finite deterministic post-proof QA.
G-NO-GO: rigorous source/domain counterexample showing no B_K exists (a lack of proof alone is NOT a NO-GO).
G-BLOCKED/NOT ESTABLISHED: a necessary branch/hull/backend/correspondence proof is missing; honestly report which assumptions remain unproved. No implicit promotion to PASS.

Post-PASS-only verification (fixed, not to be run as substitute for proof): K01,K02,K03,K04 and K05 at n={0,2,4,6,8} and p_n={128,144,160,176,192} (within source bounds), compare natural graph endpoint enclosures against 200-digit mpmath independent point values where applicable; ensure upper discrepancy <=B_K N_n2^-p_n; verify finite positive no-hit/hit statuses, plus nmax=0 fail-closed controls. Corrupt one proof-data prefix and verify auditor rejection. Do not calculate a B from these results.

Proof artifacts: proof-contract Git commit; full named derivation and source graph inventory including partial/failed lemmas; source-correspondence audit; machine-readable constants/claims/verification status; Git report, STATUS return to MASTER. No executable source changes whatsoever, no protected RNG/TR-27C/APP-3/novelty/manuscript experiments.

STOP — RETURN TO MASTER.
