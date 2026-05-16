<!-- TARGET-PATH: docs/D01-data/course/02-entities/01-catalog.md -->

# 02-1 · 课程目录(5 表) · course

> 表族:`course_tracks → course_stages → course_chapters → course_lessons` + 多对多 `course_lesson_kp`。
> 直读 F1:[01-表定义-课程目录.md](../../../../function/02-course/ai/F1-AI-数据模型规范/01-表定义-课程目录.md)。

---

## T01 · `course_tracks`(主题字典,5 条固定)

| 字段 | 类型 | 必填 | 默认 | 说明 |
|------|------|:--:|------|------|
| id | uuid | ✓ | gen_random_uuid() | PK |
| code | text | ✓ | — | UNIQUE, CHECK `IN ('share','ec','fc','hsk','dl')` |
| name_zh | text | ✓ | — | 1–20 |
| name_i18n | jsonb | ✓ | — | 5 语必填 `?& {zh,en,vi,th,id}` |
| icon_url | text |  | null | URL |
| sort_order | int | ✓ | 0 | 列表顺序 |
| is_enabled | bool | ✓ | true | 临时下线开关 |
| created_at / updated_at | timestamptz | ✓ | now() | 触发器维护 |

- 索引:`uq_course_tracks_code` / `idx_course_tracks_sort_order`;
- RLS:`select` 给 anon/authed 仅 `is_enabled=true`;`insert/update/delete` 仅 `service_role`;
- 软删:否(永不删,只 `is_enabled=false`)。

## T02 · `course_stages`(阶段,25 条)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| track_code | text | FK `course_tracks(code)` ON DELETE RESTRICT |
| stage_no | int | UNIQUE `(track_code, stage_no)`;CHECK 0–6;`stage_no=0 → track_code='share'` |
| title_zh | text | 1–40 |
| title_i18n | jsonb | 5 语必填 |
| desc_i18n | jsonb |  | ≤200/lang |
| hsk_mapping | text | CHECK `~ '^HSK[1-6]$'`(仅 hsk track 用)|
| unlock_rule | jsonb | 默认 `{"prev_stage_pass":true}`;schema = `{prev_stage_pass, require_shared_stage_done, min_score}` |
| vocab_increment | int | 0–5000 |
| sort_order | int | 默认 0 |
| is_published | bool | 默认 false |
| created_at / updated_at | timestamptz |  |

- 索引:`uq_course_stages_track_stage / idx_course_stages_track / idx_course_stages_published`;
- RLS:同 tracks;
- 软删:否。

## T03 · `course_chapters`(章,~148 条)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| stage_id | uuid | FK `course_stages(id)` ON DELETE RESTRICT |
| chapter_no | int | CHECK 1–20;partial-UNIQUE `(stage_id, chapter_no)` WHERE `deleted_at IS NULL` |
| title_zh | text | 1–40 |
| title_i18n | jsonb | 5 语必填 |
| cover_url | text |  |
| sort_order | int |  |
| is_published | bool |  |
| created_at / updated_at | timestamptz |  |
| deleted_at | timestamptz | 软删 |

- 索引:`uq_course_chapters_stage_no` (WHERE `deleted_at IS NULL`)、`idx_course_chapters_stage`、`idx_course_chapters_published`、`idx_course_chapters_deleted_at`;
- RLS:`select` authed → `is_published=true AND deleted_at IS NULL` 且 `parent_stage.is_published=true`;
- 软删:30 天后 cron 物理清理。

## T04 · `course_lessons`(节,~888 条)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| chapter_id | uuid | FK `course_chapters(id)` ON DELETE RESTRICT |
| lesson_no | int | CHECK 1–30;partial-UNIQUE `(chapter_id, lesson_no)` |
| code | text | partial-UNIQUE;CHECK `~ '^(share|ec|fc|hsk|dl)-\d{1,2}-\d{1,2}-\d{1,2}$'` |
| title_zh | text | 1–40 |
| title_i18n | jsonb | 5 语必填 |
| goal_i18n | jsonb |  | ≤80/lang |
| est_minutes | int | CHECK 5–30,默认 12 |
| sort_order | int |  |
| has_quiz | bool | 默认 true(可关闭节末小测)|
| is_published | bool | 默认 false |
| published_at | timestamptz | CHECK `(is_published AND NOT NULL) OR (NOT is_published AND NULL)` |
| created_by / updated_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| created_at / updated_at | timestamptz |  |
| deleted_at | timestamptz | 软删 |

- 索引(全部 `WHERE deleted_at IS NULL`):`uq_course_lessons_code`、`uq_course_lessons_chapter_no`、`idx_course_lessons_chapter`、`idx_course_lessons_published`、`idx_course_lessons_published_at`、`idx_course_lessons_deleted_at`;
- RLS:`select` authed → `is_published=true AND deleted_at IS NULL` 且祖先链全发布(chapter + stage + track);
- 软删:同 chapters。

## T05 · `course_lesson_kp`(多对多)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| lesson_id | uuid | PK 一部分;FK `course_lessons(id)` ON DELETE CASCADE |
| kp_id | uuid | PK 一部分;FK `course_knowledge_points(id)` ON DELETE RESTRICT |
| position | int | CHECK 1–50 |
| is_new_in_lesson | bool | 默认 true(新学 / 复习区分)|
| created_at | timestamptz |  |

- 索引:`idx_course_lesson_kp_lesson_pos (lesson_id, position)`、`idx_course_lesson_kp_kp (kp_id)`;
- RLS:跟随父节可见性;
- 软删:无(节级软删时通过 CASCADE 删除关系)。
