from fastapi import FastAPI, HTTPException, Body
from typing import Any, Dict
import datetime

# Import the canonical validation function
# This function must return a receipt dict and NEVER raise on enforcement decisions
from engine.validate import validate_claim_artifact


app = FastAPI(
    title="TESSRAX EGaaS",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.post("/v0.1.0/validate")
async def validate_endpoint(
    claim: Dict[str, Any] = Body(...),
    artifact: Dict[str, Any] = Body(...),
):
    """
    Stateless Admissibility Gate.

    Always returns an enforcement receipt.
    PASS / PARTIAL / NERF are not errors.
    """
    try:
        # Execute canonical enforcement logic
        receipt = validate_claim_artifact(claim, artifact)

        # Attach API-layer metadata without mutating engine semantics
        receipt["_egaas"] = {
            "api_timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "version": "v0.1.0",
        }

        return receipt

    except Exception as e:
        # Wrapper failure only — never swallow engine semantics
        raise HTTPException(
            status_code=500,
            detail=f"EGaaS_WRAPPER_FAULT: {str(e)}",
        )


@app.get("/health")
async def health_check():
    return {
        "status": "ACTIVE",
        "mode": "FAIL_CLOSED",
        "version": "v0.1.0",
    }
