> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `d1db6f0db95f99695f37a0d45e5aa3baba74a1943d472ddb509514675d8015e3`.

# Project Riemann — single-length marked-inverse gate

**19 October 2026. Scientific classification:** An exactly certified **conditional** improvement of the Xu–Sang endpoint calculation; the decisive analytic marked-inverse-moment improvement is **UNPROVED**. `NO_NEW_RH_FRONTIER_ADVANCE`. RH is open, complete Haglund k=2/k=3 verification is `UNVERIFIED`, and historical provenance remains `BLOCKED_UNWAIVED`.

## 1. The precise missing analytic lemma

Original source: [OpenAI, *The Quasi-Riemann Hypothesis: Re(s)>7/8*, September 30, 2026](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), `lem:marked` in the section **The inverse moment with prime factors** (source SHA in session: `268c4e3206d460c617d3d2129742a72b831b3def`). It bounds, uniformly in the paper's exact finite-order Eisenstein ray-character family, prescribed smooth weights, unit twists, original zero extensions, and fixed independent prime-slot coefficients,

\[
\sum_{0<N(u)\ll U}|M_{\psi_u}(r;W)Q_u|^2\ll_\varepsilon U^{1+\varepsilon}
\]
provided there are **fixed positive gaps** in both
\[
 r+2z<1,\qquad 2r+8z<3.
\]
Here `r` is the log-`U` length of the normalized inverse Möbius polynomial and `z` is the total selected prime-slot length. The source uses two masked Poisson transformations and a canonical marked energy recursion. **The proposed single change** is:

\[
\boxed{r+z<1,\qquad 2r+8z<3}\tag{H}
\]

with the **same conclusions and uniformity**, at least in the source's exact physical-prime coefficient subfamily and the selected parameter range below. (H) is *not proved* by the source or by this session. It is not an innocuous relaxation: the source's initialization invariant contains exactly `m-r-2z+2G`, and this doubled prime-length cost must be eliminated by a new analytic mechanism. Extending (H) by simply replacing a hypothesis in a proof is circular.

## 2. Quantitative effect assuming (H)

Use [Xu–Sang, arXiv:2610.15291v2, equations (20), (21), (27), (28), and Sections 4–8](https://arxiv.org/html/2610.15291v2). Fix

\[
 b=1/100,\quad \ell=21/125,\quad \kappa=29991/40000,\quad h=757/1000,
 \quad l_y=421/1000,
\]

and `c=1/(3κ)`, `q=δx`, `1/8 ≤ δ ≤ 5/6`, `0 ≤ x ≤ 1/2`. Define

\[
\begin{split}
D&=3-(1+2c)x,\\
P&=(2-2cx)(1-x),\\
J&=(5/6-\delta)D+\delta P,\\
R_{\rm old}&=1-\delta+\frac{(5/6-\delta)\delta P}{2J},\\
C_0&=-1/4+b/6+5\ell/4,\\
\mathrm{base}&=C_0+\delta/2+\delta x\{\ell+c(h/4-l_y/2)\},\\
E(R)&=\mathrm{base}-3h(1-R)/4.
\end{split}
\]

**Outside** the dangerous rectangle `5/12≤δ≤13/20`, `7/16≤x≤1/2`, the published `E(R_old)<-1/1000` holds exactly (three rational box certificates).

**Inside**, select

\[
\begin{split}
t&=1+\frac{\delta P}{2J}-\frac1{25},\\
r_0&=\frac{(2-2cx)t+(c-1)x}{D}-\frac3{100},\\
m_0&=t-r_0,\\
z_I&=\frac{3-2r_0}{8}-\frac1{1000},\\
z_P&=\frac{1-2m_0}{6\kappa}-\frac1{1000}.
\end{split}
\]

The exact verification proves `1≤t≤3/2`, `t-1/2≤r_0<1`, `0<m_0<1/2`, positive slot capacities `z_I,z_P`, `z_I+r_0<1`, `2r_0+8z_I≤3-1/200`, `2m_0+6κ z_P≤1-1/500`, and `z_I,z_P<ℓ/(h+10^-6)`.

By the source detector, every difficult row at this `t` has witnesses with `r+m≥t`. If `r≥1`, the source's existing unmarked long-inverse moment applies. For `r_0≤r<1`, **hypothetical (H)** gives the inverse row bound; its exponent is monotone decreasing in `r` when the marked capacity is chosen at the new constraint. For `r<r_0`, the unchanged source plain fourth moment gives the complementary row bound; its exponent decreases as `m≥t-r` increases. Thus the row-count exponent is at most the maximum of

\[
\begin{split}
R_I&=1-\delta r_0-2\delta x z_I,\\
R_P&=1-2\delta m_0-2\delta x z_P,\\
R_L&=1-\delta+(5/6-\delta)(t-1).
\end{split}
\]

**Exact rational Bernstein certificates and independent Wolfram real quantifier elimination** both prove, throughout the dangerous rectangle,

\[
E(R_I)<-1/1000,\quad E(R_P)<-1/1000,\quad E(R_L)<-1/1000.
\]

The unchanged Xu–Sang endpoint propagation, small-δ/floor rows, parameter geometry, numerator-amplification licensing and two-stage family bound were checked against their written scalar requirements. The existing reported zero-free bound `0.8748867` licenses `κ=29991/40000` because `0.8748867<(1+κ)/2`.

**Conditional mathematical implication, not a theorem:** if (H) were proved with all the original analytic input and uniformity conditions, Xu–Sang's method would yield the stronger family zero-free boundary

\[
\boxed{\operatorname{Re}s> B(\ell)=11/12-\ell/4=328/375=0.874666\ldots}.
\]

This is only an improvement of about `0.000220` over `0.8748867`; it is nowhere close to proving RH. No part of this computation demonstrates the new moment estimate, nor that it is true.

## 3. Adversarial checks and limitations

- The proof's initialization has a literal `m-r-2z` margin, so (H) is **not** available via the published recursion. One must show how to recover one mark length, possibly through nontrivial cancellation of the marked first-frequency correlations, while retaining zeros, twists, and coefficients.
- The matched sharp sextic large-sieve norm concerns **arbitrary coefficient vectors** and does not automatically refute (H) for the special inverse-times-prime vectors. Conversely, no known positivity or elementary divisor identity proves (H).
- Annular Möbius and plain sums **cannot** be replaced by complete Euler products; a formal `L·L^{-1}=1` would silently assume the missing cancellation.
- Exact Bernstein certificates establish **only polynomial inequalities under (H)**. They do not verify Poisson summation, uniform analytic bounds, or an RH proof. No Lean 4 compiler was available in this session; therefore nothing new is labelled Lean-checked.
- No original Project Riemann repository, k=2/k=3 manuscript, numerical certificate, Git ref, or service was altered.

## 4. Research decision

This is a **single proof-critical analytic target** and the first direct test should be falsification: can one construct an admissible coefficient/character configuration for which (H) fails? If not, can one replace the source initial `m-r-2z` invariant with a rigorously justified `m-r-z` bound? Do not attempt more parameter optimizations, enlarge the mark ranges beyond what is needed, or claim new RH progress before this question is settled.

Reproducer: `check_marked_inverse_single_length_gate.py` (exact rational Bernstein subdivision with no floating-point sign checks). Verify source/receipt independently and use Lean 4 for meaningful finite statement components when practical. Do not alter historical evidence.
