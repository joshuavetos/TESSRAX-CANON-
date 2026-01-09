#!/usr/bin/env python3
import requests
import argparse
import os

def fetch_ncua(url, output_dir):
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "unclaimed.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    fetch_ncua(args.url, args.output_dir)
