<!-- TARGET-PATH: docs/D01-data/course/03-business-rules.md -->

# 03 · 数据层业务规则 · course

> DBR-ID 对应 [C05 PRD BR-ID](../../C05-prd/course/PRD.md);本文是 DB 侧的实现锚点。

| DBR-ID | 规则 | 对应 PRD BR | 实现 |
|---|---|---|---|
| DBR-CAT-01 | track_code 仅 5 枚举,不允许动态新增 | BR-CAT-01 | CHECK on `course_tracks.code` + 同名 CHECK on `course_stages.track_code` |
| DBR-CAT-02 | (track_code,stage_no) UNIQUE;stage_no=0 仅 share | BR-CAT-02 | `uq_course_stages_track_stage` + CHECK |
| DBR-CAT-03 | (chapter_id,lesson_no) UNIQUE(软删感知) | BR-CAT-03 | partial-UNIQUE WHERE `deleted_at IS NULL` |
| DBR-CAT-04 | lesson code 全局 UNIQUE 且匹配父级编号 | BR-CAT-04 | partial-UNIQUE + 应用层 `fn_create_lesson` 校验上下级一致 |
| DBR-CAT-05 | 章/节/KP/题目软删,30 天后物理清理 | BR-CAT-05 | `deleted_at` 字段 + cron `purge-soft-deleted-course.ts` |
| DBR-PUB-01 | 发布父级时默认级联发布子级,可选不级联 | BR-PUB-01 | `fn_content_publish(cascade=true)` 默认级联,RPC 参数控制 |
| DBR-PUB-02 | 下架章 → 默认下架章下节;下架节不级联 KP/题目 | BR-PUB-02 | `fn_content_publish(action='unpublish')` 内分支 |
| DBR-PUB-03 | 学员可见性 = `is_published=true AND deleted_at IS NULL AND 祖先全发布` | BR-PUB-03 | RLS policy 跨 JOIN |
| DBR-PUB-04 | 题目修订后 `version += 1`,旧 attempt 不追溯 | BR-RP04 | 触发器 `tg_*_before_update_set_version` 仅当 `payload` 变动时自增;`course_user_answers.question_version` 保留快照 |
| DBR-KP-01 | KP code 由触发器生成,(track,type) 35 sequence | BR-KP-01 | `tg_before_insert_course_kp_set_code` + `fn_gen_kp_code` |
| DBR-KP-02 | 题目去重:(kp_id, q_type, payload_hash) UNIQUE | BR-KP-02 | partial-UNIQUE `uq_course_q_kp_qtype_hash` |
| DBR-KP-03 | 节-KP 绑定多对多,position 1-50 | BR-KP-03 | `course_lesson_kp` PK + CHECK |
| DBR-AS-01 | 学员答题写入 RPC,context_type!=practice 触发 SRS | BR-AS-01 | `fn_submit_answer` + 调 `fn_srs_update` |
| DBR-AS-02 | SRS 5 盒 Leitner;间隔 1/3/7/14/30 天 | BR-AS-02 | `fn_srs_update`,见 [05-calculations.md](./05-calculations.md) |
| DBR-AS-03 | SRS 单日发卡 ≤ 50 张/学员 | BR-AS-03 | RPC `fn_get_srs_queue(user_id, limit)` 内做日预算 (`select count() where context_type='srs_review' and answered_at >= today`) |
| DBR-AS-04 | 节末小测可关闭 (`lessons.has_quiz=false`) | BR-AS-04 | 列 + RPC 分支 |
| DBR-EX-01 | 同 scope_ref_id 仅一卷(hsk_mock 例外) | BR-EX-01 | `uq_course_exams_unique_per_scope` partial-UNIQUE |
| DBR-EX-02 | 试卷快照固化 question_ids + version + blueprint | BR-EX-02 | `course_user_exam_attempts.snapshot` jsonb |
| DBR-EX-03 | 阶段考通过不可重考(同学员同卷)| BR-EX-03 | 应用层校验 + 错误码 `COURSE_STAGE_EXAM_ALREADY_PASSED` |
| DBR-EX-04 | 限时超期 → cron 标 expired | BR-EX-04 | `idx_course_uea_state` + cron + RPC `/internal/exam-attempts:expire` |
| DBR-EX-05 | 阶段考过 → 解锁下一阶段全部节 | BR-EX-05 | `tg_after_stage_exam_passed_unlock_next_stage` |
| DBR-IM-01 | 导入幂等:(payload_hash, import_type) | BR-IM-01 | `idx_course_import_hash` + 应用层 EXISTS |
| DBR-IM-02 | 导入状态机 6 态 | BR-IM-02 | CHECK + RPC 状态转移 |
| DBR-MD-01 | 媒资 hash UNIQUE 去重 | BR-MD-01 | `uq_course_ma_hash` |
| DBR-MD-02 | 删除媒资前反查 KP/Question 引用 | BR-MD-02 | 应用层反查 + 入待清队列 |
| DBR-MD-03 | 待清队列 7 天后 cron 物理删 | BR-MD-03 | cron `purge-pending-media.ts` |
| DBR-RP-01 | 学员举报 24h 去重 | BR-RP-01 | 应用层 EXISTS 检查 `course_content_action_log` |
| DBR-RP-02 | 举报命中 → `course_questions.report_count += 1` | BR-RP-02 | `fn_report_question` RPC |
| DBR-RP-03 | 管理员处理举报 → action_log `dismiss / adopt` | BR-RP-03 | `fn_handle_report` RPC |
| DBR-PRG-01 | 节状态机 locked → unlocked → in_progress → passed | BR-PRG-01 | CHECK + trigger 解锁 |
| DBR-PRG-02 | 节通过判定:小测分 ≥ pass_score(默认 60) | BR-PRG-02 | `fn_lesson_pass` |
| DBR-PRG-03 | 断点续学:(last_kp_id, last_position) | BR-PRG-03 | 列 + PUT checkpoint RPC |
| DBR-LOG-01 | 编辑/发布/下架/举报全留痕,90 天保留 | BR-LOG-01 | `course_content_action_log` + cron(沿用平台日志保留策略) |
| DBR-LOG-02 | edit 记录 diff;report 记录 report_type+reason | BR-LOG-02 | CHECK 约束 + RPC 拼装 |
| DBR-RLS-01 | 学员只能读已发布且祖先全发布 | BR-RLS-01 | RLS policy |
| DBR-RLS-02 | 学员只能读写自己的 user_* 行 | BR-RLS-02 | RLS `user_id = auth.uid()` |
| DBR-RLS-03 | 管理端写入 service_role,应用层叠加 tracks_scope | BR-RLS-03 | service_role bypass + middleware |
| DBR-CC-01 | 管理端编辑乐观锁 If-Match: updated_at | BR-CC-01 | UPDATE WHERE updated_at=? + rowcount 检查 |
| DBR-CC-02 | 学员作答 append-only,无冲突 | BR-CC-02 | INSERT-only |
| DBR-CC-03 | 考试提交行锁 FOR UPDATE | BR-CC-03 | RPC `fn_submit_exam` 内 SELECT FOR UPDATE |
