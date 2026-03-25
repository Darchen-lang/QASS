# QASS Architecture Benchmark Report

- Repeats per architecture: 10
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.234375 (95% CI [0.217915, 0.250835])
- mean_abs_key_corr: 0.053319 (95% CI [0.049360, 0.057277])
- mean_hamming_rate: 0.502092 (95% CI [0.498102, 0.506082])
- mean_total_ms: 2724.496464 (95% CI [2669.629937, 2779.362991])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.052065 (95% CI [0.048413, 0.055717])
- mean_hamming_rate: 0.501096 (95% CI [0.497133, 0.505059])
- mean_total_ms: 2515.077080 (95% CI [2496.202503, 2533.951657])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.246875 (95% CI [0.225560, 0.268190])
- mean_abs_key_corr: 0.046468 (95% CI [0.043218, 0.049718])
- mean_hamming_rate: 0.498765 (95% CI [0.495185, 0.502346])
- mean_total_ms: 1517.227997 (95% CI [1498.784916, 1535.671079])
- unique_combo_count: 6.800000 (95% CI [6.538671, 7.061329])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.047684 (95% CI [0.043434, 0.051934])
- mean_hamming_rate: 0.501739 (95% CI [0.497699, 0.505779])
- mean_total_ms: 1372.200871 (95% CI [1364.493283, 1379.908460])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.448954, performance=0.000000, agility=1.000000, composite=0.474477
- no_layer2_fixed_combo: security=0.286041, performance=0.154862, agility=0.000000, composite=0.181736
- no_layer4_no_ratchet: security=0.646117, performance=0.892755, agility=0.966667, composite=0.787914
- single_source_kyber: security=0.413631, performance=1.000000, agility=0.000000, composite=0.456816

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer2_fixed_combo
- Security gate: False
- Performance gate: True (runtime ratio=1.083266)
- Composite gate: True (composite gap=0.292741)
- On par verdict: False
