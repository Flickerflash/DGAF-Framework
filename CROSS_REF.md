# CROSS_REF — DGAF Ecosystem Back-Link Registry

> **Canonical cross-reference registry** for all Flickerflash DGAF-governed repositories.  
> Maintained by: **Agent COLLEEN** (Continuity, Archive, Cross-Repo Coherence)  
> Audited by: **Agent Apogee** (Evidence Governance, Gap Detection)  
> Conductor: **Agent Amethyst**  
> Last full sweep: April 29, 2026 03:33 EDT

---

## Purpose

This file is the **single source of truth** for cross-repository links within the DGAF ecosystem.
Every repo that references another must be registered here. Any link found in a repo that does
not appear in this registry is a gap-detection trigger for COLLEEN.

---

## Ecosystem Map

```
DGAF-Framework (spine)
├── Amethyst-Governance-Eval-Stack   (evaluation infrastructure)
├── junior-apogee-app                 (primary agent eval platform)
├── ai-prompt-systems-portfolio       (public IP-safe prompt samples)
├── ai-prompt-engineering-portfolio   (prompt engineering patterns)
├── resumeapex-eval                   (flagship benchmark)
├── sentinel-governance               (CI/CD integrity + secret scanning)
├── Driftwatch                        (drift detection, monitoring)
├── Gold-star-standards               (evaluation taxonomy + Gold Star spec)
└── 3d-visualization-hub              (Driftwatch 3D drift rendering)
```

---

## Canonical Repository Registry

| Repo | URL | Role | Gov Status | NOTICE | DGAF Attr |
|------|-----|------|------------|--------|-----------|
| `DGAF-Framework` | [link](https://github.com/Flickerflash/DGAF-Framework) | Governance spine | ✅ Active | ✅ | ✅ |
| `Amethyst-Governance-Eval-Stack` | [link](https://github.com/Flickerflash/Amethyst-Governance-Eval-Stack) | Eval infrastructure | ✅ Active | ✅ | ✅ |
| `junior-apogee-app` | [link](https://github.com/Flickerflash/junior-apogee-app) | Primary agent eval | ✅ Active | ✅ | ✅ |
| `ai-prompt-systems-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-systems-portfolio) | IP-safe prompt samples | ✅ Active | ✅ | ✅ |
| `ai-prompt-engineering-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-engineering-portfolio) | Prompt patterns | ✅ Active | ✅ | ✅ |
| `resumeapex-eval` | [link](https://github.com/Flickerflash/resumeapex-eval) | Flagship benchmark | ✅ Active | ✅ | ✅ |
| `sentinel-governance` | [link](https://github.com/Flickerflash/sentinel-governance) | CI/CD + secret scan | ✅ Active | ✅ | ✅ |
| `Driftwatch` | [link](https://github.com/Flickerflash/Driftwatch) | Drift detection | ✅ Active | ✅ | ✅ |
| `Gold-star-standards` | [link](https://github.com/Flickerflash/Gold-star-standards) | Evaluation taxonomy | ✅ Active | ✅ | ✅ |
| `3d-visualization-hub` | [link](https://github.com/Flickerflash/3d-visualization-hub) | 3D drift rendering | ✅ Active | ⚠️ Unverified | ⚠️ BLG-04 |

---

## Cross-Repo Link Table

| Source Repo | File | Target Repo | Link Type | Status |
|-------------|------|-------------|-----------|--------|
| `DGAF-Framework` | `README.md` | `Amethyst-Governance-Eval-Stack` | Related project | ✅ |
| `DGAF-Framework` | `README.md` | `junior-apogee-app` | Related project | ✅ |
| `DGAF-Framework` | `README.md` | `sentinel-governance` | Related project | ✅ |
| `DGAF-Framework` | `README.md` | `Gold-star-standards` | Related project | ✅ |
| `Amethyst-Governance-Eval-Stack` | `ARCHITECTURE.md` | `DGAF-Framework` | Governance spine | ✅ |
| `Amethyst-Governance-Eval-Stack` | `README.md` | `junior-apogee-app` | Related project | ✅ |
| `junior-apogee-app` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `junior-apogee-app` | `README.md` | `resumeapex-eval` | Related benchmark | ✅ |
| `ai-prompt-systems-portfolio` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `ai-prompt-systems-portfolio` | `README.md` | `junior-apogee-app` | Related project | ✅ |
| `ai-prompt-systems-portfolio` | `README.md` | `resumeapex-eval` | Related project | ✅ |
| `sentinel-governance` | `CONTRIBUTING.md` | `DGAF-Framework` | Governance notice | ✅ |
| `Gold-star-standards` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `resumeapex-eval` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `Driftwatch` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `Driftwatch` | `README.md` | `3d-visualization-hub` | Visualization output | ✅ |
| `Driftwatch` | `README.md` | `junior-apogee-app` | Monitored platform | ✅ |
| `Driftwatch` | `README.md` | `Amethyst-Governance-Eval-Stack` | MDAR response layer | ✅ |
| `Driftwatch` | `README.md` | `sentinel-governance` | CI enforcement | ✅ |

---

## Open Back-Link Gaps

| ID | Missing Link | Action Required | Priority | Status |
|----|-------------|-----------------|----------|--------|
| BLG-01 | `Driftwatch` → `DGAF-Framework` back-link | **Resolved — false positive.** Driftwatch README has DGAF link in governance block AND Related Ecosystem section. | ✅ Closed | Resolved Apr 29 03:33 |
| BLG-02 | `ai-prompt-engineering-portfolio` back-link status unverified | COLLEEN to audit next sweep | 🟡 Medium | Open |
| BLG-03 | `resumeapex-eval` → `Amethyst-Governance-Eval-Stack` link missing | Add cross-ref in resumeapex-eval README | 🟢 Low | Open |
| BLG-04 | `3d-visualization-hub` NOTICE + DGAF attr unverified | COLLEEN to audit | 🟡 Medium | Open |

---

## Sweep History

| Date | Sweeper | Finding | Action |
|------|---------|---------|--------|
| 2026-04-29 03:33 | COLLEEN × Apogee | GAP-09: missing canonical .md files; GAP-10: specs/ missing | 5 canonical .md + full specs/ scaffold created |
| 2026-04-29 03:33 | COLLEEN | BLG-01: Driftwatch DGAF back-link | False positive — link confirmed present |
| 2026-04-29 03:33 | Apogee | `3d-visualization-hub` found in Driftwatch links | Added as BLG-04 unverified repo |
| 2026-04-29 03:27 | COLLEEN × Apogee | GAP-08: CROSS_REF.md did not exist | This file created |
| 2026-04-29 03:27 | COLLEEN | GAP-03: ai-prompt-systems-portfolio vocab clean, structural gaps | NOTICE + DGAF headers added |
| 2026-04-29 03:20 | Apogee | GAP-07: lavender_workflow.yaml active in eval_stack | Retired stub, AEP protocol created |
| 2026-04-29 03:16 | COLLEEN | GAP-01: Gold-star-standards 2 Lavender refs | Purged |

---

## COLLEEN Trigger Conditions

Auto-flag for re-audit when:
- A new repo is added to the ecosystem
- A README cross-link is added without updating this file
- A repo changes its primary governance attribution
- A back-link target repo is renamed or archived
- A repo appears in any link table here with `⚠️ Unverified` status

---

*Registry authority: Agent COLLEEN. Audit co-signer: Agent Apogee.*  
*Conductor authorization: Agent Amethyst / Njineer ([@Flickerflash](https://github.com/Flickerflash))*
