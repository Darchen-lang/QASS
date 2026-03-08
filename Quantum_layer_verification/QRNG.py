import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from scipy.stats import chisquare
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.compiler import transpile


NUM_BITS = 100000
RUNS = 10
BATCH_SIZE = 20


def classical_prng(num_bits: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 2, num_bits)


def quantum_rng(num_bits: int) -> np.ndarray:
    simulator = Aer.get_backend('aer_simulator')
    q_bits = []

    for _ in range(num_bits // BATCH_SIZE + 1):
        qc = QuantumCircuit(BATCH_SIZE, BATCH_SIZE)
        qc.h(range(BATCH_SIZE))
        qc.measure(range(BATCH_SIZE), range(BATCH_SIZE))
        job = simulator.run(transpile(qc, simulator), shots=1)
        result = job.result().get_counts()
        bitstring = list(result.keys())[0]
        q_bits.extend([int(b) for b in bitstring])

        if len(q_bits) >= num_bits:
            break

    return np.array(q_bits[:num_bits])


def calculate_entropy(bits: np.ndarray) -> float:
    p1 = np.mean(bits)
    p0 = 1 - p1
    return 0.0 if p0 == 0 or p1 == 0 else -p0 * np.log2(p0) - p1 * np.log2(p1)


def calculate_chi_square(bits: np.ndarray) -> tuple:
    observed = [np.sum(bits == 0), np.sum(bits == 1)]
    expected = [len(bits) / 2, len(bits) / 2]
    stat, p_value = chisquare(observed, expected)
    return stat, p_value


def runs_test(bits: np.ndarray) -> float:
    runs = 1 + sum(bits[i] != bits[i - 1] for i in range(1, len(bits)))
    expected_runs = (2 * np.sum(bits) * np.sum(1 - bits)) / len(bits) + 1
    return abs(runs - expected_runs) / expected_runs * 100


def serial_correlation(bits: np.ndarray) -> float:
    return float(np.corrcoef(bits[:-1], bits[1:])[0, 1])


def analyze_source(name: str, bits: np.ndarray) -> dict:
    ent = calculate_entropy(bits)
    chi_stat, p_value = calculate_chi_square(bits)
    runs_dev = runs_test(bits)
    correlation = serial_correlation(bits)
    entropy_efficiency = (ent / 1.0) * 100

    return {
        "source": name,
        "num_bits": len(bits),
        "entropy_bits": ent,
        "max_entropy": 1.0,
        "entropy_efficiency": entropy_efficiency,
        "chi_square_stat": chi_stat,
        "chi_square_p": p_value,
        "runs_deviation": runs_dev,
        "serial_correlation": correlation,
        "passes_uniformity": p_value > 0.05,
        "passes_correlation": abs(correlation) < 0.01
    }


def run_multiple_trials(runs: int) -> tuple:
    classical_entropies = []
    quantum_entropies = []
    classical_correlations = []
    quantum_correlations = []

    for i in range(runs):
        print(f"  Trial {i + 1}/{runs}...")
        c_bits = classical_prng(NUM_BITS, seed=i)
        q_bits = quantum_rng(NUM_BITS)

        classical_entropies.append(calculate_entropy(c_bits))
        quantum_entropies.append(calculate_entropy(q_bits))
        classical_correlations.append(abs(serial_correlation(c_bits)))
        quantum_correlations.append(abs(serial_correlation(q_bits)))

    return (classical_entropies, quantum_entropies,
            classical_correlations, quantum_correlations)


def log_results(classical: dict, quantum: dict, filename="qrng_entropy_data.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Source", "Num_Bits", "Entropy_bits", "Entropy_Efficiency",
                "Chi_Square_Stat", "Chi_Square_P", "Runs_Deviation",
                "Serial_Correlation", "Passes_Uniformity", "Passes_Correlation"
            ])
        for r in [classical, quantum]:
            writer.writerow([
                r["source"], r["num_bits"], r["entropy_bits"],
                r["entropy_efficiency"], r["chi_square_stat"],
                r["chi_square_p"], r["runs_deviation"],
                r["serial_correlation"], r["passes_uniformity"],
                r["passes_correlation"]
            ])


def plot_entropy_comparison(classical: dict, quantum: dict):
    sources = ["Classical PRNG", "Quantum RNG"]
    entropies = [classical["entropy_bits"], quantum["entropy_bits"]]
    colors = ['#e74c3c', '#2ecc71']

    plt.figure(figsize=(8, 5))
    bars = plt.bar(sources, entropies, color=colors, width=0.4)
    plt.axhline(y=1.0, color='black', linestyle='--', linewidth=1, label="Max Entropy (1.0 bit)")
    plt.ylim(0.999, 1.0001)
    plt.ylabel("Shannon Entropy (bits per bit)")
    plt.title("Entropy Comparison: Classical PRNG vs Quantum RNG")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5, axis='y')
    for bar, val in zip(bars, entropies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                 f'{val:.8f}', ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig("qrng_entropy_comparison.png", dpi=300)
    plt.show()


def plot_entropy_distribution(classical_entropies: list, quantum_entropies: list):
    plt.figure(figsize=(9, 5))
    plt.hist(classical_entropies, bins=20, alpha=0.6, color='#e74c3c',
             label="Classical PRNG", edgecolor='white')
    plt.hist(quantum_entropies, bins=20, alpha=0.6, color='#2ecc71',
             label="Quantum RNG", edgecolor='white')
    plt.axvline(x=1.0, color='black', linestyle='--', linewidth=1, label="Max Entropy")
    plt.xlabel("Shannon Entropy (bits per bit)")
    plt.ylabel("Frequency")
    plt.title(f"Entropy Distribution over {RUNS} Trials")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig("qrng_entropy_distribution.png", dpi=300)
    plt.show()


def plot_correlation_comparison(classical: dict, quantum: dict):
    sources = ["Classical PRNG", "Quantum RNG"]
    correlations = [abs(classical["serial_correlation"]), abs(quantum["serial_correlation"])]
    colors = ['#e74c3c', '#2ecc71']

    plt.figure(figsize=(8, 5))
    plt.bar(sources, correlations, color=colors, width=0.4)
    plt.axhline(y=0.01, color='black', linestyle='--', linewidth=1,
                label="Correlation Threshold (0.01)")
    plt.ylabel("Serial Correlation (absolute)")
    plt.title("Serial Correlation: Classical PRNG vs Quantum RNG")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5, axis='y')
    plt.tight_layout()
    plt.savefig("qrng_correlation.png", dpi=300)
    plt.show()


def plot_trial_entropies(classical_entropies: list, quantum_entropies: list):
    trials = list(range(1, RUNS + 1))
    plt.figure(figsize=(10, 5))
    plt.plot(trials, classical_entropies, color='#e74c3c', alpha=0.7,
             marker='o', label="Classical PRNG")
    plt.plot(trials, quantum_entropies, color='#2ecc71', alpha=0.7,
             marker='o', label="Quantum RNG")
    plt.axhline(y=1.0, color='black', linestyle='--', linewidth=1, label="Max Entropy")
    plt.xlabel("Trial")
    plt.ylabel("Shannon Entropy (bits per bit)")
    plt.title(f"Entropy per Trial: Classical PRNG vs Quantum RNG ({RUNS} Trials)")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig("qrng_entropy_per_trial.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    print("Running QRNG Entropy Analysis...\n")
    np.random.seed(None)

    print("Generating bits...")
    c_bits = classical_prng(NUM_BITS)
    q_bits = quantum_rng(NUM_BITS)

    classical_result = analyze_source("Classical PRNG", c_bits)
    quantum_result = analyze_source("Quantum RNG", q_bits)

    print(f"{'Metric':<25} {'Classical PRNG':<20} Quantum RNG")
    print("-" * 65)
    print(f"{'Entropy (bits/bit)':<25} {classical_result['entropy_bits']:<20.8f} {quantum_result['entropy_bits']:.8f}")
    print(f"{'Entropy Efficiency':<25} {classical_result['entropy_efficiency']:<20.6f} {quantum_result['entropy_efficiency']:.6f}")
    print(f"{'Chi-Square p-value':<25} {classical_result['chi_square_p']:<20.6f} {quantum_result['chi_square_p']:.6f}")
    print(f"{'Runs Deviation (%)':<25} {classical_result['runs_deviation']:<20.6f} {quantum_result['runs_deviation']:.6f}")
    print(f"{'Serial Correlation':<25} {classical_result['serial_correlation']:<20.8f} {quantum_result['serial_correlation']:.8f}")
    print(f"{'Passes Uniformity':<25} {classical_result['passes_uniformity']:<20} {quantum_result['passes_uniformity']}")
    print(f"{'Passes Correlation':<25} {classical_result['passes_correlation']:<20} {quantum_result['passes_correlation']}")

    log_results(classical_result, quantum_result)

    print("\nRunning multiple trials...")
    c_ents, q_ents, c_corrs, q_corrs = run_multiple_trials(RUNS)
    print(f"Classical entropy mean: {np.mean(c_ents):.8f} ± {np.std(c_ents):.2e}")
    print(f"Quantum entropy mean  : {np.mean(q_ents):.8f} ± {np.std(q_ents):.2e}")

    plot_entropy_comparison(classical_result, quantum_result)
    plot_entropy_distribution(c_ents, q_ents)
    plot_correlation_comparison(classical_result, quantum_result)
    plot_trial_entropies(c_ents, q_ents)

    print("\nAnalysis complete. CSV and plots saved.")