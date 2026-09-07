# CORE v0.3 Continuation Validation Execution Gate 0.1

## Authority

Execute only under:

- Governance Initialization 0.1 STABLE;
- RB-004 CORE Mathematical Freeze 0.1;
- RB-006 CORE v0.2 Benchmark Result Freeze 0.1;
- RB-007 CORE v0.3 Continuation Theory Freeze 0.1;
- RB-008 CORE v0.3 Continuation Validation Contract Freeze 0.1.

The frozen execution contract is exactly:

`research/core/v0_3_continuation_validation_contract_canonicalization_gate_0_1.md`

No scientific specification may be altered after outputs are observed.

## Task

Execute **V3C01 through V3C09 exactly as frozen under RB-008**.

You must execute every required fixed subcase and negative control. Record all outcomes, relevant residuals/errors, chart margins, derivative comparisons, synthetic continuation residuals, categorical controls and any INVALID classification explicitly permitted by the contract.

Overall gate result:

- `PASS` only if V3C01–V3C09 all PASS;
- `FAIL` if any scientifically valid required case fails;
- `CONDITIONAL` only for a genuine execution-completeness blocker that prevents meaningful PASS/FAIL classification without changing RB-008.

A valid failure is a valid result and must not be tuned away.

## Software-plumbing rule

A clerical/software-plumbing defect may be corrected only if RB-008 remains scientifically unchanged. Document:

1. defect;
2. affected code path;
3. correction;
4. why scientific specification is unchanged;
5. preliminary output invalidated by the defect;
6. complete rerun of every affected validation family from the beginning.

No parameter, test point, derivative step, chart margin, solver step, tolerance, reference, acceptance rule, benchmark membership or negative control may be changed.

## Forbidden

Do not:

- search or continue a Lighthouse branch;
- search for a Lighthouse fold or pitchfork;
- execute deferred legacy B11–B22 items outside their canonical V3C01–V3C09 replacements;
- compute/import v0.4 Floquet or stability results;
- fit normal forms or effect-bearing critical coefficients;
- perform adaptive-delay work;
- improve/refactor production/JAX continuation code beyond minimal deterministic validation plumbing;
- start v0.4+ recovery science;
- perform inference, observation design, active experiment design, application, novelty, manuscript or v0.27 work.

## Deliverable

Create:

`research/core/v0_3_continuation_validation_execution_gate_0_1.md`

It must include:

1. Git/reproducibility identity;
2. RB-008 identity;
3. execution environment;
4. harness audit trail;
5. V3C01 result;
6. V3C02 result;
7. V3C03 result;
8. V3C04 result;
9. V3C05 result;
10. V3C06 result;
11. V3C07 result;
12. V3C08 result;
13. V3C09 result;
14. complete suite table;
15. failures/INVALID/blockers, if any;
16. tuning statement;
17. overall gate decision PASS / FAIL / CONDITIONAL;
18. proposed MASTER result-freeze contents only if justified;
19. explicit exclusions;
20. STOP.

Then update `research/core/STATUS.md` to `RETURN TO MASTER` or `BLOCKED`.

## STOP

After the deliverable and CORE STATUS update, stop.

No second gate may be started.

STOP — RETURN TO MASTER
