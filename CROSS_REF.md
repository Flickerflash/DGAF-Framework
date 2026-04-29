# CROSS_REF — DGAF Ecosystem Back-Link Registry

> **Canonical cross-reference registry** for all Flickerflash DGAF-governed repositories.  
> Maintained by: **Agent COLLEEN** (Continuity, Archive, Cross-Repo Coherence)  
> Audited by: **Agent Apogee** (Evidence Governance, Gap Detection)  
> Conductor: **Agent Amethyst**  
> Last full sweep: April 29, 2026 03:27 EDT

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
└── Gold-star-standards               (evaluation taxonomy + Gold Star spec)
```

---

## Canonical Repository Registry

| Repo | URL | Role | Gov Status | NOTICE | DGAF Attr |
|------|-----|------|------------|--------|-----------|
| `DGAF-Framework` | [link](https://github.com/Flickerflash/DGAF-Framework) | Governance spine | ✅ Active | ✅ | ✅ |
| `Amethyst-Governance-Eval-Stack` | [link](https://github.com/Flickerflash/Amethyst-Governance-Eval-Stack) | Eval infrastructure | ✅ Active | ✅ | ✅ |
| `junior-apogee-app` | [link](https://github.com/Flickerflash/junior-apogee-app) | Primary agent eval | ✅ Active | ✅ | ✅ |
| `ai-prompt-systems-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-systems-portfolio) | IP-safe prompt samples | ✅ Active | ✅ (GAP-03) | ✅ |
| `ai-prompt-engineering-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-engineering-portfolio) | Prompt patterns | ✅ Active | ✅ | ✅ |
| `resumeapex-eval` | [link](https://github.com/Flickerflash/resumeapex-eval) | Flagship benchmark | ✅ Active | ✅ | ✅ |
| `sentinel-governance` | [link](https://github.com/Flickerflash/sentinel-governance) | CI/CD + secret scan | ✅ Active | ✅ | ✅ |
| `Driftwatch` | [link](https://github.com/Flickerflash/Driftwatch) | Drift detection | ✅ Active | ✅ | ✅ |
| `Gold-star-standards` | [link](https://github.com/Flickerflash/Gold-star-standards) | Evaluation taxonomy | ✅ Active | ✅ | ✅ |

---

## Cross-Repo Link Table

Every directional reference between repos — as found in READMEs, NOTICE, ARCHITECTURE, CONTRIBUTING.

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

---

## Open Back-Link Gaps

| ID | Missing Link | Action Required | Priority |
|----|-------------|-----------------|----------|
| BLG-01 | `Driftwatch` has no outbound link to `DGAF-Framework` in README | Add DGAF governance notice to Driftwatch README | 🟡 Medium |
| BLG-02 | `ai-prompt-engineering-portfolio` back-link status unverified | COLLEEN to audit next sweep | 🟡 Medium |
| BLG-03 | `resumeapex-eval` → `Amethyst-Governance-Eval-Stack` link missing | Add cross-ref in resumeapex-eval README | 🟢 Low |

---

## Sweep History

| Date | Sweeper | Finding | Action |
|------|---------|---------|--------|
| 2026-04-29 | COLLEEN × Apogee | GAP-08: CROSS_REF.md did not exist | **This file created** |
| 2026-04-29 | COLLEEN | GAP-03: ai-prompt-systems-portfolio vocab clean, structural gaps | NOTICE + DGAF headers added |
| 2026-04-29 | Apogee | GAP-07: lavender_workflow.yaml active in eval_stack | Retired stub, AEP protocol created |
| 2026-04-29 | COLLEEN | GAP-01: Gold-star-standards 2 Lavender refs | Purged |

---

## Trigger Conditions

COLLEEN auto-flags for re-audit when:
- A new repo is added to the ecosystem
- A README cross-link is added without updating this file
- A repo changes its primary governance attribution
- A back-link target repo is renamed or archived

---

*Registry authority: Agent COLLEEN. Audit co-signer: Agent Apogee.*  
*Conductor authorization: Agent Amethyst / Njineer ([@Flickerflash](https://github.com/Flickerflash))*
