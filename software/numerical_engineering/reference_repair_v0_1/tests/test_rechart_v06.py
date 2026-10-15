"""v0.6 independent local regression fixtures; NO governed study data."""
import numpy as np
import pytest
from numpy.testing import assert_allclose

from lighthouse_dev.reference import Parameters
from lighthouse_dev.sparse import SparseParameters, physical_rerecord_sparse
from lighthouse_dev.rechart import collision_audit, rechart_batch


def base_case():
    mask=np.array([[True,False],[True,True]])
    w=np.array([[2.2,0.],[0.,2.5]])
    delays=np.array([[.31,0.],[.83,.43]])
    p=SparseParameters.from_dense(Parameters(w,delays,adjacency=mask))
    rec=physical_rerecord_sparse(p,horizon=40.,initial_theta=np.array([.3,1.1]),
                                 history=((-3.,-.5),(-2.2,)))
    assert rec.chart_valid
    return p,rec


def collision_fixture(epsilon=0.):
    # Exactly one isolated-clock spike at T; historical arrival at T+epsilon.
    t=2*np.pi*np.e
    p=SparseParameters(1,[0],[0],[0.],[2.+t+epsilon])
    rec=physical_rerecord_sparse(p,horizon=t+1,history=((-2.,),))
    return p,rec


def test_colliding_arrival_and_spike_is_flagged():
    p,r=collision_fixture()
    audit=collision_audit(p,r)
    assert not r.chart_valid
    assert audit.closest_by_type['SPIKE_ARRIVAL'].dt < 1e-10
    assert audit.pairs_below_threshold
    assert any('COLLISION' in x for x in audit.warnings)


def test_regular_near_collision_and_both_orders():
    states=[]
    for epsilon in (-1e-4,1e-4):
        p,r=collision_fixture(epsilon)
        assert r.chart_valid, r.warnings
        audit=collision_audit(p,r,threshold=1e-8)
        assert audit.closest_by_type['SPIKE_ARRIVAL'] is not None
        assert_allclose(audit.closest_pair.dt,1e-4,rtol=0,atol=1e-9)
        assert not audit.pairs_below_threshold
        states.append(r.token)
    assert states[0] != states[1]


def test_collision_threshold_is_a_diagnostic_not_generic_proof():
    p,r=collision_fixture(5e-7)
    assert r.chart_valid
    assert collision_audit(p,r,threshold=1e-6).pairs_below_threshold
    assert not collision_audit(p,r,threshold=1e-8).pairs_below_threshold
    with pytest.raises(ValueError): collision_audit(p,r,threshold=-1)


def test_near_simultaneous_spike_spike_and_genuine_separation():
    p=SparseParameters(2,[],[],[],[])
    r=physical_rerecord_sparse(p,horizon=19.,initial_theta=np.array([0.,0.]))
    audit=collision_audit(p,r)
    assert not r.chart_valid
    assert audit.closest_by_type['SPIKE_SPIKE'].dt==0
    far=physical_rerecord_sparse(p,horizon=19.,initial_theta=np.array([0.,.02]))
    assert far.chart_valid
    assert collision_audit(p,far).closest_by_type['SPIKE_SPIKE'].dt > .01


def test_rechart_same_chart_weight_signs_at_zero():
    p,r=base_case()
    ws=np.tile(p.weight,(3,1))
    ws[:,1]=[-1e-4,0.,1e-4]
    result=rechart_batch(p,r,ws)
    assert result.counts=={'SAME_CHART':3}
    assert len(result.buckets)==1 and result.vmap_calls==1
    assert result.physical_evaluations==4
    assert all(a.max_replay_error<1e-7 for a in result.entries)
    assert_allclose(result.entries[1].physical_spike_times,r.spike_times(),atol=1e-8)


def test_rechart_history_partition_and_bucket_groups():
    p,r=base_case()
    ws=np.tile(p.weight,(4,1))
    ds=np.tile(p.delay,(4,1))
    ds[1,1]=.20  # Historical arrival moves from +0.33 to -0.30.
    ds[2,1]=.22  # Same changed itinerary, another proposal.
    ds[3,1]=.50  # Exactly on t=0; must be invalid.
    result=rechart_batch(p,r,ws,delay_batch=ds)
    assert result.entries[0].status=='SAME_CHART'
    assert result.entries[1].status=='RECHARTED',result.entries[1]
    assert result.entries[2].status=='RECHARTED',result.entries[2]
    assert result.entries[3].status=='INVALID_CHART',result.entries[3]
    assert result.entries[3].replay_spike_times is None
    assert len(result.buckets)==2 and result.vmap_calls==2
    assert result.entries[1].token==result.entries[2].token != r.token
    assert max(x.max_replay_error for x in result.entries[:3])<1e-7


def test_invalid_input_isolated_without_terminating_other_members():
    p,r=base_case()
    ds=np.tile(p.delay,(3,1))
    ds[1,1]=-1.
    ds[2,1]=.5
    result=rechart_batch(p,r,np.tile(p.weight,(3,1)),delay_batch=ds,replay=False)
    assert [x.status for x in result.entries]==[
        'SAME_CHART','INVALID_PARAMETER','INVALID_CHART']
    assert result.vmap_calls==0
    assert result.entries[0].replay_spike_times is None


def test_stale_baseline_rejected():
    p,r=base_case()
    changed=p.with_delays(p.delay+0.001)
    with pytest.raises(ValueError,match='stale'):
        rechart_batch(changed,r,np.stack([changed.weight]))


def test_edge_free_clock_and_zero_spikes_supported():
    for h,horizon in ((-1.,19.),(0.,20.)):
        p=SparseParameters(1,[],[],[],[],h=h)
        r=physical_rerecord_sparse(p,horizon=horizon)
        assert r.chart_valid
        batch=np.zeros((2,0))
        result=rechart_batch(p,r,batch)
        assert result.counts=={'SAME_CHART':2}
        assert [len(x.replay_spike_times) for x in result.entries]==[len(r.spikes)]*2


def test_batch_schema_and_bad_tolerance_rejected():
    p,r=base_case()
    with pytest.raises(ValueError,match='shape'):
        rechart_batch(p,r,np.zeros((2,p.e+1)))
    with pytest.raises(ValueError):
        rechart_batch(p,r,np.zeros((1,p.e)),replay_tolerance=0)
    with pytest.raises(ValueError):
        rechart_batch(p,r,np.zeros((1,p.e)),phase_batch=np.zeros((1,p.n+1)))


def test_physical_rechart_is_deterministic():
    p,r=base_case()
    ws=np.tile(p.weight,(2,1))
    ds=np.tile(p.delay,(2,1));ds[1,1]=.2
    left=rechart_batch(p,r,ws,delay_batch=ds,replay=False)
    right=rechart_batch(p,r,ws,delay_batch=ds,replay=False)
    assert left.buckets==right.buckets
    assert left.entries==right.entries


def test_arrival_arrival_collision_is_separate_class():
    # Two zero-weight self edges, each with one historic packet arriving at t=1.
    p=SparseParameters(2,[0,1],[0,1],[0.,0.],[2.,3.])
    r=physical_rerecord_sparse(p,horizon=5.,history=((-1.,),(-2.,)))
    audit=collision_audit(p,r)
    assert not r.chart_valid
    assert audit.closest_by_type['ARRIVAL_ARRIVAL'].dt==0
    d=p.delay.copy(); d[1]+=1e-4
    shifted=p.with_delays(d)
    good=physical_rerecord_sparse(shifted,horizon=5.,history=((-1.,),(-2.,)))
    assert good.chart_valid
    assert_allclose(collision_audit(shifted,good).closest_pair.dt,1e-4,atol=1e-11)


def test_collision_crossing_makes_new_valid_chart_not_smooth_gradient():
    p,r=collision_fixture(epsilon=-1e-4)
    db=np.tile(p.delay,(3,1))
    db[1,0]+=1e-4    # Arrival exactly at the isolated-clock spike
    db[2,0]+=2e-4    # Arrival now after the spike
    result=rechart_batch(p,r,np.tile(p.weight,(3,1)),delay_batch=db)
    assert [a.status for a in result.entries] == [
        'SAME_CHART','INVALID_CHART','RECHARTED']
    assert result.vmap_calls==2
    assert result.entries[1].replay_spike_times is None
    assert_allclose(result.entries[0].physical_spike_times,
                    result.entries[2].physical_spike_times,atol=1e-9)


def test_horizon_boundary_event_is_invalid():
    t=2*np.pi*np.e
    p=SparseParameters(1,[],[],[],[])
    r=physical_rerecord_sparse(p,horizon=t,initial_theta=np.zeros(1))
    assert not r.chart_valid
    assert any('HORIZON' in s for s in r.warnings)
    audit=collision_audit(p,r)
    assert audit.min_horizon_distance < 1e-9


def test_empty_batch_supported():
    p,r=base_case()
    output=rechart_batch(p,r,np.empty((0,p.e)))
    assert output.entries==() and output.buckets==()
    assert output.physical_evaluations==1 and output.vmap_calls==0
