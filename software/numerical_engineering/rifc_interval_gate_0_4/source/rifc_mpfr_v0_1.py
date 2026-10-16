"""RIFC-0.1: finite-soundness-only MPFR directed interval certifier.

Engineering implementation of RB-024 under NUM-ENG Gate 0.4.
No IR-A4-R, eventual termination, whole-chart-radius or scientific guarantees.
No physical simulator or float libm is used to construct certificates.
"""
from __future__ import annotations

import ctypes as C
import ctypes.util
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Any

class ArithmeticFailure(RuntimeError):
    pass

# MPFR 4.2.2 ABI on Linux x86_64; layout specified by MPFR headers.
class _MP(C.Structure):
    _fields_ = [('_mpfr_prec', C.c_long), ('_mpfr_sign', C.c_int),
                ('_mpfr_exp', C.c_long), ('_mpfr_d', C.c_void_p)]

_dll = C.CDLL(ctypes.util.find_library('mpfr'))
RNDN, RNDU, RNDD = 0, 2, 3
_dll.mpfr_get_version.restype = C.c_char_p
VERSION = _dll.mpfr_get_version().decode('ascii')
if VERSION != '4.2.2':
    raise ArithmeticFailure('MPFR version contract mismatch: '+VERSION)
for f in ('mpfr_init2', 'mpfr_clear', 'mpfr_set_str', 'mpfr_add',
          'mpfr_sub', 'mpfr_mul', 'mpfr_div', 'mpfr_exp', 'mpfr_number_p',
          'mpfr_get_str', 'mpfr_free_str', 'mpfr_sqrt'):
    fn = getattr(_dll, f)
    fn.restype = C.c_void_p if f == 'mpfr_get_str' else C.c_int
_dll.mpfr_init2.argtypes = [C.POINTER(_MP), C.c_long]
_dll.mpfr_clear.argtypes = [C.POINTER(_MP)]
_dll.mpfr_set_str.argtypes = [C.POINTER(_MP), C.c_char_p, C.c_int, C.c_int]
for name in ('mpfr_add','mpfr_sub','mpfr_mul','mpfr_div'):
    getattr(_dll,name).argtypes = [C.POINTER(_MP),C.POINTER(_MP),C.POINTER(_MP),C.c_int]
_dll.mpfr_exp.argtypes = [C.POINTER(_MP),C.POINTER(_MP),C.c_int]
_dll.mpfr_sqrt.argtypes = [C.POINTER(_MP),C.POINTER(_MP),C.c_int]
_dll.mpfr_number_p.argtypes=[C.POINTER(_MP)]
_dll.mpfr_get_str.argtypes = [C.c_void_p,C.POINTER(C.c_long),C.c_int,C.c_size_t,C.POINTER(_MP),C.c_int]
_dll.mpfr_free_str.argtypes=[C.c_void_p]

class M:
    def __init__(self,p):
        self.data=_MP();self.p=p;_dll.mpfr_init2(C.byref(self.data),p)
    def __del__(self):
        if hasattr(self,'data'):
            _dll.mpfr_clear(C.byref(self.data))
    def val(self,rnd=RNDN):
        if not _dll.mpfr_number_p(C.byref(self.data)):
            raise ArithmeticFailure('nonfinite MPFR result')
        e=C.c_long()
        ptr=_dll.mpfr_get_str(None,C.byref(e),2,0,C.byref(self.data),RNDN)
        if not ptr:
            raise ArithmeticFailure('MPFR serialization error')
        try: s=C.string_at(ptr).decode('ascii')
        finally: _dll.mpfr_free_str(ptr)
        if s in ('0','-0'): return F(0)
        neg=s.startswith('-')
        if neg:s=s[1:]
        bits=int(s,2)*(-1 if neg else 1)
        scale=e.value-len(s)
        # Extremely small correctly rounded MPFR results are conservatively
        # widened at an exact dyadic serialization floor; never manufacture
        # a mathematically false zero upper bound. This is finite SOUNDNESS,
        # not an MPFR underflow/precision convergence theorem.
        if e.value < -2048:
            floor=F(1,2**2048)
            if rnd==RNDD:return -floor if bits<0 else F(0)
            if rnd==RNDU:return F(0) if bits<0 else floor
            raise ArithmeticFailure('tiny MPFR value needs directed serialization')
        if e.value > 2048:raise ArithmeticFailure('MPFR result outside serialization domain')
        return F(bits)*F(2)**scale

def _integer(v,p,rnd):
    m=M(p)
    if _dll.mpfr_set_str(C.byref(m.data),str(v).encode(),10,rnd)!=0:
        raise ArithmeticFailure('could not parse integer input')
    return m

def _binary(name, a, b, p, rnd):
    out=M(p)
    getattr(_dll,'mpfr_'+name)(C.byref(out.data),C.byref(a.data),C.byref(b.data),rnd)
    return out

def _fraction_round(v,p,rnd):
    v=F(v)
    if v.denominator==1:return _integer(v.numerator,p,rnd)
    # Sign-sensitive interval division of two correctly rounded integers.
    if v>=0:
        a=_integer(v.numerator,p,RNDD if rnd==RNDD else RNDU)
        b=_integer(v.denominator,p,RNDU if rnd==RNDD else RNDD)
    else:
        a=_integer(v.numerator,p,RNDD if rnd==RNDD else RNDU)
        b=_integer(v.denominator,p,RNDD if rnd==RNDD else RNDU)
    return _binary('div',a,b,p,rnd)

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    p:int=128
    def __post_init__(self):
        object.__setattr__(self,'lo',F(self.lo));object.__setattr__(self,'hi',F(self.hi))
        if self.p<2 or self.lo>self.hi:raise ArithmeticFailure('invalid interval')
    @staticmethod
    def point(x,p):
        return I(_fraction_round(x,p,RNDD).val(RNDD),_fraction_round(x,p,RNDU).val(RNDU),p)
    @staticmethod
    def bounds(a,b,p):
        if F(a)>F(b):raise ArithmeticFailure('reversed bounds')
        return I(_fraction_round(a,p,RNDD).val(RNDD),_fraction_round(b,p,RNDU).val(RNDU),p)
    def _op(self,other,kind):
        if not isinstance(other,I):other=I.point(other,self.p)
        if other.p!=self.p:raise ArithmeticFailure('mixed precision')
        if kind=='div' and other.lo<=0<=other.hi:raise ArithmeticFailure('divisor contains zero')
        if kind=='add':
            pairs=[(self.lo,other.lo,'add'),(self.hi,other.hi,'add')]
        elif kind=='sub':
            pairs=[(self.lo,other.hi,'sub'),(self.hi,other.lo,'sub')]
        else:pairs=[]
        def one(a,b,rd):return _binary(kind,_fraction_round(a,self.p,rd),_fraction_round(b,self.p,rd),self.p,rd).val(rd)
        if pairs:
            return I(one(pairs[0][0],pairs[0][1],RNDD),one(pairs[1][0],pairs[1][1],RNDU),self.p)
        xy=[(a,b) for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(one(a,b,RNDD) for a,b in xy),max(one(a,b,RNDU) for a,b in xy),self.p)
    def __add__(self,y):return self._op(y,'add')
    __radd__=__add__
    def __sub__(self,y):return self._op(y,'sub')
    def __mul__(self,y):return self._op(y,'mul')
    __rmul__=__mul__
    def __truediv__(self,y):return self._op(y,'div')
    def __neg__(self):return I(-self.hi,-self.lo,self.p)
    def exp(self):
        def one(v,rd):
            x=_fraction_round(v,self.p,rd);y=M(self.p)
            _dll.mpfr_exp(C.byref(y.data),C.byref(x.data),rd)
            return y.val(rd)
        return I(one(self.lo,RNDD),one(self.hi,RNDU),self.p)
    def sqrt(self):
        if self.lo<0:raise ArithmeticFailure('negative sqrt interval')
        def one(v,rd):
            a=_fraction_round(v,self.p,rd);b=M(self.p)
            _dll.mpfr_sqrt(C.byref(b.data),C.byref(a.data),rd)
            return b.val(rd)
        return I(one(self.lo,RNDD),one(self.hi,RNDU),self.p)
    def hull(self,other):return I(min(self.lo,other.lo),max(self.hi,other.hi),self.p)
    def intersect(self,other):
        lo=max(self.lo,other.lo);hi=min(self.hi,other.hi)
        return None if lo>hi else I(lo,hi,self.p)
    def min_with(self,other):return I(min(self.lo,other.lo),min(self.hi,other.hi),self.p)
    def max_with(self,other):return I(max(self.lo,other.lo),max(self.hi,other.hi),self.p)
    def contains(self,f):return self.lo<=F(f)<=self.hi
    def data_json(self):return [f'{self.lo.numerator}/{self.lo.denominator}',f'{self.hi.numerator}/{self.hi.denominator}']

def from_json(v,p):return I(F(v[0]),F(v[1]),p)

def psi_interval(alpha,psi0,q0,t):
    p=t.p
    return (-(I.point(alpha,p)*t)).exp()*(I.point(psi0,p)+t*I.point(q0,p))

def q_interval(alpha,q0,t):return (-(I.point(alpha,t.p)*t)).exp()*I.point(q0,t.p)

def response(x:I,r,h):
    p=x.p;h=F(h);r=F(r)
    if r<=0:raise ArithmeticFailure('r must be positive')
    if x.hi<=h:return I(F(0),F(0),p)
    def top(z,rd=None):
        # Interval computation with input endpoint outward-enclosed already.
        gap=I.point(z,p)-I.point(h,p)
        return (-(I.point(r,p)/(gap*gap))).exp()
    upper=top(x.hi).hi
    if x.lo<=h:return I(F(0),upper,p)
    lower=top(x.lo).lo
    return I(lower,upper,p)

def darbouxs(alpha,r,h,psi0,q0,L,n):
    p=128+8*n;L=F(L);m=2**n
    cumulative=I.point(0,p);cells=[];prefix=[cumulative.data_json()]
    for k in range(m):
        a=L*F(k,m);b=L*F(k+1,m)
        t=I.bounds(a,b,p)
        psi=psi_interval(alpha,psi0,q0,t)
        S=response(psi,r,h)
        gain=I.point(b-a,p)*S
        cumulative=cumulative+gain
        cells.append({'t':[str(a),str(b)],'psi':psi.data_json(),'S':S.data_json(), 'gain':gain.data_json()})
        prefix.append(cumulative.data_json())
    return p,cells,prefix

def certify(alpha,r,h,psi0,q0,L,gap,nmax=8,topology=(),arithmetic=True):
    input_data=dict(alpha=str(alpha),r=str(r),h=str(h),psi0=str(psi0),q0=str(q0),L=str(L),gap=str(gap),nmax=nmax,topology=list(topology))
    def fail(status,detail):return {'status':status,'detail':detail,'inputs':input_data,'backend':VERSION}
    if not arithmetic:return fail('UNCERTIFIED_ARITHMETIC','backend marked unavailable')
    try:
        alpha,r,h,psi0,q0,L,gap=[F(z) for z in (alpha,r,h,psi0,q0,L,gap)]
    except Exception:return fail('UNSUPPORTED_CASE','non-singleton or invalid scalar')
    if alpha<=0 or r<=0 or L<=0:return fail('ASSUMPTION_VIOLATED','positive alpha,r,L required')
    if gap<=0:return fail('STRICT_MARGIN_ABSENT','initial gap not strictly positive')
    if not isinstance(nmax,int) or nmax<0 or nmax>16:return fail('UNSUPPORTED_CASE','invalid finite refinement limit')
    for n in range(nmax+1):
        try:p,cells,prefix=darbouxs(alpha,r,h,psi0,q0,L,n)
        except (ArithmeticFailure,OverflowError) as e:return fail('UNCERTIFIED_ARITHMETIC',str(e))
        pref=[from_json(v,p) for v in prefix];S=[from_json(v['S'],p) for v in cells];d=I.point(gap,p)
        common=dict(status=None,inputs=input_data,backend={'name':'GNU MPFR','version':VERSION,'precision':p,'level':n,'exp_contract':'MPFR_RNDD_RNDU'},cells=cells,prefix=prefix,phase_gap=d.data_json(),topology=list(topology),event_competitors=[])
        if pref[-1].hi<d.lo:
            common.update(status='CERTIFIED_NO_HIT',strict_margin=str(d.lo-pref[-1].hi))
            return common
        before=[j for j,x in enumerate(pref) if x.hi<d.lo]
        after=[j for j,x in enumerate(pref) if x.lo>d.hi]
        if before and after:
            j=max(before);k=min(after)
            if 0<=j<k<=len(S) and all(x.lo>0 for x in S[j:k]):
                lower=min(x.lo for x in S[j:k]);a=L*F(j,2**n);b=L*F(k,2**n)
                common.update(status='CERTIFIED_REGULAR_HIT',bracket=[str(a),str(b)],j=j,k=k,
                              transversality_lower=str(lower),strict_pre=str(d.lo-pref[j].hi),strict_post=str(pref[k].lo-d.hi))
                return common
    return fail('RESOURCE_EXHAUSTED','finite dyadic budget exhausted without strict certificate')

def event_order(a,b,initial=F(0),horizon=None):
    # Exact rational event-time endpoint proof; overlap never treated as a strict order.
    a=(F(a[0]),F(a[1]));b=(F(b[0]),F(b[1]));init=F(initial)
    if a[0]>a[1] or b[0]>b[1]:return {'status':'ASSUMPTION_VIOLATED'}
    if any(x[0]<init for x in (a,b)):return {'status':'ENCLOSURE_INCONCLUSIVE','why':'initial domain overlap/outside'}
    if any(x[0]==x[1] and (x[0]==init or (horizon is not None and x[0]==F(horizon))) for x in (a,b)):
        return {'status':'ORDINARY_CHART_INVALID','why':'exact boundary tie'}
    if horizon is not None and any(x[1]>F(horizon) for x in (a,b)):
        return {'status':'ENCLOSURE_INCONCLUSIVE','why':'horizon domain overlap/outside'}
    if a[0]==a[1]==b[0]==b[1]:return {'status':'ORDINARY_CHART_INVALID','why':'exact labelled event collision'}
    evidence=dict(interval_a=[str(a[0]),str(a[1])],interval_b=[str(b[0]),str(b[1])],
                  initial=str(init),horizon=str(F(horizon)) if horizon is not None else None,topology=['event:a','event:b'])
    if a[1]<b[0]:return {'status':'CERTIFIED_EVENT_ORDER','first':'a','margin':str(b[0]-a[1]),**evidence}
    if b[1]<a[0]:return {'status':'CERTIFIED_EVENT_ORDER','first':'b','margin':str(a[0]-b[1]),**evidence}
    return {'status':'ENCLOSURE_INCONCLUSIVE','why':'event interval overlap'}

def structural_arrival(edge,arrival,weight,alpha,others=(),horizon=None):
    if F(alpha)<=0:return {'status':'ASSUMPTION_VIOLATED'}
    if not edge:return {'status':'UNSUPPORTED_CASE'}
    if F(arrival)<0 or (horizon is not None and F(arrival)>F(horizon)):
        return {'status':'UNSUPPORTED_CASE','why':'arrival outside forward horizon'}
    w=I.bounds(F(weight[0]),F(weight[1]),128)
    jump=w*I.point(F(alpha)**2,128)
    if F(arrival)==0 or (horizon is not None and F(arrival)==F(horizon)):
        return {'status':'ORDINARY_CHART_INVALID','why':'boundary structural arrival','edge':edge}
    for v in others:
        order=event_order((arrival,arrival),(v,v),horizon=horizon)
        if order['status']!='CERTIFIED_EVENT_ORDER':return {'status':order['status'],'edge':edge}
    return {'status':'CERTIFIED_STRUCTURAL_ARRIVAL','edge':edge,'time':str(F(arrival)),
            'weight':w.data_json(),'weight_exact':[str(F(weight[0])),str(F(weight[1]))],
            'alpha':str(F(alpha)),'horizon':str(F(horizon)) if horizon is not None else None,
            'competitor_arrivals':[str(F(v)) for v in others],
            'weight_precision':128,'jump':jump.data_json(),
            'crosses_zero':w.lo<=0<=w.hi,'topology':[edge]}

def artifact_json(cert):return json.dumps(cert,sort_keys=True,separators=(',',':'),ensure_ascii=True)

def artifact_sha(cert):return hashlib.sha256(artifact_json(cert).encode('utf-8')).hexdigest()

def audit_certificate(cert,expected_inputs=None):
    """Independent proof-data replay without a physical simulator.
    Rebuild every cell and prefix by directed MPFR and verify strict conclusion.
    """
    try:
        if not isinstance(cert,dict):return False
        if cert.get('status')=='CERTIFIED_EVENT_ORDER':
            fresh=event_order(cert['interval_a'],cert['interval_b'],cert['initial'],cert['horizon'])
            return cert==fresh and F(cert['margin'])>0
        if cert.get('status')=='CERTIFIED_STRUCTURAL_ARRIVAL':
            fresh=structural_arrival(cert['edge'],cert['time'],cert['weight_exact'],cert['alpha'],
                                     cert['competitor_arrivals'],cert['horizon'])
            return cert==fresh and cert['topology']==[cert['edge']]
        if cert.get('status') not in ('CERTIFIED_NO_HIT','CERTIFIED_REGULAR_HIT'):return False
        inputs=cert['inputs'];b=cert['backend'];p=int(b['precision']);n=int(b['level'])
        if b['version']!=VERSION or b['name']!='GNU MPFR' or b['exp_contract']!='MPFR_RNDD_RNDU' or p!=128+8*n:return False
        if expected_inputs is not None and inputs!=expected_inputs:return False
        a,r,h,psi0,q0,L,d=[F(inputs[z]) for z in ('alpha','r','h','psi0','q0','L','gap')]
        if a<=0 or r<=0 or d<=0 or L<=0:return False
        if list(cert['topology'])!=inputs['topology']:return False
        _,cells,prefix=darbouxs(a,r,h,psi0,q0,L,n)
        if len(cells)!=len(cert['cells']) or len(prefix)!=len(cert['prefix']):return False
        # Bound-check serialized claims rather than trusting the original computation.
        for stored,calc in zip(cert['cells'],cells):
            if stored['t']!=calc['t']:return False
            for key in ('psi','S','gain'):
                si=from_json(stored[key],p);ci=from_json(calc[key],p)
                if not (si.lo<=ci.lo and si.hi>=ci.hi):return False
        for s,c in zip(cert['prefix'],prefix):
            si=from_json(s,p);ci=from_json(c,p)
            if not (si.lo<=ci.lo and si.hi>=ci.hi):return False
        v=[from_json(x,p) for x in cert['prefix']];gap=from_json(cert['phase_gap'],p)
        exact_gap=I.point(d,p)
        if gap.lo>exact_gap.lo or gap.hi<exact_gap.hi:return False
        if cert['status']=='CERTIFIED_NO_HIT':
            return v[-1].hi<gap.lo and F(cert['strict_margin'])==gap.lo-v[-1].hi and F(cert['strict_margin'])>0
        j=int(cert['j']);k=int(cert['k']);m=len(cells)
        if not (0<=j<k<=m):return False
        S=[from_json(c['S'],p) for c in cert['cells']]
        tr=min(x.lo for x in S[j:k]);bb=[F(x) for x in cert['bracket']]
        return (bb==[L*F(j,m),L*F(k,m)] and v[j].hi<gap.lo and v[k].lo>gap.hi
                and tr>0 and F(cert['transversality_lower'])>0
                and F(cert['transversality_lower'])<=tr
                and F(cert['strict_pre'])==gap.lo-v[j].hi and F(cert['strict_post'])==v[k].lo-gap.hi)
    except (KeyError,TypeError,ValueError,ArithmeticFailure,ZeroDivisionError,OverflowError):return False


def eta_mass_tail(alpha,A,p=128):
    if F(alpha)<=0 or F(A)<0:raise ArithmeticFailure('alpha>0,A>=0 required')
    a=I.point(alpha,p);z=I.point(A,p)
    return (-(a*z)).exp()*(I.point(1,p)+a*z)

def response_slope_bound(r,p=128):
    if F(r)<=0:raise ArithmeticFailure('r>0 required')
    a=I.point(F(3,2),p)
    return I.point(2,p)/I.point(r,p).sqrt() * a * a.sqrt() * (-a).exp()

def omitted_history_phase_error_bound(alpha,r,ages,weights,L,p=128):
    if len(ages)!=len(weights) or F(L)<0:raise ArithmeticFailure('invalid age/weight list')
    mass=I.point(0,p)
    for age,weight in zip(ages,weights):
        if F(age)<0:raise ArithmeticFailure('negative age')
        diff=eta_mass_tail(alpha,age,p)-eta_mass_tail(alpha,F(age)+F(L),p)
        # Exact upper bound remains valid despite lower interval enclosure negative.
        mass=mass + I.point(abs(F(weight)),p)*I(F(0),max(F(0),diff.hi),p)
    return response_slope_bound(r,p)*mass

def transversality_class(x,r,h,minmargin):
    s=response(x,r,h)
    if s.lo>=F(minmargin) and s.lo>0:return {'status':'CERTIFIED_TRANSVERSAL','bound':s.data_json()}
    return {'status':'STRICT_MARGIN_ABSENT','bound':s.data_json()}
