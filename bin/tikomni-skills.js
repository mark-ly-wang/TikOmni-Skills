#!/usr/bin/env node
"use strict";

const {
  installSkills,
  listAvailableSkills
} = require("../lib/installer");

function printUsage() {
  console.log(`TikOmni Skills CLI

用法:
  tikomni-skills list
  tikomni-skills install <codex|claude-code|openclaw> <skill...|all> [--dir <path>] [--force]

示例:
  tikomni-skills list
  tikomni-skills install codex all
  tikomni-skills install claude-code creator-analysis
  tikomni-skills install openclaw meta-capability --dir "/custom/skills"
`);
}

function parseFlags(argv) {
  const positionals = [];
  let explicitDir = null;
  let force = false;
  let json = false;

  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === "--dir") {
      explicitDir = argv[index + 1];
      index += 1;
      continue;
    }
    if (token === "--force") {
      force = true;
      continue;
    }
    if (token === "--json") {
      json = true;
      continue;
    }
    positionals.push(token);
  }

  return {
    positionals,
    explicitDir,
    force,
    json
  };
}

function printList(asJson) {
  const skills = listAvailableSkills().map((entry) => entry.name);
  if (asJson) {
    console.log(JSON.stringify(skills, null, 2));
    return;
  }

  console.log("可安装 skills:");
  for (const skill of skills) {
    console.log(`- ${skill}`);
  }
}

function printInstallResult(result) {
  console.log(`运行时: ${result.runtime}`);
  console.log(`目标目录: ${result.destinationRoot}`);
  console.log("已安装:");
  for (const entry of result.installed) {
    console.log(`- ${entry.name} -> ${entry.targetPath}`);
  }

  if (result.runtime === "codex") {
    console.log("请重启 Codex 以加载新 skills。");
    return;
  }
  if (result.runtime === "claude-code") {
    console.log("请重启 Claude Code 以加载新 skills。");
    return;
  }
  console.log("请让 OpenClaw 重新加载 skills 目录。");
}

function main() {
  const argv = process.argv.slice(2);
  if (argv.length === 0 || argv.includes("--help") || argv.includes("-h")) {
    printUsage();
    return;
  }

  const { positionals, explicitDir, force, json } = parseFlags(argv);
  const [command, ...rest] = positionals;

  if (command === "list") {
    printList(json);
    return;
  }

  if (command === "install") {
    const [runtime, ...skills] = rest;
    if (!runtime) {
      throw new Error("install 命令必须提供运行时");
    }

    const result = installSkills({
      runtime,
      explicitDir,
      force,
      skillNames: skills
    });
    printInstallResult(result);
    return;
  }

  throw new Error(`未知命令: ${command}`);
}

try {
  main();
} catch (error) {
  console.error(`[FAIL] ${error.message}`);
  process.exitCode = 1;
}
