> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `b32a583d0e6be56ae2a5ac44c11c4b7af9c76bbe709cd2e806ae2d58aca266db`.

# Project Riemann — Signed multiplicative parity gate

**Date:** 2026-10-20  
**Status:** `PROVED_ELEMENTARY_PARITY_CLASSIFICATION / EXACT_FINITE_AXIS_COUNTERMODEL / NO_NEW_RH_FRONTIER_ADVANCE`  
**Scope:** Direct follow-up to `ARITHMETIC_VISIBILITY_PHASE_GATE.md` (2026-10-20). This file is independent of and does not modify any earlier report, file or Git ref. RH unproved; Haglund k=2/k=3 complete verification UNVERIFIED; stronger marked-inverse estimate BLOCKED_NEW_MOMENT_ESTIMATE; historical provenance BLOCKED_UNWAIVED.

## 0. Decision

A proposed route was: recover the Möbius sign from all-direction **even-order multiplicative** observations, then use a new positivity/correlation principle to force cancellation of the summatory Möbius function. **Stop this route.** The all-depth exact classification below shows that even-order multiplicative rays collapse to squarefree counting; odd-order rays retain the sign but an RH-strength bound is precisely RH-equivalent. A finite-prime-axis gauge produces identical even-order data over *all* integers but a linearly growing summatory function. The local geometry therefore cannot give a new zero-free theorem by itself.

This is an independently derived illustration of a **known class of sieve parity obstructions**. Novelty in the literature is NOT established.

## 1. Exact all-order signed multiplicative-ray classification

Let \(\mu\) be the genuine Möbius function. For an integer \(r\ge 1\) and fixed positive integers \(m_1,\dots,m_r\), set \(M=\operatorname{rad}(m_1\cdots m_r)\). If any \(m_i\) is nonsquarefree, \(\prod_i\mu(m_i n)=0\) for all \(n\). Otherwise every \(m_i\) is squarefree, and for every \(n\ge1\),

\[
\boxed{\prod_{i=1}^r\mu(m_i n)
=\Bigl(\prod_{i=1}^r\mu(m_i)\Bigr)\mu(n)^r\mathbf1_{(n,M)=1}.}
\tag{1}
\]

**Proof (elementary, unconditional).** If \(n\) is nonsquarefree, both sides vanish. If \(n\) shares a prime with some \(m_i\), both sides vanish because \(m_i n\) has a square factor. Otherwise \(\mu(m_i n)=\mu(m_i)\mu(n)\) by coprime multiplicativity. Multiply. No analytic input.

**Even parity:** for \(r=2j\), \(\mu(n)^r=\mu(n)^2\). The full two-/four-/six-... ray signal is squarefree visibility:

\[
\prod_{i=1}^{2j}\mu(m_i n)
=\Bigl(\prod_i\mu(m_i)\Bigr)\mu(n)^2\mathbf1_{(n,M)=1}.
\]

Its summatory asymptotic is fully elementary:

\[
\sum_{n\le X}\prod_{i=1}^{2j}\mu(m_i n)
=\Bigl(\prod_i\mu(m_i)\Bigr)\frac X{\zeta(2)}
\prod_{p\mid M}\frac p{p+1}+O_M(\sqrt X).
\tag{2}
\]

**Odd parity:** for \(r=2j+1\), the sign survives:

\[
\prod_{i=1}^{2j+1}\mu(m_i n)
=\Bigl(\prod_i\mu(m_i)\Bigr)\mu(n)\mathbf1_{(n,M)=1}.
\tag{3}
\]

For example, **for every \(n\)**,

\[
\boxed{\mu(2n)\mu(3n)\mu(6n)=\mu(n)\mathbf1_{(n,6)=1}.}
\tag{4}
\]

**Exact RH-equivalence gate.** For any fixed odd \(r\) and fixed squarefree \(m_i\), the assertion

\[
\forall\varepsilon>0:\quad
\sum_{n\le X}\prod_{i=1}^r\mu(m_i n)
=O_{\varepsilon,m_i}(X^{1/2+\varepsilon})
\tag{5}
\]

is **equivalent to RH**, not independent evidence. For fixed \(M\), the Dirichlet series of \(b_M(n)=\mu(n)\mathbf1_{(n,M)=1}\) is, initially for \(\Re s>1\),

\[
\sum_{n\ge1}\frac{b_M(n)}{n^s}
=\frac1{\zeta(s)}\prod_{p\mid M}(1-p^{-s})^{-1}.
\tag{6}
\]

RH implies the bound for \(\mu\), and convolution with the fixed finite-prime Euler factors preserves every \(X^{1/2+\varepsilon}\) upper bound. Conversely, (5) implies convergence of the Dirichlet series (6) for \(\Re s>1/2\) by summation by parts. Multiplying by \(\prod_{p\mid M}(1-p^{-s})\), which is nonzero there, analytically continues \(1/\zeta(s)\) into that half-plane without poles. Hence \(\zeta\) has no zero there and the functional equation gives RH. This is a classical proof pattern; no new zero estimate is obtained.

## 2. A five-dimensional multiplicative parity-gauge countermodel

Fix any **finite** set of primes \(S\). Let the completely multiplicative \(\chi_S\) be defined by \(\chi_S(p)=1\) for \(p\in S\) and \(\chi_S(p)=-1\) otherwise. Define

\[
 a_S(n)=\mu(n)\chi_S(n)
 =\mu(n)^2(-1)^{\#\{p\in S:p\mid n\}}.
\tag{7}
\]

In particular \(a_S(n)^2=\mu(n)^2\). For any \(m_1,\dots,m_{2j}\) whose prime factors lie **only** in \(S\), and for every integer \(n\ge1\),

\[
\boxed{\prod_{i=1}^{2j}a_S(m_i n)
=\prod_{i=1}^{2j}\mu(m_i n).}
\tag{8}
\]

**Proof.** \(a_S(m_i n)=\mu(m_i n)\chi_S(m_i)\chi_S(n)\), with \(\chi_S(m_i)=1\). Multiplying an even number of factors gives \(\chi_S(n)^{2j}=1\); zeros coincide. This is an **all-\(n\)** identity, not a bounded computation.

Yet \(a_S\) has a positive mean:

\[
\boxed{\sum_{n\le X}a_S(n)
=c_S X+O_S(\sqrt X),\qquad
c_S=\frac1{\zeta(2)}\prod_{p\in S}\frac{p-1}{p+1}>0.}
\tag{9}
\]

**Elementary proof of (9).** Expand
\(a_S(n)=\mu(n)^2\prod_{p\in S}(1-2\mathbf1_{p\mid n})\).
For squarefree \(d\mid\prod_{p\in S}p\), the density of squarefree \(n\) divisible by \(d\) is \(\frac1{\zeta(2)}\prod_{p\mid d}(p+1)^{-1}\), with \(O_d(\sqrt X)\) counting error via \(\mu^2(n)=\sum_{j^2\mid n}\mu(j)\). The **finite** expansion over \(d\) gives the product in (9) and an \(O_S(\sqrt X)\) error. No Tauberian theorem is assumed.

For \(S=\{2,3,5,7,11\}\), the exact coefficient is

\[
 c_S=\frac6{\pi^2}\cdot\frac5{72}=\boxed{\frac5{12\pi^2}}.
\]

For the increasing set \(S_B=\{p:p\le B\}\), Mertens' theorem gives

\[
 c_{S_B}\sim\frac{e^{-2\gamma}}{(\log B)^2}\quad(B\to\infty),
\tag{10}
\]

but \(c_{S_B}>0\) for **each finite** \(B\). For every finite observation window \(n\le N\), choosing \(B\ge N\) makes \(a_{S_B}(n)=\mu(n)\) **on the entire window**, while the eventual summatory behavior remains linear. Finite matching and any number of bounded multiplicative dimensions cannot force RH-strength global cancellation without an independent uniform theorem.

The Dirichlet series identifies the exact analytic difference:

\[
\sum_{n\ge1}\frac{a_S(n)}{n^s}
=\frac{\zeta(s)}{\zeta(2s)}
\prod_{p\in S}\frac{1-p^{-s}}{1+p^{-s}}
\quad(\Re s>1).
\tag{11}
\]

It has a **pole at \(s=1\)** of residue \(c_S\), whereas \(\sum\mu(n)n^{-s}=1/\zeta(s)\) vanishes there. This is the analytic obstruction that the even-order observables miss.

**Adversarial scope correction:** the local gauge does NOT preserve all odd-order Möbius observables, the full Dirichlet-inverse identity, or the Möbius weights in the primitive-lattice inclusion–exclusion formula. Indeed, with the five-prime \(S\) above, \(a_S(13)=+1\) while \(\mu(13)=-1\), so \(a_S(1)+a_S(13)=2\) but \(\mu(1)+\mu(13)=0\). Uniqueness of the full identity \(\sum_{d\mid n}\mu(d)=\mathbf1_{n=1}\) fixes all signs globally; it still does not prove cancellation. The earlier five-dimensional *primitive lattice correlation formula* must not be conflated with \(\mu(n)^2\), since \(\mathbf1_{\gcd=1}\ne\mu^2(\gcd)\).

## 3. Reproducible exact finite checks

Run `python verify_signed_parity.py` (NumPy required). A linear sieve creates the actual \(\mu(n)\) up to \(N=1,500,000\), and independent trial division cross-checks its first 1,500 entries. Every later comparison is exact integer equality (no tolerance).

- \(M(1,500,000)=-293\), **versus** \(\sum_{n\le1,500,000}a_{\{2,3,5,7,11\}}(n)=63,289\).
- Analytic density prediction \(c_S N\approx63,325.74\), with observed deviation -36.74. This agreement is a diagnostic, not the proof of (9).
- 11 two-ray directions \(m=1,2,3,6,10,15,30,42,70,210,2310\) were checked pointwise for all admissible \(n\) with \(mn\le N\). All passed.
- Four rays \(\{1,2,3,6\}\) were checked at all 250,000 admissible indices. All passed.
- Odd three-ray formula (4) checked at all 250,000 admissible indices. All passed.
- Independent Wolfram symbolic/numeric kernel reproduced \(c_S=5/(12\pi^2)\), the two- and three-ray identities for all \(1\le n\le400\), and the out-of-direction exception at 13.
- Additive correlation \(\sum_{n<N}\mu(n)\mu(n+1)=1554\) versus \(\sum_{n<N}a_S(n)a_S(n+1)=6912\) at this cutoff. These are **computational diagnostics**, not asymptotic theorems. They show that additive shifts can reveal phase information that allowed multiplicative rays suppress.

## 4. Changing direction: the affine observation breaks the finite-axis gauge

The gauge symmetry (8) is specific to **multiplicative rays**. It can be broken by a genuinely different observation: an additive displacement. For a finite prime set \(S\), an elementary CRT calculation yields the exact limit

\[
\boxed{\lim_{X\to\infty}\frac1X\sum_{n\le X}a_S(n)a_S(n+1)
=\prod_{p\in S}\left(1-\frac4p+\frac2{p^2}\right)
\prod_{p\notin S}\left(1-\frac2{p^2}\right).}
\tag{12}
\]

**Proof (classical local counting, no RH input).** For a prime \(p\), modulo \(p^2\) there are \(p^2-2\) residues of \(n\) for which both \(n\) and \(n+1\) are squarefree at \(p\). If \(p\in S\), among these residues \(2(p-1)\) carry an extra negative sign (one member of the pair is divisible exactly once by \(p\)); the other \(p^2-2p\) carry a positive sign. The local mean is thus \((p^2-4p+2)/p^2\). If \(p\notin S\), the sign is invisible and the local mean is \((p^2-2)/p^2\). The CRT gives the finite-prime product. The contribution of large prime-square divisors to the overall average tends to zero: for \(p>Y\), \(p^2\mid n\) or \(p^2\mid n+1\) occurs at density at most \(O(\sum_{p>Y}p^{-2})\) plus a vanishing finite-cutoff error. Let \(X\to\infty\), then \(Y\to\infty\) to obtain (12).

For \(S=\{2,3,5,7,11\}\) let \(C_0=\prod_p(1-2/p^2)\). The ratio has the **exact rational value**

\[
\boxed{C_S/C_0=\prod_{p\in S}\frac{p^2-4p+2}{p^2-2}=\frac{79}{5593}.}
\tag{13}
\]

Therefore \(C_S\approx0.00455714\). At the finite cutoff \(X=1,500,000\), the actual countermodel correlation was **6,912**; the asymptotic main term predicts approximately **6,836**. For comparison the genuine Mobius shifted correlation over the same sample was **1,554**. These finite differences are observations, not a proof of a limiting law for the genuine shifted Mobius correlation.

**Consequence:** Adding even one *affine* observation can break the multiplicative gauge, but elementary local Euler products still govern the synthetic function. Obtaining uniform **genuine Mobius** phase cancellation along nonproportional affine directions is an independent analytic challenge. This is the narrow research direction that survives the no-go test; (12) alone does not solve it.

## 5. Why this matters and where to stop

A finite-dimensional count, all squarefree-support observables, or any number of even-order multiplicative-ray measurements cannot resolve the **multiplicative sign gauge**. Odd-order multiplicative rays restore the sign, but RH-strength cancellation of those rays is exactly another formulation of RH (equations 3–6).

The only viable broadening is to **nonproportional additive–multiplicative comparisons**, such as \(\mu(n)\mu(2n+1)\), where there is no common-factor cancellation identity (1). This is a deep, actively studied area: Tao's published 2016 logarithmically averaged two-point theorem, higher uniformity results, and an OpenAI September 2026 preprint *claiming* an ordinary-average power-of-logarithm saving for Liouville along nonproportional affine forms. We did **not** independently certify that latter preprint or use it as an analytic input. In any event a two-point \(O(X/\log^c X)\) result alone is far too weak to give \(M(X)=O(X^{1/2+\varepsilon})\) by routine correlation inequalities.

**Stop condition:** Do not launch Codex on multiplicative-ray parity, on further finite dimensional phase-gauge experiments, or on the odd-order RH-equivalent condition. Reopen only upon an explicitly stated *independently provable* nonproportional affine correlation estimate **with a quantitative route to an individual off-real Xi zero**, tested against the countermodel and prior no-go register.

## 6. Primary literature and scope

1. Friedlander and Iwaniec, *Asymptotic sieve for primes* (1998), https://arxiv.org/abs/math/9811186 — original methods to surmount sieve parity via extra bilinear information. The present example is consistent with, but not claimed as identical to, their theorem.
2. Friedlander and Iwaniec, *Using a parity-sensitive sieve to count prime values of a polynomial*, PNAS 94 (1997), https://doi.org/10.1073/pnas.94.4.1054.
3. T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum Math. Pi 4 (2016), https://arxiv.org/abs/1509.05422.
4. K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. (2026), https://doi.org/10.1007/s00222-026-01408-6.
5. OpenAI, *Ordinary two-point correlations of multiplicative functions*, dated September 24, 2026, public preprint, https://github.com/openai/math/blob/main/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/README.md — cited as a **claim** only. Related Lean scope document: https://github.com/openai/math/blob/main/lean/docs/007.md. Not audited here.
6. Classical RH equivalence: \(\sum_{n\le X}\mu(n)=O_\varepsilon(X^{1/2+\varepsilon})\). See e.g. https://mast.queensu.ca/~murty/TwinPrimes-Parity.pdf (discussion in source); the precise proof needed is given in §1.

**Verification classification:** Elementary analytic statements are written proofs, not Lean-compiled. Exact finite checks and an independent Wolfram cross-check passed. Lean 4 was not available (`command -v lean` gave no path). Historical evidence untouched. Full literature novelty of the finite-axis countermodel has not been assessed exhaustively.
