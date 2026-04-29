# CROSS_REF — DGAF Ecosystem Back-Link Registry

> **Canonical cross-reference registry** for all Flickerflash DGAF-governed repositories.  
> Maintained by: **Agent COLLEEN** (Continuity, Archive, Cross-Repo Coherence)  
> Audited by: **Agent Apogee** (Evidence Governance, Gap Detection)  
> Conductor: **Agent Amethyst**  
> Last full sweep: April 29, 2026 03:40 EDT

---

## Purpose

This file is the **single source of truth** for cross-repository links within the DGAF ecosystem.
Every repo that references another must be registered here. Any link found in a repo that does
not appear in this registry is a gap-detection trigger for COLLEEN.

---

## Ecosystem Map

```
DGAF-Framework (spine)
├── Amethyst-Governance-Eval-Stack      (evaluation infrastructure)
├── junior-apogee-app                    (primary agent eval platform)
├── ai-prompt-systems-portfolio          (public IP-safe prompt samples)
├── ai-prompt-engineering-portfolio      (v1 archive — predecessor)
├── prompt-optimization-library          (benchmark + template archive) [BLG-05]
├── ai-governance-frameworks             (NIST/ISO/IIA governance docs)
├── resumeapex-eval                      (flagship benchmark)
├── sentinel-governance                  (CI/CD integrity + secret scanning)
├── Driftwatch                           (drift detection, monitoring)
├── 3d-visualization-hub                 (Driftwatch 3D drift rendering)
├── Acoustic-mesh                        (WebRTC acoustic mesh phi-harmonic) [BLG-06]
└── Gold-star-standards                  (evaluation taxonomy + Gold Star spec)
```

---

## Canonical Repository Registry

| Repo | URL | Role | Gov Status | NOTICE | DGAF Attr |
|------|-----|------|------------|--------|-----------|
| `DGAF-Framework` | [link](https://github.com/Flickerflash/DGAF-Framework) | Governance spine | ✅ Active | ✅ | ✅ |
| `Amethyst-Governance-Eval-Stack` | [link](https://github.com/Flickerflash/Amethyst-Governance-Eval-Stack) | Eval infrastructure | ✅ Active | ✅ | ✅ |
| `junior-apogee-app` | [link](https://github.com/Flickerflash/junior-apogee-app) | Primary agent eval | ✅ Active | ✅ | ✅ |
| `ai-prompt-systems-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-systems-portfolio) | IP-safe prompt samples | ✅ Active | ✅ | ✅ |
| `ai-prompt-engineering-portfolio` | [link](https://github.com/Flickerflash/ai-prompt-engineering-portfolio) | v1 archive | ✅ Active | ✅ | ✅ |
| `prompt-optimization-library` | [link](https://github.com/Flickerflash/prompt-optimization-library) | Benchmark + templates | ⚠️ BLG-05 | ⚠️ Unverified | ⚠️ Unverified |
| `ai-governance-frameworks` | [link](https://github.com/Flickerflash/ai-governance-frameworks) | Governance docs | ✅ Active | ✅ | ✅ |
| `resumeapex-eval` | [link](https://github.com/Flickerflash/resumeapex-eval) | Flagship benchmark | ✅ Active | ✅ | ✅ |
| `sentinel-governance` | [link](https://github.com/Flickerflash/sentinel-governance) | CI/CD + secret scan | ✅ Active | ✅ | ✅ |
| `Driftwatch` | [link](https://github.com/Flickerflash/Driftwatch) | Drift detection | ✅ Active | ✅ | ✅ |
| `3d-visualization-hub` | [link](https://github.com/Flickerflash/3d-visualization-hub) | 3D drift rendering | ✅ Active | ✅ (BLG-04) | ✅ |
| `Acoustic-mesh` | [link](https://github.com/Flickerflash/Acoustic-mesh) | WebRTC phi-harmonic mesh | ⚠️ BLG-06 | ⚠️ Unverified | ⚠️ Unverified |
| `Gold-star-standards` | [link](https://github.com/Flickerflash/Gold-star-standards) | Evaluation taxonomy | ✅ Active | ✅ | ✅ |

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
| `ai-prompt-engineering-portfolio` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `ai-prompt-engineering-portfolio` | `README.md` | `ai-prompt-systems-portfolio` | Successor link | ✅ |
| `ai-prompt-engineering-portfolio` | `README.md` | `Amethyst-Governance-Eval-Stack` | Related project | ✅ |
| `ai-prompt-engineering-portfolio` | `README.md` | `prompt-optimization-library` | Featured project | ⚠️ BLG-05 |
| `sentinel-governance` | `CONTRIBUTING.md` | `DGAF-Framework` | Governance notice | ✅ |
| `Gold-star-standards` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `resumeapex-eval` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `Driftwatch` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `Driftwatch` | `README.md` | `3d-visualization-hub` | Visualization output | ✅ |
| `Driftwatch` | `README.md` | `junior-apogee-app` | Monitored platform | ✅ |
| `Driftwatch` | `README.md` | `Amethyst-Governance-Eval-Stack` | MDAR response layer | ✅ |
| `Driftwatch` | `README.md` | `sentinel-governance` | CI enforcement | ✅ |
| `3d-visualization-hub` | `README.md` | `DGAF-Framework` | Governance spine | ✅ |
| `3d-visualization-hub` | `README.md` | `Driftwatch` | Data source | ✅ |
| `3d-visualization-hub` | `README.md` | `junior-apogee-app` | Data source | ✅ |
| `3d-visualization-hub` | `README.md` | `Acoustic-mesh` | Related project | ⚠️ BLG-06 |

---

## Open Back-Link Gaps

| ID | Missing Link / Issue | Action Required | Priority | Status |
|----|---------------------|-----------------|----------|--------|
| BLG-01 | Driftwatch DGAF back-link | False positive — confirmed clean | ✅ | Resolved |
| BLG-02 | ai-prompt-engineering-portfolio CSDF + back-links | Fixed — CSDF→DGAF + callout + Related section added | ✅ | Closed Apr 29 03:40 |
| BLG-03 | resumeapex-eval → Amethyst-Eval-Stack link missing | Add cross-ref in resumeapex-eval README | 🟢 Low | Open |
| BLG-04 | 3d-visualization-hub NOTICE + DGAF callout | NOTICE created + callout added | ✅ | Closed Apr 29 03:40 |
| BLG-05 | `prompt-optimization-library` NOTICE + DGAF attr unverified | COLLEEN to audit next sweep | 🟡 Medium | **Next** |
| BLG-06 | `Acoustic-mesh` NOTICE + DGAF attr unverified | COLLEEN to audit next sweep | 🟡 Medium | **Next** |

---

## GAP-06 Drive ↔ GitHub Sync Register

> Browser-accessed Drive (April 29, 2026 03:40 EDT). Dynamic file listing not accessible via browser reader; thread-attached Drive files used as inventory source.

| Drive Asset | GitHub Counterpart | Status | Sub-Gap |
|-------------|-------------------|--------|--------|
| `PERPLEXITY-Space-standard-record-v.1.md` | None — session archive | 🟡 Drive-only | — |
| `MASTER-PORTFOLIO-INVENTORY-VERIFICATION-SYSTEM.md` | Partial — CROSS_REF.md + SWEEP_LOG.md | 🟡 Delta sync needed | GAP-06a |
| `Google-Drive-Organizer-Apps-Script.md` | None | 🟡 Evaluate for repo | GAP-06b |
| `Gmail-Routing-Table` | None | 🟡 Evaluate for repo | — |
| `careerpositioning.md` | None | 🟡 Evaluate for private repo | GAP-06d |
| `agent-lavender-space-context-analysis.pdf` | Superseded by SWEEP_LOG/NOTICE | ✅ Archived via sweep | — |
| `PROJECT-ANDROMEDA_SOVEREIGN-LEDGER-SYNC` | None | 🟡 Evaluate for DGAF subfolder | GAP-06c |

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
