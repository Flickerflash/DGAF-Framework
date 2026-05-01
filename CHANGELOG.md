# DGAF-Framework Changelog

All notable changes to this project are documented here.
Format: [Semantic Versioning](https://semver.org/) | Governed by Agent Amethyst

---

## [1.0.10] — 2026-05-01

### Session 029 — Sentinel CI + CROSS_REF v3.1

**Formation:** Amethyst + Perplexity MCP (IP Sweep Formation)

#### Added (sentinel-governance repo)
- `.github/workflows/doc-lint.yml` — markdownlint-cli 0.39.0; triggers on PR + push to `main` touching `**.md`; gates PR merge on zero lint errors; P-24 surface consistency gate (P-11 gate 7); exit code 1 blocks merge
- `.markdownlint.yml` — tuned config: MD013/MD024/MD033/MD041 disabled (gate doc width, duplicate section headers, badge HTML, comment-first files); MD034/MD022/MD032/MD010/MD047 enabled

#### Changed (DGAF-Framework)
- `CROSS_REF.md` v3.1 — Internal artifact registry added: gate specs table (P-24 compliance status), `.operations/` dir, `docs/drafts/`, sync docs, dual READMEs, CI/automation table, governance relationship diagram
- `CHANGELOG.md` v1.0.10 — S029 entries
- `SWEEP_LOG.md` — S029 sealed
- `SESSION_ANCHOR.md` — S030 priority queue

#### Harmonic Score
```
Score: 1.00 — SUSTAINED (S014–S029)
Sentinel CI: ✅ LIVE (sentinel-governance)
CROSS_REF v3.1: ✅ Full internal artifact registry
Open BLGs: GAP-08 (deferred) only
All S028 + S029 targets: ✅ CLOSED
```

---

## [1.0.9] — 2026-05-01

### Session 028 — P-24 Full Gate Stack Certification + Dual README Architecture

#### Added
- `README.governance.md` — NIST/EU AI Act compliance reference
- `README.technical.md` — Agent/engineer dense spec

#### Changed (P-24 Retrofit)
- `docs/gates/GATE_1111.md` v2.0 — P-24 CERTIFIED
- `docs/gates/GATE_11Q.md` v2.0 — P-24 CERTIFIED
- `docs/gates/TELESCOPIC_LENS.md` v2.0 — P-24 CERTIFIED

#### Harmonic Score
```
Score: 1.00 — SUSTAINED (S014–S028)
Gate stack: 4/4 P-24 CERTIFIED
```

---

## [1.0.8] — 2026-05-01

### Sessions 026–027 — Structural Enhancements & P-24 Canonical Practice Unit

#### Added
- `GATE_UNIT_TEMPLATE.md`, `.operations/` dir, `docs/drafts/`, `SESSION_ANCHOR.md`
- `NDR_PATTERN_REGISTRY.md` v1.6 — P-24 registered
- `ACOUSTIC_GATES.md` v2.0 — first P-24 certified gate

---

## [1.0.7] — 2026-05-01

### Session 025 — Template Completion Sweep

#### Added
- `.github/` templates + `FUNDING.yml` — Acoustic-mesh, resumeapex-eval, 3d-visualization-hub
- `phi-calculus-app/NOTICE` — Apache-2.0 + PHDGE/DGAF attribution

---

## [1.0.6] — 2026-05-01

### Sessions 022c–023 — README Polish, SECURITY.md, PHDGE Branding Rename

#### Changed
- PHDGE branding rename: `Phi-Harmonic Pentagon` → `Phi-Harmonic Dynamic Governance Ecosystem (PHDGE)`

---

## [1.0.5] — 2026-05-01

### Sessions 022–022b — Ecosystem Surface Sweep

#### Added
- `.github/` templates + `FUNDING.yml` + badge rows — 5 repos

---

## [1.0.4] — 2026-05-01

### Sessions 014–021 — Daily Governance Sweep Block

#### Added / Fixed / Closed
- Drive sync policy, SPDX headers, Driftwatch license, GAP-01/03/07/P1-IP closed

---

## [1.0.3] — 2026-04-29

#### Added
- `ENSEMBLE_ROSTER.md` — 11 active agents

---

## [1.0.2] — 2026-04-29

#### Fixed
- NOTICE: CSDF → DGAF-Framework; Agent Lavender → retired

---

## [1.0.1] — 2026-01-15

#### Added
- CONTRIBUTING.md + SECURITY.md initial stubs

---

## [1.0.0] — 2025-12-23

### Initial Release
- Core DGAF framework; NIST AI RMF alignment; Apache 2.0
