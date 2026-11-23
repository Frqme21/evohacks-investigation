#!/usr/bin/env python3
"""Scan images and PDFs for embedded metadata.

Usage:
    python3 scan_file_metadata.py [path]
"""

from __future__ import annotations

import pathlib
import re
import struct
import sys


def scan_png(data: bytes) -> list[tuple[str, bytes]]:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return []
    found = []
    i = 8
    while i < len(data):
        if i + 8 > len(data):
            break
        length = struct.unpack(">I", data[i : i + 4])[0]
        chunk_type = data[i + 4 : i + 8].decode("latin1", "replace")
        chunk = data[i + 8 : i + 8 + length]
        if chunk_type in {"tEXt", "iTXt", "zTXt", "eXIf", "tIME"}:
            found.append((chunk_type, chunk[:160]))
        i += 12 + length
        if chunk_type == "IEND":
            break
    return found


def scan_jpeg(data: bytes) -> list[tuple[str, bytes]]:
    if data[:2] == b"\xff\xd8" and b"Exif" in data[:8192]:
        return [("JPEG-EXIF-marker", b"")]
    return []


def scan_pdf(data: bytes) -> list[tuple[str, bytes]]:
    if not data.startswith(b"%PDF"):
        return []
    found = []
    for key in [b"/CreationDate", b"/ModDate", b"/Producer", b"/Author", b"/Creator"]:
        m = re.search(key + br"\s*\(([^)]{0,120})\)", data)
        if m:
            found.append((key.decode(), m.group(1)[:120]))
    return found


def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(".")
    exts = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".pdf"}
    for p in sorted(root.rglob("*")):
        if ".git" in p.parts or not p.is_file() or p.suffix.lower() not in exts:
            continue
        data = p.read_bytes()
        meta = scan_png(data) + scan_jpeg(data) + scan_pdf(data)
        if meta:
            print(p)
            for k, v in meta:
                try:
                    text = v.decode("utf-8", "replace")
                except Exception:
                    text = repr(v)
                print(f"  {k}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
