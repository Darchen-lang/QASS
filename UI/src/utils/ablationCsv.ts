import type { AblationDatum } from '../types/ablation';

export function parseAblationCSV(csv: string): AblationDatum[] {
  const lines = csv.trim().split(/\r?\n/);
  const header = lines[0].split(',').map((h) => h.trim());
  return lines.slice(1).map((line) => {
    const values = line.split(',').map((v) => v.trim());
    const obj: Record<string, unknown> = {};
    header.forEach((h, i) => {
      obj[h] = isNaN(Number(values[i])) ? values[i] : Number(values[i]);
    });
    return obj as AblationDatum;
  });
}
