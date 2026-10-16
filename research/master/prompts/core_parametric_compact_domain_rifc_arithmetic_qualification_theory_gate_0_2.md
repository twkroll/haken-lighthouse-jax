# MASTER Prompt — CORE Parametric Compact-Domain RIFC Arithmetic Qualification Theory Gate 0.2

## Purpose

Generalize the fixture-specific RB-028 arithmetic qualification into a symbolic theorem for a class of compact ordinary RIFC domains.

The goal is to avoid proving IR-A4-R separately for each finite fixture family.

This is a THEORY gate only.

No executable source changes or numerical experiments are authorized.

## Mandatory authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/command_protocol_v0_2.md
- RB-004
- RB-012
- RB-022
- RB-024
- RB-025
- RB-026
- RB-027
- RB-028
- current MASTER / CORE / NUM-ENG STATUS files.

RB-015 remains immutable SCIENTIFIC FAIL.

## Main question

Find explicit sufficient symbolic conditions on a compact RIFC domain \(K\) and fixed positive-certificate expression graph \(\mathcal G\) under which one can guarantee a finite constant \(B_K\) satisfying

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n},
\]

with

\[
p_n=128+8n,\qquad N_n\le a2^n+b,
\]

and hence

\[
E_{\rm arith}(n)\to0.
\]

The theorem must separate:

- model/range assumptions;
- arithmetic-backend assumptions;
- graph/depth assumptions;
- interval dependency/range width;
- arithmetic excess;
- finite-machine resource policy.

## T1 — abstract arithmetic model

Define a general directed-rounding primitive model sufficient for:

- rational endpoint load;
- +, -, multiplication;
- nonzero division;
- exponential;
- exact dyadic serialization;
- comparisons/min/max/hull/intersection;
- optional sqrt only if explicitly supported.

State exact assumptions needed for a primitive excess rate proportional to \(2^{-p}\).

Do not tie the theorem to GNU MPFR unless a source-specific corollary is being stated.

## T2 — compact semantic hull

Define sufficient conditions guaranteeing all semantic interval endpoints in the positive-certificate graph remain in a compact hull

\[
|x|\le H_K.
\]

This must be proved independently of the final coarse whole-graph arithmetic bound.

Allow branchwise hulls if more natural.

## T3 — divisor / threshold separation

For reciprocal response branches, formulate an explicit positive lower margin

\[
x-h\ge\delta_K>0
\]

or an equivalent branchwise divisor bound.

The theorem must explain:

- why no uniform arithmetic Lipschitz constant is available when above-threshold inputs may approach \(h\) arbitrarily closely;
- how threshold-straddling monotone branches avoid singular reciprocal evaluation;
- how fully subthreshold branches are handled.

## T4 — source-graph structure

Let the positive-certificate endpoint graph have:

- finite local DAG depth \(D_K\);
- bounded primitive count per cell \(c_K\);
- prefix update structure.

Derive symbolic operation-count constants

\[
N_n\le a_K2^n+b_K.
\]

Separate arithmetic primitive count from bit complexity / memory complexity.

## T5 — nodewise arithmetic propagation

Derive a symbolic recurrence from:

- primitive local rounding excess \(r_K2^{-p}\);
- endpoint-map Lipschitz majorants \(L_K\);
- finite local depth \(D_K\).

Produce an explicit finite cell constant \(C_{\rm cell}(K)\).

Avoid using an already-global bound to justify the hull/divisor assumptions.

## T6 — prefix accumulation theorem

Characterize when prefix accumulation is additive rather than repeatedly nonlinearly amplified.

For RIFC Darboux accumulation, derive a symbolic bound of the form

\[
E_{\rm prefix}(n)
\le
C_{\rm prefix}(K)2^n2^{-p_n}.
\]

State exact structural assumptions under which this is valid.

## T7 — parametric IR-A4-R theorem

Prove a theorem of the form:

If K satisfies compact-hull, divisor-separation, backend-rate, fixed-graph and additive-prefix assumptions, then there exists an explicit finite

\[
B_K=B(H_K,\delta_K,L_K,D_K,c_K,\ldots)
\]

such that

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n}.
\]

Then show convergence under any schedule

\[
p_n=p_0+\gamma n
\]

with the sharp or sufficient condition on \(\gamma\) relative to the cell-count growth.

Specialize to \(\gamma=8\).

Do not hard-code RB-028's enormous \(2^{65536}\) except as a consistency corollary.

## T8 — exact-dyadic serialization corollary

State formally that exact serialization of an already directed-rounded endpoint adds zero arithmetic excess.

Distinguish this from the finite resource cost of materializing the exact dyadic.

## T9 — finite-source correspondence theorem

Formalize conditions under which a resource-bounded executable source is a finite truncation/member of an idealized unbounded arithmetic family.

The theorem must preserve:

- exact branch semantics;
- identical rounding modes;
- exact serialization;
- fail-closed resource exits.

It must explicitly reject the inference:

\[
\text{idealized eventual certification}
\Rightarrow
\text{finite production always certifies}.
\]

## T10 — RB-028 recovery check

Show that K01–K06 satisfy the new theorem assumptions and that RB-028 becomes a corollary / instance of the parametric theorem.

Do not alter RB-028.

## T11 — failure modes and boundaries

Classify domains where the theorem cannot apply, including at least:

- arbitrarily vanishing above-threshold gap;
- unbounded semantic endpoint hull;
- denominator approaching zero;
- changing expression-graph topology/branches not covered by a finite branch partition;
- unsupported transcendental primitive rate;
- non-additive recurrent accumulation without a suitable stability bound.

Label these as theorem-assumption failures, not implementation failures.

## T12 — implementation-facing qualification recipe

End with one finite recipe that a later NUM-ENG gate can use to qualify a new compact domain:

1. define K;
2. establish semantic hull;
3. establish divisor/threshold margins;
4. enumerate graph branches;
5. bound local depth/count;
6. instantiate primitive constants;
7. compute symbolic \(B_K\);
8. verify finite-source correspondence;
9. only then run finite consistency checks.

This recipe is prospective methodology, not executed evidence.

## Claim discipline

Every result must be labelled:

- THEOREM / PROVED;
- PROPOSITION;
- LEMMA;
- ASSUMPTION;
- COROLLARY;
- INTERPRETATION;
- OPEN QUESTION.

## Forbidden

- no executable source modification;
- no numerical experiments;
- no empirical fitting of constants;
- no protected RNG;
- no TR-27C;
- no APP-3;
- no full multi-event implementation;
- no novelty/manuscript claims.

## Required output

Create:

`research/core/parametric_compact_domain_rifc_arithmetic_qualification_theory_gate_0_2.md`

and update CORE STATUS to RETURN TO MASTER or BLOCKED.

The report must contain:

- symbolic theorem assumptions;
- explicit \(B_K\) construction;
- schedule condition on precision growth;
- finite-source correspondence theorem;
- RB-028 corollary;
- failure-domain classification;
- implementation-facing qualification recipe.

## Decision

PASS only if the result genuinely generalizes RB-028 beyond a finite fixture list without silently assuming its conclusion.

If the theorem can only be proved under assumptions equivalent to manually replaying the entire fixture-specific proof, return CONDITIONAL/BLOCKED.

## STOP

STOP — RETURN TO MASTER
