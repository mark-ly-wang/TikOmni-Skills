#!/usr/bin/env python3
from pathlib import Path
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(parents=True, exist_ok=True)
ALLOWLIST_FILE = ROOT / ".skill-package-allowlist.txt"

if not ALLOWLIST_FILE.exists():
    print("[FAIL] .skill-package-allowlist.txt missing")
    sys.exit(1)

entries = []
for line in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    entries.append(line)

if not entries:
    print("[FAIL] allowlist is empty")
    sys.exit(1)

built = []
for rel in entries:
    src = ROOT / rel
    if not src.exists():
        print(f"[FAIL] allowlist path missing: {rel}")
        sys.exit(1)

    skill_name = src.name if src.is_dir() else src.stem
    out = DIST / f"{skill_name}.skill"
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        if src.is_dir():
            for f in sorted(src.rglob("*")):
                if f.is_file():
                    arc = str(f.relative_to(ROOT))
                    zf.write(f, arcname=arc)
        else:
            zf.write(src, arcname=rel)
    built.append(out.name)

print(f"[OK] built {len(built)} skill package(s): {', '.join(built)}")
