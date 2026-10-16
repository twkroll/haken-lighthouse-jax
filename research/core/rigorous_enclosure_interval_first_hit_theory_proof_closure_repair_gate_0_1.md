# CORE Rigorous Interval Theory Proof-Closure Repair Gate 0.1

Date: 2026-10-16  
Status: PASS — ARITHMETIC CONVERGENCE AND CHART-PRESERVATION PROOF CLOSURE REPAIRED

## 1. Authority and narrow scope

This gate executes:

`research/master/prompts/core_rigorous_interval_theory_proof_closure_repair_gate_0_1.md`.

Canonical identity at gate start:

- repository: `twkroll/haken-lighthouse-jax`
- branch: `main`
- `main` HEAD: `5e3364ac4d110a21858dacac47b282e45255793c`
- CORE STATUS blob: `02098968ee69273a4585986d55a7a10fe3cf2975`
- MASTER STATUS blob: `12ec2f96367c9442682b09f4e7565dcf2a001f67`
- MASTER project-status blob: `391ce957ecd98a79d56f2874eadeb8ac549b5a60`
- MASTER decision-log blob: `310d98541bf9805ebe9e2338e715b25d7f3c9d86`
- repair prompt blob: `d81be2a761508c370c3343d384b7764b1017b6d9`
- returned candidate blob: `ca2773d3845f0a36053df21c23fa9af7b4ce8759`
- RB-022 remains frozen first-hit/event-chart theory;
- RB-023 remains frozen finite engineering theory-validation evidence.

RB-015 remains immutable `SCIENTIFIC FAIL`.

The original candidate

`research/core/rigorous_enclosure_interval_first_hit_theory_gate_0_1.md`

is preserved as audit history and is not overwritten.

This repair changes only:

1. the arithmetic-convergence assumption and dependent convergence/termination statements;
2. the chart-radius/indexed-event/full-chart distinction and dependent references.

No numerical execution, interval-library benchmarking, TR-27C execution, protected RNG creation, APP-3 work, v0.28 effect-bearing work, novelty positioning, or manuscript claim work occurred.

---

# Part I — Repair A: arithmetic convergence rate

## 2. Route selected

**Label:** ASSUMPTION / REPAIR CHOICE.

The repair adopts **Route A1** from the MASTER prompt.

IR-A4 is strengthened from qualitative primitive convergence to an explicit uniform bounded-domain rate sufficient for the already chosen schedule

\[
p_n=128+8n.
\]

IR-A1–IR-A3 and IR-A5 remain unchanged.

## 3. Replacement IR-A4

The candidate IR-A4 is superseded by:

### IR-A4-R — uniform bounded-domain arithmetic excess rate

**Label:** ASSUMPTION / IMPLEMENTATION PROOF OBLIGATION.

Fix any compact admissible real domain \(K\) containing every exact scalar intermediate value used by one RIFC-0.1 segment computation under consideration.

For every working precision \(p\), the rigorous backend must satisfy all of the following.

### A4-R.1 Inclusion

Every primitive interval operation required by RIFC-0.1 remains outward-valid as required by IR-A1–IR-A3 and IR-A5.

### A4-R.2 Uniform primitive excess-width rate

There exists a finite constant

\[
C_K>0
\]

independent of \(p\) such that, for every required primitive interval operation \(\mathcal O_p\) and every exact admissible operand tuple \(x\in K\),

\[
\boxed{
\operatorname{excwid}\!\left(\mathcal O_p(x)\right)
\le
C_K\,2^{-p}.
}
\tag{A.1}
\]

Here \(\operatorname{excwid}\) denotes interval width in excess of the exact real range of that primitive on the supplied exact operands.

This requirement includes the rigorous exponential primitive used by IR-A3.

### A4-R.3 Uniform propagation factor for the fixed RIFC expression graph

For the finite family of scalar expression graphs used in one RIFC-0.1 cell evaluation—alpha propagation, response endpoint enclosure, cell gain, and prefix accumulation—there exists a finite bounded-domain propagation constant

\[
B_K>0
\]

such that the arithmetic excess width at the output of a graph with \(N\) primitive evaluations is bounded by

\[
\boxed{
E_{\rm arith}(N,p)
\le
B_K\,N\,2^{-p}.
}
\tag{A.2}
\]

\(B_K\) may depend on the compact admissible domain and the fixed expression family, but not on \(N\) or \(p\).

A later implementation must justify \(B_K\) from a backend-level error analysis, an equivalent whole-expression enclosure theorem, or a stronger formally verified interval contract.

### A4-R.4 No near-singular hidden division

Any expression branch containing division is included in (A.2) only on a compact subdomain where its divisor is rigorously bounded away from zero.

The threshold-straddling response branch does not evaluate the above-threshold reciprocal formula at \(x=h\); it uses the monotone splice enclosure from the candidate Section 10.

If a required compact-domain propagation bound cannot be established, the backend is not eligible for the eventual-convergence theorem and must return `UNCERTIFIED_ARITHMETIC` for that proof mode.

### A4-R.5 Fixed refinement precision

The deterministic precision schedule remains

\[
\boxed{
p_n=128+8n.
}
\tag{A.3}
\]

The values 128 and 8 remain algorithm-definition choices, not physical or scientific tolerances.

---

## 4. Operation-count lemma

**Label:** LEMMA / PROVED.  
**Provenance:** DERIVATION HERE.

At dyadic level \(n\), RIFC-0.1 uses

\[
m_n=2^n
\]

time cells.

For a fixed finite graph and a fixed finite set of candidate neurons/events on one segment, there exist constants

\[
a,b>0
\]

independent of \(n\) such that the number of primitive interval evaluations satisfies

\[
\boxed{
N_n\le a\,2^n+b.
}
\tag{A.4}
\]

### Proof

Each cell requires a fixed finite number of alpha-state, response, width, gain, and prefix operations per candidate neuron.

The graph/event list is finite and fixed for the segment.

Bookkeeping outside cells contributes only a fixed finite overhead. QED.

---

## 5. Corrected arithmetic-convergence lemma

This section supersedes candidate Section 18.

### Enclosure-convergence lemma for singleton deterministic data

**Label:** LEMMA / PROVED UNDER IR-A1–IR-A3, IR-A4-R, AND IR-A5.  
**Provenance:** DERIVATION HERE.

Assume:

1. \(A,Q_0,P_0,D\) represent singleton exact real data;
2. their outward endpoint representation error obeys the same bounded-domain \(O(2^{-p})\) contract as the primitive backend;
3. the segment lies in a finite compact admissible domain \(K\);
4. the relevant RIFC expression graphs satisfy (A.2);
5. no arithmetic proof failure occurs.

Then the width of the RIFC interval-Darboux phase-gain enclosure tends to zero as \(n\to\infty\).

### Proof

Split the total enclosure width into:

\[
W_n
\le
W_{\rm range}(n)
+
W_{\rm arith}(n).
\tag{A.5}
\]

#### Exact range/Darboux part

The exact arrival-free state \(\psi\) is continuous on the compact segment.

The frozen response \(S\) is continuous, so

\[
f(s)=S(\psi(s))
\]

is uniformly continuous.

The exact upper-minus-lower Darboux gap on an equal dyadic mesh therefore obeys

\[
W_{\rm range}(n)\to0
\qquad
(n\to\infty).
\tag{A.6}
\]

The natural interval state overestimation caused by the cell time variable also tends to zero as cell diameter

\[
L2^{-n}
\]

tends to zero; this is a range-dependency effect, not floating-point rounding.

#### Arithmetic part

By (A.2) and (A.4),

\[
W_{\rm arith}(n)
\le
B_K(a2^n+b)2^{-p_n}.
\tag{A.7}
\]

Using

\[
p_n=128+8n,
\]

\[
W_{\rm arith}(n)
\le
B_K
\left[
a\,2^{-128}2^{-7n}
+
b\,2^{-128}2^{-8n}
\right]
\to0.
\tag{A.8}
\]

Therefore

\[
W_n\to0.
\]

QED.

### Repair significance

The old qualitative statement "primitive overestimation tends to zero" is no longer used to infer the explicit \(2^{-p}\) rate.

The rate is now an explicit backend proof obligation.

---

## 6. Corrected finite strict-margin termination theorem

This supersedes candidate Section 19 only in its assumptions.

### Theorem

**Label:** THEOREM / PROVED.  
**Provenance:** DERIVATION HERE.

Assume the repaired Section 5 hypotheses.

### No-hit case

If the exact deterministic trajectory satisfies

\[
G(L)\le d-\gamma
\]

for some strict margin

\[
\gamma>0,
\]

then there exists a finite level \(n_*\) at which the RIFC no-hit test

\[
\overline G(L)<\underline d
\]

holds.

### Regular-hit case

Suppose the exact deterministic first hit \(T\) satisfies:

\[
0<T<L,
\]

\[
S(\psi(T^-))\ge\nu_*>0,
\]

and there exist \(a<T<b\) with strict prefix margins

\[
G(a)<d<G(b)
\]

and a neighborhood transversality margin

\[
S(\psi(s))\ge\nu_*/2
\qquad
\forall s\in[a,b].
\]

Then there exists a finite refinement level at which RIFC-0.1 emits

`CERTIFIED_REGULAR_HIT`.

### Proof

The repaired convergence lemma gives shrinking prefix gain enclosures and shrinking local response enclosures.

All deciding inequalities are strict.

Therefore the exact positive margins dominate the enclosure widths at some finite level. QED.

### Finite budget

For any fixed finite \(N_{\max}\), if certification has not been reached by level \(N_{\max}\), the algorithm still returns

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

A fixed software budget is not covered by the mathematical eventual-termination guarantee.

---

## 7. RIFC precision-schedule repair

Candidate Section 37 is retained with the following mandatory interpretation.

At level \(n\),

\[
p_n=128+8n
\]

is valid for **eventual-certification claims only if** the backend satisfies IR-A4-R on the compact admissible domain of the computation.

If inclusion is valid but the rate/pro\-pagation obligations of IR-A4-R are not established, positive finite certificates remain sound, but the implementation may not invoke the candidate's eventual-convergence/termination theorem.

In that situation it must classify unclosed refinement as fail-closed `UNCERTIFIED` / `RESOURCE_EXHAUSTED`, not infer nonexistence of a certificate.

---

# Part II — Repair B: indexed margins versus full chart preservation

## 8. Diagnosis

Candidate Section 28 correctly bounds movement of **already indexed** event times, transversality margins, and boundary distances.

Those bounds do not by themselves exclude:

- insertion of a previously absent spike between two indexed events;
- deletion of an indexed spike because an earlier competing event is inserted;
- a previously nonwinning neuron becoming the next event;
- an unindexed structural arrival entering the considered finite horizon.

Therefore the sentence

> "Therefore the same ordinary labelled event chart is preserved."

is superseded.

---

## 9. Replacement Section 28A — indexed-event margin preservation

### Setup

Let the reference finite labelled event list be

\[
E_1,\ldots,E_M
\]

at parameter \(\lambda_0\).

Suppose rigorous base margins are known for these indexed events:

\[
\nu_m(\lambda_0)
\ge
\underline\nu_m>0,
\]

\[
|T_m(\lambda_0)-T_n(\lambda_0)|
\ge
\underline\delta_{mn}>0,
\]

\[
b_m(\lambda_0)
\ge
\underline b_m>0.
\]

Let \(B_R(\lambda_0)\) be a parameter ball on which the **indexed event functions themselves are already rigorously defined** as smooth continuations and satisfy neighborhood-wide derivative bounds

\[
\|\nabla_\lambda T_m\|_*
\le
K_{T_m},
\tag{B.1}
\]

\[
\|\nabla_\lambda\nu_m\|_*
\le
K_{\nu_m}.
\tag{B.2}
\]

This assumption does **not** assert that the complete event chart is unchanged. It asserts only that the named indexed event functions exist as validated local continuations on the ball.

Define

\[
\rho_{\rm tr}
=
\min_m
\frac{\underline\nu_m}{2K_{\nu_m}},
\tag{B.3}
\]

\[
\rho_{\rm sep}
=
\min_{m<n}
\frac{\underline\delta_{mn}}
{2(K_{T_m}+K_{T_n})},
\tag{B.4}
\]

\[
\rho_{\rm bdry}
=
\min_m
\frac{\underline b_m}{2K_{T_m}},
\tag{B.5}
\]

omitting zero-denominator restrictions.

Set

\[
\boxed{
\rho_{\rm indexed}
=
\min
\{R,\rho_{\rm tr},\rho_{\rm sep},\rho_{\rm bdry}\}.
}
\tag{B.6}
\]

### Indexed-margin theorem

**Label:** THEOREM / PROVED UNDER THE STATED NEIGHBORHOOD-WIDE INDEXED-EVENT BOUNDS.  
**Provenance:** DERIVATION HERE.

For every

\[
\|\lambda-\lambda_0\|
<
\rho_{\rm indexed},
\]

the already indexed events \(E_1,\ldots,E_M\):

1. retain at least half of every certified spike-transversality margin;
2. retain at least half of every pairwise indexed-event separation margin;
3. retain at least half of every indexed event-to-boundary margin.

### Proof

Mean-value estimates give

\[
|\nu_m(\lambda)-\nu_m(\lambda_0)|
\le
K_{\nu_m}\|\lambda-\lambda_0\|,
\]

and

\[
|T_m(\lambda)-T_m(\lambda_0)|
\le
K_{T_m}\|\lambda-\lambda_0\|.
\]

The separation change for a pair is at most the sum of the two event-time motions.

Substitute (B.6). QED.

### Explicit non-conclusion

The indexed-margin theorem **does not** prove that these are the only events.

It therefore does not, by itself, certify the complete ordinary event chart.

---

## 10. Replacement Section 28B — explicit no-new-event completeness condition

### NNE-A — uniform inter-event completeness certificates

**Label:** ASSUMPTION / VALIDATED-CERTIFICATE REQUIREMENT.

For every reference inter-event segment

\[
[T_m,T_{m+1}]
\]

and every parameter

\[
\lambda\in B_\rho(\lambda_0),
\]

there must be a rigorous family-valued certification, independent of the indexed-margin conclusion, establishing all of the following.

1. **All structural arrivals are enumerated.**  
   Every structurally present labelled arrival whose time can enter the segment is included, including arrivals on structural-zero edges.

2. **Nonwinning spike candidates are excluded.**  
   For every neuron/event candidate not designated as the segment's next indexed spike, a uniform no-hit enclosure proves that it cannot fire before the certified next event window.

3. **The designated spike, when the next event is a spike, is present and regular.**  
   A uniform family-valued first-hit enclosure proves a unique transversal hit in its certified time window.

4. **Arrival ordering, when the next event is an arrival, is certified.**  
   The designated structural arrival is rigorously before all competing arrivals/spikes using interval time ordering and/or pre-arrival no-hit phase certificates.

5. **No horizon/initial insertion occurs.**  
   Boundary ordering is rigorously certified.

6. **Post-event state enclosure closes the induction.**  
   Applying the indexed jump/reset map to the certified pre-event state produces an outward enclosure valid for the next segment.

These certificates may be produced by a parameter-box extension of RIFC-0.1 or any later independently validated inclusion method.

They may not be replaced by the assumption "the chart is unchanged."

### No-new-event meaning

NNE-A is a constructive **segment-completeness condition**: it rules out insertion of any previously absent ordinary event before the designated next event.

It is logically stronger than preserving margins of already indexed events.

---

## 11. Conditional full-chart preservation theorem

**Label:** THEOREM / PROVED UNDER INDEXED-MARGIN BOUNDS + NNE-A.  
**Provenance:** DERIVATION HERE.

Assume:

1. the indexed-margin hypotheses of Section 9 hold on
   \[
   B_\rho(\lambda_0);
   \]
2. NNE-A holds uniformly on every inter-event segment of the finite reference tape;
3. fixed structural topology is maintained, including structural-zero labelled arrivals;
4. the horizon is finite.

Then every

\[
\lambda\in B_\rho(\lambda_0)
\]

has the same complete ordinary labelled event types and order as the reference tape.

### Proof

Induct over the finite reference event list.

At segment \(m\), NNE-A excludes every competing earlier event and certifies existence/order of the designated next event.

The indexed-margin theorem preserves its transversality, separation, and boundary margins.

The certified post-event enclosure initializes the next segment.

Finite induction yields the complete tape. QED.

### Non-circularity statement

The theorem does not assume "same chart" as a premise.

It assumes explicit segment-level inclusion certificates that independently rule out competing event insertion/deletion.

---

## 12. Corrected chart-radius conclusion

Candidate \(\rho_{\rm cert}\) is superseded by two distinct concepts.

### Indexed-event radius

\[
\boxed{
\rho_{\rm indexed}
}
\]

from (B.6) is a valid lower radius for preservation of margins of already indexed event functions.

### Full-chart radius

A rigorous full-chart lower radius may be asserted only when there exists some

\[
\rho_{\rm NNE}>0
\]

on which NNE-A has been independently certified.

Then

\[
\boxed{
\rho_{\rm chart}
=
\min\{\rho_{\rm indexed},\rho_{\rm NNE}\}
}
\tag{B.7}
\]

is a valid full ordinary-chart lower bound.

### Explicit non-result

**Label:** OPEN QUESTION / NON-RESULT.

This gate does not construct a general automatic method that, from base-point event sensitivities alone, produces \(\rho_{\rm NNE}>0\).

Therefore no universal nontrivial computable full-chart radius is frozen.

The general automatic parameter-box completeness/radius problem remains OPEN.

---

## 13. Structural-zero role in repaired radius theory

**Label:** PROPOSITION / PROVED.

Every structurally present zero-weight arrival remains:

- in the indexed event list when present in the reference tape;
- in all pairwise separation/boundary calculations;
- in every NNE-A competitor enumeration;
- present when the structural weight interval crosses zero.

Its instantaneous jump may be the identity at \(w_e=0\), but this does not remove its event-time or chart-margin role.

Crossing \(w_e=0\) therefore does not itself force

\[
\rho_{\rm indexed}=0
\]

or topology change.

---

# Part III — consistency audit

## 14. Candidate Section 18

**Disposition:** SUPERSEDED BY REPAIRED SECTION 5.

The old use of

\[
C2^n2^{-p_n}
\]

from qualitative IR-A4 is rejected.

The repaired estimate follows only from explicit IR-A4-R and the operation-count lemma.

## 15. Candidate Section 19

**Disposition:** VALID AFTER ASSUMPTION REPLACEMENT.

The strict-margin finite termination theorem remains valid with repaired Section 5 hypotheses.

No scientific/no-hit/hit threshold changes.

## 16. Candidate Section 28

**Disposition:** PARTLY SUPERSEDED.

The formulas for motion-based transversality/separation/boundary radii remain valid as **indexed-event margin bounds**.

The conclusion that they alone preserve the entire event chart is rejected.

## 17. Candidate Sections 29–30

**Disposition:** RETAINED WITH TERMINOLOGY REPAIR.

Structural-zero arrivals still constrain indexed-event margins and NNE-A.

The existing "no universal computable chart radius" conclusion is strengthened/clarified:

- indexed-margin radii can be computed conditionally from rigorous derivative bounds;
- a full chart radius additionally needs independent no-new-event completeness;
- the latter is not automatically supplied by base-point sensitivities.

## 18. Candidate Section 37 — RIFC precision schedule

**Disposition:** RETAINED UNDER IR-A4-R.

The fixed schedule

\[
p_n=128+8n
\]

remains part of RIFC-0.1.

Its sound finite certificates require only outward inclusion.

Its eventual-certification proof additionally requires IR-A4-R.

## 19. Candidate Section 42 — soundness theorem

**Disposition:** UNCHANGED / VALID.

### Proposition

**Label:** THEOREM / PROVED.

The RIFC-0.1 soundness theorem does **not** depend on the \(O(2^{-p})\) convergence rate.

It requires only:

- outward-valid primitive inclusion;
- correct response/state/gain interval formulas;
- strict certificate inequalities;
- correct event-order logic.

Therefore every finite positive certificate remains sound even if the backend's excess widths shrink too slowly for eventual certification.

IR-A4-R is needed for the repaired eventual-convergence theorem, not for finite inclusion soundness.

## 20. Candidate Section 43 — eventual certification

**Disposition:** VALID AFTER REPAIR.

For one deterministic next-event problem, eventual certification remains proved under:

- singleton deterministic inputs;
- repaired IR-A4-R;
- compact admissible domain;
- no arithmetic proof failure;
- strict no-hit or regular-hit/transversality margin;
- strict separation from structural arrivals/horizon for the next-event classification.

For an entire finite tape, eventual certification additionally requires the corresponding strict next-event condition recursively on every segment.

It does not follow from indexed-event sensitivity margins alone.

For any finite \(N_{\max}\), unresolved refinement remains

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

## 21. Candidate Section 33 — CERTIFIED_ORDINARY_CHART label

**Disposition:** CLARIFIED.

A full `CERTIFIED_ORDINARY_CHART` statement for a parameter family requires:

- positive certificate obligations for every indexed event; **and**
- explicit completeness/no-new-event certificates on every inter-event segment.

For a single deterministic tape constructed sequentially by RIFC next-event certification, the recursive next-event proof supplies this completeness.

For a parameter ball, NNE-A or an equivalent validated family method is required.

## 22. Candidate Section 41 unsupported cases

**Disposition:** CLARIFIED.

"Global parameter-box chart radii without independent neighborhood-wide sensitivity bounds" remains unsupported.

It is extended to:

- full parameter-box chart radii without both
  1. rigorous indexed-event neighborhood bounds and
  2. independent no-new-event segment completeness certificates.

## 23. Candidate Section 47 open problem

**Disposition:** SUPERSEDED BY REPAIRED OPEN QUESTION.

The sharp computable chart-radius problem now explicitly includes two tasks:

1. rigorous neighborhood-wide indexed-event sensitivity bounds;
2. rigorous parameter-box no-new-event completeness.

Neither is automatically obtained from base-point derivatives.

---

# Part IV — material-contradiction audit

## 24. Soundness

**Result:** PASS.

No change to alpha propagation, response enclosure, Darboux integration, no-hit/hit logic, transversality, structural-zero semantics, or event-order inclusion was required.

Positive certificate soundness remains intact.

## 25. Eventual certification

**Result:** PASS AFTER REPAIR.

The proof now has exactly the arithmetic convergence assumption it uses.

No empirical RB-023 rate is imported.

## 26. Full-chart preservation

**Result:** PASS AFTER WEAKENING + EXPLICIT COMPLETENESS CONDITION.

The previous overclaim is removed.

Indexed-event margin preservation is proved from derivative bounds.

Full-chart preservation is conditional on separate neighborhood-wide no-new-event completeness.

## 27. Additional contradiction search

**Result:** NO SECOND MATERIAL CONTRADICTION FOUND WITHIN THE AUTHORIZED REPAIR SCOPE.

No unrelated interval theorem needs reopening.

---

# Part V — repaired RIFC-0.1 freeze interpretation

## 28. Soundness versus convergence

The future freeze should distinguish:

### Finite certificate soundness

Requires:

- IR-A1–IR-A3;
- IR-A5;
- outward-valid interval formulas;
- proof-valid exponential inclusion.

IR-A4-R's rate is not logically needed for one already obtained strict positive certificate.

### Eventual certification under refinement

Additionally requires:

- IR-A4-R;
- compact admissible bounds;
- operation-count growth (A.4);
- strict mathematical margins.

This distinction prevents an implementation with valid but slowly shrinking intervals from being incorrectly called unsound.

## 29. RIFC finite-budget rule

Unchanged:

if finite \(N_{\max}\) is exhausted before a proof obligation closes,

\[
\boxed{
\texttt{RESOURCE\_EXHAUSTED / UNCERTIFIED}.
}
\]

No negative physical conclusion follows.

---

# Part VI — list of superseded candidate wording

The following candidate material is superseded by this repair:

1. **IR-A4** qualitative precision assumption  
   → replace by IR-A4-R.

2. **Section 18**, arithmetic-convergence proof using an unstated \(O(2^{-p})\) rate  
   → replace by Sections 4–5 of this repair.

3. **Section 19**, phrase "under the singleton-data assumptions of Section 18"  
   → read as the repaired Section 5 assumptions.

4. **Section 28**, title/conclusion "Conditional computable-radius theorem" insofar as it claims full chart preservation from indexed margins alone  
   → replace by Sections 9–12.

5. **Section 29**, "chart radius" terminology  
   → interpret as indexed-event margin radius unless NNE-A is also established.

6. **Section 30**, circularity discussion  
   → replace by the explicit indexed-radius/full-radius distinction and NNE-A non-result.

7. **Section 33 / CERTIFIED_ORDINARY_CHART**  
   → add inter-event completeness/no-new-event proof obligation.

8. **Section 37**, fixed precision schedule  
   → retain only with IR-A4-R for convergence claims.

9. **Section 42**, reference to IR-A1–IR-A5  
   → soundness should be read as requiring inclusion-valid parts of those assumptions; the IR-A4-R rate is not required for an already emitted certificate.

10. **Section 43**, eventual-certification theorem  
    → add IR-A4-R and recursive strict next-event/completeness conditions for a whole finite tape.

11. **Section 47**, chart-radius open problem  
    → replace by the two-part sensitivity + no-new-event completeness problem.

All other candidate sections remain unchanged unless one of these repaired references is invoked.

---

# Part VII — decision

## 30. Gate decision

# PASS — PROOF-CLOSURE REPAIR COMPLETE

Both MASTER-identified freeze blockers are closed.

### Arithmetic issue

The fixed precision schedule is now supported by an explicit uniform bounded-domain arithmetic excess-rate assumption and an explicit operation-count proof:

\[
N_n=O(2^n),
\qquad
E_{\rm arith}(n)
\le
B_KN_n2^{-(128+8n)}
\to0.
\]

No qualitative convergence assumption is used as an unstated quantitative rate.

### Chart-radius issue

The theory now distinguishes:

\[
\boxed{
\text{indexed-event margin preservation}
}
\]

from

\[
\boxed{
\text{complete ordinary-chart preservation}.
}
\]

The latter additionally requires explicit neighborhood-wide no-new-event segment completeness.

No base-point sensitivity argument alone is used to exclude event insertion.

---

## 31. Recommendation to MASTER

MASTER may establish

`CORE Rigorous Enclosure & Interval First-Hit Certification Theory Freeze 0.1`

by freezing jointly:

1. `research/core/rigorous_enclosure_interval_first_hit_theory_gate_0_1.md`;
2. this proof-closure repair as the mandatory superseding authority for the sections listed in Part VI.

The original candidate remains audit history.

A later numerical implementation gate must independently demonstrate that its interval backend actually satisfies the inclusion and IR-A4-R proof obligations before claiming eventual-certification behavior.

No numerical execution is authorized by this PASS.

## STOP

STOP — RETURN TO MASTER
