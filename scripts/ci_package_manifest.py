#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST_FILE = ROOT / ".skill-package-allowlist.txt"

if not ALLOWLIST_FILE.exists():
    print("[FAIL] .skill-package-allowlist.txt missing")
    sys.exit(1)

allowlist = set()
for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    allowlist.add(line)

missing = []
for rel in sorted(allowlist):
    p = ROOT / rel
    if not p.exists():
        missing.append(rel)

if missing:
    print("[FAIL] allowlist includes missing paths:")
    for m in missing:
        print(" -", m)
    sys.exit(1)

print(f"[OK] allowlist checked ({len(allowlist)} entries)")
