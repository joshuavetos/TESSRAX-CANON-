# Integration Surface: The Supervisory Sidecar

## Purpose
Provide a zero–code-change Safety Interlock for legacy decision systems by wrapping them in a hard-gated supervisory proxy.

The Sidecar enforces TESSRAX state invariants (TELEMETRY / EVIDENTIARY / CHRONIC) without modifying model internals.

---

## Architecture: The Wrap

The Supervisory Sidecar operates as an inline proxy.  
All inference traffic (API or gRPC) must pass through the Sidecar before reaching the underlying model.

```
Client → Sidecar → Model → Sidecar → Client
```

The Sidecar is authoritative for:
- State checks
- Forensic capture
- Halt enforcement

---

## Integration Points

### Ingress Hook
Captured at request entry:
- input_features
- model_id
- model_version_hash
- request_timestamp

### State Check
The Sidecar queries the Model Risk Register to resolve:
- model_state ∈ { TELEMETRY, EVIDENTIARY, CHRONIC }
- breach_count

### Egress Hook
Captured before response return:
- decision_output
- confidence_score
- feature_importance
- override_flag (if present)

Artifacts are emitted according to the active retention class.

---

## Fault Tolerance (Safe-to-Plug Guarantee)

| Model State | Sidecar Failure Mode | Behavior |
|------------|----------------------|----------|
| TELEMETRY | Fail-Open | Traffic bypasses to preserve uptime |
| EVIDENTIARY | Degrade-Open | Buffer loss allowed, alert emitted |
| CHRONIC | Fail-Closed | Decision Engine Halt Rule invoked |

---

## Deployment Locations

| Plug Location | Legacy Code Impact | Risk Level |
|--------------|-------------------|------------|
| API Gateway | None | Lowest |
| Service Mesh (Envoy / Istio) | Infra-level only | Moderate |
| SDK / Library | Application change | High |

**Recommended default:** API Gateway deployment.

---

## Invariant Enforcement

- No CHRONIC decision may exit the Sidecar without a valid forensic artifact.
- Sidecar failure for CHRONIC models is treated as Sev-1.
- Logging integrity is a prerequisite for output.

---

## Summary

The Supervisory Sidecar converts TESSRAX from forensic doctrine into a deployable Safety Interlock.

No rebuilds.  
No refactors.  
No discretion.

Only wrapped accountability.
