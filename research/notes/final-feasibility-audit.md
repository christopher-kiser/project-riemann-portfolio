> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `b62eda63e61a2180c12408592edad2bb9b509199452df6a6a470e7b39075b426`.

# Marked inverse-moment feasibility audit — 19 October 2026

**Decision: BLOCKED/UNVERIFIED — `BLOCKED_NEW_MOMENT_ESTIMATE`.**

The strengthened arithmetic moment has neither been proved nor disproved in this bounded audit. The attached finite gate is correct. Its analytic premise is unavailable from the published proof, including at a point of the gate's own parameter rectangle. No zero-free boundary is upgraded. RH remains open; complete Haglund k=2/k=3 verification remains `UNVERIFIED`; historical provenance remains `BLOCKED_UNWAIVED`.

Workspace: `LOCAL_ARCHIVE/project-riemann-marked-inverse-audit-20261019T185149Z`.

## Question and scope

The question is a uniform estimate for the actual Eisenstein-character sum
\[
 \sum_{0<N(u)\ll Z^{m}}|M_u(Z^r;W)Q_u|^2\ll_\epsilon Z^{m+\epsilon},
\]
with squarefree Möbius inverse coefficients, fixed ray twists, disjoint prime slots, original zero extensions, annular tests and the original coefficient/height uniformity. Here `m` is the row width, distinct from the plain-witness length `m0` in the supplied gate. Normalizing by a positive row width gives the candidate's `m=1` formulation; it does not dispense with fixed positive margins.

I read all three supplied files, ran the unchanged verifier, reconstructed its finite argument independently, and inspected the marked lemma, canonical energy, masked Poisson, initialization and recursive invariants in the [pinned original source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). I also reviewed [Xu–Sang v2, §§2 and 4–8](https://arxiv.org/html/2610.15291v2) for the conditional use of the gate. This is not a new verification of their entire analytic infrastructure or external formal proof.

## Finite gate: independently checked

The original verifier passed **19 continuum inequalities and 16 fixed comparisons**. A separate implementation uses only Python `Fraction`, reconstructs the rational formulas, and certifies all 19 inequalities on **1,216 rational boxes** by direct Bernstein coefficients. It shares neither SymPy nor the original subdivision routine. These are polynomial bounds throughout boxes, not sampled values: the Bernstein basis is nonnegative and sums to one, and every coefficient maximum is strictly negative.

With `c=1/(3κ)`, the full domain gives
\[
 D\ge5/2-c>0,\quad P\ge1-c/2>0,\quad
 J=(5/6-\delta)D+\delta P\ge(1-c/2)/8>0.
\]
Thus clearing denominators is legitimate, including at `δ=5/6`. The critical rectangle and three exterior rectangles cover the stated full parameter domain. The independent run also rejects a reversed sign and the old-margin claim at an exact gate point. Records: `verification/SUPPLIED_VERIFIER.*` and `verification/INDEPENDENT_GATE.json`.

The candidate's asserted Wolfram verification has no accompanying receipt here and is **not independently replayed**. Its 40-hex source identifier is a **Git blob SHA-1**, not a SHA-256 or commit identifier; it matches the downloaded source. Separate commit and SHA-256 pins are recorded.

## Decisive proof obstruction

Reconstruct the initial formal centers using overlap length `G`, quotient length `P1`, and remaining mark cap `z0`:
\[
 D'=r+z-2G,\quad F=D'-P_1,\quad M=2D'-m-2P_1,
 \quad Q=P_1+G,\quad z_0=z-G.
\]
Direct algebra, also compiled in Lean, gives
\[
\begin{aligned}
 F-M-Q-z_0&=m-r-2z+2G,\\
 4F-3M-6z_0&=3m-2r-8z+10G+2P_1,\\
 F-M-Q&=m-r-z+G.
\end{aligned}
\]
The first line is the actual puncture admissibility margin. The last line is what one would obtain by deleting the mark cap from that hypothesis; it is not a theorem authorizing its deletion.

At the supplied gate's `δ=x=1/2`, independently reconstructed values are
\[
 r_0={467988598319\over670130653625},\qquad
 z_I={133631714876\over670130653625}.
\]
They satisfy
\[
 1-r_0-z_I={13702068086\over134026130725}>0,\quad
 3-2r_0-8z_I={1\over125}>0,
\]
but
\[
 1-r_0-2z_I=-{65121374446\over670130653625}<0.
\]
The no-overlap sector `G=0` is not excluded by the coefficient hypotheses. At formal `P1=0`, the first canonical margin is already negative even with unit puncture; the row exponent `2(r0+zI)-1` is positive, so eliminating a negative row range cannot fix it. Arbitrarily small discretization losses and favorable clipping cannot absorb this fixed deficit. This establishes failure of the proposed implication to the existing proof's hypotheses, **not** a lower bound contradicting the arithmetic moment.

The published initialization replaces a signed two-column correlation by weighted Cauchy and positive canonical child energies. The positive measure discards Fourier phases. Recursive children preserve the original mark cap and require positive initial margins. This recursion cannot repair an inadmissible start. The canonical lemma also forbids an extra arbitrary residual column coefficient: the divisor bound on a mark does not permit absorbing it into an unmarked theorem. See `sources/openai_paper.tex:9285`, `:12120`, `:12208` and the dependency ledger.

## Falsification and bounded proof attempt

| Test | Independent conclusion and limit |
|---|---|
| Ordinary coefficient diagonal | For a fixed number `K` of slots, the product index `a=nP` has divisor-bounded multiplicity, support of size `O(Z^(r+z))`, and normalized coefficient square mass `O(Z^ε)`. Its diagonal contribution is `O(Z^(m+ε))`, not a counterexample. This does not bound off-diagonal terms. |
| Sixth-power aliases of columns | Squarefree `n` and disjoint prime slots imply valuations in `{0,1,2}`. Two such indices differing by a sixth power have identical prime valuations. The finite step is Lean-checked. This excludes that simple alias construction, not every ray-character correlation. |
| Overlap and Möbius cancellation | Overlap primes must be retained. For a fixed product index and fixed `K`, `Ω(n)=Ω(a)-K`, so all contributing Möbius signs agree. In the admissible trivial-twist, nonnegative-weight case there is no full-divisor cancellation identity. Lean checks the parity implication, not the arithmetic interpretation. |
| Imprimitive and sixth-power rows | Restoring a primitive inducing character without its removed-prime mask changes the problem. Sixth-power rows may make good-prime characters principal, but the remaining annular Möbius sum is not known here to have a lower bound violating the moment. No full Euler-product substitution is legitimate. |
| One aligned row / arbitrary vectors | A single-row absolute bound is `O(Z^(r+z+ε))`, below the target under the proposed first margin. Sharpness for unrestricted matrix vectors does not supply the required physical Möbius-times-prime vector. Neither argument proves a family upper bound. |
| Gauss factors and Poisson reorganization | Mask inclusion–exclusion, primitive finite Fourier inversion and Parseval reproduce the source prefactor and unit normalized Gauss magnitude. Taking absolute values supplies no extra power saving. Organizing the complete product first still gives column length `r+z` and dual row length `2(r+z)-m`; it does not prove the missing marked-energy estimate. |

No valid arithmetic counterexample was found by these specific tests. No signed correlation estimate sufficient to replace the failed canonical bound was established. Fixed ray phases, moving conductor factors, zero masks, product coefficients, smooth seminorms and height bounds must all remain in any such estimate; none has been dropped or declared harmless to force acceptance.

## Conditional accounting and stop

The finite value `328/375` and its licensing comparison are correct algebra. They are not an established improved zero-free boundary. A further qualification is necessary: a moment theorem only at `(r0,zI)` would not suffice for the detector's variable inverse witness. It is needed along the required range of capacities
\[
 z(r)=\max\{0,\min(1-r,(3-2r)/8)-1/1000\},
\]
with the original uniformity; the zero-slot transition uses the existing physical unmarked estimate. The relevant scalar monotonicity is Lean-checked under its explicit capacity hypothesis.

For conditional bookkeeping, one can retain the existing row bound and use `min(Rold,max(RI,RP,RL))` inside the rectangle. This preserves the old coarse bound used to license numerator amplification; the affine high-side exponent cannot increase. This observation neither establishes the new row count nor replaces the source's analytic premises.

**Single remaining proof obligation:** establish the strengthened marked inverse moment, or an adequate estimate for its actual structured initial correlations, in the new positive-gap range with every original uniformity requirement. The finite gate and the present source recursion do not discharge it. The prescribed bounded campaign stops here; no follow-on search or automatic continuation is authorized by this report.

For reproducibility, commands and exact evidence paths are in `CLAIM_DEPENDENCIES.md` and `LEAN_VERIFICATION_REPORT.md`. The strict preservation comparison recorded one added Codex capture reference; all original references and pinned inputs are unchanged. That full-reference failure is retained without waiver in `PRESERVATION_REPORT.md`. `SHA256SUMS` seals this workspace's files.
