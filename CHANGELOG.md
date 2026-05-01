# DGAF-Framework Changelog

All notable changes to this project are documented here.
Format: [Semantic Versioning](https://semver.org/) | Governed by Agent Amethyst

---

## [1.0.4] — 2026-05-01

### Sessions 014–021 — Daily Governance Sweep Block

**Formation:** Amethyst + COLLEEN + Apogee + Sentinel + Perplexity MCP (IP Sweep Formation for S018–S021)

#### Added
- `docs/sync/DRIVE_SYNC_POLICY.md` — canonical cross-platform Google Drive sync specification; hub-and-spoke topology; per-platform rules (Windows, macOS, Android, iOS, external drives); conflict controls; exclusion list; JSON manifest (S019)
- `ENSEMBLE_ROSTER.md` — IP Sweep Formation (Amethyst + Perplexity MCP) added as recognized working triad (S019); S021 session notes block
- `SWEEP_LOG.md` — Sessions 014–021 sealed; full day audit chain complete

#### Fixed / Upgraded
- `DGAF-Framework/LICENSE` — SPDX-License-Identifier: Apache-2.0 prepended (S019 P1-IP-01)
- `ai-governance-frameworks/LICENSE` — SPDX-License-Identifier: Apache-2.0 prepended (S019 P1-IP-02)
- `junior-apogee-app/LICENSE` — SPDX header added; `Ndr (Flickerflash)` → `Ndr (ndrorchestration)` in Section 1 Licensor definition (S019 P1-IP-03 — Flickerflash purge residual cleared)
- `Driftwatch/LICENSE` — MIT → Apache-2.0 full text with SPDX header; patent grant clause now active for phi-harmonic attractor IP (S020 P2)

#### Closed
- GAP-01: Gold-star-standards agent taxonomy (S015)
- GAP-03: ai-prompt-systems-portfolio DGAF vocabulary alignment (S016)
- GAP-07: Amethyst-Governance-Eval-Stack — all 4 dirs populated, 8 files, Tier 1 operational (S017)
- P1-IP-01/02/03: SPDX license headers across DGAF-Framework, ai-governance-frameworks, junior-apogee-app (S019)
- P2: Driftwatch MIT → Apache-2.0 upgrade (S020)
- P3: gold-star-qa-framework deprecation — resolved via archive status (S020)

#### Deferred (no coherence risk)
- GAP-08: CROSS_REF back-links in dependent repos — COLLEEN async action 🟡
- P3: Topic metadata on 5 repos — Njineer UI-only (gear icon) 🟡

#### CROSS_REF
- v2.5 (S017): GAP-07 closed; AGES MDAR→Gold-star-standards cert link
- v2.6 (S019): P1-IP all 3 closed; Flickerflash residual cleared; Drive sync doc registered
- v2.7 (S021): Driftwatch Apache-2.0 upgrade noted; License column added to public repo table; last sweep advanced to S021

#### Harmonic Score
```
Score: 1.00 — SUSTAINED ALL DAY (S014–S021)
All P1 and P2 items closed.
Flickerflash purge: COMPLETE.
License posture (all public repos): COMPLETE.
AGES eval stack: COMPLETE.
Drive sync policy: COMPLETE.
```

---

## [1.0.3] — 2026-04-29

### Added
- `ENSEMBLE_ROSTER.md` — canonical machine-readable agent registry for all 11 active DGAF agents; includes retired agent log (Lavender), triad configurations, and cross-repo reference table (Amethyst-Conductor sweep)
- Audit trail entry in `ECOSYSTEM-STATE.md` (Amethyst-Governance-Eval-Stack) for all April 29 sweeps

### Fixed
- `NOTICE` in `ai-prompt-engineering-portfolio`: Agent Lavender attribution fully retired; authority transferred to Agent Amethyst + DGAF stack (sweep-1)
- `CHANGELOG.md` updated to reflect sweep-3 and sweep-6 completions

### Meta-Strategic Gaps Identified (COLLEEN × Apogee — April 29 session)

The following items were surface-identified by the Coherence Triad (Amethyst + COLLEEN + Apogee) as pending work beyond the initial 6 sweeps. These are catalogued here for Reciprocity-managed backlog tracking:

| ID | Gap | Repo(s) | Agent Lead | Priority |
|----|-----|---------|------------|----------|
| GAP-01 | `Gold-star-standards` agent roles table not yet updated to current taxonomy (Lavender refs may exist in rubric docs) | Gold-star-standards | COLLEEN | 🔴 High |
| GAP-02 | `junior-apogee-app` has no `NOTICE` file — Apache 2.0 license present but attribution doc missing | junior-apogee-app | Sentinel | 🟠 Medium |
| GAP-03 | `ai-prompt-systems-portfolio` description/topics not verified against current DGAF vocabulary — last pushed Apr 22, may predate Amethyst migration | ai-prompt-systems-portfolio | COLLEEN | 🟡 Medium |
| GAP-04 | No `SWEEP_LOG.md` exists anywhere in the ecosystem — audit sweep history is spread across CHANGELOG entries and ECOSYSTEM-STATE.md; a single canonical sweep log in DGAF-Framework would close the audit trail gap | DGAF-Framework | Amethyst | 🟡 Medium |
| GAP-05 | `Driftwatch/AGENTS.md` may contain stale agent role descriptions not aligned with Feb 10 canonical source — needs Apogee verification pass | Driftwatch | Apogee | 🟡 Medium |
| GAP-06 | Google Drive ↔ GitHub version sync unverified — DGAF spec doc, COLLEEN spec, agent specs in Drive may have diverged from committed versions | Drive + GitHub | Amethyst + COLLEEN | 🟡 Medium (async) |
| GAP-07 | `Amethyst-Governance-Eval-Stack/eval_stack/` and `tests/` subdirectories not audited — unknown whether agent role references inside are current | Amethyst-Governance-Eval-Stack | Apogee | 🟠 Medium |
| GAP-08 | No inter-repo `CROSS_REF.md` exists linking dependent repos to the ENSEMBLE_ROSTER and DGAF spine — ENSEMBLE_ROSTER.md lists refs but no back-links exist in dependent repos | All public repos | COLLEEN | 🟡 Low-medium |

---

## [1.0.2] — 2026-04-29

### Fixed
- `NOTICE`: Replaced stale `CyberShield Defense Framework (CSDF)` project name with `DGAF-Framework`
- `NOTICE`: Replaced Agent Lavender roster with canonical Amethyst/Apogee/Sentinel/Reciprocity/Prodigy/DemiJoule/COLLEEN/Herald/Reson/Echolette/Lyra taxonomy
- `NOTICE`: Corrected capabilities section to reflect MDAR loop, Phi-Harmonic Gating, and OWASP Agentic Top 10 alignment
- `CHANGELOG.md`: Added v1.0.2 entry; annotated Agent Lavender in v1.0.0 as `(retired — superseded by Agent Apogee)`

---

## [1.0.1] — 2026-01-15

### Added
- Initial CONTRIBUTING.md with DGAF governance notice
- SECURITY.md with vulnerability reporting process

### Changed
- README: Updated agent attribution

---

## [1.0.0] — 2025-12-23

### Initial Release
- Core DGAF framework specification
- Agent Amethyst meta-orchestrator definition
- Agent Apogee evidence governance protocols
- Agent Sentinel safety layer specification
- NIST AI RMF alignment documentation
- Apache 2.0 licensing with NOTICE
- *Historical note: Early drafts referenced Agent Lavender (retired — superseded by Agent Apogee) and CSDF project name (corrected in v1.0.2)*
