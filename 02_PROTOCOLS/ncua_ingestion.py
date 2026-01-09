#!/usr/bin/env python3
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import os

def fetch_ncua_unclaimed(url, output_dir):
    """Fetch NCUA HTML and extract claimant table"""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, "unclaimed.html")
    with open(html_path, 'w') as f:
        f.write(response.text)
    
    tables = pd.read_html(html_path)
    if tables:
        tables[0].to_csv(os.path.join(output_dir, "unclaimed_raw.csv"), index=False)
    
    return html_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    
    fetch_ncua_unclaimed(args.url, args.output_dir)
