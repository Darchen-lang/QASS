# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.237500 (95% CI [0.222497, 0.252503])
- mean_abs_key_corr: 0.051024 (95% CI [0.041949, 0.060098])
- mean_hamming_rate: 0.502974 (95% CI [0.499564, 0.506384])
- mean_total_ms: 2505.898178 (95% CI [2457.980879, 2553.815477])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.052242 (95% CI [0.046603, 0.057880])
- mean_hamming_rate: 0.495262 (95% CI [0.489506, 0.501018])
- mean_total_ms: 2642.055935 (95% CI [2607.343314, 2676.768556])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.268750 (95% CI [0.244250, 0.293250])
- mean_abs_key_corr: 0.048943 (95% CI [0.041699, 0.056187])
- mean_hamming_rate: 0.502621 (95% CI [0.497095, 0.508147])
- mean_total_ms: 1648.155361 (95% CI [1623.901582, 1672.409139])
- unique_combo_count: 6.600000 (95% CI [6.119909, 7.080091])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.051768 (95% CI [0.047430, 0.056107])
- mean_hamming_rate: 0.499874 (95% CI [0.494112, 0.505636])
- mean_total_ms: 1596.666974 (95% CI [1567.693345, 1625.640603])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.522359, performance=0.130246, agility=1.000000, composite=0.543741
- no_layer2_fixed_combo: security=0.247631, performance=0.000000, agility=0.000000, composite=0.123816
- no_layer4_no_ratchet: security=0.640493, performance=0.950747, agility=0.933333, composite=0.791267
- single_source_kyber: security=0.278634, performance=1.000000, agility=0.000000, composite=0.389317

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer2_fixed_combo
- Security gate: False
- Performance gate: True (runtime ratio=0.948465)
- Composite gate: True (composite gap=0.419925)
- On par verdict: False
