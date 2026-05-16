<!-- TARGET-PATH: docs/D01-data/discover-china/04-validations.md -->

# 04 · 校验规则汇总

> Zod 共享:`system/packages/shared-schemas/src/china/*.ts`
> 错误码常量:`system/packages/shared-utils/src/errors/china.ts`
> 命名约定:`CHINA_<对象>_<字段>_<规则>`

## 1. `china_categories`

| 字段 | 规则 | 范围 / 正则 | 前端提示 | 错误码 |
|------|------|------------|---------|-------|
| `code` | 2 位 01–12 | `^(0[1-9]\|1[0-2])$` | 类目编码格式不正确 | `CHINA_CATEGORY_CODE_INVALID` |
| `name_i18n` | 必含 5 key | keys ⊇ `[zh,en,vi,th,id]` | 请补全 5 种语言的类目名称 | `CHINA_CATEGORY_NAME_I18N_MISSING` |
| `name_i18n[*]` | 每语 1–40 | `len ∈ [1,40]` | 类目名称最多 40 字 | `CHINA_CATEGORY_NAME_TOO_LONG` |
| `description_i18n` | 必含 5 key | 同上 | 请补全 5 种语言的类目说明 | `CHINA_CATEGORY_DESC_I18N_MISSING` |
| `description_i18n[*]` | 每语 1–200 | `len ∈ [1,200]` | 类目说明最多 200 字 | `CHINA_CATEGORY_DESC_TOO_LONG` |

## 2. `china_articles`

| 字段 | 规则 | 范围 / 正则 | 前端提示 | 错误码 |
|------|------|------------|---------|-------|
| `category_id` | 必填 + 存在 | UUID + FK | 请选择文章类目 | `CHINA_ARTICLE_CATEGORY_REQUIRED` / `CHINA_ARTICLE_CATEGORY_NOT_FOUND` |
| `code` | 12 位大写字母 + 数字,全局唯一 | `^[A-Z0-9]{12}$` | (不展示,系统生成) | `CHINA_ARTICLE_CODE_INVALID` / `CHINA_ARTICLE_CODE_DUPLICATE` |
| `title_pinyin` | 必填 1–200 | `len ∈ [1,200]` | 文章标题拼音最多 200 字 | `CHINA_ARTICLE_TITLE_PINYIN_LEN` |
| `title_i18n` | 必含 5 key | 同上 | 请补全 5 种语言的文章标题 | `CHINA_ARTICLE_TITLE_I18N_MISSING` |
| `title_i18n[*]` | 每语 1–40 | `len ∈ [1,40]` | 文章标题最多 40 字 | `CHINA_ARTICLE_TITLE_TOO_LONG` |
| `status` | 枚举 | `draft\|published` | — | `CHINA_ARTICLE_STATUS_INVALID` |
| 发布前置 | ≥ 1 条句子 | `count ≥ 1` | 请至少添加一条句子后再发布 | `CHINA_ARTICLE_PUBLISH_NO_SENTENCES` |

## 3. `china_sentences`

| 字段 | 规则 | 范围 / 正则 | 前端提示 | 错误码 |
|------|------|------------|---------|-------|
| `article_id` | 必填 + 存在 | UUID + FK | — | `CHINA_SENTENCE_ARTICLE_NOT_FOUND` |
| `seq_no` | 1..9999;`(article_id, seq_no)` 唯一 | `int ∈ [1,9999]` | (系统自动) | `CHINA_SENTENCE_SEQ_RANGE` / `CHINA_SENTENCE_SEQ_DUPLICATE` |
| `pinyin` | 必填 1–600 | `len ∈ [1,600]` | 句子拼音最多 600 字符 | `CHINA_SENTENCE_PINYIN_LEN` |
| `content_zh..id` | 必填 1–400 | 同 | 各语句子最多 400 字 | `CHINA_SENTENCE_CONTENT_<LANG>_LEN` |
| `audio_status` | 枚举 | `pending\|processing\|ready\|failed` | — | `CHINA_SENTENCE_AUDIO_STATUS_INVALID` |
| `audio_url_zh` | `audio_status='ready'` 时必填 | URL | — | `CHINA_SENTENCE_AUDIO_URL_REQUIRED` |

## 4. 通用响应结构

```ts
{
  code: 'CHINA_ARTICLE_TITLE_TOO_LONG',
  message: '文章标题最多 40 字',
  field: 'title_i18n.zh',
  meta: { max: 40, actual: 47 }
}
```

字数超长 toast 直接展示 `message`,并把光标定位到 `field`。

## 5. 多语言 locale 常量

```ts
// packages/shared-schemas/src/china/locales.ts
export const CHINA_LOCALES = ['zh','en','vi','th','id'] as const;
export type ChinaLocale = (typeof CHINA_LOCALES)[number];
```

兜底顺序:`<用户 locale>` → `en` → `zh`。
