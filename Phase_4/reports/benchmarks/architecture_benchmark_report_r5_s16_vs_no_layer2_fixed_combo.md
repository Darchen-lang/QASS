# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 16
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.287500 (95% CI [0.238501, 0.336499])
- mean_abs_key_corr: 0.051904 (95% CI [0.041806, 0.062003])
- mean_hamming_rate: 0.504687 (95% CI [0.499351, 0.510024])
- mean_total_ms: 2311.480562 (95% CI [2303.489783, 2319.471342])
- unique_combo_count: 6.800000 (95% CI [6.408007, 7.191993])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.056056 (95% CI [0.045382, 0.066730])
- mean_hamming_rate: 0.504896 (95% CI [0.501606, 0.508185])
- mean_total_ms: 2242.386589 (95% CI [2228.456582, 2256.316595])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.300000 (95% CI [0.254166, 0.345834])
- mean_abs_key_corr: 0.047199 (95% CI [0.041116, 0.053282])
- mean_hamming_rate: 0.495937 (95% CI [0.492496, 0.499379])
- mean_total_ms: 1487.525792 (95% CI [1412.831831, 1562.219754])
- unique_combo_count: 6.000000 (95% CI [5.380205, 6.619795])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.053687 (95% CI [0.044294, 0.063080])
- mean_hamming_rate: 0.499583 (95% CI [0.492521, 0.506646])
- mean_total_ms: 1383.635184 (95% CI [1356.317010, 1410.953358])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.541403, performance=0.000000, agility=1.000000, composite=0.520701
- no_layer2_fixed_combo: security=0.247552, performance=0.074467, agility=0.000000, composite=0.142393
- no_layer4_no_ratchet: security=0.644460, performance=0.888030, agility=0.862069, composite=0.759755
- single_source_kyber: security=0.303286, performance=1.000000, agility=0.000000, composite=0.401643

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer2_fixed_combo
- Security gate: True
- Performance gate: True (runtime ratio=1.030813)
- Composite gate: True (composite gap=0.378309)
- On par verdict: True
