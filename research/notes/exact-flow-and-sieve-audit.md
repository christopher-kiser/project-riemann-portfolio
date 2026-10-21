> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `dca026f584f5007312b7ed7411ad6cf448edd9e57f412247ea48a1c4e3d87827`.

# Project Riemann — Prime patterns within prime patterns: expansive flow, forbidden words and sieve horizon

**Date:** 2026-10-20. **Scope:** follow-up to the user's handwritten prime-index hierarchy and the two frozen October 20 nested-prime audits. **Historical records untouched.**  
**Status:** `EXACT_ELEMENTARY_MULTISCALE_THEOREMS / FINITE_FALSIFICATION_TEST / NO_NEW_RH_FRONTIER_ADVANCE`.

## Definitions

Let \(p_m\) be the \(m\)-th prime, \(S_1(n)=p_n\), and \(S_{k+1}(n)=p_{S_k(n)}\). Set \(\Delta_k(n)=S_k(n+1)-S_k(n)\), \(q_k(n)=\Delta_k(n)-1\), and \(b_k(n)={\bf 1}_{q_k(n)\text{ prime}}\). These match the user's convention of counting strictly skipped integers.

## Exact theorem A: expansion of every numerical gap

For all \(n,k\ge1\),

\[
\Delta_{k+1}(n)\ge2\Delta_k(n),\qquad
q_k(n)\ge 2^{k-1}\Delta_1(n)-1.
\]

**Proof.** For each index \(m\ge2\), the two consecutive primes \(p_m,p_{m+1}\) are odd, and \(p_{m+1}-p_m\ge2\). Since \(S_k(n)\ge2\),
\[
\Delta_{k+1}(n)=p_{S_k(n+1)}-p_{S_k(n)}
=\sum_{j=S_k(n)}^{S_k(n+1)-1}(p_{j+1}-p_j)\ge2(S_k(n+1)-S_k(n)).
\]
Iterate. Hence for every fixed index \(n\) the skipped counts grow at least exponentially with depth; this lower bound needs neither PNT nor RH. The actual growth is often considerably faster. The theorem gives no pattern in the *primality* of the growing gaps.

## Exact theorem B: a forbidden-transition law for prime-valued skipped counts

Except for the initial nonprime skip \(q_2(1)=1\), level-2 skipped counts are at least 5; all higher levels likewise have \(q_k(n)\ge5\). Therefore every **prime-valued** skipped count at \(k\ge2\) is a prime greater than 3, and all endpoints are odd primes exceeding 3.

Assign endpoint spin \(e_i=-1\) when \(S_k(i)\equiv5\pmod6\), and \(e_i=+1\) when \(S_k(i)\equiv1\pmod6\). An interval whose skipped count is prime can make only the transitions

* \(5\to5\) or \(1\to1\), when \(q_k(i)\equiv5\pmod6\), or
* \(5\to1\), when \(q_k(i)\equiv1\pmod6\).

The reverse transition \(1\to5\) forces \(q_k(i)\equiv3\pmod6\), hence is composite, because \(q_k(i)>3\).

Consequently, for **every uninterrupted run** of \(r\) prime-valued skipped counts, from gap indices \(i=m,\ldots,m+r-1\),

\[
\boxed{\sum_{i=m}^{m+r-1}{\bf1}_{q_k(i)\equiv1\ (6)}
=\frac{e_{m+r}-e_m}{2}\in\{0,1\}.}
\]

The residue words of such a run are therefore drawn from
\(\{5^r\}\cup\{5^{j-1}1\,5^{r-j}:1\le j\le r\}\), only \(r+1\) patterns rather than \(2^r\). This is an **upper bound on residue words**: the prime arithmetic need not realize every allowed word. Repeated \(5\to1\) transitions require an intervening composite-valued skip, a forced reset. This is a genuine finite-state/"hard-core" constraint, but it is a consequence of modular arithmetic, not a newly identified quantum law or a theorem about zeta zeros.

The underlying residue-charge identity \(\sum_i ({\bf1}_{q_i\equiv1(6)}- {\bf1}_{q_i\equiv3(6)})=(e_{\mathrm{end}}-e_{\mathrm{start}})/2\) was already in the October 20 archive. **New emphasis here** is the exact boundary formula and forbidden words *inside any all-prime-skipped-count run*, with explicit scope \(k\ge2\).

## Independent finite verification of the user's compounding-sieve observation

A new sieve was constructed from integers up to 30,000,000 (1,857,859 primes), and the first 1,000 skipped counts of levels 1 through 4 were independently regenerated and compared entry-by-entry to the frozen preceding audit. Both matched exactly. All expansion, spin-flow, run-boundary, and wheel-sieve assertions passed.

| Prime-index level | Median skipped count (1,000 gaps) | Prime-valued skips | Largest **least** prime factor of a composite skip | One composite invisible to smaller-prime sieves |
|---|---:|---:|---:|---|
| 1 | 5 | 679 | 5 | \(25=5^2\) |
| 2 | 61 | 550 | 17 | \(289=17^2\) |
| 3 | 787 | 323 | 59 | \(4307=59\cdot73\) |
| 4 | 12,114 | 240 | 173 | \(39,617=173\cdot229\) |

The factor column is the maximum, over composite skips among the first 1,000 gaps, of their **smallest** prime divisor; it is **not** a proposed asymptotic law. A fixed finite small-prime filter eventually misses such composite events in this sample, just as the user's observations suggest.

A trial sieve by primes through 47 leaves 679, 550, 324, and 294 candidates at levels 1–4. The actual prime-valued counts are 679, 550, 323, and 240. The remaining false candidates are 0, 0, 1, and 54, respectively. Each is classified correctly by extending the trial primes far enough; nothing about zeta's zeros is inferred from this.

The number of maximal prime-valued gap runs in the first 1,000 gaps is 279 at level 2, 228 at level 3, and 185 at level 4; longest run lengths are 7, 4, and 5. Every run obeyed the exact at-most-one-\(1\pmod6\) theorem; the counts are finite diagnostics rather than universal limits.

## Adversarial control: does an independent hidden prime pattern survive?

Let \(T\) mean taking elements at prime-numbered positions. Beginning with the trivial odd progression \(A(n)=2n+1\), the \(k\)-th filtered sequence is \(T^kA(n)=2S_k(n)+1\). Its skipped counts are **exactly** \(q_k^{\rm ctrl}(n)=2q_k(n)+1\). Thus identical cross-level gap-size correlations and arbitrarily deep prime-value-gap extraction can occur even when the starting sequence is not prime-valued. The control's first four prime-hit extraction totals are:

| Level | Genuine skipped-count tower | Odd-progression control tower |
|---|---|---|
| 2 | 550 → 88 → 33 → 6 | 473 → 106 → 41 → 11 |
| 3 | 323 → 106 → 36 → 10 | 325 → 124 → 35 → 9 |
| 4 | 240 → 89 → 31 → 10 | 213 → 69 → 18 → 9 |

These towers differ in their arithmetic details. The mere existence of repeated "prime patterns inside gaps" is therefore not independently characteristic of the original sequence being primes.

**Single bounded test for extra clustering:** Test \(A_k=\sum_{n=1}^{999} b_k(n)b_k(n+1)\), the number of adjacent pairs of prime-valued skips, with 2,000 fixed-seed descriptive permutations. Shuffle the prime-event labels **only within** groups with the same \(q_k(n)\bmod30\) and the same \(\lfloor\log_2(q_k(n))\rfloor\); that keeps the number of events in each modular/scale group unchanged. These are diagnostic surrogates, **not probability models for prime numbers**.

| Level | Actual adjacent prime-event pairs | Surrogate mean | Surrogate central 95% range |
|---|---:|---:|---:|
| 2 | 271 | 272.05 | 265–279 |
| 3 | 95 | 89.75 | 78–101 |
| 4 | 55 | 57.30 | 47–67 |

None of these three observed counts lies outside the descriptive surrogate range. The sample is small, the strata are heuristic, and other statistics might behave differently. Therefore this **does not prove independence or absence of arithmetic structure**. The comparison gives no robust *positive evidence* for an additional adjacency law in this particular test. At level 1 this surrogate is degenerate because the gap values are so small that the strata already determine most prime flags, so level 1 is omitted from the test table.

## Assessment of mathematical and RH relevance

**Established here:** an unconditional exponential lower bound on gap expansion; an exact finite-state forbidden-word/boundary law for prime-valued gap runs at every level \(k\ge2\); and exact finite verification of how additional prime divisors expose composite "dead ends" at increasing gap scales.

**Not established:** a new theorem about distribution of genuinely prime-valued gap positions, a persistent correlation beyond the index/residue/scale constraints, a zeta or Xi inequality, or exclusion of any hypothetical off-critical-line zero. The exact statements are derived from elementary prime-index and modular arithmetic and have not been shown novel relative to the full mathematical literature.

**Decision:** retain the 'expansion plus finite-state constraint' formulation as a cleaned-up mathematical model of the user's pattern-within-pattern observation. Do **not** translate the words "physical hard-core constraint" into a self-adjoint Hamiltonian or RH proof without a new independent spectral/arithmetic bridge. Do **not** launch Codex. A future research campaign would require a precise theorem with a demonstrable effect on the genuine prime-counting error or a hypothetical individual zeta zero, beyond what the prime-index rule already forces.

## Reproduction and integrity

Run `python verify_flow.py` in this directory; it needs Python, NumPy, and the bundled frozen input CSV. The script **independently regenerates** the full prime-index values from an exact 30-million sieve rather than trusting the CSV and writes `data.json`. No edits to prior October 19/20 evidence, Git history, RH/Haglund manuscripts, or source claims. Lean 4 was not on `PATH`, and no Lean formal verification is claimed.

**Relevant prior literature:** Robert G. Batchko (2014), *A prime fractal and global quasi-self-similar structure in the distribution of prime-indexed primes*, https://arxiv.org/abs/1405.2900. Its finite-difference correlations are not taken as a theorem controlling prime-valued-gap flags or RH.

**Project standing status:** `NO_NEW_RH_FRONTIER_ADVANCE`; RH OPEN; Haglund full \(k=2/k=3\) UNVERIFIED; `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`.
