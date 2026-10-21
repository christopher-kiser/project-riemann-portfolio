> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `c7a0c6801e7dae172c78bd60f768e2229a9b6b20be7ef6215f6d19eeb86a5036`.

# Lean verification record

**10 actual theorem declarations compiled successfully, exit code 0**, with the existing pinned Lean 4.35.0 toolchain. No packages were installed, and the external quasi-RH formal proof was not downloaded or rebuilt.

Root: `LOCAL_ARCHIVE/project-riemann-marked-inverse-audit-20261019T185149Z`.

- Accepted source: `lean/MarkedGate.lean`.
- SHA-256: `2499f8f6dd0c2aea0951b2c786e3021b0099e97bd4e4352227c06822f6fc2e3f`.
- Snapshot of the compiled source: `verification/lean_20261019T185608229212Z/MarkedGate.lean`.
- Full compiler output, printed declarations and axioms: `verification/lean_20261019T185608229212Z/build.log`.
- Machine-readable receipt: `verification/lean_20261019T185608229212Z/receipt.json`.
- Invocation wrapper: `verification/run_lean.py`, with a 60-second timeout.

Actual invocation, with working directory `lean/`:

```bash
ELAN_TOOLCHAIN=leanprover/lean4:v4.35.0 \
LOCAL_ARCHIVE/lake env lean \
LOCAL_ARCHIVE/MarkedGate.lean
```

Only `Std` is imported. The field lemmas are universally quantified over an ordered field using explicit `Field`, `LE`, `LT`, `LawfulOrderLT`, `IsLinearOrder` and `OrderedRing` instances. The arithmetic instances are not supplied by a hypothesis asserting the desired moment. The two finite valuation/parity lemmas use `Nat` and `Int`.

| Declaration in namespace `MarkedGate` | Exact scope inspected in compiler output |
|---|---|
| `initial_margin_identities` | The three displayed canonical-center polynomial identities, for all `m,r,z,G,P`; no analytic hypothesis |
| `old_implies_new` | `z>=0` and `r+2z<m` imply `r+z<m`; no converse |
| `admissibility_counterexample` | Exact rational `r=4/5,z=3/20,m=1` satisfies both proposed conditions but violates the original first margin; not an arithmetic counterexample |
| `gate_point_margin` | Exact positive proposed gaps and negative old gap for the actual independently reconstructed gate point |
| `clipping_does_not_repair` | Explicit bounds on a negative gap, clipping and nonnegative row enlargement imply a negative adjusted margin |
| `positive_width_normalization` | Both proposed strict inequalities are equivalent to their normalized forms when `m>0` |
| `no_sixth_power_alias` | Natural valuations at most two and equal modulo six are equal; ideal interpretation is separate |
| `same_mobius_sign` | `a+K=total=b+K` implies equal integer powers of `-1`; arithmetic factor-count interpretation is separate |
| `inverse_capacity_monotone` | With `r<=s`, `0<=2x<=1`, `δ>=0` and `zr-zs<=s-r`, the specified inverse exponent does not increase |
| `endpoint_and_license` | Rational endpoint identity and strict scalar licensing comparison only |

Every declaration was followed by both `#print` and `#print axioms`. All ten expected declarations appear in the output. Dependencies are only standard Lean foundations: `propext`, `Quot.sound`, and, for the ordered-field lemmas, `Classical.choice`. No custom axiom, `sorryAx`, `sorry`, `admit`, `unsafe` or `native_decide` is present. The two Nat/Int lemmas do not use `Classical.choice`.

There is one nonfatal linter warning: the `hgap` assumption in `clipping_does_not_repair` is redundant in the generated proof. Its displayed statement retains the assumption; the stronger consequence follows from the clipping inequalities. No warning was suppressed and no failed build is hidden.

The 19 Bernstein continuum checks are separate exact-rational computational certificates. **Neither the strengthened arithmetic moment, the canonical analytic theorem, Poisson summation, the detector, nor an improved zeta zero-free theorem was formalized here.** The compiled declarations do not imply any of them without their additional analytic premises.
