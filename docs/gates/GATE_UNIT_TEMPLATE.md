# GATE UNIT TEMPLATE — Canonical Practice Unit

<!-- DGAF-Framework canonical gate spec unit template (P-24) -->
<!-- Copy this file to docs/gates/[GATE_ID].md or docs/protocols/[PROTOCOL_ID].md -->
<!-- Remove all HTML comments before committing -->

**Version:** 1.0  
**Maintained by:** Agent Amethyst  
**Template authority:** `DGAF-Framework/docs/gates/GATE_UNIT_TEMPLATE.md`  
**Pattern:** P-24 (Canonical Practice Unit)  

---

```
<!-- STATUS HEADER — required on every gate/protocol doc -->
Status:       DRAFT | REVIEW | CERTIFIED
Certified-by: Agent Apogee
Cert-date:    YYYY-MM-DD
Last-updated: YYYY-MM-DD (Session SXX)
```

---

# [GATE-ID]: Gate / Protocol Name

> One-sentence summary of what this gate enforces and why it exists in the MDAR loop.

---

## Rationale

One paragraph. Answer: **why does this gate exist?** What failure mode does it prevent? What PHDGE property does it protect (harmonic coherence, temporal integrity, sovereignty, IP, evidence quality)? Name the worst-case scenario if this gate were absent.

---

## Trigger Condition

| Field | Value |
|-------|-------|
| **Agent** | [Amethyst \| Apogee \| Sentinel \| COLLEEN \| Reson \| DemiJoule \| Herald \| Echolette \| Lyra \| Reciprocity] |
| **Event** | [Input received \| Output produced \| State transition \| Cycle boundary \| Session open/close \| Commit issued] |
| **Threshold** | [Numeric: e.g., `phi_ratio < 1.0` \| Symbolic: e.g., `drift_score > 0.80` \| Boolean: e.g., `quorum = false`] |
| **Frequency** | [Every cycle \| Every session \| On-demand \| On BLG detection] |
| **Hard dependency** | [Yes — blocks next gate \| No — advisory] |

---

## Passing State

Describe the condition that constitutes a clean pass. Include a schema example.

```json
{
  "gate": "[GATE-ID]",
  "status": "PASS",
  "agent": "[owner agent]",
  "phi_ratio": 1.618,
  "score": "≥ threshold",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

**Human-readable pass condition:** [Describe in one sentence what a passing artifact looks like.]

---

## Failing State

Describe what a failure looks like. Include a schema example and the immediate consequence.

```json
{
  "gate": "[GATE-ID]",
  "status": "FAIL",
  "agent": "[owner agent]",
  "reason": "[specific failure condition]",
  "escalation": "[Sentinel | Amethyst | Njineer]",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

**Immediate consequence:** [Block commit \| Escalate to Sentinel \| Surface as BLG \| Trigger SYNC_LOCKED]

---

## Recovery Protocol

Step-by-step remediation path from FAIL to PASS.

1. **Identify root cause** — [what diagnostic to run first]
2. **Remediation action** — [what agent takes what action]
3. **Re-test** — [what triggers re-evaluation of the gate]
4. **Escalation if unresolved** — [after N cycles / N minutes, escalate to: _____]
5. **Ionian Lock** — [if applicable: conditions under which the artifact is locked and iteration terminates]

---

## References

| Field | Value |
|-------|-------|
| **MDAR Protocol** | `docs/protocols/MDAR_PROTOCOL_v1.md` |
| **Related Gates** | [GATE-ID, GATE-ID] |
| **Parent Pattern** | [P-XX] |
| **NIST Control** | [e.g., GV-1.1 \| MS-2.5 \| AC-3] |
| **EU AI Act Article** | [e.g., Art. 9 \| Art. 13 \| Art. 17] \| N/A |
| **Supersedes** | [prior version file path or N/A] |

---

## Provenance

| Field | Value |
|-------|-------|
| **Gate ID** | [GATE-ID] |
| **Session** | [SXX] |
| **Date** | YYYY-MM-DD |
| **Author** | Agent Amethyst |
| **Certifier** | Agent Apogee |
| **Architect** | Hensel, Andrew Vance (Ndr / ndrorchestration) |
| **Governance spine** | [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) |
