# Decision Engine Halt Rule

## Infra-Level Enforcement
if (model_state == CHRONIC && forensic_logging_fails) {
HALT_DECISIONS(model_id);
trigger_sev1(“Chronic model unlogged”);
}
## Enforcement Notes
- Applies only to CHRONIC models
- Logging failure is treated as a Sev-1 outage
- No degraded mode permitted
- No human override allowed

## Rationale
Chronic models without forensic memory are prohibited from producing decisions.

No memory. No output.
