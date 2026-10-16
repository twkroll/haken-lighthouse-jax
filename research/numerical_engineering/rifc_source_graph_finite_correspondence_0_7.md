# Gate 0.7 — finite Gate-0.6 / idealized-family source correspondence

Date: 2026-10-16
Scope: analytical source audit, no executable edits.
Frozen executable: `software/numerical_engineering/rifc_interval_gate_0_6/source/rifc_mpfr_v0_2.py`.
SHA256: `a447f9a4d9d2be80243a21f4a47cb04d0c5ca2e9dd360b78de4b99cb68067202`; blob `1b94cf36447f428a9968c90ac3c0e74c18494d1c`.
Frozen proof contract: `d6b76886663a911a85e4b684825b3047e517b754`.

## Allowed idealization

For each finite p>=128 and n>=0, construct a purely mathematical directed-rounding implementation with exactly the same scalar/interval computational graph, integer/Fraction exact endpoints, dyadic segmentation, response branch tests, and certificate inequalities as Gate 0.6. The only differences are eliminating finite implementation limits: p<=8192, exponent/significand/integer sizes, proof-text size, and nmax<=16. A mathematical idealization of MPFR correct rounding is assumed; no hardware permits literally infinite exponent storage or memory.

## Branch inventory and correspondence

- `M` and `_fraction_round`: rational numerator/denominator MPFR directed integer parsing and directed quotient; returns exactly directed-rounded fractions. For finite allowed data, same bits in both models.
- `M.val`: MPFR/GMP `mpfr_get_z_2exp` plus exact integer-to-Fraction conversion. No precision-dependent truncation. In finite allowed cases no resource failure and exact same dyadic output; in ideal family no caps.
- `I.point/bounds/_op`: load endpoints, interval +,-,*,/, exact compare/hull/intersect/min/max; identical finite directed images and branch comparisons.
- `I.exp`: exact same directed correctly-rounded exp input and result.
- `I.sqrt`: only a helper; never called by the positive K01–K06 first-hit or structural certificate paths. Remains same correctly-rounded scalar operation if independently invoked, but not included in the theorem's narrower positive-family claim.
- `psi_interval/q_interval`: same arrival-free alpha formula. K01–K04 have exact q0=0 and alpha=1.
- `response`: exactly same below, straddling and above threshold branches; noncircular gap margin on frozen K is established in companion proof before applying global Lipschitz overbounds.
- `darbouxs`: exactly same dyadic cell times `kL/2^n`, interval gain, and prefix propagation with p_n=128+8n. Source's `nmax<=16` cap is outside cell arithmetic itself.
- `certify`: exactly same phase-gap comparison, no-hit check, search for strict regular-hit bracket and response lower bound, then positive proof-data generation. Ideal removes only the input nmax>16 rejection to allow arbitrary n. A particular finite invocation that stays within caps uses same n levels and stops identically.
- `event_order`: exact Fraction ordering, overlapping event intervals remain inconclusive, exact ties invalid. The ideal family does not declare a whole-chart certificate.
- `structural_arrival`: same labelled zero/cross-zero topology, interval alpha^2 jump, exact boundary/competitor checks.
- `artifact_json/audit_certificate`: exact persisted rational proof-data and independent replay; ideal removes only text/integer length caps. Serialization has zero arithmetic error for valid finite inputs.
- `eta_mass_tail/response_slope_bound/omitted_history_phase_error_bound/transversality_class`: ancillary numerical helpers are not part of the frozen K01–K06 positive-certificate arithmetic path; this narrow gate proves no uniform rate for their arbitrary arguments.

## Correspondence theorem

By structural induction over each fixed finite arithmetic DAG, corresponding intermediate endpoints are equal because both versions begin with the same exact rational inputs and perform the same directed correctly rounded primitive operations. Their `Fraction` export is exact and all comparisons select the same branches. Induction over the fixed finite Darboux cell list and source prefix summation preserves equality of every computed endpoint. The same strict certification inequalities give the same classification and proof data. This proves **FINITE EXECUTION CORRESPONDENCE ESTABLISHED** for every Gate-0.6 execution satisfying all its resource bounds, *assuming* the binary MPFR ideal correct-rounding contract and the captured ABI semantics. For calls beyond the finite bounds, source fails closed; no positive source certificate is inferred. Memory and CPU costs are not bounded by this logical theorem.

The idealized IR-A4-R arithmetic-rate claim is restricted to the precommitted K01–K06 input families; this correspondence result does not reclassify arbitrary external parametric graph inputs as being inside K.

## Exclusions

No changes to frozen RB-025, RB-027, the physical authority, JAX guards, scientific/freezes, benchmark seeds, CORE or APP-3. No executable source modifications in Gate 0.7.
