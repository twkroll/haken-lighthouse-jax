"""Deterministic finite-soundness artifacts; NO statistical/scientific execution."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys,platform,ctypes,ctypes.util
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'source'))
import rifc_mpfr_v0_2 as rifc
out=Path(sys.argv[1]) if len(sys.argv)>1 else root/'certificates';out.mkdir(parents=True,exist_ok=True)
p_values=[128,256,512,2048,4096]
def compact_dyadic(f):
    if f.denominator==1:k=0
    else:
        assert f.denominator&(f.denominator-1)==0
        k=f.denominator.bit_length()-1
    return {'signed_numerator_hex':hex(f.numerator),'binary_denominator_exponent':k,'signed_numerator_bits':abs(f.numerator).bit_length()}
records=[]
for p in p_values:
    e=rifc.I.point(-10000,p).exp();v=rifc.response(rifc.I.point(F(1,100),p),1,0)
    assert 0<e.lo<=e.hi<F(1,2**2048)
    assert 0<v.lo<=v.hi<F(1,2**2048)
    records.append({'precision':p,'exp_direct':[compact_dyadic(e.lo),compact_dyadic(e.hi)],
                    'response_composed':[compact_dyadic(v.lo),compact_dyadic(v.hi)],
                    'old_fixed_floor_removed':True})
(out/'SER_FIXED_PRECISION_5.json').write_text(json.dumps(records,indent=2)+'\n')
certs={
    'S01_strict_no_hit':rifc.certify(1,1,1,0,0,1,F(1,4),nmax=10),
    'S02_regular_hit':rifc.certify(1,1,-1,0,0,4,1,nmax=10),
    'S03_narrow_pulse_hit':rifc.certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=10,topology=('fixed_topology_e0',)),
    'S10_order':rifc.event_order(('1/4','1/3'),('1/2','2/3'),horizon=1),
    'S13_zero_arrival':rifc.structural_arrival('e0',F(1,2),[0,0],1,horizon=1),
    'S13_crossing_arrival':rifc.structural_arrival('e0',F(1,2),[F(-1,16),F(1,16)],1,horizon=1),
    'SER_tiny_nohit':rifc.certify(1,1,0,F(1,100),0,1,F(1,2**2049),nmax=0)
}
entries=[]
for label,c in certs.items():
    assert c['status'].startswith('CERTIFIED_') and rifc.audit_certificate(c)
    buff=rifc.artifact_json(c).encode('ascii');p=out/(label+'.json');p.write_bytes(buff)
    entries.append({'name':p.name,'sha256':hashlib.sha256(buff).hexdigest(), 'bytes':len(buff), 'status':c['status']})
(out/'CERTIFICATE_MANIFEST.json').write_text(json.dumps(entries,indent=2)+'\n')
old=root.parent/'rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py';new=root/'source/rifc_mpfr_v0_2.py'
if not old.exists():old=Path('/mnt/data/numeng_gate04/source/rifc_mpfr_v0_1.py')
env={'python':sys.version,'os':platform.platform(),'machine':platform.machine(),'mpfr':rifc.VERSION,'gmp':rifc.GMP_VERSION,'libmpfr_sha256':'4e3ccf5b442fc91054b0153140fe62939009f98ca1367f45de62376d5b18d28c','libgmp_sha256':'d15e1585c6c267296459570c8ac217ca9123044bcd4e896d2f686b32333445d2','old_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'new_sha256':hashlib.sha256(new.read_bytes()).hexdigest(),'protected_rng': 'none','ir_a4r':'NOT ESTABLISHED','q6_q7_rate_eventual_validation':'NOT EXECUTED due to Q4 analytical prerequisite'}
(out/'ENVIRONMENT.json').write_text(json.dumps(env,indent=2)+'\n')
print('CERTIFICATES',len(entries),'ALL AUDIT TRUE', 'OLD',env['old_sha256'],'NEW',env['new_sha256'])
