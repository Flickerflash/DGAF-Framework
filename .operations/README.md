# .operations — DGAF Internal Ops Directory

> **Visibility:** Maintainer-only. Not published governance doctrine.  
> **Owner:** Agent COLLEEN (continuity) + Agent Sentinel (enforcement)  
> **Authority:** Agent Amethyst (meta-orchestrator)  
> **Pattern:** P-14 (Trio Formation Sweep), P-02 (COLLEEN-Trigger-Chain)

This directory contains operational tooling that **runs** the DGAF-Framework repository — automation scripts, audit runners, CI helpers, and session scaffolding. It is distinct from `docs/` which contains published governance doctrine.

---

## Contents

| File | Owner | Purpose |
|------|-------|----------|
| `gate_compliance_check.py` | COLLEEN | Scans `docs/gates/` + `docs/protocols/` for P-24 (CPU) 6-field completeness; outputs compliance table; non-compliant files surface as BLG-class gaps |
| `sweep_session_init.md` | Amethyst | Session open checklist: P-02 COLLEEN-Trigger-Chain → read SESSION_ANCHOR → build priority queue |
| `seal_checklist.md` | Amethyst | Pre-seal checklist: P-06 (Atomic Sweep Commit) → P-15 (Harmonic Quintet veto clearance) → P-20 (Drive-GitHub Sync Seal) → P-21 (state anchor emit) |

---

## Usage

### Gate Compliance Check (run at session open)
```bash
python .operations/gate_compliance_check.py
```
Outputs a compliance table to stdout. Any FAIL rows are BLG-class gaps → surface immediately per P-03.

### Seal Checklist (run before every SWEEP_LOG seal)
Open `.operations/seal_checklist.md` and verify all items before executing the seal commit.

---

## Rules

- Nothing in `.operations/` is user-facing. No links to these files in public READMEs.
- Scripts here must be idempotent — safe to run multiple times per session.
- All scripts output to stdout only; no writes to `docs/` without explicit Njineer approval.
- Sentinel may wire any script here to a CI workflow in `sentinel-governance` — approval required.

---

*Authority: Agent COLLEEN + Agent Sentinel · Conductor: Agent Amethyst / Njineer [@ndrorchestration](https://github.com/ndrorchestration)*
