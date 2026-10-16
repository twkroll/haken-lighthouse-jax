# NUM-ENG RIFC-0.1 — finite outward-interval certification (Gate 0.4)

Status: isolated **engineering/validation** artifact, not scientific evidence. Reference model and RB-019/RB-021 physical authority were not modified.

Frozen pre-execution contract is in Git: `research/numerical_engineering/rifc_interval_implementation_validation_contract_0_4.md`, creation commit `2aa95c77973fe63a82a7cf11472ee92273b5bb7c`.

Backend contract: GNU MPFR 4.2.2 correctly rounded primitive operations / `mpfr_exp` under `MPFR_RNDD` and `MPFR_RNDU`. This assumes MPFR's published correct-rounding contract and correct binary ABI. Compact finite fixtures only. **IR-A4-R and its whole-expression rate constants not established**; no eventual-certification theorem is claimed. No general full chart / NNE-A certificate, no global physical simulator guarantee.

Data: the six positive JSON certificates in `certificates/` include exact input rationals, per-cell psi/response/gain, all outward prefix intervals, strict inequalities, time bracket/transversality where applicable, and topology/event identity. `source/audit_saved_certificates.py` independently replays their interval proofs without executing the physical simulator. A saved SHA256 manifest allows byte checking; hashes are not a cryptographic attestation of the scientific truth.

Usage from unpacked archive:

```bash
export PYTHONPATH="$PWD/source"
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 pytest -q source/test_rifc_gate04.py
python source/audit_saved_certificates.py certificates
python source/generate_certificate_artifacts.py certificates
```

Compatibility check was performed separately in the unchanged previous local source tree:
`PYTHONPATH=. ... pytest -q tests/test_reference.py tests/test_rri_repair_v01.py tests/test_gate02_batch_guard.py` (28 passed, clean exit).

QA chronology: first 24-case run had one erroneous assertion in a max-interval unit test; fixed the assertion without changing the backend/contract. Expanded 26-case run initially exposed an exact-horizon classification ordering issue and excessive rational endpoint size for extremely tiny exponentials; both engineering code errors were corrected conservatively. The final 26-test suite was run twice cleanly. All initial failing logs retained for provenance.

Output vocabulary: positive `CERTIFIED_NO_HIT`, `CERTIFIED_REGULAR_HIT`, `CERTIFIED_EVENT_ORDER`, `CERTIFIED_STRUCTURAL_ARRIVAL`; nonpositive `ASSUMPTION_VIOLATED`, `STRICT_MARGIN_ABSENT`, `ENCLOSURE_INCONCLUSIVE`, `RESOURCE_EXHAUSTED`, `UNCERTIFIED_ARITHMETIC`, `ORDINARY_CHART_INVALID`, `UNSUPPORTED_CASE`. **`CERTIFIED_ORDINARY_CHART` intentionally NOT emitted.** Bracketing certifier is only for a single arrival-free segment with a known exact starting state and scalar parameters.

Frozen science unchanged: RB-015 SCIENTIFIC FAIL; RB-020/TR-27C parked; reserved 2711xxx streams ungenerated; APP-3 parked.
