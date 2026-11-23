# Inspection scripts

Small scripts used during the provenance/timeline checks.

## `repo_metadata.sh`

Fetch GitHub repo metadata and recent commits.

```bash
./scripts/repo_metadata.sh owner/repo
```

## `scan_file_metadata.py`

Scan PNG/JPG/JPEG/WEBP/GIF/PDF files for embedded metadata (PNG text/EXIF chunks, basic JPEG EXIF marker, PDF CreationDate/ModDate/Producer/Author/Creator).

```bash
python3 scripts/scan_file_metadata.py path/to/repo
```

## `scan_dates.py`

Find old date strings in files before a cutoff date. Skips files larger than `--max-bytes`.

```bash
python3 scripts/scan_dates.py path/to/repo --before 2026-11-20
```

## `compare_zip_dir.py`

Compare files inside a ZIP archive against a directory. Useful when a repo bundles an archive that may match another folder.

```bash
python3 scripts/compare_zip_dir.py archive.zip extracted-or-matching-dir
```
