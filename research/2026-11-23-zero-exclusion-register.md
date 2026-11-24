# Earlier zero-exclusion research: investigation register

**Recorded:** 2026-11-24.  
**Status:** HISTORICAL INVESTIGATION REGISTER. The source-verified Landau findings are documented separately in the [2026-11-24 analytic report](2026-11-24-landau-positive-part-obstruction.md); the remaining historical research prompts are not independently verified by this register.

## Investigations raised

1. **GRH proof-tree shortening:** seek a genuine mathematical shortcut from the current long formalization to Dirichlet L-function nonvanishing, without cosmetic refactoring.
2. **`VWin` route:** investigate replacing the Galois-derived `UpperTheory.Top.VWin` machinery by a weaker independently proved analytic or arithmetic estimate.
3. **`HostExW` route:** inspect what `UpperTheory.Top.zeroFreeAll_of_topG` actually consumes; avoid reproducing the full witness structure if a weaker numerical condition suffices.
4. **Positive-part / Landau window route:** subsequent source inspection verified the exact `WindowHyp` → `lemmaL` → zero-exclusion bridge and a mathematical contrapositive ruling out favorable sparse **full power** windows under a hypothetical off-line zero. The GRH-to-window converse invokes standard explicit-formula estimates and was not formalized. See [Landau positive-part obstruction](2026-11-24-landau-positive-part-obstruction.md). No independent estimate was proved.
5. **`DIVinN_at` route:** find a primewise arithmetic control of the ramification-weighted exceptional sum. See [numerical bottleneck](2026-11-24-divinn-arithmetic-bottleneck.md) for newly source-verified findings.

## Important distinction

A downstream condition can be formally weaker than a rich witness theorem and still be just as difficult as GRH or the original cohomological input. The standard for success is an independent mathematical proof plus verified sufficient implications to downstream Lean theorems.

## Next record to create

For each earlier investigation, create a separate, dated report **only after** checking exact repository declarations, stating the candidate theorem and identifying the first independently unproved step. Do not treat the earlier research prompts as proved findings.
