# PROTOCOL: FAAS_10_DAY_KILL_SPRINT

Status: OPERATIONAL  
Authority Level: PROTOCOL  
Mode: FAIL-CLOSED  
Purpose: Falsification, not validation

---

## PRODUCT DEFINITION

**Name:** The 10-Day Kill Sprint  
**Motto:** *We don’t validate. We falsify.*  
**Duration:** Fixed (10 business days)  
**Client Interaction:** Intake only; no collaboration  
**Outcome:** Binary verdict

**Deliverable:**  
- Kill Report (Forensic JSON + Executive Summary)

This protocol is a bounded adversarial stress test.  
It is not consulting, advising, or iterative design support.

---

## PHASE 1 — INGESTION & REJECTION (Days 1–2)

### Day 1: Vagueness Filter

**Input:** MECHANISM_ID Submission  
Required fields:
- Claim
- Assumptions
- Scale

**Checks:**
- Syntax: all fields populated
- Semantics: claim must be falsifiable

**Examples:**
- REJECT: “Improves developer velocity”
- ACCEPT: “Enforces memory safety without GC at N=1”

**Output:**  
- Ticket #[ID]: ACCEPTED  
- Ticket #[ID]: REJECTED (Reason: Vague / Non-Falsifiable)

Rejected mechanisms exit immediately.

---

### Day 2: Attack Surface Mapping

**Action:** Decompose accepted claim into attack vectors.

**Mapping Rules:**
- Scale claims → Physics Agent
- Cost claims → Economics Agent
- Usability claims → Human Factors Agent
- Failure semantics → Failure Agent

**Output Artifact:**  
`Agent_Directive.json`

This file defines the exact probes to be executed.  
No client review or modification is permitted.

---

## PHASE 2 — THE SWARM (Days 3–5)

All agents operate in parallel.  
No client contact is allowed during this phase.

---

### Day 3: Probe Class A & B  
**Focus:** Degradation & Boundaries

**Agents:** Physics, Economics  
**Queries:**
- “Show the silent degradation mode.”
- “Identify the scale where this collapses.”

**Early Kill Condition:**  
If any agent finds silent degradation (lies without signaling), the sprint halts.

**State:**  
- RUNNING  
- EARLY_KILL

---

### Day 4: Probe Class C  
**Focus:** Fail-Closed Semantics

**Agents:** Failure Semantics  
**Queries:**
- “Violate the input assumptions.”
- “Remove a dependency. Does it halt or lie?”

**Banned Outcome:** Graceful degradation  
**Required Outcome:** Hard failure / refusal

---

### Day 5: Probe Class D  
**Focus:** Human Operability

**Agents:** Tooling / Human Factors  
**Queries:**
- “The system is dead. Where is the proof?”
- “Time-to-Truth vs Value-of-Uptime?”

**Kill Condition:**  
If diagnosis cost exceeds system value → DEAD

---

## PHASE 3 — CONVERGENCE & VERDICT (Days 6–8)

### Day 6: Cross-Examination

**Action:** Compare agent outputs.

**Convergence Rule:**  
If ≥2 agents identify the same root failure → DEAD

Similarity is assessed by failure-class matching, not wording.

---

### Day 7: Survivor Stress Test (Optional)

Runs **only** if no kill has occurred.

**Action:** Governance Red Team  
**Focus:**  
- Can a human bypass the safety gate?
- Can enforcement be disabled under pressure?

Failure here marks the mechanism UNSTABLE.

---

### Day 8: Verdict Drafting

**Verdict States:**
- DEAD — Fatal kill condition identified
- UNSTABLE — Survives physics but fails economics or operability
- SURVIVOR — Passes all probes; canon-eligible

**Constraint:**  
No hedging language. No “it depends.”

---

## PHASE 4 — DELIVERY (Days 9–10)

### Day 9: Artifact Generation

**Outputs:**
- Executive Summary (1 page)
- Forensic_Log.json (full agent traces)
- Visual Proof (SURVIVOR only)

---

### Day 10: The “No” Meeting

**Duration:** 30 minutes  
**Script:**
1. “We found a fatal flaw.”
2. “Here is the proof.”
3. “Project is terminated.”

Or, rarely:
- “Mechanism survives. Canon ID issued.”

---

## CORE ENFORCEMENT RULES

- Verdicts are terminal.
- Re-entry requires material change to the mechanism.
- Silence is a valid terminal state.
- No optimization pressure overrides refusal.
- No collaboration loops exist by design.

---

## CANONIZATION RULE

Only mechanisms marked **SURVIVOR** are eligible for canon.  
Canon entries are residues of elimination, not endorsements.

---

## CLOSURE

This protocol is complete.  
No extensions are permitted without explicit authority grant.

End of file.
