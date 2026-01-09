# 02_PROTOCOLS/ncua_normalization.py
"""
NCUA Unclaimed Deposits Normalization Pipeline
Authoritative schema per CANON-XXX Public Liability Surface Map
"""

import pandas as pd
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ClaimantRecord:
    claimant_full_name: str
    first_name: str
    last_name: str
    city: str
    state: str
    credit_union_name: str
    amount: float
    record_source: str
    retrieval_timestamp: str
    primary_key: str
    secondary_key: str
    is_us_territory: bool = False

class NCUANormalizer:
    US_STATES = {
        'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
        'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
        'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT',
        'VA','WA','WV','WI','WY'
    }
    TERRITORIES = {'PR','VI','GU','AS','MP'}

    def __init__(self):
        self.records: List[ClaimantRecord] = []

    @staticmethod
    def parse_name(full_name: str) -> Tuple[str, str]:
        full_name = full_name.strip().title()
        if ',' in full_name:
            last, rest = full_name.split(',', 1)
            first = rest.strip().split()[0] if rest else ""
            return first, last.strip()
        parts = full_name.split()
        return parts[0], " ".join(parts[1:]) if len(parts) > 1 else ""

    @staticmethod
    def clean_amount(amount_str: str) -> float:
        cleaned = re.sub(r'[^\d.]', '', str(amount_str))
        return float(cleaned) if cleaned else 0.0

    @staticmethod
    def generate_keys(r: ClaimantRecord) -> Tuple[str, str]:
        p = f"{r.claimant_full_name}|{r.city}|{r.state}".lower()
        s = f"{r.claimant_full_name}|{r.credit_union_name}".lower()
        return p, s

    def normalize_record(self, row: Dict) -> Optional[ClaimantRecord]:
        required = ['claimant','city','state','credit_union','amount']
        if not all(row.get(k) for k in required):
            return None

        first, last = self.parse_name(row['claimant'])
        rec = ClaimantRecord(
            claimant_full_name=row['claimant'].strip(),
            first_name=first,
            last_name=last,
            city=row['city'].title(),
            state=row['state'].upper(),
            credit_union_name=row['credit_union'].strip(),
            amount=self.clean_amount(row['amount']),
            record_source=row.get('source_url','unknown'),
            retrieval_timestamp=row.get('timestamp','unknown'),
            primary_key="",
            secondary_key=""
        )
        rec.primary_key, rec.secondary_key = self.generate_keys(rec)
        rec.is_us_territory = rec.state in self.TERRITORIES
        return rec

    def process_html_table(self, html: str, source_url: str) -> List[ClaimantRecord]:
        tables = pd.read_html(html)
        if not tables:
            return []

        df = tables[0]
        df.columns = df.columns.str.lower().str.strip()

        col_map = {
            'claimant': ['name','last name'],
            'city': ['city'],
            'state': ['state'],
            'credit_union': ['credit union'],
            'amount': ['amount']
        }

        mapped = {}
        for target, options in col_map.items():
            for col in df.columns:
                if any(o in col for o in options):
                    mapped[target] = col
                    break

        for k in col_map:
            if k not in mapped:
                raise ValueError(f"Missing column: {k}")

        for _, row in df[mapped.values()].iterrows():
            raw = row.to_dict()
            raw.update({
                'source_url': source_url,
                'timestamp': pd.Timestamp.now().isoformat()
            })
            rec = self.normalize_record(raw)
            if rec:
                self.records.append(rec)

        return self.records

    def export_canonical(self, path: Path) -> None:
        df = pd.DataFrame([r.__dict__ for r in self.records])
        df.to_csv(path, index=False)
