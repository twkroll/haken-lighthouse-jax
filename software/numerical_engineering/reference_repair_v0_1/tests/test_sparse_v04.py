"""Deterministic NONCANONICAL engineering regression; no governed benchmarks."""
import numpy as np
import pytest
from numpy.testing import assert_allclose
from lighthouse_dev.reference import Parameters,physical_rerecord,sample_trajectory
from lighthouse_dev.sparse import SparseParameters,physical_rerecord_sparse,sample_sparse
from lighthouse_dev.sparse_replay import (prepare_replay,replay_sparse_fixed_chart,
                                          derivative_record_sparse,guarded_batch_replay)


def small_case():
    mask=np.array([[1,0],[1,1]],bool)
    w=np.array([[2.2,0.],[0.,2.5]])
    d=np.array([[.31,0.],[.83,.43]])
    return Parameters(w,d,adjacency=mask),((-3.,-.5),(-2.2,)),np.array([.3,1.1])


def ring_case(n=5):
    mask=np.eye(n,dtype=bool)
    for i in range(n):mask[(i+1)%n,i]=True
    w=np.zeros((n,n));d=np.zeros((n,n))
    for i in range(n):
        w[i,i]=1.7+.1*i;d[i,i]=.2+.06*i
        w[(i+1)%n,i]=.3;d[(i+1)%n,i]=.53+.17*i
    return (Parameters(w,d,adjacency=mask),
            tuple((float(-3.2-.23*i),) for i in range(n)),np.linspace(.12,1.53,n))


def _signatures(rec):
    return [(e.kind,e.neuron,e.source,e.ordinal) for e in rec.events]


def test_roundtrip_sparse_dense_and_immutable_zero_edges():
    p,_,_=small_case()
    s=SparseParameters.from_dense(p)
    assert s.n==2 and s.e==3
    assert s.weight[1]==0. and s.topology_id==SparseParameters.from_dense(p).topology_id
    assert_allclose(s.to_dense().W,p.W)
    assert_allclose(s.to_dense().delays[p.adjacency],p.delays[p.adjacency])
    with pytest.raises(ValueError):s.weight[1]=.1
    assert s.with_weights([2.2,-.1,2.5]).topology_id==s.topology_id


def test_invalid_edge_array_rejections():
    with pytest.raises(ValueError,match='sorted'):SparseParameters(2,[1,0],[0,1],[0,0],[1,1])
    with pytest.raises(ValueError,match='unique'):SparseParameters(2,[0,0],[1,1],[0,0],[1,1])
    with pytest.raises(ValueError,match='negative'):SparseParameters(1,[0],[0],[1],[-.1])
    with pytest.raises(ValueError,match='range'):SparseParameters(2,[3],[0],[0],[1])


def test_sparserecord_matches_dense_2_neurons_exact_event_signatures():
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    dr=physical_rerecord(p,horizon=40.,history=h,initial_theta=t)
    sr=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    assert dr.chart_valid and sr.chart_valid
    assert _signatures(dr)==_signatures(sr)
    assert_allclose([e.t for e in sr.events],[e.t for e in dr.events],atol=2e-10,rtol=0)
    assert_allclose(sr.final_theta,dr.final_theta,atol=2e-10,rtol=0)


def test_sparserecord_matches_dense_5_neurons_and_samples():
    p,h,t=ring_case()
    s=SparseParameters.from_dense(p)
    dr=physical_rerecord(p,horizon=33.,history=h,initial_theta=t)
    sr=physical_rerecord_sparse(s,horizon=33.,history=h,initial_theta=t)
    assert dr.chart_valid and sr.chart_valid
    assert _signatures(dr)==_signatures(sr)
    assert_allclose([e.t for e in dr.events],[e.t for e in sr.events],atol=1e-9,rtol=0)
    times=np.linspace(0.,33.,12)
    dense=sample_trajectory(p,dr,times)
    sparse=sample_sparse(s,sr,times)
    assert sparse['a'].shape==(12,s.e)
    assert_allclose(sparse['theta'],dense.theta,rtol=0,atol=1e-9)
    assert_allclose(sparse['psi'],dense.psi,rtol=0,atol=1e-9)
    for eid,(target,source) in enumerate(zip(s.target,s.source)):
        assert_allclose(sparse['a'][:,eid],dense.a[:,target,source],atol=1e-10)
        assert_allclose(sparse['q'][:,eid],dense.q[:,target,source],atol=1e-10)


def test_sparse_jax_scan_and_fd_at_zero_weight():
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    jac=derivative_record_sparse(s,rec,tol=2e-9)
    assert len(jac.times)==5
    assert jac.max_reference_disagreement<2e-9
    assert jac.d_times_d_edge_weights.shape==(len(rec.spikes),s.e)
    zero_id=int(np.flatnonzero((s.target==1)&(s.source==0))[0])
    eps=1e-4
    plus=s.weight.copy();minus=s.weight.copy()
    plus[zero_id]+=eps;minus[zero_id]-=eps
    pos=physical_rerecord_sparse(s.with_weights(plus),horizon=40.,history=h,initial_theta=t)
    neg=physical_rerecord_sparse(s.with_weights(minus),horizon=40.,history=h,initial_theta=t)
    assert pos.chart_valid and neg.chart_valid and pos.token==neg.token==rec.token
    fd=(pos.spike_times()-neg.spike_times())/(2*eps)
    assert np.max(np.abs(fd))>.001
    assert_allclose(jac.d_times_d_edge_weights[:,zero_id],fd,atol=3e-5,rtol=2e-4)


def test_sparse_jax_jit_scan_and_guarded_vmap():
    import jax
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    prepared=prepare_replay(rec,s)
    f=jax.jit(lambda w,d,ph:replay_sparse_fixed_chart(w,d,ph,rec,s,prepared=prepared))
    assert_allclose(np.asarray(f(s.weight,s.delay,t)),rec.spike_times(),atol=2e-9)
    weights=np.tile(s.weight,(3,1))
    weights[:,1]=[-1.e-4,0.,1.e-4]
    batch=guarded_batch_replay(s,rec,weights)
    assert batch.shape==(3,len(rec.spikes))
    assert_allclose(batch[1],rec.spike_times(),atol=2e-9)


def test_stale_topology_is_rejected_before_derivative():
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    s2=SparseParameters(2,[0,1],[0,1],[2.2,2.5],[.31,.43])
    with pytest.raises(ValueError,match='Stale/invalid'):
        derivative_record_sparse(s2,rec)


def test_boundary_at_t0_rejected_and_no_loss_of_packet():
    s=SparseParameters(1,[0],[0],[3.],[.5])
    rec=physical_rerecord_sparse(s,horizon=20.,history=((-0.5,),))
    assert not rec.chart_valid
    assert 'INITIAL_ARRIVAL_CHART_BOUNDARY' in rec.warnings
    with pytest.raises(ValueError,match='invalid'):
        derivative_record_sparse(s,rec)


def test_zero_delay_chart_rejected():
    s=SparseParameters(1,[0],[0],[0.],[0.])
    rec=physical_rerecord_sparse(s,horizon=20.)
    assert not rec.chart_valid
    assert any('ZERO_DELAY' in warning for warning in rec.warnings)


def test_no_edge_graph_first_hit_and_jax_replay():
    s=SparseParameters(1,[],[],[],[])
    rec=physical_rerecord_sparse(s,horizon=19.,initial_theta=np.array([0.]))
    assert rec.chart_valid and len(rec.spikes)==1
    assert_allclose(rec.spike_times()[0],2*np.pi*np.e,atol=2e-10)
    times=np.asarray(replay_sparse_fixed_chart(s.weight,s.delay,rec.initial_theta,rec,s))
    assert_allclose(times,rec.spike_times(),atol=2e-9)


def test_sparse_storage_bytes_n1000_e3000():
    n=1000
    targets=[];sources=[]
    for i in range(n):
        targets.extend([i,i,i]);sources.extend([i,(i+1)%n,(i+2)%n])
    order=np.lexsort((sources,targets))
    t=np.asarray(targets)[order];src=np.asarray(sources)[order]
    s=SparseParameters(n,t,src,np.ones(3*n),np.full(3*n,.25))
    assert s.e==3000
    sparse_alpha_bytes=np.zeros(s.e,dtype=np.float64).nbytes*2
    dense_alpha_bytes=np.zeros((n,n),dtype=np.float64).nbytes*2
    assert sparse_alpha_bytes==48000
    assert dense_alpha_bytes==16000000
    assert dense_alpha_bytes/sparse_alpha_bytes>300


def test_sparse_jax_fd_delay_and_initial_phase():
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    jac=derivative_record_sparse(s,rec)
    eps=1e-4
    for edgeid in (0,2):
        up=s.delay.copy();down=s.delay.copy()
        up[edgeid]+=eps;down[edgeid]-=eps
        plus=physical_rerecord_sparse(s.with_delays(up),horizon=40.,history=h,initial_theta=t)
        minus=physical_rerecord_sparse(s.with_delays(down),horizon=40.,history=h,initial_theta=t)
        assert plus.chart_valid and minus.chart_valid and plus.token==minus.token==rec.token
        fd=(plus.spike_times()-minus.spike_times())/(2*eps)
        assert_allclose(jac.d_times_d_edge_delays[:,edgeid],fd,rtol=2e-4,atol=3e-5)
    plus_t=t.copy();minus_t=t.copy();plus_t[0]+=eps;minus_t[0]-=eps
    plus=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=plus_t)
    minus=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=minus_t)
    assert plus.chart_valid and minus.chart_valid and plus.token==minus.token==rec.token
    assert_allclose(jac.d_times_d_initial_theta[:,0],
                    (plus.spike_times()-minus.spike_times())/(2*eps),rtol=2e-4,atol=3e-5)

def test_guarded_batch_rejects_history_partition_change():
    p,h,t=small_case();s=SparseParameters.from_dense(p)
    rec=physical_rerecord_sparse(s,horizon=40.,history=h,initial_theta=t)
    trial_delays=np.stack([s.delay.copy(),s.delay.copy()])
    # Emitted at -0.5 arrives after t0 at base 0.83, but before t0 at 0.2.
    trial_delays[1,1]=.2
    with pytest.raises(ValueError,match='Stale/invalid'):
        guarded_batch_replay(s,rec,np.stack([s.weight,s.weight]),delays=trial_delays)

def test_sparse_graph_is_frozen_not_inferred_from_weight():
    s=SparseParameters(2,[0,1],[0,0],[1.,0.],[.3,.9])
    assert len(s.outgoing[0])==2 and s.e==2
    q=s.with_weights([1.,-1.])
    assert q.topology_id==s.topology_id
    with pytest.raises(ValueError,match='integer'):
        SparseParameters(2,[0.5],[1],[.0],[.3])
    with pytest.raises(ValueError):s.incoming[1][0]=1
