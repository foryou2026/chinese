<!-- TARGET-PATH: docs/C05-prd/course/PRD.md -->

# PRD · course · v1.0

> **阶段**:C05-E · **feature**:`course` · **冻结状态**:已冻结 · 2026-05-16
> **上游**:[C01](../../C01-requirements/course/baseline.md) · [C02](../../C02-ia/course/00-index.md) · [C03](../../C03-pages/course/) · [C04](../../C04-prototype/course/)
> **下游**:D01 数据模型 / D02 接口 / D03 校验

---

## 1. 产品概述

`course` 是知语主战场:面向东南亚学习者的中文学习引擎,以 **5 主题 × 25 阶段 × 148 章 × 888 节 × ~1.2 万 KP × ~5 万题** 的结构化课程为骨架,以 **7 类 KP + 12 种题型 + SRS Leitner 5 盒 + 4 类考试** 为学习与评估闭环,以 **管理端 9 大页 + 离线生成 / 导入 / 点检 / 发布** 为内容运营闭环。所有 UI 文本与内容字段 5 语(`zh/en/vi/th/id`)齐备,管理端 UI 固定中文。

## 2. 术语表

| 术语 | 说明 |
|------|------|
| 主题(Track)| 5 个固定主题码 `share / ec / fc / hsk / dl` |
| 阶段(Stage)| 主题下 6 级阶段(Stage 0..6);`share` 提供共享 Stage 0 一次性预备 |
| 章(Chapter)| 每阶段 6 章 |
| 节(Lesson)| 每章 6 节;节 code 格式 `{track}-{stage}-{chapter}-{lesson}` |
| KP(Knowledge Point)| 7 类:pinyin / hanzi / word / phrase / grammar / sentence / dialog;code 格式 `kp_{track}_{type_initial}_{seq5}` |
| 题目(Question)| 12 种:mcq_meaning / mcq_zh / listen_pick / listen_pinyin / tone_pick / match_pairs / sort_words / fill_blank_choice / type_pinyin / type_zh_ime / image_pick / dialog_cloze;code 格式 `q_{track}_{seq8}` |
| 节末小测 | 节学习后 6 题统一交卷,可跳过(`is_quiz_required=false`),通过线 60% |
| 章测 / 阶段考 / HSK 模考 | 见 §7 BR-EXAM 段 |
| SRS | Leitner 5 盒,间隔 1 / 3 / 7 / 14 / 30 天 |
| 5 语 | `zh / en / vi / th / id`,与 discover-china 等其他 feature 全局对齐 |
| Admin 角色 | `super / content_admin / readonly`,行级 `admins.tracks_scope[]` 过滤可见主题 |

## 3. 角色 / 用户故事

- **应用学员(C 端)**:5 语 UI 切换 → 引导定级 → 学节 → 节末小测 → SRS 复习 → 章测 / 阶段考 / HSK 模考;
- **content_admin(B 端)**:线下生成内容 → 批量导入 → 人工点检 → 发布 → 处理学员举报 → 管考试中心;
- **super**:全权限 + 管理员账号 / 主题 scope 配置;
- **readonly**:只读全部。

详见 [`C01/baseline.md §3`](../../C01-requirements/course/baseline.md)。

## 4. 模块清单

承自 [`C02/01-feature-catalog.md`](../../C02-ia/course/01-feature-catalog.md):**10 个 M-ID**(content / learning / srs / exam / onboarding / media / report / search / profile / i18n-perm)。

## 5. 用户旅程

主旅程 6 + 异常旅程 7,详 [`C01/flows/`](../../C01-requirements/course/flows/) 与 [`C02/02-flows.md`](../../C02-ia/course/02-flows.md)。

## 6. 页面清单与原型

| page-id | 路由 | 规格 | 原型(F4 源)|
|---------|------|------|------|
| P-app-course-001 | `/` 或 `/home` | [规格](../../C03-pages/course/P-app-course-001.md) | F4 `_assets/` + P-C-1 顶部 |
| P-app-course-002 | `/learn/...` | [规格](../../C03-pages/course/P-app-course-002.md) | [F4 P-C-1](../../../function/02-course/ai/F4-AI-原型设计/P-C-1-学习地图.html) + [F4 P-C-2](../../../function/02-course/ai/F4-AI-原型设计/P-C-2-节学习页.html) |
| P-app-course-003 | `/lesson/{code}/kp/{id}` | [规格](../../C03-pages/course/P-app-course-003.md) | F4 P-C-2 节学习页内卡片 |
| P-app-course-004 | `/review` | [规格](../../C03-pages/course/P-app-course-004.md) | [F4 P-C-4](../../../function/02-course/ai/F4-AI-原型设计/P-C-4-SRS复习.html) |
| P-app-course-005 | `/wrong` | [规格](../../C03-pages/course/P-app-course-005.md) | [F4 P-C-5](../../../function/02-course/ai/F4-AI-原型设计/P-C-5-错题本.html) |
| P-app-course-006 | `/exam` | [规格](../../C03-pages/course/P-app-course-006.md) | [F4 P-C-6](../../../function/02-course/ai/F4-AI-原型设计/P-C-6-考试中心.html) |
| P-app-course-007 | `/exam/{attemptId}` | [规格](../../C03-pages/course/P-app-course-007.md) | [F4 P-C-7](../../../function/02-course/ai/F4-AI-原型设计/P-C-7-考试进行.html) |
| P-app-course-008 | `/me` | [规格](../../C03-pages/course/P-app-course-008.md) | [F4 P-C-8](../../../function/02-course/ai/F4-AI-原型设计/P-C-8-个人统计.html) |
| P-admin-course-001 | `/admin/course` | [规格](../../C03-pages/course/P-admin-course-001.md) | [F4 P-A-1](../../../function/02-course/ai/F4-AI-原型设计/P-A-1-课程目录总览.html) |
| P-admin-course-002 | `/admin/course/tree` | [规格](../../C03-pages/course/P-admin-course-002.md) | [F4 P-A-2](../../../function/02-course/ai/F4-AI-原型设计/P-A-2-主题-阶段-章列表.html) |
| P-admin-course-003 | `/admin/course/lesson/{code}` | [规格](../../C03-pages/course/P-admin-course-003.md) | [F4 P-A-3](../../../function/02-course/ai/F4-AI-原型设计/P-A-3-节编辑.html) |
| P-admin-course-004 | `/admin/course/kp` | [规格](../../C03-pages/course/P-admin-course-004.md) | [F4 P-A-4](../../../function/02-course/ai/F4-AI-原型设计/P-A-4-KP列表.html) |
| P-admin-course-005 | `/admin/course/question` | [规格](../../C03-pages/course/P-admin-course-005.md) | [F4 P-A-5](../../../function/02-course/ai/F4-AI-原型设计/P-A-5-题目列表.html) |
| P-admin-course-006 | `/admin/course/report` | [规格](../../C03-pages/course/P-admin-course-006.md) | [F4 P-A-6](../../../function/02-course/ai/F4-AI-原型设计/P-A-6-举报处理.html) |
| P-admin-course-007 | `/admin/course/media` | [规格](../../C03-pages/course/P-admin-course-007.md) | [F4 P-A-7](../../../function/02-course/ai/F4-AI-原型设计/P-A-7-媒资库.html) |
| P-admin-course-008 | `/admin/course/exam` | [规格](../../C03-pages/course/P-admin-course-008.md) | [F4 P-A-8](../../../function/02-course/ai/F4-AI-原型设计/P-A-8-考试中心管理.html) |
| P-admin-course-009 | `/admin/course/search` | [规格](../../C03-pages/course/P-admin-course-009.md) | [F4 P-A-9](../../../function/02-course/ai/F4-AI-原型设计/P-A-9-全局搜索.html) |

弹窗 D-1..D-18 详 [`C02/07-error-pages.md §2`](../../C02-ia/course/07-error-pages.md)。

## 7. 业务规则(全量,标 BR-ID)

### 7.1 BR-STRUCTURE(骨架与命名)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-S01 | 5 主题码白名单 `share / ec / fc / hsk / dl`,系统不可自助新增 | §4 / R-013 |
| BR-S02 | 节 code 格式 `{track}-{stage}-{chapter}-{lesson}`,UNIQUE | §4 / R-014 |
| BR-S03 | KP code 格式 `kp_{track}_{type_initial}_{seq5}`,UNIQUE;type_initial = p/h/w/ph/g/s/d | §4 / R-016 |
| BR-S04 | Question code 格式 `q_{track}_{seq8}`,UNIQUE | §4 / R-017 |
| BR-S05 | 主题 `share` 提供共享 Stage 0;任一业务主题学员完成 share/Stage 0 即四主题 Stage 0 通用 | R-027 |
| BR-S06 | 节默认绑定 12 KP(可 8-14),节末小测固定 6 题 | R-005, R-006 |
| BR-S07 | KP / Lesson / Chapter / Stage / Track 顺序由 `seq_no` 管理,管理端可拖拽重排;持久化后唯一 | R-014 |

### 7.2 BR-CONTENT(内容生命周期)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-C01 | 内容生产 = 线下生成 → 批量导入(CSV/JSON)→ 人工点检 → 发布;**系统内不设生成工作台** | R-022 |
| BR-C02 | 导入 KP / Question 默认 `is_published=false`;批量 / 行内发布显式触发 | R-022 |
| BR-C03 | 章发布默认级联节 + KP + 题;节发布默认级联 KP + 题 | R-023 |
| BR-C04 | 章 / 节下架**不级联** KP / 题(只切自身可见性) | R-023 |
| BR-C05 | 发布前必须 5 语字段完整(`zh/en/vi/th/id` 任一为空 → 拒绝发布)| §4 / R-016 |
| BR-C06 | KP / Question 编辑保存自动 `version+1`;旧版本归档查询 | R-024 |
| BR-C07 | 删除 KP / Question:若被 `lesson_kp` 引用或 `user_exam_attempts.snapshot` 引用,**禁止硬删**,只能下架 | R-017, R-025 |
| BR-C08 | 媒资按 `hash` 全局去重;有 `ref_kp_id / ref_q_id` 引用时禁止软删 | R-019 |
| BR-C09 | 媒资软删 30 天后由 cron 物理清理 | R-019 |
| BR-C10 | LWW 后写覆盖:保存请求带 `loaded_updated_at`,服务端比对若不一致则覆盖并返被覆盖管理员名,前端 Toast 提示 | (横切)|

### 7.3 BR-LEARNING(学习与节内)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-L01 | 进节自动整节预下载(KP+题+音频);部分失败不阻塞,音频按需重拉 | R-008 |
| BR-L02 | 节末小测可跳过(`is_quiz_required=false`);跳过则 `user_progress.status=in_progress`,仍解锁下一节 | R-006 |
| BR-L03 | 节末小测通过线 60%;通过 `status=passed` | R-006 / R-011 |
| BR-L04 | 学员答题统一接口 `POST /app/answer { context_type, question_id, payload }`;`context_type ∈ {lesson_practice, lesson_quiz, srs_review, chapter_test, stage_exam, hsk_mock}` | R-007 |
| BR-L05 | 答题副作用:正确 → `user_srs.box+1, due_at += 间隔表`;错误 → `box=1, due_at=明天` | R-026 |
| BR-L06 | 弱网答题写本地队列(`localforage`),回网后批量同步 `POST /app/answer:batch` | FX-course-01 |
| BR-L07 | 多端进度以服务端 `user_progress / user_srs / user_exam_attempts` 为准,前端只缓存 | R-030 |

### 7.4 BR-SRS

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-R01 | Leitner 5 盒间隔:1 / 3 / 7 / 14 / 30 天 | §4 / R-009 |
| BR-R02 | 每日复习按 `box ASC, due_at ASC` 拉,默认上限 50 KP | R-009 |
| BR-R03 | 每 KP 抽 1 题轮换题型,避免学员背答案 | R-009 |
| BR-R04 | 错题本视图只读,引导回 SRS;不修改成绩 | R-010 / R-024 |

### 7.5 BR-EXAM

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-E01 | 4 类考试:`lesson_quiz`(6 题 / 60%)/ `chapter_test`(15 题 / 70%)/ `stage_exam`(50 题 / 70%)/ `hsk_mock`(HSK 主题独享) | R-011 / R-020 |
| BR-E02 | 满分恒 100;单题分 = 100 / 当前 attempt snapshot 题数;已存 attempt snapshot 不变 | R-025 |
| BR-E03 | `POST /exam/{id}/start` 写 `user_exam_attempts`,按 blueprint 抽题写 snapshot;`POST /exam/{attempt}/submit` 批量判分 | R-011 |
| BR-E04 | 倒计时归零自动提交;5 分钟无心跳 → `status=failed score=0` | R-011 |
| BR-E05 | 阶段考通过(`scope_type=stage_exam` && `passed=true`)自动解锁同主题下一阶段全部节 | R-027 |
| BR-E06 | 阶段考通过后默认**不可重考**(决策 H5) | R-011 |
| BR-E07 | 试抽预览仅渲染,**不写 `user_exam_attempts`**,不算 attempt | R-020 |
| BR-E08 | 试抽题量不足 blueprint count → `[发布]` 置灰 + 错误 banner | FX-course-02 |

### 7.6 BR-REPORT(学员举报)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-RP01 | 学员通过答题反馈页 D-14 举报 → `content_action_log { action: 'report', target_q_id, reason }` | R-018 |
| BR-RP02 | P-A-6 按 `question_id` 聚合;`report_count ≥ 3` 自动置顶 | R-018 |
| BR-RP03 | 采纳 / 忽略不自动改 `questions.is_published`;改与不改由 admin 显式操作 | R-018 |
| BR-RP04 | 修正题目后 `version+1`;`user_answers` 历史不动,新作答取新 version | R-024 |

### 7.7 BR-AUTH-PERM(权限与多语)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-P01 | 5 语 locale 集合 `zh/en/vi/th/id`(全局对齐)| §4 |
| BR-P02 | 应用端 UI 按 `users.ui_lang` 切换,缺失回退 `zh`;管理端 UI 固定中文 | §4 |
| BR-P03 | 订阅主题访问控制:无订阅 → 前 1 章试学,试学完强制订阅页 | R-028 |
| BR-P04 | 用户端 API + 视图层强制 `is_published=true` 且父级全发布;违反返 404 / 410 | R-029 |
| BR-P05 | admin 行级 `tracks_scope[]` 过滤:列表 / 详情 / 写入全部 SQL 自动 `WHERE track_code = ANY($scope)`;越权 403 | R-013..021 |
| BR-P06 | `readonly` 角色:全部写入按钮置灰,前端 + 后端双校验 | (横切)|

### 7.8 BR-SYS(系统副作用)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-Y01 | `user_answers` 写入触发 `user_srs` 升降盒 + 重算 `due_at`(BR-L05) | R-026 |
| BR-Y02 | 阶段考通过 → 自动写下一阶段全部节 `user_progress.status='unlocked'`(BR-E05) | R-027 |
| BR-Y03 | 节下架 → 已学进度保留 / 用户端节级直链返 410 / 学员端不可再进 | R-029 / BR-C04 |
| BR-Y04 | 媒资软删 cron(daily)+ 引用反查(BR-C08/C09) | R-019 |

## 8. 角色权限矩阵

| 操作 | 学员 | content_admin (scope ⊃ track) | super | readonly |
|------|:--:|:--:|:--:|:--:|
| 浏览应用端 5 Tab | ✓ | × | × | × |
| 节学习 / SRS / 错题本 | ✓ | × | × | × |
| 考试(节/章/阶段/HSK)| ✓ | × | × | × |
| 进 `/admin/course/*` | × | ✓ | ✓ | ✓(只读)|
| 内容 CRUD(节 / KP / 题)| × | ✓(scope 内)| ✓ | ✗ |
| 媒资 CRUD | × | ✓ | ✓ | ✗ |
| 学员举报处理 | × | ✓ | ✓ | ✗ |
| 考试中心配置 / 发布 | × | ✓(scope 内)| ✓ | ✗ |
| 全局搜索 | × | ✓(scope 过滤)| ✓ | ✓(只读跳转)|
| 管理员账号 / `tracks_scope` 配置 | × | × | ✓ | × |

## 9. 数据量级与性能基线

- 课程骨架:5 主题 / 25 阶段 / 148 章 / 888 节 / ~12 000 KP / ~50 000 题 / ~20 000 音频;
- 单节聚合接口 `GET /app/lesson/{code}` 响应体 ≤ 200 KB(`gzip`),P95 ≤ 300ms;
- `GET /app/srs/today` 单用户单次 LIMIT 50 → P95 ≤ 200ms;
- 答题 `POST /app/answer` P95 ≤ 150ms;
- 考试交卷 `POST /app/exam/{attempt}/submit` 批量判分 50 题 P95 ≤ 800ms;
- 限流:`/app/answer` 60 次/分/用户 → 超出 429。

## 10. 国际化与端策略

- 应用端 5 语 UI 切换,文案 key 前缀 `course.*`;
- 应用端学员**端**:Web App + 微信 H5 + 后期 RN(同套页面);
- 管理端:Web 桌面优先;
- 数据层 5 语字段统一 `*_i18n: { zh, en, vi, th, id }`;
- 缺失语言渲染回退 `zh`,前端浅色提示。

## 11. 与其它 feature 的边界

- 与 [`discover-china`](../../C05-prd/discover-china/PRD.md) 共享:5 语 locale、媒资库技术栈、Admin 角色与 LWW 模式;不共享:类目编码 / 文章结构 / TTS 缓存键命名;
- 与未来 `payments`(订阅)feature:`users.subscription` 字段对接,本期 BR-P03 视订阅状态拦截;支付流走 mock 适配(docker-policy)。

## 12. 决策封板与本期不在范围

- **不做(v1)**:AI 对话陪练 / 发音打分 / 作文批改 / 千人千面;直播 / 1v1;论坛 UGC;系统内 AI 生成工作台(2025-11 废)、自定义主题码、自由建题、阶段考重考、举报自动改内容、AI 提示词管理页;
- **决策已封板**(详 [`function/02-course/prd/07-待确认问题清单.md`](../../../function/02-course/prd/07-待确认问题清单.md)):
  - A 段范围(主题数 5 固定 / Stage 0 共享一次性);
  - B 段内容发布(章节级联 / 下架不级联 / 节末测可跳过);
  - C 段考试(满分 100 动态均分 / 不可重考阶段考 / 试抽不写 attempt);
  - H 段版本(`version+1` 治理 + 历史不追溯);
- **跨域副作用契约**:见 §7.8 BR-Y01..Y04 与 [`C02/03-state-machines.md`](../../C02-ia/course/03-state-machines.md)。

## 13. 下游交付

- D01 数据规范:18 张表 DDL + 索引 + 视图(基于 [`function/02-course/prd/03-数据库schema.md`](../../../function/02-course/prd/03-数据库schema.md))
- D02 接口规范:OP-ID 清单(应用端 ~30 + 管理端 ~50)+ 错误码 `COURSE_*` ~40
- D03 校验:上游链 / 模块闭环 / PRD 回链(三段 PASS)
- 实现 schema:`zhiyu_course`
