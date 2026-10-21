> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `fcc85852fec5c80c5723b7a2c6ab683f461b9ec393d4bf32f6b632dad37cabd5`.

# Project Riemann — new candidate theorem: transfer of unconditional simple-real-zero density to theta truncations

Date: 2026-10-18. Classification: **NEW WRITTEN THEOREM CANDIDATE, PROVED CONDITIONALLY ON EXPLICIT CLASSICAL ANALYTIC INPUTS AND THE PUBLISHED LAMZOURI THEOREM; NOT LEAN-CHECKED OR EXTERNALLY REFEREED. NO RH PROOF.** The numerical proportions below belong to published zeta research; possible novelty is their uniform transfer to the actual Haglund truncations and deformations. No literature-novelty claim is made.

## A. Exact statement and definitions

Use the preserved Riemann/Haglund normalization

\[
 \Xi(z)=\xi(1/2+iz),\quad h_n(u)=\pi n^2e^{5u/2-\pi n^2e^{2u}}(2\pi n^2e^{2u}-3),
\]
\[
 \Phi_n(z)=4\int_0^\infty h_n(u)\cos(zu)\,du,\qquad
 F_{j,v}(z)=\sum_{n=1}^j\Phi_n(z)+v\Phi_{j+1}(z),\quad j\ge1,\ 0\le v\le1.
\]

For a regular positive height R, let \(Z_{j,v}(R)\) be the multiset of zeros (counted with multiplicity) of \(F_{j,v}\) in \(0<\Re z<R,\ |\Im z|<1/2\). Let \(M_{j,v}(R)\) be its total multiplicity; \(S_{j,v}(R)\) the number of its *simple, real* zeros; and \(D_{j,v}(R)\) the number of its *distinct* zeros.

**Candidate Theorem.** For every fixed \(0<b<4\), choose for each sufficiently large integer \(N\) a common regular height
\[
 R_N\in[bN^2,bN^2+1].
\]
It can be chosen independently of \(j,v\) such that simultaneously for **all** \(j\ge N-1\) and \(v\in[0,1]\):

1. \(M_{j,v}(R_N)=N_\zeta(R_N)\), with multiplicity.
2. With \(c_{\rm MT}=\frac12+\frac{1}{\sqrt2}\cot(1/\sqrt2)\),
\[
 \liminf_{N\to\infty}\;\inf_{j\ge N-1,\ v\in[0,1]}
 \frac{S_{j,v}(R_N)}{M_{j,v}(R_N)}\ \ge\ 2-c_{\rm MT}
 =0.6725007036794116\ldots,
\]
\[
 \liminf_{N\to\infty}\;\inf_{j\ge N-1,\ v\in[0,1]}
 \frac{D_{j,v}(R_N)}{M_{j,v}(R_N)}\ \ge\ \frac32-\frac{c_{\rm MT}}2
 =0.8362503518397058\ldots.
\]

These are **asymptotic lower-density** statements, not effective starting thresholds. They leave up to 32.75% of zeros unaccounted for by the simple-real-zero conclusion. They do NOT establish zero-free expanding inner regions or Haglund zero-motion monotonicity.

## B. Published input (not our theorem)

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1 and Lemma 3.2, https://arxiv.org/html/2609.02882v1. It uses the unconditional Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh pair-correlation formula. For each epsilon>0 there is an even real nonnegative \(f=\eta^2\in C_c^\infty((-1/2,1/2))\), \(\int f=1\), such that \(K(w)=\int f(u)e^{-2\pi iwu}du\) and
\[
 Q_\Xi(T):=\sum_{\substack{0<\Re z_\rho,\Re z_{\rho'}\le T\\|\Im z_\rho|,|\Im z_{\rho'}|<1/2}}
 K\!\left(\frac{\log T}{2\pi}(z_\rho-z_{\rho'})\right)^2
 =\left(c_f+O_f((\log T)^{-1/2})\right)\frac{T}{2\pi}\log T,
 \quad |c_f-c_{\rm MT}|<\varepsilon.
\]
Here \(z_\rho=-i(\rho-1/2)\) for each nontrivial zeta zero \(\rho\), positive imaginary part of \(\rho\), and multiplicities in the double sum; K is even, making the sign convention immaterial. For any finite conjugation-invariant multiset \(Z\) of complex numbers and this K, Lamzouri Proposition 2.1 states
\[
 S(Z)\ge2|Z|-\sum_{z,w\in Z}K(z-w)^2,\qquad
 D(Z)\ge\tfrac32|Z|-\tfrac12\sum_{z,w\in Z}K(z-w)^2.
\]
This is a rigorous *published* input, but has not been independently rebuilt in this session.

## C. Tail and contour setup — one check requiring independent audit

The October-18 consolidated theta estimates give uniformly in \(j\ge N-1\), \(v\in[0,1]\), and \(|\Im z|\le1/2\):
\[
 |F_{j,v}(z)-\Xi(z)|\le64N^2e^{-\pi N^2};
\]
by the same positive kernel majorants with an extra factor u, the derivative discrepancy is \(O(N^C e^{-\pi N^2})\) for an absolute C. The important feature is uniformity in both \(j,v\), not the polynomial prefactor.

Select \(R_N\in[bN^2,bN^2+1]\) using the classical good-ordinate lemma, away from zeta ordinates by \(\gg1/\log R_N\). Riemann–von Mangoldt implies only \(O(\log R_N)\) zeros within height one. The standard local partial-fraction/logarithmic lower bound then gives, *uniformly along the right vertical segment* and the zero-free horizontal boundaries, for the rectangle \(D_N=\{0<\Re z<R_N,\ |\Im z|<1/2\}\):
\[
 \min_{\partial D_N}|\Xi(z)|\ge
 \exp\left[-\frac{\pi R_N}{4}-C\log^2(3+R_N)\right].
\]
At left x=0, \(\Xi(iy)=\xi(1/2-y)>0\); at y=\pm1/2, no zeros follow from the known zero-free lines Re(s)=0,1. Standard logarithmic-derivative bounds on these contours give \(\sup_{\partial D_N}|\Xi'/\Xi|\ll\log^C R_N\), with C absolute; or use local Cauchy estimates and a narrow zero-free neighborhood. These good-ordinate and log-derivative assertions are the **main technical verification gate**: cite exact classical lemmas and show the corner/near-boundary behavior, rather than silently assuming a lower bound.

As b<4, uniformly on \(\partial D_N\),
\[
 \left|\frac{F_{j,v}-\Xi}{\Xi}\right|+
 \left|\frac{F_{j,v}'}{F_{j,v}}-\frac{\Xi'}\Xi\right|
 \ll \exp[-c_bN^2]
\]
for some c_b>0 after absorbing the polynomial/subexponential factors. Hence all the F are boundary-nonzero and Rouche gives exactly \(N_\zeta(R_N)\) enclosed zeros, for all j,v.

## D. The novel step: transferring the entire quadratic pair statistic, not individual roots

For each fixed admissible f and T=R_N define
\[
 \mathscr K_T(z,w)=K\left(\frac{\log T}{2\pi}(z-w)\right)^2,
\]
a function entire in z and w. The argument principle *twice*, including multiplicity, gives the exact formula
\[
 \boxed{\quad Q_F(T)=\frac1{(2\pi i)^2}
 \oint_{\partial D_N}\oint_{\partial D_N}
 \mathscr K_T(z,w)\frac{F'(z)}{F(z)}\frac{F'(w)}{F(w)}\,dw\,dz.\quad}
\]
Importantly, it has **no singularity at z=w**, so no separation of zeros, root matching or simplicity hypothesis enters.

Because \(f\ge0\), \(\int f=1\), and \(|\Im(z-w)|\le1\) on the boundary,
\[
 |K(\tfrac{\log T}{2\pi}(z-w))|\le T^{1/2},\qquad
 |\mathscr K_T(z,w)|\le T.
\]
The contour has length O(T). The logarithmic derivatives on its boundary are polynomially bounded; their difference is \(e^{-c_bN^2}\). Therefore uniformly for all \(j\ge N-1,v\in[0,1]\),
\[
 |Q_{F_{j,v}}(R_N)-Q_\Xi(R_N)|\ll
 R_N^C e^{-c_b N^2}=o(1),
\]
for a fixed admissible f. This is much stronger than the o(N_zeta) required by Lamzouri's finite-multiset inequality.

Apply Lamzouri's bounds to the finite conjugation-invariant zero multiset of \(F_{j,v}\). Since its count equals \(N_\zeta(R_N)\) by Rouche, and since the transferred quadratic statistic has the same first-order limit as Xi's, the candidate theorem follows by fixing epsilon and letting epsilon decrease *after* taking N to infinity.

## E. Adversarial tests and proof limits

- **Zero collisions / exponential clustering:** No root-by-root matching is used. The double-contour statistic is holomorphic and counts multiplicities automatically. E.g. zeros of \(z^2\) can split to \(\pm i\sqrt\epsilon\); the pair statistic remains continuous and the simple-real lower bound does not falsely force either perturbed root to be real.
- **Off-real zeros of finite truncations at unbounded |Im z|:** They are outside the fixed critical-height rectangle. The theorem does not claim all truncation zeros real.
- **Uniformity in deformation t, later j:** Follows if the archived value and first-derivative tail bounds hold uniformly for j>=N-1 and t∈[0,1]. Must rederive derivative uniformity rather than simply quote the value bound.
- **Endpoint choice:** Choose one common R_N after the good-ordinate argument; it cannot depend on t. Vertical-side lower bound and interior zero count must include multiplicity.
- **Fixed b<4:** Essential for the exponential gap. The argument does not establish a uniform result at b=4 or beyond.
- **Arithmetic novelty:** The >67.25% constant is NOT ours. What appears potentially new is its quantitative-uniform transfer to the actual Haglund truncations/deformations, improving the earlier lower bound of roughly N^(1−delta) distinct real zeros to a fixed proportion of ~N²log N total zeros in a quadratic window. The literature search so far did not identify this particular transfer, but no novelty claim has been established.
- **Proof-critical limits:** This leaves an O(N²log N) population that could be nonreal. It does not close the <2 integer gap or any RH-equivalent shrinking-floor exclusion. It is genuinely new information *about the approximating family*, not a new zero-location theorem for genuine zeta beyond the published input.
- **Formal status:** No local Lean toolchain was available this session. Published Lamzouri finite-multiset inequality is separately reported formally checked; our analytic bridge was NOT Lean-compiled.

## F. Decision

This is worthy of **one bounded independent Codex/Lean audit**, focused exclusively on (i) the good-ordinate uniform min-modulus/log-derivative gate, (ii) exact double contour normalization and uniform exponential error, and (iii) source/literature novelty. No broad parameter sweep, no new countermodels, no changes to earlier files or historical Git refs. If the technical gate fails, reject the theorem immediately. Preserve all original Project Riemann evidence and BLOCKED_UNWAIVED. RH remains unproved and full k=2/k=3 verification remains UNVERIFIED.
