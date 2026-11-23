# FindThem / DonaldStewart4/FindThem

- **Repo:** https://github.com/DonaldStewart4/FindThem
- **Live site:** https://donaldstewart4.github.io/FindThem/
- **Local clone inspected:** `/home/frqme/Desktop/test/FindThem`

## Summary

In a quick pass, I did not find strong provenance or timeline red flags. The repo has incremental commits across two authors, no obvious embedded image/PDF metadata, and no suspicious old asset dates.

## Repo metadata

| Field | Value |
|---|---|
| Created | 2026-11-21T19:03:23Z |
| Updated | 2026-11-21T22:21:48Z |
| Pushed | 2026-11-22T19:34:56Z |
| Size | 8732 KB |
| Fork | No |
| GitHub Pages | Enabled |
| License | None detected |

Source: https://api.github.com/repos/DonaldStewart4/FindThem

## Evidence

### 1. Incremental commit history

- Commits: https://github.com/DonaldStewart4/FindThem/commits/main
- History runs from 2026-11-21 11:03:08 -0800 (`b1fe862`) to 2026-11-22 11:33:57 -0800 (`093b884`).
- Authors visible in history include DonaldStewart4 and Nathan Chacko.
- The sequence includes docs, engine, planner, tests, audits, UI fixes, and merges.

Command:

```bash
git log --all --reverse --date=iso --pretty=format:'%H|%ad|%an|%s' | head
git log --all --date=iso --pretty=format:'%H|%ad|%an|%s' | head
```

Screenshot target: commit list showing incremental development over 2026-11-21–22.

### 2. No obvious embedded image/PDF metadata

A scan of PNG/JPG/JPEG/WEBP/GIF/PDF for EXIF/tEXt/tIME/PDF creation metadata returned no obvious embedded metadata.

Command:

```bash
python3 - <<'PY'
import pathlib, struct, re
for p in pathlib.Path('.').rglob('*'):
    if '.git' in p.parts or not p.is_file():
        continue
    if p.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.pdf'}:
        continue
    b = p.read_bytes(); meta = []
    if b.startswith(b'\x89PNG\r\n\x1a\n'):
        i = 8
        while i < len(b):
            l = struct.unpack('>I', b[i:i+4])[0]
            t = b[i+4:i+8].decode('latin1', 'replace')
            c = b[i+8:i+8+l]
            if t in ('tEXt', 'iTXt', 'zTXt', 'eXIf', 'tIME'):
                meta.append((t, c[:80]))
            i += 12 + l
            if t == 'IEND':
                break
    elif b.startswith(b'%PDF'):
        for k in [b'/CreationDate', b'/ModDate', b'/Producer']:
            m = re.search(k + br'\s*\(([^)]{0,60})\)', b)
            if m:
                meta.append((k.decode(), m.group(1)[:60]))
    if meta:
        print(p, meta)
PY
```

### 3. Old date strings are explainable

A quick scan found 16 pre-hackathon/older date hits. They were in research/data/config contexts, including news article dates in `docs/research/cases-public.csv`, `compatibility_date` in `proxy/wrangler.toml`, and a test fixture version string in `tools/browser/twotab.mjs`. I did not see old asset creation dates suggesting prebuilt project media.

### 4. Copy/origin scan

A quick grep for `forked from`, `adapted from`, `based on`, `copyright`, and `EvoHacks` found normal attributions and project documentation (including OSM attribution and an EvoHacks II note in README/CLAUDE). No obvious fork/copy markers were found. This was not a full plagiarism audit.

## Bottom line

The commit history and metadata I checked look plausible for hackathon work. I did not find a strong reason to flag it from this quick pass.
