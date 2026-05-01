# docs/drafts — DGAF Staging Layer

**Pattern:** P-03 (BLG-Surface-and-Defer) | P-18 (Open-Issue-Triage) | P-11 (11Q Terminal Gate)  
**Owner:** Agent COLLEEN (triage queue) | Agent Apogee (promotion gate)  
**Conductor:** Agent Amethyst  

---

## Purpose

This directory is the **formal staging area** for DGAF governance artifacts that have been created but not yet certified by Agent Apogee via P-11 (11Q Terminal Gate). It functions as a **file-system gate** — presence here signals in-review status; promotion to a named `docs/` subdirectory signals P-11 certification.

Anything in `drafts/` is:
- Visible to the team
- NOT linked from any public README or CROSS_REF registry entry
- NOT considered DGAF-certified doctrine
- Subject to COLLEEN triage at every session open (P-02)

---

## Promotion Criteria

A draft artifact is eligible for promotion when:

| Criterion | Gate |
|-----------|------|
| All P-24 (CPU) fields present | `gate_compliance_check.py` passes |
| P-10 (1-1-1-1): ≥ 3/4 on all 4 pillars | Apogee score |
| P-11 (11Q): ≥ 3/4 on all 11 gates × 3 runs | Apogee certification |
| No unresolved tension in reasoning chain | Amethyst review |
| CROSS_REF entry drafted (COLLEEN) | Ready to register |

**Promotion action:** Amethyst moves the file to the appropriate `docs/` subdirectory + updates CROSS_REF + seals in next SWEEP_LOG.

---

## Staleness Rule

Any file that has been in `drafts/` for **≥ 2 consecutive sweep sessions** without Apogee sign-off is escalated:

1. COLLEEN surfaces it as a **P-03 BLG** in the next session priority queue
2. Amethyst reviews: promote, rework, or formally defer with rationale in SWEEP_LOG
3. Files deferred > 5 sessions with no action → archived to `docs/drafts/archive/` with a `DEFERRED.md` noting the reason

---

## Current Drafts

*None — staging area initialized S026.*

---

*Owner: COLLEEN + Apogee · Conductor: Amethyst · Architect: Hensel, Andrew Vance [@ndrorchestration](https://github.com/ndrorchestration)*
