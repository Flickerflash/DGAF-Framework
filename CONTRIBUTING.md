# Contributing

> **Governance:** DGAF / Agent Amethyst — All changes to this repository are subject to Sentinel CI/CD integrity enforcement. Contributions must pass governance checks before merge. See [DGAF-Framework](https://github.com/Flickerflash/DGAF-Framework) for spine documentation.

## Scope
This repository is the DGAF governance spine — agent role definitions, phi-harmonic gating specs, MDAR loop protocols, and NIST/OWASP alignment documentation.

## Development
- Keep changes small and reviewable.
- Prefer explicit, versioned documentation over informal notes.
- Update CHANGELOG.md for every meaningful change following Keep a Changelog conventions.

## Spec Changes
- Agent role changes must update the canonical role table in ARCHITECTURE docs.
- Any retired agent must be annotated `(retired — superseded by [Agent Name])` in historical entries.
- Do not remove historical changelog entries — annotate them.

## Pull Requests
- Explain which governance component is affected.
- Note whether the change affects agent roles, gating patterns, MDAR protocols, or compliance alignment.
