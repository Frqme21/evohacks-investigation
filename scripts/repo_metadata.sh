#!/usr/bin/env bash
set -euo pipefail

# Usage: ./repo_metadata.sh owner/repo
# Prints key GitHub metadata and recent commits.

REPO="${1:?Usage: repo_metadata.sh owner/repo}"

echo "== Repo metadata =="
curl -s "https://api.github.com/repos/$REPO" | python3 -c '
import json, sys
d = json.load(sys.stdin)
for k in ["full_name","html_url","description","created_at","updated_at","pushed_at","size","fork","license","homepage","default_branch"]:
    v = d.get(k)
    if k == "license" and isinstance(v, dict):
        v = v.get("spdx_id")
    print(f"{k}: {v}")
'

echo
echo "== Recent commits =="
curl -s "https://api.github.com/repos/$REPO/commits?per_page=10" | python3 -c '
import json, sys
for c in json.load(sys.stdin):
    sha = c.get("sha","")[:12]
    commit = c.get("commit", {})
    author = commit.get("author", {})
    msg = commit.get("message", "").splitlines()[0]
    print(f"{sha} | {author.get(\"date\",\"?\")} | {author.get(\"name\",\"?\")} | {msg}")
'
