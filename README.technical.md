# DGAF-Framework — Technical & Agent-Facing Reference

> **Audience:** Agent Amethyst, Agent Apogee, Agent COLLEEN, Agent Sentinel, and all ensemble members; engineers integrating with DGAF  
> **Entry point for:** Gate specs · Pattern registry · Formation protocols · Session open/close procedures  
> **Compliance/governance entry point:** [`README.governance.md`](./README.governance.md)  
> **Architect:** Hensel, Andrew Vance · [@ndrorchestration](https://github.com/ndrorchestration)

---

## MDAR Loop — Master Cycle

```
Map → Diagnose → Act → Review
  ↑                        |
  └────────────────────────┘
     (each cycle = one phi-gate interval)
```

Every agent action occurs within an MDAR cycle. Cycles are time-bounded by the Acoustic Gate Chain (P-13). No artifact crosses a cycle boundary without Cadence gate confirmation.

---

## Gate Stack — Execution Order

| Priority | Gate | Pattern | Trigger | Owner |
|----------|------|---------|---------|-------|
| 1 (always) | GATE-ACO: Acoustic Chain | P-13 | Every synthesis cycle | Amethyst + DemiJoule |
| 2 (every artifact) | GATE-1111: 1-1-1-1 | P-10 | Pre-registry sign-off | Apogee |
| 3 (pre-deploy) | GATE-11Q: Hendecagonal | P-11 | Production deployment | Apogee + Sentinel |
| 4 (S-TIER/audit) | GATE-TEL: Telescopic Lens | P-12 | S-TIER cert · structural audit | Apogee + Amethyst |

Full specs: [`docs/gates/`](./docs/gates/)

---

## NDR Pattern Registry — Quick Reference

| Range | Domain |
|-------|--------|
| P-01–P-08 | Coherence, continuity, git hygiene, cross-platform sync |
| P-09–P-13 | AXIS enforcement, quality gates, acoustic temporal chain |
| P-14–P-15 | Formation protocols (Trio, Harmonic Quintet) |
| P-16–P-20 | Metadata hygiene, IP, issue triage, branding, Drive sync |
| P-21–P-24 | Session continuity, storage topology, taxonomy audit, canonical practice unit |

Full registry: [`docs/patterns/NDR_PATTERN_REGISTRY.md`](./docs/patterns/NDR_PATTERN_REGISTRY.md)

---

## Session Open Protocol (COLLEEN — P-02)

```
1. Read SESSION_ANCHOR.md  →  rehydrate open BLGs + priority queue
2. Run .operations/gate_compliance_check.py  →  surface P-24 gaps
3. Emit session priority queue to Amethyst
4. Amethyst opens wave; Apogee scores; Sentinel monitors
```

Checklist: [`.operations/sweep_session_init.md`](./.operations/sweep_session_init.md)

---

## Session Close Protocol (Amethyst — P-06 + P-21)

```
1. All repo fixes committed
2. SWEEP_LOG.md updated + buoy appended
3. CHANGELOG.md versioned
4. CROSS_REF.md updated
5. SESSION_ANCHOR.md overwritten (not appended)
6. Seal commit pushed (atomic — all files in one push_files call)
```

Checklist: [`.operations/seal_checklist.md`](./.operations/seal_checklist.md)

---

## Formation Reference

| Formation | Pattern | Agents | Use |
|-----------|---------|--------|-----|
| Trio | P-14 | Amethyst + Apogee + COLLEEN | Standard multi-repo sweep |
| Harmonic Quintet | P-15 | Trio + Reson + Sentinel | Seal commits; sovereign file changes |
| IP Sweep | — | Amethyst + Perplexity MCP | Research, external source integration |

---

## Key File Locations

```
DGAF-Framework/
├── README.md                          ← Public-facing entry point
├── README.governance.md               ← NIST/EU AI Act compliance reference
├── README.technical.md                ← This file — agent/engineer reference
├── SESSION_ANCHOR.md                  ← P-21 session state (overwrite pattern)
├── SWEEP_LOG.md                       ← Sealed audit trail
├── CHANGELOG.md                       ← Semantic versioned history
├── CROSS_REF.md                       ← Ecosystem artifact map
├── ENSEMBLE_ROSTER.md                 ← Canonical agent registry
├── docs/
│   ├── gates/
│   │   ├── GATE_UNIT_TEMPLATE.md      ← P-24 blank (copy to start new gate)
│   │   ├── ACOUSTIC_GATES.md          ← GATE-ACO (P-13) — CERTIFIED v2.0
│   │   ├── GATE_1111.md               ← GATE-1111 (P-10) — CERTIFIED v2.0
│   │   ├── GATE_11Q.md                ← GATE-11Q (P-11) — CERTIFIED v2.0
│   │   ├── TELESCOPIC_LENS.md         ← GATE-TEL (P-12) — CERTIFIED v2.0
│   │   └── GATE_SPECS.md              ← Gate index
│   ├── patterns/
│   │   └── NDR_PATTERN_REGISTRY.md    ← P-01 through P-24
│   ├── protocols/
│   │   └── MDAR_PROTOCOL_v1.md        ← Master cycle protocol
│   └── drafts/                        ← Staging area (P-03/P-11/P-18)
├── .operations/                       ← Maintainer-only ops tooling
│   ├── gate_compliance_check.py       ← P-24 compliance scanner
│   ├── sweep_session_init.md          ← Session open checklist
│   └── seal_checklist.md              ← Session close/seal checklist
└── .github/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

---

## ANDROMEDA-AXIS Declarations (P-09)

All agent actions are checked against four sovereign constraints:

| Declaration | Constraint |
|-------------|------------|
| COGNITIVE_SOVEREIGNTY | No agent may alter Njineer's epistemic autonomy or decision authority |
| BIOLOGICAL_INTEGRITY | No output may threaten physical or psychological integrity of the architect |
| TRANSVERSAL_GROWTH | All systems must support ongoing learning and capability expansion |
| ENTROPY_RESISTANCE | No action may increase systemic disorder beyond recoverable bounds |

Violation triggers `SYNC_LOCKED` escalation to Amethyst-Conductor immediately.

---

*License: Apache 2.0 · See [NOTICE](./NOTICE) for full attribution*  
*Governance spine: [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework)*
