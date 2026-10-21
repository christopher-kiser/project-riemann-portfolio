> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `e7a20083d251804bb2d821ef203933670eebc070dd1841b888efd1c4f50bead1`.

# Claim and dependency ledger

Overall: **BLOCKED/UNVERIFIED / BLOCKED_NEW_MOMENT_ESTIMATE**. Historical status: **BLOCKED_UNWAIVED**. These classifications are independent of successful script execution.

| ID | Claim | Evidence and classification | Remaining boundary |
|---|---|---|---|
| F1 | Supplied 19 polynomial-box checks and 16 scalar checks | `verification/SUPPLIED_VERIFIER.json`, `.log`; unchanged input script, existing SymPy 1.14.0 | Computational exact-rational check, not the analytic moment |
| F2 | Independent gate reconstruction over the complete stated domain | `verification/independent_gate.py`, `INDEPENDENT_GATE.json`; Fraction-only Bernstein proof, 1,216 boxes, positive denominators, two negative controls | Written Bernstein basis justification; not a Lean formalization of the checker |
| F3 | Initialization identities, normalized inequalities, gate-point deficit | `lean/MarkedGate.lean`; compiled statements and axioms in `verification/lean_20261019T185608229212Z/` | No Poisson or arithmetic moment hypothesis is inserted into these algebraic theorems |
| F4 | Capacity monotonicity, valuation and parity implications | Same Lean source; explicit ordered-field/Nat/Int assumptions | Capacity formula, ideal-factorization interpretation and arithmetic estimates are written arguments |
| W1 | Elementary diagonal bound and absence of distinct pure sixth-power product aliases | Written argument in final audit; squarefreeness, fixed slot count, ideal divisor bound and Eisenstein lattice counting | No control of the remaining off-diagonal correlation |
| W2 | Primitive masked Poisson identity and normalized Gauss magnitude | Independently reconstructed inclusion–exclusion, finite Fourier change of variables, primitivity and Parseval; source lines 9722–9780 | Classical lattice Poisson and ideal/ray conventions retained as analytic inputs; not formalized here |
| P1 | Existing marked and canonical moment estimates | Published source statements and scoped proof inspection | External analytic inputs, not newly fully proved or locally Lean-verified |
| P2 | Xu–Sang detector, plain moment, numerator amplification and endpoint framework | v2 §§2,4–8 reviewed; physical coefficients and family scope retained | Their global analytic inputs, appendices and reported family zero-free premise were not independently rebuilt |
| U1 | New first condition `r+z<m` with unchanged second condition | **UNVERIFIED**; actual gate point violates the old canonical margin | Missing structured moment/correlation estimate with fixed positive gaps and full uniformity |
| U2 | Endpoint `Re(s)>328/375` | Algebraic output of a conditional gate, **NOT ESTABLISHED** | U1 throughout detector witness ranges, plus P1/P2 at their full scope |
| U3 | Candidate's independent Wolfram claim | **REPORTED_NOT_REPLAYED** | No accompanying Wolfram receipt; unnecessary for F2 |

## Source authentication and exact inspected locations

All paths below are relative to `LOCAL_ARCHIVE/project-riemann-marked-inverse-audit-20261019T185149Z`.

Original paper: [pinned GitHub source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), local `sources/openai_paper.tex`.

- Commit: `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
- Git blob SHA-1: `268c4e3206d460c617d3d2129742a72b831b3def`, matching the candidate's identifier.
- SHA-256: `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
- Lines 7250–7390: zero extensions, product marks, completion and fixed arithmetic support.
- Lines 7747–7805: reflected energy and local/sector structure.
- Lines 9209–9373: original coefficient family, marked lemma, canonical family and uniformity.
- Lines 9722–9780: masked primitive Poisson.
- Lines 9860–9930 and 11060–11128: terminal/recursive admissibility and shorter rows.
- Lines 11600–11775 and 11900–11975: overlap and initial formal centers.
- Lines 12120–12265: fibre count, signed-to-positive Cauchy, puncture and initial margins.

Xu–Sang: [arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2), local `sources/XuSang.html`, extracted `sources/XuSang.txt`.

- HTML SHA-256: `74ace7acb59fe416c7891da3b29b0a0ea1c8601304aa9274d40b4f662c2afbc8`.
- Text lines 310–525 and 706–1383: §2 and §§4–8, including coefficient class, uniformity, variable witnesses, numerator licensing and endpoint closure.
- Retrieval URLs, times, sizes and SHA-256 values: `sources/RETRIEVAL.json`; Git metadata: `sources/PIN.json`.

## Analytic contract that may not be weakened

| Component | Retained requirement / audit consequence |
|---|---|
| Arithmetic family | Actual Eisenstein ideals and element rows; fixed ray-character data outside the moving conductor. Physical sixth-power-free row restriction is kept where a later source theorem requires it. |
| Coefficients | Squarefree Möbius inverse coefficients; fixed finite disjoint prime slots with coefficients independent of the averaged row/label. Physical slots have the prescribed finite character combinations. A general column-vector bound cannot be substituted. |
| Zeros and masks | Symbols remain zero on nonunits, including residue exponents congruent to zero. Primitive induction retains removed Euler support as a coprimality mask. |
| Conductors and phases | Overlap primes, active/inactive marked factors and finite ray reciprocity phases remain in the corresponding branch. Moving primes are not absorbed into the fixed ray modulus. |
| Canonical puncture | `q(rho) <= Z^(F-M-z0-c*)`, independently of current row/label. This is the failed premise; the second premise is `3M+6z0+c* <= 4F`. |
| Quantifiers | Bounded nonnegative length ranges, fixed strictly positive margins, fixed slot count, uniform prime supports and allowed coefficients; every required subcollection and common sign. Normalizing row width requires `m>0`. |
| Analytic uniformity | Finitely many controlled smooth seminorms and a fixed polynomial height cost after separation; the original order of choosing losses, mesh, slot count and height cutoffs. |
| Variable witnesses | A proof only at the selected crossing point is insufficient. Positive-mark capacities above it and the unmarked transition must be covered uniformly. |
| Family licensing | The scalar comparison against `0.8748867` does not prove the reported bound for the complete physical character family. It remains a cited analytic premise. |

## Reproduction without changing the sealed workspace

Run these commands from the workspace root. The first two print to stdout and do not create historical evidence or bytecode:

```bash
sha256sum -c SHA256SUMS
LOCAL_ARCHIVE/python -I -B inputs/check_marked_inverse_single_length_gate.py
ELAN_TOOLCHAIN=leanprover/lean4:v4.35.0 LOCAL_ARCHIVE/lake env lean lean/MarkedGate.lean
```

The independent checker writes its receipt alongside its own source. To replay it, put only that new checker into a fresh scratch workspace; do not run it over the sealed receipt:

```bash
scratch=$(mktemp -d /tmp/riemann-marked-gate-replay.XXXXXXXX)
mkdir "$scratch/verification"
cp verification/independent_gate.py "$scratch/verification/independent_gate.py"
/usr/bin/python3 -I -B "$scratch/verification/independent_gate.py"
```

The regenerated JSON's deterministic certificate fields should match the saved receipt; elapsed time need not match. No external package installation or numerical controller is required. Do not interpret rerunning these commands as permission for a new research campaign.
