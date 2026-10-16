"""Frozen SER-01...SER-06; non-stochastic source/serialization finite QA."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, importlib.util, json
import ctypes as C
import pytest
import mpmath as mp

import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source'))
from rifc_mpfr_v0_2 import I, M, VERSION, GMP_VERSION, ArithmeticFailure, F as _F, \
  certify, response, audit_certificate, event_order, structural_arrival, artifact_json, _dll

BASELINE=next(p for p in (Path(__file__).resolve().parents[2]/'rifc_interval_gate_0_4', Path('/mnt/data/numeng_gate04')) if (p/'source/rifc_mpfr_v0_1.py').exists())
OLD=BASELINE/'source/rifc_mpfr_v0_1.py'
OLD_SHA='0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539'


def test_frozen_identity_backend():
    assert hashlib.sha256(OLD.read_bytes()).hexdigest()==OLD_SHA
    assert VERSION=='4.2.2' and GMP_VERSION=='6.3.0'

@pytest.mark.parametrize('prec',[128,256,512,2048,4096])
def test_tiny_exp_unchanged_exact_mpfr_and_floor_removed(prec):
    x=I.point(-10000,prec).exp()
    y=response(I.point(F(1,100),prec),1,0)
    assert F(0)<x.lo<=x.hi<F(1,2**2048)
    assert F(0)<y.lo<=y.hi<F(1,2**2048)
    assert x.lo.denominator.bit_length()>10000
    assert x.hi.denominator.bit_length()>10000
    # Comparator requires more than p binary digits; not used as certificate.
    with mp.workdps(max(300,int(prec*.30103)+100)):
        z=mp.exp(-10000)
        def m(v):return mp.mpf(v.numerator)/mp.mpf(v.denominator)
        assert m(x.lo)<=z<=m(x.hi)
        assert m(y.lo)<=z<=m(y.hi)

@pytest.mark.parametrize('p',[128,256,512,2048,4096])
def test_exact_powers_signed_and_fraction_inputs(p):
    for x in (F(0),F(1),F(-1),F(1,3),F(-1,3),
              F(1,2**100),F(-1,2**2048),F(1,2**8192),
              F(1,2**10000),F(-1,2**10000),F(2**10000)):
        z=I.point(x,p)
        assert z.lo<=x<=z.hi
        if x.denominator&(x.denominator-1)==0 and abs(x.numerator).bit_length()<=p:
            assert z.lo==z.hi==x


def test_mpfr_zero_sign_equivalence():
    for s in (b'0',b'-0'):
        x=M(128)
        assert _dll.mpfr_set_str(C.byref(x.data),s,10,0)==0
        assert x.val()==F(0)


def test_resource_invalid_precision():
    for p in (1,8193,0,-1):
        with pytest.raises(ArithmeticFailure):M(p)


def test_resource_exponent_guard_and_nonfinite():
    m=M(128)
    # direct MPFR initialization to outside frozen exponent limit, not a certificate
    _dll.mpfr_set_str(C.byref(m.data),b'1e-45000',10,0)
    with pytest.raises(ArithmeticFailure,match='exponent'):m.val()
    _dll.mpfr_set_inf.argtypes=[C.POINTER(type(m.data)),C.c_int]
    _dll.mpfr_set_nan.argtypes=[C.POINTER(type(m.data))]
    _dll.mpfr_set_inf(C.byref(m.data),1)
    with pytest.raises(ArithmeticFailure,match='nonfinite'):m.val()
    _dll.mpfr_set_nan(C.byref(m.data))
    with pytest.raises(ArithmeticFailure,match='nonfinite'):m.val()


def test_zero_divisor_rejected():
    with pytest.raises(ArithmeticFailure):_ = I.point(1,128)/I.bounds(-1,1,128)


def test_tiny_nohit_certificate_large_exact_decimal_replay():
    cert=certify(1,1,0,F(1,100),0,1,F(1,2**2049),nmax=0)
    assert cert['status']=='CERTIFIED_NO_HIT'
    assert audit_certificate(cert)
    text=artifact_json(cert)
    assert len(text)>10000
    assert audit_certificate(json.loads(text))
    text_mut=json.loads(text)
    text_mut['strict_margin']='0/1'
    assert not audit_certificate(text_mut)


def test_small_fixed_budget_and_threshold_and_collisions():
    a=certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=0)
    assert a['status']=='RESOURCE_EXHAUSTED'
    assert response(I.bounds(F(-1,100),F(1,100),128),1,0).lo==0
    assert event_order(['1/2','1/2'],['1/2','1/2'])['status']=='ORDINARY_CHART_INVALID'
    assert structural_arrival('e0',F(1,2),[0,0],1,horizon=1)['status']=='CERTIFIED_STRUCTURAL_ARRIVAL'


def test_old_positive_certificates_under_original_auditor():
    p=OLD
    spec=importlib.util.spec_from_file_location('rifc_original_unchanged_06',p)
    original=importlib.util.module_from_spec(spec)
    import sys
    sys.modules[spec.name]=original
    spec.loader.exec_module(original)
    d=BASELINE/'certificates'
    man=json.loads((d/'CERTIFICATE_MANIFEST.json').read_text())
    assert len(man)==6
    for entry in man:
        buf=(d/entry['path']).read_bytes()
        assert hashlib.sha256(buf).hexdigest()==entry['sha256']
        assert original.audit_certificate(json.loads(buf))


def test_new_six_positive_certs_roundtrip(tmp_path):
    from rifc_mpfr_v0_2 import structural_arrival,event_order
    a={
      'S01':certify(1,1,1,0,0,1,F(1,4),nmax=10),
      'S02':certify(1,1,-1,0,0,4,1,nmax=10),
      'S03':certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=10,topology=('fixed_topology_e0',)),
      'S10':event_order(('1/4','1/3'),('1/2','2/3'),horizon=1),
      'S13_zero':structural_arrival('e0',F(1,2),[0,0],1,horizon=1),
      'S13_cross':structural_arrival('e0',F(1,2),[F(-1,16),F(1,16)],1,horizon=1)
    }
    assert len(a)==6
    for name,cert in a.items():
        assert cert['status'].startswith('CERTIFIED_')
        assert audit_certificate(json.loads(artifact_json(cert))),name
        (tmp_path/(name+'.json')).write_text(artifact_json(cert))
