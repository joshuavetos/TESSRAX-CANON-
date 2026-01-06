# Foundational Claim Escrow

## Purpose
Guarantee recovery from dependency collapse without allowing unlimited governance mutation.

## Escrow Definition
- Escrow Amount: 5.0 STRUC units
- Write-locked
- Non-transferable

## Access Rule
Escrow funds may ONLY be used for claims tagged:
- type == Foundational

Examples:
- Identity rebind
- Domain rebind
- Canon re-anchor

## Recovery Mode
If Total_Budget < 0.1 AND Escrow > 0:
- System enters RECOVERY MODE
- Only legal output: a Foundational Structural claim

Escrow cannot be replenished.
