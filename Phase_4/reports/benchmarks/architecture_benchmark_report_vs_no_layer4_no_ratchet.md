# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.237500 (95% CI [0.222497, 0.252503])
- mean_abs_key_corr: 0.055147 (95% CI [0.046740, 0.063555])
- mean_hamming_rate: 0.499572 (95% CI [0.496841, 0.502302])
- mean_total_ms: 2346.930245 (95% CI [2274.863243, 2418.997246])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.047699 (95% CI [0.043770, 0.051627])
- mean_hamming_rate: 0.496623 (95% CI [0.490044, 0.503202])
- mean_total_ms: 2207.669016 (95% CI [2186.748449, 2228.589584])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.268750 (95% CI [0.244250, 0.293250])
- mean_abs_key_corr: 0.048491 (95% CI [0.042795, 0.054188])
- mean_hamming_rate: 0.498513 (95% CI [0.494421, 0.502605])
- mean_total_ms: 1423.168276 (95% CI [1378.594004, 1467.742547])
- unique_combo_count: 6.600000 (95% CI [6.119909, 7.080091])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.046678 (95% CI [0.036003, 0.057353])
- mean_hamming_rate: 0.499068 (95% CI [0.494668, 0.503467])
- mean_total_ms: 1331.513642 (95% CI [1279.761920, 1383.265363])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.449786, performance=0.000000, agility=1.000000, composite=0.474893
- no_layer2_fixed_combo: security=0.424215, performance=0.137147, agility=0.000000, composite=0.246394
- no_layer4_no_ratchet: security=0.598240, performance=0.909737, agility=0.933333, composite=0.759888
- single_source_kyber: security=0.449534, performance=1.000000, agility=0.000000, composite=0.474767

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer4_no_ratchet
- Security gate: False
- Performance gate: False (runtime ratio=1.649088)
- Composite gate: False (composite gap=-0.284995)
- On par verdict: False
