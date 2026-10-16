from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"source"))
"""Deterministic preregistered RI-01..RI-12 + RI-14 RIFC QA. No stochastic science."""
import copy
from fractions import Fraction as F
from math import pi
import mpmath as mp
import pytest

from rifc_mpfr_v0_2 import (I,VERSION,ArithmeticFailure,certify,audit_certificate,
    artifact_json,artifact_sha,darbouxs,event_order,eta_mass_tail,
    omitted_history_phase_error_bound,psi_interval,q_interval,response,
    response_slope_bound,structural_arrival,transversality_class)

mp.mp.dps=200

def mm(x):
    x=F(x)
    return mp.mpf(x.numerator)/mp.mpf(x.denominator)

def enclose(i,x):
    assert mm(i.lo)<=x<=mm(i.hi), (i.lo,i.hi,mp.nstr(x,24))

def test_ri01_directed_primitives():
    assert VERSION=='4.2.2'
    a,b,c=F(-7,8),F(3,5),F(11,10)
    for x in (a,b,c,F(1,100),F(1000),F(0)):
        y=I.point(x,128);assert y.contains(x)
    A,B=I.point(a,128),I.point(b,128)
    for v,x in ((A+B,a+b),(A-B,a-b),(A*B,a*b),(A/B,a/b)):
        assert v.contains(x)
    assert I.bounds(a,b,128).contains(0)
    assert A.hull(B).contains(a) and A.hull(B).contains(b)
    assert I.bounds(a,c,128).intersect(I.bounds(b,2,128)).contains(b)
    assert I.bounds(a,c,128).min_with(I.bounds(b,2,128)).contains(a)
    assert I.bounds(a,c,128).max_with(I.bounds(b,2,128)).contains(2) is True
    with pytest.raises(ArithmeticFailure):A/I.bounds(-1,1,128)

@pytest.mark.parametrize('x', ['-20','-1','0','1'])
def test_ri02_exp_contract(x):
    enclose(I.point(F(x),128).exp(),mp.exp(mm(F(x))))

@pytest.mark.parametrize('A,B', [('-20','-1'),('-1','0'),('0','1')])
def test_ri02_exp_interval(A,B):
    z=I.bounds(F(A),F(B),128).exp()
    enclose(z,mp.exp(mm(F(A))));enclose(z,mp.exp(mm(F(B))))

def test_ri03_a4r_explicitly_deferred():
    # Backend proof does NOT assert B_K N 2^-p.
    assert VERSION=='4.2.2'

def test_ri04_alpha_propagation():
    for alpha,psi0,q0,t in [
        (1,F(1,4),F(1,2),F(0)), (1,F(1,4),F(1,2),F(1,8)),
        (1,F(1,4),F(1,2),F(1,2)), (1,F(1,4),F(1,2),F(1)),
        (1000,0,4000000,F(1,1000)),(1000,0,4000000,F(1,200)),
        (1000,0,4000000,F(1,50))]:
        x=I.point(t,128)
        q=q_interval(alpha,q0,x);p=psi_interval(alpha,psi0,q0,x)
        ee=mp.exp(-alpha*mm(t))
        enclose(q,ee*mm(q0))
        enclose(p,ee*(mm(psi0)+mm(q0)*mm(t)))

def test_ri05_threshold_splice():
    for a,b,case in [(0,F(1,2),'below'),(1,1,'touch'),
                     (F(3,4),F(5,4),'straddle'),(2,3,'above')]:
        y=response(I.bounds(a,b,128),1,1)
        assert y.lo>=0 and y.hi<=1
        if case in ('below','touch'):assert y.lo==y.hi==0
        if case=='straddle':assert y.lo==0<y.hi
        if case=='above':assert y.lo>0
        for x in (F(a),F(b)):
            z=mp.mpf(0) if x<=1 else mp.exp(-1/(mm(x)-1)**2)
            enclose(y,z)

def test_ri06_darboux_gain_inclusion_s16():
    alpha,r,h,psi0,q0,L=1,1,-1,F(1,4),F(1,2),F(1)
    def f(t):
        p=mp.exp(-t)*(mm(psi0)+mm(q0)*t)
        return mp.exp(-1/(p+1)**2)
    exact=mp.quad(f,[mp.mpf(0),mp.mpf('0.5'),mp.mpf(1)])
    widths=[]
    for n in (0,2,4,8):
        p,cells,pref=darbouxs(alpha,r,h,psi0,q0,L,n)
        z=I(F(pref[-1][0]),F(pref[-1][1]),p)
        enclose(z,exact)
        widths.append(mm(z.hi-z.lo))
    assert widths[-1]<widths[0]

def test_ri06_narrow_gain_inclusion_s03():
    c=certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=10)
    assert c['status']=='CERTIFIED_REGULAR_HIT'
    assert audit_certificate(c)
    assert F(c['bracket'][0]) <= F('0.005000505363421') <= F(c['bracket'][1])

def test_ri07_no_hit_and_boundary():
    good=certify(1,1,1,0,0,1,F(1,4),nmax=5)
    assert good['status']=='CERTIFIED_NO_HIT' and F(good['strict_margin'])>0
    assert audit_certificate(good)
    assert certify(1,1,1,0,0,1,0,nmax=5)['status']=='STRICT_MARGIN_ABSENT'

def test_ri08_strict_regular_hit():
    a=certify(1,1,-1,0,0,4,1,nmax=7)
    assert a['status']=='CERTIFIED_REGULAR_HIT' and audit_certificate(a)
    t=mp.e
    assert mm(F(a['bracket'][0]))<t<mm(F(a['bracket'][1]))
    assert F(a['transversality_lower'])>0

def test_ri09_structural_zero_arrival():
    ids=[]
    for w in ([F(-1,16),F(-1,16)],[0,0],[F(1,16),F(1,16)],[F(-1,16),F(1,16)]):
        s=structural_arrival('e0',F(1,2),w,1,horizon=1)
        assert s['status']=='CERTIFIED_STRUCTURAL_ARRIVAL'
        assert audit_certificate(s)
        assert s['topology']==['e0']
        ids.append(s)
    assert ids[1]['jump']==['0/1','0/1']
    assert ids[3]['crosses_zero']
    assert ids[1]['topology']!=[]
    # The physical q jump at exact zero equals graph with edge omitted, but tapes differ.
    assert ids[1]['jump']==['0/1','0/1']
    wrong=copy.deepcopy(ids[1]);wrong['topology']=[]
    assert not audit_certificate(wrong)

def test_ri10_ordering_collision_boundary():
    a=['1/4','1/3'];b=['1/2','2/3']
    for x,y,first in ((a,b,'a'),(b,a,'b')):
        result=event_order(x,y)
        assert result['status']=='CERTIFIED_EVENT_ORDER' and result['first']==first
        assert audit_certificate(result)
    assert event_order(['2/5','3/5'],['1/2','7/10'])['status']=='ENCLOSURE_INCONCLUSIVE'
    assert event_order(['1/2','1/2'],['1/2','1/2'])['status']=='ORDINARY_CHART_INVALID'
    assert event_order(['1/2','1/2'],['3/4','3/4'],horizon='1/2')['status']=='ORDINARY_CHART_INVALID'
    assert event_order(['0','0'],['1/2','1/2'])['status']=='ORDINARY_CHART_INVALID'
    assert event_order(['1/2','1/2'],['1/2','1/2'],horizon=1)['status']=='ORDINARY_CHART_INVALID'
    qa=I.point(F(1,4),128);qb=I.point(F(1,5),128)
    assert (qa+qb)==(qb+qa)
    assert structural_arrival('e0','1/2',['0','0'],'1',others=['1/2'])['status']=='ORDINARY_CHART_INVALID'

def test_ri11_nonpositive_taxonomy():
    outcomes={
      certify(-1,1,1,0,0,1,F(1,4))['status'],
      certify(1,1,1,0,0,1,0)['status'],
      certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=0)['status'],
      certify(1,1,1,0,0,1,F(1,4),arithmetic=False)['status'],
      certify('[1,2]',1,1,0,0,1,F(1,4))['status'],
      event_order(['1/2','3/4'],['3/4','7/8'])['status'],
      event_order(['1/2','1/2'],['1/2','1/2'])['status']}
    expected={'ASSUMPTION_VIOLATED','STRICT_MARGIN_ABSENT','RESOURCE_EXHAUSTED',
              'UNCERTIFIED_ARITHMETIC','UNSUPPORTED_CASE',
              'ENCLOSURE_INCONCLUSIVE','ORDINARY_CHART_INVALID'}
    assert outcomes==expected

def test_ri12_artifact_replay_and_mutation():
    for params in [(1,1,1,0,0,1,F(1,4)),(1,1,-1,0,0,4,1)]:
        c=certify(*params,nmax=7,topology=('e0',))
        loaded=__import__('json').loads(artifact_json(c))
        assert artifact_sha(c)==artifact_sha(loaded)
        assert audit_certificate(loaded,expected_inputs=loaded['inputs'])
        mutations=[]
        q=copy.deepcopy(c);q['prefix'][-1][1]=str(F(q['prefix'][-1][1])-1);mutations.append(q)
        q=copy.deepcopy(c);q['backend']['precision']+=1;mutations.append(q)
        q=copy.deepcopy(c);q['topology']=[];mutations.append(q)
        q=copy.deepcopy(c);q['phase_gap']=['0/1','0/1'];mutations.append(q)
        if c['status']=='CERTIFIED_REGULAR_HIT':
            q=copy.deepcopy(c);q['bracket']=['0','1'];mutations.append(q)
        assert all(not audit_certificate(q) for q in mutations)

def test_ri13_ir_a4r_not_claimed():
    # No whole-expression propagation proof B_K; refinement may still work in a finite case.
    results=[certify(1,1,1,0,0,1,F(1,4),nmax=n)['status'] for n in (0,2,4)]
    assert all(v=='CERTIFIED_NO_HIT' for v in results)

def test_ri14_budget_exhaustion():
    a=certify(1000,1,F(1,10),0,4000000,F(1,50),F(1,200),nmax=0)
    assert a['status']=='RESOURCE_EXHAUSTED'

def test_th_fh_03_transversality():
    z=transversality_class(I.point(F(-3,4),128),1,-1,F(1,1000))
    assert z['status']=='STRICT_MARGIN_ABSENT'
    y=transversality_class(I.point(0,128),1,-1,F(1,1000))
    assert y['status']=='CERTIFIED_TRANSVERSAL'

def test_th_fh_05_tail_mass_and_phase():
    a=eta_mass_tail(1,4)
    enclose(a,mp.exp(-4)*5)
    bs=omitted_history_phase_error_bound(1,1,[4,5],[F(1,2),F(1,4)],1)
    def pulse(s,age):
        x=mm(F(age))+s
        return x*mp.exp(-x)
    def f(s):
        psi=mp.mpf('0.5')*pulse(s,4)+mp.mpf('0.25')*pulse(s,5)
        return mp.exp(-1/(1+psi)**2)-mp.exp(-1)
    actual=mp.quad(f,[0,mp.mpf('0.5'),1])
    assert actual>=0
    assert actual<=mm(bs.hi)
    # Without an absolute-tail bound, no nontrivial quantified result is inferred.

def test_duplicate_proof_audits_independently():
    a=certify(1,1,-1,0,0,4,1,nmax=7)
    b=certify(1,1,-1,0,0,4,1,nmax=7)
    assert artifact_json(a)==artifact_json(b)
    assert audit_certificate(a)

def test_ri06_narrow_high_precision_darboux_comparator():
    p,cells,pref=darbouxs(1000,1,F(1,10),0,4000000,F(1,50),8)
    enclosure=I(F(pref[-1][0]),F(pref[-1][1]),p)
    def f(t):
        psi=mp.mpf(4000000)*t*mp.exp(-1000*t)
        return mp.mpf(0) if psi<=mp.mpf('0.1') else mp.exp(-1/(psi-mp.mpf('0.1'))**2)
    pieces=[mp.mpf(str(F(i,1000))) for i in (0,1,2,3,4,5,6,7,8,10,12,15,18,20)]
    exact=mp.quad(f,pieces)
    enclose(enclosure,exact)

def test_ri09_structural_delay_remains_labelled():
    left=structural_arrival('zero_edge',F(1,4),[0,0],1,others=[F(1,2)],horizon=1)
    right=structural_arrival('zero_edge',F(3,4),[0,0],1,others=[F(1,2)],horizon=1)
    assert left['status']==right['status']=='CERTIFIED_STRUCTURAL_ARRIVAL'
    assert left['jump']==right['jump']==['0/1','0/1']
    assert left['time'] != right['time']
    assert audit_certificate(left) and audit_certificate(right)
