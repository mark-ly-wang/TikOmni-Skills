#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "tikomni-skill"

BLOCKED_FILE_PATTERNS = [
    re.compile(r"(^|/)\.env(\..+)?$"),
    re.compile(r"(^|/)\.source-meta\.json$"),
    re.compile(r"(^|/).*\.pem$"),
    re.compile(r"(^|/).*\.key$"),
    re.compile(r"(^|/).*\.p12$"),
    re.compile(r"(^|/).*\.local$"),
]

ALLOW_EXACT = {
    "skills/tikomni-skill/env.example",
}

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"gho_[A-Za-z0-9]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
]

TIKOMNI_KEY_LINE = re.compile(r"TIKOMNI_API_KEY\s*=\s*[\"']?([^\"'\n]+)[\"']?")
TIKOMNI_KEY_PLACEHOLDERS = {
    "tk_your_real_key_here",
    "your_key_here",
    "replace_me",
    "changeme",
    "<required>",
    "required",
}

violations = []

for p in SKILL.rglob("*"):
    if not p.is_file():
        continue
    rel = str(p.relative_to(ROOT)).replace('\\', '/')

    if rel in ALLOW_EXACT:
        # content scan is still applied below
        pass
    else:
        for pat in BLOCKED_FILE_PATTERNS:
            if pat.search(rel):
                violations.append(f"blocked file present: {rel}")
                break

    try:
        content = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        content = ""

    for sp in SECRET_PATTERNS:
        if sp.search(content):
            violations.append(f"secret-like pattern found in {rel}")
            break

    for m in TIKOMNI_KEY_LINE.finditer(content):
        value = m.group(1).strip().strip('"').strip("'")
        lower = value.lower()
        if value and lower not in TIKOMNI_KEY_PLACEHOLDERS and "your" not in lower and "replace" not in lower:
            violations.append(f"real-looking TIKOMNI_API_KEY found in {rel}")
            break

if violations:
    print("[FAIL] secret scan failed:")
    for v in violations:
        print(" -", v)
    sys.exit(1)

print("[OK] secret scan passed")
