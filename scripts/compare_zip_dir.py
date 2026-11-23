#!/usr/bin/env python3
"""Compare files inside a zip against a directory.

Usage:
    python3 compare_zip_dir.py archive.zip directory [--zip-prefix prefix/]

Reports counts and lists differing/missing files.
"""

from __future__ import annotations

import argparse
import os
import zipfile


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("directory")
    ap.add_argument("--zip-prefix", default=None, help="Prefix inside zip to strip; auto-detected if omitted")
    args = ap.parse_args()

    with zipfile.ZipFile(args.zip_path) as z:
        names = [n for n in z.namelist() if not n.endswith("/")]
        prefix = args.zip_prefix
        if prefix is None:
            # auto-detect common top-level prefix
            first = names[0].split("/", 1)[0] + "/" if names else ""
            if first and all(n.startswith(first) for n in names):
                prefix = first
            else:
                prefix = ""
        zip_map = {n[len(prefix):]: n for n in names if n.startswith(prefix)}

    dir_files = []
    for r, _, fs in os.walk(args.directory):
        for f in fs:
            rel = os.path.relpath(os.path.join(r, f), args.directory)
            dir_files.append(rel)

    zip_set = set(zip_map)
    dir_set = set(dir_files)
    common = sorted(zip_set & dir_set)
    zip_only = sorted(zip_set - dir_set)
    dir_only = sorted(dir_set - zip_set)

    identical = []
    different = []
    with zipfile.ZipFile(args.zip_path) as z:
        for rel in common:
            zb = z.read(zip_map[rel])
            db = open(os.path.join(args.directory, rel), "rb").read()
            (identical if zb == db else different).append(rel)

    print(f"zip files: {len(zip_set)}")
    print(f"dir files: {len(dir_set)}")
    print(f"common: {len(common)}")
    print(f"identical: {len(identical)}")
    print(f"different: {len(different)}")
    print(f"zip-only: {len(zip_only)}")
    print(f"dir-only: {len(dir_only)}")

    for label, items in [("DIFFERENT", different), ("ZIP-ONLY", zip_only), ("DIR-ONLY", dir_only)]:
        if items:
            print(f"\n== {label} ==")
            for i in items:
                print(i)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
