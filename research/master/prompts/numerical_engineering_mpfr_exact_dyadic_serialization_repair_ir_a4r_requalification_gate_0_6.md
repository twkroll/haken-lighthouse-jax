# MASTER Prompt — NUM-ENG MPFR Exact-Dyadic Serialization Repair & IR-A4-R Requalification Gate 0.6

## Purpose

Prospectively repair the specific Gate-0.5 source-level blocker while preserving RB-025 as an immutable finite-soundness baseline, then requalify IR-A4-R on a frozen compact domain.

The sole authorized repair target is the MPFR-to-exact-dyadic serialization path responsible for the precision-independent \(2^{-2048}\) floor identified in RB-026.

This gate must not silently edit, replace or relabel RB-025.

It must create a new versioned repair implementation and validate it separately.

## Mandatory authorities

Read and obey:

- `PROJECT_GOVERNANCE.md`
- `research/master/command_protocol_v0_2.md`
- `research/master/parallel_engineering_policy_v0_1.md`
- RB-019
- RB-021
- RB-023
- RB-024
- RB-025
- RB-026
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

`engineering/numerics-v0.1`.

The physical authority remains:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

## Immutable baseline rule

The RB-025 subtree/source must remain byte-identical.

In particular, do not overwrite:

`software/numerical_engineering/rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py`.

Create a new versioned Gate-0.6 repair subtree.

Any source hash change to the RB-025 file itself is an automatic governance failure.

## Pre-repair / pre-execution contract

Before modifying source or producing Gate-0.6 validation outputs, create and commit:

`research/numerical_engineering/rifc_exact_dyadic_repair_requalification_contract_0_6.md`.

The contract must freeze:

1. exact RB-025 source SHA-256 and blob SHA;
2. exact MPFR/GMP/backend identities;
3. exact proposed serialization API/path;
4. exact proof that the new conversion is an exact representation of the already rounded MPFR value, not an additional numerical approximation;
5. exact behavior for zero, signed values, tiny values, large exponents and unsupported resource cases;
6. exact resource/fail-closed limits for materializing dyadic integers/rationals;
7. exact repaired source path/version;
8. exact compact IR-A4-R domain \(K_{0.6}\);
9. exact expression-graph inventory;
10. exact primitive-rate proof strategy;
11. exact whole-expression \(B_K\) propagation strategy;
12. exact operation-count bound strategy;
13. exact precision/refinement schedule;
14. exact finite regression fixtures;
15. exact negative controls;
16. exact PASS / BLOCKED / bounded-result criteria;
17. exact artifact/manifests required.

No repair design, domain, proof constant, test fixture or classification threshold may be changed after Gate-0.6 outputs are inspected.

## R1 — exact dyadic serialization repair

Replace the Gate-0.5 fixed-floor behavior in the **new versioned implementation** with an exact MPFR-to-dyadic export.

Preferred route:

- use MPFR/GMP primitives such as an exact significand/exponent extraction (for example `mpfr_get_z_2exp`) and exact GMP integer export;

or another route only if it is proven equivalent.

The repaired conversion must satisfy:

for every finite MPFR value \(y_p\) produced after directed rounding, the serialized rational equals exactly

\[
y_p = z\,2^e
\]

for some exact integer \(z\) and integer exponent \(e\).

There must be no precision-independent artificial floor.

Do not use:

- Python float;
- decimal round-trip;
- `math.exp`;
- unproved `nextafter`;
- fixed underflow clamps;
- precision-independent widening.

## R2 — resource safety

Exact serialization of extremely small/large dyadics may create large Python integers.

Freeze finite resource guards prospectively.

If exact export exceeds those guards, return a fail-closed arithmetic/resource class.

Never replace an exact export by an inward approximation.

If a resource guard uses conservative outward fallback, that fallback must be analyzed separately and must not be included in IR-A4-R unless it also satisfies the required rate.

## R3 — finite-soundness regression after repair

Re-run the complete Gate-0.4 finite-soundness acceptance set required by the frozen Gate-0.6 contract.

At minimum include:

- the 26 Gate-0.4 RIFC tests;
- the 28 frozen compatibility tests;
- all six saved positive certificate replays or their versioned Gate-0.6 equivalents;
- all Gate-0.5 negative-control points;
- exact tiny positive/negative serialization tests across the predeclared precision set.

The new implementation must preserve all positive finite-soundness/fail-closed semantics before requalification can PASS.

RB-025 itself remains untouched even if Gate 0.6 passes.

## R4 — exact Gate-0.5 counterexample closure

On the exact prospectively frozen Gate-0.5 point

\[
\exp(-10000),
\]

show that the repaired exact-dyadic serialization no longer returns the fixed interval

\[
[0,2^{-2048}]
\]

solely due to serialization.

For each predeclared precision, record the exact dyadic directed endpoints.

Demonstrate from source/proof, not empirical fitting, that the old precision-independent floor has been removed.

## Q1 — primitive-rate requalification

Derive the bounded-domain precision-rate result for the repaired primitive graph.

Separate:

1. MPFR correctly-rounded arithmetic error;
2. exact dyadic serialization, which should contribute zero additional arithmetic error once the MPFR value exists;
3. interval dependency/range width, which is not arithmetic excess.

For every primitive appearing in a positive RIFC certificate, derive an explicit compact-domain bound of the required form or a stronger sufficient bound.

## Q2 — response-graph requalification

Re-derive the threshold-safe Lighthouse response rate on the frozen Gate-0.6 domain.

Above threshold, freeze explicit positive distance-from-threshold conditions needed to bound reciprocal-square sensitivity.

Threshold-straddling logic must remain monotone and singularity-safe.

Do not shrink the domain after results.

## Q3 — alpha propagation / Darboux propagation

Re-derive the arithmetic excess propagation for:

\[
q(s)=e^{-\alpha s}q_0,
\qquad
\psi(s)=e^{-\alpha s}(\psi_0+s q_0),
\]

and the dyadic Darboux cell/prefix expression graph.

Prove an explicit operation-count overbound:

\[
N_n\le a2^n+b.
\]

## Q4 — whole-expression IR-A4-R requalification

Produce exactly one of two outcomes.

### PASS route

Prove on the prospectively frozen Gate-0.6 compact domain:

\[
E_{\rm arith}(n)
\le
B_KN_n2^{-p_n},
\]

with finite \(B_K\), independent of \(n\) and \(p_n\), and with

\[
p_n=128+8n.
\]

Then prove:

\[
E_{\rm arith}(n)\to0.
\]

### NO-GO route

Provide a rigorous source-level counterexample showing that no such finite \(B_K\) can exist for the repaired expression graph/domain.

A NO-GO is a valid return and must not be repaired again inside the same gate.

## Q5 — source/proof correspondence

Audit the complete repaired positive-certificate expression graph.

Every operation/branch capable of affecting a positive certificate must appear in the rate derivation.

Any unmodeled approximation, clamp, serialization widening or resource fallback that can enter a positive certificate is a BLOCKER.

## Q6 — validation only after analytical qualification

Only if Q4 PASS is established:

- run the predeclared precision-rate consistency checks;
- verify observed arithmetic excess remains below the proved bounds;
- do not infer/fine-tune \(B_K\) from observed data.

## Q7 — eventual-certification requalification

Only if Q4 PASS is established:

run prospectively frozen strict-margin:

- CERTIFIED_NO_HIT;
- CERTIFIED_REGULAR_HIT;

fixtures across the predetermined refinement schedule.

Require eventual positive certification within the fixture-specific predeclared level envelope.

Also include deliberately insufficient finite \(N_{\max}\) controls returning:

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

This validates the implementation of the RB-024 theorem; it does not replace the analytical proof.

## Q8 — hard finite nmax distinction

The production/test API may retain a finite resource limit.

The Gate-0.6 report must distinguish:

- mathematical eventual certification under unbounded theoretical refinement;
- a finite software budget that can still return RESOURCE_EXHAUSTED.

Do not claim that finite `nmax` itself proves eventual certification.

## Q9 — unchanged non-goals

Do not implement or claim:

- full sequential multi-event tape certification;
- parameter-box NNE-A;
- full-chart radius;
- performance/scaling work;
- TR-27C;
- APP-3;
- stochastic scientific experiments.

## Result classes

Every material result must be classified:

- SERIALIZATION REPAIR VALIDATED;
- FINITE SOUNDNESS PRESERVED;
- IR-A4-R ESTABLISHED;
- IR-A4-R NOT ESTABLISHED;
- EVENTUAL-CERTIFICATION IMPLEMENTATION VALIDATED;
- REPAIR-REQUIRED;
- BLOCKED;
- DEFERRED.

## PASS hierarchy

### Full Gate-0.6 PASS

Requires all of:

1. prospective contract committed before repair/output;
2. RB-025 source byte-identical;
3. exact-dyadic serialization repair proven and validated;
4. finite-soundness regression PASS;
5. Gate-0.5 fixed-floor counterexample closed;
6. primitive/source correspondence complete;
7. IR-A4-R analytically established on frozen \(K_{0.6}\);
8. eventual-certification validation fixtures PASS;
9. no post-output retuning.

### Repair-only bounded result

If exact-dyadic repair and finite-soundness preservation PASS but IR-A4-R still cannot be established:

return

`SERIALIZATION REPAIR VALIDATED / IR-A4-R NOT ESTABLISHED`

and do not claim eventual certification.

### BLOCKED

If exact finite outward inclusion cannot be preserved, RB-025 is not altered; Gate 0.6 returns BLOCKED.

## Required outputs

On `engineering/numerics-v0.1`, create:

1. `research/numerical_engineering/rifc_exact_dyadic_repair_requalification_contract_0_6.md`
2. `research/numerical_engineering/rifc_exact_dyadic_repair_requalification_gate_0_6.md`
3. a new versioned implementation subtree, e.g.
   `software/numerical_engineering/rifc_interval_gate_0_6/`
4. exact serialization proof/derivation artifact;
5. IR-A4-R derivation artifact;
6. deterministic regression/rate/eventual-certification logs as permitted by the analytical prerequisites;
7. byte-level manifests/provenance.

Update:

`research/numerical_engineering/STATUS.md`

to RETURN TO MASTER or BLOCKED.

## Recommendation

If full PASS, recommend a new bounded engineering freeze for:

- repaired exact-dyadic RIFC finite soundness;
- qualified IR-A4-R on the frozen Gate-0.6 domain;
- validated eventual-certification implementation semantics.

Do not modify or replace RB-025.

## Forbidden

- no editing RB-025 source/file;
- no post-output domain shrinking;
- no empirical fitting of \(B_K\);
- no protected RNG;
- no TR-27C;
- no APP-3;
- no stochastic benchmark;
- no scientific speedup/scaling claim;
- no executable source merge to `main`;
- no novelty/manuscript claims.

## STOP

STOP — RETURN TO MASTER
