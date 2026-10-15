"""Deterministic Gate-0.2 QA, fixed by the precommitted engineering stress matrix.
DEVELOPMENT EVIDENCE / ENGINEERING METRICS only. No stochastic experiments.
"""
import numpy as np
import pytest
import jax
import jax.numpy as jnp
from math import pi
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse
from lighthouse_dev.reference import Parameters,physical_rerecord
from lighthouse_dev.fast_first_hit_gauss_v09 import physical_rerecord_gauss
from lighthouse_dev.fast_first_hit_quiet_v010 import physical_rerecord_quiet
from lighthouse_dev.fast_first_hit_bound_v010 import physical_rerecord_phase_bound
from lighthouse_dev.physical_first_hit_repair import pulse_aware_integral,PhysicalFirstHitUncertified
from lighthouse_dev.sparse_replay import derivative_record_sparse,prepare_replay,replay_sparse_fixed_chart
from stress_gate02 import fixture,compare

ids=[f'F{i:02d}' for i in range(1,14)]+[f'F{i:02d}' for i in range(15,19)]
invalid={'F08','F11','F12','F13'}

@pytest.mark.parametrize('case',ids)
def test_physical_dense_sparse_and_certification(case):
    p,kw=fixture(case)
    rec=physical_rerecord_sparse(p,**kw)
    dense=physical_rerecord(p.to_dense(),**kw)
    c=compare(rec,dense)
    assert c['token_exact'] and c['signature_exact'] and c['validity_match']
    assert c['time_error'] is not None and c['time_error']<=2e-8
    assert c['final_phase_error'] <=3e-8
    assert rec.chart_valid == (case not in invalid)
    assert rec.physical_certification == ('INVALID' if case in invalid else 'NUMENG_PULSE_AWARE_REFERENCE_V1')
    if case=='F01':
        assert len(rec.spikes)==1 and abs(rec.spikes[0].t-.505000505363421)<=2e-9
    if case=='F02': assert len(rec.spikes)==0
    if case=='F08':assert any('EVENT_CHART_COLLISION' in s for s in rec.warnings)
    if case in ('F11','F12'): assert any('CHART_BOUNDARY' in s for s in rec.warnings)
    if case=='F13':assert 'EVENT_BUDGET_EXCEEDED' in rec.warnings

acceleration_ids=[f'F{i:02d}' for i in list(range(1,8))+[10]+list(range(15,19))]
methods=[('gauss',physical_rerecord_gauss),('quiet',physical_rerecord_quiet),('phase_bound',physical_rerecord_phase_bound)]
acceleration_cases=[(f'{case}_{nm}',case,method) for case in acceleration_ids for nm,method in methods if nm!='phase_bound' or case in ('F15','F16','F17','F18')]

@pytest.mark.parametrize('name,case,method',acceleration_cases,ids=[x[0] for x in acceleration_cases])
def test_accelerated_comparator_no_certification_promotion(name,case,method):
    p,kw=fixture(case);base=physical_rerecord_sparse(p,**kw);candidate=method(p,**kw)
    c=compare(base,candidate)
    assert c['signature_exact'] and c['validity_match'] and c['time_error'] is not None and c['time_error']<=2e-8
    assert c['final_phase_error']<=3e-8
    assert candidate.physical_certification != 'NUMENG_PULSE_AWARE_REFERENCE_V1'


def test_strict_integrator_budget_fails_closed():
    with pytest.raises(PhysicalFirstHitUncertified,match='SEGMENT_BUDGET_EXCEEDED'):
        pulse_aware_integral(10.,0.,4e6,1000.,1.,.1,max_segments=1)


def test_repeated_determinism_no_rng():
    p,kw=fixture('F15');a=physical_rerecord_sparse(p,**kw);b=physical_rerecord_sparse(p,**kw)
    assert a.token==b.token and [e.t for e in a.events]==[e.t for e in b.events]


def test_regular_chart_gradients_and_jvp_vjp():
    w=np.array([[2.2,0.],[0.,2.5]]); d=np.array([[.31,0.],[.83,.43]]);mask=np.array([[1,0],[1,1]],bool)
    p=SparseParameters.from_dense(Parameters(w,d,adjacency=mask))
    kw=dict(horizon=40.,history=((-3.,-.5),(-2.2,)),initial_theta=[.3,1.1])
    rec=physical_rerecord_sparse(p,**kw)
    assert rec.chart_valid and rec.physical_certification=='NUMENG_PULSE_AWARE_REFERENCE_V1'
    drec=derivative_record_sparse(p,rec)
    assert drec.max_reference_disagreement<=1e-7
    idx={'weight':int(np.flatnonzero(p.weight==0.)[0]),'delay':int(np.flatnonzero(p.weight!=0)[-1]),'phase':0}
    for kind,i in idx.items():
        old=(p.weight if kind=='weight' else p.delay if kind=='delay' else rec.initial_theta).copy()
        ep,em=old.copy(),old.copy();ep[i]+=.0001;em[i]-=.0001
        def get(arr):
            x=p.with_weights(arr) if kind=='weight' else p.with_delays(arr) if kind=='delay' else p
            th=arr if kind=='phase' else rec.initial_theta
            return physical_rerecord_sparse(x,horizon=rec.horizon,initial_theta=th,history=rec.history)
        plus,minus=get(ep),get(em)
        assert plus.chart_valid and minus.chart_valid and plus.token==minus.token==rec.token
        fd=(plus.spike_times()-minus.spike_times())/.0002
        jac={'weight':drec.d_times_d_edge_weights,'delay':drec.d_times_d_edge_delays,'phase':drec.d_times_d_initial_theta}[kind]
        np.testing.assert_allclose(fd,jac[:,i],rtol=0,atol=3e-5)
    prepared=prepare_replay(rec,p)
    f=lambda wt: replay_sparse_fixed_chart(wt,jnp.asarray(p.delay),jnp.asarray(rec.initial_theta),rec,p,prepared=prepared)
    direct=np.zeros(p.e);direct[idx['weight']]=1
    _,jv=jax.jvp(f,(jnp.asarray(p.weight),),(jnp.asarray(direct),))
    y,pullback=jax.vjp(f,jnp.asarray(p.weight))
    u=np.linspace(.3,1.1,len(rec.spikes))
    adjoint=np.asarray(pullback(jnp.asarray(u))[0]); assert abs(np.asarray(jv)@u-direct@adjoint)<1e-8
    np.testing.assert_allclose(np.asarray(jv),drec.d_times_d_edge_weights@direct,atol=1e-8,rtol=0)
