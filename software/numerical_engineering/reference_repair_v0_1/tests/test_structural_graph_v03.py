"""v0.3 noncanonical engineering-only graph/gradient tests.

No governed BC/V3C/TR execution, no trainable AI experiment and no RNG.
"""
import numpy as np
import pytest
from numpy.testing import assert_allclose
from lighthouse_dev import Parameters, physical_rerecord, sample_trajectory
from lighthouse_dev.replay import derivative_record, replay_fixed_chart


def _zero_edge_case():
    # [target,source].  Source 0 -> target 1 exists even when W[1,0]=0.
    adjacency = np.array([[True, False], [True, True]])
    weights = np.array([[2.2, 0.0], [0.0, 2.5]])
    delays = np.array([[0.31, 0.0], [0.83, 0.43]])
    p = Parameters(weights, delays, adjacency=adjacency)
    history = ((-3.0, -0.5), (-2.2,))
    theta = np.array([0.3, 1.1])
    return p, history, theta


def test_strict_boolean_graph_and_absent_weight_validation():
    w = np.zeros((2, 2)); d = np.zeros((2, 2))
    with pytest.raises(ValueError, match='Boolean'):
        Parameters(w, d, adjacency=np.ones((2, 2), dtype=int))
    with pytest.raises(ValueError, match='Boolean'):
        Parameters(w, d, adjacency=np.ones((3, 3), dtype=bool))
    w[1, 0] = 0.25
    with pytest.raises(ValueError, match='absent'):
        Parameters(w, d, adjacency=np.zeros((2, 2), dtype=bool))


def test_explicit_zero_weight_connection_retains_arrival_packets():
    p, history, theta = _zero_edge_case()
    assert p.edge_count == 3
    assert p.W[1, 0] == 0. and bool(p.adjacency[1, 0])
    assert not p.W.flags.writeable and not p.adjacency.flags.writeable
    rec = physical_rerecord(p, horizon=40, history=history, initial_theta=theta)
    assert rec.chart_valid, rec.warnings
    # A zero-weight connection still carries physical packet timestamps.
    assert (1, 0, -1) in rec.initial_arrived
    assert any(e.kind == 'arrival' and e.neuron == 1 and e.source == 0
               for e in rec.events)
    assert rec.edge_mask[1][0]


def test_zero_weight_edge_vs_absent_edge_same_phases_but_different_chart():
    p, history, theta = _zero_edge_case()
    absent = Parameters(p.W, p.delays, adjacency=np.array([[1, 0], [0, 1]], dtype=bool))
    with_edge = physical_rerecord(p, horizon=40, history=history, initial_theta=theta)
    without_edge = physical_rerecord(absent, horizon=40, history=history, initial_theta=theta)
    assert with_edge.chart_valid and without_edge.chart_valid
    assert with_edge.token != without_edge.token
    assert len(with_edge.events) > len(without_edge.events)
    assert_allclose(with_edge.spike_times(), without_edge.spike_times(), atol=2e-10)
    with pytest.raises(ValueError, match='Stale/invalid'):
        derivative_record(absent, with_edge)


def test_zero_crossing_preserves_event_itinerary_and_jax_gradient():
    p, history, theta = _zero_edge_case()
    horizon = 40.
    rec = physical_rerecord(p, horizon=horizon, history=history, initial_theta=theta)
    assert rec.chart_valid, rec.warnings
    jac = derivative_record(p, rec, tol=2e-9)
    epsilon = 1e-4
    plus_w, minus_w = p.W.copy(), p.W.copy()
    plus_w[1, 0] = epsilon
    minus_w[1, 0] = -epsilon
    plus_p, minus_p = p.with_weights(plus_w), p.with_weights(minus_w)
    plus = physical_rerecord(plus_p, horizon=horizon, history=history, initial_theta=theta)
    minus = physical_rerecord(minus_p, horizon=horizon, history=history, initial_theta=theta)
    assert plus.chart_valid and minus.chart_valid, (plus.warnings, minus.warnings)
    assert plus.token == minus.token == rec.token
    fd = (plus.spike_times()-minus.spike_times())/(2*epsilon)
    derivative = jac.d_times_d_weights[:, 1, 0]
    assert np.max(np.abs(derivative)) > 1e-3
    assert_allclose(derivative, fd, rtol=2e-4, atol=3e-5)
    assert jac.max_reference_disagreement < 2e-9
    assert_allclose(np.asarray(replay_fixed_chart(p.W, p.delays, theta, rec)),
                    rec.spike_times(), atol=2e-9)


def test_absent_weight_and_delay_derivatives_are_zero():
    p, history, theta = _zero_edge_case()
    rec = physical_rerecord(p, horizon=40, history=history, initial_theta=theta)
    jac = derivative_record(p, rec)
    assert_allclose(jac.d_times_d_weights[:, 0, 1], 0., atol=0)
    assert_allclose(jac.d_times_d_delays[:, 0, 1], 0., atol=0)


def test_same_topology_weight_constructor_guards_outside_edges():
    p, _, _ = _zero_edge_case()
    changed = p.W.copy()
    changed[1, 0] = -0.4
    new = p.with_weights(changed)
    assert new.W[1, 0] == -0.4
    assert np.array_equal(p.adjacency, new.adjacency)
    changed[0, 1] = 0.1
    with pytest.raises(ValueError, match='absent'):
        p.with_weights(changed)
    # Legacy convenience mode is still available for existing callers.
    legacy = Parameters(p.W, p.delays)
    assert not legacy.adjacency[1, 0]


def test_five_neuron_heterogeneous_sparse_graph_runs_and_samples():
    n = 5
    adjacency = np.eye(n, dtype=bool)
    for source in range(n):
        adjacency[(source+1) % n, source] = True
    W = np.zeros((n, n))
    delays = np.zeros((n, n))
    for i in range(n):
        W[i, i] = 1.7 + 0.1*i
        delays[i, i] = 0.2 + 0.06*i
        W[(i+1) % n, i] = 0.3
        delays[(i+1) % n, i] = 0.53 + 0.17*i
    p = Parameters(W, delays, adjacency=adjacency)
    theta = np.linspace(0.12, 1.53, n)
    history = tuple((float(-3.2-0.23*i),) for i in range(n))
    rec = physical_rerecord(p, horizon=33., initial_theta=theta, history=history)
    assert rec.chart_valid, rec.warnings
    assert len(rec.spikes) >= 7
    assert p.edge_count == 10
    sampled = sample_trajectory(p, rec, np.linspace(0, 33, 12))
    assert sampled.theta.shape == (12, 5)
    assert sampled.a.shape == (12, 5, 5)
    assert_allclose(sampled.theta[-1], rec.final_theta, atol=1e-9)


def test_structural_mask_mutation_does_not_modify_original():
    adjacency = np.array([[1, 0], [1, 1]], dtype=bool)
    p = Parameters(np.zeros((2, 2)), np.ones((2, 2))*0.5, adjacency=adjacency)
    adjacency[1, 0] = False
    assert p.adjacency[1, 0]
    with pytest.raises(ValueError):
        p.adjacency[1, 0] = False
