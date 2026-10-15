"""Chart-aware inverse problem benchmark for CORE v0.18.

Recover (p, tau3) from synthetic labelled spike times inside one regular hybrid
chart. The fixed chart is differentiable; a separate chart margin detects the
first event-order collision and forbids blind continuation across it.
"""
from __future__ import annotations

import math
import argparse
from typing import NamedTuple

import jax
import jax.numpy as jnp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, least_squares

jax.config.update("jax_enable_x64", True)

ALPHA = 0.5
TWO_PI = 2.0 * math.pi
P_TRUE = -3.267985407948901
TAU_TRUE = 8.0
QMAX = 12
N = 3
SIGMA_T = 1.0e-4

GX_np, GW_np = leggauss(20)
GX = jnp.asarray(GX_np)
GW = jnp.asarray(GW_np)

# Ring edge metadata: e=3*s + {0:self,1:short,2:long}.
MODE = jnp.asarray([0, 1, 2] * 3, dtype=jnp.int32)
TARGET = jnp.asarray([0,1,2, 1,2,0, 2,0,1], dtype=jnp.int32)

# Known hybrid state after the two initial symmetric arrival batches.
PSI0 = jnp.asarray([-0.207423841618632] * 3)
Q0 = jnp.asarray([0.780899408476725] * 3)
PHI0 = jnp.asarray([1.838519273976891, 1.488519273976891, 1.658519273976891])

# Truth chart until six labelled firings have been observed.
# (kind, selected neuron/slot, truth dt, emitted slots for a firing)
CHART = (
    ("F",0,8.152762890488507,(0,1)),
    ("F",2,0.4133264085732442,(2,3)),
    ("F",1,0.39878960976146416,(4,5)),
    ("A",0,1.1878839816652915,None),
    ("A",2,0.4133264085732442,None),
    ("A",4,0.39878960976146427,None),
    ("A",1,5.1878839816652915,None),
    ("A",3,0.4133264085732442,None),
    ("A",5,0.39878960976146427,None),
    ("F",0,7.660810424419556,(0,1)),
    ("F",2,0.07291563283769714,(2,3)),
    ("F",1,0.6676961106216582,(4,5)),
)

TRUTH_SPIKES = np.asarray([
    8.152762890488507, 8.566089299061751, 8.964878908823215,
    24.62568933324277, 24.69860496608047, 25.36630107670213,
])

class State(NamedTuple):
    t: jax.Array
    psi: jax.Array
    q: jax.Array
    phi: jax.Array
    active: jax.Array
    edge_id: jax.Array
    rho: jax.Array


def response(x):
    y = x + 1.0
    ys = jnp.maximum(y, 1.0e-15)
    return jnp.where(y > 0.0, jnp.exp(-1.0 / (ys * ys)), 0.0)


def phase_gain_single(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e * (psi + q * s)
    return 0.5 * dt * jnp.sum(GW * response(ps))


def phase_gain_vec(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    return 0.5 * dt * jnp.sum(GW[None, :] * response(ps), axis=1)


def firing_root(psi, q, phi, guess):
    # Fixed-chart differentiable root: recorded truth dt is only a stop-gradient
    # initializer. Newton restores the implicit event-time derivative.
    t = jax.lax.stop_gradient(jnp.asarray(guess, dtype=jnp.float64))
    for _ in range(6):
        g = phi + phase_gain_single(psi, q, t) - TWO_PI
        e = jnp.exp(-ALPHA * t)
        psi_end = e * (psi + q * t)
        t = t - g / response(psi_end)
    return t


def edge_weight(p, edge):
    r = edge % 3
    return jnp.where(r == 0, 1.0, jnp.where(r == 1, p, -p))


def initial_state():
    return State(
        jnp.array(0.0), PSI0, Q0, PHI0,
        jnp.zeros(QMAX, dtype=bool),
        jnp.zeros(QMAX, dtype=jnp.int32),
        jnp.zeros(QMAX, dtype=jnp.float64),
    )


def advance(st, dt, tau):
    e = jnp.exp(-ALPHA * dt)
    psi = e * (st.psi + st.q * dt)
    q = e * st.q
    phi = st.phi + phase_gain_vec(st.psi, st.q, dt)
    speed = jnp.where(MODE[st.edge_id] == 1, 0.5, 1.0 / tau)
    rho = jnp.where(st.active, st.rho - speed * dt, st.rho)
    return State(st.t + dt, psi, q, phi, st.active, st.edge_id, rho)


def replay(theta):
    """Six labelled spike times on the recorded regular chart."""
    p, tau = theta
    st = initial_state()
    obs = []
    for kind, idx, truth_dt, slots in CHART:
        if kind == "A":
            edge = st.edge_id[idx]
            speed = jnp.where(MODE[edge] == 1, 0.5, 1.0 / tau)
            dt = st.rho[idx] / speed
        else:
            dt = firing_root(st.psi[idx], st.q[idx], st.phi[idx], truth_dt)
        st = advance(st, dt, tau)
        if kind == "A":
            edge = st.edge_id[idx]
            q = st.q.at[TARGET[edge]].add(edge_weight(p, edge) * ALPHA**2)
            st = st._replace(
                q=q,
                active=st.active.at[idx].set(False),
                rho=st.rho.at[idx].set(0.0),
            )
        else:
            i = idx
            phi = st.phi.at[i].add(-TWO_PI)
            q = st.q.at[i].add(ALPHA**2)
            active, edge_id, rho = st.active, st.edge_id, st.rho
            for slot, edge in zip(slots, (3*i+1, 3*i+2)):
                active = active.at[slot].set(True)
                edge_id = edge_id.at[slot].set(edge)
                rho = rho.at[slot].set(1.0)
            st = st._replace(phi=phi, q=q, active=active, edge_id=edge_id, rho=rho)
            obs.append(st.t)
    return jnp.stack(obs)


def state_before_step9(p):
    """Replay steps 0..8, then expose the state before the first chart collision."""
    tau = jnp.asarray(TAU_TRUE)
    st = initial_state()
    for kind, idx, truth_dt, slots in CHART[:9]:
        if kind == "A":
            edge = st.edge_id[idx]
            speed = jnp.where(MODE[edge] == 1, 0.5, 1.0 / tau)
            dt = st.rho[idx] / speed
        else:
            dt = firing_root(st.psi[idx], st.q[idx], st.phi[idx], truth_dt)
        st = advance(st, dt, tau)
        if kind == "A":
            edge = st.edge_id[idx]
            st = st._replace(
                q=st.q.at[TARGET[edge]].add(edge_weight(p, edge) * ALPHA**2),
                active=st.active.at[idx].set(False),
                rho=st.rho.at[idx].set(0.0),
            )
        else:
            i = idx
            active, edge_id, rho = st.active, st.edge_id, st.rho
            for slot, edge in zip(slots, (3*i+1, 3*i+2)):
                active = active.at[slot].set(True)
                edge_id = edge_id.at[slot].set(edge)
                rho = rho.at[slot].set(1.0)
            st = st._replace(
                phi=st.phi.at[i].add(-TWO_PI),
                q=st.q.at[i].add(ALPHA**2), active=active, edge_id=edge_id, rho=rho,
            )
    return st


def step9_chart_margin(p):
    """Reference event is neuron 0 firing; competitor is neuron 2 firing."""
    st = state_before_step9(jnp.asarray(p, dtype=jnp.float64))
    t0 = firing_root(st.psi[0], st.q[0], st.phi[0], CHART[9][2])
    t2 = firing_root(st.psi[2], st.q[2], st.phi[2], CHART[10][2])
    return t2 - t0


def inverse_checks():
    theta = jnp.asarray([P_TRUE, TAU_TRUE])
    y = np.asarray(replay(theta))
    assert np.max(np.abs(y - TRUTH_SPIKES)) < 1.0e-12

    jac_fun = jax.jit(jax.jacfwd(replay))
    J = np.asarray(jac_fun(theta))
    sv = np.linalg.svd(J, compute_uv=False)
    cond = float(sv[0] / sv[-1])
    assert sv[-1] > 0.14
    assert cond < 6.0

    h = 1.0e-6
    fd_cols = []
    for j in range(2):
        e = np.zeros(2); e[j] = 1.0
        yp = np.asarray(replay(theta + h * e))
        ym = np.asarray(replay(theta - h * e))
        fd_cols.append((yp - ym) / (2.0 * h))
    Jfd = np.column_stack(fd_cols)
    jac_fd_rel = float(np.linalg.norm(J - Jfd) / np.linalg.norm(Jfd))
    assert jac_fd_rel < 1.0e-7

    def residual(x, data=TRUTH_SPIKES):
        return np.asarray(replay(jnp.asarray(x))) - data
    def jacobian(x):
        return np.asarray(jac_fun(jnp.asarray(x)))

    starts = [(-3.0,7.7), (-3.5,8.2), (-2.9,8.15)]
    recovered = []
    for x0 in starts:
        sol = least_squares(
            residual, x0, jac=jacobian, max_nfev=50,
            xtol=1e-13, ftol=1e-13, gtol=1e-13,
        )
        recovered.append(sol.x)
        assert np.max(np.abs(sol.x - np.array([P_TRUE, TAU_TRUE]))) < 5.0e-12
        assert sol.nfev <= 6

    cov = SIGMA_T**2 * np.linalg.inv(J.T @ J)
    pred_std = np.sqrt(np.diag(cov))
    # Stored 20-realization noise audit; rerun only with --noise-direct.
    emp_std = np.asarray([0.000493373748929, 0.000568116085893])
    noise_mean = np.asarray([-3.267937029013076, 8.000069626492031])
    assert np.all(np.abs(emp_std / pred_std - 1.0) < 0.20)

    p_boundary = brentq(lambda p: float(step9_chart_margin(p)), -3.79, -3.78,
                        xtol=1e-13, rtol=1e-13)
    m_left = float(step9_chart_margin(-3.7870))
    m_right = float(step9_chart_margin(-3.7872))
    assert abs(p_boundary + 3.78713044385) < 2.0e-10
    assert m_left > 0.0 and m_right < 0.0

    return {
        "singular_values": sv,
        "condition_number": cond,
        "jacobian_vs_fd_relative_error": jac_fd_rel,
        "recovered": np.asarray(recovered),
        "predicted_noise_std": pred_std,
        "empirical_noise_std": emp_std,
        "noise_mean": noise_mean,
        "chart_boundary_p": p_boundary,
        "margin_p_minus3p7870": m_left,
        "margin_p_minus3p7872": m_right,
    }


def noise_direct():
    theta = jnp.asarray([P_TRUE, TAU_TRUE])
    jac_fun = jax.jit(jax.jacfwd(replay))
    J = np.asarray(jac_fun(theta))
    def jacobian(x):
        return np.asarray(jac_fun(jnp.asarray(x)))
    rng = np.random.default_rng(123)
    noisy = []
    for _ in range(20):
        data = TRUTH_SPIKES + rng.normal(scale=SIGMA_T, size=TRUTH_SPIKES.shape)
        sol = least_squares(
            lambda x: np.asarray(replay(jnp.asarray(x))) - data,
            (-3.2,7.95), jac=jacobian, max_nfev=20,
            xtol=1e-12, ftol=1e-12, gtol=1e-12,
        )
        noisy.append(sol.x)
    noisy = np.asarray(noisy)
    emp_std = noisy.std(axis=0, ddof=1)
    mean = noisy.mean(axis=0)
    print("noise mean/std", mean, emp_std)
    assert np.max(np.abs(emp_std - np.asarray([0.000493373748929, 0.000568116085893]))) < 2e-10


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--noise-direct", action="store_true")
    args = parser.parse_args()
    out = inverse_checks()
    print("CORE v0.18 chart-aware inverse problem checks passed")
    for key, value in out.items():
        print(key, value)
    if args.noise_direct:
        noise_direct()


if __name__ == "__main__":
    main()
