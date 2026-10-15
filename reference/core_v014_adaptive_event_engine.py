"""Full adaptive packet-queue Lighthouse reference for CORE v0.14.

The solver is an imperative scientific oracle, not the eventual production JAX
kernel. It implements the causal remaining-distance semantics of CORE v0.13
inside a full three-cell Lighthouse event network.

Run from the repository root with

    python reference/core_v014_adaptive_event_engine.py

Use ``--slow-passage-only`` for the 1e-5 comparison and ``--upper-only``
for the empirical upper persistence bracket of the large timing-modulated
attractor. The split keeps each reference invocation short.
"""

from __future__ import annotations

import argparse
import copy
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

PI = math.pi
ALPHA = 0.5
N = 3
P_ADAPT = -3.267985407948901

T_NS = 16.297496058505022
TAU_NS = 7.941411830425917
TAU_FIC = 7.94140373739
A_FIC = 0.0660575
C_NS = 1.0 / TAU_NS

TAU_TARGET = TAU_FIC - 5.0e-5
C0 = 1.0 / TAU_TARGET

L2 = 0.021546133331
S_TAU = -0.050533543527464524
WINDOW = TAU_NS - TAU_FIC
BETA1_FIC = S_TAU * (TAU_FIC - TAU_NS)
BETA2_EFF = -math.sqrt(4.0 * L2 * BETA1_FIC)

U_S = 0.03**2
KAPPA_ACTIVITY = 2.0e-6

GX, GW = leggauss(20)


def response_scalar(x: float) -> float:
    y = x + 1.0
    return math.exp(-1.0 / (y * y)) if y > 0.0 else 0.0


def response_vec(x):
    y = np.asarray(x) + 1.0
    return np.where(y > 0.0, np.exp(-1.0 / (y * y)), 0.0)


def phase_gain(psi: float, q: float, dt: float) -> float:
    if dt <= 0.0:
        return 0.0
    s = 0.5 * dt * (GX + 1.0)
    e = np.exp(-ALPHA * s)
    psi_s = e * (psi + q * s)
    return float(0.5 * dt * np.dot(GW, response_vec(psi_s)))


class Packet:
    __slots__ = ("source", "target", "weight", "rho", "kind")

    def __init__(self, source, target, weight, rho, kind):
        self.source = int(source)
        self.target = int(target)
        self.weight = float(weight)
        self.rho = float(rho)
        self.kind = str(kind)


class AdaptivePacketEngine:
    """Three-cell ring with exact alpha flow and causal packet propagation.

    Ring displacement convention:
      d=0: self, weight 1, zero delay;
      d=1: target=(source+1) mod 3, weight p, fixed delay 2;
      d=2: target=(source+2) mod 3, weight -p, unit path with adaptive speed c.

    The plasticity conversion follows CORE v0.12 locally:
      dc/dt = (epsilon/T_NS) [c_eq(A)-c].
    With kappa=0 this is exactly the no-feedback slow benchmark. When
    kappa>0, A is the most recently completed q=1 spike-time Fourier amplitude.
    c is continuous even though that held activity statistic updates by cycle.
    """

    def __init__(self, *, p=P_ADAPT, c=C_NS, epsilon=0.0, kappa=0.0, c0=C0):
        self.p = float(p)
        self.c = float(c)
        self.epsilon = float(epsilon)
        self.kappa = float(kappa)
        self.c0 = float(c0)
        self.rate = self.epsilon / T_NS

        self.t = 0.0
        self.psi = np.zeros(N)
        self.q = np.zeros(N)
        self.phi = np.zeros(N)

        self.packets: list[Packet] = []
        self.count = np.zeros(N, dtype=int)
        self.spike_times = [[] for _ in range(N)]

        self.A_held = 0.0
        self.cycle_A = []
        self.cycle_t = []
        self.periods = []
        self._last_cycle_mean = None

        # Define t=0 as a simultaneous firing batch.
        self._process_spikes(np.arange(N), initial=True)

    @staticmethod
    def activity_gate(u):
        return u / (u + U_S)

    def c_equilibrium(self):
        return self.c0 + self.kappa * self.activity_gate(self.A_held**2)

    def adaptive_distance(self, dt):
        if self.rate == 0.0:
            return self.c * dt
        ceq = self.c_equilibrium()
        return (
            ceq * dt
            + (self.c - ceq) * (1.0 - math.exp(-self.rate * dt)) / self.rate
        )

    def _advance_c(self, dt):
        if self.rate == 0.0:
            return
        ceq = self.c_equilibrium()
        self.c = ceq + (self.c - ceq) * math.exp(-self.rate * dt)

    def packet_time(self, packet):
        if packet.kind == "short":
            return packet.rho / 0.5

        if self.rate == 0.0:
            return packet.rho / self.c

        f = lambda dt: self.adaptive_distance(dt) - packet.rho
        ceq = self.c_equilibrium()
        cmin = min(self.c, ceq)
        hi = 1.2 * packet.rho / max(cmin, 1.0e-12) + 1.0e-12
        while f(hi) < 0.0:
            hi *= 2.0
        return brentq(f, 0.0, hi, xtol=1.0e-13, rtol=1.0e-13)

    def next_arrival_dt(self):
        if not self.packets:
            return math.inf
        return min(self.packet_time(p) for p in self.packets)

    def next_spike_dt(self, dtmax):
        best = math.inf
        for i in range(N):
            deficit = 2.0 * PI - self.phi[i]
            if deficit <= 1.0e-12:
                return 0.0

            if math.isfinite(dtmax):
                if phase_gain(self.psi[i], self.q[i], dtmax) + 1.0e-13 < deficit:
                    continue
                f = lambda dt: phase_gain(self.psi[i], self.q[i], dt) - deficit
                root = brentq(f, 0.0, dtmax, xtol=1.0e-12, rtol=1.0e-12)
            else:
                hi = 1.0
                while phase_gain(self.psi[i], self.q[i], hi) < deficit:
                    hi *= 2.0
                    if hi > 1.0e3:
                        raise RuntimeError("failed to bracket firing event")
                f = lambda dt: phase_gain(self.psi[i], self.q[i], dt) - deficit
                root = brentq(f, 0.0, hi, xtol=1.0e-12, rtol=1.0e-12)
            best = min(best, root)
        return best

    def advance(self, dt):
        if dt < -1.0e-12:
            raise RuntimeError("negative event step")
        dt = max(0.0, float(dt))

        for i in range(N):
            self.phi[i] += phase_gain(self.psi[i], self.q[i], dt)

        e = math.exp(-ALPHA * dt)
        self.psi = e * (self.psi + self.q * dt)
        self.q = e * self.q

        long_distance = self.adaptive_distance(dt)
        for packet in self.packets:
            if packet.kind == "short":
                packet.rho -= 0.5 * dt
            else:
                packet.rho -= long_distance

        self._advance_c(dt)
        self.t += dt

    def _update_completed_cycle(self):
        m = int(self.count.min())
        if m <= 0 or not np.all(self.count == m):
            return

        times = np.array([self.spike_times[i][-1] for i in range(N)])
        mean_time = float(times.mean())
        xi = np.exp(-1j * 2.0 * PI * np.arange(N) / N)
        A = abs(np.dot(times - mean_time, xi) / N)

        self.A_held = float(A)
        self.cycle_A.append(float(A))
        self.cycle_t.append(mean_time)
        if self._last_cycle_mean is not None:
            self.periods.append(mean_time - self._last_cycle_mean)
        self._last_cycle_mean = mean_time

    def _process_spikes(self, indices, *, initial=False):
        indices = np.asarray(indices, dtype=int)
        if initial:
            for i in indices:
                self.spike_times[i].append(self.t)
        else:
            for i in indices:
                self.phi[i] -= 2.0 * PI
                if abs(self.phi[i]) < 1.0e-10:
                    self.phi[i] = 0.0
                self.count[i] += 1
                self.spike_times[i].append(self.t)

        for i in indices:
            self.q[i] += ALPHA**2

        for source in indices:
            self.packets.append(Packet(source, (source + 1) % N, self.p, 1.0, "short"))
            self.packets.append(Packet(source, (source + 2) % N, -self.p, 1.0, "adaptive"))

        if not initial:
            self._update_completed_cycle()

    def _process_arrivals(self):
        arrived = [p for p in self.packets if p.rho <= 1.0e-9]
        if not arrived:
            rho_min = min(p.rho for p in self.packets)
            arrived = [p for p in self.packets if p.rho <= rho_min + 1.0e-10]

        for packet in arrived:
            self.q[packet.target] += packet.weight * ALPHA**2

        ids = {id(p) for p in arrived}
        self.packets = [p for p in self.packets if id(p) not in ids]

    def step(self):
        dt_arrival = self.next_arrival_dt()
        dt_spike = self.next_spike_dt(dt_arrival)
        dt = min(dt_arrival, dt_spike)
        if not math.isfinite(dt):
            raise RuntimeError("no future event")

        self.advance(dt)

        # Arrivals do not jump phase, so a threshold already reached at the
        # common time remains a firing event.
        if dt_arrival <= dt + 1.0e-8:
            self._process_arrivals()

        firing = np.where(self.phi >= 2.0 * PI - 2.0e-8)[0]
        if len(firing):
            self._process_spikes(firing)

    def run_cycles(self, cycles):
        start = int(self.count.min())
        while int(self.count.min()) - start < cycles:
            self.step()

    def set_adaptation(self, epsilon, *, kappa=None, c0=None):
        self.epsilon = float(epsilon)
        self.rate = self.epsilon / T_NS
        if kappa is not None:
            self.kappa = float(kappa)
        if c0 is not None:
            self.c0 = float(c0)


def warm_synchronous(tau, cycles=80):
    engine = AdaptivePacketEngine(c=1.0 / tau, c0=1.0 / tau)
    engine.run_cycles(cycles)
    return engine


def prepare_center_seed(A_guess=1.0e-3):
    engine = warm_synchronous(TAU_NS, 80)
    nu = response_scalar(float(engine.psi[0]))
    desired_dt = 2.0 * A_guess * np.cos(2.0 * PI * np.arange(N) / N)
    engine.phi += -nu * desired_dt
    engine.run_cycles(20)
    return engine


def reduced_to_fic(epsilon, seed, kappa=0.0):
    def H(u):
        return u / (u + U_S)

    def rhs(n, y):
        A, c = y
        tau = 1.0 / c
        beta1 = S_TAU * (tau - TAU_NS)
        dA = A * (beta1 + BETA2_EFF * A**2 + L2 * A**4)
        dc = epsilon * (C0 - c + kappa * H(A * A))
        return [dA, dc]

    def event_fic(n, y):
        return 1.0 / y[1] - TAU_FIC

    event_fic.terminal = True
    event_fic.direction = -1
    sol = solve_ivp(
        rhs,
        [0.0, 1.0e8],
        [seed, C_NS],
        events=event_fic,
        rtol=1.0e-10,
        atol=[1.0e-13, 1.0e-16],
        max_step=1.0e4,
    )
    return float(sol.t_events[0][0]), float(sol.y_events[0][0, 0])


def full_to_fic(seed_state, epsilon, kappa=0.0):
    engine = copy.deepcopy(seed_state)
    engine.set_adaptation(epsilon, kappa=kappa, c0=C0)
    start = int(engine.count.min())
    while 1.0 / engine.c > TAU_FIC:
        engine.step()
    return engine, int(engine.count.min()) - start


def tail_stats(values, n=500):
    x = np.asarray(values[-n:], dtype=float)
    return {"mean": float(x.mean()), "std": float(x.std()), "min": float(x.min()), "max": float(x.max())}


def psi_interval_extrema(psi, q, dt):
    times = [0.0, dt]
    if abs(q) > 1.0e-15:
        critical = (q - ALPHA * psi) / (ALPHA * q)
        if 0.0 < critical < dt:
            times.append(critical)
    values = [math.exp(-ALPHA * t) * (psi + q * t) for t in times]
    return min(values), max(values)


def smoothness_audit(engine, cycles=300):
    probe = copy.deepcopy(engine)
    start = int(probe.count.min())
    psi_min = math.inf
    psi_max = -math.inf
    max_packets = len(probe.packets)
    min_step = math.inf

    while int(probe.count.min()) - start < cycles:
        dt_arrival = probe.next_arrival_dt()
        dt_spike = probe.next_spike_dt(dt_arrival)
        dt = min(dt_arrival, dt_spike)
        for i in range(N):
            lo, hi = psi_interval_extrema(float(probe.psi[i]), float(probe.q[i]), dt)
            psi_min = min(psi_min, lo)
            psi_max = max(psi_max, hi)
        min_step = min(min_step, dt)
        probe.step()
        max_packets = max(max_packets, len(probe.packets))

    return {
        "psi_min": float(psi_min),
        "psi_max": float(psi_max),
        "threshold_margin": float(psi_min + 1.0),
        "max_packets": int(max_packets),
        "min_event_step": float(min_step),
    }


def bistability_test():
    low = warm_synchronous(7.8, 80)
    nu = response_scalar(float(low.psi[0]))
    low.phi += -nu * (2.0e-3 * np.cos(2.0 * PI * np.arange(N) / N))
    low.run_cycles(2500)
    low_stats = tail_stats(low.cycle_A)

    large8 = copy.deepcopy(low)
    large8.c = 1.0 / 8.0
    large8.c0 = large8.c
    large8.set_adaptation(0.0, kappa=0.0)
    large8.run_cycles(2500)
    large_stats = tail_stats(large8.cycle_A)
    large_period = tail_stats(large8.periods)

    small8 = warm_synchronous(8.0, 80)
    nu8 = response_scalar(float(small8.psi[0]))
    small8.phi += -nu8 * (2.0e-3 * np.cos(2.0 * PI * np.arange(N) / N))
    small8.run_cycles(2200)
    small_stats = tail_stats(small8.cycle_A, 200)

    return low_stats, large_stats, large_period, small_stats, large8


def main():
    sync = warm_synchronous(TAU_NS, 80)
    frozen_period = float(sync.periods[-1])
    assert abs(frozen_period - T_NS) < 1.0e-6

    last = [sync.spike_times[i][-10:] for i in range(N)]
    spreads = [max(last[i][k] for i in range(N)) - min(last[i][k] for i in range(N)) for k in range(10)]
    assert max(spreads) < 1.0e-12

    seed = prepare_center_seed()
    A0 = float(seed.A_held)
    assert 9.5e-4 < A0 < 1.05e-3

    table = []
    for epsilon in (1.0e-3, 3.0e-4, 1.0e-4):
        full, cycles = full_to_fic(seed, epsilon, 0.0)
        n_red, A_red = reduced_to_fic(epsilon, A0, 0.0)
        rel = (float(full.A_held) - A_red) / A_red
        assert abs(rel) < 1.0e-3
        table.append((epsilon, cycles, float(full.A_held), n_red, A_red, rel))

    full_fb, cycles_fb = full_to_fic(seed, 1.0e-4, KAPPA_ACTIVITY)
    n_fb, A_fb = reduced_to_fic(1.0e-4, A0, KAPPA_ACTIVITY)
    rel_fb = (float(full_fb.A_held) - A_fb) / A_fb
    assert abs(rel_fb) < 1.0e-3

    low, large, large_period, small, large8 = bistability_test()
    assert low["mean"] > 0.7
    assert large["mean"] > 0.6
    assert small["mean"] < 1.0e-5

    smooth = smoothness_audit(large8, 300)
    assert smooth["threshold_margin"] > 0.4
    assert smooth["max_packets"] <= 6

    print("CORE v0.14 full adaptive packet-queue checks passed")
    print("frozen period at NS=", frozen_period, "reference=", T_NS)
    print("prepared center amplitude=", A0)
    print("no-feedback full vs reduced table:")
    for row in table:
        print(row)
    print("feedback eps=1e-4:", cycles_fb, full_fb.A_held, n_fb, A_fb, rel_fb)
    print("tau=7.8 large-state stats=", low)
    print("tau=8.0 large-state stats=", large)
    print("tau=8.0 large-state period stats=", large_period)
    print("tau=8.0 small-seed sync-basin stats=", small)
    print("tau=8.0 large-state smoothness audit=", smooth)


def slow_passage_check():
    seed = prepare_center_seed()
    A0 = float(seed.A_held)
    full_slow, cycles_slow = full_to_fic(seed, 1.0e-5, 0.0)
    n_slow, A_slow = reduced_to_fic(1.0e-5, A0, 0.0)
    rel_slow = (float(full_slow.A_held) - A_slow) / A_slow
    assert abs(rel_slow) < 1.0e-3
    assert float(full_slow.A_held) / A_FIC < 0.02
    print("CORE v0.14 slow-passage check:", cycles_slow, full_slow.A_held, n_slow, A_slow, rel_slow)


def upper_bracket_check():
    _, _, _, _, large8 = bistability_test()

    keep = copy.deepcopy(large8)
    keep.c = 1.0 / 8.0073
    keep.c0 = keep.c
    keep.set_adaptation(0.0, kappa=0.0)
    keep.run_cycles(3000)
    keep_stats = tail_stats(keep.cycle_A)

    lose = copy.deepcopy(large8)
    lose.c = 1.0 / 8.0075
    lose.c0 = lose.c
    lose.set_adaptation(0.0, kappa=0.0)
    lose.run_cycles(6000)
    lose_stats = tail_stats(lose.cycle_A)

    assert keep_stats["mean"] > 0.5
    assert lose_stats["mean"] < 5.0e-4
    print("CORE v0.14 upper persistence tau=8.0073:", keep_stats)
    print("CORE v0.14 upper loss tau=8.0075:", lose_stats)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--slow-passage-only", action="store_true")
    parser.add_argument("--upper-only", action="store_true")
    args = parser.parse_args()

    if args.slow_passage_only:
        slow_passage_check()
    elif args.upper_only:
        upper_bracket_check()
    else:
        main()
