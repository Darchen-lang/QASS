# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.237500 (95% CI [0.222497, 0.252503])
- mean_abs_key_corr: 0.053131 (95% CI [0.047376, 0.058886])
- mean_hamming_rate: 0.501815 (95% CI [0.499138, 0.504491])
- mean_total_ms: 2346.061984 (95% CI [2320.007794, 2372.116173])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.054486 (95% CI [0.050163, 0.058809])
- mean_hamming_rate: 0.501058 (95% CI [0.495831, 0.506286])
- mean_total_ms: 2405.427230 (95% CI [2359.467372, 2451.387087])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.268750 (95% CI [0.244250, 0.293250])
- mean_abs_key_corr: 0.053919 (95% CI [0.047384, 0.060454])
- mean_hamming_rate: 0.501714 (95% CI [0.498023, 0.505404])
- mean_total_ms: 1480.152322 (95% CI [1458.194458, 1502.110185])
- unique_combo_count: 6.600000 (95% CI [6.119909, 7.080091])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.052304 (95% CI [0.046839, 0.057769])
- mean_hamming_rate: 0.502268 (95% CI [0.497479, 0.507057])
- mean_total_ms: 1404.080696 (95% CI [1389.477929, 1418.683462])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.573316, performance=0.059285, agility=1.000000, composite=0.551479
- no_layer2_fixed_combo: security=0.249471, performance=0.000000, agility=0.000000, composite=0.124735
- no_layer4_no_ratchet: security=0.492937, performance=0.924031, agility=0.933333, composite=0.710810
- single_source_kyber: security=0.448866, performance=1.000000, agility=0.000000, composite=0.474433

## Parity Decision
- Candidate: baseline_full
- Reference: single_source_kyber
- Security gate: False
- Performance gate: False (runtime ratio=1.670888)
- Composite gate: True (composite gap=0.077047)
- On par verdict: False
