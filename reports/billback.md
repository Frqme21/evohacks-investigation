# BillBack / MarvinRidgeMT/BillBack

- **Repo:** https://github.com/MarvinRidgeMT/BillBack
- **Live site:** https://billback-ten.vercel.app/
- **Local clone inspected:** `/home/frqme/Desktop/test/BillBack`

## Summary

In a quick pass, I did not find strong provenance or timeline red flags. The git history is incremental across multiple authors. Old PDF metadata I found was mostly in downloaded hospital policy/source documents, which fits the app.

## Repo metadata

| Field | Value |
|---|---|
| Created | 2026-11-22T05:41:47Z |
| Updated | 2026-11-22T20:12:36Z |
| Pushed | 2026-11-22T17:34:34Z |
| Size | 9709 KB |
| Fork | No |
| License | MIT |

Source: https://api.github.com/repos/MarvinRidgeMT/BillBack

## Evidence

### 1. Incremental commit history

- Commits: https://github.com/MarvinRidgeMT/BillBack/commits/main
- History shows incremental feature, fix, docs, eval, and deploy commits on 2026-11-22.
- Git authors visible in history include Anish Meruva, Siddharth Tumati, Person B (`person-b@billback.local`), and abhinavmedisetty.

Screenshot target: commit list showing multiple authors and incremental commits, not one bulk import.

### 2. Old PDF metadata mostly in downloaded policy/source docs

Many files under `data/policies/*.pdf` have older PDF CreationDate/ModDate/XMP metadata (2011+ through 2025 in scanned examples). These appear to be downloaded hospital financial assistance policies used as source data.

Command:

```bash
python3 - <<'PY'
import os, re
for root, _, fs in os.walk('data/policies'):
    for f in fs:
        if not f.lower().endswith('.pdf'):
            continue
        b = open(os.path.join(root, f), 'rb').read()
        m = re.search(br'/CreationDate\s*\(([^)]{0,60})\)', b)
        if m:
            print(f, m.group(1).decode('latin1', 'replace'))
PY
```

Screenshot target: sample output showing old dates in `data/policies/*.pdf`.

### 3. Hackathon-generated PDFs are dated 2026-11-22

Sample/test PDFs such as `sample_bills/bill_02_text.pdf`, `sample_bills/bill_09_text.pdf`, and `backend/tests/fixtures/bills/bill_a_text.pdf` have 2026-11-22 CreationDate values and ReportLab producer metadata.

Command:

```bash
python3 - <<'PY'
import os, re
for folder in ['sample_bills', 'backend/tests/fixtures/bills']:
    for root, _, fs in os.walk(folder):
        for f in fs:
            if not f.lower().endswith('.pdf'):
                continue
            b = open(os.path.join(root, f), 'rb').read()
            m = re.search(br'/CreationDate\s*\(([^)]{0,60})\)', b)
            p = re.search(br'/Producer\s*\(([^)]{0,80})\)', b)
            print(os.path.join(root, f))
            if m: print('  CreationDate', m.group(1).decode('latin1','replace'))
            if p: print('  Producer', p.group(1).decode('latin1','replace'))
PY
```

### 4. No obvious embedded image metadata

A scan of PNG/JPG/JPEG/WEBP for PNG tEXt/iTXt/eXIf/tIME chunks and basic JPEG EXIF markers returned no obvious embedded metadata.

### 5. Copy/origin scan

A quick grep for `forked from`, `adapted from`, `based on`, and `copyright` did not turn up suspicious code-copy attribution. This was not a full plagiarism audit.

## Bottom line

The history and file dates I checked look consistent with a hackathon project that includes downloaded policy documents as data. I did not find a strong reason to flag it from this quick pass.
