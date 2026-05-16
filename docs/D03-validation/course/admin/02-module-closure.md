<!-- TARGET-PATH: docs/D03-validation/course/admin/02-module-closure.md -->

> **本文件为 surface=`admin` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端独立重写校验链路与 PRD 回链)。**


# D03-02 · 模块内闭环 · course

> **结论**:✅ PASS。表 CRUD / endpoint 写入 / 错误码 / 状态机 / RLS / cron 闭环无悬空。

## 1. 表 CRUD 闭环

| 表 | 创建 | 读 | 更新 | 删除 |
|----|------|---|------|------|
| course_tracks | seed | OP-app-001 / OP-admin-001 | OP-admin-001(PATCH name_i18n)| 不删 |
| course_stages | OP-admin-002 POST | OP-app-003 / OP-admin-002 | OP-admin-002 PATCH(If-Match)| OP-admin-002 DELETE(空检查)|
| course_chapters | OP-admin-003 POST | OP-app-003 / OP-admin-003 | OP-admin-003 PATCH | 软删 OP-admin-003 DELETE(空检查)|
| course_lessons | OP-admin-004 POST | OP-app-003/004 / OP-admin-004 | OP-admin-004 PATCH + bind-kps + reorder | 软删 OP-admin-004 DELETE |
| course_lesson_kp | OP-admin-004 bind-kps | OP-app-004 | DELETE+INSERT 替换 | CASCADE 节删除 |
| course_knowledge_points | OP-admin-007 / 015(导入)| OP-app-005 / OP-admin-005-006 | OP-admin-008 PATCH(If-Match)| 软删 OP-admin-009 |
| course_questions | OP-admin-013 / 015(导入) | OP-admin-010-011 | OP-admin-012 PATCH | 软删 OP-admin-014 |
| course_exams | OP-admin-021 POST | OP-app-013 / OP-admin-021 | OP-admin-021 PATCH | 软删 OP-admin-021 DELETE |
| course_user_progress | OP-app-004 首次进节 UPSERT | OP-app-003/019 / 自身 | OP-app-007/010 | CASCADE 账号删除 |
| course_user_answers | OP-app-009 INSERT(RPC)| OP-app-012 / OP-admin-011 聚合 | 禁(append-only)| 月分区归档 |
| course_user_srs | RPC `fn_srs_update` UPSERT | OP-app-011 | UPSERT | CASCADE |
| course_user_exam_attempts | OP-app-014 INSERT | OP-app-015 / OP-admin-010 | OP-app-016/017 + cron 超期 | CASCADE 账号 |
| course_import_batches | OP-admin-015 POST | OP-admin-015 GET | OP-admin-015b PATCH status | 保留(审计)|
| course_content_action_log | OP-app-018 / OP-admin-016/019 | OP-admin-017/018 | 禁(append-only)| 90 天 cron 清理 |
| course_media_assets | OP-app-006(TTS)/ OP-admin-020 | OP-admin-020 / public CDN | 禁(hash 决定)| OP-admin-020 DELETE → 7 天 cron |

## 2. 错误码 vs endpoint 覆盖

- 55 个错误码,在 `04-error-codes.md` 全部登记;
- 每个错误码至少在一个 endpoint 文档(03-endpoints/*)以 "错误:" 字段引用;
- 抽样验证:
  - `COURSE_STALE_VERSION` → 出现在所有管理端 PATCH(catalog/kp-question/media-exam);
  - `COURSE_EXAM_EXPIRED` → OP-app-015/016/017 + OP-internal-002;
  - `COURSE_REPORT_DUPLICATE` → OP-app-018 + RPC `fn_report_question`;
- 兜底 `COURSE_INTERNAL_ERROR` 由中间件统一抛。

## 3. 状态机闭环

- SM-course-progress:`locked → unlocked → in_progress → passed`;
  - `locked → unlocked`:trigger `tg_after_lesson_pass_unlock_next` / `tg_after_stage_exam_passed_unlock_next_stage`;
  - `unlocked → in_progress`:OP-app-004 首次 UPSERT;
  - `in_progress → passed`:`fn_lesson_pass`;
  - `passed → in_progress`:禁(只能保留 best_score)。
- SM-course-attempt:`in_progress → submitted/abandoned/expired`,3 个终态,无回流;
- SM-course-import:`draft → validating → ready/failed → imported/cancelled`,失败可回 ready(修文件重传 → 新批次);
- SM-course-publish:`unpublished(false) ⇄ published(true) → soft_deleted`,三态闭环。

## 4. RLS 闭环

- 学员侧 `select` 严格 `is_published AND deleted_at IS NULL AND 祖先链`,无遗漏表;
- 学员侧 `user_*` 表 `user_id = auth.uid()`,所有 5 张表(progress/answers/srs/exam_attempts + report 写入 RPC)覆盖;
- 管理端 `service_role`,应用层 `tracks_scope` 在每条 SQL 显式叠加。

## 5. cron 闭环

- 5 个 cron job 全部在 [06-events.md](../../D02-api/course/06-events.md) 登记;
- 对应内部 endpoint 在 [10-internal.md](../../D02-api/course/03-endpoints/10-internal.md) 全覆盖;
- 文件名模板:`system/scripts/cron/expire-exam-attempts.ts` 等,落地路径明确。

**判定**:✅ PASS
