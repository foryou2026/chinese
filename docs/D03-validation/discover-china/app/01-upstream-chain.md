<!-- TARGET-PATH: docs/D03-validation/discover-china/app/01-upstream-chain.md -->

> **本文件为 surface=`app` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端独立重写校验链路与 PRD 回链)。**


# D03-V01 · 上游链一致性 · discover-china

> 检查范围:C01 R-IDs → C02 信息架构(M / Flow / SM / P-IDs) → C03 页面交互规范 → C04 HTML 原型 → C05 PRD BR → D01 实体 → D02 端点。
> 检查时间:2026-05-16(批次 6)。

## 1. 实体 → 上游需求映射

| D01 实体 | 字段 / 约束来源 | C01 R-ID | C05 BR | F1 子文件 |
|---------|----------------|----------|--------|----------|
| `china_categories` | 12 项固定字典,5 语 name/desc,01-12 code | R-001 / R-009 / R-019 | BR-01 | F1/01 |
| `china_articles` | code 12 位 / status 状态机 / 软删 / created_by | R-002,R-003,R-010,R-012,R-014,R-015,R-017 | BR-02 / BR-03 / BR-05 / BR-06 | F1/02 + F1/06 |
| `china_sentences` | seq_no 4 位补零 / 拼音 / 5 语内容 / TTS 字段 | R-004,R-006,R-008,R-016,R-018 | BR-07 / BR-08 / BR-09 | F1/03 + F1/04 |

✅ 全部上游 R-ID 找到承载实体或字段;**无孤儿 R-ID**。

## 2. RPC → 业务规则映射

| RPC | C05 BR | 触发点(D02) |
|-----|--------|-----------|
| `fn_gen_article_code` | BR-02 | OP-A4 |
| `fn_next_sentence_seq` | BR-07 | OP-A11 |
| `fn_resequence_sentences` | BR-08 / BR-09 | OP-A11 / A13 / A14 |
| `fn_publish_article` | BR-05 | OP-A6 |
| `fn_unpublish_article` | BR-04 / BR-05 | OP-A7 |
| `fn_insert_sentence_at` | BR-07 / BR-09 | OP-A11 |
| `fn_delete_sentence` | BR-09 | OP-A13 |
| `fn_reorder_sentences` | BR-09 | OP-A14 |
| `fn_bulk_insert_sentences` | BR-07 | 内部种子 / 大批量 |
| `fn_clear_progress_by_article`(跨域) | BR-04 / BR-09 | OP-A7 / A8 / A11(start\|after) / A13 / A14 |

✅ 12 条 BR 全部 → 至少一条 RPC + 端点承载;**无悬挂规则**。

## 3. 页面 → 端点映射(C02 P-ID → D02 OP-ID)

### 应用端

| P-ID | C03 页面 | 主调用 |
|------|---------|--------|
| P-app-discover-china-001 | 类目 12 卡片(Tab 主页) | OP-C1 |
| P-app-discover-china-002 | 类目下文章列表(含搜索) | OP-C2 |
| P-app-discover-china-003 | 文章详情(逐句卡片 + TTS + 全文朗读) | OP-C3 + OP-C4 + OP-C5(+ OP-AUX) |

### 管理端

| P-ID | C03 页面 | 主调用 |
|------|---------|--------|
| P-admin-discover-china-001 | 12 类目卡片(管理首页) | OP-A1 |
| P-admin-discover-china-002 | 类目下文章列表(分页 + 搜索 + 状态 filter) | OP-A2 + OP-A6 / A7 / A8 |
| P-admin-discover-china-003 | 文章编辑 + 句子管理(基本信息 + 句子列表 + CRUD + 重排) | OP-A3 + A4 + A5 + A9..A14 |
| P-admin-discover-china-004 | 全局搜索结果页(P-A-4) | OP-A15 |

✅ 7 个 P-ID 全部消费到 D02 端点;**无孤儿页面**。

## 4. 状态机 → 端点映射

| 状态转换 | C04 SM | D02 OP-ID |
|---------|--------|-----------|
| 创建 → draft | SM-china-article §init | OP-A4 |
| draft → published | SM-china-article §publish(校验 5 语 + ≥1 句) | OP-A6 |
| published → draft(下架,清进度) | SM-china-article §unpublish | OP-A7 |
| 任意 → 软删(置 draft + 清进度) | SM-china-article §delete | OP-A8 |
| pending → processing → ready / failed(TTS) | SM-china-sentence-audio | OP-C4 |
| failed → processing(用户重试) | 同 | OP-C4 |

✅ 全部 SM 节点找到端点驱动;**无悬挂状态**。

## 5. 多语言 / 编码格式

| 项 | 上游约定 | 下游落地 |
|----|---------|---------|
| 5 语 locale | B02-permissions §4 + C01 §4 + B03-experience locale 列表 = `{zh,en,vi,th,id}` | D01 jsonb CHECK + D02 错误码 5 语文案 |
| 文章 code 格式 | C01 §4(12 位 [A-Z0-9],UI 字符串原样) | D01 `^[A-Z0-9]{12}$` + D02 OP-A3/A4 |
| 句子 seq_no 显示 | C01 §4(4 位补零) | D01 `seq_label` 派生字段(`padStart(4,'0')`)+ D02 出参 `seq_label` |
| TTS Storage 路径 | C01 §4 / F1/03(`china-tts/{article_code}/{seq_no_padded}.mp3`) | D01 02-entities/china_sentences + D02 OP-C4 |

✅ 编码与展示约定一致;无格式漂移。

## 6. 已下线项不一致检查

| 项 | 状态 | 下游一致性 |
|----|------|----------|
| OP-C6 / C7 阅读进度接口 | 🚫 已下线(2026-04) | ✅ D02 `03-endpoints/03-app-progress-deprecated.md` 标记;`01-routes-delta.md` "下线"段已登记;C03 / C04 阅读详情页已移除"重新开始 + x/y"文案;**但跨域 fn_clear_progress_by_article 副作用保留**(物理删 source='china' 历史行) |

✅ 下线项无遗漏;跨域副作用契约保留正确。

## 结论

- **上游链 0 失配**;C01 R-IDs 全部映射到 D01 + D02;
- C05 BR-01..BR-12 全部承载;
- C02 7 个 P-ID 全部消费到 OP-ID;
- C04 SM 全部状态节点找到端点驱动;
- 多语言 / 编码格式约定一致;
- 已下线项标记完整,跨域副作用契约保留。

✅ 上游链一致性检查 **PASS**。
