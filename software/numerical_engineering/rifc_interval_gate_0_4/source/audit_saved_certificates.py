"""Independent executable proof-artifact replayer: NO physical simulator involved."""
import hashlib,json,sys
from pathlib import Path
from rifc_mpfr_v0_1 import audit_certificate
p=Path(sys.argv[1]); entries=json.loads((p/'CERTIFICATE_MANIFEST.json').read_text())
for x in entries:
    body=(p/x['path']).read_bytes()
    assert hashlib.sha256(body).hexdigest()==x['sha256'], 'hash mismatch'
    cert=json.loads(body)
    assert cert['status']==x['class']
    assert audit_certificate(cert), 'not outward-auditable '+x['path']
print(f'AUDIT PASS: {len(entries)} positive certificate proofs; zero physical simulation calls')
