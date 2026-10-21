# Case study: a correct finite gate with an unresolved analytic premise

The proposed strengthening replaced

$$r+2z<m,\qquad 2r+8z<3m$$

with

$$r+z<m,\qquad 2r+8z<3m.$$

The arithmetic character family, coefficient restrictions, masks and uniformity requirements had to remain unchanged. Proving the relaxed scalar inequalities alone would not establish the stronger moment theorem.

## What the audit did

1. Reconstructed the parameter formulas using exact rational arithmetic.
2. Checked 19 polynomial inequalities on 1,216 Bernstein boxes and 16 fixed comparisons.
3. Examined the source's masked Poisson initialization and canonical energy hypotheses.
4. Tested diagonal, overlap, sixth-power, coefficient-class and cancellation shortcuts.
5. Compiled ten focused Lean lemmas, including the exact obstruction identities.

For the formal centers, with overlap length G and remaining mark cap z₀,

$$F-M-Q-z_0=m-r-2z+2G.$$

At the actual gate point δ=x=1/2 and m=1,

$$r=\frac{467988598319}{670130653625},\qquad z=\frac{133631714876}{670130653625}.$$

The proposed first gap is positive, the second gap is 1/125, but

$$1-r-2z=-\frac{65121374446}{670130653625}<0.$$

Thus the new conditions do not imply the existing analytic initialization's conditions. **This is a proof-method obstruction, not a counterexample to the proposed arithmetic moment.**

## Why this is useful engineering evidence

A green finite verifier can coexist with an unproved theorem. The investigation identified precisely where the implication fails, retained the successful finite work, and stopped without relabeling a conditional endpoint as a result. Negative controls and an independent implementation strengthen the computational claim without hiding the analytic gap.

Read [the full audit](../../research/notes/final-feasibility-audit.md), [Lean source](../../lean/MarkedGate.lean), [exact checker](../../scripts/check_exact_gate.py), and [reference certificate](../../evidence/expected-exact-gate.json).

The public checker preserves the original mathematical formulas; its changes are an output-directory adjustment and a guard against disabled Python assertions. See [reproduction and trust boundaries](../reproduce.md).
