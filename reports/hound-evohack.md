# Hound / rishith-c/hound-evohack

- **Repo:** https://github.com/rishith-c/hound-evohack
- **Live/demo context:** Repo identifies itself as "HOUND: EvoHacks 2 Devpost answers" in `evohacks/DEVPOST.md`.
- **Local clone inspected:** `/home/frqme/Desktop/test/hound-evohack`

## Summary

The public repo has timeline/provenance indicators that warrant review. Almost all project content was added in one commit, and several bundled artifacts contain dates from September 2026 and 2026-11-15, before the repo was created on 2026-11-22.

## Repo metadata

| Field | Value |
|---|---|
| Created | 2026-11-22T08:21:28Z |
| Pushed | 2026-11-22T18:22:26Z |
| Commits | 4 |
| Size | 34831 KB |

Source: https://api.github.com/repos/rishith-c/hound-evohack

## Evidence

### 1. Bulk import history

- Commit list: https://github.com/rishith-c/hound-evohack/commits/main
- Large import commit: `334bdab67959aeb27c11b2e37a4f7dadcaf4c3de` ("Import HOUND EvoHacks project", 2026-11-22 00:23:56 -0800)
- The import commit added 400+ files in one unsigned commit.

Screenshot target: commit list showing 4 commits on 2026-11-22 and the large file-add list on the import commit.

### 2. Embedded ZIP with 2026-09-04 internal dates

File: `mecanum-rover-cad-concept.zip`

Command:

```bash
python3 - <<'PY'
import zipfile
with zipfile.ZipFile('mecanum-rover-cad-concept.zip') as z:
    for i in z.infolist()[:15]:
        print(i.date_time, i.filename)
PY
```

Observed: entries dated `(2026, 9, 4, 19, 26, xx)`, including `mecanum-rover-cad-concept/CAD_BRIEF.md` and `parts/motor_mount.step`.

### 3. STEP CAD headers dated 2026-09-04

File: `models-SUPERSEDED/parts/motor_mount.step`

Command:

```bash
grep -n "FILE_NAME\|2026-09-04" models-SUPERSEDED/parts/motor_mount.step | head
```

Observed header:

```text
FILE_NAME('Open CASCADE Shape Model','2026-09-04T19:26:42',('Author'),(
'Open CASCADE STEP processor 7.7','Open CASCADE 7.7','Unknown');
```

### 4. Shopping/evidence files dated 2026-09-05

Files:

- `shopping/evidence/offer-index.json`
- `shopping/evidence/kit-search-nema17-mecanum.txt`

Observed:

- `offer-index.json` contains `"checked": "2026-09-05T03:58:53.336Z"` and other 2026-09-05 timestamps.
- `kit-search-nema17-mecanum.txt` contains `Search: Amazon US, 2026-09-05, "NEMA 17 mecanum wheel chassis kit robot"`.

### 5. Blender PNG metadata dated 2026-11-15

File: `ml/data/previews/person_00.png`

Command:

```bash
python3 - <<'PY'
import struct, pathlib
p = pathlib.Path('ml/data/previews/person_00.png')
b = p.read_bytes(); i = 8
while i < len(b):
    l = struct.unpack('>I', b[i:i+4])[0]
    t = b[i+4:i+8].decode('latin1', 'replace')
    c = b[i+8:i+8+l]
    if t in ('tEXt', 'iTXt', 'eXIf'):
        print(t, c[:120])
    i += 12 + l
    if t == 'IEND':
        break
PY
```

Observed: `tEXt b'Date\x002026/11/15 17:53:08'`, `File <untitled>`, `Scene Scene`, `Camera Camera`, `RenderTime 00:00.00`.

### 6. Embedded ZIP nearly identical to `models-SUPERSEDED/`

Command:

```bash
python3 - <<'PY'
import zipfile, os
with zipfile.ZipFile('mecanum-rover-cad-concept.zip') as z:
    zn = {n.split('/', 1)[1]: n for n in z.namelist() if not n.endswith('/')}
sn = []
for r, _, fs in os.walk('models-SUPERSEDED'):
    for f in fs:
        sn.append(os.path.relpath(os.path.join(r, f), 'models-SUPERSEDED'))
common = set(zn) & set(sn)
same = [n for n in common if z.read(zn[n]) == open(os.path.join('models-SUPERSEDED', n), 'rb').read()]
print('zip', len(zn), 'sup', len(sn), 'common', len(common), 'identical', len(same))
PY
```

Observed: `zip 53 sup 76 common 52 identical 51`.

## Bottom line

The repo has multiple pre-hackathon dates inside bundled CAD/shopping/image artifacts and almost no git development history. That combination is enough to justify asking where and when the work was created.
