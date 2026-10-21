> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `c57780aeea9361e0e91bf359a4a916f6f36b845e376afa9ec1ef4556e5e9f51f`.

# Project Riemann — Nested Prime Patterns, Gap-of-Gap Primality and the Residue-Flow Test

**Date:** 2026-10-20  
**Verdict:** EXACT MODULAR INVARIANT / FINITE PRIME-FLAG TEST / NO NEW RH FRONTIER ADVANCE  
**Prior evidence:** untouched. This audit is separate from the October 19 Project Riemann handoff and all intervening audits.

## Goal and scope

Investigate the user's original prime-index/dead-end construction from independent directions: (i) repeated prime-index filtering, (ii) skipped-number counts, (iii) primality of these counts, (iv) the positions of prime-valued skipped counts, (v) skipped counts between those positions, (vi) modular residue dynamics, and (vii) cross-level correlation controls. Avoid inferring a zeta-zero result from finite self-similarity.

The prime-index hierarchy is known (e.g., Robert G. Batchko, *A prime fractal and global quasi-self-similar structure in the distribution of prime-indexed primes*, arXiv:1405.2900, 2014). This audit does **not** claim novelty for that structure or for the elementary modular observations below.

## Definitions

Write `p_n` for the `n`th prime. Set `S_1(n)=p_n`, `S_{k+1}(n)=S_k(p_n)` for `n,k>=1`. The **skipped-number count** is

`q_k(n) = S_k(n+1)-S_k(n)-1`.

Define `b_k(n)=1` if `q_k(n)` is prime, otherwise `0`. Let `J_k` be the increasing list of positive indices `n` where `b_k(n)=1`. Its skipped counts are `r_{k,2}(j)=J_k(j+1)-J_k(j)-1`. Apply the same prime-valued gap-position operation repeatedly to define `r_{k,3}`, `r_{k,4}`, etc. This makes a two-axis pattern map: prime-index depth `k`, versus prime-gap-of-hit depth `j`.

### Exact gap recursion

Telescoping yields

`q_{k+1}(n) = q_1(n) + sum_{j=p_n}^{p_{n+1}-1} q_k(j)`.

The extra `q_1(n)=p_{n+1}-p_n-1` is essential. The verifier checked all instances with `k=1,2,3` and `1<=n<100`.

## Exact residue-flow theorem (no RH assumption)

Let `a_1<a_2<...` be **any** sequence of prime numbers all at least 5. Define `q_n=a_{n+1}-a_n-1`.

Each `a_n` is congruent to 1 or 5 modulo 6. Let `e_n=+1` when `a_n ≡ 1 (mod 6)` and `e_n=-1` when `a_n ≡ 5 (mod 6)`. Then:

- `q_n ≡ 5 (mod 6)` precisely when the residue stays the same;
- `q_n ≡ 1 (mod 6)` precisely on the flip `5 -> 1`;
- `q_n ≡ 3 (mod 6)` precisely on the flip `1 -> 5`.

Writing `c_n=1_{q_n≡1 (mod 6)}-1_{q_n≡3 (mod 6)}`, we have the exact discrete-gradient identity

`c_n = (e_{n+1}-e_n)/2`.

Thus `sum_{n=1}^N c_n=(e_{N+1}-e_1)/2 ∈ {-1,0,1}`. In particular, if we delete all gaps with `q_n ≡ 5 (mod 6)`, the remaining residues `1,3,1,3,...` (or their reverse order) alternate **exactly**. This holds at every prime-index level after omitting the initial primes 2 and 3, and equally for any other subsequence of primes >3. This is a genuine identity, not probabilistic evidence for RH.

Moreover `q_n ≡ 3 (mod 6)` can be prime only when `q_n=3`. For prime-index levels `k>=2`, there are no skipped counts equal to 3: `q_2(1)=1`, while for `n>=2` a block of at least two ordinary prime gaps starting at 5 cannot total 4 (there is no triplet of primes >3 of the form `p,p+2,p+4`); hence `q_2(n)>=5`. The gap recurrence propagates this property to `k>=3`. So *every* skipped count congruent to 3 modulo 6 at levels `k>=2` is automatically composite.

### Modulo-30 refinement

For primes >5, allowed endpoint residues are `[1,7,11,13,17,19,23,29]` modulo 30. If the skipped count is prime and exceeds 5, its residue `r'-r-1` modulo 30 must be coprime to 30. Exactly **39 of the 64** possible *oriented residue transitions* meet this necessary condition. This is a finite wheel-sieve constraint, not a statement that actual transitions are uniformly distributed or that the remaining gaps are prime.

## Finite exact computations

The script uses an integer prime sieve through 30,000,000 (1,857,859 primes). It builds four exact nested levels, computes their first 1,000 skipped counts and tests primality by direct table lookup.

| Prime-index level | Prime-valued gaps out of 1,000 | `q ≡1 mod6` | `q ≡3 mod6` | `q ≡5 mod6` |
|---|---:|---:|---:|---:|
| 1 | 679 | 314 | 312 | 373 |
| 2 | 550 | 250 | 248 | 502 |
| 3 | 323 | 258 | 257 | 485 |
| 4 | 240 | 235 | 234 | 531 |

The level-one counts have an initial exception at `2 -> 3`, and level two starts at the exceptional prime 3; the modular alternating theorem applies after removing the relevant initial endpoints.

### Successive prime-gap-of-gap hierarchy

The number of **prime-valued gaps** when starting with the first 1,000 gaps on each level and repeatedly taking gaps between prime-hit positions is:

| Depth of prime-gap-position extraction | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---:|---:|---:|---:|
| 1 | 679 | 550 | 323 | 240 |
| 2 | 53 | 88 | 106 | 89 |
| 3 | 17 | 33 | 36 | 31 |
| 4 | 7 | 6 | 10 | 10 |

This is the requested explicit **prime pattern within prime pattern** in two recursive directions. The total number of entries shrinks at every further extraction, so these counts should **not** be interpreted as asymptotic densities.

### Gap-size structure versus gap-primality structure

Pearson correlation of **second differences of the numeric sequences**, for 200 first indices:

| Adjacent levels | Second-difference correlation | Correlation of prime-gap flags (200) | Correlation of prime-gap flags (1,000) |
|---|---:|---:|---:|
| 1-2 | 0.917185 | -0.007066 | -0.088048 |
| 2-3 | 0.991960 | +0.076875 | +0.044489 |
| 3-4 | 0.997938 | +0.014226 | +0.027439 |

This is a distinction: **size** of gaps is highly correlated across levels, while primality of the skipped counts does not show comparably strong same-index correlations in these finite samples. These are deterministic finite diagnostics; they do not prove statistical independence.

Restricting to pairs with both skipped counts at least 7 and not divisible by 3 gives prime-flag correlations approximately `-0.0784`, `+0.0351`, `+0.0071`, based on 207, 555, 562 pairs respectively. This control reduces the concern that the raw near-zero correlation is solely a mod-3 artifact; it does not control every residue or size effect.

## Adversarial control: the apparently fractal gap-size correlations can be manufactured

Start instead from the **trivial odd arithmetic progression** `A(n)=2n+1`. Prime-index it repeatedly using the *same genuine prime index set*: `T a(n)=a(p_n)`. Then

`T^k A(n)=2S_k(n)+1`, hence

`G(T^k A)(n)=2q_k(n)+1`, where `G(a)(n)=a(n+1)-a(n)-1`.

Every Pearson correlation between corresponding second differences is **exactly the same** for this all-odd control as for the original nested prime-number sequences (positive affine scaling leaves correlation unchanged).

Thus the high cross-level gap correlations *cannot by themselves* establish a new arithmetic pattern beyond the prime-indexing operation. The original primality of the values and the subsequent primality of the skipped counts are the aspects the control does **not** reproduce.

## Mathematical interpretation and stopping rule

The modular-6 identity is analogous to a conserved discrete domain-wall charge in a two-state spin chain. It is a faithful and exact mathematical analogy, but it is fully explained by residue classes of primes and applies to arbitrary prime subsequences. Higher wheel moduli generate more states and local exclusion rules; they do not by themselves yield noncircular global constraints on zeta zeros.

**No zero-exclusion theorem emerged.** The present open research question is whether a genuinely new correlation between prime-valued skip counts at distinct depths remains *after* all forced modular rules, local gap scales, and indexing artifacts are removed. The 1,000-gap experiment does not provide convincing evidence of such a correlation. Do not launch Codex or assert an RH connection solely from these finite patterns. Do not conflate the existence of repeated primality tests with mathematical independence of the generated sequences.

## Verification scope

- Exact finite computations: Python/Numpy integer sieve and deterministic primality; output files `finite_results.json`, `nested_prime_gap_table.csv`.
- Proved elementary statements: gap telescoping, modulo-6 alternation/charge, modulo-30 necessary sieve and odd-arithmetic control.
- No use of RH, Haglund k=2/k=3, Lean 4, numerical Xi certificates or assumptions about hypothetical nontrivial zeros.
- Lean 4 was not available on the local `PATH`; no Lean compilation is claimed.
- Literature novelty not established; Batchko (arXiv:1405.2900) reports the underlying finite-difference quasi-self-similarity.

## References

- Batchko, *A prime fractal and global quasi-self-similar structure in the distribution of prime-indexed primes* (2014): https://arxiv.org/abs/1405.2900
- Higher-order prime numbers (OEIS Wiki): https://oeis.org/wiki/Higher-order_prime_numbers
- Torquato, Zhang and De Courcy-Ireland, *Hidden Multiscale Order in the Primes* (2018, conditional diffraction connection): https://arxiv.org/abs/1804.06279
