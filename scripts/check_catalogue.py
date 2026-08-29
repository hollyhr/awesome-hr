#!/usr/bin/env python3
"""Enforce the Awesome HR catalogue floor and basic URL hygiene."""

from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, urlparse

README = Path(__file__).resolve().parents[1] / "README.md"
MINIMUM_RESOURCE_COUNT = 50
TRACKING_KEYS = {"ref", "referrer", "affiliate", "aff", "utm_source", "utm_medium", "utm_campaign"}

resource_pattern = re.compile(r"^- \[[^]]+\]\((https?://[^)]+)\)", re.MULTILINE)
contents = README.read_text(encoding="utf-8")
catalogue = contents.split("## UK employment essentials", 1)[1].split("## Contributing", 1)[0]
urls = resource_pattern.findall(catalogue)

errors: list[str] = []
if len(urls) < MINIMUM_RESOURCE_COUNT:
    errors.append(f"catalogue has {len(urls)} resources; minimum is {MINIMUM_RESOURCE_COUNT}")

duplicates = sorted({url for url in urls if urls.count(url) > 1})
if duplicates:
    errors.append("duplicate resource URLs: " + ", ".join(duplicates))

for url in urls:
    query_keys = {key.lower() for key in parse_qs(urlparse(url).query)}
    forbidden = sorted(query_keys & TRACKING_KEYS)
    if forbidden:
        errors.append(f"tracking parameters in {url}: {', '.join(forbidden)}")

if errors:
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"catalogue policy passed: {len(urls)} resources (target: 100)")
