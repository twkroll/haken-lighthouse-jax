"""Deterministic source-rate counterexample for frozen NUM-ENG Gate 0.5.
Run from any directory with: python software/numerical_engineering/rifc_ir_a4r_gate_0_5/diagnose_rate_v05.py
No RNG, protected data, physical simulation, or empirical bound fitting.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, importlib.util, json, sys

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT/"software/numerical_engineering/rifc_interval_gate_0_4/source/rifc_mpfr_v0_1.py"
SHA = "0b33f0e1049025048b219a7355692bbb95dc2c62ca8aa6d74781ebff1f1e6539"
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SHA
spec = importlib.util.spec_from_file_location("frozen_rifc_gate04",SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
assert module.VERSION == "4.2.2"
floor=F(1,2**2048)
rows=[]
for p in (128,256,512,2048,4096):
    z=module.I.point(-10000,p).exp()
    r=module.response(module.I.point(F(1,100),p),1,0)
    assert (z.lo,z.hi)==(F(0),floor),(p,"exp",z)
    assert (r.lo,r.hi)==(F(0),floor),(p,"response",r)
    rows.append({"p":p,"direct_exp_interval":["0","2^-2048"],
                 "response_interval":["0","2^-2048"],
                 "excess_over_2_to_minus_p":f"2^({p}-2048)"})
print(json.dumps({"status":"IR-A4-R NOT ESTABLISHED",
                  "source_sha256":SHA,"mpfr":module.VERSION,
                  "counterexample":"exp(-10000) / x-h=1/100,r=1",
                  "rows":rows},indent=2))
