# Alpoge's methodological remarks and the next structural-cut investigation

**Recorded:** 2026-11-24.  
**Status:** RESEARCH MOTIVATION / PROPOSED INVESTIGATION, NOT A PROVED SHORTCUT.  
**Provenance:** Message attributed to Alpoge and supplied verbatim by a collaborator in conversation. The original posting and its context have **not** been independently authenticated here.  
**Lean check:** not run; no Lean changes.

## Relevant remarks (user-provided attribution)

The supplied message makes four distinct points:

1. The much-repeated page counts (including “250,000+ pages”) were jokes, not accurate measurements of the proof.
2. The existing Lean development compiles according to the speaker, but the speaker considers substantial portions unnecessarily messy; this is **not** an independently verified compilation report.
3. The speaker expects substantial simplification: “I bet most is unnecessary in the end”.
4. The speaker describes the absence of an appropriate “H^1 object” over number fields as a conceptual obstacle and suggests that current difficulty may reflect an inadequate setup rather than intrinsic complexity.

These are a researcher's methodological views, **not** evidence that a mathematical shortcut exists, that GRH has an elementary proof, or that a specific branch can be deleted. Do not infer an exact page count or verified source provenance from this note.

## Interpretation, qualified

**Three different tasks must be kept separate.**

- *Lean source simplification:* removing duplicated constructions, overly elaborate elaboration, proof engineering overhead, or unused source code. This can substantially shorten text without changing mathematics or proof constants.
- *Dependency simplification:* replacing a verified collection of proof-constant dependencies with a shorter and mathematically genuine theorem. Import graph reductions require a separate measurement.
- *Conceptual simplification:* finding a natural definition, object, pairing, duality, trace, or positivity mechanism that makes parts of the existing construction unnecessary. The hinted H^1-like object is a speculative research direction, not a defined object or established replacement.

The author's expectation strengthens the *motivation to look*, not the probability of any specific unproved inequality.

## Existing source-verified boundaries in this PR

- [Host/TopG logical-cut note](2026-11-24-hostexw-topg-logical-cut.md): `zeroFreeAll_of_topG` takes a `TopG` family-connection input and a separate `HostExW` supply input. Replacing `supplyChi` alone retains the `shape_closed_link_n_of_green` / `TopG` branch.
- [Landau obstruction note](2026-11-24-landau-positive-part-obstruction.md): a universal favorable power-window condition is not automatically a weaker independently provable principle; the positive-part estimate remains unproved.
- [DIVinN arithmetic bottleneck](2026-11-24-divinn-arithmetic-bottleneck.md): the source-visible `VVle → vvRecord → divinN_at` transfer is numerical, and an independent uniform exceptional-sum bound has **not** been proved.

None of these establishes that `DIVinN` or `TopG` is dispensable; none measures a reduced proof-constant graph.

## Next research decision: can the final contradiction avoid the current family architecture?

Do **not** start by postulating a universal zero-free window estimate, a renamed `DIVinN` budget, or an unspecified H^1-object. Instead work backward from the *actual last use* of `TopG`, `HostExW`, and `DIVinN`, and look for a structural theorem with assumptions that are concretely simpler **and independently demonstrable**.

Two options should be investigated and compared:

**A. Local arithmetic repair.** For constructed families only, seek proved bounds on the denominators of spectral idempotents / local Hecke congruence modules and propagate them through `D7.etaJ_tie` to `DIVinN`. Abstract finite rank is not enough: a rank-two split-order model allows arbitrarily deep congruence, so any uniform theorem must use a further arithmetic hypothesis. Do not claim this model refutes a complete `D7` family.

**B. Structural bypass.** Inspect the last analytic or arithmetic use of the geometric/family objects, determine whether it needs *all* the family connectivity/witness constructions, and formulate one natural, independently testable lemma (perhaps arising from a pairing, trace formula, positivity, or a genuinely defined cohomological object) that implies zero-exclusion without the `VVle → DIVinN → topDesWin → TopG` route. A restatement of the GRH-equivalent universal power-window condition is not a shortcut.

## Exact research task to run next

**Goal:** Identify either (i) a source-supported structural cut that demonstrably avoids both the `TopG` and `HostExW` witnesses, with an independently provable mathematical input, or (ii) a rigorous explanation why each promising cut is equivalent to a known hard analytic estimate, with the first missing inequality identified.

1. Audit `src/Main.lean`, `src/Statements.lean`, `ZeroFreeAllOfTopG.lean`, `TopPlug.lean`, `TopShape.lean`, `DesWin.lean`, `TopWin.lean`, and `Window.lean`; follow actual theorem applications, not names alone.
2. Record the **minimum logical input** consumed at the final contradiction, its exact quantifiers and constants, and which earlier constructions provide it. Disentangle the `TopG` branch from the independent `HostExW` supply.
3. For each alternative (local arithmetic, structural pairing/trace/positivity, analytic cut), exhibit its *first genuinely new lemma* and either prove it or provide a precise obstruction. Check circularity against `VVle`, `HypV`, `VWin`, `HostExW`, `TopG`, and GRH-equivalent window criteria.
4. If proposing an H^1-like object, give a mathematically precise definition, its key properties, and the actual derived inequality. Do not count the name or an analogy as a proof.
5. Show the exact changed proof-constant dependency path **only if proved**; distinguish it from textual simplification and imports. No `sorry`, `admit`, new axioms, Lean import changes, CI or GitHub Actions. Only report successful compilation after a local Lean check.
6. Deliver a source-linked note classifying proposed routes A (independently proved and sufficient), B (comparably difficult/circular), C (false or insufficient with obstruction), or D (precisely unresolved); name exactly **one** next decisive theorem.

**Success condition:** A genuinely independent lemma together with the complete numerical/logical bridge to Dirichlet L-function nonvanishing, or a new rigorous obstruction that narrows the search. A mere renamed interface, shorter file, or conditional theorem is not success.

## Current result / classification

**D — structural simplification is a concrete research question, not an established result.** No new arithmetic estimate, structural cohomology object, alternative zero-exclusion principle, compiled Lean proof, or verified dependency reduction is claimed.
