import argparse
import csv
import math
import os
import statistics
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

from scipy.stats import norm


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from Phase_4.qass_ablation import MODES, _run_mode


BASE_DIR = os.path.dirname(__file__)
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
BENCHMARKS_DIR = os.path.join(ARTIFACTS_DIR, "benchmarks")
REPORTS_DIR = os.path.join(BASE_DIR, "reports", "benchmarks")
for directory in (BENCHMARKS_DIR, REPORTS_DIR):
    os.makedirs(directory, exist_ok=True)

SUMMARY_CSV = os.path.join(BENCHMARKS_DIR, "architecture_benchmark_summary.csv")
SCORES_CSV = os.path.join(BENCHMARKS_DIR, "architecture_benchmark_scores.csv")
REPORT_MD = os.path.join(REPORTS_DIR, "architecture_benchmark_report.md")


KEY_METRICS = [
    "decrypt_success_rate",
    "predictability_rate",
    "mean_abs_key_corr",
    "mean_hamming_rate",
    "mean_total_ms",
    "unique_combo_count",
]


@dataclass
class MetricStats:
    mean: float
    stdev: float
    ci_low: float
    ci_high: float


def _normal_ci(mean: float, stdev: float, n: int, alpha: float = 0.05) -> Tuple[float, float]:
    if n <= 1:
        return mean, mean
    z = float(norm.ppf(1.0 - alpha / 2.0))
    margin = z * (stdev / math.sqrt(float(n)))
    return mean - margin, mean + margin


def _as_stats(values: Sequence[float]) -> MetricStats:
    if not values:
        return MetricStats(mean=0.0, stdev=0.0, ci_low=0.0, ci_high=0.0)
    mean = float(statistics.mean(values))
    stdev = float(statistics.stdev(values)) if len(values) > 1 else 0.0
    low, high = _normal_ci(mean, stdev, len(values))
    return MetricStats(mean=mean, stdev=stdev, ci_low=low, ci_high=high)


def _score_clamped(value: float, low: float, high: float, higher_is_better: bool) -> float:
    if high <= low:
        return 0.0
    scaled = (value - low) / (high - low)
    scaled = max(0.0, min(1.0, scaled))
    return scaled if higher_is_better else 1.0 - scaled


def _hamming_proximity_score(mean_hamming: float) -> float:
    # Ideal consecutive-key hamming distance is near 0.5.
    return max(0.0, 1.0 - (abs(mean_hamming - 0.5) / 0.5))


def run_repeated(mode: str, repeats: int, sessions: int, base_seed: int) -> Dict[str, MetricStats]:
    collected: Dict[str, List[float]] = {k: [] for k in KEY_METRICS}

    for i in range(repeats):
        seed = base_seed + i * 1000
        row = _run_mode(mode=mode, sessions=sessions, base_seed=seed)
        for key in KEY_METRICS:
            collected[key].append(float(row[key]))

    return {k: _as_stats(v) for k, v in collected.items()}


def compute_weighted_scores(all_stats: Dict[str, Dict[str, MetricStats]]) -> Dict[str, Dict[str, float]]:
    decrypt_values = [all_stats[m]["decrypt_success_rate"].mean for m in MODES]
    pred_values = [all_stats[m]["predictability_rate"].mean for m in MODES]
    corr_values = [all_stats[m]["mean_abs_key_corr"].mean for m in MODES]
    runtime_values = [all_stats[m]["mean_total_ms"].mean for m in MODES]
    combo_values = [all_stats[m]["unique_combo_count"].mean for m in MODES]

    d_min, d_max = min(decrypt_values), max(decrypt_values)
    p_min, p_max = min(pred_values), max(pred_values)
    c_min, c_max = min(corr_values), max(corr_values)
    t_min, t_max = min(runtime_values), max(runtime_values)
    u_min, u_max = min(combo_values), max(combo_values)

    scores: Dict[str, Dict[str, float]] = {}
    for mode in MODES:
        s = all_stats[mode]

        security_score = (
            0.35 * _score_clamped(s["decrypt_success_rate"].mean, d_min, d_max, higher_is_better=True)
            + 0.20 * _score_clamped(s["predictability_rate"].mean, p_min, p_max, higher_is_better=False)
            + 0.20 * _score_clamped(s["mean_abs_key_corr"].mean, c_min, c_max, higher_is_better=False)
            + 0.25 * _hamming_proximity_score(s["mean_hamming_rate"].mean)
        )
        performance_score = _score_clamped(s["mean_total_ms"].mean, t_min, t_max, higher_is_better=False)
        agility_score = _score_clamped(s["unique_combo_count"].mean, u_min, u_max, higher_is_better=True)

        composite = 0.50 * security_score + 0.25 * performance_score + 0.25 * agility_score

        scores[mode] = {
            "security_score": security_score,
            "performance_score": performance_score,
            "agility_score": agility_score,
            "composite_score": composite,
        }

    return scores


def check_on_par(
    all_stats: Dict[str, Dict[str, MetricStats]],
    scores: Dict[str, Dict[str, float]],
    candidate: str,
    reference: str,
    perf_tolerance: float,
) -> Dict[str, object]:
    cand = all_stats[candidate]
    ref = all_stats[reference]

    security_ok = (
        cand["decrypt_success_rate"].ci_low >= ref["decrypt_success_rate"].ci_low
        and cand["predictability_rate"].ci_high <= ref["predictability_rate"].ci_high
        and cand["mean_abs_key_corr"].ci_high <= ref["mean_abs_key_corr"].ci_high
    )

    # Candidate runtime must be within perf_tolerance (e.g., 0.20 => up to 20% slower).
    runtime_ratio = cand["mean_total_ms"].mean / max(ref["mean_total_ms"].mean, 1e-12)
    performance_ok = runtime_ratio <= (1.0 + perf_tolerance)

    composite_gap = scores[candidate]["composite_score"] - scores[reference]["composite_score"]
    composite_ok = composite_gap >= -0.05

    return {
        "candidate": candidate,
        "reference": reference,
        "security_ok": security_ok,
        "performance_ok": performance_ok,
        "composite_ok": composite_ok,
        "runtime_ratio": runtime_ratio,
        "composite_gap": composite_gap,
        "on_par": security_ok and performance_ok and composite_ok,
    }


def write_summary(all_stats: Dict[str, Dict[str, MetricStats]]) -> None:
    with open(SUMMARY_CSV, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mode", "metric", "mean", "stdev", "ci_low", "ci_high"])
        for mode in MODES:
            for metric in KEY_METRICS:
                m = all_stats[mode][metric]
                writer.writerow([mode, metric, m.mean, m.stdev, m.ci_low, m.ci_high])


def write_scores(scores: Dict[str, Dict[str, float]], parity: Dict[str, object]) -> None:
    with open(SCORES_CSV, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mode", "security_score", "performance_score", "agility_score", "composite_score"])
        for mode in MODES:
            s = scores[mode]
            writer.writerow([
                mode,
                s["security_score"],
                s["performance_score"],
                s["agility_score"],
                s["composite_score"],
            ])
        writer.writerow([])
        writer.writerow(["parity_field", "value"])
        writer.writerow(["candidate", parity["candidate"]])
        writer.writerow(["reference", parity["reference"]])
        writer.writerow(["security_ok", parity["security_ok"]])
        writer.writerow(["performance_ok", parity["performance_ok"]])
        writer.writerow(["composite_ok", parity["composite_ok"]])
        writer.writerow(["runtime_ratio", parity["runtime_ratio"]])
        writer.writerow(["composite_gap", parity["composite_gap"]])
        writer.writerow(["on_par", parity["on_par"]])


def write_report(
    repeats: int,
    sessions: int,
    base_seed: int,
    all_stats: Dict[str, Dict[str, MetricStats]],
    scores: Dict[str, Dict[str, float]],
    parity: Dict[str, object],
) -> None:
    lines: List[str] = [
        "# QASS Architecture Benchmark Report",
        "",
        f"- Repeats per architecture: {repeats}",
        f"- Sessions per repeat: {sessions}",
        f"- Base seed: {base_seed}",
        "",
        "## Aggregate Metrics (mean with 95% CI)",
    ]

    for mode in MODES:
        lines.extend(["", f"### {mode}"])
        for metric in KEY_METRICS:
            m = all_stats[mode][metric]
            lines.append(
                f"- {metric}: {m.mean:.6f} (95% CI [{m.ci_low:.6f}, {m.ci_high:.6f}])"
            )

    lines.extend([
        "",
        "## Weighted Scores",
    ])
    for mode in MODES:
        s = scores[mode]
        lines.extend([
            f"- {mode}: security={s['security_score']:.6f}, performance={s['performance_score']:.6f}, agility={s['agility_score']:.6f}, composite={s['composite_score']:.6f}",
        ])

    lines.extend([
        "",
        "## Parity Decision",
        f"- Candidate: {parity['candidate']}",
        f"- Reference: {parity['reference']}",
        f"- Security gate: {parity['security_ok']}",
        f"- Performance gate: {parity['performance_ok']} (runtime ratio={parity['runtime_ratio']:.6f})",
        f"- Composite gate: {parity['composite_ok']} (composite gap={parity['composite_gap']:.6f})",
        f"- On par verdict: {parity['on_par']}",
    ])

    with open(REPORT_MD, mode="w", newline="") as f:
        f.write("\n".join(lines) + "\n")


def run(
    repeats: int,
    sessions: int,
    base_seed: int,
    candidate: str,
    reference: str,
    perf_tolerance: float,
) -> Dict[str, object]:
    if candidate not in MODES:
        raise ValueError(f"candidate must be one of {MODES}")
    if reference not in MODES:
        raise ValueError(f"reference must be one of {MODES}")
    if repeats <= 0:
        raise ValueError("repeats must be > 0")
    if sessions <= 0:
        raise ValueError("sessions must be > 0")
    if perf_tolerance < 0.0:
        raise ValueError("perf_tolerance must be >= 0")

    all_stats: Dict[str, Dict[str, MetricStats]] = {}
    for idx, mode in enumerate(MODES):
        mode_seed = base_seed + idx * 100000
        all_stats[mode] = run_repeated(mode=mode, repeats=repeats, sessions=sessions, base_seed=mode_seed)

    scores = compute_weighted_scores(all_stats)
    parity = check_on_par(
        all_stats=all_stats,
        scores=scores,
        candidate=candidate,
        reference=reference,
        perf_tolerance=perf_tolerance,
    )

    write_summary(all_stats)
    write_scores(scores, parity)
    write_report(repeats, sessions, base_seed, all_stats, scores, parity)

    return {
        "all_stats": all_stats,
        "scores": scores,
        "parity": parity,
        "summary_csv": SUMMARY_CSV,
        "scores_csv": SCORES_CSV,
        "report_md": REPORT_MD,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--sessions", type=int, default=32)
    parser.add_argument("--base-seed", type=int, default=910000)
    parser.add_argument("--candidate", type=str, default="baseline_full")
    parser.add_argument("--reference", type=str, default="no_layer4_no_ratchet")
    parser.add_argument("--perf-tolerance", type=float, default=0.20)
    args = parser.parse_args()

    start = time.perf_counter()
    out = run(
        repeats=args.repeats,
        sessions=args.sessions,
        base_seed=args.base_seed,
        candidate=args.candidate,
        reference=args.reference,
        perf_tolerance=args.perf_tolerance,
    )
    elapsed = (time.perf_counter() - start) * 1000.0

    parity = out["parity"]
    for label in ["candidate", "reference", "security_ok", "performance_ok", "composite_ok", "on_par"]:
        print(label, parity[label])
    print("elapsed_ms", elapsed)
    print("summary_csv", out["summary_csv"])
    print("scores_csv", out["scores_csv"])
    print("report_md", out["report_md"])


if __name__ == "__main__":
    main()