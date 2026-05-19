import assert from 'node:assert/strict';

import { RESOURCES } from '../src/index.ts';

type MessageTree = Record<string, string | MessageTree>;

const SOURCE_LOCALE = 'en';
const PLACEHOLDER_RE = /{{\s*[\w.]+\s*}}/g;

function isMessageTree(value: unknown): value is MessageTree {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function flattenMessages(tree: MessageTree, prefix = ''): Record<string, string> {
  const result: Record<string, string> = {};

  for (const [key, value] of Object.entries(tree)) {
    const path = prefix ? `${prefix}.${key}` : key;

    if (typeof value === 'string') {
      result[path] = value;
      continue;
    }

    if (isMessageTree(value)) {
      Object.assign(result, flattenMessages(value, path));
      continue;
    }

    throw new Error(`Invalid i18n value at ${path}`);
  }

  return result;
}

function placeholders(value: string): string[] {
  return Array.from(value.matchAll(PLACEHOLDER_RE), ([match]) => match.replace(/\s+/g, '')).sort();
}

const sourceMessages = flattenMessages(RESOURCES[SOURCE_LOCALE]);
const sourceKeys = Object.keys(sourceMessages).sort();

for (const [locale, tree] of Object.entries(RESOURCES)) {
  const messages = flattenMessages(tree);
  const keys = Object.keys(messages).sort();

  assert.deepEqual(keys, sourceKeys, `${locale} must have the same i18n keys as ${SOURCE_LOCALE}`);

  for (const [key, value] of Object.entries(messages)) {
    assert.notEqual(value.trim(), '', `${locale}.${key} must not be empty`);
    assert.deepEqual(
      placeholders(value),
      placeholders(sourceMessages[key]),
      `${locale}.${key} must preserve placeholders from ${SOURCE_LOCALE}.${key}`,
    );
  }
}

