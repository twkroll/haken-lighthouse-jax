# MASTER Prompt — NUM-ENG RIFC Source-Graph Arithmetic Propagation & Idealized IR-A4-R Qualification Gate 0.7

## Purpose

Close the analytical gap left after RB-027 without modifying any executable source.

Gate 0.7 must distinguish rigorously between:

1. the finite resource-bounded Gate-0.6 executable implementation; and
2. an idealized unbounded-precision RIFC arithmetic family with the same positive-certificate expression graph and exact-dyadic endpoint semantics.

The gate must attempt to prove or refute the whole-expression IR-A4-R bound for that idealized family and establish the exact correspondence of finite Gate-0.6 executions to finite members of the idealized family.

This is an analytical numerical-engineering qualification gate.

No source repair, performance work, stochastic experiment, full multi-event/NNE-A expansion or scientific effect execution is authorized.

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
- RB-027
- current MASTER / CORE / NUM-ENG STATUS files.

Work only on:

`engineering/numerics-v0.1`.

The physical authority remains:

`NUMENG_PULSE_AWARE_REFERENCE_V1`.

No executable source modification is authorized in Gate 0.7.

## Pre-analysis contract

Before producing any new Gate-0.7 analytical result or validation output, create and commit:

`research/numerical_engineering/rifc_source_graph_ir_a4r_proof_contract_0_7.md`.

The contract must prospectively freeze:

1. exact Gate-0.6 source SHA-256 and blob identity;
2. exact RB-025 baseline source identity;
3. exact idealized arithmetic-family definition;
4. exact compact domain \(K_{0.7}\);
5. exact positive-certificate expression graph;
6. exact primitive rounding model;
7. exact exact-dyadic serialization semantics;
8. exact dependency/range-width versus arithmetic-excess definitions;
9. exact nodewise norm and error-propagation convention;
10. exact Lipschitz/derivative constants or overbounds to be proved;
11. exact operation-count recurrence/bound;
12. exact target form of \(B_K\);
13. exact refinement schedule \(p_n=128+8n\), \(m_n=2^n\);
14. exact finite-source correspondence statement;
15. exact validation checks permitted only after analytical PASS;
16. exact PASS / NO-GO / BLOCKED outcome rules.

No compact-domain shrinking, graph simplification, constant fitting or proof-target weakening is allowed after outputs are inspected.

## A. Idealized arithmetic family

Define one mathematical family, denoted for example \(\mathrm{RIFC}_\infty\), with:

- the same positive-certificate arithmetic graph as Gate-0.6 `rifc_mpfr_v0_2.py`;
- arbitrary precision \(p\ge128\);
- sufficiently wide exponent/integer resources for every finite level \(n\);
- correct directed rounding matching MPFR semantics;
- exact dyadic export adding zero arithmetic error;
- the same threshold-safe response branch logic;
- the same dyadic Darboux/prefix construction;
- the same strict no-hit/hit certificate inequalities.

This abstraction must remove only finite machine-resource caps.

It must not alter the mathematical arithmetic graph or certificate logic.

## B. Finite-source correspondence

Prove a correspondence statement of the form:

For every Gate-0.6 executable call that remains within its frozen precision/exponent/integer/`nmax` resource domain, the arithmetic/certificate result equals the corresponding finite member of \(\mathrm{RIFC}_\infty\) under the same directed backend semantics and exact inputs.

Any branch present in executable positive-certificate logic but absent from the idealized family is a BLOCKER.

Resource failures may map only to fail-closed nonpositive outcomes; they cannot be silently omitted from the correspondence statement.

## C. Primitive arithmetic bounds

On the frozen compact domain derive explicit directed-rounding excess bounds for every primitive that can affect a positive certificate:

- exact rational endpoint load into directed precision-\(p\) arithmetic;
- addition;
- subtraction;
- multiplication;
- permitted division with explicit denominator margin;
- exponential;
- square root if present in positive certificate paths;
- exact comparison/hull/intersection operations where relevant.

Exact-dyadic serialization must contribute exactly zero additional arithmetic excess.

Do not use finite empirical measurements to define the primitive constants.

## D. Response-graph propagation

For all frozen response branches:

1. below threshold;
2. threshold-straddling monotone branch;
3. strictly above threshold reciprocal-square/exponential branch;

derive explicit arithmetic-excess propagation bounds.

For the above-threshold branch, prove a positive compact-domain lower bound on \(x-h\).

If no single compact-domain bound covers every frozen branch, state a finite branchwise constant and prove a uniform maximum over the prospectively frozen domain.

## E. Alpha-state propagation

For the frozen arrival-free graph

\[
q(s)=e^{-\alpha s}q_0,
\qquad
\psi(s)=e^{-\alpha s}(\psi_0+s q_0),
\]

derive nodewise arithmetic-excess propagation with explicit finite constants on \(K_{0.7}\).

Keep exact interval dependency/range width separate from arithmetic excess.

## F. Darboux cell and prefix propagation

For one cell, derive the arithmetic-excess map for:

- dyadic time endpoints;
- state enclosure;
- response enclosure;
- cell gain;
- prefix accumulation.

Then derive an explicit source-graph operation-count overbound

\[
N_n\le a2^n+b.
\]

The constants \(a,b\) must be prospectively defined/proved, not inferred from runtime.

## G. Whole-expression IR-A4-R theorem

Produce exactly one analytical outcome.

### G-PASS

Prove a finite compact-domain constant \(B_K\), independent of \(n\) and \(p_n\), such that

\[
E_{\rm arith}(n)
\le
B_K N_n2^{-p_n}
\]

for the idealized family and all \(n\ge0\), with

\[
p_n=128+8n.
\]

Then prove

\[
E_{\rm arith}(n)\to0.
\]

The bound may be extremely conservative.

It must nevertheless be explicit and finite.

### G-NO-GO

Produce a rigorous counterexample showing that no finite \(B_K\) of the frozen target form can exist for the prospectively frozen idealized family/domain.

Do not repair the graph or shrink the domain inside Gate 0.7.

### G-BLOCKED

Use only if the source/idealized-family correspondence cannot be established or a necessary backend theorem is unavailable.

## H. Eventual-certification semantics

If G-PASS is established, state carefully:

- RB-024 eventual certification applies to the idealized unbounded family under its strict-margin assumptions;
- a finite resource-bounded production call remains permitted to return `RESOURCE_EXHAUSTED / UNCERTIFIED`;
- no finite hardware execution can be equated with the mathematical unbounded limit merely because the idealized theorem holds.

Gate 0.7 must not claim an impossible finite-machine guarantee of unlimited resources.

## I. Post-proof validation

Only if G-PASS is analytically established, run a prospectively frozen finite consistency suite that checks:

- actual Gate-0.6 finite arithmetic widths are below the proved idealized bounds for selected levels/precisions within executable resources;
- finite strict no-hit and regular-hit fixtures behave consistently with the idealized theorem;
- deliberately insufficient `nmax` still returns `RESOURCE_EXHAUSTED / UNCERTIFIED`.

Observed values may check implementation correspondence but may not determine \(B_K\).

## J. Non-goals

Do not:

- modify Gate-0.6 or RB-025 source;
- lift production resource caps in code;
- implement full sequential multi-event certification;
- implement NNE-A / chart-radius machinery;
- perform performance/scaling work;
- execute TR-27C;
- execute APP-3;
- generate protected RNG;
- make novelty/manuscript claims.

## Result classes

Every material result must be classified as one of:

- IDEALIZED SOURCE-GRAPH CORRESPONDENCE ESTABLISHED;
- IR-A4-R IDEALIZED FAMILY ESTABLISHED;
- IR-A4-R IDEALIZED FAMILY NOT ESTABLISHED;
- FINITE EXECUTION CORRESPONDENCE ESTABLISHED;
- ANALYTICAL NO-GO;
- BLOCKED;
- DEFERRED.

## Full PASS criteria

Full Gate-0.7 PASS requires:

1. prospective contract committed before analytical outputs;
2. no source modification;
3. exact idealized-family definition;
4. complete positive-certificate graph correspondence;
5. explicit primitive and branchwise error bounds;
6. explicit \(N_n\) operation-count bound;
7. explicit finite \(B_K\);
8. proof that \(E_{\rm arith}(n)\to0\);
9. finite post-proof consistency checks pass;
10. finite production-resource limitations remain explicitly separate from the idealized theorem.

## Required outputs

On `engineering/numerics-v0.1`, create:

1. `research/numerical_engineering/rifc_source_graph_ir_a4r_proof_contract_0_7.md`
2. `research/numerical_engineering/rifc_source_graph_ir_a4r_qualification_gate_0_7.md`
3. a mathematical derivation artifact containing all constants and recurrences;
4. source/idealized-family correspondence artifact;
5. finite post-proof validation logs only if analytical PASS;
6. complete provenance/manifest.

Update:

`research/numerical_engineering/STATUS.md`

to RETURN TO MASTER or BLOCKED.

## Recommendation

If G-PASS succeeds, recommend a bounded qualification freeze stating:

- IR-A4-R established for the idealized unbounded-precision source family on the frozen compact domain;
- finite Gate-0.6 executions correspond to finite family members within resource limits;
- production finite resource exhaustion remains fail-closed and is not contradicted by the idealized eventual-certification theorem.

Do not claim full multi-event certification.

## STOP

STOP — RETURN TO MASTER
