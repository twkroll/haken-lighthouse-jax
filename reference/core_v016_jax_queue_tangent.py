"""Differentiable fixed-chart event maps for CORE v0.16.

The value scheduler may use bisection/argmin, but scientific derivatives are
computed only inside a fixed event chart. Roots are refined by Newton with a
``stop_gradient`` initial guess so JAX recovers the implicit event-time
sensitivity without differentiating through discrete bracketing decisions.
"""
from __future__ import annotations

import math
import numpy as np
import jax
import jax.numpy as jnp

from core_v016_jax_queue_kernel import ALPHA, N, TWO_PI, GX, GW, response

jax.config.update("jax_enable_x64", True)


def phase_gain_single(psi, q, dt):
    s = 0.5 * dt * (GX + 1.0)
    e = jnp.exp(-ALPHA * s)
    ps = e * (psi + q * s)
    return 0.5 * dt * jnp.sum(GW * response(ps))


def flow_scalar(psi, q, dt):
    e = jnp.exp(-ALPHA * dt)
    return e * (psi + q * dt), e * q


def _fire_root_raw(psi, q, phi, guess):
    t0 = jax.lax.stop_gradient(jnp.asarray(guess, dtype=jnp.float64))
    def body(_, t):
        g = phi + phase_gain_single(psi, q, t) - TWO_PI
        psi_end, _ = flow_scalar(psi, q, t)
        return t - g / response(psi_end)
    return jax.lax.fori_loop(0, 7, body, t0)


def firing_time(x, neuron=0, guess=10.0):
    x = jnp.asarray(x, dtype=jnp.float64)
    psi = x[0:N]; q = x[N:2*N]; phi = x[2*N:3*N]
    return _fire_root_raw(psi[neuron], q[neuron], phi[neuron], guess)


def firing_chart(x, neuron=0, guess=10.0):
    x = jnp.asarray(x, dtype=jnp.float64)
    psi = x[0:N]; q = x[N:2*N]; phi = x[2*N:3*N]; c = x[-1]
    dt = firing_time(x, neuron, guess)
    s = 0.5 * dt * (GX + 1.0)
    e_quad = jnp.exp(-ALPHA * s)
    psi_s = e_quad[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    gain = 0.5 * dt * jnp.sum(GW[None, :] * response(psi_s), axis=1)
    e = jnp.exp(-ALPHA * dt)
    psi2 = e * (psi + q * dt); q2 = e * q; phi2 = phi + gain
    phi2 = phi2.at[neuron].add(-TWO_PI)
    q2 = q2.at[neuron].add(ALPHA**2)
    return jnp.concatenate([psi2, q2, phi2, jnp.array([c])])


def arrival_time_frozen(rho, c):
    return rho / c


def arrival_chart(x, target=1, weight=1.7):
    x = jnp.asarray(x, dtype=jnp.float64)
    psi = x[0:N]; q = x[N:2*N]; phi = x[2*N:3*N]
    c = x[3*N]; rho = x[3*N+1]
    dt = arrival_time_frozen(rho, c)
    s = 0.5 * dt * (GX + 1.0)
    e_quad = jnp.exp(-ALPHA * s)
    psi_s = e_quad[None, :] * (psi[:, None] + q[:, None] * s[None, :])
    gain = 0.5 * dt * jnp.sum(GW[None, :] * response(psi_s), axis=1)
    e = jnp.exp(-ALPHA * dt)
    psi2 = e * (psi + q * dt); q2 = e * q; phi2 = phi + gain
    q2 = q2.at[target].add(weight * ALPHA**2)
    return jnp.concatenate([psi2, q2, phi2, jnp.array([c, 0.0])])


def central_directional(fun, x, v, h=1.0e-6):
    x = np.asarray(x, dtype=float); v = np.asarray(v, dtype=float)
    return (np.asarray(fun(x+h*v)) - np.asarray(fun(x-h*v))) / (2*h)


def tangent_checks():
    target_endpoint = -2.288917546306807
    S_end = -1.0 / target_endpoint
    psi_end = 1.0 / math.sqrt(-math.log(S_end)) - 1.0
    psi0 = psi_end * math.exp(ALPHA)
    q0 = 0.0
    gain1 = float(phase_gain_single(psi0, q0, 1.0))
    phi0 = TWO_PI - gain1
    psi = np.array([psi0, 0.05, -0.12])
    q = np.array([q0, -0.03, 0.04])
    phi = np.array([phi0, 1.20, 0.70])
    xf = np.r_[psi, q, phi, 0.125]
    tf = lambda z: firing_time(z, 0, 1.0)
    chartf = lambda z: firing_chart(z, 0, 1.0)
    tval = float(tf(jnp.asarray(xf)))
    dtdphi = float(jax.grad(tf)(jnp.asarray(xf))[2*N])
    psi_e, _ = flow_scalar(psi[0], q[0], tval)
    implicit = -1.0 / float(response(psi_e))
    rng = np.random.default_rng(1234)
    vf = rng.normal(size=xf.size); vf /= np.linalg.norm(vf)
    _, jvp_f = jax.jvp(chartf, (jnp.asarray(xf),), (jnp.asarray(vf),))
    fd_f = central_directional(chartf, xf, vf, 2.0e-6)
    rel_f = float(np.linalg.norm(np.asarray(jvp_f)-fd_f) / np.linalg.norm(fd_f))

    rho = 0.747999776493991
    xa = np.r_[np.array([0.11,-0.07,0.02]), np.array([0.08,0.03,-0.02]),
               np.array([1.1,0.8,0.4]), 0.125, rho]
    ta = lambda z: arrival_time_frozen(z[3*N+1], z[3*N])
    grad_ta = np.asarray(jax.grad(ta)(jnp.asarray(xa)))
    chart_a = lambda z: arrival_chart(z, 1, 1.7)
    va = rng.normal(size=xa.size); va /= np.linalg.norm(va)
    _, jvp_a = jax.jvp(chart_a, (jnp.asarray(xa),), (jnp.asarray(va),))
    fd_a = central_directional(chart_a, xa, va, 2.0e-6)
    rel_a = float(np.linalg.norm(np.asarray(jvp_a)-fd_a) / np.linalg.norm(fd_a))
    return {
        "fire_time": tval,
        "fire_dtime_dphi": dtdphi,
        "fire_implicit": implicit,
        "fire_jvp_relerr": rel_f,
        "arrival_dtime_drho": float(grad_ta[3*N+1]),
        "arrival_dtime_dc": float(grad_ta[3*N]),
        "arrival_jvp_relerr": rel_a,
    }


if __name__ == "__main__":
    out = tangent_checks(); print(out)
    assert abs(out["fire_dtime_dphi"]-out["fire_implicit"]) < 2e-8
    assert abs(out["fire_implicit"]+2.288917546306807) < 2e-10
    assert out["fire_jvp_relerr"] < 5e-8
    assert abs(out["arrival_dtime_drho"]-8.0) < 1e-12
    assert abs(out["arrival_dtime_dc"]+47.87198569561542) < 5e-10
    assert out["arrival_jvp_relerr"] < 5e-8
