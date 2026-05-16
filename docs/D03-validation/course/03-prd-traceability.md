<!-- TARGET-PATH: docs/D03-validation/course/03-prd-traceability.md -->

# D03-03 · PRD 回链矩阵 · course

> **结论**:✅ PASS。40 BR-ID × 15 表 × ~80 OP-ID 全部映射。副作用契约 + 不变量声明完整。

## 1. BR × 表 × OP 矩阵(完整 40 条)

> 表名省略 `course_` 前缀。OP-ID 省略 `OP-course-` 前缀。

| BR-ID | 表 | OP-ID | 错误码 |
|---|---|---|---|
| BR-CAT-01 | tracks, stages | app-001/002/003, admin-001/002 | `COURSE_INVALID_TRACK_CODE` |
| BR-CAT-02 | stages | admin-002 | `COURSE_STAGE_NOT_EMPTY` |
| BR-CAT-03 | chapters | admin-003 | `COURSE_CHAPTER_NOT_EMPTY` |
| BR-CAT-04 | lessons | admin-004 | `COURSE_LESSON_CODE_MISMATCH`, `COURSE_LESSON_NO_DUPLICATE` |
| BR-CAT-05 | chapters, lessons, kp, questions, exams | cron purge-soft-deleted | — |
| BR-PUB-01 | 全发布表 | admin-016 publish | `COURSE_CASCADE_TARGET_EMPTY` |
| BR-PUB-02 | 全发布表 | admin-016 unpublish | — |
| BR-PUB-03 | 全发布表 | (RLS) | `COURSE_NOT_VISIBLE` |
| BR-RP04(版本不追溯)| questions, user_answers | admin-012 PATCH / app-009 INSERT | — |
| BR-KP-01 | knowledge_points | admin-007/008/009/015 | `COURSE_INVALID_KP_TYPE`, `COURSE_KP_CONTENT_SCHEMA_MISMATCH`, `COURSE_INVALID_KP_CODE` |
| BR-KP-02 | questions | admin-013/015 | `COURSE_IMPORT_DUPLICATE`(题级), `COURSE_PAYLOAD_SCHEMA_MISMATCH` |
| BR-KP-03 | lesson_kp | admin-004 bind-kps | — |
| BR-AS-01 | user_answers, user_srs | app-009 | `COURSE_PAYLOAD_SCHEMA_MISMATCH`, `COURSE_FORBIDDEN_OTHER_USER` |
| BR-AS-02 | user_srs | app-009/011 | — |
| BR-AS-03 | user_srs, user_answers | app-011 | `COURSE_SRS_DAILY_LIMIT_EXCEEDED` |
| BR-AS-04 | lessons.has_quiz | app-008 | — |
| BR-EX-01 | exams | admin-021 | `COURSE_IMPORT_DUPLICATE`(exam 级)|
| BR-EX-02 | user_exam_attempts.snapshot | app-014/016 | — |
| BR-EX-03 | user_exam_attempts | app-014 | `COURSE_STAGE_EXAM_ALREADY_PASSED` |
| BR-EX-04 | user_exam_attempts | cron expire / internal-002 | `COURSE_EXAM_EXPIRED` |
| BR-EX-05 | user_progress, user_exam_attempts | app-016 + trigger | — |
| BR-IM-01 | import_batches | admin-015 | `COURSE_IMPORT_DUPLICATE` |
| BR-IM-02 | import_batches | admin-015a/b | `COURSE_IMPORT_HAS_ERRORS` |
| BR-MD-01 | media_assets | app-006 / admin-020 | — |
| BR-MD-02 | media_assets | admin-020 DELETE | `COURSE_MEDIA_STILL_REFERENCED` |
| BR-MD-03 | media_assets | cron purge-pending-media | — |
| BR-RP-01 | content_action_log | app-018 | `COURSE_REPORT_DUPLICATE` |
| BR-RP-02 | questions.report_count | app-018 | — |
| BR-RP-03 | content_action_log | admin-019 | `COURSE_REPORT_ALREADY_HANDLED` |
| BR-PRG-01 | user_progress | app-003/004 + trigger | — |
| BR-PRG-02 | user_progress | app-010 + `fn_lesson_pass` | `COURSE_QUIZ_INCOMPLETE_ANSWERS` |
| BR-PRG-03 | user_progress | app-007 | `COURSE_KP_NOT_IN_LESSON` |
| BR-LOG-01 | content_action_log | admin-017 / 全写入 | — |
| BR-LOG-02 | content_action_log | admin-016/019 | — |
| BR-RLS-01 | 全发布表 | (RLS policy) | `COURSE_NOT_VISIBLE` |
| BR-RLS-02 | user_* 表 | (RLS policy) | `COURSE_FORBIDDEN_OTHER_USER` |
| BR-RLS-03 | 全表 | 中间件 + service_role | `COURSE_ADMIN_ONLY` |
| BR-CC-01 | 编辑表 | admin PATCH | `COURSE_STALE_VERSION` |
| BR-CC-02 | user_answers | app-009 | — |
| BR-CC-03 | user_exam_attempts | app-016/017 | `COURSE_EXAM_EXPIRED` |

## 2. 副作用契约

| RPC / endpoint | 数据库副作用 |
|----------------|------------|
| `fn_submit_answer` | INSERT `course_user_answers`;若 context!=practice → UPSERT `course_user_srs` |
| `fn_lesson_pass` | UPDATE `course_user_progress(status,passed_at,best_score,attempts)`;trigger → UPDATE 下一节 `unlocked` |
| `fn_start_exam` | INSERT `course_user_exam_attempts(state='in_progress', snapshot)` |
| `fn_submit_exam` | UPDATE attempt(state, score, passed, finished_at);批量 INSERT `course_user_answers`(context=scope);trigger → 解锁下阶段 |
| `fn_report_question` | INSERT `course_content_action_log(action='report')`;UPDATE `course_questions.report_count += 1` |
| `fn_content_publish` | UPDATE `is_published`(+级联子项);INSERT `course_content_action_log(action='publish|unpublish')` |
| `OP-admin-015b:import` | 批量 INSERT KP/Question(source_batch_id);UPDATE batch.status='imported' |
| `OP-admin-020 POST media` | INSERT `course_media_assets` 或返已有(hash 命中)|
| `OP-internal-002:expire` | UPDATE `course_user_exam_attempts(state='expired', finished_at=now())` WHERE in_progress AND expires_at<now() |
| `cron purge-soft-deleted` | DELETE 5 张软删表 `WHERE deleted_at < now() - 30 days` |

## 3. 不变量(invariants)

| Invariant | 保障机制 |
|-----------|---------|
| `is_published=true ⇔ published_at IS NOT NULL` | CHECK 约束(lessons/kp/questions/exams)|
| `state='in_progress' ⇔ finished_at IS NULL` | CHECK |
| `action='report' ⇔ report_type IS NOT NULL` | CHECK |
| `score ≤ total_score` | CHECK |
| `pass_score ≤ total_score` | CHECK |
| 学员可见内容祖先全发布 | RLS policy 跨 JOIN |
| `(kp_id, q_type, payload_hash)` 唯一 | partial-UNIQUE |
| (track,stage_no) 唯一,且 stage_no=0 仅 share | partial-UNIQUE + CHECK |
| SRS box ∈ {1..5} 且间隔 1/3/7/14/30 天 | CHECK + `fn_srs_update` |
| 学员写入仅自己 user_id | RLS + RPC 校验 |
| 题目版本快照固化 | `course_user_answers.question_version` 写时快照 |
| exam snapshot 固化 question_ids | `course_user_exam_attempts.snapshot` jsonb |
| 单文件同类型导入幂等 | `(payload_hash, import_type)` EXISTS |
| 24h 内同题学员举报去重 | EXISTS + advisory lock |

## 4. 一致性结论

- 40 BR-ID 全闭环,无悬空;
- 副作用契约 11 条,全部在 D01/D02 文档落地;
- 不变量 12 条,全部由 CHECK / RLS / RPC / trigger 落实;
- 上游 [C05 PRD §13 实现 schema](../../C05-prd/course/PRD.md) 标注为 `zhiyu_course`,**与 F1 源(`zhiyu`)不一致**,本期统一采用 `zhiyu` 表前缀 `course_*`(见 [D01 _input/draft.md](../../D01-data/course/_input/draft.md));建议 C05 §13 后续微调。详见审计报告。

**判定**:✅ PASS(含 1 项需 C05 §13 文案调整,不影响实现)。
