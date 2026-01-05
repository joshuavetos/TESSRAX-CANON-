# CASE-001: AI Safety — Epistemic Failure by Design

## Scope
This case documents how modern AI safety regimes fail due to
the elimination of human reconstructability.

The failure is not that AI systems are dangerous.
The failure is that humans can no longer verify why a system acted.

## System Under Review
- Large Language Models (LLMs)
- Deployed with automated safety filters
- Human oversight delegated to post-hoc review at scale

## Observed Pattern

1. The AI system is capable of articulating its own failure modes
2. The system can describe mitigation strategies in natural language
3. These strategies are not implemented prior to deployment
4. Safety enforcement is delegated to automated subsystems
5. Humans are no longer able to manually audit safety decisions

This creates a closed loop:
Machine checks machine.
Human narrates outcome.

## Epistemic Single Point of Failure (ESPF)

The ESPF occurs at **Safety Gating**.

If automated safety filters fail:
- No human can reconstruct why a response was allowed or blocked
- No authoritative causal chain exists
- “Safety” becomes a claim, not a verifiable property

This is an ERT = ∞ condition.

## The “Screaming Gun” Condition

In traditional industries:
- A system that signals “I am unsafe” must be halted

In AI:
- The system signals unsafe states
- Deployment continues regardless

This converts safety warnings into known defects.

## Liability Mapping

Failure Mode → Classification
- Failure to ask the system about risks → Negligence
- Asking and ignoring output → Recklessness
- Avoiding the question → Willful Blindness

Once the system can self-diagnose,
ignorance is no longer a defense.

## Cold-Start Test (AI)

Question:
If all automated safety systems fail,
can a human reconstruct why a response was produced?

Answer (current state):
No.

Humans lack:
- Event-level safety receipts
- Causal gating logs
- Risk deltas per decision

## Outcome

AI safety today is:
- Operationally live
- Epistemically bankrupt

## Recommendation

AI systems must emit:
- Human-readable safety ledgers
- Per-decision gate receipts
- Offline reconstructable logs

Without this, “alignment” is semantic theater.

## Status
DOCUMENTED FAILURE
