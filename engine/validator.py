import datetime
from datetime import timezone

# VecScript v1.2 Authority Mapping
CAPABILITY_MATRIX = {
    "COURT": ["ROOT", "ADMIN"],
    "TREASURER": ["ROOT", "ADMIN", "USER"],
    "FEDERAL_LIQUIDATOR": ["ROOT", "ADMIN"]
}

REQUIRED_FIELDS = {
    "COURT": ["claimant_name", "case_number", "jurisdiction_code"],
    "TREASURER": ["claimant_name", "dormancy_context"],
    "FEDERAL_LIQUIDATOR": ["claimant_name", "failed_institution_name"]
}

EXCLUSION_INDICATORS = [
    "login_required", "aggregate_only", "admin_contact_only", "no_claimant_list", "sealed_docket"
]

MAX_STALENESS_DAYS = 365

class TessraxValidator:
    def __init__(self, current_system_state="IDLE"):
        self.current_state = current_system_state

    def enforce_mve(self, claim_data, artifact):
        violations = []
        
        # 1. Authority Gate (INV-7: Privilege Isolation)
        custodian = claim_data.get("custodian_class")
        provided_cap = claim_data.get("cap")
        
        if provided_cap not in CAPABILITY_MATRIX.get(custodian, []):
            violations.append(f"INV-7_BREACH: {custodian} cannot exercise {provided_cap} privileges")
            return "NERF", violations

        # 2. State Transition Gate (INV-1: Sequential State)
        requested_prev = claim_data.get("prev")
        if requested_prev != self.current_state:
            violations.append(f"INV-1_BREACH: State mismatch. Current: {self.current_state}, Claim: {requested_prev}")
            return "NERF", violations

        # 3. Exclusion Gate (Immediate Halt)
        metadata = artifact.get("metadata", {})
        for indicator in EXCLUSION_INDICATORS:
            if metadata.get(indicator) is True:
                violations.append(f"INV-3_BREACH: EXCLUSION_TRIGGERED: {indicator.upper()}")
                return "NERF", violations

        # 4. Required Field Lock (MVE Validation)
        required = REQUIRED_FIELDS.get(custodian, [])
        for field in required:
            if not artifact.get(field):
                violations.append(f"INV-3_BREACH: MVE_MISSING: {field}")

        # 5. Temporal Decay Check (INV-0: MAS Staleness)
        try:
            # Deterministic UTC handling
            ts_str = artifact["retrieval_timestamp"].replace("Z", "+00:00")
            retrieval = datetime.datetime.fromisoformat(ts_str)
            now = datetime.datetime.now(timezone.utc)
            delta_days = (now - retrieval).days

            if delta_days > MAX_STALENESS_DAYS:
                violations.append(f"INV-0_BREACH: TEMPORAL_DRIFT: {delta_days} days")
        except Exception:
            violations.append("INV-3_BREACH: TEMPORAL_ERROR: invalid_timestamp")
            return "NERF", violations

        # 6. Final State Commitment
        if any("BREACH" in v for v in violations):
            return "NERF", violations

        return "PASS", []
