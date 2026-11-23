# EvoHacks investigation notes

Quick provenance and timeline checks for four EvoHacks-related projects. These notes are based on public repo metadata, git history, file metadata scans, and local inspection of cloned repos. They flag timeline/provenance indicators, not proof of a rule violation.

## Reports

- [Hound / rishith-c/hound-evohack](reports/hound-evohack.md) - review requested; several pre-hackathon date indicators found.
- [BillBack / MarvinRidgeMT/BillBack](reports/billback.md) - no strong red flags in a quick pass.
- [FindThem / DonaldStewart4/FindThem](reports/findthem.md) - no strong red flags in a quick pass.
- [Shelf Check / Arnav66692/shelf-check](reports/shelf-check.md) - no strong red flags in a quick pass.

## Scope

Each check looked at:

- GitHub repo metadata and commit timeline
- Bulk import vs incremental history
- Embedded old dates in files
- Image/PDF metadata
- Obvious copy/origin signals

This was not a full plagiarism comparison against external codebases.

## Scripts

The `scripts/` folder has the small scripts used for these checks: repo metadata fetch, image/PDF metadata scan, old date scan, and ZIP-vs-directory comparison.

