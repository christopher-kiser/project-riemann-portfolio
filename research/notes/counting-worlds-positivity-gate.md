> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `c86cde7169a257629614234662ad3141568f0eda0442351edf650a427875e71b`.

# Project Riemann — Counting Worlds, Geometry, and Positivity Gate

**Date:** 2026-10-20. **Outcome:** `EXACT_ELEMENTARY_COUNTERMODEL / GEOMETRIC_POSITIVITY_GATE_IDENTIFIED / NO_NEW_RH_FRONTIER_ADVANCE`.

## Research question

Does the nested prime-index viewpoint generalize to other counting worlds, and can the similarities tell us what a proof of an RH-type theorem needs? Specifically, are positive point counts, prime-orbit decompositions, functional-equation symmetry, and scale hierarchy sufficient to force zeros to a critical line? This was tested using an explicit constructed counting system and an independent graph spectral counterexample. It does **not** establish a mathematical discovery new to the literature.

## 1. Established proofs: where the difficult input actually enters

For an elliptic curve E/F_q, Frobenius has characteristic polynomial X^2-aX+q and gives exact counts N_n=q^n+1-alpha^n-beta^n. The **additional geometric fact** is that degree is a nonnegative quadratic form on endomorphisms:

    deg(m * id - n * Frob) = m^2 - a*m*n + q*n^2 >= 0

for all integers m,n, and hence all rational slopes m/n. Its discriminant therefore is nonpositive, a^2<=4q, forcing |alpha|=|beta|=sqrt(q). This nonnegative norm is not a consequence of mere positivity of N_n.

Reference: Andrew Sutherland, MIT 18.783 Lecture 8, Hasse's theorem: https://math.mit.edu/classes/18.783/2015/LectureNotes8.pdf

## 2. A fully explicit counting world that passes the easy tests but violates RH

Fix q=5, a=5. Define alpha,beta=(5 +/- sqrt(5))/2, so alpha+beta=5, alpha*beta=5 and 1<beta<2<alpha<4<5. Define

    Z(T) = (1-5T+5T^2) / ((1-T)(1-5T)),
    N_n = 5^n+1-alpha^n-beta^n.

Because a_0=2, a_1=5, a_n=5a_(n-1)-5a_(n-2), all N_n are integers. Direct substitution gives

    Z(T) = exp(sum_(n>=1) N_n*T^n/n)

as formal power series and for |T| small. The numerator and denominator both satisfy F(1/(5T))=F(T)/(5T^2), hence **Z(1/(5T))=Z(T)**. Setting T=5^{-s} gives the symmetry s <-> 1-s.

Define primitive-orbit multiplicities

    b_n = (1/n) * sum_(d|n) mu(n/d)*N_d.

Every b_n is an integer: the formal series Z(T) has constant coefficient 1 and integer coefficients, so it has a unique integer Euler-transform factorization Z(T)=product_(n>=1)(1-T^n)^(-b_n). Taking logarithms and applying Möbius inversion gives the formula above. Prove **strict positivity for every n**:

- b_1=N_1=1; b_2=(N_2-N_1)/2=(11-1)/2=5.
- For n>=3, alpha<4 and beta<2 imply

      N_n > 5^n-4^n-2^n >= (53/125)*5^n.

- Every proper divisor d of n satisfies d<=n/2, N_d>0, and N_d<5^d+1<=5^(n/2)+1. There are fewer than n such divisors.
- Thus

      n*b_n >= N_n - sum_(proper d|n) N_d
            > (53/125)*5^n - n*(5^(n/2)+1) > 0.

  The last inequality for n>=3 follows because n/5^(n/2)+n/5^n is decreasing for n>=3 and at n=3 is <3/10+3/125=0.324<53/125=0.424. Hence b_n>0 for **all n**.

Interpretation: a disjoint union of exactly b_n directed cycles of length n defines a countable discrete dynamical system with precisely N_n points fixed by the nth iterate. Thus the model has a genuine positive prime-orbit Euler product, positive periodic-point counts at all depths, leading count 5^n, and the prescribed functional equation. It is **not** asserted to be a finite-field algebraic curve, smooth compact system, or a faithful model of the Riemann zeta function.

Yet numerator roots are 1/alpha and 1/beta: setting T=5^{-s}, the zeros have real parts log_5(alpha)=0.7989937178... and log_5(beta)=0.2010062822..., paired by reflection and off the critical line 1/2. The geometric degree polynomial the system would need is Q(m,n)=m^2-5mn+5n^2; it violates positivity already at Q(2,1)=**-1**. This falsifies the proposition that positive hierarchical counts + prime-orbit Euler product + rationality + reflection alone imply an RH-type statement.

The constructed countermodel may be elementary/known in related dynamical zeta literature: **literature novelty not established**.

## 3. Independent graph test: even a self-adjoint operator isn't enough

Let G have 14 vertices: take two disjoint K_7 graphs, remove edge (0,1) from the first and (7,8) from the second, then add cross edges (0,7) and (1,8). G is connected, undirected, simple and 6-regular. Its adjacency matrix A is real symmetric and thus self-adjoint. Set v_i=+1 for first K_7 vertices, v_i=-1 for second. Then v is orthogonal to the constant vector and

    (v^T A v)/(v^T v) = 76/14 = 38/7 > 2 sqrt(5).

Therefore, the nontrivial adjacency eigenvalue lambda_2 >= 38/7 exceeds the Ramanujan bound for a (q+1)-regular graph with q=5. The nontrivial Ihara zeta poles arising from 1-lambda_2*u+5*u^2 consequently are **off** the circle |u|=5^{-1/2}. Graphs have honest nonnegative primitive-cycle counts, an Ihara zeta Euler product and a self-adjoint adjacency operator, but self-adjointness and counting are not enough to imply the graph RH analogue. (The trivial adjacency eigenvalue 6 is excluded; G is connected, and v is orthogonal to its eigenspace.)

Reference: Rangarajan, *A Combinatorial Proof of Ihara-Bass's Formula for the Zeta Function of Regular Graphs*, FSTTCS 2017: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2017.46; Lubotzky, *The Ramanujan conjecture and its applications*: https://pmc.ncbi.nlm.nih.gov/articles/PMC6939229/.

## 4. Adversarial conclusion for Project Riemann

- `PROVED_WITH_STATED_CLASSICAL_INPUTS`: Point-count/degree positivity distinction; fake system's exact integer positive orbit counts at all n and offcritical zeta zeros; explicit graph Rayleigh witness. These are elementary proofs with standard Hasse and Ihara-Bass sources, not new zeta results.
- `FALSIFIED`: Universal RH from counting hierarchy, growth, Euler product, reflection, and positive counts; RH from spectral self-adjointness alone.
- `MISSING`: An **independent** arithmetic-geometric positivity or spectral *bound* for the actual Riemann Xi function that is not imported from a known RH-equivalent criterion.
- `EQUIVALENCE TRAP`: Connes–Consani–Marcolli (2007) shows a number-field trace positivity formulation equivalent to RH. Stating this positivity is not proving it. https://arxiv.org/abs/math/0703392
- `FUTURE PROOF-CRITICAL TEST`: Any proposed prime-index renormalization pairing must (i) be canonically built from genuine prime arithmetic without RH assumptions; (ii) be shown nonnegative by an independent structural argument rather than simply defined as a Gram square; (iii) provably correspond to the *signed* Weil explicit formula or Xi zeros; and (iv) reject the explicit fake counting system above and the non-Ramanujan graph. Without all four, do not launch Codex or label an RH advance.

## 5. Reproduction and preservation

The accompanying `verify_counting_worlds.py` uses only Python's standard library. It checks all periodic point/primitive orbit identities through n=40 with exact integers, the toy symmetry and negative fake degree certificate, direct F5 enumeration on a genuine curve, and the graph's exact rational Rayleigh quotient and connectivity. The all-n positivity and spectral exclusion are analytic/exact proofs above, not inferred from 40 instances. Original project files remain unchanged.

`Lean`: Not installed/available in this environment, no Lean certification claimed. `Codex`: Not launched. RH open; Haglund k=2/k=3 full verification unverified; prior moment estimate `BLOCKED_NEW_MOMENT_ESTIMATE`; provenance `BLOCKED_UNWAIVED`.
