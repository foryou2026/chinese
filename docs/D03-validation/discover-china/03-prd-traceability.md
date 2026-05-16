<!-- TARGET-PATH: docs/D03-validation/discover-china/03-prd-traceability.md -->

# D03-V03 · PRD 回链校验 · discover-china

> 矩阵:C01 R-ID × C05 BR × D01 实体 / 字段 × D02 OP-ID。
> 检查时间:2026-05-16(批次 6)。

## 完整追溯矩阵

| R-ID | C05 BR | D01 实体 / 字段 | D02 OP-ID | 状态 |
|------|--------|----------------|----------|------|
| R-001 | BR-01 | `china_categories.*`(12 种子) | OP-C1 | ✅ |
| R-002 | BR-02 | `china_articles.code` + `category_id` | OP-C2 | ✅ |
| R-003 | BR-05 | `china_articles.status` + `published_at` | OP-C3 | ✅ |
| R-004 | BR-10 | `china_sentences.audio_*` | OP-C4 | ✅ |
| R-005 | BR-10 | `china_sentences.audio_url_zh`(ready 集) | OP-C5 | ✅ |
| R-006 | BR-10 | `china_sentences.audio_status='failed'` 允许重试 | OP-C4(failed → processing) | ✅ |
| R-007 | BR-02 + BR-12 | `china_articles.title_i18n` + `content_*` ILIKE | OP-C2(q) | ✅ |
| R-008 | BR-07 | `china_sentences.seq_no` + `pinyin` + `content_*` | OP-A9 | ✅ |
| R-009 | BR-01 | `china_categories` COUNT 派生 | OP-A1 | ✅ |
| R-010 | BR-02 + BR-03 | `china_articles.status` + `deleted_at` | OP-A2 | ✅ |
| R-011 | — | `china_articles` 全字段 | OP-A3 | ✅ |
| R-012 | BR-02 + BR-05 | `china_articles`(INSERT,默认 draft) | OP-A4 | ✅ |
| R-013 | BR-11 | `china_articles`(部分更新) | OP-A5 | ✅ |
| R-014 | BR-05 | `china_articles.status='published'` | OP-A6 | ✅ |
| R-015 | BR-04 + BR-06 | `china_articles.status='draft'` + 清进度 | OP-A7 | ✅ |
| R-016 | BR-07 + BR-08 + BR-09 | `china_sentences` 全 CRUD + RPC | OP-A11 / A12 / A13 / A14 + OP-A15 | ✅ |
| R-017 | BR-03 + BR-06 | `china_articles.deleted_at` + cron | OP-A8 | ✅ |
| R-018 | BR-07 | `seq_label = padStart(4)` + `audio.url` | OP-C3 / OP-C4 出参 | ✅ |
| R-019 | BR-01 + BR-12 | `china_categories.name_i18n` 完整 5 语 | OP-C1 / OP-A1 | ✅ |
| R-020 | BR-09 | `fn_clear_progress_by_article` 跨域调用 | OP-A7 / A8 / A11 / A13 / A14 | ✅ |

合计 **20 / 20 R-ID 通过追溯**,无悬挂需求。

## 跨域副作用追溯

| 副作用 | 触发端点 | 跨域目标 | 契约位置 |
|--------|---------|---------|---------|
| 清空 `learning_progress where source='china' and source_code=<code>` | OP-A7 / A8 / A11(start\|after) / A13 / A14 | learning-engine 域 | D01-data/discover-china/03-business-rules.md §3 + D02-api/discover-china/06-events.md |
| `pg_notify('china_article_published')` | OP-A6 | api-app / api-admin 应用层缓存 | D02-api/discover-china/06-events.md |
| Storage `china-tts/{code}/{seq}.mp3` 写入 | OP-C4 | Storage 桶 / cron `cron_china_purge_orphan_audio` | D01-data/discover-china/05-calculations.md §6 |

✅ 全部跨域副作用契约明确;调用点 + 接收方 + 清理 cron 三层闭合。

## PRD § 边界与不变量追溯

[`docs/C01-requirements/discover-china/baseline.md` §4](../../C01-requirements/discover-china/baseline.md) 的 5 条不变量:

| 不变量 | D01 / D02 落地 |
|--------|---------------|
| 5 语 locale 严格 `{zh,en,vi,th,id}` | D01 三表 jsonb CHECK + D02 04-error-codes.md `CHINA_*_I18N_MISSING` |
| 文章 code `^[A-Z0-9]{12}$` UI / API 字符串 | D01 02-entities/china_articles.md + D02 02-overview.md §1 |
| 句子 seq_no UI 4 位补零 | D01 02-entities/china_sentences.md + D02 出参 `seq_label` |
| TTS 缓存键 `china-tts/{article_code}/{seq_no_padded}.mp3` | D01 02-entities/china_sentences.md + 05-calculations.md §3 + D02 02-app-tts.md |
| 软删 30 天不可恢复 + cron 物理清理 | D01 01-er-diagram.md + 05-calculations.md §6 + D02 05-admin-articles.md OP-A8 |

✅ PRD 5 条不变量全部落地。

## 反向漂移检查(D02 端点是否新增了未授权能力)

- ✅ 无端点超出 C01 + C05 范围;
- ✅ OP-A15 全局搜索 = PM F3-Q2 明示需求;
- ✅ OP-AUX TTS 轮询 = 配合 C4 202 响应,无新增能力;
- ✅ OP-I1 mock 回调 = zhiyu-docker-policy 要求,仅 dev / 内网;
- ✅ OP-I2 健康检查 = 标准实践,公开但只读。

## 结论

- ✅ 20 条 R-ID 全部追溯成功;
- ✅ 12 条 C05 BR 全部承载;
- ✅ 5 条 PRD 不变量全部落地;
- ✅ 跨域副作用契约完整(本域 → learning-engine + Storage + 应用层缓存);
- ✅ D02 端点无反向漂移。

✅ PRD 回链校验 **PASS**。
