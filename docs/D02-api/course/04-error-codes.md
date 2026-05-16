<!-- TARGET-PATH: docs/D02-api/course/04-error-codes.md -->

# 04 · 错误码登记 · course

> 全部以 `COURSE_` 开头。HTTP 列为默认状态码,部分接口可微调。

## 4.1 字段格式 / 长度 / 范围 (400)

| Code | 触发 |
|------|------|
| `COURSE_FIELD_TOO_LONG` | 字段长度超限 |
| `COURSE_INVALID_TRACK_CODE` | track 不在 5 枚举 |
| `COURSE_INVALID_LESSON_CODE` | lesson code 格式错 |
| `COURSE_INVALID_KP_CODE` | kp_code 格式错 |
| `COURSE_INVALID_Q_CODE` | q_code 格式错 |
| `COURSE_INVALID_KP_TYPE` | kp_type 非 7 枚举 |
| `COURSE_INVALID_Q_TYPE` | q_type 非 12 枚举 |
| `COURSE_SCORE_OUT_OF_RANGE` | best_score 越界 |
| `COURSE_ITEM_SCORE_OUT_OF_RANGE` | answer.score 不在 0–10 |
| `COURSE_DURATION_OUT_OF_RANGE` | duration_ms 越界 |
| `COURSE_SRS_BOX_INVALID` | box 非 1–5 |
| `COURSE_EXAM_SCORE_OUT_OF_RANGE` | attempt.score 越界 |
| `COURSE_PASS_SCORE_OUT_OF_RANGE` | pass_score 越界 |
| `COURSE_EXAM_TIME_LIMIT_INVALID` | time_limit 越界 |

## 4.2 Schema / 一致性 (400)

| Code | 触发 |
|------|------|
| `COURSE_KP_CONTENT_SCHEMA_MISMATCH` | content jsonb 不匹配 kp_type |
| `COURSE_PAYLOAD_SCHEMA_MISMATCH` | payload jsonb 不匹配 q_type |
| `COURSE_LESSON_CODE_MISMATCH` | lesson.code 与父级编号不一致 |
| `COURSE_EXAM_BLUEPRINT_OUT_OF_SCOPE` | blueprint KP 范围超出 scope |
| `COURSE_KP_NOT_IN_LESSON` | checkpoint last_kp_id 不属于该 lesson |
| `COURSE_QUIZ_INCOMPLETE_ANSWERS` | submit 缺答 |
| `COURSE_REPORT_TYPE_REQUIRED` | 举报缺 report_type |

## 4.3 状态机 / 业务流 (403 / 410 / 429)

| Code | HTTP | 触发 |
|------|------|------|
| `COURSE_PREREQUISITE_NOT_MET` | 403 | 前置 stage / lesson 未通过 |
| `COURSE_LESSON_QUIZ_REQUIRED` | 403 | 强制小测未过 |
| `COURSE_LESSON_NOT_ENTERED` | 403 | 未进节就答 quiz 题 |
| `COURSE_EXAM_LOCKED` | 403 | 考试未解锁 |
| `COURSE_STAGE_EXAM_ALREADY_PASSED` | 403 | 阶段考已通过 |
| `COURSE_QUIZ_EXPIRED` | 410 | quiz_id 过期(10 分钟)|
| `COURSE_EXAM_EXPIRED` | 410 | attempt 已超时 |
| `COURSE_SRS_NOT_DUE` | 403 | 强制取未到期 KP |
| `COURSE_SRS_DAILY_LIMIT_EXCEEDED` | 429 | 今日 50 张已发完 |
| `COURSE_INVALID_PUBLISH_ACTION` | 400 | 发布状态机不允许 |

## 4.4 唯一 / 外键 / 引用 (409)

| Code | 触发 |
|------|------|
| `COURSE_IMPORT_DUPLICATE` | 重复导入 / 重复同 scope exam / 题级 payload_hash 冲突 |
| `COURSE_REPORT_DUPLICATE` | 24h 内同题再次举报 |
| `COURSE_LESSON_NO_DUPLICATE` | (chapter, lesson_no) 冲突 |
| `COURSE_STAGE_NOT_EMPTY` | 阶段下仍有章 |
| `COURSE_CHAPTER_NOT_EMPTY` | 章下仍有节 |
| `COURSE_KP_STILL_REFERENCED` | KP 仍被节/题目引用 |
| `COURSE_MEDIA_STILL_REFERENCED` | 媒资仍被引用 |
| `COURSE_EXAM_HAS_ACTIVE_ATTEMPTS` | 删 exam 时有进行中 attempt |
| `COURSE_FIELD_IMMUTABLE` | 改不可变字段(kp_code/q_code/track 等)|
| `COURSE_CASCADE_TARGET_EMPTY` | 发布时无有效子项 |
| `COURSE_EXAM_EFFECTIVE_QUESTION_EMPTY` | 抽题时已发布题不足 |
| `COURSE_REPORT_ALREADY_HANDLED` | 举报已处理 |

## 4.5 并发 / 锁 (409)

| Code | 触发 |
|------|------|
| `COURSE_STALE_VERSION` | If-Match `updated_at` 不一致 |
| `COURSE_IMPORT_HAS_ERRORS` | 导入批次有阻断错误,无法 import |

## 4.6 权限 / 鉴权 (401 / 403 / 429)

| Code | HTTP | 触发 |
|------|------|------|
| `COURSE_NOT_VISIBLE` | 404(隐藏存在) | 学员访问不可见内容(RLS 拒)|
| `COURSE_FORBIDDEN_OTHER_USER` | 403 | 操作他人 user_* 数据 |
| `COURSE_IMMUTABLE_RECORD` | 403 | 流水不可改/删 |
| `COURSE_ADMIN_ONLY` | 403 | 角色不足 / tracks_scope 不覆盖 |
| `COURSE_RATE_LIMIT` | 429 | 限流命中 |

## 4.7 通用 (兜底)

| Code | HTTP | 触发 |
|------|------|------|
| `COURSE_NOT_FOUND` | 404 | 资源不存在(应用层主动判定后返,与 RLS 隐式 404 区分)|
| `COURSE_INTERNAL_ERROR` | 500 | 未捕获异常 |

合计:**55** 个 `COURSE_*` 错误码。
