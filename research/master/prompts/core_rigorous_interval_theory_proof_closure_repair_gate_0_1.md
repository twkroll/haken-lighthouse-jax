# MASTER Prompt — CORE Rigorous Interval Theory Proof-Closure Repair Gate 0.1

## Purpose

Repair two freeze-relevant proof-closure issues in the returned
\`CORE Rigorous Enclosure & Interval First-Hit Certification Theory Gate 0.1\`
before MASTER establishes a theory freeze.

The returned report is otherwise retained as the candidate theory artifact.
Do not reopen unrelated mathematics and do not execute numerics.

## Authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/command_protocol_v0_2.md
- RB-004
- RB-012
- RB-019
- RB-020
- RB-021
- RB-022
- RB-023
- returned candidate:
  \`research/core/rigorous_enclosure_interval_first_hit_theory_gate_0_1.md\`

RB-015 remains immutable SCIENTIFIC FAIL.

## Repair issue A — arithmetic convergence rate

### Problem

Section 18 claims that accumulated outward-rounding contribution is bounded by

\[
C 2^n 2^{-p_n},
\qquad
p_n=128+8n,
\]

but IR-A4 currently requires only that primitive interval overestimation tends to zero as precision increases.

That qualitative assumption alone does not imply an \(O(2^{-p})\) rate strong enough to control exponentially increasing operation count.

### Mandatory repair

Choose exactly one coherent route and prove it:

#### Route A1 — strengthen the arithmetic assumption

Replace/refine IR-A4 by an explicit uniform bounded-domain rate assumption sufficient for the chosen schedule \(p_n=128+8n\), e.g. a backend guarantee of the form

\[
\operatorname{wid}(\mathcal O_p(x))
\le C_K 2^{-p}
\]

or another explicitly summable precision-error bound on each compact domain \(K\), including the exponential primitive.

Then prove that total accumulated arithmetic overestimation tends to zero under the fixed operation-count growth.

OR

#### Route A2 — weaken the fixed precision schedule

Keep only qualitative shrinking assumptions but define a deterministic adaptive precision schedule \(p_n\) selected prospectively from a proved computable primitive-error bound so that

\[
N_n\,\varepsilon(p_n)\to0,
\]

where \(N_n\) bounds level-\(n\) arithmetic work.

The schedule must remain constructive and independent of observed certification outcomes.

Do not retain the current Section-18 proof unchanged.

### Required consequence

Recheck Sections 18, 19, 42 and 43 and the RIFC-0.1 algorithm statement so that:

- inclusion soundness remains independent of convergence rate;
- eventual certification has exactly the assumptions needed for enclosure widths to vanish;
- finite \(N_{\max}\) still returns fail-closed UNCERTIFIED/RESOURCE_EXHAUSTED when certification is not reached.

## Repair issue B — chart-radius overclaim

### Problem

Section 28 bounds motion of already indexed event times, transversality margins and boundaries, then concludes:

\[
\text{“Therefore the same ordinary labelled event chart is preserved.”}
\]

Those margin bounds alone do not exclude creation of an additional previously absent spike/event between indexed events.

The phrase “prevalidated parameter ball” risks making the statement circular if it already assumes chart preservation.

### Mandatory repair

Replace Section 28 by a non-circular statement.

At minimum distinguish:

1. **indexed-event margin preservation**:
   given rigorous neighborhood-wide derivative bounds for already-defined indexed event functions, the listed transversality/separation/boundary margins retain positive lower bounds inside a computable radius;

2. **full chart preservation**:
   this additionally requires a rigorous no-new-event completeness condition on every inter-event segment for every possible competing neuron/event, or another equivalent validated continuation hypothesis.

A full same-chart theorem may be retained only if its assumptions explicitly include sufficient neighborhood-wide segment certificates that rule out event insertion/deletion and are not merely the conclusion restated.

Otherwise freeze only a proposition for indexed-event margin preservation and keep full computable chart-radius certification OPEN.

### Structural-zero requirement

Structural-zero labelled arrivals remain part of all event lists and competing-event/no-new-event conditions.

Crossing a structural weight through zero must not change topology.

## Consistency audit

After repairing A and B:

- check every reference to Sections 18–19, 28–30, 42–43 and RIFC-0.1;
- confirm that the soundness theorem for emitted positive RIFC certificates remains valid;
- confirm whether eventual certification for strict deterministic next-event cases remains valid;
- identify any statement that depended on the overstrong chart-radius conclusion.

If another material contradiction is discovered, return CONDITIONAL/BLOCKED rather than silently broadening the gate.

## What must remain unchanged unless logically forced

Retain:

- IR-A1–IR-A3 and IR-A5;
- interval alpha propagation;
- structural-zero interval jump semantics;
- monotone threshold-safe response enclosure;
- dyadic interval Darboux phase-gain route;
- no-hit and regular-hit certificate logic;
- rigorous bracket transversality;
- event-order/horizon logic;
- fail-closed taxonomy;
- one constructive RIFC-0.1 algorithm;
- no library endorsement;
- grouped-event and interval-r/h open problems.

## Claim discipline

Every repaired statement must keep the existing labels:
THEOREM / PROVED, PROPOSITION, LEMMA, ASSUMPTION, INTERPRETATION, OPEN QUESTION.

## Forbidden

- no numerical execution;
- no interval-library benchmarking;
- no tolerance selection from outputs;
- no TR-27C execution;
- no \`2711xxx\` RNG;
- no APP-3;
- no v0.28 effect-bearing science;
- no novelty/manuscript claims.

## Required output

Create:

\`research/core/rigorous_enclosure_interval_first_hit_theory_proof_closure_repair_gate_0_1.md\`

Do not overwrite the original returned candidate.

The repair report must include:

1. exact replacement for IR-A4 / precision-schedule logic;
2. corrected convergence lemma and eventual-certification theorem assumptions;
3. corrected chart-radius/indexed-margin statement;
4. explicit no-new-event requirement for any full-chart preservation claim;
5. consistency audit of RIFC-0.1 soundness/termination;
6. list of every candidate section whose wording is superseded;
7. PASS recommendation for
   \`CORE Rigorous Enclosure & Interval First-Hit Certification Theory Freeze 0.1\`
   or CONDITIONAL/BLOCKED.

Update CORE STATUS to RETURN TO MASTER or BLOCKED.

## STOP

STOP — RETURN TO MASTER
