import json
import sys
from datetime import datetime
from validator import TessraxValidator  # assumes this file is engine/validator.py


ENGINE_VERSION = "v0.1.0"


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        sys.exit(f"INPUT_ERROR: failed to load {path} ({e})")


def emit_receipt(verdict, violations):
    receipt = {
        "engine_version": ENGINE_VERSION,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "verdict": verdict,
        "violations": violations,
    }
    print(json.dumps(receipt, indent=2))


def main():
    if len(sys.argv) != 3:
        sys.exit(
            "USAGE_ERROR: python -m engine.main <claim_data.json> <artifact.json>"
        )

    claim_data_path = sys.argv[1]
    artifact_path = sys.argv[2]

    claim_data = load_json(claim_data_path)
    artifact = load_json(artifact_path)

    validator = TessraxValidator()
    verdict, violations = validator.enforce_mve(claim_data, artifact)

    emit_receipt(verdict, violations)

    if verdict != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
