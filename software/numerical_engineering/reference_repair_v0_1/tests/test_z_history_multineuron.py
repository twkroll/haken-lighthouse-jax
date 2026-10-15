"""NONCANONICAL engineering tests, not frozen BC/V3C confirmation."""
import numpy as np
import pytest
from numpy.testing import assert_allclose
from scipy.integrate import quad
from scipy.optimize import brentq
from lighthouse_dev import Parameters, physical_rerecord, normalize_history, alpha_kernel, response
from lighthouse_dev.replay import derivative_record


def test_reject_bad_prehistory():
    for malformed in (((-1, -1.),), ((-1., 0.),), ((-.5, -1.),), ((float('nan'),),)):
        with pytest.raises(ValueError):
            normalize_history(malformed, 1)
    with pytest.raises(ValueError):
        normalize_history([(-1.,)], 2)


def test_prehistory_filter_seed_and_packet_in_flight():
    # One edge source=0 -> target=1, with distinct arrived and in-flight pulses.
    W = np.array([[0., 0.], [2., 0.]])
    delays = np.array([[0., 0.], [1.8, 0.]])
    p = Parameters(W, delays)
    history = ((-3., -.5), ())
    rec = physical_rerecord(p, history=history, horizon=25., initial_theta=[.25, 1.7])
    assert rec.chart_valid, rec.warnings
    age = 3-1.8
    assert_allclose(rec.initial_a[1,0], alpha_kernel(1.,age), atol=2e-15)
    assert_allclose(rec.initial_q[1,0], np.exp(-age), atol=2e-15)
    assert rec.initial_arrived == ((1, 0, -1),)
    pending = [e for e in rec.events if e.kind == 'arrival' and e.ordinal == 0]
    assert len(pending) == 1
    assert_allclose(pending[0].t, 1.3, atol=1e-13)
    assert rec.initial_a[0,0] == 0.
    assert rec.initial_q[0,0] == 0.


def test_history_alpha_first_hit_vs_independent_convolution():
    p = Parameters(np.array([[2.7]]), np.array([[1.3]]))
    past = [-4., -.5]
    rec = physical_rerecord(p, history=(past,), horizon=23., initial_theta=[0.2])
    assert rec.chart_valid, rec.warnings

    def exact_rate(t):
        psi = 2.7 * sum(alpha_kernel(1., t-emit-1.3) for emit in past)
        return response(psi, 1., -1.)

    def phase_gap(t):
        # Independent convolution directly using original spike times, split
        # at packet arrivals so independent quadrature sees each input kink.
        knots = [0., .8, t] if t > .8 else [0., t]
        return .2 + sum(quad(exact_rate, lo, hi, epsabs=3e-12, epsrel=3e-12)[0]
                        for lo, hi in zip(knots[:-1], knots[1:])) - 2*np.pi

    expected = brentq(phase_gap, .01, 23., xtol=1e-11)
    assert_allclose(rec.spike_times()[0], expected, atol=1e-9)


def test_history_partition_change_rejected_even_if_same_future_spikes():
    p = Parameters(np.array([[2.3]]), np.array([[1.1]]))
    old = physical_rerecord(p, horizon=12., history=((-1.,),), initial_theta=[2.0])
    assert old.chart_valid
    newp = Parameters(p.W, np.array([[.6]]))
    new = physical_rerecord(newp, horizon=12., history=old.history, initial_theta=old.initial_theta)
    assert new.initial_arrived != old.initial_arrived
    assert new.token != old.token
    with pytest.raises(ValueError, match='Stale/invalid'):
        derivative_record(newp, old)


def test_arrival_collision_fails_strict_derivative_chart():
    p = Parameters(np.array([[1., 0.], [1., 0.]]),
                   np.array([[1.2, 0.], [1.2, 0.]]))
    rec = physical_rerecord(p, horizon=4., history=((-.2,), ()), initial_theta=[.1, .3])
    assert not rec.chart_valid
    assert any('COLLISION' in s for s in rec.warnings)
    with pytest.raises(ValueError, match='Invalid reference chart'):
        from lighthouse_dev.replay import replay_fixed_chart
        replay_fixed_chart(p.W, p.delays, rec.initial_theta, rec)


def test_two_neuron_history_jax_ad_fd_crosscheck():
    p = Parameters(np.array([[2.2, 0.8], [0.6, 2.5]]),
                   np.array([[0.37, 0.73], [1.11, 0.41]]))
    history = ((-3., -.75), (-2.1,))
    theta = np.array([.5, 1.4])
    horizon = 48.
    rec = physical_rerecord(p, horizon=horizon, initial_theta=theta, history=history)
    assert rec.chart_valid, rec.warnings
    assert len(rec.spikes) == 6
    # One queued prespike packet arrives after t=0.
    assert rec.events[0].kind == 'arrival' and rec.events[0].ordinal == 0
    jac = derivative_record(p, rec, tol=1e-9)
    assert jac.max_reference_disagreement < 1e-10

    def record(W, delays, phase):
        return physical_rerecord(Parameters(W, delays), horizon=horizon,
                                 initial_theta=phase, history=history)

    eps = 1e-4
    Wp, Wm = p.W.copy(), p.W.copy()
    Wp[0,1] += eps
    Wm[0,1] -= eps
    Dp, Dm = p.delays.copy(), p.delays.copy()
    Dp[1,0] += eps
    Dm[1,0] -= eps
    tp, tm = theta.copy(), theta.copy()
    tp[0] += eps
    tm[0] -= eps

    for plus, minus, predicted in (
        (record(Wp,p.delays,theta),record(Wm,p.delays,theta),jac.d_times_d_weights[:,0,1]),
        (record(p.W,Dp,theta),record(p.W,Dm,theta),jac.d_times_d_delays[:,1,0]),
        (record(p.W,p.delays,tp),record(p.W,p.delays,tm),jac.d_times_d_initial_theta[:,0]),
    ):
        assert plus.chart_valid and minus.chart_valid
        assert plus.token == rec.token == minus.token
        fd = (plus.spike_times()-minus.spike_times())/(2*eps)
        assert_allclose(predicted, fd, rtol=3e-4, atol=3e-5)


def test_three_neuron_sparse_graph_allows_distinct_histories():
    W = np.array([[1.5, 0., 1.8], [2.0, 1.3, 0.], [0., 1.1, 1.2]])
    delays = np.array([[.35, .0, .81], [.6, .42, .0], [.0, 1.3, .55]])
    p = Parameters(W, delays)
    h = ((-3.1, -.55), (-2.2,), (-4.0, -1.7))
    rec = physical_rerecord(p, horizon=42., history=h, initial_theta=[.2,.91,1.75])
    assert rec.chart_valid, rec.warnings
    assert len(rec.spikes) >= 5
    for i in range(3):
        t = rec.spike_times(i)
        assert np.all(np.diff(t) >= 2*np.pi - 1e-9)
    assert any(e.kind == 'arrival' and e.ordinal <= 0 for e in rec.events)


def test_sampled_states_recover_exact_final_phase_and_alpha():
    from lighthouse_dev import sample_trajectory
    p = Parameters(np.array([[2.2, .8],[.6, 2.5]]),
                   np.array([[.37, .73],[1.11, .41]]))
    rec = physical_rerecord(p, horizon=42., history=((-3., -.75),(-2.1,)),
                            initial_theta=[.5,1.4])
    snapshots = sample_trajectory(p, rec, np.linspace(0, 42, 41))
    assert_allclose(snapshots.theta[0], rec.initial_theta, atol=1e-15)
    assert_allclose(snapshots.a[0], rec.initial_a, atol=1e-15)
    assert_allclose(snapshots.q[0], rec.initial_q, atol=1e-15)
    assert_allclose(snapshots.theta[-1], rec.final_theta, atol=2e-10)
    assert_allclose(snapshots.psi, np.sum(p.W*snapshots.a, axis=2), atol=2e-12)

    # Even with identical event labels, an old record must not sample new physics.
    newp = Parameters(p.W+.1, p.delays)
    with pytest.raises(ValueError, match='stale'):
        sample_trajectory(newp, rec, np.array([0., 20.]))


def test_arrival_exactly_at_t0_has_invalid_derivative_chart():
    p = Parameters(np.array([[2.]]), np.array([[1.]]))
    rec = physical_rerecord(p, history=((-1.,),), horizon=12.)
    assert any('INITIAL_ARRIVAL_CHART_BOUNDARY' == warning for warning in rec.warnings)
    assert not rec.chart_valid
    assert any(e.kind == 'arrival' and e.t == 0. for e in rec.events)
