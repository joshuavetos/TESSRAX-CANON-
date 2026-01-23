use clap::Parser;
use chrono::NaiveDate;
use uuid::Uuid;

use vk01::audit::{audit, AuditRequest, Standing, AuditError};
use vk01::schema::{ArtifactReceipt, StateOut, StandingOut};
use vk01::crypto::CryptoProvider;

/// VK-01 — Statutory Defense Auditor
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Cli {
    /// Jurisdiction code (e.g. US-SD)
    #[arg(long)]
    jurisdiction: String,

    /// Debt type (CREDIT_CARD | MEDICAL)
    #[arg(long)]
    debt_type: String,

    /// Last Activity Date (YYYY-MM-DD)
    #[arg(long)]
    lad: String,

    /// As-of date (YYYY-MM-DD)
    #[arg(long)]
    as_of: String,

    /// Tolling detected flag (fail-closed)
    #[arg(long, default_value_t = false)]
    tolling: bool,

    /// Signing key (hex-encoded 32 bytes)
    #[arg(long, env = "VK01_SIGNING_KEY")]
    signing_key: String,
}

fn main() {
    let cli = Cli::parse();

    // --- Parse dates (INVALID INPUT => exit 1) ---
    let lad = match NaiveDate::parse_from_str(&cli.lad, "%Y-%m-%d") {
        Ok(d) => d,
        Err(_) => exit_error("Invalid LAD date format"),
    };

    let as_of = match NaiveDate::parse_from_str(&cli.as_of, "%Y-%m-%d") {
        Ok(d) => d,
        Err(_) => exit_error("Invalid as_of date format"),
    };

    // --- Build audit request ---
    let req = AuditRequest {
        jurisdiction: cli.jurisdiction.clone(),
        debt_type: cli.debt_type.clone(),
        lad,
        as_of,
        tolling_detected: cli.tolling,
    };

    // --- Run audit (HALT => exit 2) ---
    let standing = match audit(req.clone()) {
        Ok(s) => s,
        Err(e) => exit_halt(e),
    };

    // --- Crypto provider ---
    let key_bytes = decode_key(&cli.signing_key);
    let crypto = CryptoProvider::new(key_bytes);

    // --- Build receipt ---
    let receipt_id = format!(
        "VK-01-{}-{}",
        cli.jurisdiction.to_uppercase(),
        Uuid::new_v4()
    );

    let input_checksum = CryptoProvider::compute_input_checksum(&req);

    let (standing_out, exit_code) = match standing {
        Standing::Expired => (StandingOut::EXPIRED, 0),
        Standing::Active => (StandingOut::ACTIVE, 0),
    };

    let receipt = ArtifactReceipt {
        artifact_id: receipt_id,
        timestamp: chrono::Utc::now().to_rfc3339(),
        input_checksum,
        logic_version: "VK-01.v1.0-SD-LOCKED".to_string(),
        verification_path: "https://sdlegislature.gov/Statutes/Codified_Laws/2043694".to_string(),
        statute_hash: "sha256:d4f3b2a1c0e9876543210fedcba9876543210fedcba9876543210fedcba98765".to_string(),
        state_out: StateOut {
            standing: standing_out,
            elapsed_time: format_elapsed(lad, as_of),
            statutory_limit: "6 years".to_string(),
            tolling_events: if cli.tolling { 1 } else { 0 },
            halt_condition: None,
            signature: String::new(),
        },
    };

    // --- Sign receipt ---
    let signed = crypto.sign_receipt(receipt);

    // --- Emit JSON only ---
    println!(
        "{}",
        serde_json::to_string_pretty(&signed).expect("JSON serialization failed")
    );

    std::process::exit(exit_code);
}

// ----------------- Helpers -----------------

fn exit_error(msg: &str) -> ! {
    eprintln!("ERROR: {}", msg);
    std::process::exit(1);
}

fn exit_halt(err: AuditError) -> ! {
    eprintln!("{}", err);
    std::process::exit(2);
}

fn decode_key(hex_key: &str) -> [u8; 32] {
    let bytes = hex::decode(hex_key).expect("Invalid hex key");
    bytes.try_into().expect("Signing key must be 32 bytes")
}

fn format_elapsed(lad: NaiveDate, as_of: NaiveDate) -> String {
    let days = as_of.signed_duration_since(lad).num_days();
    let years = days / 365;
    let months = (days % 365) / 30;
    let rem_days = (days % 365) % 30;
    format!("{} years, {} months, {} days", years, months, rem_days)
}
