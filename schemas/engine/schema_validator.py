import json
import jsonschema
from jsonschema import ValidationError
import os
import sys

class SchemaValidator:
    """
    TESSRAX Canonical Schema Validator.
    Enforces strict adherence to JSON schemas.
    Posture: Fail-Closed.
    """
    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self._schema = None

    def _load_schema(self) -> None:
        """Loads the JSON schema from the specified path."""
        if self._schema is None:
            if not os.path.exists(self.schema_path):
                raise FileNotFoundError(f"CRITICAL: Schema file not found at {self.schema_path}")
            try:
                with open(self.schema_path, 'r') as f:
                    self._schema = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"CRITICAL: Invalid JSON schema at {self.schema_path}: {e}")

    def validate(self, document: dict) -> tuple[bool, list[str]]:
        """
        Validates an incoming JSON document against the loaded schema.
        
        Returns:
            tuple[bool, list[str]]: (isValid, list_of_errors)
        """
        try:
            self._load_schema()
            jsonschema.validate(instance=document, schema=self._schema)
            return True, []
        except FileNotFoundError as e:
            return False, [str(e)]
        except ValueError as e:
            return False, [str(e)]
        except ValidationError as e:
            errors = []
            # Create a validator instance to fetch all errors, not just the first one
            validator_instance = jsonschema.Draft7Validator(self._schema)
            for error in sorted(validator_instance.iter_errors(document), key=str):
                path = '/'.join(map(str, error.path)) if error.path else 'root'
                errors.append(f"SCHEMA_VIOLATION: {error.message} (Path: {path})")
            return False, errors
        except Exception as e:
            return False, [f"SYSTEM_FAULT: Unexpected error during validation: {str(e)}"]

if __name__ == '__main__':
    # CLI Entrypoint for Pipeline Integration
    if len(sys.argv) != 3:
        print("Usage: python -m engine.schema_validator <schema_path> <document_path>")
        sys.exit(1)

    schema_file = sys.argv[1]
    document_file = sys.argv[2]

    if not os.path.exists(document_file):
        print(f"Error: Document file not found at {document_file}")
        sys.exit(1)

    try:
        with open(document_file, 'r') as f:
            doc = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON document at {document_file}: {e}")
        sys.exit(1)

    validator = SchemaValidator(schema_file)
    is_valid, error_list = validator.validate(doc)

    if is_valid:
        print(json.dumps({"status": "PASS", "file": document_file}, indent=2))
        sys.exit(0)
    else:
        print(json.dumps({"status": "FAIL", "file": document_file, "errors": error_list}, indent=2))
        sys.exit(1)
