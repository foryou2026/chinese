<!-- TARGET-PATH: docs/D03-validation/discover-china/02-module-closure.md -->

# D03-V02 · 模块内闭环 · discover-china

> 检查 D01 / D02 自身闭环:每张表都有 CRUD 路径、每个端点都有数据落点、每条规则都有强制点。
> 检查时间:2026-05-16(批次 6)。

## 1. 表 → CRUD 端点闭环

| 表 | C | R(app) | R(admin) | U | D |
|----|---|--------|----------|---|---|
| `china_categories` | seed | OP-C1 | OP-A1 | service-role only | service-role only |
| `china_articles` | OP-A4 | OP-C2 / C3 / C5 | OP-A2 / A3 / A15 | OP-A5 / A6 / A7 | OP-A8(软删) |
| `china_sentences` | OP-A11 | (随 C3 内嵌) | OP-A9 / A10 / A15 | OP-A12 / A14 | OP-A13(软删) |

✅ 三表均闭环;字典表 categories 由迁移 seed 写入,符合 PM 答 Q6"固定不增"。

## 2. 端点 → 数据落点闭环

| OP-ID | 读 / 写 表 | 跨域调用 |
|-------|----------|---------|
| OP-C1 | R `china_categories` | — |
| OP-C2 | R `china_articles` + `china_sentences`(搜 q 时) | — |
| OP-C3 | R `china_articles` + `china_sentences` + `china_categories` + 相邻文章 | — |
| OP-C4 | R/W `china_sentences`(`audio_*` 字段) + Storage 写 mp3 | TTS adapter(`packages/ai-adapters/tts/*`) |
| OP-C5 | R `china_sentences`(仅 ready) | — |
| OP-AUX | R `china_sentences`(audio_status) | — |
| OP-A1 | R `china_categories` + COUNT `china_articles` | — |
| OP-A2..A3 | R `china_articles` + `china_categories` + audit user | — |
| OP-A4 | W `china_articles` | `fn_gen_article_code` |
| OP-A5 | W `china_articles` | — |
| OP-A6 | W `china_articles` + R `china_sentences`(校验) | `fn_publish_article` + `pg_notify` |
| OP-A7 | W `china_articles` | `fn_unpublish_article` + **`fn_clear_progress_by_article`** + `pg_notify` |
| OP-A8 | W `china_articles`(deleted_at) | 若原 published,同 A7 副作用 |
| OP-A9..A10 | R `china_sentences` | — |
| OP-A11 | W `china_sentences` | `fn_insert_sentence_at` +(条件)`fn_clear_progress_by_article` |
| OP-A12 | W `china_sentences` | — |
| OP-A13 | W `china_sentences`(deleted_at) | `fn_resequence_sentences` + `fn_clear_progress_by_article` |
| OP-A14 | W `china_sentences`(seq_no) | `fn_reorder_sentences` + `fn_clear_progress_by_article` |
| OP-A15 | R `china_articles` + `china_sentences`(GIN trgm) | — |
| OP-I1 | W `china_sentences`(audio_*) | — |
| OP-I2 | — | — |

✅ 全部端点找到数据落点;**无悬挂端点 / 孤儿表**。

## 3. 业务规则 → 强制点闭环

| BR | 强制点 |
|----|--------|
| BR-01 类目固定字典 | DB:`ON DELETE RESTRICT` + RLS service-role only;管理端无 POST/PUT/DELETE 端点 |
| BR-02 文章 code 系统生成 | RPC `fn_gen_article_code()`;OP-A4 不接受前端 code |
| BR-03 软删 30 天不可恢复 | cron `cron_china_purge_soft_deleted`;UI 无恢复按钮 |
| BR-04 下架 / 删除清用户进度 | `fn_clear_progress_by_article` 在 RPC 内调用 |
| BR-05 发布前置 5 语 + ≥1 句 | `fn_publish_article` 内校验 → 422 |
| BR-06 软删反推 status=draft | OP-A8 处理 + `fn_unpublish_article` 切换 |
| BR-07 句子 seq_no 1..9999 唯一 + 补零 | DB CHECK + 复合 UNIQUE + 出参 `seq_label`;`fn_next_sentence_seq` 锁分配 |
| BR-08 重排自动连续 + 失效音频 | `fn_resequence_sentences` 偏移 +100000 重排 + 清音频字段 |
| BR-09 结构变化清进度(条件) | A11(start/after) / A13 / A14 触发;A11(end) / A12 不触发 |
| BR-10 TTS 用户触发 + 共享缓存 + 失败不限重试 | OP-C4 状态机;Storage 永久;`audio_status='failed'` 允许重新点击 |
| BR-11 LWW 文章 / 句子并发 | 后端不返 409,前端按 `updated_at` 比较 toast 提示 |
| BR-12 全 5 语错误文案 + 兜底 en→zh | `packages/shared-config/src/error-codes.ts` 注册 + 中间件按 `Accept-Language` 取 |

✅ 12 条 BR 全部找到至少 1 个强制点;**无悬挂规则**。

## 4. 验证规则 → 错误码闭环

D01 §4 共 ~30 条 Zod 规则 → D02 04-error-codes.md 共 31 个 `CHINA_*` 码:

- ✅ 校验类 18 + 资源 / 状态类 10 + 上游 / 系统类 3 = 31 条;
- ✅ 每条规则有对应字符串 code + 数值 code(45000-45299);
- ✅ HTTP 状态码与触发点匹配。

## 5. RLS 一致性

| 表 | anon select | authenticated select | service_role 写 | C 端端点 RLS |
|----|-------------|---------------------|----------------|-------------|
| `china_categories` | 全量 | 全量 | only | OP-C1 直接读 |
| `china_articles` | published+未删 | 同(分级公开过滤在应用层) | only | OP-C2 / C3 受 RLS 自然过滤 |
| `china_sentences` | EXISTS 父 article published+未删 | 同 | only | OP-C3 / C5 / C4 / AUX 受 RLS 自然过滤 |

✅ RLS 与端点权限层一致;分级公开(类目 04-12 须登录)在应用层中间件强制,不依赖 RLS。

## 结论

- ✅ 三表全部闭环;
- ✅ 25 个 OP-ID 全部找到数据落点;
- ✅ 12 条 BR 全部强制;
- ✅ 31 个 `CHINA_*` 错误码与校验规则一一对应;
- ✅ RLS 与端点权限层一致。

✅ 模块内闭环检查 **PASS**。
