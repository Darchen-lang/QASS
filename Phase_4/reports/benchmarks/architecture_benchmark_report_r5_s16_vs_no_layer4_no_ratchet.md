# QASS Architecture Benchmark Report

- Repeats per architecture: 5
- Sessions per repeat: 16
- Base seed: 910000

## Aggregate Metrics (mean with 95% CI)

### baseline_full
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.287500 (95% CI [0.238501, 0.336499])
- mean_abs_key_corr: 0.058071 (95% CI [0.045044, 0.071098])
- mean_hamming_rate: 0.501510 (95% CI [0.495391, 0.507630])
- mean_total_ms: 2410.919880 (95% CI [2381.800790, 2440.038971])
- unique_combo_count: 6.800000 (95% CI [6.408007, 7.191993])

### no_layer2_fixed_combo
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.062398 (95% CI [0.047365, 0.077431])
- mean_hamming_rate: 0.495625 (95% CI [0.492604, 0.498646])
- mean_total_ms: 2323.505488 (95% CI [2286.363819, 2360.647158])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

### no_layer4_no_ratchet
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 0.300000 (95% CI [0.254166, 0.345834])
- mean_abs_key_corr: 0.042937 (95% CI [0.039083, 0.046791])
- mean_hamming_rate: 0.501458 (95% CI [0.497060, 0.505857])
- mean_total_ms: 1459.902614 (95% CI [1433.517154, 1486.288073])
- unique_combo_count: 6.000000 (95% CI [5.380205, 6.619795])

### single_source_kyber
- decrypt_success_rate: 1.000000 (95% CI [1.000000, 1.000000])
- predictability_rate: 1.000000 (95% CI [1.000000, 1.000000])
- mean_abs_key_corr: 0.054248 (95% CI [0.042638, 0.065857])
- mean_hamming_rate: 0.508333 (95% CI [0.500954, 0.515712])
- mean_total_ms: 1374.812072 (95% CI [1350.610997, 1399.013147])
- unique_combo_count: 1.000000 (95% CI [1.000000, 1.000000])

## Weighted Scores
- baseline_full: security=0.493712, performance=0.000000, agility=1.000000, composite=0.496856
- no_layer2_fixed_combo: security=0.247812, performance=0.084368, agility=0.000000, composite=0.144998
- no_layer4_no_ratchet: security=0.645762, performance=0.917875, agility=0.862069, composite=0.767867
- single_source_kyber: security=0.329592, performance=1.000000, agility=0.000000, composite=0.414796

## Parity Decision
- Candidate: baseline_full
- Reference: no_layer4_no_ratchet
- Security gate: False
- Performance gate: False (runtime ratio=1.651425)
- Composite gate: False (composite gap=-0.271011)
- On par verdict: False
