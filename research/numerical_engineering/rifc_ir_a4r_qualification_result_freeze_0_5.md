# NUM-ENG IR-A4-R Qualification Result Freeze 0.5

Date: 2026-10-16
Status: FROZEN / STABLE ENGINEERING NEGATIVE QUALIFICATION RESULT
Rollback point: RB-026

## Authority

MASTER reviews and accepts the returned:

\`NUM-ENG MPFR IR-A4-R Qualification & Eventual-Certification Gate 0.5\`

from branch:

\`engineering/numerics-v0.1\`.

Frozen provenance:

- pre-execution Gate-0.5 contract commit:
  \`20d9ae3c5973b5226387c5f679c9ae03c1e58973\`;
- contract blob SHA:
  \`4e0ab6963c0c84e023c7e94fc4080a0456e7bc1e\`;
- returned gate blob SHA:
  \`faab42ba63400a0a9b8f7603c05251ec8f6c2f98\`;
- frozen RB-025 source blob:
  \`6df6740e86344628a2b9583f0a3f719f9d5817f8\`;
- frozen RB-025 source SHA-256:
  \`0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539\`;
- MPFR runtime:
  GNU MPFR 4.2.2;
- MPFR shared-library SHA-256:
  \`4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c\`.

RB-025 remains unchanged and authoritative for finite certificate soundness.

RB-024 remains unchanged and authoritative for the rigorous interval theory.

## Frozen Gate-0.5 result

\`IR-A4-R NOT ESTABLISHED — SOURCE-LEVEL ANALYTICAL NO-GO\`.

This is an engineering qualification result.

It is not:

- a failure of MPFR correct rounding;
- a contradiction of RB-024;
- a revocation of RB-025 finite certificate soundness;
- a scientific effect result.

## Prospective negative-control discipline

Before Gate-0.5 diagnosis, the frozen contract fixed:

- compact domain \(K=[-100000,100000]\);
- exact source identity;
- exact backend identity;
- exact source expression graph;
- exact counterexample candidate arising from
  \(S(1/100)=\exp(-10000)\);
- exact diagnostic precisions
  \(p\in\{128,256,512,2048,4096\}\);
- Q7/Q8 as forbidden unless the analytical Q5 rate qualification first passed.

No source repair, domain shrinking, empirical rate fitting or post-output fixture change occurred inside Gate 0.5.

## Analytical blocker

The frozen RB-025 serializer \`M.val\` contains an algorithm-level small-value branch:

- if the MPFR binary exponent is below \(-2048\),
- the directed lower/upper conversion is widened to a dyadic floor involving \(2^{-2048}\),
- independent of requested precision \(p\).

For the prospectively fixed singleton:

\[
x=\frac1{100},\qquad r=1,\qquad h=0,
\]

the exact response is

\[
S(x)=\exp(-10000).
\]

Using \(e>2\),

\[
0<\exp(-10000)<2^{-10000}<2^{-2048}.
\]

The frozen source therefore serializes the directed response interval as

\[
[0,2^{-2048}]
\]

for every tested and, by source logic, every supported precision once this branch is taken.

Hence the arithmetic excess width has a precision-independent lower floor

\[
2^{-2048}.
\]

A uniform bound

\[
\operatorname{excwid}
\le C_K2^{-p}
\]

for all \(p\) would require

\[
C_K\ge 2^{p-2048},
\]

which is unbounded as \(p\to\infty\).

Therefore no finite \(C_K\) exists for the implemented Python+MPFR graph on the frozen Gate-0.5 domain.

Consequently the RB-024 IR-A4-R obligation and the derived whole-expression \(B_K\) rate cannot be established for the RB-025 source.

## Diagnostic confirmation

The prospectively fixed precisions:

\[
128,\ 256,\ 512,\ 2048,\ 4096
\]

all reproduce the same interval:

\[
[0,2^{-2048}]
\]

for both:

- direct \(\exp(-10000)\);
- the composed Lighthouse response at \(x=1/100\).

These runs validate the diagnosed mechanism only.

They are not used to fit \(C_K\) or \(B_K\).

## Correctly withheld work

Because the analytical prerequisite failed:

- no Q7 empirical rate-fitting exercise was performed;
- no Q8 eventual-certification fixture was used as a substitute for proof.

The hard finite \`nmax<=16\` implementation budget remains correctly separated from any mathematical eventual-certification statement.

## RB-025 preservation

RB-025 remains:

\`FROZEN / STABLE ENGINEERING CERTIFICATION LAYER — FINITE SOUNDNESS ONLY\`.

Its source is not modified by RB-026.

Gate 0.5 confirms:

- finite certificate soundness remains preserved;
- 26/26 RB-025 targeted tests still pass;
- 6/6 saved positive certificate replays still pass.

The fixed serialization floor is inclusion-widening and therefore compatible with finite positive soundness, while blocking the requested precision-rate theorem.

## Component classification

### FINITE SOUNDNESS PRESERVED

- RB-025 positive finite certificates;
- MPFR directed-rounding contract;
- existing finite proof replay.

### REPAIR-REQUIRED

- exact-dyadic serialization path used by \`M.val\` for very small nonzero MPFR values.

### IR-A4-R NOT ESTABLISHED

- primitive/full-expression rate for the unchanged RB-025 source;
- eventual-certification implementation qualification.

### DEFERRED

- whole-expression \(B_K\) for a repaired source;
- eventual-certification validation after successful requalification;
- full sequential multi-event RIFC;
- NNE-A / full parameter-box chart radius.

## Governance boundaries

RB-026 does not modify:

- RB-025;
- RB-024 or any prior scientific freeze;
- RB-015 SCIENTIFIC FAIL;
- RB-020;
- any protected RNG state.

It does not authorize:

- TR-27C execution;
- APP-3;
- v0.28 effect-bearing science;
- executable-source merge to \`main\`;
- novelty/manuscript claims.

## STOP

RB-026 freezes only the negative Gate-0.5 engineering qualification result.

STOP — FROZEN / STABLE ENGINEERING NEGATIVE QUALIFICATION RESULT
