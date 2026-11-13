# Project Riemann — geometric unfolding and xi-positivity audit

**Research date:** 2026-11-07  
**Classification:** published-source deduction + exact synthetic falsification; **NO_NEW_RH_FRONTIER_ADVANCE**  
**Research direction:** Christopher Kiser; mathematical derivation and checks with AI assistance.  
**Scope:** an exploratory continuation inspired by complex transformations in the reconstruction of Escher's *Print Gallery*. No claim of originality in the mathematical literature.

## 1. Question and exact transformation

For the completed zeta function

\[
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad c_0=\xi(1/2)>0,
\]

let

\[
h(u)=\xi(1/2+\sqrt{u})/c_0.
\]

This is entire: \(\xi(1/2+z)\) is even, and so is an entire function of \(u=z^2\). Riemann's hypothesis is equivalent to all zeros of \(h(u)\) being negative and real. The target condition is that \(R(u)=h'(u)/h(u)\) be holomorphic and map the upper half-plane into the lower half-plane. This reformulation does not by itself prove RH.

Suvrit Sra, *On some positivity properties of the Riemann Xi function*, arXiv:2611.02944v1 (2026-11-02), proves substantial unconditional but finite positivity statements about reciprocal-xi transforms; complete monotonicity and all-order total positivity remain RH-equivalent. The paper is a recent preprint, not an independently certified solution. See https://arxiv.org/abs/2611.02944 and its Proposition A.1.

## 2. Source-dependent sign corollary on a half-plane

Use the notation of Sra's §§2–3. Put \(q=\gamma_1^2\), with \(\gamma_1\) the lowest positive zeta-zero ordinate and \(m_1\) its multiplicity. The cited paper establishes

\[
R(u)=\int_0^\infty e^{-ut}H(t)\,dt
\quad(\Re u>-q),
\]

and in its equation (3.1) proves

\[
J(t)=e^{qt}(H(t)-m_1 e^{-qt})>0,\quad J'(t)<0\qquad(t>0).
\]

**Deduction (conditional on the cited paper's established premises).** For \(\Re u>-q\) and \(\Im u>0\),

\[
\boxed{\Im R(u)<0.}
\]

Indeed, write \(u=x+iy\) with \(x>-q\). Then

\[
g_x(t)=e^{-xt}H(t)=e^{-(x+q)t}[m_1+J(t)]
\]

is strictly positive, strictly decreasing and integrable. A positive, strictly decreasing integrable function has a strictly positive sine transform at every frequency \(y>0\). One elementary proof divides the sine integral into successive positive/negative half-periods and pairs the integrals: on each paired interval the positive-half integrand is strictly larger. Hence

\[
\Im R(x+iy)=-\int_0^\infty g_x(t)\sin(yt)\,dt<0.
\]

This half-plane stops at the first real pole, \(u=-q\). To reach the entire upper half-plane one needs genuinely additional global structure, not merely the above monotonicity. This corollary is not claimed to be first-in-literature or to exclude any previously unverified zero. Its proof imports Sra's source result; that analytic source was read but not independently refereed or reproduced here.

## 3. Fully elementary synthetic counterexample: positivity does not force real zeros

Define distinct rational rates \(a_j=1+j/100\) (\(j=0,\dots,7\)) and the normalized polynomial

\[
p(u)=\frac{\left(\prod_{j=0}^7 (u+a_j)\right)[(u+2)^2+9]}{\left(\prod_{j=0}^7 a_j\right)13}.
\]

It is positive at every real \(u\geq0\), has eight simple negative real zeros and two nonreal zeros \(-2\pm3i\). Its logarithmic derivative is

\[
\frac{p'(u)}{p(u)}=\sum_{j=0}^7\frac1{u+a_j}+\frac1{u+2-3i}+\frac1{u+2+3i}.
\]

The inverse Laplace kernel of this derivative is

\[
H_*(t)=\sum_{j=0}^{7} e^{-a_jt}+2e^{-2t}\cos(3t).
\]

For all \(t\ge0\), the inequalities

\[
H_*(t)\ge 8e^{-1.07t}-2e^{-2t}>0
\]

and

\[
-H_*'(t)\ge 8e^{-1.07t}-2\sqrt{13}\,e^{-2t}>0
\]

follow from \(a_j\in[1,1.07]\) and \(8>2\sqrt{13}\). However the next sign fails exactly:

\[
H_*''(0)=\sum_{j=0}^7 a_j^2+2(2^2-3^2)
=\boxed{-713/500}.
\]

A direct upper-half-plane witness is \(u_*=-2+29i/10\), for which

\[
\Im\frac{p'(u_*)}{p(u_*)}=
\frac{60430254355211422137113494640862546}{8225185041587396199596947465865015}
>0\quad(\text{approximately }7.3469781).
\]

Thus even \(H>0\) and \(H'<0\) globally, and positivity of \(p\) on the positive axis, are insufficient for the global Pick condition or negative-real-zero property. This is a **synthetic** polynomial, not the Riemann xi function. Its nonreal poles do not match the exact zeta critical-strip placement; a more geometry-compatible family is noted below.

## 4. Any finite number of alternating derivative tests can be spoofed

**Elementary obstruction theorem.** Given any integer \(m\ge0\), put

\[
K=\sqrt{404},\quad A_m=\lfloor2K^m\rfloor+2,\quad
H_m(t)=A_m e^{-t}+2e^{-2t}\cos(20t).
\]

For every \(t\ge0\) and every integer \(0\le k\le m\),

\[
(-1)^kH_m^{(k)}(t)
\ge A_m e^{-t}-2K^k e^{-2t}
\ge (A_m-2K^m)e^{-t}>0.
\]

Yet if \(\theta=\arctan(10)\), choose \(t_m\in[0,\pi/10)\) such that

\[
\cos(20t_m-(m+1)\theta)=-1.
\]

Then

\[
(-1)^{m+1}H_m^{(m+1)}(t_m)
=e^{-2t_m}\left[A_m e^{t_m}-2K^{m+1}\right]<0.
\]

The final inequality holds because \(e^{t_m}<e^{\pi/10}<2\), \(A_m\le2K^m+2\le4K^m\), and \(K>4\). The corresponding normalized polynomial

\[
p_m(u)=\frac{(u+1)^{A_m}[(u+2)^2+400]}{404}
\]

has nonreal zeros \(-2\pm20i\). Therefore **no fixed finite number of all-domain alternating derivative-sign checks on a generic Laplace kernel implies its generating polynomial has exclusively real zeros**.

This general construction uses repeated negative real roots for convenience; the distinct-real-root example above avoids that simplification at order 1.

**Critical-strip-shaped variant (scope check).** Choose any real \(q>0\), real \(\Gamma>0\) and \(0<\delta<1/2\) with \(a=\Gamma^2-\delta^2>q\). Let \(\lambda=(\Gamma-i\delta)^2=a-2i\Gamma\delta\). For every fixed \(m\), choose an integer \(A>2(|\lambda|/q)^m\) and define

\[
\widetilde H_m(t)=A e^{-qt}+e^{-\lambda t}+e^{-\bar\lambda t}.
\]

Then \((-1)^k\widetilde H_m^{(k)}(t)>0\) for every \(t\ge0\) and \(0\le k\le m\), by the same modulus comparison, despite nonreal zeros \(-\lambda,-\bar\lambda\) of the associated polynomial. These complex zeros correspond, under the squared transformation, to hypothetical zeta-type points with \(\Re s=1/2\pm\delta\) and \(|\Im s|=\Gamma\). This shows that the *strip-shaped geometry alone*, without the actual xi-specific theta/arithmetic constraints, does not repair the finite-order logical gap. This is not a construction of off-line zeros of actual zeta.

## 5. Implications for the research program

1. **Retain as a verified finite obstruction:** synthetic exact algebra (\(H''_*(0)\), off-axis zeros, exact Pick witness), global inequality proofs, and written all-\(m\) construction. Wolfram checked the root and derivative identities; a separate standard-library Python checker reproduces exact rational witnesses. Numeric demonstrations for \(m=0\dots6\) are diagnostics only.
2. **Retain as a source-dependent mathematical deduction:** half-plane Pick sign \(\Re u>-\gamma_1^2\), using Sra (2026) eq. (3.1). This is not a verified extension beyond the previously known zero-free region.
3. **Reject as proof strategies:** checking finitely many derivatives, finite PF orders, or using positivity/decrease of \(H\) alone as though that implied complete monotonicity or RH.
4. **Still missing:** an unconditional all-order theta-specific estimate or independently justified analytic continuation/zero-exclusion mechanism across the entire negative real-axis pole sequence. A direct Pick sign proof for all \(\Im u>0\) remains RH-equivalent, not a solved lemma.
5. **Separate unresolved obligations:** marked-inverse \(r+2z<1\to r+z<1\) is still `BLOCKED_NEW_MOMENT_ESTIMATE`; complete Haglund \(k=2/k=3\) remains `UNVERIFIED`; historical provenance remains `BLOCKED_UNWAIVED`. The Nov. 1 fixed-node Xi/Pick/Loewner certificates are not altered by this work.

**Scientific verdict:** `NO_NEW_RH_FRONTIER_ADVANCE`. No zeta counterexample, no RH proof, no extension of a certified zero-free region, no completion of the marked inverse estimate.

## 6. Verification, provenance, references

- **Tool run:** Wolfram Language evaluated the elementary polynomial roots, Laplace/log-derivative identity, \(H''_*(0)\), exact rational Pick witness, and \(m=1,2,3\) numerical finite-order witnesses. One additional Wolfram check returned a symbol-warning even though its rational outputs were independently matched; the warning is not hidden.
- **Independent replay:** `scripts/check_xi_positivity_obstruction.py` (Python standard library) uses exact `fractions.Fraction` for the rational findings and integer checks for the universal comparison; its float-based \(m\)-witness loop is explicitly diagnostic.
- **Not run:** Lean compilation, Arb/interval certification for the actual xi function, hosted CI, mathematical referee review, and any high-zero computation.
- **Primary recent source:** Suvrit Sra (2026-11-02), *On some positivity properties of the Riemann Xi function*, https://arxiv.org/abs/2611.02944; especially Theorem 1.1, Proposition 3.2 (3.1), Proposition A.1. Source results are attributed, not claimed as Project Riemann discoveries.
- **Background:** Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function in the Hermite, Meixner-Pollaczek, and continuous Hahn bases*, https://www.math.ucdavis.edu/~romik/data/uploads/papers/riemannxi-final.pdf. Reference explains the classical theta-kernel and Fourier-transform program.
- **Internal lineage:** `docs/continuations/2026-11-01-round11.md`, `docs/research-status.md`, `docs/research-maintenance.md`, and the earlier marked-inverse case study. This note does not supplant or overwrite any previous certificate.