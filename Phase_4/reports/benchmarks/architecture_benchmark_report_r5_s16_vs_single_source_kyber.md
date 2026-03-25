# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 16
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.287500 (95% CI [0.238501, 0.336499])
- mean_abs_key_corr: 0.052967 (95% CI [0.043664, 0.062270])
- mean_hamming_rate: 0.500104 (95% CI [0.494762, 0.505447])
- mean_total_ms: 2504.906026 (95% CI [2455.949630, 2553.862423])
- unique_combo_count: 6.800000 (95% CI [6.408007, 7.191993])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.050070 (95% CI [0.042715, 0.057426])
- mean_hamming_rate: 0.501615 (95% CI [0.492669, 0.510560])
- mean_total_ms: 2360.436696 (95% CI [2305.708643, 2415.164749])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.300000 (95% CI [0.254166, 0.345834])
- mean_abs_key_corr: 0.051268 (95% CI [0.040692, 0.061845])
- mean_hamming_rate: 0.508906 (95% CI [0.500693, 0.517120])
- mean_total_ms: 1542.133521 (95% CI [1497.507449, 1586.759593])
- unique_combo_count: 6.000000 (95% CI [5.380205, 6.619795])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.049366 (95% CI [0.037959, 0.060774])
- mean_hamming_rate: 0.499479 (95% CI [0.492550, 0.506408])
- mean_total_ms: 1490.437559 (95% CI [1429.423349, 1551.451770])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.449948, performance=0.000000, agility=1.000000, composite=0.474974
- no_layer2_fixed_combo: security=0.410075, performance=0.142409, agility=0.000000, composite=0.240640
- no_layer4_no_ratchet: security=0.536385, performance=0.949041, agility=0.862069, composite=0.720970
- single_source_kyber: security=0.449740, performance=1.000000, agility=0.000000, composite=0.474870

## Parity Decision
- Candidate: baseline_full
- Reference: single_source_kyber
- Security gate: False
- Performance gate: False (runtime ratio=1.680651)
- Composite gate: True (composite gap=0.000104)
- On par verdict: False
