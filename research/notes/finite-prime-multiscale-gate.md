> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `9d9e95758446a46dd9adaa4bf6f28ea89b4e1414da32d38b13f7d1bf615d9089`.

# Project Riemann — Finite-prime constraints and the observation-scale barrier

**Date:** 2026-10-20  
**Status:** `PROVED_WITH_CLASSICAL_PROBABILISTIC_INPUTS / NO_NEW_RH_FRONTIER_ADVANCE`  
**Scope:** Bounded continuation of `MESOSCOPIC_SIGNED_CORRELATION_AUDIT.md` and `SIGNED_PARITY_AND_AFFINE_GATE.md`.  
**Historical statuses:** RH open; complete Haglund k=2/k=3 unverified; `BLOCKED_NEW_MOMENT_ESTIMATE` remains blocked; provenance `BLOCKED_UNWAIVED`. No original artifact was modified.

## 1. Mathematical question and result

The previous result showed that an off-critical-line zeta zero with real part \(\beta>1/2\) forces a positive Fejér-weighted excess of Möbius shifted correlations at scale roughly \(H=N^{2-2\beta}\). Its biased-sign control preserved squarefree support but *not even the exact Möbius rule under multiplication by 2*. We now retain any prescribed **finite collection of prime-multiplication sign laws** while testing **all window lengths simultaneously**.

**Theorem (finite-prime mesoscopic no-go).** Fix any finite set of primes \(S\) and any \(1/2<\beta<1\); write \(\vartheta=2-2\beta\in(0,1)\). There exists a deterministic function \(b:\mathbb N\to\{-1,0,1\}\) such that:

1. \(b(n)^2=\mu(n)^2\) for every \(n\ge1\);
2. for **every** \(p\in S\), \(b(pn)=-b(n)\) if \(p\nmid n\), and \(b(pn)=0\) if \(p\mid n\);
3. with the explicitly positive constant \(A_{S,\beta}\) below, \(\sum_{n\le N}b(n)\sim A_{S,\beta}N^\beta\) as \(N\to\infty\);
4. extending \(b\) by zero outside \(1\le n\le N\) and writing
\[
 E_H(N)=\sum_{x\in\mathbb Z}\bigg|\sum_{j=0}^{H-1}b(x+j)\mathbf1_{1\le x+j\le N}\bigg|^2,
\]
we have **simultaneously for every sufficiently large integer** \(N\) and **every** \(1\le H\le N^\vartheta\),
\[
 \boxed{E_H(N)\ll_{S,\beta} NH(\log N)^4.}
\]
The existence result is unconditional and uses standard elementary number theory, Hoeffding's inequality, the Hilbert-space \(L^2\) Doob maximal inequality, and Borel–Cantelli. It is *not* a theorem about the actual Möbius partial sums. It proves that squarefree support, finitely many exact multiplicative prime-direction laws, and all subcritical window-energy observations do not logically force RH-strength square-root cancellation.

The proof is a new combination for this project of standard probabilistic methods. **Mathematical priority or literature novelty has not been established.**

## 2. Explicit random construction and first moment

Write \(R=\prod_{p\in S}p\) (empty product \(R=1\)) and \(D=2^{|S|}\). For every squarefree \(m\) coprime to \(R\), select independent signs \(\xi_m\in\{-1,1\}\) with
\[
 \mathbb E\xi_m=m^{\beta-1},\qquad
 \Pr(\xi_m=1)=(1+m^{\beta-1})/2.
\]
For squarefree \(n\), write it uniquely \(n=d m\) with \(d=(n,R)\mid R\) and \((m,R)=1\), and put
\[
 b(n)=\mu(d)\xi_m; \qquad b(n)=0\ \text{if $n$ is not squarefree}.
\]
The zero support and exact prime-dilation law for every \(p\in S\) follow immediately. There is *no multiplicativity claim* for primes outside \(S\).

The standard squarefree counting formula with the finite coprimality restriction is
\[
 Q_R(X)=\sum_{m\le X\atop(m,R)=1}\mu(m)^2=c_R X+O_R(\sqrt X),\quad
 c_R=\frac1{\zeta(2)}\prod_{p\mid R}\frac{p}{p+1}.
\]
Partial summation yields, for \(\beta>1/2\),
\[
 \sum_{m\le X\atop(m,R)=1}\mu(m)^2m^{\beta-1}
 =\frac{c_R}{\beta}X^\beta+O_{R,\beta}(X^{\beta-1/2}+1).
\]
Therefore
\[
 \mathbb E M_b(N)
 =\frac{c_R}{\beta}N^\beta\sum_{d\mid R}\frac{\mu(d)}{d^\beta}
 +O_{R,\beta}(N^{\beta-1/2}+1)
 = A_{S,\beta}N^\beta+o(N^\beta),
\]
where
\[
 \boxed{A_{S,\beta}=\frac{1}{\beta\zeta(2)}
 \prod_{p\in S}\frac p{p+1}(1-p^{-\beta})>0.}
\]
Further, \(M_b(N)=\sum_{m\le N}\mu(m)^2\xi_m\,w_m(N)\), with \(w_m(N)=\sum_{d\mid R,\,dm\le N}\mu(d)\) and \(|w_m(N)|\le D\). The \(\xi_m\) are independent, so weighted Hoeffding plus Borel–Cantelli gives almost surely
\[
 M_b(N)=\mathbb E M_b(N)+O_{S,\beta}(\sqrt{N\log N})
 \sim A_{S,\beta}N^\beta
\]
for *all sufficiently large* \(N\), since \(\beta>1/2\).

## 3. Exact all-window second-moment estimate

Let \(b_N\in\ell^2(\mathbb Z)\) be the truncated sequence and \(K_H\) the convolution operator that maps \(b_N\) to its length-\(H\) moving sums. Young's inequality says \(\|K_H v\|_2\le H\|v\|_2\). At \(n=dm\), the deterministic mean obeys
\[
 |\mathbb E b(n)|\le R^{1-\beta}n^{\beta-1};\qquad
 \sum_{n\le N}|\mathbb E b(n)|^2
 \le R^{2-2\beta}\Big(1+\frac{N^{2\beta-1}}{2\beta-1}\Big).
\]
Thus
\[
 \|K_H\mathbb E b_N\|_2^2
 \le R^{2-2\beta}H^2\Big(1+\frac{N^{2\beta-1}}{2\beta-1}\Big).
\]
For the centered part \(Z_{N,H}=K_H(b_N-\mathbb E b_N)\), decompose it into the \(D\) prime-axis components indexed by \(d\mid R\). A single independent core sign \(\xi_m\) contributes to at most \(D\) locations \(dm\); each location contributes an \(H\)-point window vector of squared norm \(H\). Cauchy–Schwarz, followed by independence, gives
\[
 \mathbb E\|Z_{N,H}\|_2^2\le D^2NH.
\]
Combining the deterministic mean and centered part,
\[
 \mathbb E E_H(N)
 \le D^2 NH+R^{2-2\beta}H^2\Big(1+\frac{N^{2\beta-1}}{2\beta-1}\Big)
 \ll_{S,\beta}NH\quad(H\le N^{2-2\beta}).
\]
This already proves the random-walk-sized bound **in expectation at every subcritical window length**. We require a stronger, simultaneous almost-sure conclusion.

## 4. Uniformization over every N and H (the proof-critical step)

For fixed \(d\mid R\), the sequence of \(\ell^2(\mathbb Z)\)-valued random variables
\[
 Y_{d,k}=\mu(d)\sum_{m\le k\atop(m,R)=1}\mu(m)^2
 (\xi_m-\mathbb E\xi_m)K_He_{dm}
\]
is a Hilbert-valued martingale as \(k\) increases. Here \(\|K_He_{dm}\|_2^2=H\). The \(L^2\) Doob maximal inequality and orthogonality of independent centered increments give
\[
 \mathbb E\max_{k\le X/d}\|Y_{d,k}\|_2^2
 \le4\mathbb E\|Y_{d,\lfloor X/d\rfloor}\|_2^2
 \le4HX/d.
\]
Since \(Z_{N,H}=\sum_{d\mid R}Y_{d,\lfloor N/d\rfloor}\), finite Cauchy–Schwarz yields the **simultaneous cutoff bound**
\[
 \boxed{\mathbb E\max_{N\le X}\|Z_{N,H}\|_2^2\le4D^2HX.}
\]
Let \(X=2^j\) and take every dyadic window \(H=2^\ell\le X^\vartheta\). Markov's inequality gives probability \(O(j^{-4})\) that the corresponding maximum exceeds a suitable constant times \(j^4HX\). There are \(O(j)\) such \(H\), so the union-failure probability is \(O(j^{-3})\), summable in \(j\). Borel–Cantelli therefore implies that almost surely, for every sufficiently large \(j\), **all dyadic** \(H\le X^\vartheta\) and all \(N\le X\) satisfy
\[
 \|Z_{N,H}\|_2^2\ll_{S,\beta}j^4HX.
\]
Restricting to \(X/2<N\le X\) turns \(X\) into at most \(2N\). The deterministic mean estimate from §3 is \(O_{S,\beta}(NH)\) for \(H\le N^\vartheta\). This proves \(E_H(N)\ll_{S,\beta}NH(\log N)^4\) for dyadic \(H\), **uniformly at every large cutoff \(N\)**.

For arbitrary \(H\), partition a length-\(H\) window into disjoint dyadic blocks, using each power of 2 at most once. Minkowski's inequality and \(\sum_{2^\ell\text{ used}}\sqrt{2^\ell}\ll\sqrt H\) extend the estimate without increasing the logarithmic exponent. This proves the theorem for every integer \(N,H\) in the claimed range.

**Important scope:** This is not a uniform-in-\(S\) theorem. The constants depend on \(D=2^{|S|}\) and \(R\), and can become enormous as new prime directions are added. The \(S\to\text{all primes}\) limit cannot be taken from it.

## 5. Why the observation exponent is sharp for this information

For **any** real sequence \(a_n\) of length \(N\), the exact window-sum identity and finite Cauchy–Schwarz give
\[
 E_H(N)\ge \frac{H^2|\sum_{n\le N}a_n|^2}{N+H-1}.
\]
In our construction \(|M_b(N)|\asymp N^\beta\). For \(H=o(N)\), this forces
\[
 \frac{E_H(N)}{NH}\ \gg_{S,\beta}\ H N^{2\beta-2}
 =\frac{H}{N^{2-2\beta}}.
\]
Thus the natural crossover scale is \(H\asymp N^{2-2\beta}\). Below that scale, random-walk-sized total window energy can coexist with a power-law cumulative bias; above it, the Cauchy lower bound eventually grows beyond any fixed random-walk constant. This **matches the shift exponent of the previous inverse-correlation theorem** and explains why the exponent cannot be improved by a purely universal Hilbert-space inequality.

This is a scale-information obstruction, not a zeta-zero confinement theorem.

## 6. Exact computation and adversarial checks

`verify_scale_gate.py` uses exact integer linear-sieve values of \(\mu(n)\) and a fixed seed to generate the model for \(S=\{2,3,5,7,11\}\), \(\beta=3/4\), \(N=400000\). It checks:

- exact equality \(b(n)^2=\mu(n)^2\) for all integers through 400,000;
- exact \(p\)-dilation sign laws for **all** five primes and all valid \(n\);
- the Fejér autocorrelation identity for ten window lengths \(1\le H\le512\);
- the Möbius divisor inverse identity independently for 498 integers;
- finite expectation and asymptotic coefficient.

For this five-prime case the asymptotic coefficient is
\[
 A_{S,3/4}=\frac{385}{192\pi^2}\,\frac43
 \prod_{p\in\{2,3,5,7,11\}}(1-p^{-3/4})
 \approx0.02767598555656.
\]
A Wolfram symbolic evaluation independently confirmed \(c_R=385/(192\pi^2)\), \(A_{S,3/4}\approx0.02767598555656\). The single finite sample gave \(M_b(400000)=355\), exact finite expectation \(434.312\), and asymptotic prediction \(440.198\). Its window-energy ratios \(E_H/(NH)\) varied from about 0.606 to 0.628 for dyadic \(H\le512\). A single seed cannot verify the almost-sure theorem. The theorem is proved in §§2–4.

The construction even agrees with the exact genuine Möbius function (and therefore with the full divisor-inverse identity) on the infinite multiplicative submonoid of integers whose prime factors all lie in \(S\): for those integers the coprime core is \(m=1\), and \(\xi_1=1\) deterministically. The construction is nevertheless deliberately *not* the actual Möbius function. The sample has \(b(13)=+1\) but \(\mu(13)=-1\); it fails coprime multiplicativity at \((13,19)\): \(b(13)b(19)=+1\), while \(b(247)=-1\). At the prime 13, the global divisor-inverse identity already fails: \(b(1)+b(13)=2\ne0\). This explicitly identifies the missing **all-primes Dirichlet-inverse law**. These are adversarial checks of the exact missing assumption, not defects being concealed.

## 7. Literature comparison and decision

- Matomäki and Radziwiłł, *Multiplicative functions in short intervals*, **Annals of Mathematics** (2016), https://annals.math.princeton.edu/2016/183-3/p06 — almost-all short interval cancellation, not RH-strength uniformity over all cutoffs.
- Matomäki, Radziwiłł, Tao, Teräväinen, and Ziegler, *Higher uniformity of bounded multiplicative functions in short intervals on average*, **Annals of Mathematics** (2023), https://annals.math.princeton.edu/2023/197-2/p03 — higher uniformity on average, not a pointwise square-root energy bound.
- Matomäki, Radziwiłł, Shao, Tao, and Teräväinen, *Higher uniformity of arithmetic functions in short intervals II: Almost all intervals*, **Inventiones Mathematicae** (2026), https://doi.org/10.1007/s00222-026-01408-6 — the stated almost-all interval scope is not a substitute for all-scale pointwise control.
- Exact finite Fejér / van der Corput autocorrelation identity, Young convolution inequality, Hoeffding's inequality, Hilbert-valued Doob maximal inequality, Borel–Cantelli, and the classical squarefree count are the proof inputs.

**Decision:** `EXACT_FINITE_PRIME_ALL_SCALE_NO_GO / NO_NEW_RH_FRONTIER_ADVANCE`. We have proved a stronger methodological limitation, not a new zero-free region and not RH. Neither the exact scale threshold nor the survival of finite-prime sign constraints gives a prime-specific cancellation theorem. If a new candidate emerges, it must have **uniform compatibility as the number of prime directions grows with the observation scale** and must bound an individual off-line-zero signal without presupposing RH. We do not currently possess such a bound, so do not launch Codex on this branch.

**Tool scope:** Numerical and exact finite arithmetic checks executed; Wolfram symbolic constant cross-checked. Lean 4 compiler absent, so no Lean-certified theorem is claimed. No original manuscript, historical evidence, Git ref, or seal was changed.
