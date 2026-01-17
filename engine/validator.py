import datetime

REQUIRED_FIELDS = {
    "COURT": ["claimant_name", "case_number", "jurisdiction_code"],
    "TREASURER": ["claimant_name", "dormancy_context"],
    "FEDERAL_LIQUIDATOR": ["claimant_name", "failed_institution_name"]
}

EXCLUSION_INDICATORS = [
    "login_required",
    "aggregate_only",
    "admin_contact_only",
    "no_claimant_list",
    "sealed_docket"
]

FRESHNESS_DAYS = 365


class TessraxValidator:
    def enforce_mve(self, claim_data, artifact):
        violations = []
        custodian_class = claim_data.get("custodian_class")

        # 1. Exclusion Gate (Immediate Halt)
        metadata = artifact.get("metadata", {})
        for indicator in EXCLUSION_INDICATORS:
            if metadata.get(indicator) is True:
                violations.append(f"EXCLUSION_TRIGGERED: {indicator.upper()}")
                return "NERF", violations

        # 2. Required Field Lock
        required = REQUIRED_FIELDS.get(custodian_class, [])
        for field in required:
            if field not in artifact:
                violations.append(f"MVE_MISSING: {field}")

        # 3. Temporal Decay Check
        try:
            retrieval = datetime.datetime.fromisoformat(
                artifact["retrieval_timestamp"].replace("Z", "")
            )
            now = datetime.datetime.utcnow()
            days_stale = (now - retrieval).days

            if days_stale > FRESHNESS_DAYS:
                violations.append(f"TEMPORAL_DRIFT: {days_stale} days")
                if len(violations) == 1:
                    return "PARTIAL", violations
        except Exception:
            violations.append("TEMPORAL_ERROR: invalid_timestamp")
            return "NERF", violations

        # 4. Final Verdict
        if any("MVE_MISSING" in v or "EXCLUSION" in v for v in violations):
            return "NERF", violations

        return "PASS", []
