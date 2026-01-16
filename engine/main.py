import json
import sys
from datetime import datetime
from jsonschema import Draft202012Validator

from engine.validator import TessraxValidator


ENGINE_VERSION = "v0.1.0"
SCHEMA_PATH = "schemas/claim_and_artifact.schema.json"


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        sys.exit(f"INPUT_ERROR: failed to load {path} ({e})")


def load_schema(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        sys.exit(f"SCHEMA_ERROR: failed to load schema ({e})")


def enforce_schema(schema, payload):
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)

    if errors:
        messages = []
        for e in errors:
            location = ".".join([str(p) for p in e.path])
            messages.append(f"SCHEMA_VIOLATION at '{location}': {e.message}")
        emit_receipt("NERF", messages)
        sys.exit(1)


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

    schema = load_schema(SCHEMA_PATH)

    # Schema enforcement happens BEFORE any logic
    enforce_schema(
        schema,
        {
            "claim_data": claim_data,
            "artifact": artifact,
        },
    )

    validator = TessraxValidator()
    verdict, violations = validator.enforce_mve(claim_data, artifact)

    emit_receipt(verdict, violations)

    if verdict != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
