# Interface-Based Governance

## Problem
Prescriptive law creates entanglement.
Systems become legally indispensable.

## Solution
Govern boundaries, not behavior.

## Principles
- Laws define interfaces
- Compliance = passing tests
- Intent is irrelevant

## Implications
- No vendor-specific mandates
- No proprietary compliance paths
- No narrative audits

## Enforcement
Regulator acts as CI server.
Failure triggers automatic consequence.

## Outcome
Systems are penalized for indispensability.
## PARASITIC OVERLAY INTEGRATION (CANONICAL MECHANISM)

### Definition
A **Parasitic Overlay** is a governance integration pattern used when a superior verification or enforcement system cannot replace an existing host system. Instead of introducing a new workflow, UI, or decision surface, the overlay **impersonates a pre-trusted upstream identity** already privileged by the host, injecting higher-fidelity signals without triggering organizational or procedural immune responses.

The host system remains unchanged. The overlay survives by conforming to the host’s intake expectations while altering the truth content of what is ingested.

---

### Invariant 1 — Trust Inheritance
If a host system differentiates inputs by trust tier (e.g., direct input vs. referral vs. agency), the overlay **must enter through the highest-trust intake path** available.

- New dashboards → rejected  
- New workflows → rejected  
- New review rules → resisted  
- Pre-trusted upstream identity → accepted by default  

**Law**: Governance cannot demand trust; it must inherit it.

---

### Invariant 2 — Primary Artifact Dominance
Signals embedded in metadata, tags, side-channels, or auxiliary fields are **non-durable** and subject to stripping, ignorance, or denial.

**Law**: If the signal must survive contact with humans, it must be embedded in the *primary artifact* the human is forced to view.

- Metadata → ignorable  
- Notes → skippable  
- Attachments → optional  
- Primary artifact (first page / first surface) → unavoidable  

This converts verification from *optional context* into *visible reality*.

---

### Invariant 3 — Zero Workflow Mutation
Any integration that requires actors to:
- log into a new system
- learn a new interface
- change daily habits
- accept new responsibility

will be rejected via **process compliance** regardless of merit.

**Law**: Adoption probability approaches zero as required behavior change approaches one.

Parasitic overlays succeed by requiring **no conscious adoption decision**.

---

### Invariant 4 — Fail-Closed Injection
If verification cannot be completed to the required standard, **the artifact must not be generated at all**.

- Partial truth is forbidden
- Soft warnings are forbidden
- “Review later” states are forbidden

**Law**: The absence of an artifact is the only safe failure mode.

---

### Failure Modes and Defenses

| Failure Mode | Defense |
|-------------|---------|
| Metadata stripping | Signal embedded in primary artifact |
| Human discretion | Binary artifact existence (present / absent) |
| Process rejection | No workflow or UI changes |
| Trust skepticism | Entry via pre-trusted intake path |
| Denial | Visual, first-surface irreversibility |

---

### Generalization Scope
This pattern applies wherever:
- A legacy system controls intake
- Trust tiers already exist
- Human review is unavoidable
- Replacement is politically or operationally impossible

Examples (non-exhaustive):
- ATS / hiring systems
- Legal filings
- Insurance claims
- Compliance submissions
- Audit artifacts
- Safety certifications

---

### Canonical Summary
**Parasitic Overlay Integration** is governance that survives not by permission, but by inevitability.  
It does not ask the host system to change.  
It ensures the host system cannot unknow what it has already accepted.
