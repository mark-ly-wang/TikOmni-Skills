"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

const {
  installSkills,
  listAvailableSkills,
  resolveRuntimeDestination
} = require("../lib/installer");

test("listAvailableSkills returns distributable skills", () => {
  const skills = listAvailableSkills().map((entry) => entry.name);
  assert.deepEqual(skills, [
    "meta-capability",
    "single-work-analysis",
    "creator-analysis"
  ]);
});

test("resolveRuntimeDestination respects CODEX_HOME", () => {
  const original = process.env.CODEX_HOME;
  const tempHome = fs.mkdtempSync(path.join(os.tmpdir(), "tikomni-codex-home-"));

  process.env.CODEX_HOME = tempHome;
  try {
    assert.equal(resolveRuntimeDestination("codex"), path.join(tempHome, "skills"));
  } finally {
    if (original === undefined) {
      delete process.env.CODEX_HOME;
    } else {
      process.env.CODEX_HOME = original;
    }
  }
});

test("installSkills copies a selected skill into the target directory", () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "tikomni-install-"));
  const destinationRoot = path.join(tempRoot, "skills");
  const result = installSkills({
    runtime: "codex",
    explicitDir: destinationRoot,
    skillNames: ["meta-capability"]
  });

  assert.equal(result.installed.length, 1);
  assert.ok(fs.existsSync(path.join(destinationRoot, "meta-capability", "SKILL.md")));
});

test("installSkills rejects overwriting without force", () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "tikomni-force-"));
  const destinationRoot = path.join(tempRoot, "skills");

  installSkills({
    runtime: "codex",
    explicitDir: destinationRoot,
    skillNames: ["meta-capability"]
  });

  assert.throws(
    () =>
      installSkills({
        runtime: "codex",
        explicitDir: destinationRoot,
        skillNames: ["meta-capability"]
      }),
    /--force/
  );
});
