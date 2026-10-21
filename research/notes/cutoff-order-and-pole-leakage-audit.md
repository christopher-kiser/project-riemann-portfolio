> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `5730fd3220d1be7d81c6a1714aed27335c26cd6d0bd36107bec69f30162e0cd8`.

# Project Riemann — Cutoff-order, pole leakage, and the illusion of rare coherence

**Date:** 2026-10-19 US/Eastern (continued investigation).  
**Scientific verdict:** `CUTOFF_ARTIFACT_IDENTIFIED / NO_NEW_RH_FRONTIER_ADVANCE`.  
**Proof classification:** Exact finite combinatorial identity; conditional-on-stated-classical-input asymptotic using the verified 2026 7/8 zeta zero-free half-plane and its standard Mertens/prime-counting consequences. No independent new zeta zero exclusion, no Lean compilation, no originality/priority claim.  
**Relationship to archive:** This is a falsification audit of the previous `ARITHMETIC_COHERENCE_INTERMITTENCY_AUDIT.md`, **not** a replacement for or modification of any original handoff, k=2/k=3 evidence, or marked-inverse-moment campaign.

## 1. Finite exact algebra — the correct cutoff matters

Let \(\mu\) be Möbius and \(\Lambda\) von Mangoldt, \(s\in\mathbb C\) and \(K\ge2\). Define

\[
M_K(s)=\sum_{n\le K}\mu(n)n^{-s},\quad Q_K(s)=\sum_{n\le K}\Lambda(n)n^{-s},\quad D_K(s)=\sum_{n\le K}\mu(n)\log n\,n^{-s}.
\]

The earlier coherence experiment used \(H_K=M_KQ_K+D_K\). The **exact identity**
\[
\mu*\Lambda=-\mu\log
\]
implies
\[
\boxed{\sum_{ab\le K}\mu(a)\Lambda(b)(ab)^{-s}+D_K(s)=0\quad\text{for every }K,s.}\tag{1}
\]

In contrast,
\[
\boxed{H_K(s)=\sum_{K<ab\le K^2\atop a,b\le K}\mu(a)\Lambda(b)(ab)^{-s}.}\tag{2}
\]
Thus \(H_K\) is **exactly a mismatch of cutoff order**: cutting each factor at \(K\) and then multiplying is different from applying a cutoff to the multiplicative convolution. The huge coherent values described in the previous audit remain correct as statements about this *finite observable*; they are not an intrinsic violation of the arithmetic conservation identity.

**Origin of identity:** Since \(\mu*\mathbf1=\delta_1\) and \(\Lambda*\mathbf1=\log\), convolve with \(\mu\) and use \(\mu\log=-\mu*\Lambda\). This is standard Möbius inversion, see NIST DLMF §27.5.

## 2. Stronger theorem — the two limiting procedures do not commute

We formulate the analytic statement with all its hypotheses exposed.

**Hypothesis \(\mathrm{ZFR}(\theta)\):** For some \(\theta<1\), and every \(\epsilon>0\), standard partial-summation bounds hold:
\[
U(x):=\sum_{n\le x}\mu(n)=O_\epsilon(x^{\theta+\epsilon}),\qquad
\psi(x)=\sum_{n\le x}\Lambda(n)=x+O_\epsilon(x^{\theta+\epsilon}).\tag{3}
\]
These follow by classical arguments from the global zero-free half-plane \(\zeta(s)\ne0\) for \(\Re s>\theta\). The released and formally checked 2026 result supplies \(\theta=7/8\); its underlying theorem, NOT our work, is the input. The standard passage from zero-free half-plane to (3) is an explicit classical analytic dependency, not a new Lean-checked proof in this audit.

**Theorem.** Under (3), for \(\theta<\sigma<1\) and any fixed \(T>0\), uniformly for \(s=\sigma+it\), \(|t|\le T\),
\[
\boxed{\lim_{K\to\infty}K^{s-1}H_K(s)=\frac{1}{(1-s)\zeta(s)}.}\tag{4}
\]
The limit is nonzero throughout this compact height interval. Therefore
\[
|H_K(\sigma+it)|\sim\frac{K^{1-\sigma}}{|(1-s)\zeta(s)|}
\quad\text{at every fixed }t,\tag{5}
\]
uniformly on compact intervals. Consequently
\[
\frac1{2T}\int_{-T}^T|H_K(\sigma+it)|^2dt
\sim K^{2(1-\sigma)}\frac1{2T}\int_{-T}^{T}\frac{dt}{|(1-\sigma-it)\zeta(\sigma+it)|^2}.\tag{6}
\]
The last integral is finite and **strictly positive**. This finite-height-window mean square diverges with \(K\).

But the previous audit rigorously proved, *unconditionally for each* \(\sigma>1/2\),
\[
\lim_{A\to\infty}\frac1{2A}\int_{-A}^A|H_K(\sigma+it)|^2dt\ll_{\sigma,\epsilon}K^{1-2\sigma+\epsilon}\longrightarrow0.\tag{7}
\]
Therefore the infinite-height/time average and the infinite arithmetic cutoff have profoundly different behavior. There is no contradiction: all claims use different orders of limits.

**Proof of (4).** Partial summation applied to (3), and comparison with the Dirichlet series/analytic continuations initially valid for \(\Re s>1\), give uniformly on each bounded height interval and for \(\epsilon<\sigma-\theta\):
\[
\begin{split}
M_K(s)&=\zeta(s)^{-1}+O(K^{\theta+\epsilon-\sigma}),\\
D_K(s)&=\zeta'(s)\zeta(s)^{-2}+O(K^{\theta+\epsilon-\sigma}\log K),\\
Q_K(s)&=\frac{K^{1-s}}{1-s}-\frac{\zeta'(s)}{\zeta(s)}+O(K^{\theta+\epsilon-\sigma}).
\end{split}\tag{8}
\]
The third line arises because \(\psi(x)\) has a main term \(x\) from the pole of \(\zeta(s)\) at \(s=1\). Consequently
\[
H_K(s)=M_K(s)\frac{K^{1-s}}{1-s}+R_K(s),\qquad R_K(s)=O(K^{\theta+\epsilon-\sigma}\log K),\tag{9}
\]
where \(R_K=M_K[Q_K-K^{1-s}/(1-s)]+D_K\). Multiply by \(K^{s-1}\) and apply the first line of (8). The nonvanishing limit then gives (5), and uniform convergence on compact \(t\)-intervals gives (6).

**Pole subtraction.** A direct consequence of (9) is the uniformly decaying *renormalized mismatch*
\[
\boxed{R_K(s)=H_K(s)-\frac{K^{1-s}}{1-s}M_K(s)\to0\quad(\Re s>\theta,\ \Re s<1,\ |\Im s|\le T).}\tag{10}
\]
This shows the fixed-height growth is a **pole-driven cutoff leakage**, not a signal that a new off-line zero exists. Without an independently proved estimate below \(\theta\), (10) provides no new zero-free region. Simply demanding it for all \(\sigma>1/2\) is another unproved pointwise analytic assertion, not an independently established physical law.

## 3. Falsification and numerical evidence

The standalone script `verify_cutoff.py` performed a fully **exact** symbolic-log-prime check of \(\mu*\Lambda=-\mu\log\) for all \(1\le n\le750\) and independently checked each coefficient of matched-cutoff sums for \(K=10,31,100,300\). No floating point is used for these exact tests. In a separate Wolfram Language kernel, Mathematica built-ins `MoebiusMu`, `MangoldtLambda`, `Divisors`, and exact symbolic `Log` reproduced the same identity for all `2 <= n <= 120`, with zero failures.

Separate 35-digit floating-point diagnostics evaluate \(K^{s-1}H_K\) and the pole-subtracted residual at three sample heights; they are checks, NOT the proof of the limit. For example at \(s=0.9+2i\), the exact analytic target is approximately \(-0.3618691500+0.6590188737i\):

| K | Re\(K^{s-1}H_K\) | Im\(K^{s-1}H_K\) | \(|R_K(s)|\) approximate |
|---:|---:|---:|---:|
| 100 | -0.277171 | 0.602087 | 0.1354 |
| 1,000 | -0.331559 | 0.663338 | 0.0527 |
| 10,000 | -0.377572 | 0.658540 | 0.0421 |

All finite checks pass; numerical convergence need not be monotone. The theorem relies on classical asymptotics, not on this table.

## 4. Interpretation and stop condition

- A cutoff-inconsistent 'energy' can look enormous even when the exact multiplicative conservation relation is identically satisfied. The mathematical analog of measurement/renormalization *depends on the observable*, not observers affecting primes.
- The long-time \(L^2\) estimate from the preceding audit does **not** give local uniform control. Here it fails by a positive power of \(K\) at every fixed height in an already known zero-free half-plane.
- Crucially, the divergent part in this example is determined by the **existing zeta pole at 1**. It does not carry a new arithmetic restriction on hypothetical nontrivial zeros.
- A genuinely new proof-critical detector would have to survive convolution-compatible regularization or introduce independent signed arithmetic input beyond (3). We currently have neither.
- **Stop:** Do not resume optimizing this cutoff or infer that incoherent averages exclude individual zeros. Do not substitute this experiment into the marked-inverse-moment proof; that problem has different characters, annular masks, and correlation constraints.

## 5. Sources and evidence status

1. NIST DLMF §27.5, Dirichlet convolution and \(\Lambda=\mu*\log\): https://dlmf.nist.gov/27.5
2. OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*, published Oct 2026, with Lean theorem available: https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf
3. Original 2026 mathematical checkpoint and official scope: https://math20.org/f/003/
4. Classical Littlewood equivalence reference (as cited by the 2026 research): https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex
5. Prior investigation (uploaded in this conversation): `project_riemann_arithmetic_interference_20261019/ARITHMETIC_COHERENCE_INTERMITTENCY_AUDIT.md`.

## 6. Claim ledger

| Claim | Status |
|---|---|
| Matched-cutoff flux exactly zero | PROVED, finite elementary algebra |
| Unmatched flux is boundary-only | PROVED, finite elementary algebra |
| Mean-square-infinite-height bound from earlier audit | CLASSICAL proof, independent of RH |
| Fixed-height growth (4)–(6) | PROVED **with stated 7/8 zero-free + classical Tauberian/partial summation inputs** |
| Pole-subtracted residual tends zero in \(7/8<\sigma<1\) | PROVED with same classical inputs |
| Extension into \(1/2<\sigma\le7/8\) | UNVERIFIED |
| Any off-line zero excluded by this analysis | **NO** |
| Historical Haglund k=2/k=3 | UNVERIFIED, unchanged |
| Original marked inverse moment | BLOCKED_NEW_MOMENT_ESTIMATE, unchanged |
| Historical provenance | BLOCKED_UNWAIVED, unchanged |

**Final decision:** `CLOSE_CUTOFF_INTERFERENCE_AS_PROOF_ROUTE / NO_NEW_RH_FRONTIER_ADVANCE`. The original mathematical insight from nature is preserved as a valid analogy about measurement and limit order, but we explicitly retract interpreting this *particular* cutoff residual as a new physical instability of the primes. No Codex, no Lean 4 compilation, no modification of archival originals.
