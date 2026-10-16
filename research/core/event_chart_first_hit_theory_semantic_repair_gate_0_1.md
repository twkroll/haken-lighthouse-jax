# CORE Event-Chart / Structural-Zero Semantic Repair Gate 0.1

Date: 2026-10-16  
Status: PASS — STRUCTURAL-ZERO / EVENT-CHART SEMANTICS REPAIRED; ORIGINAL CANDIDATE PRESERVED AS AUDIT HISTORY

## 1. Authority and exact repair scope

This gate executes:

\`research/master/prompts/core_event_chart_first_hit_theory_semantic_repair_gate_0_1.md\`.

Canonical identity at gate start:

- repository: \`twkroll/haken-lighthouse-jax\`
- branch: \`main\`
- \`main\` HEAD: \`53b02ca612dd1ab9b493e6bac84288b76b4ae01b\`
- CORE STATUS blob: \`549847b08592859f92aed7a041778a5aae8b565d\`
- MASTER STATUS blob: \`ca10af1072be839ffc39a19d5ff38b8ebb2edc53\`
- MASTER project-status blob: \`fdd8b9818d24363ece057feee5c466d4dbf1ad6a\`
- MASTER decision-log blob: \`0f5e6c4abff1df4de7030723ae797c49bc982f6d\`
- repair prompt blob: \`[resolved from canonical file at gate execution]\`
- returned candidate theory blob: \`a889d19d0679f61f75750db1cf8c51669857ade4\`
- RB-019 Numerical Engineering Freeze blob: \`68c674e50772620960b5e52092b9f6cd606d8f42\`
- RB-021 Numerical Engineering Freeze 0.2 blob: \`88cac66ae5dbeb4f5ca9d006fcca2d2c4c792b0b\`
- RB-020 v0.27c contract remains frozen and parked.

RB-015 remains immutable \`SCIENTIFIC FAIL\`.

This is a **narrow semantic repair**. The original returned candidate

\`research/core/event_chart_first_hit_theory_gate_0_1.md\`

is not overwritten and remains audit history.

No numerical validation, TR-27C execution, \`2711xxx\` RNG creation, APP-3 execution, scaling experiment, effect-bearing v0.28 work, novelty positioning, or manuscript claim work occurred.

---

## 2. Repair diagnosis

The returned candidate contained one canonical inconsistency:

> structural zero-weight edges were deleted from the ordinary event chart.

That statement conflicts with the topology-fixed structural-coordinate convention already accepted in the numerical lineage.

The repaired convention is:

### SZ-1 — topology is independent of coupling value

**Label:** ASSUMPTION / CANONICAL SEMANTIC REPAIR.  
**Provenance:** MASTER-AUTHORIZED REPAIR + RB-019/RB-021 CONSISTENCY.

Let \(E\) be the fixed structural directed-edge set.

For every \(e=(j\to i)\in E\), edge existence is independent of the numerical value of \(w_{ij}\).

Thus \(w_{ij}=0\) does **not** remove the edge.

### SZ-2 — structural launch and arrival remain present at zero weight

**Label:** PROPOSITION / PROVED UNDER FIXED-TOPOLOGY EVENT SEMANTICS.  
**Provenance:** DERIVATION HERE.

For every structural edge \(e=(j\to i)\) and every source spike \(T_j^m\), the labelled delayed arrival is

\[
A_{ij}^m=T_j^m+\tau_{ij}.
\tag{SZ.1}
\]

This labelled arrival exists for all admissible \(w_{ij}\), including \(w_{ij}=0\).

The alpha-state jump map is

\[
q_i^+=q_i^-+w_{ij}\alpha^2.
\tag{SZ.2}
\]

At exactly zero weight,

\[
q_i^+=q_i^-.
\tag{SZ.3}
\]

Therefore the state jump is the identity, but the labelled structural arrival remains an event in the topology-fixed tape.

### SZ-3 — physical state equivalence does not imply tape equivalence

**Label:** PROPOSITION / PROVED.  
**Provenance:** DERIVATION HERE.

Consider two otherwise identical systems:

1. a topology-fixed graph containing \(e=(j\to i)\) with \(w_{ij}=0\);
2. a graph in which edge \(e\) is omitted.

Assume identical initial physical state/history for all remaining coordinates and no other rule depends on the mere presence of the edge.

Then, on any horizon on which both systems are physically well-posed,

- their continuous physical state and spike trajectories coincide;
- the topology-fixed event tapes do **not** coincide, because system 1 retains the labelled arrivals (SZ.1).

Hence "edge omitted" and "edge present at zero weight" are physically state-equivalent at the exact zero value but are not the same structural chart.

This distinction is necessary for differentiability through \(w_{ij}=0\).

---

## 3. R1/R2 replacement for EC-A4

The candidate's original EC-A4 sentence

> Structural zero-weight edges are not treated as physical input events in the ordinary chart.

is rejected and superseded.

### Repaired EC-A4 — structural arrival regularity

**Label:** ASSUMPTION.

Every structurally present delayed edge \(e=(j\to i)\in E\), including an edge with \(w_{ij}=0\), has a well-defined labelled launch and arrival event.

For a \(C^k\) delay map,

\[
A_e(\lambda)
=
T_{\rm launch}(\lambda)+\tau_e(\lambda).
\tag{R.1}
\]

The event-state map is \(C^k\). For the frozen alpha jump,

\[
q_i^+=q_i^-+w_e\alpha^2.
\tag{R.2}
\]

At \(w_e=0\), (R.2) is the identity in the physical state but remains a labelled structural event map.

Every structurally present arrival participates in ordinary event-order, event-separation, collision, and boundary-margin conditions, whether or not its instantaneous state jump is zero.

### Consequence for the event-chart theorem

**Label:** THEOREM / REPAIR CHECK PASSED.  
**Provenance:** DERIVATION HERE.

The candidate Section 11 finite-event event-chart theorem remains valid with repaired EC-A4.

The proof is unchanged except for one semantic clarification:

- scheduled arrival times include all structurally present edges;
- the associated reset/jump map is allowed to be the identity at isolated parameter values such as \(w_e=0\).

A smooth identity event map does not obstruct the induction argument.

If a zero-jump arrival has positive separation from competing events, its labelled order persists locally.

If its separation reaches zero, the ordinary labelled chart reaches a chart boundary even if the physical continuous state would remain well-defined under a different grouped/quotiented representation.

---

## 4. Dependent replacement for arrival-separation language

The candidate Section 12.3 phrase

> Positive separation of active arrival times ...

is superseded by:

### Repaired Section 12.3 — arrival separation

**Label:** INTERPRETATION.

Positive separation of **all structurally present labelled arrival times** is sufficient for the topology-fixed sequential ordinary chart.

This includes arrivals whose jump is the identity at \(w_e=0\).

Two or more simultaneous arrivals may still yield a well-defined physical state when their jump maps commute, including the trivial zero-jump case. But zero separation destroys uniqueness/stability of the **ordinary labelled total-order representation** unless a separate grouped-event convention is adopted.

Thus:

- physical well-posedness,
- topology-fixed labelled-chart regularity,

remain distinct notions.

---

## 5. R3 — derivatives at structural zero weight

### 5.1 Direct jump derivative

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

For the structural jump map

\[
J_e(q_i,w_e)=q_i+w_e\alpha^2,
\]

\[
\boxed{
\partial_{w_e}J_e=\alpha^2.
}
\tag{R.3}
\]

Therefore the event map is smooth through \(w_e=0\), and its direct weight derivative does not vanish there.

### 5.2 Downstream alpha-input derivative at zero weight

**Label:** PROPOSITION / PROVED ON A STABLE REGULAR CHART.  
**Provenance:** DERIVATION HERE.

Write the contribution of one structural edge pulse to downstream input as

\[
\psi_e(t;w)
=
w\,\eta_\alpha\!\left(t-A_e(w)\right)
\]

for \(t\) after the labelled arrival and while the same regular chart is valid.

Differentiate:

\[
\partial_w\psi_e
=
\eta_\alpha(t-A_e(w))
-
w\,\eta_\alpha'(t-A_e(w))\,\partial_w A_e(w).
\]

Hence

\[
\boxed{
\left.\partial_w\psi_e(t;w)\right|_{w=0}
=
\eta_\alpha(t-A_e(0)).
}
\tag{R.4}
\]

Thus downstream state/phase/spike-time sensitivity with respect to a structural weight at \(w=0\) **need not vanish**.

No blanket claim is made that it must be nonzero for every downstream observable: cancellations, response plateaus, timing, symmetry, or later dynamics may make a particular derivative zero.

### 5.3 Spike-time derivative with respect to weight at zero

**Label:** PROPOSITION / QUALIFIED.  
**Provenance:** DERIVATION HERE.

For any regular downstream spike \(T\),

\[
D_wT
=
-\frac{D_w\theta(T)|_{t\ {\rm fixed}}}
{S(\psi(T^-))}.
\tag{R.5}
\]

Equation (R.4) shows that the numerator can receive a nonzero first-order contribution even at \(w=0\).

Therefore a zero coupling value is **not** grounds for deleting the weight coordinate or setting its spike-time derivative to zero.

### 5.4 Delay derivative of the labelled zero-weight arrival

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

For the structural arrival

\[
A_e=T_{\rm launch}+\tau_e,
\]

\[
\boxed{
D_{\tau_e}A_e
=
D_{\tau_e}T_{\rm launch}+1.
}
\tag{R.6}
\]

This is the same delayed-arrival derivative as at nonzero weight.

If \(\tau_e\) appears nowhere except this structural edge and \(w_e=0\), then on a stable physical regular chart the continuous physical state is independent of \(\tau_e\), so

\[
D_{\tau_e}T_{\rm launch}=0,
\qquad
D_{\tau_e}A_e=1.
\tag{R.7}
\]

The labelled arrival therefore moves with its delay even though its jump remains zero.

### 5.5 Downstream spike-time delay sensitivity at zero weight

**Label:** PROPOSITION / QUALIFIED.  
**Provenance:** DERIVATION HERE.

Under the restricted situation of (R.7), while the labelled arrival remains separated from every competitor and no topology-dependent rule affects the physical flow, moving \(\tau_e\) changes only the position of an identity event in the tape.

Then physical state/spike times are locally unchanged, so their direct sensitivity to this zero-edge delay is zero.

However:

- the labelled arrival-time derivative is still nonzero;
- event-separation and boundary margins vary with \(\tau_e\);
- a collision or order change can occur;
- at such a chart boundary the ordinary fixed-tape derivative statement no longer applies.

No stronger blanket zero-delay-sensitivity claim is made.

---

## 6. Repair to Section 16 parameter-class statement

The candidate Section 16 remains valid but is clarified as follows.

### Repaired weight-coordinate clause

**Label:** PROPOSITION / PROVED.

Within an ordinary topology-fixed regular chart, local derivatives exist with respect to every structural real weight coordinate \(w_e\), including at \(w_e=0\), provided the surrounding event chart remains regular.

The structural arrival corresponding to that coordinate remains in the tape.

No topology creation/deletion occurs when the weight crosses zero.

This preserves the open-coordinate interpretation required for differentiating weights through zero.

---

## 7. Repair to Section 20 pulse-aware segmentation

The candidate sentence

> Arrival times are points where the target-local q state jumps ...

is too strong at structural zero weight and is superseded.

### Repaired Section 20 — topology-fixed pulse-aware segmentation

**Label:** PROPOSITION / MATHEMATICALLY JUSTIFIED.  
**Provenance:** DERIVATION HERE.

Every structurally present delayed arrival is a labelled point at which the corresponding arrival map

\[
q_i^+=q_i^-+w_e\alpha^2
\]

is applied.

For \(w_e\ne0\), the target-local \(q_i\) changes.

For \(w_e=0\), the map is the identity, but the labelled structural event remains present.

Segmentation at every structurally present labelled arrival is therefore a mathematically consistent decomposition for a topology-fixed event tape.

On each open segment between successive labelled events, the arrival-free alpha-state formula remains exact.

### Qualification

For physical state propagation alone, identity events could be algebraically removed at the exact parameter value \(w_e=0\).

They may **not** be removed from the topology-fixed chart used for derivatives through zero, event-order margins, or structural-coordinate certification.

As before, segmentation alone does not prove first-hit completeness.

---

## 8. R4 — corrected TH-FH-06

The candidate TH-FH-06 is rejected and replaced completely by the following fixture.

## TH-FH-06 — topology-fixed structural-zero edge

**Label:** PROPOSED THEORY-DERIVED VALIDATION FIXTURE / NOT EXECUTED.

Fix a structural graph containing edge \(e=(j\to i)\) with fixed delay \(\tau_e\).

Use three coupling values without changing topology:

\[
w_e=-\varepsilon,\qquad
w_e=0,\qquad
w_e=+\varepsilon,
\]

with a prospectively chosen small \(\varepsilon>0\) such that the intended ordinary event margins remain positive in the noncollision cases.

Also construct a separate comparison graph in which edge \(e\) is genuinely omitted. This comparison graph is **not** the same event chart.

Required future checks:

1. **Exact-zero physical-state equivalence.**  
   At \(w_e=0\), physical continuous state and spike times agree with the otherwise identical graph in which \(e\) is omitted, whenever both trajectories are physically regular.

2. **Tape non-equivalence.**  
   The topology-fixed \(w_e=0\) tape retains the labelled launch/arrival events for \(e\); the graph-with-edge-omitted tape does not. The tapes must therefore not be declared identical.

3. **Topology preservation through zero.**  
   The \(-\varepsilon,0,+\varepsilon\) cases retain the same structural edge coordinate. No edge insertion/deletion or graph recompilation is allowed merely because the weight changes sign or equals zero.

4. **Weight derivative at zero.**  
   On a predetermined regular same-chart fixture, compare the fixed-chart/JAX derivative with respect to \(w_e\) at zero against physically rerecorded centered finite differences using \(\pm\varepsilon\).  
   The expected mathematical reference is the structural derivative implied by (R.3)–(R.5), not a forced zero derivative.

5. **Zero-edge delay semantics.**  
   Varying \(\tau_e\) at \(w_e=0\) must move the labelled arrival according to (R.6). The implementation must retain any consequent change in event-separation/boundary margins.

6. **State-versus-chart distinction.**  
   If the zero-jump arrival moves while remaining strictly separated from all competitors, physical state/spike times may remain unchanged even though the labelled event time moves.

7. **Collision case.**  
   Prospectively choose a delay value for which the structural-zero arrival becomes simultaneous, within the mathematical fixture, with another labelled event. The ordinary chart must fail closed as a collision/boundary case; the arrival may not be dismissed as "spurious" because its jump is zero.

8. **Horizon case.**  
   A structural-zero arrival exactly on the horizon remains a boundary case for the labelled chart.

Negative control:

- delete the structural arrival from the \(w_e=0\) tape while retaining the same topology signature and then attempt a same-chart derivative through \(w=0\). The topology/tape sentinel must reject the comparison.

No part of TH-FH-06 is executed in this CORE repair gate.

---

## 9. R5 — complete candidate consistency audit

The full returned candidate was searched for statements depending on deletion of zero-weight structural edges.

The affected statements are:

1. **EC-A4**, candidate line containing  
   "Structural zero-weight edges are not treated as physical input events..."  
   → replaced by Section 3 above.

2. **Section 12.3**, phrase  
   "Positive separation of active arrival times..."  
   → clarified to all structurally present labelled arrival times in Section 4.

3. **Section 20**, statements  
   "Arrival times are points where q jumps" and "every active arrival"  
   → replaced by topology-fixed arrival-map language in Section 7.

4. **TH-FH-06**, candidate requirements deleting the zero-edge arrival competitor  
   → replaced completely by Section 8.

5. **Section 16 weight-coordinate interpretation**  
   → clarified in Section 6 so structural weight derivatives explicitly include \(w=0\).

No other statement in the candidate was found whose truth requires deleting structural zero-weight arrivals.

---

## 10. Recheck of candidate Sections 3–19

### Sections 3–9 — first-hit, response and tail mathematics

**Result:** UNCHANGED / VALID.

The first-hit/no-hit theorems, exact alpha extrema, response smoothness/derivative bounds, alpha decay, remaining-mass formula and phase-tail bounds do not depend on deleting zero-weight structural edges.

A zero-weight arrival simply applies an identity alpha-state map before the next segment.

### Sections 10–12 — event-chart regularity

**Result:** VALID AFTER EC-A4 / ARRIVAL-SEPARATION REPLACEMENT.

The finite-event induction theorem permits identity jump maps.

What matters for the ordinary topology-fixed chart is:

- smooth event-time dependence;
- smooth event maps;
- positive spike transversality;
- positive labelled-event separation;
- positive boundary margin;
- finite event list.

A zero jump violates none of these.

### Sections 13–16 — local differentiability

**Result:** VALID AFTER ZERO-WEIGHT CLARIFICATION.

The spike-time IFT formula and arrival derivative remain unchanged.

The structural weight derivative is valid through zero because the jump/convolution map is smooth in \(w_e\) and topology is fixed.

### Sections 17–19 — fixed-chart replay and chart radius

**Result:** UNCHANGED / VALID WITH REPAIRED TAPE SEMANTICS.

The same-chart computational object must now include structurally present zero-weight arrivals.

Deleting such an arrival is a topology/tape mismatch, even when the physical continuous trajectory at the base point is unchanged.

Positive chart-radius existence is unaffected; zero-weight arrival separation contributes one of the continuity margins that must remain positive.

---

## 11. Interaction with RB-019 / RB-021

**Label:** INTERPRETATION / CONSISTENCY RESTORED.

The repair aligns the theory with the frozen numerical structural-coordinate convention:

- topology/signature is independent of the current weight value;
- structural zero-weight support is retained;
- certified event tapes may contain identity arrival maps;
- fixed-chart/JAX guards must reject topology/tape deletion across a weight perturbation through zero;
- state equality at \(w=0\) is not used to equate event tapes.

No RB-019 or RB-021 numerical tolerance is promoted to a theorem.

No numerical result is reclassified.

---

## 12. Material contradiction audit

**Result:** NO SECOND MATERIAL CONTRADICTION FOUND WITHIN THE AUTHORIZED R1–R5 CONSISTENCY AUDIT.

The repair does not require reopening:

- first-hit existence/no-hit theory;
- finite-certification theorem;
- response smoothness/derivative bounds;
- alpha-tail or phase-error bounds;
- transversality theory;
- boundary theory;
- general local implicit-function theorem;
- theorem/engineering distinction;
- parked v0.27c boundaries.

The original candidate's broader open questions remain unchanged.

---

## 13. Gate decision

# PASS — STRUCTURAL-ZERO / EVENT-CHART SEMANTICS REPAIRED

The candidate theory can be frozen only when read together with this repair artifact.

The repaired canonical rule is:

\[
\boxed{
\text{fixed structural topology}
\;\not\equiv\;
\text{nonzero coupling support}
}
\]

and specifically:

\[
\boxed{
w_e=0
\Rightarrow
\text{identity state jump, but retained labelled structural arrival}.
}
\]

This restores consistency between the theory layer and RB-019/RB-021 without changing unrelated mathematics.

---

## 14. Proposed MASTER freeze

MASTER may now establish

\`CORE Event-Chart Regularity & Certified First-Hit Theory Freeze 0.1\`

by freezing:

1. the returned candidate  
   \`research/core/event_chart_first_hit_theory_gate_0_1.md\`,
2. this semantic repair artifact as a mandatory superseding correction for EC-A4, Section 12.3, Section 16's zero-weight interpretation, Section 20, and TH-FH-06.

The freeze should state explicitly that the original conflicting structural-zero sentences remain audit history and are superseded by this repair.

No numerical validation or v0.27c execution is authorized by this PASS.

## STOP

STOP — RETURN TO MASTER
