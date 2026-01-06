# TESSRAX COLD-START PROTOCOL v0.1
## Reconstructable Truth Under Total System Failure

---

## Purpose

The Cold-Start Protocol defines the minimum conditions under which
truth can be reconstructed by humans after total digital failure.

If this protocol cannot be executed with paper, pens, and time,
the system is not safe.

---

## Core Principle

Truth is not stored.
Truth is reconstructed.

If reconstruction fails, sovereignty has already been lost.

---

## Cold-Start Assumptions

- No power
- No cloud access
- No databases
- No automation
- No LLMs
- Only printed logs and human reasoning

---

## Success Criterion

Five tired humans must be able to reach **≥99% agreement**
on system state within 48 hours.

If not, the system fails the protocol.

---

## Component 1: Canonical Ledger of Intent

Every critical action must generate a **human-readable receipt**.

### Format Constraints
- Fixed-width text (Markdown / CSV)
- Printable on A4
- No nested structures
- No JSON
- No binary encoding

### Required Fields
| Field | Description |
|---|---|
| Timestamp | When the action occurred |
| Actor_ID | Who initiated it |
| Action_Type | What was done |
| Evidence_Hash | Reference to supporting input |
| Gate_Status | L3 / L4 / REJECT |
| Risk_Delta | Change in systemic risk |
| Invariant_Protected | Safety rule enforced |

If a human cannot read one line and understand the decision,
the receipt is invalid.

---

## Component 2: Offline Forensic Replay (The X-Ray)

### Procedure
1. Disconnect all live systems
2. Print the ledger
3. Assemble five auditors
4. Reconstruct system state manually

### Test Questions
- Why did this decision happen?
- What alternatives were rejected?
- Which invariant prevented catastrophe?
- Where did risk spike?

If answers require live systems → FAIL.

---

## Component 3: Manual Override Muscle

### Weekly Re-Enactment
Once per week, humans must:
- Review all L4-sealed entries
- Write a one-sentence invariant summary
- Sign their name

No clicking.
No automation.
No delegation.

This prevents split-brain confabulation.

---

## Failure Modes

### Soft Failure
- Reconstruction possible but slow
- Humans disagree on causality
- ERT > 24 hours

### Hard Failure
- Reconstruction impossible
- Missing causal links
- Humans defer to authority
- Ledger unreadable

Hard failure = System already unsafe.

---

## Why This Matters

Disaster recovery focuses on uptime.
Cold-Start focuses on **understanding**.

A system that can restart but cannot be understood
will repeat its failure.

---

## Enforcement Rule

If Cold-Start fails:
- Freeze expansion
- Block automation growth
- Prioritize epistemic repair

Continuity is not allowed to override reconstructability.

---

## Final Invariant

If the box breaks
and humans cannot rebuild truth,
the box was never safe.

END PROTOCOL
