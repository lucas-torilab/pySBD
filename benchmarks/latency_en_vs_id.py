# -*- coding: utf-8 -*-
"""Latency benchmark: pySBD English vs Indonesian.

Measures accuracy (GRS score) and average segmentation latency for each
language over its own golden rules set, then prints a side-by-side table.

Usage:
    cd benchmarks && python latency_en_vs_id.py
"""

import sys
import time

sys.path.insert(0, '..')

import pysbd
from english_golden_rules import GOLDEN_EN_RULES
from indonesian_golden_rules import GOLDEN_ID_RULES

RUNS = 1000

en_seg = pysbd.Segmenter(language="en", clean=False, char_span=False)
id_seg = pysbd.Segmenter(language="id", clean=False, char_span=False)


def run_benchmark(segmenter, golden_rules, runs=RUNS):
    """Return (accuracy_pct, avg_ms_per_run, avg_us_per_sentence)."""
    total = len(golden_rules)

    score = 0
    for text, expected in golden_rules:
        if [s.strip() for s in segmenter.segment(text)] == expected:
            score += 1
    accuracy = score / total * 100.0

    t0 = time.perf_counter()
    for _ in range(runs):
        for text, _ in golden_rules:
            segmenter.segment(text)
    elapsed = time.perf_counter() - t0

    avg_ms_per_run = elapsed * 1_000 / runs
    avg_us_per_sentence = elapsed * 1_000_000 / (runs * total)

    return accuracy, avg_ms_per_run, avg_us_per_sentence


if __name__ == "__main__":
    configs = [
        ("English (en)", en_seg, GOLDEN_EN_RULES),
        ("Indonesian (id)", id_seg, GOLDEN_ID_RULES),
    ]

    results = []
    for label, seg, rules in configs:
        print(f"Benchmarking {label} ({len(rules)} rules, {RUNS} runs)…", flush=True)
        acc, ms_run, us_sent = run_benchmark(seg, rules)
        results.append((label, len(rules), acc, ms_run, us_sent))

    print()
    print(f"{'Language':<22} {'Rules':>6} {'Accuracy':>10} {'ms / run':>10} {'µs / sentence':>14}")
    print("-" * 66)
    for label, n, acc, ms_run, us_sent in results:
        print(f"{label:<22} {n:>6} {acc:>9.1f}% {ms_run:>10.2f} {us_sent:>13.2f}")

    if len(results) == 2:
        ratio = results[1][3] / results[0][3]
        print()
        print(f"Indonesian is {ratio:.2f}x the latency of English per run "
              f"({results[1][3]:.2f} ms vs {results[0][3]:.2f} ms)")
