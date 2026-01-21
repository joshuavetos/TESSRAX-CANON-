# LIABILITY TRANSFER RECEIPT SPEC

Authority: PROTOCOL  
Status: ACTIVE  
Purpose: Formalize human override as an explicit, irreversible action.

## Definition
A Liability Transfer Receipt (LTR) is a signed artifact emitted when a human bypasses automated gates.

## Trigger Conditions
- Manual DB write
- Emergency override
- Out-of-band correction
- Direct state mutation

## Required Fields
- Operator Identity (human)
- Timestamp (UTC)
- Affected System / State
- Reason for Override (free text)
- Acknowledgement of Legitimacy Void

## Effects
- Automated legitimacy claims are permanently disabled for affected scope
- Subsequent outputs must reference this receipt
- No silent re-entry allowed

## Prohibitions
- No retroactive issuance
- No deletion or amendment
- No automation may issue LTRs

## Rationale
Discretion is permitted. Concealment is not.
