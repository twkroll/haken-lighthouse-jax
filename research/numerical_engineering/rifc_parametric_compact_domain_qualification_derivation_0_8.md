# NUM-ENG Gate 0.8 — symbolic Q-RIFC-K qualification on genuinely parametric compact boxes

Date: 2026-10-17. Analytical qualification PRECEDES any Gate-0.8 finite validation. Contract committed \`32ec665ffe2ba1d3dae243725aaca9e630e3d0e0\`.
Theoretical authority RB-029 Q-RIFC-K; source v0.2 SHA256 \`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202\`, backend MPFR 4.2.2/GMP 6.3.0. Frozen RB-025/RB-027 remain untouched. Every box here has **positive width in multiple coordinates**.

## A. Semantic enclosure proofs before any coarse B_K argument

### B1: globally below threshold
For any admissible alpha>0 and 0<=s<=L<=1, \`exp(-alpha*s)\` lies (0,1]. Given \`psi0,q0\` in [-1/16,0], \`psi(s)=exp(-alpha*s)(psi0+s q0)\` lies [-1/8,0], and h>=1. Thus the **whole** state interval over every dyadic cell has upper endpoint <=0<h, and the response is identically 0; no active division or reciprocal exists. All phase gains and prefixes vanish exactly, and d>=1/4 gives uniform no-hit margin >=1/4. This argument applies to the continuum parameter box, not just its three sample points. Directed endpoint arithmetic preserves nonpositivity of \`psi\`; finite-p rounding cannot select a positive/straddling response branch because h>=1.

### B2: uniformly positive response and strict first hit
For all s in [0,L], with L<=5 and alpha>=1, both \`psi0,q0\` are nonnegative, and:
\[
0\le\psi(s)=e^{-\alpha s}(\psi_0+s q_0)\le\frac1{16}+\frac5{16}=\frac38.
\]
As \(-1\le h\le-7/8\), the exact active gap obeys
\[
7/8\le\psi(s)-h\le11/8.
\]
On the box \(1\le r\le9/8\), response rate
\[
S(\psi(s))=\exp[-r/(\psi(s)-h)^2]
\ge e^{-72/49}>e^{-3/2}>1/5.
\]
The elementary inequality \(e^{3/2}<5\) makes this strict without a numerical fit. Hence \(G(L)>L/5\ge4/5>3/4\ge d\), while \(G(0)=0<d\). By strict positivity and continuity there is one unique regular first hit in the **interior** of the segment with transversal rate >1/5. The same argument excludes a collision/arrival competitor because B2 has fixed empty structural topology for the segment.

**Noncircular computed-interval safety.** Let u=2^(1-p)<=2^-127. For exact nonnegative inputs, all MPFR outward load/multiply/add/exp evaluations preserve nonnegative signs, even when exact operand is zero. The finite alpha subgraph has fewer than 32 sequential rounded operations, including repeated fraction endpoint loading; any nonzero ratio load has relative error <=8u and the remaining primitive endpoint relative error <=u. Therefore the bounded positive alpha-state graph has at most \((1+8u)^{32}<1+512u\) multiplicative upper widening. Thus its computed \`psi\` endpoints are in [0, (3/8)(1+512u)] which is <1/2. For arbitrary h in [-1,-7/8], its directed-rounded upper endpoint is below -7/8+8u. When \`response.top\` re-loads the endpoint and subtracts h, the loss of lower gap is at most 64u on this bounded graph. Consequently the **computed** positive gap for all p>=128 exceeds 7/8-64u>3/4>1/2, and both copies of its interval square have lower endpoint >1/4 (the interval multiplication is outward, and under its subnormal-free MPFR semantics at these magnitudes the gap-squared lower rounding differs by <16u). The active reciprocal is uniformly finite and bounded by 4 in magnitude; the exponent argument is within [-16,0] by a very generous margin. All computed semantic scalar nodes remain within H=2^18 independently of any desired final propagation constant. This prevents the circular "B_K proves its own prerequisites" reasoning.

The lower computed response bound is nonzero by the same strict gap; its upper endpoint cannot exceed 1 since its exponential argument is nonpositive, and RNDU exp(y)<=1 for y<=0 under correct rounding. Thus every cell response is in [0,1] and the source's strict bracket/transversality checks are meaningful on a continuum of singleton parameter inputs.

### B3: topology-fixed structural weight crossing zero
Structural edge \`e0\` is present for every w in [-1/8,1/8]. An arrival is always labelled t=1/2, and the next competitor is t=3/4, both strictly inside horizon=1. The event-order margin is 3/4-1/2=1/4; the boundary distance of the first arrival is 1/2. The edge jump is \(w\alpha^2\), bounded by \((1/8)(5/4)^2=25/128\) in absolute value. If w=0 the jump is the identity but its arrival label is **retained**. If the interval weight straddles zero, the uniform enclosure [-25/128,25/128] is outward-valid. Other box parameters \`h>=1,psi0<=0,q0=0\` ensure the separate prearrival segment is subthreshold/no-hit. **No postarrival propagation, whole tape or parameter-wide NNE-A certificate is asserted by this gate**, since that is a separate RB-030 implementation task.

## B. Finite branch cover and exact graph audit

The positive certificate branches used across B1/B2/B3 are: rational-to-MPFR directed loads; \`I.point/I.bounds\`; \`I._op\` add/sub/multiply/permitted divide; unary minus and exp; arrival-free \`psi_interval/q_interval\`; response below threshold B1/B3 or fully positive B2; \`darbouxs\` cell gain and additive prefix; \`certify\` no-hit or transversal-hit strict inequalities; \`structural_arrival\` and \`event_order\` labelled arrival/time comparisons; \`artifact_json/audit_certificate\` exact rational serialization and independent replay. The \`response\` straddling branch is **not reachable** on these qualified boxes; it is covered only by intentionally unqualified negative X1. Unused \`sqrt\`, tail-history and response-slope helpers are not included in the positive source graph. At every source resource violation, the gate retains fail-closed \`UNCERTIFIED_ARITHMETIC\`/\`RESOURCE_EXHAUSTED\`, not a positive certificate.

## C. Primitive constants, semantic hull and local Lipschitz rates

Define ideal directed MPFR precision p>=128 with unbounded resources, and \(u=2^{1-p}\). Exact dyadic export \`mpfr_get_z_2exp\` adds **zero** new numeric error. On a finite semantic result magnitude |z|<=H=2^18, correctly directed primitive rounding gives |fl_p(z)-z|<=u|z|. The source's rational input loader rounds separately the exact numerator and positive denominator (arbitrarily long raw integer strings allowed), then divides directed; for nonzero rationals its final relative ratio error is <=8u, independently of sizes of raw numerator/denominator integers (the semantic ratio is bounded, not the strings). For zero, loading is exact. Hence a safe per-rounded-node absolute error coefficient is
\[
r_K=2^{24},\quad \epsilon_v\le r_K 2^{-p}.
\]
On the noncircular compact perturbation tube established in A, endpoint map Lipschitz constants can be conservatively chosen:
- addition/subtraction <=2;
- multiplication <=2H=2^19;
- positive division <=4+H*16<2^23 using active squared divisor >=1/4;
- exp on nonpositive arguments <=1;
- exact endpoint min/max/hull/intersection <=1;
- negation <=1;
- structural labelled jump \`W*A*A\` uses the same bounded multiplication graph.

Therefore \`L_K=2^80\` safely dominates all nodewise maps. This oversized choice is symbolic and fixed before post-proof numerical checks. For branches with no active reciprocal, \`delta\` is not required and the same L_K remains an overbound.

The longest scalar dependency path through a single interval cell is <512 rounded primitive nodes (\`D_K=512\` chosen as a safe overbound). One interval product/division needs <=8 single-endpoint calls; each such call has <=7 directed MPFR primitives including up to two rational operand-load quotients. Direct source inspection yields <700 rounded primitives per cell and <1024 fixed wrapper primitives. Consequently
\[
2^n\le N_n\le1024\cdot2^n+1024
\]
for nonempty dyadic prefix computation. This counts rounded arithmetic operations, **not** GMP big-integer bit operations, Python string materialization, or elapsed time.

## D. Uniform prefixes for variable non-dyadic L and source-level rate proof

For each real L∈[1/2,5], each exact dyadic cell width is Δ=L/2^n, not necessarily a representable binary fraction. The interval loader \`I.point(Δ,p)\` outward-encloses exact Δ and adds <=8u relative. Nonnegative cell response upper is <=1. Each gain upper is therefore <=Δ(1+8u)^c for a fixed c<=8. The source prefix is a sequence of rounded **additions**, and if \(U_k\) is the upper bound after k cells, the source logic implies
\[
U_{k+1}\le(1+8u)(U_k+\Delta(1+8u)^8).
\]
With m=2^n, u=2^(1-128-8n), we have m u=2^(-127-7n). Thus \((1+8u)^{m+9}<2\) uniformly in n and the prefix bound \(0\le U_k\le2L\le10\) holds **without** invoking the global B_K. Similarly the lower endpoints stay nonnegative. This proves the required invariant arithmetic hull for arbitrary real L in the boxes.

Let \(L_K=2^{80}\), \(D_K=512\), \(r_K=2^{24}\), and write the exact frozen symbolic constants
\[
\Phi_K=\sum_{j=0}^{512}(2^{80})^j,\quad
C_{\rm cell}=2^{24}\Phi_K,\quad
C_{\rm gain}=C_{\rm cell},\quad
C_{\rm prefix}=C_{\rm gain}+2^{24},\quad
C_{\rm wrap}=C_{\rm cell},\quad
C_*=\max(C_{\rm cell},C_{\rm prefix},C_{\rm wrap}),\quad
B_K=2C_*.
\]
For the exact *natural interval arithmetic graph at the same partition*, excluding non-rounding range/dependency width, the nodewise recurrence \(e_{j+1}\le L_K e_j+r_K2^{-p}\) for at most D_K dependencies gives
\[
E_{\rm cell}\le C_{\rm cell}\,2^{-p}.
\]
The prefix recurrence is purely additive in the previous prefix, so after m cells:
\[
E_{\rm prefix}(n)\le m(C_{\rm gain}+r_K)\,2^{-p_n}
=2^n C_{\rm prefix}\,2^{-p_n}.
\]
Wrapper proof bookkeeping contributes at most \(C_{\rm wrap}2^{-p_n}\); hence by \(N_n\ge2^n\):
\[
\boxed{E_{\rm arith}(n)\le B_K N_n2^{-p_n}},\quad p_n=128+8n.
\]
Since \(N_n\le1024\,2^n+1024\),
\[
E_{\rm arith}(n)\le B_K(1024\,2^n+1024)2^{-128-8n}
\longrightarrow0.
\]
The schedule has \(\gamma=8>\beta=1\); it is an arithmetic excess theorem, not proof of a useful runtime or full event-tape completeness. Natural interval width and the RB-024 strict-margin/horizon requirements remain separate.

## E. Finite-source correspondence, exact role of parameter boxes

The symbolic statements above apply to **every exact real parameter choice in the described compact boxes** under the ideal directed arithmetic semantics, without replacing them with three sampled vertices. The unchanged executable Gate-0.6 source accepts exact rational specifications; for every rational point representable within all p/exponent/GMP/JSON/nmax limits, the same source DAG and directed rounding produce equal mathematical dyadic endpoints and classifications as the corresponding ideal finite member. This is *pointwise finite-source correspondence*, not an assertion that the Python API itself can consume arbitrary exact irrational parameters or propagate arbitrary parameter boxes in one call.

The finite source still has \`p<=8192\`, \`nmax<=16\` and GMP/exponent/integer size limits. A resource exception fails closed. The ideal n->infinity theorem is not a finite-machine guarantee.

## F. Negative analytical controls — prospective dispositions

X1: upper active endpoint b∈(0,1/32] approaches h=0 from above; inf_b(b-h)=0, so the above-threshold reciprocal source graph has no uniform positive \(\delta_K\). **THEOREM ASSUMPTION FAILED**. The composed smooth response alone cannot qualify its singular intermediate.
X2: deliberately finite nmax=0 on the predeclared narrow pulse should return **RESOURCE_EXHAUSTED / UNCERTIFIED**, not a physical no-hit.
X3: removing structural e0 at exactly w=0 changes the labelled arrival graph and invalidates the fixed-topology correspondence. **IMPLEMENTATION/GRAPH MISMATCH** for that hypothetical alternative, while the real B3 source retains e0.

## G. Pre-validation classification

B1: **PARAMETRIC DOMAIN QUALIFIED** — uniform subthreshold / no-hit, no active reciprocal.
B2: **PARAMETRIC DOMAIN QUALIFIED** — uniform active gap and interior transversal first hit.
B3: **PARAMETRIC DOMAIN QUALIFIED** — fixed labelled structural arrival and separately subthreshold prearrival segment (not full tape).
X1: THEOREM ASSUMPTION FAILED (intentionally unqualified).
X2: RESOURCE-LIMITED / QUALIFIED IDEALLY in finite tester.
X3: IMPLEMENTATION/GRAPH MISMATCH (hypothetical graph deletion rejected).

All classifications are **analytical and recorded before any Gate-0.8 finite validation**. A failed subsequent frozen finite validation must be disclosed as FINITE VALIDATION FAILED without changing these parameters. No RB-025/RB-027 source, main, CORE, RIFC-TAPE or APP-3 work is authorized.
