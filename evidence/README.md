# Verification evidence

- `expected-exact-gate.json`: the October 19 deterministic rational certificate, with elapsed time removed. It is checked against a fresh local run by the public verifier.
- `lean-build.log`: fresh local compilation of the exact released Lean source, including full printed declarations and axiom dependencies.
- `lean-verification.json`: source hash, pinned toolchain, declaration names, axiom inspection and compiler exit status. It does not claim formalized analytic premises.
- `public-checks.json`: fresh local output of the public Python verification command. GitHub Actions repeats the Python checks; it does not compile Lean.

The source hash and all result scopes are explicit. Build success, file integrity, finite diagnostics, formal algebra and unproved analytic research are different evidence classes.
