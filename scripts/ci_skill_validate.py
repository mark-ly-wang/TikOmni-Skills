#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "tikomni-skill"
SKILL_MD = SKILL / "SKILL.md"


def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    sys.exit(1)


if not SKILL_MD.exists():
    fail("skills/tikomni-skill/SKILL.md is missing")

text = SKILL_MD.read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not match:
    fail("SKILL.md frontmatter is missing")

frontmatter = match.group(1)
if "name:" not in frontmatter:
    fail("SKILL.md frontmatter missing 'name'")
if "description:" not in frontmatter:
    fail("SKILL.md frontmatter missing 'description'")

name_m = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
if not name_m:
    fail("SKILL.md name field empty")
name = name_m.group(1).strip().strip('"').strip("'")
if name != "tikomni-skill":
    fail(f"skill name must be 'tikomni-skill', got '{name}'")

if len(text.splitlines()) > 500:
    fail("SKILL.md too long (>500 lines), split into references/")

if not (SKILL / "references").exists():
    fail("references/ directory missing")

print("[OK] static skill validation passed")
