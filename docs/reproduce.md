# Reproduce the public checks

## Standard-library Python

Requires Python 3.10 or newer. No package installation, historical data download, network access or paid API is needed.

```bash
python3 -I -B scripts/verify_portfolio.py
```

The command:

1. Validates 76 unique claim records, their source links, and public-note hashes.
2. Runs the Fraction-only gate checker: 19 continuum inequalities on 1,216 boxes, 16 scalar comparisons and negative controls.
3. Compares the complete deterministic certificate with the saved expected certificate. Timing is excluded from that comparison.
4. Runs a small nested-prime demonstration, including a deliberately incorrect missing-correction formula and a nonprime affine control.
5. Checks curated documentation links and rejects accidental local machine paths or recognizable credential material in released text.

Generated files go into the ignored `build/` directory. The checker refuses Python's `-O` mode, which would disable assertions. A nonzero exit is a failed check; it must not be relabeled as mathematical success.

The gate calculator is a public adaptation of the October 19 independent checker. Its formulas and Bernstein conversion are unchanged. Changes are limited to output routing and assertion-mode protection. The expected certificate is the authenticated saved result with its elapsed-time field omitted.

## Lean

The repository pins **Lean 4.35.0**, imports only `Std`, and requires no Mathlib packages. With that toolchain already installed:

```bash
lean lean/MarkedGate.lean
```

The source is byte-identical to the accepted historical source. Every theorem has `#print` and `#print axioms`. The included fresh local build log records ten declarations, no `sorryAx` and only the standard dependencies `propext`, `Classical.choice` and `Quot.sound`. These are not custom mathematical assumptions.

The formalized material includes canonical-center identities, an exact counterexample to an implication between admissibility conditions, the actual gate-point margins, positive-width normalization, finite valuation/parity implications and capacity monotonicity. It does not formalize the analytic moment, zeta, the full numerical corpus, or RH.

The GitHub workflow runs Python and file-integrity checks only. **It does not build Lean.** The Lean record is a separately labeled local compilation receipt; no CI formal-proof badge is implied.

## File integrity

```bash
sha256sum --check SHA256SUMS
```

This verifies this public snapshot, not the full historical research archive. Public notes include editorial notices and path redactions, so their hashes differ from the sealed originals. Both hashes are recorded in `research/source-index.csv`. Original private paths and unrelated third-party paper sources are not included.

The large k=2/k=3 evidence corpus and full C1–C4 regeneration workflow are outside this minimal public reproducer. Their unresolved reproduction and provenance limits remain in the status documentation.
