# QASS Architecture Benchmark Report

- Repeats per architecture: 10
- Sessions per repeat: 32
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.234375 (95% CI [0.217915, 0.250835])
- mean_abs_key_corr: 0.051697 (95% CI [0.045141, 0.058252])
- mean_hamming_rate: 0.500378 (95% CI [0.496451, 0.504305])
- mean_total_ms: 2521.221839 (95% CI [2503.400447, 2539.043232])
- unique_combo_count: 7.000000 (95% CI [7.000000, 7.000000])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.049615 (95% CI [0.046755, 0.052475])
- mean_hamming_rate: 0.501285 (95% CI [0.497628, 0.504943])
- mean_total_ms: 2419.038740 (95% CI [2398.290483, 2439.786998])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.246875 (95% CI [0.225560, 0.268190])
- mean_abs_key_corr: 0.049535 (95% CI [0.045303, 0.053767])
- mean_hamming_rate: 0.503138 (95% CI [0.499549, 0.506726])
- mean_total_ms: 1487.559414 (95% CI [1481.892613, 1493.226214])
- unique_combo_count: 6.800000 (95% CI [6.538671, 7.061329])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.043772 (95% CI [0.039969, 0.047574])
- mean_hamming_rate: 0.499005 (95% CI [0.496568, 0.501441])
- mean_total_ms: 1405.868939 (95% CI [1403.345369, 1408.392510])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.449811, performance=0.000000, agility=1.000000, composite=0.474905
- no_layer2_fixed_combo: security=0.301901, performance=0.091615, agility=0.000000, composite=0.173854
- no_layer4_no_ratchet: security=0.499713, performance=0.926758, agility=0.966667, composite=0.723213
- single_source_kyber: security=0.449502, performance=1.000000, agility=0.000000, composite=0.474751

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer4_no_ratchet
- Security gate: False
- Performance gate: False (runtime ratio=1.694871)
- Composite gate: False (composite gap=-0.248307)
- On par verdict: False
