> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `a2e42cd8bd07d317fd787385c15bbc45f916583d69b892e0a15d6812a017c57f`.

# Project Riemann — Prime gas, orthogonality catastrophe, Dickman critical scaling, and the phase-winding obstruction

**Checkpoint:** 2026-10-19 (US/Eastern). **Verdict:** `PHYSICAL_CRITICALITY_EXACT_WITH_CLASSICAL_INPUTS / FREE_PRIME_MODEL_CLOSED_AS_RH_ROUTE / NO_NEW_RH_FRONTIER_ADVANCE`.

**Claims discipline:** The Hamiltonian construction and displayed deductions are independently derived **in this investigation** using classical number theory, Hilbert space, and complex analysis. This does **not** establish global novelty or mathematical priority. The scale-invariant Poisson/Dickman law is classical; related applications to multiplicative models and smooth numbers already appear in the literature. Numerical checks are not proofs. No imaginary off-line zeta zero is constructed or excluded. Historical Haglund k=2/k=3 verification remains `UNVERIFIED`, marked-inverse moment remains `BLOCKED_NEW_MOMENT_ESTIMATE`, and historical provenance remains `BLOCKED_UNWAIVED`. No prior evidence edited.

## 1. The exact full-prime-power quantum model

For each prime p take the Hilbert space H_p = l²(N_0) with occupation-number operator N_p |k> = k |k>. Let sigma>0. The normalized local vector is

    |psi_{p,sigma}> = sqrt(1-p^{-2sigma}) * sum_{k>=0} p^{-sigma*k} |k>.

The finite-cutoff state is the tensor product over p<=X, and the finite Hamiltonian is

    H_X = sum_{p<=X} (log p) N_p.

H_X is self-adjoint (with its natural occupation-number domain); U_X(t)=exp(-itH_X) is unitary. Its energies are log n for X-smooth positive integers n, including all prime powers. The normalized Loschmidt amplitude is **exactly**

    A_{X,sigma}(t) = <Psi_{X,sigma}|U_X(t)|Psi_{X,sigma}>
                   = product_{p<=X} (1-p^{-2sigma})/(1-p^{-2sigma-it})
                   = zeta_X(2sigma+it)/zeta_X(2sigma),

where zeta_X(s)=product_{p<=X}(1-p^{-s})^{-1}. This is the ordinary truncated Euler product, not the analytically continued full Riemann Xi function. The corresponding probability law gives each X-smooth integer n mass proportional to n^{-2sigma}.

Write alpha=2sigma. Hilbert-space normalization for the **full infinite prime excitation** is possible in the vacuum Fock sector precisely when sum_p p^{-alpha} converges, i.e. alpha>1. Equivalently sigma>1/2. At alpha=1, the finite vacuum-state overlap obeys

    |<Omega|Psi_{X,1/2}>|² = product_{p<=X}(1-1/p)
                               ~ e^{-EulerGamma}/log X -> 0.

(The vacuum overlap is positive, so its magnitude is the positive square root.) This is the orthogonality-catastrophe boundary of this *specific* independent-mode construction. It does not establish a physical realization of Xi's zeros.

## 2. Sharp fixed-time phase transition

**Theorem 1 (classical-input proof).** For any fixed real t != 0, as X grows:

- If sigma>1/2, then A_{X,sigma}(t) -> zeta(2sigma+it)/zeta(2sigma), **nonzero**.
- If sigma=1/2, then

    (log X) A_{X,1/2}(t) -> exp(-EulerGamma) zeta(1+it),

  so the unscaled amplitude tends to zero at rate 1/log X; the limit constant is nonzero.
- If 0<sigma<1/2, then |A_{X,sigma}(t)| -> 0, with decay at least exp(-c_{sigma,t} X^{1-2sigma}/log X) for X large enough, for some c_{sigma,t}>0.
- At t=0 the amplitude is identically 1 for every X and sigma. Thus for sigma<=1/2 the pointwise real-time limit is 1 at t=0 and 0 at any fixed t !=0: not a continuous characteristic function, and not a normalizable limiting survival amplitude in one fixed Hilbert representation.

**Proof.** The first case follows from the absolutely convergent Euler product when alpha=2sigma>1. At alpha=1, the denominator zeta_X(1)=product_p(1-1/p)^-1 ~ e^gamma log X by Mertens. For fixed t!=0, the ordered product zeta_X(1+it) converges to zeta(1+it). This follows from the *strong* unconditional PNT error pi(x)-Li(x)=O(x exp(-c sqrt(log x))) and partial summation: sum_{p<=X}p^{-1-it} converges for t!=0 because its Li main term becomes the conditionally convergent integral int exp(-it v)/v dv, and its PNT error is absolutely integrable. All higher Euler-factor logarithm terms converge absolutely. Uniform convergence from Re(s)>1 identifies the boundary product with zeta(1+it). The classical zero-free line ensures its limit is nonzero.

For alpha<1, write q=p^{-alpha} and phi=t log p. The local factor satisfies

    |(1-q)/(1-q exp(-i phi))|²
     = [1+2q(1-cos phi)/(1-q)²]^{-1}.

Using log(1+x)>=x/(1+x) for x>=0 gives

    -log|A_{X,sigma}(t)| >= (1/4) sum_{p<=X}p^{-alpha}(1-cos(t log p)).

The PNT and partial summation imply, for alpha<1 and fixed t!=0,

    sum_{p<=X} p^{-alpha}(1-cos(t log p))
     = X^{1-alpha}/log X * [1/(1-alpha) - Re(X^{-it}/(1-alpha-it)) + o(1)].

The bracket is bounded below by the positive constant

    d(alpha,t)=1/(1-alpha) - 1/sqrt((1-alpha)^2+t²)>0.

This proves the stated decay (with any sufficiently small c). At alpha=1, the denominator Mertens behavior and conditional numerator limit give the sharper rate. □

**Interpretation.** Ordinary unitarity/normalization turns a prime amplitude p^{-sigma} into a *probability* p^{-2sigma}; hence the model's sharp Hilbert threshold is sigma=1/2. However the arithmetic zeta function entering the overlap is evaluated at **2sigma+it**, not at sigma+it. In its normalized domain it only reaches Re(s)>1, where Euler's product already guarantees zero exclusion. It cannot infer RH from that positivity.

## 3. A nontrivial critical scaling limit (Dickman law)

**Theorem 2 (quantitative classical-input proof).** For every fixed U<infinity, uniformly for real |u|<=U,

    A_{X,1/2}(u/log X)
      = D(u) + O_U(1/log X),

    D(u) = exp( int_0^1 (exp(-i u v)-1) dv/v ).

D(u) is the characteristic function of the **Dickman distribution**, the sum of the points of a scale-invariant Poisson process on (0,1] with intensity dv/v. It has density exp(-gamma)rho(y), where rho(y)=1 on [0,1], rho(y)=0 for y<0 and y rho'(y)=-rho(y-1) for y>1. The characteristic function D is zero-free (indeed the exponential of an entire function), and its distribution has mean 1 and variance 1/2.

**Proof.** Put L=log X, v_p=log p/L, and expand finite Euler factors using their absolutely convergent logarithms (for each finite X):

    log A_{X,1/2}(u/L)
      = sum_{p<=X} sum_{m>=1} (exp(-i u m v_p)-1)/(m p^m).

For |u|<=U, the m>=2 portion is O_U(1/L): because |exp(-i u m v_p)-1|<=U m v_p and sum_p log p/[p(p-1)] is finite. The first power gives

    S_X(u)=sum_{p<=X} [exp(-i u v_p)-1]/p
          = (1/L) sum_{p<=X} (log p/p) g_u(v_p),

    g_u(v)=[exp(-iuv)-1]/v, g_u(0)=-iu.

Classical Mertens yields B(z)=sum_{p<=exp(z)} log p/p = z+O(1), with an O(1) bound down to z=0. Stieltjes integration by parts then gives

    S_X(u)=int_0^1 g_u(v) dv+O_U(1/L),

uniformly for |u|<=U, since g_u and g_u' are uniformly bounded on [0,1]. Exponentiation gives the claimed amplitude convergence and O_U(1/L) error. The Poisson characteristic-function formula identifies the Dickman law, and differentiation gives E[Y]=int_0^1 dv=1 and Var(Y)=int_0^1 v dv=1/2. □

**What it means.** Fixing a nonzero observation time first produces complete dephasing. Scaling the time as 1/log X first produces a stable nonzero universal waveform. This is a rigorous order-of-limits/measurement-resolution phenomenon. It recovers a known multiplicative-number-theory limit, not RH. In particular D has no zeros, so the universal critical pattern itself **loses all information about individual nontrivial zeta zeros**. The zero-sensitive arithmetic lies in the non-universal finite-size corrections, where the issue of independently bounding signed cancellations reappears.

## 4. Direct zero-topology obstruction for actual zeta (and Xi)

The following unconditional no-go is not specific to the quantum gas; it formalizes the physical concept of *phase-winding charge*.

**Theorem 3 (Rouché obstruction).** Choose a closed disk D entirely inside 0<Re(s)<1, avoiding s=1, whose boundary has no zeta zero and whose interior contains at least one **known, genuine** nontrivial zeta zero. Such a disk exists unconditionally; no RH assumption is needed. Let m_D=min_{s in boundary D}|zeta(s)|>0. For any X and any holomorphic nonvanishing function C_X on a neighborhood of D, put G_X(s)=C_X(s) zeta_X(s), where zeta_X(s)=product_{p<=X}(1-p^{-s})^-1. Then

    sup_{s in boundary D}|G_X(s)-zeta(s)| >= m_D.

Thus no sequence of zero-free analytic local counterterms multiplied by finite Euler products can converge uniformly on D (or even approximate zeta on its boundary with error <m_D). This remains true after the nonvanishing gamma/s-completion needed to form Xi, on a disk avoiding the completion singularities and its trivial-factor zeros.

**Proof.** For Re(s)>0, |p^{-s}|<1, so each finite Euler product zeta_X is holomorphic and nonvanishing, and multiplication by a holomorphic nonvanishing C_X retains that property. If the displayed supremum were <m_D, Rouché's theorem would give G_X and zeta the same number of zeros in D, counted with multiplicities. But G_X has zero and zeta has at least one. Contradiction. □

Equivalently, the argument principle gives zero phase-winding on D for the finite multiplicative model, and nonzero winding for the actual zeta. A zero-free analytic normalization cannot change this topological index. Producing the genuine zeros requires either finite approximants that themselves acquire zeros (as coherent additive theta approximants may) or a limiting process that is not locally uniform. This is **not** a route to eliminating hypothetical off-line zeros: phase-winding conservation counts them; it does not independently pin their locations to the critical line.

## 5. Adversarial checks and relation to prior work

- The model includes **all prime powers**, not only squarefree states. The energy log n is exact for X-smooth integers.
- The global state is only a finite tensor product. Its infinite Fock-sector failure at sigma<=1/2 is **not** a theorem forbidding other interacting Hilbert constructions.
- The sigma=1/2 threshold is caused by squaring p^-sigma for probabilities, and the actual zeta argument becomes 2sigma+it. It must **not** be misrepresented as an independent restriction on a nontrivial zero at Re(s)=1/2.
- The Dickman law and scale-invariant Poisson interpretation are **known** from probabilistic number theory. The quantum presentation does not establish research priority.
- The uniform no-go is just the classical argument principle/Rouché; it rules out a *particular type* of zero-free renormalization. It is **not** an impossibility theorem against all spectral operators, canonical systems, or theta truncations.
- At fixed nonzero t, the limiting survival amplitude for sigma<=1/2 is discontinuous at t=0. Therefore it cannot be treated as a continuous normalizable characteristic function. A singular limiting state is **not a proof of RH**.
- Our prior exact theta approximants Xi_k converge locally uniformly to Xi and can have their own zeros: this is categorically different from multiplying zero-free local prime factors. Do not infer zero pinning from that distinction.
- Smooth-number expansions with corrections involving actual zeta zeros are a research topic (Gorodetsky 2023). A universal Dickman limit by itself cannot exclude even one hypothetical off-critical-line zero.
- No Lean 4 compiler was present in the execution environment; no Lean certification is claimed. No Codex campaign run and no historical evidence modified.

## 6. Finite reproducibility and limitation

`verify_prime_gas.py` independently computes finite normalized Euler products for all primes p<=1,000,000; a rational vacuum/partition identity for p<=19; fixed-time monotonicity samples; the scaled-time Dickman limiting characteristic function by numerical quadrature; and first two scaled-energy moments. `verification_log.txt` gives results. None of the numerics are used as proofs of asymptotics.

At sigma=1/2, t=1, x=1,000,000 the calculated amplitude magnitude is ~0.04753034, while the fixed-time theorem forces it to zero as x->infinity. With scaled time u=2 (t=2/log x) the amplitude magnitude at x=1,000,000 is ~0.42934844, near the analytically proved universal magnitude ~0.42853536. This contrast is the central diagnostic.

## 7. Relevant primary/authoritative sources checked

- Nature Communications (2026), *The Riemann Hypothesis manifested in dynamical quantum phase transitions*, engineered log n energies, without a proof of RH: https://www.nature.com/articles/s41467-026-74935-8 . Their models are **not** identical to our independent bosonic prime product.
- Arratia, Barbour, Tavaré, *The scale-invariant Poisson process and the Dickman distribution*, original paper copy: https://user.math.uzh.ch/barbour/pub/Barbour/ABT_PDScaleInvt.pdf . The explicit Poisson sum and Laplace transform show the classical limit.
- Gorodetsky, *Smooth integers and the Dickman rho function* (2023), corrections from actual zeta zeros: https://arxiv.org/abs/2211.08973 .
- DLMF §27.4 Euler products: https://dlmf.nist.gov/27.4 .
- DLMF §25.10 nontrivial zeta zeros: https://dlmf.nist.gov/25.10 .
- Mertens prime products as summarized with exact constants: https://mathworld.wolfram.com/PrimeProducts.html .
- Quantum many-body orthogonality and scaling: https://doi.org/10.1103/PhysRevLett.117.146602 ; https://doi.org/10.1103/physrevlett.124.110601 . These are physical **analogies**, not inputs to the proofs.

## 8. Research decision / stop condition

**Verdict: `EXACT_QUANTUM_CRITICALITY_AND_DICKMAN_LIMIT / NO_NEW_RH_FRONTIER_ADVANCE`.** The free-prime quantum analogy passes its exact normalization tests but the large-system dynamics loses zeta zeros rather than constraining them. A locally uniform, zero-free factor-by-factor counterterm also cannot recover the actual zeta zeros, by a quantitative phase-winding obstruction. Stop this noninteracting product-state branch.

The only remaining physically motivated candidate would be a **specific arithmetic coupling between prime modes and theta modular duality** whose *finite* coherent amplitudes already carry nonzero phase winding and whose stability law can be proved independently of RH. None is currently constructed. Do not launch Codex to search an unspecified interaction. The prior independent zero-exclusion gap remains open. All historical project statuses remain unchanged.
