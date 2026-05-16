<!-- TARGET-PATH: docs/C06-prd/course/_shared/business-rules.md -->

> **跨 surface 共享业务规则(Round 2 从 PRD.md 第 7 章迁出)。** 端特定补充见各 surface 下的 07-business-rules.md。

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
| BR-RP02 | P-admin-course-006 按 `question_id` 聚合;`report_count ≥ 3` 自动置顶 | R-018 |
| BR-RP03 | 采纳 / 忽略不自动改 `questions.is_published`;改与不改由 admin 显式操作 | R-018 |
| BR-RP04 | 修正题目后 `version+1`;`user_answers` 历史不动,新作答取新 version | R-024 |

### 7.7 BR-AUTH-PERM(权限与多语)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-P01 | 5 语 locale 集合 `zh/en/vi/th/id`(全局对齐)| §4 |
| BR-P02 | 应用端 UI 按 `users.ui_lang` 切换,缺失回退 `zh`;管理端 UI 固定中文 | §4 |
| BR-P03 | 订阅主题访问控制:无订阅 → 前 1 章试学,试学完强制订阅页 | R-028 |
| BR-P04 | 用户端 API + 视图层强制 `is_published=true` 且父级全发布;违反返 404 / 410 | R-029 |
| BR-P05 | admin 端中间件统一校验 `role === 'super_admin'`；非该角色访问 `/api/admin/course/*` 返 403 | R-013..021 |

### 7.8 BR-SYS(系统副作用)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-Y01 | `user_answers` 写入触发 `user_srs` 升降盒 + 重算 `due_at`(BR-L05) | R-026 |
| BR-Y02 | 阶段考通过 → 自动写下一阶段全部节 `user_progress.status='unlocked'`(BR-E05) | R-027 |
| BR-Y03 | 节下架 → 已学进度保留 / 用户端节级直链返 410 / 学员端不可再进 | R-029 / BR-C04 |
| BR-Y04 | 媒资软删 cron(daily)+ 引用反查(BR-C08/C09) | R-019 |
