# CORE Rigorous Enclosure & Interval First-Hit Certification Theory Freeze 0.1

Date: 2026-10-16
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-024

## Authority

MASTER jointly freezes:

1. \`research/core/rigorous_enclosure_interval_first_hit_theory_gate_0_1.md\`
   - candidate blob SHA: \`ca2773d3845f0a36053df21c23fa9af7b4ce8759\`
2. \`research/core/rigorous_enclosure_interval_first_hit_theory_proof_closure_repair_gate_0_1.md\`
   - repair blob SHA: \`a20937a65e77b4c16d6f140de30154b7f828aa62\`

The repair is the mandatory superseding authority for every section listed as superseded in its Part VI.

The original candidate remains audit history.

## Frozen scope

RB-024 freezes one constructive rigorous interval-certification theory layer for ordinary Lighthouse first-hit/event-chart certification.

No numerical interval implementation is frozen here.

## 1. Interval arithmetic assumptions

The finite-certificate soundness layer requires inclusion-valid interval arithmetic with:

- outward-directed arithmetic for +, -, multiplication and permitted division;
- rigorous interval exponential;
- fail-closed behavior on overflow/NaN/loss of inclusion;
- no silent substitution of ordinary scalar arithmetic.

The repaired precision/convergence assumption is:

### IR-A4-R

On each compact admissible domain K used by one RIFC computation, the backend must provide a uniform primitive excess-width bound of the form

\[
\operatorname{excwid}(\mathcal O_p(x))
\le C_K 2^{-p},
\]

together with a finite propagation bound

\[
E_{\rm arith}(N,p)
\le B_K N 2^{-p}
\]

for the fixed RIFC expression family.

These are implementation proof obligations, not empirical tolerances.

## 2. Fixed refinement schedule

For eventual-certification claims, RIFC-0.1 uses

\[
p_n=128+8n,
\qquad
m_n=2^n
\]

with deterministic dyadic refinement.

The primitive-operation count obeys

\[
N_n\le a2^n+b,
\]

so under IR-A4-R,

\[
E_{\rm arith}(n)
\le
B_K(a2^n+b)2^{-(128+8n)}
\to0.
\]

This closes the convergence-rate gap identified by MASTER.

Finite positive certificate soundness does not require the convergence rate once a strict outward-valid certificate has already been produced.

## 3. Rigorous interval alpha propagation

On an arrival-free interval,

\[
q(s)=e^{-\alpha s}q_0,
\qquad
\psi(s)=e^{-\alpha s}(\psi_0+s q_0)
\]

are enclosed by outward-valid interval compositions.

Subdivision preserves inclusion.

Optional monotonicity sharpening is valid only when the derivative-sign interval excludes zero.

## 4. Structural-zero interval semantics

Structural topology is fixed independently of the numerical coupling value.

A structural edge remains present even when its weight interval contains zero.

At its labelled arrival,

\[
Q_i^+
=
Q_i^-+W_e A^2.
\]

If

\[
W_e=[0,0],
\]

the jump is the identity but the labelled arrival remains in the event tape and all ordering/boundary logic.

Crossing zero does not alter topology.

## 5. Rigorous response enclosure

The frozen response is enclosed monotonically in three cases:

- fully below threshold;
- threshold-straddling;
- fully above threshold.

Threshold-straddling intervals are handled by the smooth monotone splice rather than by evaluating a reciprocal expression at the threshold.

Derivative enclosures may use the RB-022 global derivative bounds.

## 6. Primary phase-gain route

The only frozen integration route is:

\[
\boxed{\text{dyadic interval Darboux/Riemann enclosure}}
\]

using outward-valid state and response intervals.

For each cell \(I_k\),

\[
\mathcal G_k
=
\Delta_k R_k
\]

and cumulative outward prefix sums enclose the exact accumulated phase gain.

No alternative validated quadrature family is frozen by RB-024.

## 7. Certified no-hit

If

\[
\overline G_m<\underline d,
\]

then the represented trajectory family has no first hit on the certified segment.

Output:

\`CERTIFIED_NO_HIT\`.

The positive certificate retains the strict margin

\[
\gamma_{\rm nohit}
=
\underline d-\overline G_m>0.
\]

## 8. Certified regular hit

If a prefix bracket satisfies

\[
\overline G_j<\underline d,
\qquad
\underline G_k>\overline d,
\]

and every cell in the bracket has response lower bound

\[
\underline r_\ell\ge\nu_{\rm cert}>0,
\]

then every represented trajectory has a unique transversal first hit in the bracket.

Output:

\`CERTIFIED_REGULAR_HIT\`.

The certificate includes the hit bracket and rigorous transversality lower bound.

## 9. Eventual certification under strict margins

For singleton deterministic inputs on a compact admissible domain, under IR-A4-R and no arithmetic proof failure:

- strict no-hit cases are eventually certified under refinement;
- strict regular-hit cases are eventually certified under refinement.

A finite resource budget does not inherit this eventual guarantee.

If \(N_{\max}\) is exhausted first, the required output remains:

\`RESOURCE_EXHAUSTED / UNCERTIFIED\`.

## 10. Rigorous transversality

Given a certified first-hit bracket \(B\), if the outward response enclosure satisfies

\[
\underline\nu_B>0,
\]

then the exact event is rigorously transversal.

If the input enclosure still straddles threshold and the lower response bound is zero, the current method is inconclusive rather than negative.

## 11. Event ordering and boundaries

For rigorous event-time intervals

\[
E_a=[\underline t_a,\overline t_a],
\qquad
E_b=[\underline t_b,\overline t_b],
\]

strict separation

\[
\overline t_a<\underline t_b
\]

certifies the event order.

Interval overlap alone means:

\`UNCERTIFIED_EVENT_ORDER\`

and does not prove collision.

The same principle applies to spike/arrival order, arrival/arrival order, horizon boundaries and initial boundaries.

Structural-zero arrivals participate fully.

## 12. Arrival-before-spike certification

If the hypothetical pre-arrival flow extended to the latest possible arrival remains rigorously below the phase section,

\[
\overline G_{\rm pre}(\overline A_e)<\underline d,
\]

then no spike can precede that arrival.

The remaining phase-gap lower bound produces a conservative post-arrival time-separation lower bound via the global phase-rate bound.

## 13. Indexed-event margin preservation

The repaired theory distinguishes indexed-event motion from complete chart preservation.

Given rigorous neighborhood-wide derivative bounds for already-defined indexed event functions, one may compute

\[
\rho_{\rm indexed}
=
\min
\{\rho_{\rm tr},\rho_{\rm sep},\rho_{\rm bdry},R\},
\]

such that already indexed events retain positive fractions of their transversality, separation and boundary margins.

This theorem does not state that these are the only events.

## 14. Full ordinary-chart preservation

Full chart preservation additionally requires an independent neighborhood-wide no-new-event condition NNE-A on every inter-event segment.

NNE-A requires, uniformly over the parameter ball:

- enumeration of all structural arrivals;
- no-hit certificates for nonwinning spike candidates;
- certified presence/regularity of the designated next spike where relevant;
- certified ordering when the next event is an arrival;
- boundary exclusion;
- post-event enclosure closure for induction.

Only under both indexed-margin preservation and NNE-A may one assert full ordinary-chart preservation.

If a radius \(\rho_{\rm NNE}\) is independently certified, then

\[
\rho_{\rm chart}
=
\min\{\rho_{\rm indexed},\rho_{\rm NNE}\}
\]

is a valid full-chart lower radius.

No universal automatic nontrivial \(\rho_{\rm NNE}\) construction is frozen.

The general full parameter-box chart-radius problem remains OPEN.

## 15. Fail-closed taxonomy

The frozen certification taxonomy includes:

- CERTIFIED_NO_HIT;
- CERTIFIED_REGULAR_HIT;
- CERTIFIED_EVENT_ORDER;
- CERTIFIED_STRUCTURAL_ARRIVAL;
- CERTIFIED_ORDINARY_CHART;
- ASSUMPTION_VIOLATED;
- STRICT_MARGIN_ABSENT;
- ENCLOSURE_INCONCLUSIVE;
- RESOURCE_EXHAUSTED;
- UNCERTIFIED_ARITHMETIC;
- ORDINARY_CHART_INVALID;
- UNSUPPORTED_CASE;
- MATHEMATICAL_CONTRADICTION.

For a parameter-family \`CERTIFIED_ORDINARY_CHART\`, explicit inter-event no-new-event completeness is mandatory.

## 16. RIFC-0.1

RB-024 freezes the deterministic constructive algorithm:

\`RIFC-0.1 — Rigorous Interval First-Hit Certifier\`.

Its core structure is:

1. validate supported inputs and topology;
2. choose dyadic level \(n\) and precision \(p_n=128+8n\);
3. propagate outward interval alpha states;
4. construct threshold-safe response enclosures;
5. construct outward prefix phase-gain enclosures;
6. test strict no-hit certificate;
7. otherwise search deterministic regular-hit brackets;
8. combine spike brackets, labelled structural arrivals and horizon intervals;
9. certify the next event only through strict outward inequalities;
10. refine or return fail-closed classification.

A scalar root estimate alone is not a certificate.

## 17. Positive certificate proof obligations

A later implementation may emit a positive certificate only if it can retain/reconstruct:

- exact input interval endpoints;
- topology signature;
- arithmetic precision/backend identity;
- rigorous exponential contract;
- every cell state enclosure;
- every response enclosure;
- every outward prefix gain interval;
- phase-gap interval;
- bracket inequalities;
- transversality lower bound;
- competing event intervals;
- event-separation/boundary inequalities;
- structural-zero arrivals/jump enclosures;
- absence of arithmetic proof failure.

## 18. Unsupported/open cases

RB-024 does not solve:

- grouped simultaneous-event charts;
- parameter-dependent topology;
- interval uncertainty in response parameters \(r,h\);
- nonsmooth response variants;
- adaptive/state-dependent delays;
- infinite-history global certification without explicit summability/density hypotheses;
- general automatic parameter-box no-new-event certification;
- sharp/global chart-radius computation;
- formal proof-assistant verification;
- efficient alternative validated quadrature families.

## 19. Relationship to previous freezes

RB-024 strengthens the theory layer above RB-022/RB-023.

It does not retroactively promote RB-023 float64 finite validation into rigorous interval proof.

RB-019/RB-021 engineering tolerances remain engineering evidence.

RB-020 remains a separate frozen but unexecuted v0.27c contract.

## 20. Governance boundaries

RB-024 does not:

- alter RB-015 SCIENTIFIC FAIL;
- execute TR-27C;
- create any \`2711xxx\` RNG object;
- authorize v0.27c confirmatory execution;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- create numerical speedup/scaling claims;
- endorse a specific interval library;
- authorize novelty/manuscript claims.

## STOP

RB-024 is a scientific-theory freeze only.

STOP — FROZEN / STABLE SCIENTIFIC THEORY
