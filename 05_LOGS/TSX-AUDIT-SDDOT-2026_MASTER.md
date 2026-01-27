# TESSRAX MASTER AUDIT RECORD: TSX-AUDIT-SDDOT-2026-001
# STATUS: SEALED / RUPTURE CONFIRMED

## 1. REGISTRY LEDGER ENTRY (Canonical Index)
Date,Artifact_ID,Registry,Breach_Code,Status,Location
2026-01-27,TSX-AUDIT-SDDOT-2026-001,DOT-VMT_RealityRepo,INV-M,RUPTURE,05_LOGS/TSX-AUDIT-SDDOT-2026_MASTER.md

## 2. HASH CONTRACT (THC-v1)
*Enforcement Rule for this Artifact*
1. BINARY TARGETS: SHA-256 of raw file bytes (PDF/Images).
2. TEXT TARGETS: SHA-256 of NF-Clean (UTF-8, LF only) stream.
3. VIOLATION: Commit of `e3b0...` (Empty Hash) triggers IMMEDIATE HALT.

## 3. FORENSIC EVIDENCE (XBRL INSTANCE)
*To use: Extract the block below to .xml format.*

```xml
<?xml version="1.0" encoding="utf-8"?>
<xbrli:xbrl 
  xmlns:xbrli="[http://www.xbrl.org/2003/instance](http://www.xbrl.org/2003/instance)" 
  xmlns:link="[http://www.xbrl.org/2003/linkbase](http://www.xbrl.org/2003/linkbase)" 
  xmlns:xlink="[http://www.w3.org/1999/xlink](http://www.w3.org/1999/xlink)" 
  xmlns:iso4217="[http://www.xbrl.org/2003/iso4217](http://www.xbrl.org/2003/iso4217)" 
  xmlns:tsrx="[http://tessrax.io/taxonomy/2026/risk-overlay](http://tessrax.io/taxonomy/2026/risk-overlay)"
  xmlns:us-gaap="[http://fasb.org/us-gaap/2025-01-31](http://fasb.org/us-gaap/2025-01-31)">

  <link:schemaRef 
    xlink:type="simple" 
    xlink:href="[http://tessrax.io/taxonomy/2026/risk-overlay.xsd](http://tessrax.io/taxonomy/2026/risk-overlay.xsd)" />

  <xbrli:context id="FY2026_Forensic_Snapshot">
    <xbrli:entity>
      <xbrli:identifier scheme="[http://www.standards.gov/DOT](http://www.standards.gov/DOT)">SD-DOT-01</xbrli:identifier>
    </xbrli:entity>
    <xbrli:period>
      <xbrli:instant>2026-01-27</xbrli:instant>
    </xbrli:period>
  </xbrli:context>

  <xbrli:unit id="USD">
    <xbrli:measure>iso4217:USD</xbrli:measure>
  </xbrli:unit>
  <xbrli:unit id="Pure">
    <xbrli:measure>xbrli:pure</xbrli:measure>
  </xbrli:unit>
  <xbrli:unit id="Year">
    <xbrli:measure>xbrli:P1Y</xbrli:measure>
  </xbrli:unit>

  <tsrx:VerdictHash 
    contextRef="FY2026_Forensic_Snapshot" 
    tsrx:hashAlgo="SHA-256">[INSERT_SHA256_OF_PDF]</tsrx:VerdictHash>

  <tsrx:PreservationFundingDeficit 
    contextRef="FY2026_Forensic_Snapshot" 
    unitRef="USD" 
    decimals="-6">48000000</tsrx:PreservationFundingDeficit>

  <tsrx:CapitalMisallocationExpansion 
    contextRef="FY2026_Forensic_Snapshot" 
    unitRef="USD" 
    decimals="-6">95000000</tsrx:CapitalMisallocationExpansion>

  <tsrx:SyntheticSolvencyRatio 
    contextRef="FY2026_Forensic_Snapshot" 
    unitRef="Pure" 
    decimals="2">0.84</tsrx:SyntheticSolvencyRatio>

  <tsrx:TimeToInsolvency 
    contextRef="FY2026_Forensic_Snapshot" 
    unitRef="Year" 
    tsrx:horizonBasis="Compound O&M Inflation vs Flat Revenue"
    decimals="1">7.0</tsrx:TimeToInsolvency>

  <tsrx:MetaRegistrySignature 
    contextRef="FY2026_Forensic_Snapshot" 
    tsrx:registryId="DOT-VMT_RealityRepo"
    tsrx:artifactId="TSX-AUDIT-SDDOT-2026-001"
    tsrx:signerAuthority="Tessrax_Governance_Primitive_v1.3" />

  <tsrx:InvariantBreachFlag 
    contextRef="FY2026_Forensic_Snapshot" 
    unitRef="Pure">true</tsrx:InvariantBreachFlag>

  <tsrx:RegulatoryViolation 
    contextRef="FY2026_Forensic_Snapshot">23 CFR 515.13(c)</tsrx:RegulatoryViolation>

</xbrli:xbrl>
