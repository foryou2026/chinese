<!-- TARGET-PATH: docs/D01-data/course/02-entities/02-kp-question.md -->

# 02-2 · KP + Question(2 表) · course

> 直读 F1:[02-表定义-知识点与题目.md](../../../../function/02-course/ai/F1-AI-数据模型规范/02-表定义-知识点与题目.md)。

---

## T06 · `course_knowledge_points`(KP 主表,~1.2 万)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| kp_code | text | partial-UNIQUE;CHECK `~ '^kp_(share|ec|fc|hsk|dl)_(p|h|w|ph|g|s|d)_\d{6}$'`;触发器 `tg_before_insert_course_kp_set_code` 自动调 `fn_gen_kp_code(track, kp_type)` |
| kp_type | text | CHECK `IN ('pinyin','hanzi','word','phrase','grammar','sentence','dialog')` |
| primary_track | text | FK `course_tracks(code)` ON DELETE RESTRICT |
| title_zh | text | 1–60 |
| pinyin | text | 1–200 |
| difficulty | int | CHECK 1–6,默认 1 |
| hsk_level | int | CHECK NULL OR 1–6 |
| content | jsonb | 7 种 KP 类型差异结构,必填 |
| translations | jsonb |  | 5 语必填 `?& {zh,en,vi,th,id}`(可为 null,有则全填)|
| audio_url | text |  |
| image_url | text |  |
| tags | text[] | 默认 `'{}'`,GIN 索引 |
| is_published | bool | 默认 false |
| version | int | 默认 1,CHECK ≥ 1;编辑保存 `version += 1` |
| source_batch_id | uuid | FK `course_import_batches(id)` ON DELETE SET NULL |
| published_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| published_at | timestamptz |  |
| created_at / updated_at | timestamptz |  |
| deleted_at | timestamptz | 软删 |

**索引**(全 `WHERE deleted_at IS NULL` 部分索引):
- `uq_course_kp_code` UNIQUE;
- `idx_course_kp_type / track / published / difficulty / title_zh / source_batch`;
- GIN:`idx_course_kp_tags_gin (tags)`、`idx_course_kp_content_gin (content)`;
- `idx_course_kp_deleted_at`。

**RLS**:
- `select` authed → `is_published=true AND deleted_at IS NULL`;
- `select` anon → 拒;
- 写 → `service_role`。

**序列**:35 个 sequence `seq_course_kp_<track>_<type_initial>`(5 主题 × 7 KP 类型),容量 999 999 / (track,type)。

---

## T07 · `course_questions`(题库,~5 万)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| q_code | text | partial-UNIQUE;CHECK `~ '^q_(share|ec|fc|hsk|dl)_\d{8}$'`;触发器 `tg_before_insert_course_q_set_code` 调 `fn_gen_q_code(track)` |
| kp_id | uuid | FK `course_knowledge_points(id)` ON DELETE RESTRICT |
| q_type | text | CHECK 12 种:`mcq_meaning / mcq_zh / listen_pick / listen_pinyin / tone_pick / match_pairs / sort_words / fill_blank_choice / type_pinyin / type_zh_ime / image_pick / dialog_cloze` |
| exam_scope | text[] | GIN;CHECK `array_length >= 1` 且子集 `{practice, lesson_quiz, chapter_test, stage_exam, hsk_mock}` |
| difficulty | int | CHECK 1–6(已弱化,2025-11 决策,以 KP 难度为准)|
| payload | jsonb | 题型差异结构,必填 |
| payload_hash | text | CHECK `~ '^[a-f0-9]{64}$'`;partial-UNIQUE `(kp_id, q_type, payload_hash)` 去重(F1 决策 Q9)|
| audio_url / image_url | text |  |
| is_published | bool | 默认 false |
| version | int | 默认 1;CHECK ≥ 1 |
| source_batch_id | uuid | FK `course_import_batches(id)` ON DELETE SET NULL |
| published_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| published_at | timestamptz |  |
| report_count | int | 默认 0,CHECK ≥ 0;`fn_report_question` 自增 |
| created_at / updated_at | timestamptz |  |
| deleted_at | timestamptz | 软删 |

**索引**(全 `WHERE deleted_at IS NULL`):
- `uq_course_q_code` UNIQUE;
- `uq_course_q_kp_qtype_hash (kp_id, q_type, payload_hash)` UNIQUE 去重;
- `idx_course_q_kp / type / published / difficulty / source_batch / report_count`;
- GIN `idx_course_q_exam_scope (exam_scope)`;
- `idx_course_q_deleted_at`。

**RLS**:同 KP。

**序列**:5 个 sequence `seq_course_q_<track>`,容量 99 999 999 / track。

**软删与流水**:
- 若 `course_user_exam_attempts.snapshot` 仍引用该 `q_id` → 删除被拦截(应用层校验,返 `COURSE_KP_STILL_REFERENCED` / 题对应错误码);
- 修正后 `version += 1`,旧 `course_user_answers.question_version` 保留原始版本,**不追溯改分**。
