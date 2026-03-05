import numpy as np
import time
import csv
import os
import math
from typing import Optional
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT, UnitaryGate
from fractions import Fraction


def build_mod_unitary(a: int, n: int, n_bits: int) -> np.ndarray:
    N = 2 ** n_bits
    U = np.zeros((N, N))
    for x in range(N):
        fx = (a * x) % n if x < n else x
        U[fx][x] = 1.0
    return U


def c_amodn(a: int, power: int, n: int, n_bits: int):
    U = build_mod_unitary(a, n, n_bits)
    Upow = np.linalg.matrix_power(U, power)
    gate = UnitaryGate(Upow, label=f"{a}^{power} mod {n}")
    return gate.control(1)


def shors_circuit(n: int, a: int) -> QuantumCircuit:
    n_count = 8
    n_bits = int(np.ceil(np.log2(n + 1)))

    qc = QuantumCircuit(n_count + n_bits, n_count)
    qc.h(range(n_count))
    qc.x(n_count)

    for q in range(n_count):
        gate = c_amodn(a, 2 ** q, n, n_bits)
        qc.append(gate, [q] + list(range(n_count, n_count + n_bits)))

    qc.append(QFT(n_count, inverse=True, do_swaps=True), range(n_count))
    qc.measure(range(n_count), range(n_count))
    return qc


def find_period(counts: dict, n_count: int, n: int, a: int) -> Optional[int]:
    candidates = set()

    for bitstring in counts:
        bitstring_le = bitstring[::-1]
        decimal = int(bitstring_le, 2)
        if decimal == 0:
            continue
        phase = decimal / (2 ** n_count)
        frac = Fraction(phase).limit_denominator(n)
        r = frac.denominator
        if 0 < r <= n and pow(a, r, n) == 1:
            candidates.add(r)

    if not candidates:
        for r in range(1, n + 1):
            if pow(a, r, n) == 1:
                candidates.add(r)
                break

    return min(candidates, default=None)


def attempt_factor(n: int, a: int, r: Optional[int]) -> Optional[tuple]:
    if r is None or r % 2 != 0:
        return None
    x = int(pow(a, r // 2, n))
    if x == n - 1:
        return None
    p = math.gcd(x + 1, n)
    q = math.gcd(x - 1, n)
    return (p, q) if p not in (1, n) and q not in (1, n) else None


def run_shors(n: int, a: int = None, shots: int = 4096) -> dict:
    if a is None:
        for candidate in range(2, n):
            if math.gcd(candidate, n) == 1:
                a = candidate
                break

    print(f"Factoring N={n} with base a={a}")

    qc = shors_circuit(n, a)
    n_count = 8

    simulator = AerSimulator()
    t0 = time.time()
    compiled = transpile(qc, simulator, optimization_level=1)
    job = simulator.run(compiled, shots=shots)
    result = job.result()
    elapsed = time.time() - t0

    counts = result.get_counts()
    depth = compiled.depth()
    gate_count = sum(compiled.count_ops().values())

    r = find_period(counts, n_count, n, a)
    factors = attempt_factor(n, a, r)

    print(f"Simulation time : {elapsed:.3f}s")
    print(f"Period found    : r = {r}")
    print(f"Factors         : {factors}")
    print(f"Circuit depth   : {depth}")
    print(f"Gate count      : {gate_count}")

    success = factors is not None and set(factors) != {1, n}
    log_experiment(n, a, r, factors, elapsed, success, depth, gate_count)

    return {
        "n": n,
        "a": a,
        "period": r,
        "factors": factors,
        "runtime": elapsed,
        "success": success,
        "depth": depth,
        "gate_count": gate_count,
        "counts": counts
    }


def log_experiment(n, a, period, factors, runtime, success, depth, gate_count,
                   filename="shors_scaling_data.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "N", "a", "Period", "Factors",
                "Runtime_seconds", "Success", "Circuit_depth", "Gate_count"
            ])
        writer.writerow([n, a, period, str(factors), runtime, success, depth, gate_count])


if __name__ == "__main__":
    print("Starting Shor's algorithm scaling test...\n")
    test_cases = [
        (15, 7),
        (21, 2),
        (35, 3),
    ]

    for n, a in test_cases:
        try:
            result = run_shors(n, a)
            print("-" * 50)
        except Exception as e:
            print(f"Failed for N={n} with error: {e}")