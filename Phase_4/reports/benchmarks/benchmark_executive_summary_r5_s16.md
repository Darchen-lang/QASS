# QASS Benchmark Executive Summary (r5_s16)

## Protocol
- Candidate architecture: `baseline_full`
- Reference architectures: `no_layer2_fixed_combo`, `no_layer4_no_ratchet`, `single_source_kyber`
- Repeats: 5
- Sessions per repeat: 16
- Performance tolerance: 20%
- Gate rule: On-par requires all three gates to pass (`security_ok`, `performance_ok`, `composite_ok`).

## Final Comparison Outcomes
| Candidate | Reference | Security Gate | Performance Gate | Composite Gate | Runtime Ratio | On-Par |
|---|---|---:|---:|---:|---:|---:|
| baseline_full | no_layer2_fixed_combo | True | True | True | 1.0308 | True |
| baseline_full | no_layer4_no_ratchet | False | False | False | 1.6514 | False |
| baseline_full | single_source_kyber | False | False | True | 1.6807 | False |

## Interpretation
- QASS baseline is on-par against the fixed-combination baseline.
- QASS baseline is not on-par against the no-ratchet and single-source baselines under this protocol.
- Primary blocker is runtime overhead versus lighter baselines (runtime ratios 1.65x to 1.68x), plus security-gate failures on those two references.

## Presentable Claim You Can Use
Under a standardized protocol (5 repeats x 16 sessions, 20% performance tolerance), QASS full architecture demonstrates successful parity against a fixed-combination baseline while showing measurable overhead against lightweight baselines. This supports the position that QASS provides stronger agility-oriented behavior but still requires performance optimization before broad parity across lean reference architectures.

## Evidence Files
- `Phase_4/architecture_benchmark_report_r5_s16_vs_no_layer2_fixed_combo.md`
- `Phase_4/architecture_benchmark_report_r5_s16_vs_no_layer4_no_ratchet.md`
- `Phase_4/architecture_benchmark_report_r5_s16_vs_single_source_kyber.md`
- `Phase_4/benchmark_leaderboard_r5_s16.csv`
