"use strict";

const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

const PACKAGE_ROOT = path.resolve(__dirname, "..");
const SKILLS_ROOT = path.join(PACKAGE_ROOT, "skills");
const ALLOWLIST_FILE = path.join(PACKAGE_ROOT, ".skill-package-allowlist.txt");
const RUNTIME_ALIASES = {
  claude: "claude-code",
  "claude-code": "claude-code",
  codex: "codex",
  openclaw: "openclaw"
};

function listAvailableSkills() {
  const allowlistEntries = loadAllowlistEntries();
  if (allowlistEntries.length > 0) {
    return allowlistEntries
      .map((entry) => {
        const absolutePath = path.join(PACKAGE_ROOT, entry);
        return {
          name: path.basename(entry),
          relativePath: entry,
          absolutePath
        };
      })
      .filter((entry) => fs.existsSync(path.join(entry.absolutePath, "SKILL.md")));
  }

  return fs
    .readdirSync(SKILLS_ROOT, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => ({
      name: entry.name,
      relativePath: path.join("skills", entry.name),
      absolutePath: path.join(SKILLS_ROOT, entry.name)
    }))
    .filter((entry) => fs.existsSync(path.join(entry.absolutePath, "SKILL.md")));
}

function loadAllowlistEntries() {
  if (!fs.existsSync(ALLOWLIST_FILE)) {
    return [];
  }

  return fs
    .readFileSync(ALLOWLIST_FILE, "utf8")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#") && line.startsWith("skills/"));
}

function normalizeRuntime(runtime) {
  const normalized = RUNTIME_ALIASES[String(runtime || "").trim().toLowerCase()];
  if (!normalized) {
    throw new Error(`不支持的运行时: ${runtime}`);
  }
  return normalized;
}

function resolveRuntimeDestination(runtime, explicitDir) {
  if (explicitDir) {
    return path.resolve(explicitDir);
  }

  const normalizedRuntime = normalizeRuntime(runtime);
  if (normalizedRuntime === "codex") {
    const codexHome = process.env.CODEX_HOME || path.join(os.homedir(), ".codex");
    return path.join(codexHome, "skills");
  }

  if (normalizedRuntime === "claude-code") {
    if (process.env.CLAUDE_SKILLS_DIR) {
      return path.resolve(process.env.CLAUDE_SKILLS_DIR);
    }

    const claudeHome =
      process.env.CLAUDE_CODE_HOME ||
      process.env.CLAUDE_HOME ||
      path.join(os.homedir(), ".claude");
    return path.join(claudeHome, "skills");
  }

  if (process.env.OPENCLAW_SKILLS_DIR) {
    return path.resolve(process.env.OPENCLAW_SKILLS_DIR);
  }

  if (process.env.OPENCLAW_HOME) {
    return pickExistingOrDefault([
      path.join(process.env.OPENCLAW_HOME, "workspace", "skills"),
      path.join(process.env.OPENCLAW_HOME, "skills")
    ]);
  }

  return pickExistingOrDefault([
    path.join(os.homedir(), ".openclaw", "workspace", "skills"),
    path.join(os.homedir(), ".openclaw", "skills")
  ]);
}

function pickExistingOrDefault(candidates) {
  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) {
      return candidate;
    }
  }
  return candidates[0];
}

function resolveSkillSelection(skillNames) {
  const requested = skillNames.length === 0 ? ["all"] : skillNames;
  const availableSkills = listAvailableSkills();
  const byName = new Map(availableSkills.map((skill) => [skill.name, skill]));

  if (requested.includes("all")) {
    return availableSkills;
  }

  return requested.map((name) => {
    const skill = byName.get(name);
    if (!skill) {
      const candidates = availableSkills.map((entry) => entry.name).join(", ");
      throw new Error(`未知 skill: ${name}；可选值: ${candidates}`);
    }
    return skill;
  });
}

function installSkills(options) {
  const runtime = normalizeRuntime(options.runtime);
  const destinationRoot = resolveRuntimeDestination(runtime, options.explicitDir);
  const selectedSkills = resolveSkillSelection(options.skillNames || []);
  const force = Boolean(options.force);

  fs.mkdirSync(destinationRoot, { recursive: true });

  const installed = [];
  for (const skill of selectedSkills) {
    const targetPath = path.join(destinationRoot, skill.name);
    if (fs.existsSync(targetPath)) {
      if (!force) {
        throw new Error(`目标目录已存在: ${targetPath}；如需覆盖请加 --force`);
      }
      fs.rmSync(targetPath, { recursive: true, force: true });
    }

    fs.cpSync(skill.absolutePath, targetPath, { recursive: true });
    installed.push({
      name: skill.name,
      sourcePath: skill.absolutePath,
      targetPath
    });
  }

  return {
    runtime,
    destinationRoot,
    installed
  };
}

module.exports = {
  installSkills,
  listAvailableSkills,
  normalizeRuntime,
  resolveRuntimeDestination,
  resolveSkillSelection
};
