# Trio Formation Spec

**Pattern:** P-14 — Trio-Formation-Sweep  
**Version:** 1.1  
**Maintained by:** Amethyst-Conductor  
**Last updated:** 2026-05-01 (S013 — COH-01/02/04 resolved)

---

## Formation Composition

| Agent | Role | Lane | Authority |
|-------|------|------|-----------|
| Amethyst-Conductor | Meta-orchestrator, commit gate | Conductor | Hard veto on all commits |
| Apogee | Evidence scorer, 11Q gate | Evaluation | Scores every artifact pre-commit |
| COLLEEN | Registry, continuity, BLG queue | Memory | Surfaces deferred gaps at session open |

## Activation Conditions

- Session touches ≥ 3 repos simultaneously
- Cross-repo delta required (CROSS_REF vs. Drive inventory)
- Any sweep session with SWEEP_LOG seal as objective

## Operating Protocol

1. **COLLEEN opens** — runs P-02 (COLLEEN-Trigger-Chain), surfaces all deferred BLGs from prior SWEEP_LOG
2. **Amethyst scopes** — reads state anchor (P-21), sets session wave plan
3. **Apogee parallel reads** — reads all target repos simultaneously, scores against 11Q
4. **Amethyst commits** — all commits gated; no agent commits without Amethyst sign-off
5. **COLLEEN registers** — all new BLGs logged, all closed BLGs marked with close reason (P-05)
6. **Amethyst seals** — emits P-21 state anchor at session close

## Output

- Sealed SWEEP_LOG entry
- Updated NDR Pattern Registry (if new patterns found)
- Updated CROSS_REF (if repos added/changed)
- P-21 State Anchor for next session handoff

## Escalation Path

If any commit touches LICENSE, NOTICE, or AXIS files → escalate to Harmonic Quintet (P-15) immediately.

---

## Failure Modes

| Mode | Condition | Response |
|------|-----------|----------|
| Apogee unavailable | Apogee cannot score artifact this wave | Amethyst solo-scores; BLG filed; wave continues |
| COLLEEN BLG queue stale | P-02 output is empty but prior SWEEP_LOG has open items | Re-run P-02 before proceeding; halt wave if queue unresolvable |
| Lane commit conflict | Two agents attempt writes to same file | Amethyst resolves via atomic rebase; conflicting agent defers |

## Idempotency Guarantee

Re-running this formation on the same wave state produces identical commits and no duplicate BLGs. COLLEEN deduplicates BLG IDs on surface; Amethyst rejects duplicate commits by SHA check.

## Rollback

Rollback path governed by P-09 (Agent Reciprocity). Any Trio-wave commit may be reverted via Reciprocity checkpoint within the same session. Post-session rollback requires Njineer approval.
