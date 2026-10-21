> **ARCHIVED PROJECT NOTE — read the stated proof scope.** This is a public reading copy of an AI-assisted project research note. Statements retain their original evidence limits; no external peer review or literature-priority claim is implied. See [current research status](../../docs/research-status.md) and [attribution](../../docs/contributions.md). Local paths and obsolete local links have been removed; the sealed original is unchanged.
>
> Original SHA-256: `b4e0c51dcabdcb0b7b243ff452dbdd2e795d4d0aad68fb171869c0f80e42bf91`.

# Project Riemann — Primitive lattice, dual origins and dimensional zero-wave audit

Date: 2026-10-20. Classification: `CLASSICAL_DUALITY_WITH_EXACT_LOCAL_CERTIFICATE / NO_NEW_RH_FRONTIER_ADVANCE`.

## Scientific status and scope

This is a bounded investigation into the compatibility of the multiplicative origin 1 (unit for multiplication, gcd = 1) with the additive origin 0 (zero vector and Fourier transform) in integer dimension d. The constructions are classical and should NOT be attributed as newly discovered. They are not the same as the earlier infinite prime-exponent coordinates: the latter use axes labeled by primes, whereas here d labels ordinary spatial integer coordinates. No RH assumption or assertion of RH follows. This archive does not alter the historical Project Riemann handoff or its evidence.

## I. Local prime sieve and exact Fourier obstruction

Let G=(Z/pZ)^d, p prime, and f_p(x)=1_{x != 0}. Using the UNNORMALIZED additive Fourier transform

  fhat_p(xi) = sum_{x in G} f_p(x) exp(-2 pi i <x,xi>/p),

character orthogonality gives

  fhat_p(0)=p^d-1,  and  fhat_p(xi)=-1 for every nonzero xi.

The normalized uniform distribution on allowed points has characteristic Fourier coefficient -1/(p^d-1) at each nonzero mode. This is allowed for a positive probability measure; it specifically refutes a proposed NONNEGATIVE-FOURIER-COEFFICIENT condition on the indicator. It does NOT refute ordinary positive definiteness of a characteristic function, nor any proven RH criterion.

Changing the origin to a in G changes f to f_{p,a}(x)=1_{x != a}. Then fhat_{p,a}(xi)=-exp(-2 pi i <a,xi>/p) at nonzero xi: the spectral magnitude stays 1. Thus translating what is called the origin merely changes the phases.

For d=5,p=2 there are 32 parity configurations; the exact Walsh spectrum is 31 at the zero mode and -1 at each of the remaining 31. Exact enumeration verified it for d=1,...,9. Wolfram independently reproduced the d=5 spectrum.

## II. Exact multidimensional prime arithmetic

Let Theta_d(t)=sum_{m in Z^d} exp(-pi t |m|^2)=Theta_1(t)^d and define the primitive heat trace

  P_d(t)=sum_{m in Z^d \ {0}, gcd(|m_1|,...,|m_d|)=1} exp(-pi t |m|^2).

For every t>0, Mobius inversion gives the absolutely convergent identity

  P_d(t)=sum_{k>=1} mu(k) (Theta_d(k^2 t)-1).

For d>=2, primitive lattice points have natural density

  prod_p (1-p^{-d}) = 1/zeta(d).

For d=5, 1/zeta(5)=0.964387340429262459126436588445....

The origin vector MUST be excluded before using the gcd sieve; otherwise it is divisible by every positive integer and the naive Mobius formula contains a divergent ambiguity. The use of 1 as the multiplicative identity does not make the additive origin disappear.

### Classical unconditional short-time bound

For each fixed integer d>=2, as t decreases to 0,

  P_d(t)=t^{-d/2}/zeta(d)+O_d(t^{-1/2}).

Proof: set M=floor(t^{-1/2}). For k<=M, Gaussian Poisson duality yields
Theta_d(k^2t)-1=(k^2t)^{-d/2}+O_d(1), uniformly in k: the exponentially small dual-Gaussian remainder is bounded after multiplying by (k^2t)^{-d/2}. Summing O_d(1) over k<=M costs O_d(M). For k>M, Theta_d(k^2t)-1 <= C_d exp(-pi k^2t), whose sum is O_d(t^{-1/2}). Completing the main sum uses

 t^{-d/2} sum_{k>M} k^{-d} = O_d(t^{-1/2})

for fixed d>1. This is an arithmetic-geometry consequence of known theorems; it cannot exclude a single nontrivial zeta zero.

## III. Mellin transform and exact duality defect

For Re(s)>d/2, set

  Z_d(s)=sum_{m in Z^d \ {0}} |m|^{-2s},
  Z_d^prim(s)=sum_{gcd(m)=1} |m|^{-2s}.

Unique gcd factorization implies the exact identity

  Z_d(s)=zeta(2s) Z_d^prim(s).

Denote their completed Mellin transforms by

  E_d(s)=pi^{-s} Gamma(s) Z_d(s),
  A_d(s)=pi^{-s} Gamma(s) Z_d^prim(s)=E_d(s)/zeta(2s).

Poisson summation gives the meromorphic functional equation E_d(s)=E_d(d/2-s). More explicitly,

 E_d(s)=int_1^infty (Theta_d(t)-1) [t^{s-1}+t^{d/2-s-1}] dt
        +1/(s-d/2)-1/s.

Therefore the primitive / multiplicative duality defect is exactly

  zeta(2s) A_d(s) = zeta(d-2s) A_d(d/2-s)

as a MEROMORPHIC identity. Its non-divided form is important at poles and zeros. The only analytically new obligation would be an independent bound on A_d(s); the identity is a consequence of existing zeta/lattice theory. For d=1, Z_1^prim(s)=2 and E_1(s)=2 Lambda(2s); the identity is the usual Riemann zeta functional equation in the variable 2s. Dimension d=5 has lattice symmetry around Re(s)=5/4 but the zero-sensitive denominator zeta(2s) involves Re(s)=1/4 under RH: the geometries' symmetry lines are different.

## IV. Conditional individual-zero sensitivity

Let rho=beta+i gamma be a SIMPLE nontrivial zeta zero. Then at s=rho/2, A_d(s)=E_d(s)/zeta(2s) has a pole if E_d(rho/2) is nonzero, with exact residue

  C_{d,rho}=E_d(rho/2)/(2 zeta'(rho)).

Its term in a contour-shifted inverse Mellin formula, when the contour shift and sum of residues are justified, is

  C_{d,rho} t^{-rho/2} + conj(C_{d,rho}) t^{-conj(rho)/2}
  = 2 t^{-beta/2} Re(C_{d,rho} exp(-i gamma log(t)/2)).

For t=e^{-2u}, this is 2 exp(beta*u) Re(C_{d,rho} exp(i gamma*u)). These waves carry exact height gamma and growth beta, but their absence/presence also depends on cancellation E_d(rho/2)=0. Establishing no such cancellation universally, or bounding all the waves independently, has NOT been achieved. The construction does not exclude off-line zeros. Without fully justified contour and uniform bounds, a residue calculation is NOT a complete asymptotic expansion.

Other exact residues of A_d(s): at s=d/2, 1/zeta(d) (bulk); at s=0, +2 (origin correction; E_d(s) has residue -1 and zeta(0)=-1/2); at s=-1, E_d(-1)/(2 zeta'(-2)) (trivial-zero correction). These are meromorphic residues, not a claim that the primitive heat-trace remainder converges to 2.

## V. Falsification-first numerical test, d=5

Using high-precision theta integration, Mobius inversion and the first numerically computed zeta zero rho_1=1/2+14.13472514173469379...i, we obtained

  C_{5,rho_1} ~= -0.0000351095215397546111 - 0.000732923118714249263 i,
  c_{5,-1} := E_5(-1)/(2 zeta'(-2)) ~= -18.7045318570797349.

For each t, subtract bulk=t^{-5/2}/zeta(5), the residue 2 and c_{5,-1} t from P_5(t). Compare the resulting remainder with the simple first-zero pair 2 Re(C_{5,rho_1} t^{-rho_1/2}):

| t | Corrected remainder | First-zero wave | Difference |
|---|---:|---:|---:|
| 0.04 | +0.0788624958622 | -0.0021388547040 | +0.0810013505662 |
| 0.01 | +0.00946540967569 | +0.00409863027042 | +0.00536677940527 |
| 0.0025 | -0.00621178039070 | -0.00651924200613 | +0.00030746161543 |
| 0.000625 | +0.00894320331723 | +0.00897626684580 | -0.00003306352856 |
| 0.0001 | +0.0117203090824 | +0.0117507970343 | -0.0000304879519 |

Numerical proximity is striking at small t but cannot certify an omitted-zero expansion, a zeta-zero count, uniform error, or RH. Computations were high precision, not rigorously rounded interval certificates. The first zero's numerical location and apparent noncancellation are not independently certified here.

## VI. Literature precedence and novelty audit

Tate's original adelic framework combines additive Fourier analysis and multiplicative Mellin transforms to derive the functional equation; the additive/multiplicative bridge is known, not newly invented here. See Terence Tao (2008), "Tate's proof of the functional equation", https://terrytao.wordpress.com/2008/07/27/tates-proof-of-the-functional-equation/.

The primitive Epstein quotient Z_Q(s)/zeta(2s) and its error-term relationship with zeta zeros are explicitly in Walter G. Nowak (2005), "Primitive lattice points inside an ellipse", https://math.mit.edu/classes/18.158/Nowak.pdf, esp. (1.8) and the lower-bound theorem. Nowak proves an Omega-type 1/4 discrepancy phenomenon in 2D. Mark Watkins' 2004 work also uses this quotient: https://www.ams.org/mcom/2004-73-246/S0025-5718-03-01517-5/S0025-5718-03-01517-5.pdf.

Thus this audit provides a coherent multidimensional interpretation and a reproducible five-dimensional numerical illustration of **classical** arithmetic geometry. It does NOT constitute a new theorem with established research priority, a new positive form, or an RH advance.

## VII. Decision and stop condition

Verdict: `NO_NEW_RH_FRONTIER_ADVANCE`. The exact local Fourier calculation falsifies the naive assumption that removing nonprimitive points preserves nonnegative Fourier coefficients; the completed primitive-lattice formula reveals where the usual zeta zeros re-enter through the denominator. The missing theorem would be an **independent**, all-height bound on primitive-lattice oscillations that is not imported from a zero-free statement about 1/zeta. No such theorem candidate survived this audit. Do not launch Codex or make an RH claim.

Verification: `verify.py` checks exact Walsh transforms in d=1..9, direct 5D gcd-point counts against Mobius formulas at R=2,3,4, five-square coefficient convolutions for n<=200, and complex completed-Epstein duality in d=1 and d=5. `wave_diagnostic.py` reproduces the high-precision but uncertified five-dimensional residue illustration. Lean was not available in this environment. Original Project Riemann artifacts have not been modified.

Standing project statuses unchanged: RH unproved; Haglund k=2/k=3 complete verification `UNVERIFIED`; moment estimate `BLOCKED_NEW_MOMENT_ESTIMATE`; historical provenance `BLOCKED_UNWAIVED`.
