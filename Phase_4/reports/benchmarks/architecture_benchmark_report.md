# QASS Architecture Benchmark Report

- Repeats per architecture: 1
- Sessions per repeat: 1
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.000000 (95% CI [0.000000, 0.000000])
- mean_hamming_rate: 0.000000 (95% CI [0.000000, 0.000000])
- mean_total_ms: 2641.274302 (95% CI [2641.274302, 2641.274302])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.000000 (95% CI [0.000000, 0.000000])
- mean_hamming_rate: 0.000000 (95% CI [0.000000, 0.000000])
- mean_total_ms: 2325.606447 (95% CI [2325.606447, 2325.606447])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.000000 (95% CI [0.000000, 0.000000])
- mean_hamming_rate: 0.000000 (95% CI [0.000000, 0.000000])
- mean_total_ms: 1458.055459 (95% CI [1458.055459, 1458.055459])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.000000 (95% CI [0.000000, 0.000000])
- mean_hamming_rate: 0.000000 (95% CI [0.000000, 0.000000])
- mean_total_ms: 1311.968300 (95% CI [1311.968300, 1311.968300])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.000000, performance=0.000000, agility=0.000000, composite=0.000000
- no_layer2_fixed_combo: security=0.000000, performance=0.237468, agility=0.000000, composite=0.059367
- no_layer4_no_ratchet: security=0.000000, performance=0.890103, agility=0.000000, composite=0.222526
- single_source_kyber: security=0.000000, performance=1.000000, agility=0.000000, composite=0.250000

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer2_fixed_combo
- Security gate: True
- Performance gate: True (runtime ratio=1.135736)
- Composite gate: False (composite gap=-0.059367)
- On par verdict: False
