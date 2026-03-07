#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    sys.exit(1)


skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").is_file())
if not skill_dirs:
    fail("no skills found under skills/")

for skill_dir in skill_dirs:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{skill_md.relative_to(ROOT)} frontmatter is missing")

    frontmatter = match.group(1)
    if "name:" not in frontmatter:
        fail(f"{skill_md.relative_to(ROOT)} frontmatter missing 'name'")
    if "description:" not in frontmatter:
        fail(f"{skill_md.relative_to(ROOT)} frontmatter missing 'description'")

    name_m = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
    if not name_m:
        fail(f"{skill_md.relative_to(ROOT)} name field empty")
    name = name_m.group(1).strip().strip('"').strip("'")
    expected_name = skill_dir.name
    if name != expected_name:
        fail(f"{skill_md.relative_to(ROOT)} name must be '{expected_name}', got '{name}'")

    if len(text.splitlines()) > 500:
        fail(f"{skill_md.relative_to(ROOT)} too long (>500 lines), split into references/")

    if not (skill_dir / "references").exists():
        fail(f"{skill_dir.relative_to(ROOT)}/references directory missing")

print(f"[OK] static skill validation passed ({len(skill_dirs)} skills)")
