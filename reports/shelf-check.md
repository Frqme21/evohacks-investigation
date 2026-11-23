# Shelf Check / Arnav66692/shelf-check

- **Repo:** https://github.com/Arnav66692/shelf-check
- **Live site:** https://shelf-check-nu.vercel.app/
- **Local clone inspected:** `/home/frqme/Desktop/test/shelf-check`

## Summary

In a quick pass, I did not find strong provenance or timeline red flags. The repo has 155 commits by one author with incremental development after a large in-window initial commit. Old date strings I found were mostly in saved FDA/NIH API fixtures/data, and I did not find obvious embedded image/PDF metadata.

## Repo metadata

| Field | Value |
|---|---|
| Created | 2026-11-22T00:10:29Z |
| Updated | 2026-11-22T04:18:26Z |
| Pushed | 2026-11-22T20:01:07Z |
| Size | 35818 KB |
| Fork | No |
| License | None detected |
| Description | None set via GitHub API |
| README claim | “Built for EvoHacks 2 (Projects for Social Good), November 21 to 22, 2026.” |

Source: https://api.github.com/repos/Arnav66692/shelf-check

## Evidence

### 1. Commit history

- Commits: https://github.com/Arnav66692/shelf-check/commits/main
- 155 commits total, all by `Arnav66692`.
- First commit: `c564a5c26e4a3ef5ff77901232e780b45b3e9c17` (2026-11-21 16:10:29 -0800), "feat: Shelf Check, a medicine cabinet safety check built on official labels".
- The first commit added 393 files. After that, history is incremental with features, fixes, docs, and merges through 2026-11-22 12:01:06 -0800.

Commands:

```bash
git log --all --oneline | wc -l
git shortlog -sn --all
git show --stat --oneline c564a5c26e4a3ef5ff77901232e780b45b3e9c17 | head -20
git log --all --reverse --date=iso --pretty=format:'%H|%ad|%an|%s' | head -5
```

Screenshot target: commit count/author summary and the first commit stat showing 393 files.

### 2. No obvious embedded image/PDF metadata

A scan of PNG/JPG/JPEG/WEBP/GIF/PDF for PNG metadata chunks, basic JPEG EXIF markers, and PDF Creation/Mod/Producer/Author/Creator returned no obvious embedded metadata.

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
    elif b[:2] == b'\xff\xd8' and b'Exif' in b[:8192]:
        meta.append(('JPEG-EXIF', b''))
    elif b.startswith(b'%PDF'):
        for k in [b'/CreationDate', b'/ModDate', b'/Producer', b'/Author', b'/Creator']:
            m = re.search(k + br'\s*\(([^)]{0,60})\)', b)
            if m:
                meta.append((k.decode(), m.group(1)[:60]))
    if meta:
        print(p, meta)
PY
```

### 3. Old date strings mostly in saved API fixtures/data

A date scan excluding files over 500KB found 618 old-date hits. The hits I inspected were mostly in `lookup/fixtures/bodies/*` and `engine/fixtures/*`, where saved NIH DSLD/openFDA-style records contain historical dates (for example “Date entered into DSLD”, off-market dates). These look like expected source fixtures/data.

Command:

```bash
grep -RInE '2011-|2012-|2013-|2014-' lookup/fixtures engine/fixtures | head
```

### 4. Large bundled assets

Large files include `web/public/matcher/dinov2s-run3.q8.onnx` (~24.9MB), `engine/data/recalls.json` (~12.8MB), `web/public/matcher/gallery.i8` (~4.7MB), and `engine/data/pills.json` (~2.4MB). Their size alone is not a red flag, but provenance of bundled model/data assets is a reasonable follow-up question. I did not verify external provenance beyond the repo contents.

### 5. Copy/origin scan

A quick grep for `forked from`, `adapted from`, `copied from`, and similar markers did not turn up obvious copy attribution. Some tool scripts include a hardcoded local path (`/Users/arnavsingh/Desktop/Competitions/evohacks-2/shelf-check`), which looks like a local dev-environment artifact. This was not a full plagiarism audit.

## Bottom line

The main note is the large 393-file initial commit, but it is in the hackathon window and followed by extensive incremental history. I did not find strong provenance red flags in the quick metadata/date/origin scan.
