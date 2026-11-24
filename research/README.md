# Research findings index

This directory tracks investigations into mathematical simplifications of the Lean formalization. It is **research documentation**, not a claim that an independent proof has been found or compiled.

## Protocol

For each investigation, record:
- scope and source files inspected;
- **verified from source**, **mathematically proved on paper**, **hypothesis**, or **not verified** for each significant finding;
- exact theorem statements and any extra hypotheses;
- explicit obstruction or first unresolved inequality;
- Lean compilation status, if applicable;
- effect on the **proof-constant** dependency graph separately from import paths;
- one next decisive theorem.

A reformulation of a hard assertion is not an independent proof. Do not credit simplification to an unverified replacement or to a conditional theorem whose premise merely restates the target.

## Investigations

| Date | Topic | Status | Notes |
| --- | --- | --- | --- |
| 2026-11-24 | Weil two-translate obstruction and explicit periodic Möbius approximation | Mathematical reductions proved; finite approximation estimate unproved (B, GRH-hard) | [Arithmetic positivity and approximation](2026-11-24-positivity-and-periodic-mobius-approximation.md) |
| 2026-11-24 | Structural alternatives and discriminant control of `NData.etaLoc` | Local DVR/Hecke defect estimate proved on paper; family bound unproved (D) | [Structural and discriminant audit](2026-11-24-structural-alternatives-and-hecke-discriminants.md) |
| 2026-11-24 | Alpoge's methodological remarks and possible structural bypass | User-attributed methodological hypothesis; no independent shortcut proved | [Structural-cut research direction](2026-11-24-alpoge-methodological-remarks-and-structural-cut.md) |
| 2026-11-24 | `HostExW` / `TopG` logical cut and remaining dependencies | Source-verified proof interface; independent analytic estimate unresolved | [Host/TopG audit](2026-11-24-hostexw-topg-logical-cut.md) |
| 2026-11-24 | Landau positive-part windows / sparse-scale obstruction | Source-level bridge verified; mathematical contrapositive; no independent analytic estimate | [Landau bottleneck](2026-11-24-landau-positive-part-obstruction.md) |
| 2026-11-24 | `DIVinN_at` and the cohomological `VVle` input | Source-level transfer verified; independent bound unresolved | [Numerical bottleneck](2026-11-24-divinn-arithmetic-bottleneck.md) |
| 2026-11-23 | Analytic zero-exclusion / `HostExW` / `VWin` | Historical investigation tracked; no independent shortcut verified here | [Investigation register](2026-11-23-zero-exclusion-register.md) |

## Repository policy

Do not modify exported theorem signatures, existing imports, or main proof files for research-only results. No CI/GitHub Actions should be invoked to validate these notes. A document does not count as a compiled Lean result.

**Pull-request workflow:** maintain this documentation on a separate research branch in a draft PR; use subsequent commits for distinct findings, and only mark a theorem as proved after independent mathematical justification and verification.
