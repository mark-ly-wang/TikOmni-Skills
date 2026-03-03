#!/usr/bin/env python3
from pathlib import Path
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(parents=True, exist_ok=True)
ALLOWLIST_FILE = ROOT / ".skill-package-allowlist.txt"
OUT = DIST / "tikomni-skill.skill"

if not ALLOWLIST_FILE.exists():
    print("[FAIL] .skill-package-allowlist.txt missing")
    sys.exit(1)

entries = []
for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    entries.append(line)

with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for rel in entries:
        src = ROOT / rel
        if src.is_dir():
            for f in sorted(src.rglob("*")):
                if f.is_file():
                    arc = str(f.relative_to(ROOT))
                    zf.write(f, arcname=arc)
        elif src.is_file():
            zf.write(src, arcname=rel)
        else:
            print(f"[FAIL] allowlist path missing: {rel}")
            sys.exit(1)

print(f"[OK] built {OUT}")
