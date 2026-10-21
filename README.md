# Project Riemann — Research & Verification Portfolio

**Christopher Kiser · Independent, AI-assisted mathematical research**

[Research atlas](docs/research-atlas.md) · [Proofs & reproducibility](docs/reproduce.md) · [My contributions](docs/contributions.md) · [Scientific status](docs/research-status.md)

Project Riemann investigates how mathematical ideas can be turned into precise claims, reproducible computations, and proofs whose assumptions can be inspected. It began with zeros of approximations to the Riemann Xi function and grew into a documented study of prime hierarchies, arithmetic cancellation, spectral models, and the limits of proposed proof methods.

This portfolio brings together **76 recorded claims and questions, 46 research notes, 10 focused Lean declarations, and a portable exact-rational verifier**. It includes successful limited results, countermodels, corrections, and the reasons promising approaches stopped.

**Current boundary:** RH remains open. Complete Haglund k=2/k=3 verification is unverified. The Lean proofs establish the precise algebraic statements in their source; they do not establish the unresolved analytic premises.

## Start with three case studies

| Case study | What you can inspect | What the result establishes |
|---|---|---|
| [A promising inequality that did not close the proof](docs/case-studies/marked-inverse.md) | Ten Lean declarations, exact rational witnesses, independent Bernstein certificates and negative controls | The finite gate passes, while the published analytic initialization remains unavailable in the proposed range |
| [Nested prime indices and gap structure](docs/case-studies/nested-primes.md) | A research question I originated, general telescoping/rank-count arguments and a small reproducible Python demonstration | Exact combinatorial identities, with an explicit control showing why those identities alone do not imply RH |
| [Building an auditable research record](docs/case-studies/evidence-engineering.md) | A classified claim registry, source hashes, proof dependencies, failure records and formal-proof scope | A reviewable chain from a claim to its evidence, including unresolved provenance and mathematical obligations |

## Run a meaningful check

The public Python checks use **only the standard library**:

```bash
python3 scripts/verify_portfolio.py
```

This replays 19 exact continuum inequalities on 1,216 Bernstein boxes, checks 16 fixed comparisons, exercises negative controls, and runs a bounded nested-prime identity demonstration. It also validates the public registry and source hashes. No historical numerical campaign is started.

With the already installed **Lean 4.35.0** toolchain:

```bash
lean lean/MarkedGate.lean
```

Every declaration prints its statement and axiom dependencies. See [the complete reproduction guide](docs/reproduce.md), [Lean source](lean/MarkedGate.lean), and [verification evidence](evidence/README.md).

## What this project demonstrates

- **Research specification:** turning intuitive patterns into statements with explicit domains, quantifiers and failure conditions.
- **Exact computation:** rational arithmetic and polynomial certificates rather than sampled floating-point signs.
- **Formal verification:** separating compiled algebra from analytic claims that have not been formalized.
- **Adversarial evaluation:** testing countermodels, invalid inferences and boundary cases before accepting a result.
- **Evidence engineering:** source-bound records, independent replay, immutable historical snapshots and disclosed failures.
- **AI-assisted research direction:** organizing a sustained investigation, comparing approaches and preserving an honest account of what is known.

The [contribution statement](docs/contributions.md) explains my role and the substantial AI assistance in derivations and code. This repository documents work that can be examined; it is not a substitute for independently demonstrating a skill in an interview.

## Research coverage

The [research atlas](docs/research-atlas.md) covers Xi/Haglund zero motion, contour transfer, exact inequalities, nested prime-index sequences, signed Möbius correlations, prime-phase regularization, theta kernels, probability, quantum/spectral models, primitive lattice geometry, and finite-versus-infinite obstructions.

The distinctive contribution is the project-specific research trail and verification work. **First-in-literature novelty has not been established.** Classical identities and external results are attributed; unproved candidates are labeled. The archive includes negative results so that future work does not repeat an invalid inference.

## Repository map

```text
docs/                 Guided case studies, status, research atlas and reproduction
lean/                 Exact formal statements; no analytic RH bridge assumed
scripts/              Small, local, standard-library verification tools
data/claims.csv       All 76 classified claims and questions
research/notes/       Public reading copies of 46 project research notes
research/source-index.csv  Original and public-copy hashes and transformations
evidence/             Reference certificates and fresh local verification receipts
```

[Timeline and current frontier](docs/research-status.md) · [Limitations and corrections](docs/limitations.md) · [References](docs/references.md)

**Related projects:** [earlier Project Riemann overview](https://github.com/christopher-kiser/project-riemann-research) · [formal-verification workspace](https://github.com/christopher-kiser/math-research-verifier) · [Christopher Kiser on GitHub](https://github.com/christopher-kiser)

Research snapshot: **October 20, 2026**. Public code and notes are provided for inspection; no project-wide reuse license has yet been selected.
