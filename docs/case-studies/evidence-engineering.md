# Case study: making mathematical work reviewable

Project Riemann generated many different kinds of evidence: written analytic arguments, floating-point diagnostics, interval calculations, exact rational checks, formal helper lemmas, and failed approaches. A useful research record must prevent those categories from silently merging.

The October 20 synchronization retained all 34 records from the October 19 master and all 42 records from the newer handoff. The public [claim registry](../../data/claims.csv) carries their evidence classes, dependencies, actions and source references. The [research atlas](../research-atlas.md) provides a readable entry point.

## Three safeguards

**Bind statements to sources.** Original hashes identify the exact saved source bytes. Public reading copies have separate hashes because editorial notices and path redactions change their bytes. A checksum is integrity evidence, not a signature, theorem or proof of authorship.

**Preserve failed checks.** The historical full Git-reference inventory failed when capture references changed. Matching source hashes did not waive that failure. The portfolio records `BLOCKED_UNWAIVED`; it does not publish a rewritten “all preservation passed” story.

**Keep the proof boundary explicit.** A Lean helper theorem does not formalize an integral estimate merely because the surrounding report mentions it. A polynomial certificate checks the actual inequality over its declared box; it does not establish the number-theoretic premise needed to apply that inequality.

## Public reproducibility boundary

The exact gate and small combinatorial demo are runnable here. The Lean source is complete and its local build record is included. The large historical Arb/FLINT certificate corpus, manuscripts and operational snapshots remain in the original archive; this repository does not claim a turnkey public reproduction of every historical k=2/k=3 calculation.

The record synchronization authenticated 32 archive layers/manifests and the saved October 18/19 audit seals. These are **historical execution records**, not newly rerun analytic proofs. The public verification command checks only the checks explicitly listed in [the reproduction guide](../reproduce.md).
