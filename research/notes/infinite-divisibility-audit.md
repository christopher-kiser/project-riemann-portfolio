> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `82cffe33390f412765f836553fee4b267213bb712b818ff6ba8bb6dfdcf8eaad`.

# Project Riemann — exact non-infinite-divisibility certificate for the full Xi theta law

**Checkpoint:** October 19, 2026.  
**Classification:** `PROVED_WITH_STATED_CLASSICAL_INPUTS` (new exact self-contained certificate for this project; literature novelty **not claimed**).  
**RH frontier:** `NO_NEW_RH_FRONTIER_ADVANCE`.  
**Other standing statuses:** Full Haglund Conjecture 4 k=2/k=3 `UNVERIFIED`; marked inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`; original historical Git reference provenance `BLOCKED_UNWAIVED`.  
**Historical preservation:** All earlier uploaded handoffs, source archives, and evidence left unchanged. No Codex campaign, WSL service, Git mutation, or publication was initiated.

## 1. Precise theorem

Use the standard entire completed zeta function

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \Xi(z)=\xi(\tfrac12+iz).
\]

Let the **full** Riemann theta kernel, not a finite summand, be

\[
K(v)=\sum_{n=1}^\infty \pi n^2 e^{5|v|}\big(2\pi n^2 e^{4|v|}-3\big)e^{-\pi n^2e^{4|v|}}>0\qquad (v\in\mathbb R).
\]

The handoff's exact normalization is

\[
\Xi(z)=4\int_{\mathbb R} K(v)e^{2izv}\,dv,
\quad
\xi(s)=4\int_{\mathbb R} K(v)e^{2(s-1/2)v}\,dv
\quad (s\in\mathbb C).
\]

For every real \(\sigma\), let \(\mu_\sigma\) be the probability distribution of \(Y=2V\) with

\[
\mathbb P_\sigma(V\in dv)=\frac{K(v)e^{2(\sigma-1/2)v}}{\int_{\mathbb R}K(w)e^{2(\sigma-1/2)w}dw}\,dv.
\]

**Theorem.** For *every* real \(\sigma\), the distribution \(\mu_\sigma\) is not infinitely divisible (in the classical additive probability sense). Equivalently, although

\[
\varphi_\sigma(t)=\frac{\xi(\sigma+it)}{\xi(\sigma)}
\]

is a genuine positive-definite characteristic function on \(\mathbb R\), **none** of these characteristic functions is the characteristic function of an infinitely divisible law.

The assertion is unconditional and makes no assumption about whether RH holds. The proof does **not** imply Xi has a nonreal zero.

## 2. Key necessary inequality for infinite divisibility

Let \(X\) be an infinitely divisible real random variable with moment-generating function \(M(t)=\mathbb E e^{tX}\) finite for every real \(t\). Write \(L(t)=\log M(t)\). The Lévy–Khintchine representation (with the usual nonnegative Lévy measure \(\nu\)) reads

\[
L(t)=bt+\frac{a}{2}t^2+\int_{\mathbb R\setminus\{0\}}
\big(e^{tx}-1-tx\mathbf1_{|x|\le1}\big)\,\nu(dx),\qquad a\ge0.
\]

For \(h>0\), define the forward fourth difference

\[
\Delta_h^4L(t)
=L(t+4h)-4L(t+3h)+6L(t+2h)-4L(t+h)+L(t).
\]

It annihilates the linear, quadratic, constant, and compensation terms. The remaining term is

\[
\boxed{\Delta_h^4L(t)
=\int_{\mathbb R\setminus\{0\}}e^{tx}(e^{hx}-1)^4\,\nu(dx)\ge0.}
\]

The interchange is justified by the assumption of all real exponential moments (and Lévy integrability at zero). This sign condition is a **necessary**, not sufficient, criterion for infinite divisibility.

## 3. Exact integer certificate using genuine Xi values

The full-theta representation above implies every exponential moment exists and

\[
M_\sigma(t)=\frac{\xi(\sigma+t)}{\xi(\sigma)},\qquad
L_\sigma(t)=\log\xi(\sigma+t)-\log\xi(\sigma).
\]

Take \(h=2\), \(t=2-\sigma\). The fourth difference does not depend on \(\sigma\):

\[
\Delta_2^4 L_\sigma(2-\sigma)
=\log\left(\frac{\xi(10)\xi(6)^6\xi(2)}{\xi(8)^4\xi(4)^4}\right).
\]

From Euler's formulas \(\zeta(2)=\pi^2/6\), \(\zeta(4)=\pi^4/90\), \(\zeta(6)=\pi^6/945\), together with the standard \(\zeta(8)=\pi^8/9450\) and \(\zeta(10)=\pi^{10}/93555\), one obtains exactly

\[
\xi(2)=\frac\pi6,\qquad \xi(4)=\frac{\pi^2}{15},\qquad
\xi(6)=\frac{2\pi^3}{63},\qquad
\xi(8)=\frac{4\pi^4}{225},\qquad
\xi(10)=\frac{8\pi^5}{693}.
\]

Thus all powers of \(\pi\) cancel and

\[
\boxed{\exp\big(\Delta_2^4 L_\sigma(2-\sigma)\big)
=\frac{244140625}{244592271}<1.}
\]

Indeed the denominator exceeds the numerator by the **positive integer 451646**. Hence the fourth difference is strictly negative, contradicting the necessary nonnegative difference for an infinitely divisible law. As \(\sigma\in\mathbb R\) was arbitrary, this proves the theorem simultaneously for all exponential tilts.

The entire certificate can be checked by the bundled standard-library-only Python program `verify_exact_id_obstruction.py` (it computes rational coefficients and the rational ratio with `fractions.Fraction`; it does not prove the Lévy–Khintchine input). A separate SymPy symbolic check confirmed the same rational simplification. Nothing depends on a numerical zero list or a truncation of the Xi theta series.

## 4. Stronger versus weaker notions; avoid overclaiming

1. **This rules out infinite divisibility, NOT positive definiteness.** The same Xi distribution is a bona fide positive probability measure on every vertical slice. There is no contradiction: positive-definite characteristic functions need not be infinitely divisible.
2. **The theorem does not contradict or settle RH.** A self-adjoint Hamiltonian may have a non-infinitely-divisible spectral measure. The no-go is restricted to a proposed *infinitely divisible Lévy/Gibbs* upgrade of this exact theta characteristic distribution, and any theorem that requires such an upgrade.
3. **The square-root reciprocal is a different variable.** The criterion involving \(\xi(1/2)/\xi(1/2+\sqrt{2\theta})\) is *not* refuted by this calculation. Converting a linear parameter into \(\sqrt\theta\) changes fourth differences and Laplace transform properties; generalized gamma convolution/Thorin positivity at the critical point remains RH-equivalent, rather than proved here.
4. **The linear reciprocal also fails an elementary Laplace test.** For \(R_2(u)=\xi(2)/\xi(2+u)\), direct evaluation gives \(R_2(0)=1\), \(R_2(2)=5/(2\pi)\), \(R_2(4)=21/(4\pi^2)\). Every positive Laplace transform must obey \(R_2(2)^2\le R_2(0)R_2(4)\) by Cauchy–Schwarz. In fact

   \[
   R_2(2)^2-R_2(0)R_2(4)=\frac1{\pi^2}>0.
   \]

   This is an exact three-point obstruction to interpreting the **linear** reciprocal as an ordinary positive-law Laplace transform, regardless of infinite divisibility. The more general reason is that \(\log\xi(s)\) is strictly convex for all real \(s\), by the variance identity from the positive theta representation, while the log of a Laplace transform of a positive law must be convex. The reciprocal ratio has *strictly concave* log instead.
5. **Literature scope:** N. G. Polson's July 2026 SSRN abstract uses a linear reciprocal completed-xi Laplace language; the August 2026 SSRN abstract discusses the *different square-root transform* and also notes failure of infinite divisibility for a completed-zeta distribution at \(\sigma>1\). Full PDF texts were not accessible in this environment (SSRN retrieval returned a forbidden response). We therefore flag a literal linear-variable obstruction but **do not claim a vetted correction of the full manuscripts** or assert priority for the result.

## 5. Falsification decision and exact frontier

**What was genuinely verified:** A clean, full-Xi, RH-independent theorem stating non-infinite-divisibility of every theta exponential tilt, with an exact integer certificate. The entire finite algebra was checked independently using `fractions.Fraction` and SymPy. The characteristic-function and exponential-moment representation was inherited from the prior full-kernel audit and explicitly re-derived. The infinite-divisibility implication is standard Lévy–Khintchine theory, stated with its exact hypotheses.

**What was not proved:** A nonvanishing bound for \(\xi(\sigma+it)\), a new zero-free window for zeta, a failure of the hypothetical spectral self-adjointness model, or a positive Thorin measure. This theorem *does not exclude a single off-critical-line zero*, and it does not imply one exists.

**Next action/stop:** Close the direct positive/infinitely-divisible probability lifting of Xi's vertical characteristic distributions for all real tilts. Do not launch Codex for this issue; the exact proof is finished and a new audit would not add a proof-critical RH inequality. The possible **square-root Thorin/GGC program** requires a separate new noncircular arithmetic input before further work (otherwise it is a known RH equivalence). Retain the original failure `BLOCKED_NEW_MOMENT_ESTIMATE` unchanged.

## 6. Sources and provenance

- User's handoff: `Project_Riemann_Complete_Handoff_20261019(1).zip`, `01_AUTHORITY_AND_SCIENTIFIC_STATUS.md` (full theta normalization and project limitations).
- Immediately preceding audit: `project_riemann_gibbs_pf_audit_20261019/PRIME_GIBBS_THETA_TILT_AUDIT.md` (full kernel, positive-definite vertical characteristic functions for all σ). Its numerical PF5 result was not used in this theorem.
- NIST DLMF, [§25.6(i)](https://dlmf.nist.gov/25.6) (exact ζ(2k) values).
- Encyclopedia of Mathematics, [Infinitely-divisible distribution](https://encyclopediaofmath.org/wiki/Infinitely-divisible_distribution) (classical Lévy–Khintchine background).
- N. G. Polson, [*Thorin Positivity, GGC Factorization and the Riemann Xi Function*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6930178), July 2026, public abstract only.
- N. G. Polson, [*Thorin Measures and the Reciprocal Xi Function*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7320139), August 2026, public abstract only.

**Formalization:** The proof was not Lean-compiled: Lean 4 was not installed in this container. The nontrivial analytic step is the standard Lévy–Khintchine representation; the finite rational check does not depend on Lean and is fully reproducible. No numerical inference of a zero sign or proof of RH is claimed.
