> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `bc36a83aac03aead1e2df27620007c03c0a58bb6c03291eaddb41d951988498d`.

# Project Riemann — Nested prime-index, gaps of gaps, and run-length arithmetic

Date: 2026-10-20. This note extends the separately preserved `Project_Riemann_Nested_Prime_Angles_20261020.zip` audit; no historical Project Riemann archive was modified. Mathematical classification: `EXACT_ELEMENTARY_INVARIANT / CONDITIONAL_PNT_GROWTH_ASYMPTOTIC / FINITE_RECURSIVE_EVENT_TEST / NO_NEW_RH_FRONTIER_ADVANCE`.

## Purpose

The user's precise proposal is not just prime-indexed primes, but all recurring patterns among: original values, skipped numbers, primality of skipped numbers, spacing between the locations of prime-valued skips, and number of consecutive prime-valued skips before composite-valued skips, with every transformation repeated. Model these as different observable directions and distinguish exact invariant rules from finite trends that eventually break.

## Definitions and the two axes

Let `p_n` denote the n-th prime and `S_1(n)=p_n`, `S_(k+1)(n)=S_k(p_n)`. For each level, define the count of strictly skipped integers

`q_k(n)=S_k(n+1)-S_k(n)-1`.

Define the prime-gap event bit `b_k(n)=1_P(q_k(n))`. Let `H_k(j)` be the j-th index `n` with `b_k(n)=1`, so `H_k(j+1)-H_k(j)-1` is the number of *nonprime-valued* skipped counts between consecutive prime-valued skipped counts. Apply the operation again to the resulting counts to descend through a second axis.

Independently let `U_k(j)` be the number of *consecutive prime-valued skipped counts* between the j-th and (j+1)-st nonprime event; include an initial and final boundary run for finite samples. Both directions are recorded separately rather than being mistakenly conflated.

The exact one-step coarse-graining formula is:

`q_(k+1)(n) = q_1(n) + sum_{j=p_n}^{p_(n+1)-1} q_k(j)`.

This follows by telescoping, no RH assumptions, and is distinct from applying the prime-valued-gap event operation.

## Exact residue-transition law

For *any* increasing sequence `a_1<a_2<...` of primes with each `a_i>=5`, let `q_i=a_(i+1)-a_i-1` and `e_i=+1` if `a_i≡1 (mod 6)`, `e_i=-1` if `a_i≡5 (mod 6)`. The residue table is:

| Transition | q mod 6 | Meaning |
|---|---|---|
| 5 → 5 or 1 → 1 | 5 | No flip |
| 5 → 1 | 1 | One flip direction |
| 1 → 5 | 3 | Opposite flip direction |

For `c_i=1_{q_i≡1 (mod6)}-1_{q_i≡3 (mod6)}`,

`c_i = (e_(i+1)-e_i)/2` and hence `sum_{i=1}^N c_i = (e_(N+1)-e_1)/2 ∈ {-1,0,1}`.

Consequences: After dropping gaps of residue 5, the residues 1 and 3 alternate perfectly. For levels `k>=2`, no `q_k(n)` equals 3: one has `q_2(1)=1`, and any interval defining `q_2(n)` for `n>=2` contains at least two ordinary prime gaps starting with prime 5 or higher; their sum cannot be 4 because three primes >3 cannot all be spaced by 2. The prime-index composition only increases the distances at subsequent levels. Therefore every `q_k≡3 (mod6)` at levels `k>=2` is **guaranteed composite without factoring**. These conclusions do not specify which other skips are prime and are not new RH constraints.

Example from level 4: `S_4` starts 11,31,127,277,709,1063,1787,2221. Its skipped counts begin 19,95,149,431,353,723,433. The 1→5 residue change from 1063 to1787 forces 723≡3 (mod6) composite; the next opposite change produces 433≡1 (mod6) and does not by itself force primality.

## Growth in two non-interchangeable limits

### Fixed depth, large index

For each *fixed* positive integer k, the prime number theorem implies

`S_k(n) ~ n (log n)^k` as `n→∞`.

Induct from `p_n~n log n`; note that `log S_k(n)~log n` for fixed k. This explains why typical magnitudes increase rapidly at deeper levels but says nothing about individual exceptional gaps.

### Fixed index, large depth

For a *fixed* starting index n, write `a_0=n`, `a_(k+1)=p_(a_k)`. Then

`log a_k ~ k log k` and hence `a_k=exp((1+o(1))k log k)=k^{k(1+o(1))}` as `k→∞`.

Proof: Put `b_k=log a_k`. As `p_m~m log m`, `b_(k+1)-b_k=log b_k+o(1)`. Eventually `b_k≥k-O(1)`. As `log b≤sqrt b`, the upper increment bound `b_(k+1)-b_k≤2 sqrt(b_k)` yields `b_k=O(k^2)`; then the same increment equation improves this to `b_k=O(k log k)`. Hence `log b_k=log k+O(log log k)`, so summing increments gives `b_k=k log k+O(k log log k)`. This derivation uses the standard PNT, not RH.

The two limits `n→∞` at fixed k and `k→∞` at fixed n are genuinely different. Neither creates a quantum measurement effect.

## Computations (integer sieve to 30 million)

For the first **200 skipped counts** at each level:

| k | Median skipped | Maximum skipped | Prime-valued skips |
|---|---:|---:|---:|
| 1 | 5 | 21 | 136 |
| 2 | 41 | 189 | 124 |
| 3 | 416 | 2,089 | 78 |
| 4 | 5,346 | 29,473 | 65 |
| 5 | 84,112 | 495,769 | 38 |

For the first **1,000 skipped counts** at each of levels 1–4:

| k | Prime-valued skipped counts | Prime-valued *spacings between their positions* (out of one fewer position intervals) | Prime-valued lengths of consecutive prime-gap-event runs (including boundary runs) |
|---|---:|---:|---:|
| 1 | 679 | 53 / 678 | 102 / 322 |
| 2 | 550 | 88 / 549 | 123 / 451 |
| 3 | 323 | 106 / 322 | 63 / 678 |
| 4 | 240 | 89 / 239 | 42 / 761 |

Different columns represent different mathematical operations and different sample denominators. Differences between their frequencies are not evidence of self-similar laws without controls.

Recursively extracting prime-valued positions of skipped counts, then forming fresh skipped counts, gives these *raw* event totals at depths one through four:

| k | Depth 1 | Depth 2 | Depth 3 | Depth 4 |
|---|---:|---:|---:|---:|
| 1 | 679 | 53 | 17 | 7 |
| 2 | 550 | 88 | 33 | 6 |
| 3 | 323 | 106 | 36 | 10 |
| 4 | 240 | 89 | 31 | 10 |

The sample shrinks at each depth, so totals are not comparable population densities.

### The deceptive 1,000-gap pattern and its exact first failure

In the first 1,000 ordinary prime gaps, every skipped count `q≡5 (mod6)` is actually prime, because no gap length reaches 36 and the possible values are 5, 11, 17, 23, 29. Yet the *first* exception occurs at ordinary prime-gap pair **index 1,183**:

`9551 -> 9587`, difference 36, skipped count 35 = 5×7 (composite).

This is a precise illustration of a pattern that looks perfect for a long time and fails at a later size, which is central to the user's scale concern. No inference of infinite repetition from the first 1,000 values is legitimate.

## Independent controls and relation to RH

The earlier October 20 `Project_Riemann_Nested_Prime_Angles` audit reports very high same-index numeric gap-size correlations across adjacent levels but weak same-index correlations of the **prime-valued gap flags** in the first 1,000 tests: -0.088, +0.044, +0.027. It also proves that the numeric gap-size correlations are reproduced *exactly* when starting with the all-odd progression and applying the **same prime-index selector**, so those size correlations alone are not evidence of a separate prime-gaps law.

The new residue-transition law uses only the fact that every prime after 3 lies at residue 1 or 5 modulo 6; it applies to arbitrary prime subsequences. The recursive event totals depend on the full sequence and must be tested against appropriate controls for gap magnitude, arithmetic residue and finite sampling. They do not imply any independent information about nontrivial zeros of the Riemann zeta function.

Physical interpretation: The two residue classes resemble a two-state spin, and the `q≡1` and `q≡3` events resemble oppositely oriented domain walls with a conserved net charge. This analogy is exact at the level of combinatorics. It is **not** quantum entanglement, wave-function collapse or a proof of spectral confinement.

## Verdict and conditions for further work

**`EXACT_ARITHMETIC_STRUCTURE / NO_NEW_RH_FRONTIER_ADVANCE`.** This investigation explains genuine scale-dependent patterns and an exact conservation invariant. The next mathematically meaningful gate is an independent bound/correlation for prime-valued gap events that remains nontrivial after removing residue constraints, size effects and the prime-indexing selection artifacts. Do **not** promote sample correlations into global laws, assume an RH implication, or launch broad Codex optimization until a specific falsifiable theorem candidate arises.

## Verification

`verify.py` uses an exact boolean prime sieve through 30,000,000, with 1,857,859 primes. It checks five prime-index levels for 200 gaps, four for 1,000 gaps, recursion for 99 positions, the residue-transition invariant for every tested valid position, the first 1,183rd-gap exception, and the recursive run/event tables. Re-run `python verify.py` to reproduce `results.json` and `nested_prime_200_5levels.csv`. Lean 4 was not available locally; no Lean certification is claimed. All historical project files remain untouched.
