> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `47f1a8a0ee03813936d30b78af2e0e88d60cd5d8586b88c1b5edb5a4471d693f`.

# Project Riemann — Prime-index renormalization of signed prime-counting error

**Date:** 2026-10-20. **Research classification:** `EXACT_GENERAL_COARSE_GRAINING_IDENTITY / COMPUTATIONAL_COVARIANCE_SIGNAL / NO_NEW_RH_FRONTIER_ADVANCE`.

This note follows the user's suggestion that iterated prime indexing, skipped numbers, and higher-order prime-valued gap patterns might require a new scale-dependent mathematical language. The note tests one potential proof-critical route: whether the actual signed *prime-counting error* has a special cancellation law under repeated prime-index block aggregation. No claim of a new branch of mathematics or an RH proof is made. Existing October 19–20 archives remain untouched.

## 1. Definitions and exact theorem

Let `p_n` be the `n`-th prime, `S_0(n)=n`, `S_k(n)=p_(S_(k-1)(n))`, and `E(x)=pi(x)-li(x)` for `x>1`. Define

`e_k(n)=E(S_k(n+1))-E(S_k(n))`.

**Exact theorem (unconditional).** For every `k>=1` and `n>=1`,

`e_(k+1)(n)=sum_(j=p_n)^(p_(n+1)-1) e_k(j)`.

**Proof:** As `S_(k+1)(n)=S_k(p_n)` and `S_(k+1)(n+1)=S_k(p_(n+1))`, summing the differences on the right telescopes to `E(S_k(p_(n+1)))-E(S_k(p_n))`, which is the left side. QED.

**Important scope:** This statement is **universal**, not specific to primes. For *any* strictly increasing map `f: N->N`, any `E` on its range, and `S_k=f^k`, the same proof gives the block identity with `p_n` replaced by `f(n)`. Thus merely verifying the recursion at every depth cannot distinguish primes from arbitrary nested sequences.

For `k>=2`, the integer count inside this error is `pi(S_k(n+1))-pi(S_k(n))=S_(k-1)(n+1)-S_(k-1)(n)`. For `k=1` it equals 1. These exact count identities allow direct evaluation of the errors from frozen prime-index sequences without independently computing `pi` at each endpoint.

## 2. The squared-error covariance identity

For a prime-index block `I_n={p_n,...,p_(n+1)-1}`, let `u_j=e_k(j)`. Then identically,

`e_(k+1)(n)^2 = sum_(j in I_n) u_j^2 + 2 sum_(i<j, i,j in I_n) u_i u_j`.

Consequently the ratio

`R_k(B)=[sum_(n in B) e_(k+1)(n)^2]/[sum_(n in B) sum_(j in I_n) e_k(j)^2]`

is below 1 exactly when the aggregate off-diagonal signed correlation across the chosen disjoint blocks is negative. The identity alone has **no sign**, and the ratio is not a thermodynamic contraction coefficient or pointwise bound.

## 3. Bounded numerical test

Reused unchanged `FROZEN_INPUT_NESTED_GAPS_1000.csv` from the previous October 20 audit. The bundled script validates all consecutive gaps and higher-level prime-index selections, then computes `E` differences using `scipy.special.expi(log x)` (corresponding to `li(x)` for `x>1`). It checks the exact recursion over 167 blocks whose corresponding lower-level indices lie between 2 and 996. Numerical equality is within `1.8e-15` in these tests; the mathematical proof does not depend on numerics.

| Transition | Ratio R_k over 167 blocks | Blocks with negative / positive off-diagonal contribution | Median local-shuffle ratio (window 100) |
|---|---:|---:|---:|
| 1 -> 2 | 0.713328544 | 113 / 53 | 0.940563 |
| 2 -> 3 | 0.476368820 | 125 / 41 | 0.939249 |
| 3 -> 4 | 0.428267085 | 124 / 42 | 0.932023 |

(The remaining block at each level has zero off-diagonal contribution.) The diagnostic randomized controls shuffle the 1,000 error values **only within consecutive index windows of 50, 100, or 200**, not across the entire sequence; 1,000 deterministic-seed surrogates were tested per window and level. At levels 2->3 and 3->4, all 1,000 window-100 controls had larger `R_k` than the genuine data. This is descriptive sensitivity evidence only. These surrogates are **not** a probability model for the primes and do not establish a significance theorem.

### Adversarial controls and falsifications

1. The proposed strong law `R_k(B)<1 for every nonempty consecutive block collection B` **fails for actual prime data**: at transition 1->2, blocks `n=121..140` give `R_1=1.035587...`. Several individual prime blocks have positive off-diagonal contributions at every tested depth.
2. The completely nonprime-specific oscillatory input `u_j=(-1)^j` has zero sum on every even-length block. Prime-index block lengths are even except the first. Its 167-block ratio is `1/995 ~= 0.001005`, **far stronger cancellation** than the actual prime-error data, despite containing no information about prime-counting discrepancies.
3. The constant input `u_j=1` has ratio `8029/995 ~= 8.06935`: the same block transform can amplify rather than cancel.

Thus an unconditional algebraic "renormalization contraction" **does not exist** for arbitrary nested structures, and small ratios alone do not reveal a uniquely prime-generated law. A new theorem about **prime-specific** covariance would need hypotheses and independent arithmetic content.

## 4. What would justify a new mathematical framework?

We can provisionally describe the combined viewpoint as **prime-index renormalization of arithmetic discrepancy**. This is only working terminology. The operator merges signed prime-counting errors into exactly the blocks determined by consecutive primes; the same operator merges positive numerical gaps, giving a rigorous way to compare expanding distances with cancellation.

To earn mathematical substance beyond established combinatorics and analytic number theory, it would have to produce a **new quantitative covariance/cancellation estimate**, uniform over unbounded index windows and genuinely derived from prime arithmetic, and then rigorously convert that estimate into an improved *pointwise* bound on `E(x)` or directly into exclusion of a hypothetical zeta zero. A finite average, even at many depths, cannot rule out an isolated exceptional height without a separate uniform interpolation mechanism. Merely assuming such a bound repackages the RH or a zero-free-region obligation.

There is a particularly strong literature precedent: Montgomery and Soundararajan (2004) study variance of prime counts in short intervals, and Goldston–Montgomery-type relations connect certain variance asymptotics to zeta-zero correlations. The current finite negative-covariance signal must not be claimed to originate a new field, theorem, or zero-exclusion result.

## 5. Literature placement

- Bayless, Klyve, Oliveira e Silva, *New Bounds and Computations on Prime-Indexed Primes*, INTEGERS 13 (2013): https://math.colgate.edu/~integers/n43/n43.pdf. Already treats higher prime-index iterates, gaps, reciprocal sums.
- Batchko (2014), *A prime fractal and global quasi-self-similar structure in the distribution of prime-indexed primes*: https://arxiv.org/abs/1405.2900. Describes strong empirical correlations under iterated prime indexing.
- Montgomery and Soundararajan (2004), *Primes in short intervals*: https://arxiv.org/abs/math/0409258. Arithmetic correlations and variance estimates already have a rigorous mathematical literature.

## 6. Verification and status

- `verify_prime_error_flow.py` + frozen copy of the input CSV + `results.json` + `VERIFICATION_LOG.txt` are bundled. The input CSV is copied, not modified in its original directory.
- Wolfram independent check of `e_(k+1)(n)=sum e_k(j)` returned **exactly 0** in all 15 tests for `k=1,2,3`, `n=1,...,5` using `Nest[Prime,...]`, `PrimePi`, and `LogIntegral`. (No novel proof is attributed to numerical checks.)
- Lean 4 was not on `PATH`; no Lean compilation is claimed. No Codex run was launched.
- `NO_NEW_RH_FRONTIER_ADVANCE`. RH open; full Haglund k=2/k=3 verification `UNVERIFIED`, moment gate `BLOCKED_NEW_MOMENT_ESTIMATE`, provenance `BLOCKED_UNWAIVED`.

**Decision:** Preserve this precise error-flow formalism and the falsified strong contraction claim. Do **not** launch further large statistics or declare a new subject before a falsification-resistant, prime-specific uniform covariance theorem with a demonstrable consequence for the genuine zeta function has been identified.
