# NUM-ENG RIFC Exact-Dyadic Serialization Repair Freeze 0.6

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING REPAIR BASELINE — FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED
Rollback point: RB-027

## Authority

MASTER reviews and accepts the returned:

\`NUM-ENG MPFR Exact-Dyadic Serialization Repair & IR-A4-R Requalification Gate 0.6\`

from branch:

\`engineering/numerics-v0.1\`.

Frozen provenance:

- Gate-0.6 pre-repair / pre-execution contract commit:
  \`779c8f05256406c5684d4dec35ae123a418027fb\`;
- contract blob SHA:
  \`efd03c296a58b35d4f4a193a93ed29a3b8dbbdf4\`;
- returned gate blob SHA:
  \`dd5f7207e63b3b70388659050bb9b3fde9d3401e\`;
- repaired source path:
  \`software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py\`;
- repaired source SHA-256:
  \`a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202\`;
- exact-dyadic / IR-A4-R proof artifact blob:
  \`9e432e5abaeed3226a860c8baddcc3d2e72cb285\`;
- backend:
  GNU MPFR 4.2.2 + GNU GMP 6.3.0;
- MPFR shared-library SHA-256:
  \`4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c\`;
- GMP shared-library SHA-256:
  \`d15e1585c6c267296459570c8ac217ca9123044bcd4e896d2f686b32333445d2\`.

The RB-025 source remains immutable and byte-identical:

- blob:
  \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`;
- SHA-256:
  \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`.

RB-026 remains historically valid for the old RB-025 serializer.

## Gate result

\`SERIALIZATION REPAIR VALIDATED / FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED\`.

This is a bounded engineering repair result.

Full Gate-0.6 PASS for eventual certification is not claimed.

## Frozen repair

The Gate-0.5 fixed tiny-value serialization floor is removed only in the new versioned Gate-0.6 source.

The repaired path uses an exact MPFR/GMP dyadic export:

\[
y_p=z\,2^e
\]

for each already directed-rounded finite MPFR value \(y_p\).

The accepted conversion path uses:

- \`mpfr_get_z_2exp\` to obtain an exact integer significand and exponent;
- exact GMP integer serialization;
- integer-only Python reconstruction;
- exact \`Fraction\` construction.

The conversion adds zero numerical rounding error beyond the already directed-rounded MPFR endpoint.

No:

- Python float;
- \`math.exp\`;
- decimal numerical roundtrip;
- unproved \`nextafter\`;
- fixed underflow floor;
- precision-independent widening

enters the repaired endpoint conversion.

## Resource-safe finite domain

The accepted Gate-0.6 implementation remains deliberately resource-bounded.

Frozen finite guards include:

- precision \(2\le p\le8192\);
- \(|e|\le131072\);
- significand bound approximately tied to \(p\);
- exact rational numerator/denominator bit-length bounds;
- finite \`certify\` refinement budget with \`nmax<=16\`.

Unsupported resource cases fail closed.

No outward fallback that would recreate a fixed serialization floor is accepted into RB-027.

## Gate-0.5 counterexample closure

For the prospectively frozen Gate-0.5 response point

\[
S(1/100)=\exp(-10000),
\]

the new exact serializer no longer produces the artificial fixed interval

\[
[0,2^{-2048}].
\]

At all five predeclared precisions

\[
p\in\{128,256,512,2048,4096\},
\]

the directed MPFR endpoints are exported exactly and remain strictly below \(2^{-2048}\) while enclosing the independently checked high-precision value.

This closes the specific source-level blocker frozen by RB-026 for the new versioned source only.

RB-026 is not relabelled or erased.

## Finite-soundness regression

Frozen Gate-0.6 QA:

- new exact-serialization/resource tests: 19/19 PASS;
- original Gate-0.4 RIFC tests on repaired source: 26/26 PASS;
- original Gate-0.4 RIFC tests on unchanged RB-025 source: 26/26 PASS;
- combined RIFC regression: 71/71 PASS, clean exit;
- physical/reference/JAX compatibility subset: 28/28 PASS, clean exit;
- six original RB-025 certificate artifacts replay PASS under the unchanged old auditor;
- at least six ordinary repaired positive artifacts plus the extended tiny-response no-hit proof replay PASS under the repaired auditor;
- branch manifest/provenance consistency: PASS as reported by Gate 0.6.

These are finite engineering-validation results only.

## IR-A4-R status

IR-A4-R remains:

\`NOT ESTABLISHED\`.

The exact serializer removes the previously proven fixed-rate obstruction, but Gate 0.6 does not prove a complete source-wide constant

\[
B_K<\infty
\]

such that

\[
E_{\rm arith}(n)\le B_K N_n2^{-p_n}
\]

for the entire positive-certificate expression graph.

A conservative operation-count bound

\[
N_n\le1024\,2^n+1024
\]

is retained as an engineering proof candidate, not as a completed whole-expression qualification.

## Finite implementation versus eventual theorem

The repaired source enforces finite resource caps.

In particular:

- \(p\le8192\);
- \`certify\` rejects \`nmax>16\`.

The RB-024 theoretical refinement schedule

\[
p_n=128+8n
\]

is an unbounded mathematical family.

Therefore the finite executable source cannot itself be identified with an unbounded refinement process.

This does not contradict RB-024.

It means that:

- finite positive certificates remain sound;
- finite resource exhaustion remains \`RESOURCE_EXHAUSTED / UNCERTIFIED\`;
- implementation-wide eventual certification is not frozen.

## Component classification

### ENGINEERING-APPROVED

- exact MPFR/GMP dyadic endpoint export in the versioned Gate-0.6 source;
- finite resource fail-closed behavior;
- finite certificate serialization/replay tooling;
- regression/provenance harness.

### FINITE SOUNDNESS PRESERVED

- RIFC finite no-hit/hit certification semantics within the tested finite envelope;
- RB-025 compatibility.

### IR-A4-R NOT ESTABLISHED

- complete source-graph arithmetic propagation bound;
- unbounded eventual-certification implementation semantics.

### DEFERRED

- idealized unbounded-precision source-family qualification;
- production-resource correspondence to such a family;
- full sequential multi-event tape certification;
- NNE-A / parameter-box chart radius.

## Governance boundaries

RB-027 does not modify or replace:

- RB-025;
- RB-026;
- RB-024 or any earlier scientific freeze;
- RB-015 SCIENTIFIC FAIL;
- RB-020;
- protected RNG state.

It does not authorize:

- TR-27C execution;
- APP-3;
- v0.28 effect-bearing science;
- full multi-event/NNE-A work;
- executable-source merge to \`main\`;
- novelty/manuscript claims.

## STOP

RB-027 freezes the bounded exact-dyadic engineering repair only.

STOP — FROZEN / STABLE ENGINEERING REPAIR BASELINE — FINITE SOUNDNESS PRESERVED / IR-A4-R NOT ESTABLISHED
