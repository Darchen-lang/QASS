# QASS Architecture Benchmark Report

- Repeats per architecture: 10
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.234375 (95% CI [0.217915, 0.250835])
- mean_abs_key_corr: 0.051062 (95% CI [0.046014, 0.056111])
- mean_hamming_rate: 0.499307 (95% CI [0.496676, 0.501938])
- mean_total_ms: 2551.356375 (95% CI [2461.096753, 2641.615998])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.051397 (95% CI [0.048120, 0.054675])
- mean_hamming_rate: 0.497669 (95% CI [0.494419, 0.500919])
- mean_total_ms: 2588.757223 (95% CI [2584.133122, 2593.381323])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.246875 (95% CI [0.225560, 0.268190])
- mean_abs_key_corr: 0.053452 (95% CI [0.048975, 0.057928])
- mean_hamming_rate: 0.502747 (95% CI [0.499687, 0.505806])
- mean_total_ms: 1600.635657 (95% CI [1594.308439, 1606.962875])
- unique_combo_count: 6.800000 (95% CI [6.538671, 7.061329])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.046968 (95% CI [0.044035, 0.049901])
- mean_hamming_rate: 0.499773 (95% CI [0.497656, 0.501891])
- mean_total_ms: 2152.439542 (95% CI [1834.491658, 2470.387425])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.523348, performance=0.037850, agility=1.000000, composite=0.521137
- no_layer2_fixed_combo: security=0.312205, performance=0.000000, agility=0.000000, composite=0.156103
- no_layer4_no_ratchet: security=0.445361, performance=1.000000, agility=0.966667, composite=0.714347
- single_source_kyber: security=0.449887, performance=0.441563, agility=0.000000, composite=0.335334

## Parity Decision
- Candidate: baseline_full
- Reference: single_source_kyber
- Security gate: False
- Performance gate: True (runtime ratio=1.185332)
- Composite gate: True (composite gap=0.185803)
- On par verdict: False
