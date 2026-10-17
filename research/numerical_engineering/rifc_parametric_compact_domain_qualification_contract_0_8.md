# NUM-ENG Gate 0.8 — preregistered parametric compact-domain Q-RIFC-K qualification

Date 2026-10-17. Status: **FROZEN BEFORE ALL NEW GATE-0.8 QUALIFICATION RESULTS AND VALIDATION**. Branch \`engineering/numerics-v0.1\`. This document fixes ALL boxes, theorem proof targets, sampling and decision rules before observing Gate-0.8 outputs.

## Authorities and immutable implementation
MASTER v2.19, RB-019/021/023/024/025/026/027/028/029/030; numerical Gate-0.8 prompt Git blob 4ebfa4b2bfe8336b64a8baa688c40bdef45e0357. Original RIFC v0.1 (RB-025) unchanged. RIFC repaired v0.2 (RB-027) \`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py\`, SHA256 \`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202\`, git blob \`1b94cf36447f428a9968c90ac3c0e74c18494d1c\`. Backend GNU MPFR 4.2.2 / GMP 6.3.0 directed RNDD/RNDU, exact dyadic GMP export. No executable source modification or main merge. Physical authority \`NUMENG_PULSE_AWARE_REFERENCE_V1\`.

## Frozen compact parameter boxes (exact rational closed intervals, not just point lists)
All intervals include every real value between endpoints, with fixed structural topology and fixed branch-selection rules:
- **B1 SUBTHRESHOLD**: alpha in [1,3/2], r in [1,5/4], h in [1,5/4], psi0 in [-1/16,0], q0 in [-1/16,0], L in [1/2,1], phase gap d in [1/4,1/2]. Every segment is wholly below h and must be strict CERTIFIED_NO_HIT. All seven coordinates vary (nontrivial compact product box).
- **B2 ACTIVE REGULAR HIT**: alpha in [1,3/2], r in [1,9/8], h in [-1,-7/8], psi0 in [0,1/16], q0 in [0,1/16], L in [4,5], phase gap d in [1/2,3/4]. Every segment has positive active gap >=7/8 in the **exact natural semantic flow** and has a strictly regular first hit in (0,L); fixed topology with no arrivals. All seven coordinates vary.
- **B3 STRUCTURAL ZERO CROSSING**: fixed labelled edge \`e0\`, weight w in [-1/8,1/8], alpha in [1,5/4], h in [1,9/8], psi0 in [-1/16,0]; fixed r=1,q0=0,L=1,d=1/4, structural arrival t=1/2, one competitor arrival t=3/4, horizon=1. This qualifies the **single structural-arrival certificate** and separately the pre-arrival subthreshold segment. Do NOT assert complete post-arrival trajectory or whole event tape for a box. Source routine \`structural_arrival\` accepts exact singleton alpha and a weight **interval**, thus the whole family is represented by uniform interval/hull reasoning plus pointwise source correspondence, not falsely claimed to execute a parameter-box scheduler.

## Prospectively fixed failure-domain controls
- **X1 VANISHING ACTIVE GAP**: x=[-1/32,b], h=0,r=1, b ranges over [0,1/32]. For b>0, source straddling top evaluates reciprocal (b-h)^-2 with infimum gap 0. Reject qualification: THEOREM ASSUMPTION FAILED. b=0 selects below branch; neither this isolated point nor physical smoothness rescues uniform active source-graph qualification.
- **X2 RESOURCE**: alpha=1000,r=1,h=1/10,psi0=0,q0=4000000,L=1/50,d=1/200, nmax=0. Predeclared expected \`RESOURCE_EXHAUSTED / UNCERTIFIED\` (not a no-hit).
- **X3 TOPOLOGY MISMATCH**: a putative family algorithm deletes structural edge e0 exactly when its weight w=0; this changes the labelled-event graph. Reject as IMPLEMENTATION/GRAPH MISMATCH even though the physical zero jump is the identity. Positive B3 must retain e0 for w<0,w=0,w>0.
No failure-domain box may be retuned or dropped based on output.

## Target branchwise hull and divisor proofs (must be established before invoking B_K)
B1: for all s in [0,L] q0<=0,psi0<=0, exp(-alpha*s)>0, so psi<=0<h with h>=1; source below-only response=0, no reciprocal. |psi|<=1/8. B3 pre-arrival: psi<=0<h, and weight jump size bounded by (1/8)(5/4)^2=25/128. Labelled t=1/2 strictly before t=3/4 and horizon=1.
B2: for all s in [0,L], exp(-alpha*s) in (0,1], psi in [0,3/8], hence psi-h in [7/8,11/8]. r<=9/8 gives response S>=exp(-72/49)>1/5 (using exp(3/2)<5). Thus G(L)>=4/5>3/4>=d, while G(0)=0<d, and S>1/5 throughout; ordinary transversal first hit is strictly interior. The *computed* interval gap must be shown to stay >=1/2 uniformly under p>=128 without circular use of the final B_K: use directed relative rounding u=2^(1-p), at most 256u multiplicative widening on the bounded nonnegative alpha-state subgraph, h<=-7/8, so gap_lo>=7/8 - 1/64 >1/2. Its squared divisor is >=1/4. Upper gap remains <2, negative reciprocal exp arguments remain in [-16,0], and all intermediate scalar magnitudes <=H=2^18 (conservative).

For arbitrary real L in a box (non-dyadic allowed), source exact rational dyadic cell partition endpoints are converted with directed rounding. Although k*L/2^n need not be representable, each nonnegative rounded cell width and computed response <=1+8u, and every source prefix addition contributes <=8u relative factor. Since m=2^n and p_n=128+8n, m u<=2^-127-7n; use (1+8u)^(m+4)<2, so prefixes remain between 0 and 2L<=10 at all n. This compact proof must not assume that ALL variable L are exactly representable.

## Positive source graph, primitive and propagation budget (freeze before proof)
Source branches: exact-rational directed load \`_fraction_round\`; \`I.point/bounds\`; I add/sub/mul/div, negation, exp; \`psi_interval,q_interval\`; \`response\` below/above with no straddle in B1/B2/B3 pre-arrival; \`darbouxs\` dyadic width, gain and additive cumulative prefix; \`certify\` strict no-hit/first-hit bracket, transversality; \`structural_arrival/event_order\` exact topology/weight interval jump/event order; \`audit_certificate\` (re-compute proof data, no physics). \`I.sqrt\`, \`eta_mass_tail\` and optional derivatives are NOT reached by these positive-certificate paths. X1 straddle is UNQUALIFIED because active upper-endpoint gap can collapse.
Backend model: idealized unbounded correct directed p-bit binary MPFR exp/add/sub/mul/div plus exact GMP dyadic export (zero extra rounding); finite source agrees where no cap fires. Positive certificate r<=5/4 and all semantic endpoint operands bounded by H. For raw arbitrary-length exact rational numerator/denominator (used internally by \`_fraction_round\`), use the independent relative ratio-load bound <=8u, never a false bound on raw integer magnitudes. For p>=128, freeze local absolute roundoff \`r_K=2^24\` times 2^-p, nodewise endpoint Lipschitz \`L_K=2^80\`, cell dependency depth \`D_K=512\`, <=1024 directed rounded primitive evaluations per cell, <=1024 wrapper work, N_n<=1024*2^n+1024 and N_n>=2^n (nonempty prefix).
Construct **symbolic rather than fitted** per-box constants:
\`C_cell=r_K*sum_{j=0}^{D_K}L_K^j\`,
\`C_gain=C_cell\`,
\`C_prefix=C_gain+r_K\`,
\`C_wrap=C_cell\`,
\`C_star=max(C_cell,C_prefix,C_wrap)\`,
\`B_K=2*C_star\`.
Any error-bound claim relies on separate noncircular hull/gap proof. If D_K/primitive count or hull cannot be proved, box NOT QUALIFIED; do not replace constants post-output. Prefix error measured as maximum arithmetic endpoint displacement from exact NATURAL interval graph at the same partition, **not** the Darboux/range width.
Schedule p_n=128+8n, m_n=2^n: gamma=8>beta=1. No practical cost or global certification claim.

## Frozen post-proof deterministic validation (ONLY for analytically qualified boxes)
Use exact rational **diagonal samples** at lower, coordinatewise midpoint and upper corners of each box; do not call these samples the proof of the box.
B1 sample points:
(1,1,1,-1/16,-1/16,1/2,1/4),
(5/4,9/8,9/8,-1/32,-1/32,3/4,3/8),
(3/2,5/4,5/4,0,0,1,1/2).
B2:
(1,1,-1,0,0,4,1/2),
(5/4,17/16,-15/16,1/32,1/32,9/2,5/8),
(3/2,9/8,-7/8,1/16,1/16,5,3/4).
B3 (alpha,w,h,psi0):
(1,-1/8,1,-1/16),
(9/8,0,17/16,-1/32),
(5/4,1/8,9/8,0).
For B1/B2 test nmax in {0,2,4} at each sample; must give respectively CERTIFIED_NO_HIT / CERTIFIED_REGULAR_HIT on every call, physical/inclusion data check, and independently \`audit_certificate\` PASS. For B3 require 3/3 CERTIFIED_STRUCTURAL_ARRIVAL with e0 retained, strict comparison to competitor and successful proof replay, plus family spanning [-1/8,1/8] at each alpha sample, and prearrival subthreshold no-hit at each sample. Total planned positive calls 18 (B1/B2)+3*3 (B3 arrival singleton/family + prearrival)=27, no retrospective changes. For B1/B2 evaluate directed q/psi endpoint inclusion at segment times 0,L/2,L using 160-digit mpmath point calculations. Arithmetic excess vs exact natural graph is compared at selected rational/dyadic reference evaluations only; where absent report NOT INDEPENDENTLY ESTABLISHED, never invent a direct empirical B check. Qualifying proof constant may exceed usable floating-point range; comparison must use integer/rational logic.
Negative checks: X1 rejected analytically, X2 resource status as fixed, X3 topology mismatch rejected before certificate; corrupt one stored B2 prefix and require \`audit_certificate\` False. Record all checks and CPU/process exit. If a frozen expectation fails, classify FINITE VALIDATION FAILED, do not repair/retune this gate.

## Output
Proof/contract/report under research/numerical_engineering; machine-readable box inventory and symbolic constants, raw finite validation logs, full file SHA256, source identity and backend environment. Gate decision PASS only when B1/B2/B3 all analytically qualify and every specified post-proof check and negative control passes. No edits to RB-025/RB-027 or main. STOP — RETURN TO MASTER.
