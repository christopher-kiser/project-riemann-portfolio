> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `53d22a97fe25b883108ede99624034625c44df9dba2e225ec991c201ef0e97ee`.

# Project Riemann — Sharpness of reflected Heath–Brown/logistic zero-pair positivity

**Date:** October 19, 2026 (America/New_York).  
**Verdict:** `EXACT_CLASSICAL_LEMMA_WITH_PUBLISHED_KERNEL_INPUT / SHARPNESS_CONFIRMED / NO_NEW_RH_FRONTIER_ADVANCE`.

This audit continues the October 19 exact-logistic transfer investigation. It **does not** assert RH, Haglund Conjecture 4, a new zeta zero-free region, a verified off-critical-line zero, or theorem priority. It closes only the proposal to extend the *uniform nonnegative reflected-zero-pair inequality* from the published strip into the unknown interior strip without paying for additional negative contributions. The original handoff and audit workspaces were not modified.

## 1. Controlling primary sources and scope

- Chiara Bellotti, Tim Trudgian, Andrew Yang, *Zero-free regions inspired by work of Heath-Brown*, arXiv:2603.21490v1, March 23, 2026: https://arxiv.org/html/2603.21490 . In particular Definition 1 (exact `w_theta`), their proposed logistic smoothing (equation 14), and Lemma 5 (paired positivity for `0<=Re z<=2sigma-1`). The **published classical input** is `Re W(i y)>=0` for all real `y`, for this Heath–Brown kernel.
- OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*, September 30, 2026: https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md and its Lean scope https://github.com/openai/math/blob/main/lean/docs/003.md . Independently reported Lean rebuilds exist, but **this audit did not perform a new Lean build**.
- Yuanda Xu and Hejian Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2, October 15, 2026: https://arxiv.org/html/2610.15291v2 . The reported stronger `0.8748867` boundary explicitly relies on the earlier analytic inputs. It is **not** an independently compiled new proof here.
- Previous Project Riemann October 19 report: `project_riemann_logistic_transfer_20261019/EXACT_LOGISTIC_TRANSFER_AUDIT.md`. Earlier transferred `38 eta/y^2` estimates are valid in their own narrow parameter domain and **do not** imply globally nonnegative zero pairs outside the central strip.

## 2. Precise theorem

Let `0<theta<pi/2` and define `T=tan(theta)`, `S=sec(theta)^2`, `U=2 theta cot(theta)`. Let `w(v)` be *exactly* Definition 1 from Bellotti–Trudgian–Yang, defined by

\[
 w(v)=S\Big[S(\theta\cot\theta-v/2)\cos(Tv)
       +2\theta\cot\theta-v
       +\frac{\sin(2\theta-Tv)}{\sin(2\theta)}
       -2\left(1+\frac{\sin(\theta-Tv)}{\sin\theta}\right)\Big]
\]

on `0<=v<=U`, and zero beyond `U`. Fix arbitrary `eta>0`, `d>0`, and define

\[
 f(u)=\frac{\eta w(\eta u)}{1+e^{-du}},\quad
 F(z)=\int_0^{U/\eta}e^{-zu}f(u)\,du,
 \quad B(a,y)=\operatorname{Re}F(a+iy)+\operatorname{Re}F(d-a+iy).
\]

**Theorem (with the published positivity `Re W(iy)>=0` as classical input):**

\[
\boxed{\bigl(\forall y\in\mathbb R,\ B(a,y)\ge0\bigr)
       \quad\Longleftrightarrow\quad 0\le a\le d.}
\]

In fact, if `a<0` or `a>d`, writing `L=U/eta` and `y_n=(2n+1)pi/L`, the **strict quantitative asymptotic** is

\[
\boxed{\lim_{n\to\infty} y_n^4B(a,y_n)
     =\eta^4 S T^4\left(1-
         \frac{\cosh((a-d/2)L)}{\cosh(d L/2)}\right)<0.}
\]

This excludes a universal nonnegative extension even by an arbitrarily small positive distance outside either endpoint. It does not assert anything about the actual ordinates of zeta zeros.

## 3. Proof

**Interior direction.** Define `G(z)=F(z)+F(d-z)`. Since `f` is compactly supported, `G` is holomorphic and bounded on the closed strip `0<=Re z<=d`. On either boundary `Re z=0` or `d`, using the exactly logistic factor,

\[
 \operatorname{Re}G(iy)
 =\int_0^L f(u)(1+e^{-du})\cos(yu)du
 =\int_0^L\eta w(\eta u)\cos(yu)du
 =\operatorname{Re}W(iy/\eta)\ge0.
\]

(The other boundary has the same real part.) Thus `e^{-G}` is holomorphic and bounded in the strip with modulus at most one on both boundary lines. Hadamard's three-lines theorem yields `|e^{-G}|<=1` inside. As `B(a,y)=Re G(a+iy)`, `B>=0` for every frequency when `0<=a<=d`. This is the positivity already supplied by the published kernel input.

**Endpoint identities.** Differentiate the *displayed exact source formula* for `w`. Substitution at zero and at `U=2theta cot theta`, followed only by the identities `sec²theta=1+tan²theta`, `cos 2theta=(1−tan²theta)/(1+tan²theta)` and `sin 2theta=2tan theta/(1+tan²theta)`, gives

\[
 w'(0)=0,\qquad w(U)=w'(U)=w''(U)=0,
 \qquad w'''(0)=S T^4>0,\qquad w'''(U)=-S T^4.
\]

The five nontrivial equalities and the direct endpoint substitution are **independently rechecked with exact symbolic algebra** in `verify_pair_sharpness.py`. The third derivatives were also independently checked using Wolfram Language. This is **not Lean checking**.

**Exterior direction.** Put

\[
 q_a(u)=\frac{e^{-au}+e^{-(d-a)u}}{1+e^{-du}}
 =\frac{\cosh((a-d/2)u)}{\cosh(du/2)},\qquad
 g_a(u)=\eta w(\eta u)q_a(u).
\]

Then `B(a,y)=int_0^L g_a(u) cos(yu) du`. Since `q_a` is even as a function of `u`, `q_a'(0)=0`. The endpoint identities prove

\[
 g_a'(0)=0,\quad g_a(L)=g_a'(L)=g_a''(L)=0,\quad
 g_a'''(0)=\eta^4 ST^4,\quad
 g_a'''(L)=-\eta^4 ST^4 q_a(L).
\]

For every `y!=0`, four integrations by parts give the **exact identity**

\[
 y^4B(a,y)=g_a'''(0)-g_a'''(L)\cos(yL)
                  +\int_0^L g_a^{(4)}(u)\cos(yu)du.
\]

For fixed `a,d,eta`, `g_a^{(4)}` is integrable on `[0,L]`. By the Riemann–Lebesgue lemma, the last integral tends to zero as `|y|->infinity`. Along `y_n=(2n+1)pi/L`, `cos(y_n L)=-1`, hence the displayed asymptotic. If `a` lies outside `[0,d]`, then `|a−d/2|>d/2` and consequently `q_a(L)>1` strictly. This forces negative `B(a,y_n)` for all sufficiently large `n`, establishing the reverse implication.

**Dependency precision:** The exterior-negative theorem depends only on the explicit elementary kernel formula and classical Fourier calculus; it is unconditional upon zeta zero placement and on `Re W>=0`. The interior-positive half uses the **published** Heath–Brown positivity input. If that input were mistaken, the exterior impossibility remains valid, while the full iff theorem would need a new boundary-positivity proof.

## 4. Falsification example in the currently unresolved interior strip

Choose `theta=5669/5000=1.1338`, `eta=0.007`, `sigma=0.874`, `d=2sigma−1=0.748`, and a **hypothetical** zero with real part `beta=0.8745`. Then `a=sigma−beta=-0.0005<0`, and `beta` is *below* the stronger **reported conditional** Xu–Sang boundary `0.8748867`: its exclusion is not already provided by that claim.

- `L=151.318991268426535...` and `q_a(L)=1.078595245232363...>1`.
- At `n=5`, `y_5=(11 pi)/L=0.228375294467736...`, independent high-precision quadrature and QUADPACK's cosine-weight integration both return `B(a,y_5)≈−0.000440360527927`.
- The theorem gives the strictly negative limiting coefficient `eta^4 S T^4(1−q_a(L))≈−2.2128705738e−8`.

The **finite-frequency numerical value is a cross-check**, not an interval-arithmetic certificate; the analytic theorem already proves the existence of infinitely many negative frequencies exactly. No actual zeta zero is alleged at `beta=0.8745`, and `y_5` is not asserted to equal the difference of any actual zeta-zero ordinates.

## 5. Proof-critical significance and stop/go

In an attempted improvement from known `beta<=B` to a candidate smaller `sigma<B`, the zero-pair formula has `a=sigma−beta`. For an as-yet-unexcluded zero with `sigma<beta<=B`, that `a` is negative. The theorem proves one cannot *simply extend the all-frequency nonnegative zero-pair bound* to cover this case, no matter how small the improvement `B−sigma` is. A proof could still proceed by a **genuine signed cancellation estimate on the actual zero ordinates**, by changing the kernel or the arithmetic method, or by an independently established lower bound. It cannot proceed through the claimed unconditional extension of the old positivity lemma.

There is a second architectural barrier to reusing this *fixed-scale single-zero* inequality to exclude a **constant** `beta<1` at all large heights: if `eta,d,sigma,beta` stay fixed, every `F(sigma−beta)` and `F(sigma−1)` is a finite, `t`-independent number, whereas the positive digamma/gamma contribution retained by the standard trigonometric-polynomial detector grows as `f(0)log t` for `t->infinity`. Discarding other zeros by mere nonnegativity then gives no contradiction at sufficiently high `t`. This observation is **conditional on that architecture**; it does not rule out height-dependent weights, a global signed cancellation, or the different cubic-theta/Poisson moment method underlying the 2026 quasi-RH theorem.

**Decision:** Close the `uniform pair positivity beyond [0,d]` idea decisively. Do not optimize logistic coefficients or launch a Codex campaign. The exact negative-frequency lemma is a genuine mathematical boundary test, **not** an independent constraint excluding a hypothetical zero of the actual zeta function. New work must first provide a source-grounded theorem candidate controlling signed actual-zero/prime interactions, and should not merely restate RH or a zero-free half-plane as its assumption.

## 6. Verification, provenance and classifications

- `verify_pair_sharpness.py`: SymPy exact symbolic identities with no floating-point pass/fail for the endpoint conditions; second **diagnostic only** using 55-digit mpmath and independently formulated double-precision cosine-weight QUADPACK integration.
- `VERIFICATION_LOG.txt`: output of that script, including example and asymptotic coefficient.
- The independent Wolfram Language result on the source derivative formula returns `w'(0)=0`, `w'''(0)=sec²theta tan⁴theta`, `w(U)=w'(U)=w''(U)=0`, `w'''(U)=−sec²theta tan⁴theta`; there were minor harmless local-symbol warnings, so the independent SymPy replay is included.
- No `lean` or `lake` binary is installed in this execution environment. No Lean compilation or external mathematical peer review was performed. Classical integration-by-parts and Riemann–Lebesgue steps remain **written mathematical proofs**.
- The user's master handoff and previous audit source files were **read, not changed**. No WSL or Git access, ref mutation, Codex, systemd restart, network publication or paid action occurred. A SHA-256 manifest of this new additive research directory accompanies the audit.

**Standing historical status:** `RH=OPEN`, `HAGLUND_K2_K3=UNVERIFIED`, `MARKED_MOMENT=BLOCKED_NEW_MOMENT_ESTIMATE`, `PROVENANCE=BLOCKED_UNWAIVED`, `NEW_RH_FRONTIER_ADVANCE=NO`.
