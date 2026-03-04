# Customization Guide

## 0. Start from Configuration

1. Update environment values in `.env` (`TIKOMNI_API_KEY` is required).
2. Edit `references/runtime-config.md` to set output folders, markdown defaults, and execution policy.
3. If the user provides a custom config path, use that file as the first config source.

## 1. What Can Be Extended

1. New intent routing rules.
2. Field normalization mapping.
3. Markdown templates.
4. New fixed playbooks.

## 2. Required Definition for New Capabilities

Every new capability must define:

1. Input schema.
2. Primary/secondary endpoint chain.
3. Fallback conditions and fallback limits.
4. Markdown output template.

## 3. Non-Negotiable Rules

1. Douyin copy extraction always goes through U2.
2. Xiaohongshu copy extraction is subtitle-first with U2 fallback.
3. Once homepage extraction is matched, do not switch to free routing.
