# Sweep Session Init Checklist

**Pattern:** P-02 (COLLEEN-Trigger-Chain) | P-21 (Session-Boundary-State-Anchor)  
**Run at:** Every session open, before any commits  
**Owner:** Agent COLLEEN → handoff to Agent Amethyst  

---

## Step 1 — Read SESSION_ANCHOR.md

```
File: DGAF-Framework/SESSION_ANCHOR.md
Action: Read open BLGs, last seal status, Drive-GitHub sync status, priority queue
Owner: COLLEEN
```

- [ ] SESSION_ANCHOR.md read
- [ ] Open BLGs loaded into session priority queue
- [ ] NDR version confirmed: ____
- [ ] Last seal status: SEALED / PENDING
- [ ] Drive-GitHub sync delta: ✅ / ⚠️ (describe: ____)

---

## Step 2 — Run Gate Compliance Check (P-24)

```bash
python .operations/gate_compliance_check.py
```

- [ ] Compliance check run
- [ ] BLG-class gaps surfaced (count: ____)
- [ ] Gaps added to session priority queue per P-03

---

## Step 3 — COLLEEN-Trigger-Chain Output

Produce a compact priority queue for Amethyst:

```
SESSION [SXX] OPEN — [DATE] [TIME] EDT
Open BLGs:       [ID list or "none"]
P-24 gaps:       [count] files non-compliant
Drive delta:     ✅ / ⚠️
Priority queue:  1. [top item]  2. [item]  3. [item]
Formation:       [Trio / Quintet / IP Sweep / Solo]
```

- [ ] Priority queue emitted to Amethyst
- [ ] Formation selected for this session

---

## Step 4 — Confirm Scope

- [ ] Repos in scope this session: ____
- [ ] Phase target (S026 / S027 / S028 / ad-hoc): ____
- [ ] Seal expected this session: Yes / No

---

*Owner: COLLEEN · Conductor: Amethyst · Architect: Hensel, Andrew Vance*
