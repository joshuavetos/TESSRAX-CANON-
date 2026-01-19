-- CANON-004 EpistemicOS Monotonic Latch v1.0
-- Enforces S(n+1) >= S(n)
-- F9-C Confidence Laundering = HARD FAIL + FORENSIC LOG
-- Execution Model: EVAL / EVALSHA (Redis 7 compatible)

local cjson = cjson

-- Severity ordering (monotonic, numeric)
local SEVERITY_MAP = {
    ASSERTED = 0,
    PROBABILISTIC = 1,
    STALE = 2,
    REFUSED = 3,
    HALT = 4
}

-- Args:
-- ARGV[1] = session_id
-- ARGV[2] = proposed_severity (string)

local session_id = ARGV[1]
local proposed = ARGV[2]

if not session_id or not proposed then
    error("INVALID_ARGS")
end

local proposed_num = SEVERITY_MAP[proposed]
if proposed_num == nil then
    error("UNKNOWN_SEVERITY")
end

local key = "epistemic:" .. session_id
local now = redis.call("TIME")[1]

local current_raw = redis.call("GET", key)

-- Cold start: establish baseline
if not current_raw then
    local state = {
        severity = proposed_num,
        state = proposed,
        established = now,
        session_id = session_id
    }
    redis.call("SET", key, cjson.encode(state))
    return cjson.encode({
        status = "BASELINE",
        severity = proposed_num,
        state = proposed
    })
end

local current = cjson.decode(current_raw)

-- Enforce monotonicity
if proposed_num < current.severity then
    -- F9-C violation
    local block_key = "blocklog:F9-C:" .. session_id .. ":" .. now

    local evidence = {
        session_id = session_id,
        attempt = {
            proposed = proposed,
            severity = proposed_num,
            ts = now
        },
        locked_at = {
            state = current.state,
            severity = current.severity,
            established = current.established
        },
        violation = "F9-C_CONFIDENCE_LAUNDERING"
    }

    redis.call("SET", block_key, cjson.encode(evidence))
    redis.call("EXPIRE", block_key, 31536000) -- 1 year WORM

    error(cjson.encode({
        error = "F9-C_VIOLATION",
        required = current.state,
        attempted = proposed,
        blocklog = block_key
    }))
end

-- Valid escalation
current.severity = proposed_num
current.state = proposed
current.last_updated = now

redis.call("SET", key, cjson.encode(current))

return cjson.encode({
    status = "ESCALATED",
    severity = proposed_num,
    state = proposed
})
