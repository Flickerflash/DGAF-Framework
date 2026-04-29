# NDR Pattern Registry

**Version:** 1.3
**Maintained by:** Amethyst-Conductor
**Canonical home:** `DGAF-Framework/docs/patterns/NDR_PATTERN_REGISTRY.md`
**Last updated:** 2026-04-29 (Session 004 — Gate patterns P-10 through P-13 added)

---

## Registry

| ID | Pattern Name | Category | Spec | Use | Trigger |
|----|-------------|----------|------|-----|---------|
| P-01 | Agent-Roster-Synchronization | Coherence | When an agent is retired/renamed, all diagrams, NOTICE files, and CHANGELOG historical entries update atomically in the same commit sweep | Stale role label found in any diagram or doc | Agent name in diagram ≠ canonical role table |
| P-02 | COLLEEN-Trigger-Chain | Continuity | COLLEEN activates on session open to surface deferred gaps from prior SWEEP_LOG entries; output becomes the session priority queue | Every new sweep session | New session opened with no explicit priority list |
| P-03 | BLG-Surface-and-Defer | Gap Management | Surface newly found gaps immediately into SWEEP_LOG; defer if non-blocking; never silently drop | Any time a gap is found mid-wave that doesn’t block current commits | Gap found during read that isn’t in current wave scope |
| P-04 | NOTICE-Authority-Chain | Legal/Governance | Every repo has a NOTICE file attributing Njineer + DGAF-Framework spine link + license; CHANGELOG tracks agent-level changes | Repo missing NOTICE or NOTICE missing DGAF attribution | New repo created or NOTICE audit run |
| P-05 | False-Positive-Close | Audit Hygiene | Before closing a BLG, verify the item was actually a gap vs. already-compliant; log close reason explicitly in SWEEP_LOG | BLG item resolved | BLG marked closed in SWEEP_LOG |
| P-06 | Atomic-Sweep-Commit | Git Hygiene | All repo fixes land before the seal commit; seal commit updates SWEEP_LOG + CROSS_REF + NDR Registry simultaneously | End of each sweep wave | Wave complete, ready to seal |
| P-07 | DGAF-Callout-Block | Documentation | Every repo README includes a standardized DGAF governance callout block with spine link, agent attribution, and license badge | README audit or new repo creation | README missing DGAF callout |
| P-08 | Drive-GitHub-Delta | Cross-Platform Sync | COLLEEN diffs Drive master inventory against CROSS_REF to surface repos or docs that exist in one but not the other | Periodic or when Drive files are uploaded to session | Drive file list and CROSS_REF both accessible |
| P-09 | ANDROMEDA-AXIS-Enforcement | Sovereign Constraints | Any agent output, commit, or architectural decision is checked against the four AXIS declarations (COGNITIVE_SOVEREIGNTY, BIOLOGICAL_INTEGRITY, TRANSVERSAL_GROWTH, ENTROPY_RESISTANCE); violation triggers SYNC_LOCKED escalation to Amethyst-Conductor | All agent operations | Any decision that could contradict NDR-01 IONIAN mode constraints |
| P-10 | 1-1-1-1-Gate-Audit | Quality Gate / Normative | Four-pillar mandatory filter (Mathematically Coherent, Epistemically Honest, Non-Violative, Historically Sequential) applied to all outputs before registry sign-off; ≥ 3/4 per pillar over N ≥ 3 runs | Any artifact approaching the read-only registry or external publication surface | Output ready for sign-off or publication |
| P-11 | 11Q-Terminal-Gate | Quality Gate / Deployment | 11-gate sequential filter derived from hendecagonal lattice nodes; all 11 gates must pass at ≥ 3/4 before production deployment; owned by Agent Apogee | Pre-production hardening of any artifact | Artifact declared production-ready |
| P-12 | Telescopic-Lens-Audit | Quality Gate / Meta-Strategic | 4 altitudes (Macro/Mid/Tactical/Quantum) × 8 dimensions = 32 checkpoints; S-TIER requires ≥ 31/32; prevents Architext Bleed | Deep structural audit of any artifact or architectural claim | Pre-registry sign-off or S-TIER certification required |
| P-13 | Acoustic-Gate-Chain | Quality Gate / Temporal | Six sequential gates (Clef→Time Signature→Measures→Key→Phrase→Cadence) enforce temporal integrity; each gate is a hard dependency; Cadence gate triggers Ionian Lock and artifact hardening | Every orchestration cycle; any artifact entering synthesis phase | New synthesis cycle opened |

---

## Gate Spec Cross-Reference

| Pattern | Full Spec |
|---------|-----------|
| P-10 (1-1-1-1 Gate) | `docs/gates/GATE_1111.md` |
| P-11 (11Q Framework) | `docs/gates/GATE_11Q.md` |
| P-12 (Telescopic Lens) | `docs/gates/TELESCOPIC_LENS.md` |
| P-13 (Acoustic Gates) | `docs/gates/ACOUSTIC_GATES.md` |
| Master index | `docs/gates/GATE_SPECS.md` |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-29 | Initial registry — P-01 through P-07 |
| 1.1 | 2026-04-29 | P-08 Drive-GitHub-Delta added (Session 002) |
| 1.2 | 2026-04-29 | P-09 ANDROMEDA-AXIS-Enforcement added (Session 004) |
| 1.3 | 2026-04-29 | P-10 through P-13 added — full Yggdrasil gate stack hardened to registry (Session 004 / SYS-UPDATE-v53.1) |
