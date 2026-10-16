"""Reproducible finite proof artifacts from committed Gate-0.4 fixed inputs.
No stochastic evidence, no scientific benchmark, no physical simulator replacement.
"""
import hashlib,json,platform,sys,ctypes.util,os
from pathlib import Path
from fractions import Fraction as F
from rifc_mpfr_v0_1 import (certify,event_order,structural_arrival,
                            artifact_json,artifact_sha,audit_certificate,VERSION)

out=Path(sys.argv[1] if len(sys.argv)>1 else 'certificates');out.mkdir(parents=True,exist_ok=True)
args={
 'S01_strict_no_hit':(1,1,1,0,0,1,F(1,4)),
 'S02_regular_hit':(1,1,-1,0,0,4,1),
 'S03_narrow_pulse_hit':(1000,1,F(1,10),0,4000000,F(1,50),F(1,200))}
objects={}
for label,par in args.items():
    cert=certify(*par,nmax=10,topology=('fixed_topology_e0',) if label.endswith('pulse_hit') else ())
    if not cert['status'].startswith('CERTIFIED_') or not audit_certificate(cert):
        raise RuntimeError(f'could not audit positive {label}: {cert["status"]}')
    objects[label]=cert
objects['S10_strict_event_order']=event_order(['1/4','1/3'],['1/2','2/3'],initial=0,horizon=1)
objects['S13_zero_weight_arrival']=structural_arrival('e0',F(1,2),[0,0],1,horizon=1)
objects['S13_cross_zero_weight_arrival']=structural_arrival('e0',F(1,2),[F(-1,16),F(1,16)],1,horizon=1)
if not all(audit_certificate(x) for x in objects.values()):raise RuntimeError('positive certificate audit failed')
manifest=[]
for name,cert in objects.items():
    data=artifact_json(cert).encode('ascii')
    path=out/(name+'.json');path.write_bytes(data)
    manifest.append({'path':path.name,'sha256':hashlib.sha256(data).hexdigest(),
                     'bytes':len(data),'class':cert['status']})
(out/'CERTIFICATE_MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')

info={'date':'2026-10-16','python':sys.version,'machine':platform.machine(),
      'platform':platform.platform(),'backend':'GNU MPFR '+VERSION,
      'mpfr_shared':ctypes.util.find_library('mpfr'),
      'precision_schedule':'128+8*n','ir_a4_r':'DEFERRED / NOT ESTABLISHED',
      'physical_reference':'NUMENG_PULSE_AWARE_REFERENCE_V1 (unchanged)',
      'data_classification':'DEVELOPMENT EVIDENCE / FINITE ENGINEERING CERTIFICATES',
      'rng':'none', 'cert_count':len(objects)}
(out/'ENVIRONMENT.json').write_text(json.dumps(info,indent=2,sort_keys=True)+'\n')
print(json.dumps({'certificates':manifest,'environment':info},indent=2))
