# MASTER Prompt — CORE Sequential Event-Tape & NNE-A Certification Theory Gate 0.3

## Purpose

Extend RB-024 single-segment rigorous first-hit/event-order certification into a finite-horizon ordinary sequential event-tape theory.

The central open problem is NNE-A: proving that no unlisted/new event appears between already certified labelled events.

Develop one constructive theory and algorithm specification for sequential ordinary-chart certification.

This is a THEORY gate only.

No numerical execution is authorized.

## Mandatory authorities

Read and obey:

- PROJECT_GOVERNANCE.md
- research/master/command_protocol_v0_2.md
- RB-004
- RB-012
- RB-022
- RB-024
- RB-029
- RB-019/RB-021/RB-023/RB-025/RB-027/RB-028 as engineering evidence only
- current MASTER / CORE / NUM-ENG STATUS files.

RB-015 remains immutable SCIENTIFIC FAIL.

## S1 — finite-horizon event-count foundation

Use the frozen Lighthouse model to derive explicit sufficient finiteness statements on a finite horizon \(H\).

Exploit where legitimate:

\[
0\le S(\psi)<1
\]

and the lifted phase section spacing \(2\pi\) to bound spike counts per neuron.

Include fixed delayed structural arrivals and finite in-flight history assumptions.

State exact assumptions needed for the total labelled event list on \([0,H]\) to be finite.

Do not assume the desired tape is finite without proof/assumption.

## S2 — state/tape semantics

Define a sequential certified state containing at least:

- current certified time interval or exact time;
- phase/state interval enclosure;
- alpha states;
- labelled pending structural arrivals;
- structural topology including zero-weight edges;
- current event index;
- horizon;
- accumulated proof data.

Distinguish exact singleton trajectory certification from parameter-family boxes.

## S3 — candidate next events

At each ordinary step, formalize the candidate set:

- all pending labelled arrivals;
- one possible first spike for each neuron over the current arrival-free segment;
- horizon.

Specify how RB-024 RIFC segment certificates generate:

- certified no-hit;
- certified regular-hit bracket;
- inconclusive/resource outcomes.

## S4 — certified next-event rule

Derive a sufficient rule under which exactly one labelled candidate is proven to be the next ordinary event.

Examples of acceptable logic:

- a certified spike bracket lies strictly before every competing arrival interval and all competing neurons are certified not to hit before that bracket;
- a labelled arrival interval lies strictly before every spike candidate and other arrivals;
- horizon lies strictly before every possible event.

The rule must be stated with outward interval inequalities, not point estimates.

## S5 — no-new-event completeness (NNE-A)

State and prove a constructive NNE-A condition on one inter-event segment.

It must account for every neuron and every structural arrival.

For a designated next spike, competitors must be excluded on the entire prefix relevant to the certified next-event time.

For a designated next arrival, all neurons must be excluded before that arrival.

Structural-zero arrivals must remain candidates.

Show that satisfying NNE-A at every certified segment excludes insertion of an unlisted event.

## S6 — post-event enclosure propagation

For each ordinary event type:

- spike launch;
- delayed structural arrival;
- horizon termination;

derive the certified post-event state/tape update.

Preserve topology-fixed zero-weight semantics.

If simultaneous/grouped events occur or event intervals overlap without strict order, ordinary sequential certification must fail closed unless already covered by frozen commuting-event theory.

## S7 — induction theorem for a whole finite tape

Prove an induction theorem:

If the initial state/history is certified and each step satisfies the segment-level certificate, strict next-event ordering, NNE-A and post-event enclosure obligations, then the resulting finite labelled tape is complete and ordinary on the certified horizon.

State precisely what “complete” means.

Do not conflate completeness of the labelled tape with uniqueness over an entire broad parameter family unless separately assumed/proved.

## S8 — termination and no-Zeno

Establish a finite-horizon termination theorem or sufficient conditions.

Separate:

- spike-count finiteness from phase-rate bound;
- arrival-count finiteness induced by finitely many launches/edges and finite in-flight history;
- algorithmic finite-resource exhaustion.

Mathematical finite event count does not imply finite software resources are sufficient.

## S9 — parameter-family extension

Determine what additional assumptions are required to certify one identical ordinary tape for a compact parameter box.

At minimum address:

- uniform transversality;
- uniform event separation;
- uniform boundary margin;
- uniform NNE-A;
- fixed structural topology;
- uniform post-event enclosure closure.

If a full parameter-box theorem is possible, prove it.

Otherwise freeze a weaker sufficient proposition and keep sharp/general parameter-box NNE-A OPEN.

## S10 — relationship to RB-029 arithmetic qualification

State how segment-level arithmetic qualification composes with sequential tape certification.

A segment positive certificate may rely on a compact-domain \(B_K\) qualification, but the sequential theorem must not assume one global \(B_K\) if segment states leave the qualified domain.

Specify whether per-segment domain qualification or one invariant global domain is sufficient.

## S11 — failure taxonomy

Distinguish at least:

- segment arithmetic unqualified;
- segment enclosure inconclusive;
- no strict next-event order;
- NNE-A not established;
- ordinary collision/grouped event;
- post-event enclosure leaves qualified domain;
- resource exhaustion;
- mathematical contradiction.

All nonpositive cases must fail closed.

## S12 — constructive algorithm

End with exactly one deterministic algorithm specification:

`RIFC-TAPE-0.1 — Sequential Certified Ordinary Event-Tape Builder`.

Specify:

1. inputs;
2. state data;
3. candidate enumeration;
4. segment RIFC calls;
5. next-event decision rule;
6. NNE-A proof data;
7. post-event update;
8. stopping conditions;
9. failure labels;
10. certificate artifact structure.

## S13 — future deterministic fixtures

Define a finite theory-derived fixture family for later NUM-ENG validation, including at least:

- spike before arrival;
- arrival before spike;
- two-neuron competing spikes;
- structural-zero arrival;
- near collision / inconclusive order;
- exact ordinary collision;
- horizon boundary;
- two or more sequential events;
- delayed feedback arrival generated by an earlier certified spike;
- resource-exhausted but physically ordinary case.

No execution in CORE.

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

- no numerical execution;
- no source modification;
- no empirical tuning;
- no protected RNG;
- no TR-27C;
- no APP-3;
- no effect-bearing science;
- no novelty/manuscript claims.

## Required output

Create:

`research/core/sequential_event_tape_nne_a_certification_theory_gate_0_3.md`

and update CORE STATUS to RETURN TO MASTER or BLOCKED.

## Decision

PASS only if one coherent constructive sequential ordinary-tape theorem and algorithm is established, with explicit NNE-A and finite-horizon termination logic.

If completeness still depends on an unstated assumption that no extra event appears, return CONDITIONAL/BLOCKED.

## STOP

STOP — RETURN TO MASTER
