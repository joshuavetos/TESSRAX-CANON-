import unittest
import datetime
from engine.validator import TessraxValidator

def iso_days_ago(days: int) -> str:
    return (datetime.datetime.utcnow() - datetime.timedelta(days=days)).isoformat() + "Z"

def base_claim(custodian_class: str = "COURT") -> dict:
    return {"custodian_class": custodian_class}

def base_artifact() -> dict:
    return {
        "claimant_name": "ACME CORP",
        "case_number": "2023-CV-1234",
        "jurisdiction_code": "US-MO",
        "retrieval_timestamp": iso_days_ago(30),
        "metadata": {},
    }

class TestTessraxValidator(unittest.TestCase):

    def test_pass_clean_court_artifact(self):
        v = TessraxValidator()
        verdict, violations = v.enforce_mve(base_claim(), base_artifact())
        self.assertEqual(verdict, "PASS")
        self.assertEqual(violations, [])

    def test_exclusion_gate_halts_immediately(self):
        artifact = base_artifact()
        artifact["metadata"]["login_required"] = True

        v = TessraxValidator()
        verdict, violations = v.enforce_mve(base_claim(), artifact)

        self.assertEqual(verdict, "NERF")
        self.assertTrue(any("EXCLUSION_TRIGGERED" in x for x in violations))

    def test_missing_required_field_triggers_nerf(self):
        artifact = base_artifact()
        artifact.pop("case_number")

        v = TessraxValidator()
        verdict, violations = v.enforce_mve(base_claim(), artifact)

        self.assertEqual(verdict, "NERF")
        self.assertTrue(any("MVE_MISSING" in x for x in violations))

    def test_temporal_drift_returns_partial(self):
        artifact = base_artifact()
        artifact["retrieval_timestamp"] = iso_days_ago(400)

        v = TessraxValidator()
        verdict, violations = v.enforce_mve(base_claim(), artifact)

        self.assertEqual(verdict, "PARTIAL")
        self.assertTrue(any("TEMPORAL_DRIFT" in x for x in violations))

    def test_invalid_timestamp_halts(self):
        artifact = base_artifact()
        artifact["retrieval_timestamp"] = "not-a-timestamp"

        v = TessraxValidator()
        verdict, violations = v.enforce_mve(base_claim(), artifact)

        self.assertEqual(verdict, "NERF")
        self.assertTrue(any("TEMPORAL_ERROR" in x for x in violations))

    def test_treasurer_requires_dormancy_context(self):
        artifact = {
            "claimant_name": "ACME CORP",
            "retrieval_timestamp": iso_days_ago(10),
            "metadata": {},
        }

        v = TessraxValidator()
        verdict, violations = v.enforce_mve({"custodian_class": "TREASURER"}, artifact)

        self.assertEqual(verdict, "NERF")
        self.assertTrue(any("MVE_MISSING" in x for x in violations))

if __name__ == '__main__':
    unittest.main()
