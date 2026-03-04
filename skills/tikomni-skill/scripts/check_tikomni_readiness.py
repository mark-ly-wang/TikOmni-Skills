#!/usr/bin/env python3
"""Canonical Tikomni runtime readiness check (non-secret output)."""

from __future__ import annotations

import argparse
import os

from config_loader import REPO_ROOT, SKILL_ROOT, config_get, load_tikomni_config, resolve_storage_paths
from tikomni_common import bootstrap_runtime_env, write_json_stdout


def main() -> None:
    parser = argparse.ArgumentParser(description="Check Tikomni runtime readiness without exposing secrets")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path (overrides runtime.env_file)")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    args = parser.parse_args()

    config, _ = load_tikomni_config(args.config)
    resolved_env_file = args.env_file or config_get(config, "runtime.env_file", None)
    api_key_env = args.api_key_env or config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")

    bootstrap = bootstrap_runtime_env(primary_env_file=resolved_env_file)

    key_source = bootstrap.get("key_source", {}).get(api_key_env)
    source_chain = bootstrap.get("source_chain", {}).get(api_key_env, [])
    key_is_present = bool((os.getenv(api_key_env) or "").strip())

    storage_paths = resolve_storage_paths(config)
    resolved_output_root = storage_paths.get("root_dir", "")
    skill_root_str = str(SKILL_ROOT.resolve())
    output_root_in_skill_dir = False
    if resolved_output_root:
        try:
            output_root_in_skill_dir = os.path.commonpath([resolved_output_root, skill_root_str]) == skill_root_str
        except Exception:
            output_root_in_skill_dir = False

    payload = {
        "ready": key_is_present,
        "api_key_env": api_key_env,
        "key_present": key_is_present,
        "key_source": key_source or "missing",
        "source_chain": source_chain,
        "priority": bootstrap.get("priority", ["process_env", ".env.local", ".env"]),
        "repo_root": bootstrap.get("repo_root") or str(REPO_ROOT.resolve()),
        "workspace_env": bootstrap.get("workspace_env"),
        "local_env": bootstrap.get("local_env"),
        "loaded_files": bootstrap.get("loaded_files", []),
        "storage_paths": storage_paths,
        "output_root_in_skill_dir": output_root_in_skill_dir,
    }
    write_json_stdout(payload)
    raise SystemExit(0 if key_is_present else 1)


if __name__ == "__main__":
    main()
