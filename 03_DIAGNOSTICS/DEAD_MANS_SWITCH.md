# Diagnostic: Dead Man’s Switch

## Purpose
A Dead Man’s Switch reveals whether humans still own the system or merely operate inside it.

## Trigger
Run this diagnostic whenever a system claims “full automation” or “no human fallback.”

## Question
What single task must humans perform manually if the system fails tomorrow to prevent collapse?

## Method
Ignore high‑tech components.  
Identify the most boring dependency.

Examples:
- Manual ledger reconciliation
- Inventory state reconstruction
- Patient status derivation
- Access revocation authority

## Failure Signal
“If the system is down, we wait.”

## Decorative Switch Example
A “manual override” that requires the login server to be online.

## Interpretation
If no human can perform the task offline:
- the switch is decorative
- the system is already terminal

## Consequence
If the switch fails, the institution loses the ability to recover truth after a crash.

## Note
A Dead Man’s Switch is not a lever.  
It is trained memory.
