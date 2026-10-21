> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `16b04025283a991ae881b582dafe0269c14de25c867b1c7268667ff991d0ee40`.

# Project Riemann — exact prime-Gibbs / theta-tilt stability audit

**Date:** 19 October 2026 (New-chat continuation)  
**Frontier verdict:** `NO_NEW_RH_FRONTIER_ADVANCE`. The ordinary quantum thermal-characteristic-function route into the critical strip is **CLOSED**, as is recovery of continuous-theta-kernel PF∞ by any real exponential tilt. We independently rechecked an already published **actual-theta** finite PF5 counterexample; it is a structural obstruction, not an RH counterexample.  
**Preserved project status:** RH open; full Haglund Conjecture 4 k=2/k=3 `UNVERIFIED`; marked-inverse moment `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`. No prior evidence, Git refs, k2/k3 records, services, or WSL trees modified. No Codex launched.

## 1. Precise physical/arithmetic bridge and its two tests

### 1.1 Arithmetic prime Gibbs system (unconditional on Re s>1)

Take a quantum Hamiltonian with energy levels \(E_n=\log n\), \(n\ge1\). For fixed real \(\sigma>1\), the thermal partition function is trace-class:

\[
Z_\sigma=\operatorname{Tr}e^{-\sigma H}=\sum_{n\ge1}n^{-\sigma}=\zeta(\sigma),
\quad p_n=\frac{n^{-\sigma}}{\zeta(\sigma)}>0,\quad \sum_np_n=1.
\]

The normalized unitary survival/thermal amplitude is

\[
A^{\rm prime}_\sigma(t)=\operatorname{Tr}(e^{-\sigma H}e^{-itH})/Z_\sigma
=\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=\sum_np_ne^{-it\log n}.
\]

This is a positive-definite function of time and \(|A^{\rm prime}_\sigma(t)|\le1\). **The trace diverges for \(\sigma\le1\)**: analytic continuation of \(\zeta\) is *not* continuation of the positive Gibbs state.

**Falsification criterion:** Would \(A^{\rm prime}_\sigma(t)=\zeta(\sigma+it)/\zeta(\sigma)\) remain the characteristic function of *any* positive probability measure for fixed \(1/2<\sigma<1\)? No. Voronin universality (an unconditional theorem for the actual zeta function) implies \(\sup_{t\in\mathbb R}|\zeta(\sigma+it)|=\infty\) for each such fixed \(\sigma\). Since \(\zeta(\sigma)\ne0\) and is finite for real \(\sigma\in(1/2,1)\), the ratio is unbounded, whereas every normalized positive-definite characteristic function has modulus at most one. No RH or zero-location assumption is used.

**Illustrative numerical two-point witness (not an interval certificate):** With mpmath at 20, 40, and 70 digits, \(\sigma=0.55,t=100\) gives

\[
|\zeta(0.55+100i)/\zeta(0.55)|=1.49986778150623789584085\ldots>1.
\]

This already violates the necessary \(2\times2\) Gram condition \(\det\bigl[\begin{smallmatrix}1&A(t)\\\overline{A(t)}&1\end{smallmatrix}\bigr]=1-|A(t)|^2\ge0\). The theorem via universality, rather than the un-certified numerical value, is the rigorous global rejection.

### 1.2 The exact completed Xi function *is* a characteristic function at every vertical slice

Use the **full**, untruncated theta kernel (not the first summand):

\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\quad u\ge0,\qquad K(v)=\Phi(|v|)>0.
\]

Each summand is positive since \(2\pi n^2e^{4u}-3>0\). The actual Xi normalization verified from the handoff is \(\Xi(z)=8\int_0^\infty\Phi(u)\cos(2zu)\,du=4\int_{\mathbb R}K(v)e^{2izv}\,dv\). With \(\alpha=2(\sigma-1/2)\) this gives the **exact** identity

\[
\xi(\sigma+it)=4\int_{\mathbb R}K(v)e^{\alpha v}e^{2itv}\,dv,
\qquad
\frac{\xi(\sigma+it)}{\xi(\sigma)}
=\int_{\mathbb R}e^{2itv}\,d\mu_\sigma(v),
\quad d\mu_\sigma(v)=\frac{K(v)e^{\alpha v}}{\int K(w)e^{\alpha w}dw}\,dv.
\]

All exponential moments exist because \(K\) has super-exponential tails. Thus \(\mu_\sigma\) is a genuine probability measure **for every real \(\sigma\)**. No assumptions about zeros are needed. For every real \(\sigma\), times \(t_j\) and complex \(c_j\),

\[
\sum_{j,k}c_j\overline{c_k}
\frac{\xi(\sigma+i(t_j-t_k))}{\xi(\sigma)}
=\int\left|\sum_j c_je^{2it_jv}\right|^2d\mu_\sigma(v)\ge0.
\]

Because \(K(v)>0\) on every real interval, the triangle inequality is strict for \(t\ne0\):

\[
\boxed{|\xi(\sigma+it)|<\xi(\sigma)\quad(\sigma,t\in\mathbb R,\ t\ne0).}
\]

Also \(\frac{d^2}{d\sigma^2}\log\xi(\sigma)=\operatorname{Var}_{\mu_\sigma}(2v)>0\). Both claims are **proved from the actual theta representation with classical analysis**, not new zero-exclusion theorems. Positive-definite time slices may have zeros, and their horizontal parameter family has no proved nonzero Fourier lower bound. At the same \((\sigma,t)=(0.55,100)\), a numerical check gives \(|\xi(\sigma+it)/\xi(\sigma)|\approx1.49356\times10^{-30}\), consistently below one; the gamma/completion factor changes the positivity behavior drastically.

## 2. The exact PF5 obstruction survives every thermal tilt

A published **preprint**, Wojciech Michałowski, *On the Pólya Frequency Order of the de Bruijn--Newman Kernel: Certified Failure at Order Five*, **arXiv:2602.20313v2 (20 July 2026)**, gives a rigorously interval-certified negative 5×5 Toeplitz minor of the full \(K\) at \(u_0=0.01,h=0.05\). Version 2 **withdraws** its earlier global/asymptotic sign thresholds because of an unsound high-derivative tail bound. Only its direct finite PF5 witness is used here. Primary text: https://arxiv.org/html/2602.20313v2, Theorem 1.1 and §4.

We independently recomputed its central witness with the source's **correct full theta kernel** and a separately justified tail bound. Define

\[
D_r=\det[K(u_0+(i-j)h)]_{i,j=0}^{r-1};\quad (u_0,h)=(1/100,1/20).
\]

With mpmath **1.3.0** outward-rounded `iv` at 90 decimal digits, summing \(n=1,\ldots,50\) and enclosing the omitted tail by \(\pm10^{-70}\) in each entry, both (i) a direct 120-term signed Leibniz interval sum and (ii) an **independent exact rational** determinant bound (after outward-decimal-rounding each interval input to 40 decimal places) establish the signs:

| Minor | Independently checked enclosure / sign |
|---|---|
| \(D_2\) | \(0.034064040622631369\ldots>0\) |
| \(D_3\) | \(0.000697697064264379\ldots>0\) |
| \(D_4\) | \(0.000003827471367568\ldots>0\) |
| **\(D_5\)** | **\(-1.847237\times10^{-9}<D_5<-1.847235\times10^{-9}<0\)** |

The analytic truncation bound can be checked without trusting an undocumented empirical cutoff: for \(0\le u\le0.21\) and \(n\ge51\), the absolute summand is at most \(200n^4e^{-3n^2}\), using \(\pi>3\), \(\pi^2<10\), \(e^{1.89}<7\), \(e^{1.05}<3\). Consecutive majorant terms shrink by a factor less than \(1/2\) for \(n\ge51\), hence the tail is less than \(400\cdot51^4e^{-3\cdot51^2}<10^{-70}\). Input arguments are the exact rational decimals \(|1+5j|/100\), not binary floating-point approximations. This computation rests on mpmath 1.3.0's stated interval rounding implementation; it is an independently reproduced **computational certificate**, not Lean-checked and not external peer review.

**New exact observation for this project's tested mechanism (elementary and not claimed literature-novel):** For any real \(\alpha\), let \(K_\alpha(v)=e^{\alpha v}K(v)\). For any ordered tuples \(x_i,y_j\),

\[
\det[K_\alpha(x_i-y_j)]
=\exp\!\left(\alpha\sum_i x_i-\alpha\sum_jy_j\right)\det[K(x_i-y_j)].
\]

The multiplier is strictly positive. In our Toeplitz configuration, \(\det[K_\alpha(u_0+(i-j)h)] =e^{r\alpha u_0}D_r\). The normalized thermal density \(d\mu_\sigma\) merely introduces an additional strictly positive factor \((\int K e^{\alpha v}dv)^{-r}\). **Therefore this actual-kernel PF5 obstruction persists for every real \(\sigma\), not just \(\sigma=1/2\)**. No choice of physically legitimate exponential Gibbs tilt can turn this continuous theta kernel into PF5 or PF∞.

A further logical caution: continuous-kernel PF∞ is **stronger than, and different from**, hyperbolicity of the correct factorial-normalized Jensen polynomials of Xi. By Schoenberg's characterization, for an integrable PF∞ kernel, the reciprocal of its bilateral Laplace transform has an entire Laguerre–Pólya extension. Here the transform is entire and has **known real-frequency Fourier zeros** (the established critical-line Xi zeros), so PF∞ of this particular full kernel would already be incompatible with existing known zeros, even if RH were true. Its failure is **not evidence against RH**. The PF5 witness supplies a finite-order classification, not a necessary condition for RH. Never conflate kernel Toeplitz minors with Xi coefficient Toeplitz/Jensen minors.

## 3. Bounded falsification verdict and exact stop gate

**What is established (with stated analytic/implementation dependencies):**

1. Genuine prime Gibbs characteristic/positive definite structure exists for \(\sigma>1\); it **cannot** be analytically continued as a probability state to any fixed \(1/2<\sigma<1\) (Voronin universality, no RH).
2. Genuine completed Xi, by contrast, has normalized positive-definite vertical time slices for **all real** \(\sigma\), with unconditional Gram inequalities and a strict \(|\xi(\sigma+it)|<\xi(\sigma)\) bound for \(t\ne0\). These are theta-kernel consequences, not RH claims.
3. The actual theta kernel's negative PF5 Toeplitz determinant was **independently recomputed with interval arithmetic and an exact-rational cross-check**. Exponential tilting cannot alter its sign. This is an explicit no-go for one natural Lee–Yang/total-positivity lifting strategy.

**Not established:** Any lower bound on \(|\xi(\sigma+it)|\) for nonzero time, horizontal growth positivity of \(\xi\), exclusion of even one hypothetical off-critical zero, or an improved zeta zero-free strip. The contrast between zeta and xi positivity does **not** produce a bridge carrying the prime Euler product into the critical strip as a positive thermal state. We do not promote the published PF5 preprint into an RH disproof, nor assume its withdrawn v1 theorems.

**Lean/Codex status:** Lean 4 is not installed in this execution container. No Lean declarations were compiled; no custom axioms, `sorry`, or fake formal proof were used. Finite determinant signs were tested instead with interval arithmetic and separate exact rational algebra. No Codex run is justified: no independent arithmetic theorem candidate remains that could now exclude a nonreal Xi zero. Continue only when a **specified phase-sensitive arithmetic estimate for the actual Xi/primes** survives a new falsification gate; do not restart heat lifetime constant tuning, raw moments, global kernel PF∞, or unrestricted Weil operator norms.

## 4. Primary references and reproducibility

- Project master handoff: `Project_Riemann_Complete_Handoff_20261019.zip`, especially `01`–`08`, `CLAIM_REGISTER.csv`, and the full theta normalizations.
- Original project nature audit: `project_riemann_nature_20261019/NATURE_HEAT_FLOW_AUDIT.md`; theta/Jensen audit: `project_riemann_theta_jensen_audit_20261019/THETA_MOMENT_STABILITY_AUDIT.md`.
- S. M. Voronin, *Theorem on the “universality” of the Riemann zeta-function*, Math. USSR Izvestiya 9 (1975), 443–453: https://www.mathnet.ru/eng/im2037.
- S. M. Voronin theorem applications, Sourmelidis & Steuding (2023), arXiv:2306.00460: https://arxiv.org/abs/2306.00460.
- W. Michałowski, *Certified Failure at Order Five*, **v2**, https://arxiv.org/html/2602.20313v2; direct PF5 Theorem 1.1, Section 4; v1 asymptotic threshold withdrawn in §5.
- Schoenberg's PF∞ reciprocal-transform theorem is summarized (with original primary references) in Michałowski v2 §1.2; apply strictly to the **continuous kernel**, not Xi Jensen-coefficient sequence.
- A. Grigutis and L. Turčinskas, *Note on the positivity of the real part of the log-derivative of the Riemann ξ-function near the critical line*, https://arxiv.org/html/2509.18963, Theorem 6 bounds only the sum from *critical-line zeros*; it cannot independently control the off-line contribution.

Reproducer: `check_tilted_theta_pf.py` (bounded single-configuration check, not a search). Reproduces PF2/PF3/PF4/PF5 signs and independently verifies the determinant signs using exact `Fraction` arithmetic from outward-rounded interval entries. All old workspaces are read-only for this investigation; output files are located only in this new directory.
