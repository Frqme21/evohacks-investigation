#!/usr/bin/env python3
"""Scan files for date strings that fall before a cutoff.

Usage:
    python3 scan_dates.py [path] [--before YYYY-MM-DD] [--max-bytes N]

Defaults:
    path: .
    --before: 2026-11-20
    --max-bytes: 2000000
"""

from __future__ import annotations

import argparse
import pathlib
import re


DATE_PATTERNS = [
    re.compile(r"20\d\d-\d\d-\d\d"),
    re.compile(r"20\d\d/\d\d/\d\d"),
    re.compile(
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+20\d\d",
        re.I,
    ),
]


def normalize(s: str) -> str | None:
    m = re.match(r"(20\d\d)-(\d\d)-(\d\d)", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r"(20\d\d)/(\d\d)/(\d\d)", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--before", default="2026-11-20")
    ap.add_argument("--max-bytes", type=int, default=2_000_000)
    args = ap.parse_args()

    root = pathlib.Path(args.path)
    before = args.before
    seen = set()
    total = 0

    for p in sorted(root.rglob("*")):
        if ".git" in p.parts or not p.is_file():
            continue
        try:
            if p.stat().st_size > args.max_bytes:
                continue
            text = p.read_bytes().decode("utf-8", errors="ignore")
        except Exception:
            continue

        for pat in DATE_PATTERNS:
            for m in pat.finditer(text):
                raw = m.group(0)
                norm = normalize(raw)
                if norm is None or norm >= before:
                    continue
                line = text[max(0, m.start() - 40) : m.end() + 60].replace("\n", " ")
                key = (norm, str(p), line[:80])
                if key in seen:
                    continue
                seen.add(key)
                total += 1
                print(f"{norm} | {p} | {line[:140]}")

    print(f"TOTAL {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
