# CORE Sequential Event-Tape & NNE-A Certification Theory Freeze 0.3

Date: 2026-10-17
Status: FROZEN / STABLE SCIENTIFIC THEORY
Rollback point: RB-030

## Authority

MASTER accepts:

`research/core/sequential_event_tape_nne_a_certification_theory_gate_0_3.md`

as the canonical source for this freeze.

Returned gate blob SHA:

`fe76c5fd3206adc9f3dda451768d0a41ff5a7272`.

No numerical execution or source modification occurred in the gate.

## Frozen scope

RB-030 freezes a constructive finite-horizon theory for complete ordinary sequential labelled event tapes built from rigorous segment first-hit/no-hit certificates.

Grouped/simultaneous event charts remain outside scope.

## Finite-horizon event-count foundation

For finite graph

\[
G=(V,E),\qquad |V|=N<\infty,\qquad |E|=M<\infty,
\]

finite horizon length \(T_H\), fixed nonnegative delays, and a finite certified horizon-relevant pending-arrival queue of size \(P_0\), the frozen baseline phase rate

\[
0\le \dot\theta_i=S(\psi_i)<1
\]

implies strict same-neuron interspike separation

\[
T_i^{k+1}-T_i^k>2\pi.
\]

Hence a conservative per-neuron spike-count bound is

\[
K_i\le 1+\left\lfloor \frac{T_H}{2\pi}\right\rfloor,
\]

and total spike count is finite.

Every spike launches at most one labelled arrival on each finite outgoing structural edge, including structural zero-weight edges, so

\[
K_{\rm arr}
\le
P_0+\sum_i d_i^{\rm out}K_i.
\]

Therefore the total finite-horizon labelled event count is finite.

This excludes spike/arrival Zeno for the frozen ordinary event ontology under the stated finite-history assumptions.

## Initial-history boundary

The theory requires a finite certified list of all already in-flight labelled structural arrivals capable of occurring in the horizon.

It does not infer this from arbitrary locally finite infinite prehistory.

## Zero-delay boundary

A zero structural delay does not break finite event count.

However, a spike and its newly launched zero-delay arrival occur at the same physical time and therefore lie on a simultaneous/grouped-event boundary, not in the ordinary strictly ordered tape.

## Certified sequential state

At each step, the certified state contains at least:

- current event-time enclosure;
- outward physical-state enclosure;
- next lifted section labels;
- complete pending labelled structural-arrival queue;
- fixed structural topology;
- horizon;
- event index;
- accumulated proof ledger.

Structural topology remains fixed through zero weight.

## Candidate ontology

At every ordinary step the complete candidate-next-event set consists of:

1. one next possible first-hit candidate per neuron;
2. every already pending labelled structural arrival;
3. the horizon sentinel.

A future arrival not yet pending can only arise from a source spike after the current event.

## Certified next-spike rule

A designated spike is uniquely next only if:

- it has a rigorous regular first-hit bracket;
- its bracket lies strictly before every pending arrival;
- it lies strictly before horizon;
- every competing neuron is rigorously certified no-hit through the full latest designated-hit prefix.

All inequalities are strict outward interval inequalities.

## Certified next-arrival rule

A designated pending arrival is uniquely next only if:

- it is causally after the current event;
- it lies strictly before every other pending arrival;
- it lies strictly before horizon;
- every neuron is rigorously no-hit on the hypothetical pre-arrival flow through the latest designated-arrival time.

## Certified horizon rule

Horizon is the terminating next sentinel only if:

- every pending arrival is strictly after horizon;
- every neuron is certified no-hit through horizon.

Exact equality with horizon is not treated as an ordinary interior event.

## NNE-A-SEG

RB-030 freezes the constructive segment-level No-New-Event condition.

For one segment, NNE-A-SEG requires:

1. complete pending-arrival inventory;
2. fixed-topology completeness, including structural-zero edges;
3. explicit coverage of every neuron by designated hit or required no-hit proof;
4. exactly one strict designated next-event rule;
5. exclusion of any unlisted future arrival by excluding the source spike that would be required to launch it;
6. complete launch bookkeeping after an accepted spike;
7. fail-closed handling of zero-delay simultaneity.

## No-new-event theorem

If NNE-A-SEG holds, no unlisted ordinary physical event exists strictly between the current event and the designated next event.

The proof uses the complete frozen event ontology:

- any unlisted earlier spike contradicts explicit neuron coverage;
- any earlier arrival was either already launched and must be in the complete queue, or would require a forbidden earlier source spike.

Thus tape completeness is not assumed in order to prove tape completeness.

## Post-event updates

### Spike

Lifted phase and alpha physical state remain continuous through the spike.

The firing neuron's section index increments.

Every outgoing structural edge launches one labelled delayed arrival, including \(w=0\) edges.

Zero-delay launch/arrival simultaneity fails ordinary certification closed.

### Arrival

Propagate to the certified arrival interval and apply

\[
q_i^+=q_i^-+w_e\alpha^2,
\qquad
\psi_i^+=\psi_i^-,
\qquad
\theta_i^+=\theta_i^-.
\]

Remove exactly the processed causal queue record.

At \(w_e=0\), the state jump is identity but the labelled arrival remains in the tape.

### Horizon

Terminate certification.

## Sequential completeness theorem

Suppose:

1. the initial state/history and pending queue are certified complete;
2. at each step one strict next-event rule is proved;
3. NNE-A-SEG holds;
4. the designated event certificate is sound;
5. the post-event state and queue update are outward-valid and complete;
6. grouped/simultaneous events are rejected;
7. the construction reaches a certified horizon termination.

Then the finite labelled tape is complete and ordinary on the certified horizon.

The proof is by induction over the finite event index.

## Mathematical termination

Under the finite-event assumptions, any complete ordinary tape has finite length bounded by the spike/arrival count plus horizon sentinel.

Under additional strict-margin and segment-certifiability assumptions, the ideal unbounded-resource RIFC-TAPE refinement process eventually certifies the finite ordinary tape.

This does not imply any finite software resource budget is sufficient.

Finite production implementations may return:

`RESOURCE_EXHAUSTED / UNCERTIFIED`.

## Compact parameter-family theorem

For a compact family \(\Lambda\), one identical ordinary labelled tape is certified under recursive uniform conditions:

- fixed structural topology;
- complete uniform initial pending history;
- uniform arithmetic qualification of every segment;
- positive uniform transversality;
- strict uniform next-event separation;
- uniform boundary margin;
- uniform NNE-A-SEG;
- uniform outward post-event closure into the next qualified segment domain.

Under these conditions every represented member has the same complete ordinary label sequence, although event times/states may vary within enclosures.

No general automatic method for broad parameter-box NNE-A/post-event closure is frozen.

## Composition with RB-029

Segment arithmetic qualification may use:

- one invariant global compact qualified domain; or
- prospectively justified segment-specific domains.

If a post-event enclosure leaves all available qualified domains, sequential certification must stop fail-closed.

No single global \(B_K\) is required when segment-specific qualifications are available.

## Fail-closed taxonomy

Frozen nonpositive classes include:

- INITIAL_HISTORY_UNCERTIFIED;
- SEGMENT_ARITHMETIC_UNQUALIFIED;
- SEGMENT_ENCLOSURE_INCONCLUSIVE;
- NEXT_EVENT_ORDER_UNCERTIFIED;
- NNE_A_NOT_ESTABLISHED;
- ORDINARY_COLLISION_OR_GROUPED_EVENT;
- POST_EVENT_QUALIFIED_DOMAIN_ESCAPE;
- POST_EVENT_ENCLOSURE_FAILURE;
- RESOURCE_EXHAUSTED;
- UNSUPPORTED_CASE;
- MATHEMATICAL_CONTRADICTION.

No nonpositive class may be promoted to a positive event certificate, complete tape or physical conclusion without its independent strict proof obligations.

## RIFC-TAPE-0.1

RB-030 freezes exactly one future implementation specification:

`RIFC-TAPE-0.1 — Sequential Certified Ordinary Event-Tape Builder`.

Its deterministic cycle is:

1. maintain complete certified state/queue/tape ledger;
2. enumerate every neuron, every pending labelled arrival and horizon;
3. issue rigorous segment first-hit/no-hit queries on certified arrival-free prefixes;
4. attempt strict unique next-spike proof;
5. otherwise attempt strict unique next-arrival proof;
6. otherwise attempt strict horizon proof;
7. otherwise refine or fail closed;
8. retain complete NNE-A proof data for every accepted segment;
9. perform outward post-event update and queue bookkeeping;
10. emit `CERTIFIED_ORDINARY_TAPE` only after horizon completion and replayable proof closure.

A partial tape is never relabelled as complete.

## Frozen future validation fixtures

TT-01 through TT-10 are frozen as theory-derived, unexecuted future fixtures:

- spike before arrival;
- arrival before spike;
- two-neuron competing spikes;
- structural-zero arrival;
- near collision / inconclusive order;
- exact ordinary collision;
- horizon boundary;
- multiple sequential events;
- delayed feedback arrival generated by an earlier certified spike;
- resource-exhausted but physically ordinary case.

No fixture is treated as executed evidence by RB-030.

## Explicit non-results

RB-030 does not establish:

- grouped simultaneous-event chart theory;
- automatic broad parameter-box NNE-A;
- infinite-prehistory queue completeness;
- finite-machine unconditional termination;
- sharp/full chart radius;
- efficient correlation-aware interval representation;
- global simulator correctness;
- effect-bearing science.

## Governance boundaries

RB-030 does not modify or replace RB-024 through RB-029.

It does not:

- alter RB-015 SCIENTIFIC FAIL;
- execute RB-020/TR-27C;
- create protected RNG;
- authorize APP-3;
- authorize v0.28 effect-bearing science;
- authorize numerical implementation by itself;
- authorize novelty/manuscript claims.

## STOP

RB-030 is a scientific-theory freeze only.

STOP — FROZEN / STABLE SCIENTIFIC THEORY
