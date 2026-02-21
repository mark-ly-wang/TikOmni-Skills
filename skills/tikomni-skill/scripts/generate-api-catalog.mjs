#!/usr/bin/env node

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HTTP_METHODS = [
  'get',
  'post',
  'put',
  'patch',
  'delete',
  'head',
  'options',
];
const PUBLIC_PREFIXES = ['/api/u1/v1/', '/api/u2/v1/'];
const DEFAULT_OPENAPI =
  'public/openapi/tikomni-openapi.full.with-u2.public.latest.json';
const DEFAULT_OUTPUT_DIR = 'skills/tikomni-skill/references/api-catalog';

const repoRoot = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  '../../..'
);

function argValue(name, fallback) {
  const idx = process.argv.indexOf(name);
  if (idx === -1) {
    return fallback;
  }
  const value = process.argv[idx + 1];
  if (!value || value.startsWith('--')) {
    return fallback;
  }
  return value;
}

function isRecord(value) {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function normalizePath(pathname) {
  if (typeof pathname !== 'string') {
    return '/';
  }
  const trimmed = pathname.trim();
  if (!trimmed) {
    return '/';
  }
  const withSlash = trimmed.startsWith('/') ? trimmed : `/${trimmed}`;
  const deduped = withSlash.replace(/\/{2,}/g, '/');
  return deduped.length > 1 ? deduped.replace(/\/$/, '') : deduped;
}

function isPublicPath(pathname) {
  return PUBLIC_PREFIXES.some((prefix) => pathname.startsWith(prefix));
}

function decodeRefSegment(segment) {
  return segment.replace(/~1/g, '/').replace(/~0/g, '~');
}

function resolveRef(spec, ref) {
  if (typeof ref !== 'string' || !ref.startsWith('#/')) {
    return null;
  }
  const segments = ref
    .slice(2)
    .split('/')
    .map((segment) => decodeRefSegment(segment));
  let current = spec;
  for (const segment of segments) {
    if (!isRecord(current) || !(segment in current)) {
      return null;
    }
    current = current[segment];
  }
  return current;
}

function resolveObject(spec, input, maxDepth = 8) {
  let current = input;
  for (let i = 0; i < maxDepth; i += 1) {
    if (!isRecord(current)) {
      return null;
    }
    if (typeof current.$ref !== 'string') {
      return current;
    }
    const resolved = resolveRef(spec, current.$ref);
    if (!isRecord(resolved)) {
      return current;
    }
    current = { ...resolved, ...current };
    delete current.$ref;
  }
  return isRecord(current) ? current : null;
}

function compactText(value, max = 160) {
  if (typeof value !== 'string') {
    return '';
  }
  const compact = value.replace(/\s+/g, ' ').trim();
  if (!compact) {
    return '';
  }
  if (compact.length <= max) {
    return compact;
  }
  return `${compact.slice(0, max - 3)}...`;
}

function getPlatform(pathname) {
  const segments = pathname.split('/').filter(Boolean);
  if (segments.length < 3 || segments[0] !== 'api') {
    return 'unknown';
  }
  if (segments[1] === 'u2') {
    return 'u2';
  }
  if (segments[1] === 'u1') {
    return segments[3] || 'unknown';
  }
  return 'unknown';
}

function mergeParameters(pathItem, operation) {
  const list = [];
  if (Array.isArray(pathItem.parameters)) {
    list.push(...pathItem.parameters);
  }
  if (Array.isArray(operation.parameters)) {
    list.push(...operation.parameters);
  }

  const unique = new Map();
  for (const item of list) {
    if (!isRecord(item)) {
      continue;
    }
    if (typeof item.$ref === 'string') {
      unique.set(`$ref:${item.$ref}`, item);
      continue;
    }
    const name = typeof item.name === 'string' ? item.name.trim() : '';
    const location =
      typeof item.in === 'string' ? item.in.trim().toLowerCase() : '';
    if (!name || !location) {
      continue;
    }
    unique.set(`${location}:${name.toLowerCase()}`, item);
  }
  return [...unique.values()];
}

function collectRequestBodyParams(spec, requestBodyLike) {
  const required = [];
  const optional = [];
  const requestBody = resolveObject(spec, requestBodyLike);
  if (!requestBody || !isRecord(requestBody.content)) {
    return { required, optional };
  }

  const media =
    requestBody.content['application/json'] ||
    Object.values(requestBody.content)[0];
  const mediaObj = isRecord(media) ? media : null;
  const schema = resolveObject(spec, mediaObj?.schema);
  if (!schema || !isRecord(schema)) {
    if (requestBody.required === true) {
      required.push('body');
    } else {
      optional.push('body');
    }
    return { required, optional };
  }

  if (!isRecord(schema.properties)) {
    if (requestBody.required === true) {
      required.push('body');
    } else {
      optional.push('body');
    }
    return { required, optional };
  }

  const requiredSet = new Set(
    Array.isArray(schema.required)
      ? schema.required.filter((key) => typeof key === 'string')
      : []
  );
  for (const key of Object.keys(schema.properties)) {
    const name = `body:${key}`;
    if (requiredSet.has(key)) {
      required.push(name);
    } else {
      optional.push(name);
    }
  }

  if (required.length === 0 && optional.length === 0) {
    if (requestBody.required === true) {
      required.push('body');
    } else {
      optional.push('body');
    }
  }

  return { required, optional };
}

function dedupeParams(params) {
  const set = new Set();
  const ordered = [];
  for (const param of params) {
    if (!param || set.has(param)) {
      continue;
    }
    set.add(param);
    ordered.push(param);
  }
  return ordered;
}

function suggestIntent(pathname, summary, tags) {
  const haystack =
    `${pathname} ${summary} ${(tags || []).join(' ')}`.toLowerCase();
  if (haystack.includes('/health/') || haystack.includes('health')) {
    return 'health';
  }
  if (
    haystack.includes('/services/audio/asr') ||
    haystack.includes('transcription') ||
    haystack.includes('subtitle')
  ) {
    return 'asr_transcription';
  }
  if (
    haystack.includes('fetch_user_post_videos') ||
    haystack.includes('fetch_home_notes') ||
    haystack.includes('get_user_notes') ||
    haystack.includes('home') ||
    haystack.includes('timeline')
  ) {
    return 'home_posts';
  }
  if (
    haystack.includes('user_profile') ||
    haystack.includes('fetch_user_info') ||
    haystack.includes('get_user_info') ||
    haystack.includes('profile')
  ) {
    return 'author_profile';
  }
  if (
    haystack.includes('fetch_one_video') ||
    haystack.includes('note_info') ||
    haystack.includes('detail') ||
    haystack.includes('post_detail')
  ) {
    return 'single_post';
  }
  if (haystack.includes('comment')) {
    return 'comments';
  }
  if (haystack.includes('search')) {
    return 'search';
  }
  if (
    haystack.includes('hot') ||
    haystack.includes('trending') ||
    haystack.includes('billboard')
  ) {
    return 'trend';
  }
  return 'other';
}

function formatParamList(list, maxItems = 8) {
  if (!list || list.length === 0) {
    return '-';
  }
  if (list.length <= maxItems) {
    return list.join(', ');
  }
  const head = list.slice(0, maxItems).join(', ');
  return `${head}, ...(+${list.length - maxItems})`;
}

function escapeCell(value) {
  if (typeof value !== 'string') {
    return String(value ?? '');
  }
  return value.replace(/\|/g, '\\|').replace(/\n/g, ' ').replace(/\r/g, ' ');
}

function sortByMethodAndPath(a, b) {
  if (a.path === b.path) {
    return (
      HTTP_METHODS.indexOf(a.method.toLowerCase()) -
      HTTP_METHODS.indexOf(b.method.toLowerCase())
    );
  }
  return a.path.localeCompare(b.path);
}

function buildOperations(spec) {
  const operations = [];
  if (!isRecord(spec.paths)) {
    return operations;
  }

  for (const [rawPath, pathItemLike] of Object.entries(spec.paths)) {
    const pathname = normalizePath(rawPath);
    if (!isPublicPath(pathname)) {
      continue;
    }

    const pathItem = isRecord(pathItemLike) ? pathItemLike : {};

    for (const method of HTTP_METHODS) {
      const opLike = pathItem[method];
      if (!isRecord(opLike)) {
        continue;
      }

      const operation = resolveObject(spec, opLike) || opLike;
      const summary = compactText(
        operation.summary ||
          operation.operationId ||
          `${method.toUpperCase()} ${pathname}`,
        140
      );
      const description = compactText(operation.description, 220);
      const tags = Array.isArray(operation.tags)
        ? operation.tags.filter((tag) => typeof tag === 'string')
        : [];

      const mergedParams = mergeParameters(pathItem, operation);
      const requiredParams = [];
      const optionalParams = [];

      for (const paramLike of mergedParams) {
        const param = resolveObject(spec, paramLike);
        if (!param || !isRecord(param)) {
          continue;
        }
        const name = typeof param.name === 'string' ? param.name.trim() : '';
        const location =
          typeof param.in === 'string' ? param.in.trim().toLowerCase() : '';
        if (!name || !location) {
          continue;
        }
        const fullName = `${location}:${name}`;
        if (param.required === true) {
          requiredParams.push(fullName);
        } else {
          optionalParams.push(fullName);
        }
      }

      const bodyParams = collectRequestBodyParams(spec, operation.requestBody);
      requiredParams.push(...bodyParams.required);
      optionalParams.push(...bodyParams.optional);

      const required = dedupeParams(requiredParams);
      const optional = dedupeParams(
        optionalParams.filter((item) => !required.includes(item))
      );

      operations.push({
        platform: getPlatform(pathname),
        method: method.toUpperCase(),
        path: pathname,
        summary,
        description,
        requiredParams: required,
        optionalParams: optional,
        tags,
        suggestedIntent: suggestIntent(pathname, summary, tags),
      });
    }
  }

  operations.sort(sortByMethodAndPath);
  return operations;
}

function buildIndexMarkdown(openapiFile, operations, grouped) {
  const now = new Date().toISOString();
  const lines = [];
  lines.push('# Tikomni API Catalog Index');
  lines.push('');
  lines.push(`- generated_at: ${now}`);
  lines.push(`- source_openapi: \`${openapiFile}\``);
  lines.push(`- total_operations: ${operations.length}`);
  lines.push('');
  lines.push('## Platforms');
  lines.push('');
  lines.push('| Platform | Operations | Catalog |');
  lines.push('| --- | ---: | --- |');

  const sortedPlatforms = Object.keys(grouped).sort(
    (a, b) => grouped[b].length - grouped[a].length
  );
  for (const platform of sortedPlatforms) {
    lines.push(
      `| ${platform} | ${grouped[platform].length} | [${platform}.md](./${platform}.md) |`
    );
  }

  lines.push('');
  lines.push('## Core References');
  lines.push('');
  lines.push(
    '- Douyin homepage: `GET /api/u1/v1/douyin/app/v3/handler_user_profile`, `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`'
  );
  lines.push(
    '- Xiaohongshu homepage: `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`, `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`'
  );
  lines.push(
    '- U2 ASR: `POST /api/u2/v1/services/audio/asr/transcription`, `GET /api/u2/v1/tasks/{task_id}`'
  );
  lines.push('');
  lines.push('## Selection Baseline');
  lines.push('');
  lines.push('1. Same platform + same intent: prefer `app > web_v2 > web`.');
  lines.push(
    '2. Douyin homepage default sort: latest (`sort_type=0`), switch to hot only when requested.'
  );
  lines.push(
    '3. Use fallback when core fields are missing even if HTTP is 2xx.'
  );
  lines.push('');

  return `${lines.join('\n')}\n`;
}

function buildPlatformMarkdown(platform, operations) {
  const lines = [];
  lines.push(`# ${platform} API Catalog`);
  lines.push('');
  lines.push(`- operation_count: ${operations.length}`);
  lines.push('');
  lines.push(
    '| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |'
  );
  lines.push('| --- | --- | --- | --- | --- | --- | --- |');

  for (const op of operations) {
    lines.push(
      `| ${escapeCell(op.method)} | ${escapeCell(op.path)} | ${escapeCell(op.summary)} | ${escapeCell(formatParamList(op.requiredParams))} | ${escapeCell(formatParamList(op.optionalParams))} | ${escapeCell(op.suggestedIntent)} | ${escapeCell(op.tags.join(', ') || '-')} |`
    );
  }

  lines.push('');
  return `${lines.join('\n')}\n`;
}

async function main() {
  const openapiFile = argValue('--openapi', DEFAULT_OPENAPI);
  const outputDir = argValue('--output', DEFAULT_OUTPUT_DIR);
  const openapiPath = path.join(repoRoot, openapiFile);
  const outputPath = path.join(repoRoot, outputDir);

  const raw = await readFile(openapiPath, 'utf8');
  const spec = JSON.parse(raw);
  const operations = buildOperations(spec);

  const grouped = {};
  for (const op of operations) {
    if (!grouped[op.platform]) {
      grouped[op.platform] = [];
    }
    grouped[op.platform].push(op);
  }

  await mkdir(outputPath, { recursive: true });

  const indexMarkdown = buildIndexMarkdown(openapiFile, operations, grouped);
  await writeFile(path.join(outputPath, 'index.md'), indexMarkdown, 'utf8');

  const platforms = Object.keys(grouped).sort();
  for (const platform of platforms) {
    const markdown = buildPlatformMarkdown(platform, grouped[platform]);
    await writeFile(path.join(outputPath, `${platform}.md`), markdown, 'utf8');
  }

  console.log(
    `[api-catalog] generated ${operations.length} operations into ${outputDir}`
  );
  console.log(`[api-catalog] generated ${platforms.length} platform files`);
}

main().catch((error) => {
  console.error('[api-catalog] failed:', error);
  process.exitCode = 1;
});
