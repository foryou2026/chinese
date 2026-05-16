<!-- TARGET-PATH: docs/D03-validation/course/01-upstream-chain.md -->

# D03-01 · 上游链一致性 · course

> 校验范围:[C01](../../C01-requirements/course/baseline.md) → [C02](../../C02-ia/course/00-index.md) → [C03](../../C03-pages/course/00-index.md) → [C05 PRD](../../C05-prd/course/PRD.md) → [D01](../../D01-data/course/00-index.md) → [D02](../../D02-api/course/00-index.md)。
> **结论**:✅ PASS。30 R-ID / 40 BR / 17 P-ID / 7 SM 全部解析,数据/接口无遗漏。

## 1. R-ID → BR-ID → 数据/接口 映射(精选 12 条核心,完整 30 条见 [C05 PRD §1.2 矩阵](../../C05-prd/course/PRD.md))

| R-ID | 简述 | BR | 表 | OP-ID |
|------|------|----|----|-------|
| R-CRS-01 | 5 主题地图 | BR-CAT-01 | `course_tracks` `course_stages` `course_chapters` `course_lessons` `course_user_progress` | OP-course-app-001/003 |
| R-CRS-02 | 节学习 12 KP | BR-KP-03 | `course_lessons` `course_lesson_kp` `course_knowledge_points` | OP-course-app-004/005 |
| R-CRS-03 | 7 KP 类型 | BR-KP-01 | `course_knowledge_points` | (后台 OP-A5..A9) |
| R-CRS-04 | 12 题型作答 | BR-AS-01 | `course_questions` `course_user_answers` | OP-course-app-009 |
| R-CRS-05 | SRS Leitner | BR-AS-02/03 | `course_user_srs` `course_user_answers` | OP-course-app-009/011 |
| R-CRS-06 | 节末小测 | BR-PRG-02 | `course_user_progress` `course_questions` | OP-course-app-008/010 |
| R-CRS-07 | 章/阶段/HSK 考试 | BR-EX-01..05 | `course_exams` `course_user_exam_attempts` | OP-course-app-013..017 |
| R-CRS-08 | 错题本 | BR-AS-03 | `course_user_answers` `course_user_srs` | OP-course-app-012 |
| R-CRS-09 | 学员举报 | BR-RP-01..03 | `course_content_action_log` `course_questions` | OP-course-app-018 / OP-course-admin-018/019 |
| R-CRS-10 | TTS 触发 | BR-MD-01 | `course_media_assets` | OP-course-app-006 |
| R-CRS-11 | 断点续学 | BR-PRG-03 | `course_user_progress` | OP-course-app-007 |
| R-CRS-12 | 个人统计 | BR-PRG-01 | `mv_course_user_daily` | OP-course-app-019 |
| R-CRS-13 | 主题切换 | BR-CAT-01 | `auth_user_profiles.current_track` | OP-course-app-002 |
| R-CRS-14 | 5 语翻译 | BR-CAT-04 | jsonb `*_i18n / translations` | 全 endpoint |
| R-CRS-20..29 | 后台运营 | BR-PUB / BR-KP / BR-IM / BR-MD | 全 15 表 | OP-course-admin-001..024 |
| R-CRS-30 | 内部任务 | BR-EX-04 / BR-CAT-05 / BR-MD-03 | — | OP-course-internal-001..003 |

## 2. P-ID → endpoint 映射

| P-ID | 页面 | 主要 OP |
|------|------|--------|
| P-app-course-001 | 主题首页 | OP-app-001/002 |
| P-app-course-002 | 学习地图 | OP-app-003 |
| P-app-course-003 | 节学习 | OP-app-004/005/006/007/009 |
| P-app-course-004 | 节末小测 | OP-app-008/010 |
| P-app-course-005 | SRS 复习 | OP-app-011/009 |
| P-app-course-006 | 考试入口 | OP-app-013/014 |
| P-app-course-007 | 考试中 / 结果 | OP-app-015/016/017 |
| P-app-course-008 | 错题本 / Profile | OP-app-012/018/019 |
| P-admin-course-001 | 目录管理 | OP-admin-001..004 |
| P-admin-course-002 | KP 库 | OP-admin-005..009 |
| P-admin-course-003 | 题目库 | OP-admin-010..014 |
| P-admin-course-004 | 内容导入 | OP-admin-015 |
| P-admin-course-005 | 发布/下架 | OP-admin-016 |
| P-admin-course-006 | 举报处理 | OP-admin-018/019 |
| P-admin-course-007 | 媒资库 | OP-admin-020 |
| P-admin-course-008 | 考试中心 | OP-admin-021/022 |
| P-admin-course-009 | 操作日志 / 统计 | OP-admin-017/023/024 |

## 3. SM-ID → 表/RPC 映射

| SM-ID | 状态机 | 落点 |
|-------|--------|------|
| SM-course-publish | 内容发布(KP/Q/Lesson/Chapter/Stage/Exam) | `is_published / deleted_at` + `fn_content_publish` |
| SM-course-import | 导入批次 6 态 | `course_import_batches.status` |
| SM-course-progress | 节进度 4 态 | `course_user_progress.status` + `tg_after_lesson_pass_unlock_next` |
| SM-course-attempt | 考试 attempt 4 态 | `course_user_exam_attempts.state` + cron + `fn_submit_exam` |
| SM-course-srs | SRS box 1–5 + due_at | `course_user_srs` + `fn_srs_update` |
| SM-course-report | 学员举报 → 处理 | `course_content_action_log(action='report|dismiss|adopt')` |
| SM-course-quiz | 节末小测 quiz_id 内存 TTL | Redis kv + `OP-app-008/010` |

## 4. 一致性结论

- 30 R-ID 全部追溯到表 + endpoint;
- 40 BR-ID 全部映射 DBR(D01-03) + endpoint;
- 17 P-ID 全部对接 OP-ID;
- 7 SM 全部有触发器 / 字段约束 / cron 落点。

**判定**:✅ PASS
