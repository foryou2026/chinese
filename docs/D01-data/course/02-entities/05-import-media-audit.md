<!-- TARGET-PATH: docs/D01-data/course/02-entities/05-import-media-audit.md -->

# 02-5 · 导入批次 + 媒资 + 操作日志(3 表) · course

> 直读 F1:[05-表定义-内容导入与媒资.md](../../../../function/02-course/ai/F1-AI-数据模型规范/05-表定义-内容导入与媒资.md)。

---

## T13 · `course_import_batches`(导入追溯)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| batch_code | text | UNIQUE;CHECK `~ '^imp_(kp|question|media)_\d{8}_\d{4}$'`;应用层生成 |
| import_type | text | CHECK `IN ('kp','question','media')` |
| track | text | FK `course_tracks(code)` ON DELETE RESTRICT(可空,media 可跨主题)|
| source_file_name | text | 1–255 |
| source_file_url | text |  | CDN 路径 |
| payload_hash | text | CHECK `~ '^[a-f0-9]{64}$'`;幂等键 |
| row_count / success_count / failed_count | int | CHECK ≥ 0 |
| validation_errors | jsonb | 行级错误数组 |
| status | text | CHECK `IN ('draft','validating','ready','imported','failed','cancelled')` |
| created_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| created_at / updated_at | timestamptz |  |

- 索引:`uq_course_import_batch_code`、`idx_course_import_type / track / status / creator / created / hash`;
- RLS:`select / write` content_admin+(走 service_role + 应用鉴权);
- 幂等:重传同 `(payload_hash, import_type)` → 返回已有批次。

## T14 · `course_media_assets`(媒资库,hash 去重)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| kind | text | CHECK `IN ('audio','image','video','svg','lottie')` |
| url | text | 1–500 |
| hash | text | UNIQUE;CHECK `~ '^[a-f0-9]{64}$'`(sha256)|
| meta | jsonb | 默认 `'{}'`;`{duration_ms, bitrate, format, width, height, ...}` |
| source | text | CHECK `IN ('tts','human_recorded','uploaded','stock_library')` |
| voice_profile | text |  | ≤80,仅 audio |
| ref_kp_id | uuid | FK `course_knowledge_points(id)` ON DELETE SET NULL(弱引用)|
| ref_q_id | uuid | FK `course_questions(id)` ON DELETE SET NULL |
| created_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| created_at | timestamptz |  |

- 索引:`uq_course_ma_hash`、`idx_course_ma_kind / source / kp / q`;
- RLS:`select` 全部角色 public;`write` service_role;
- 软删策略:无 `deleted_at` 字段,但删除前应用层反查 `ref_kp_id / ref_q_id` + `course_knowledge_points.audio_url/image_url LIKE url` + `course_questions.audio_url/image_url LIKE url`;有引用 → 拒;无引用 → 进 cron 待清队列(7 天后 CDN 物理删)。

## T15 · `course_content_action_log`(操作日志 + 学员举报)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| target_type | text | CHECK `IN ('kp','question','lesson','exam')` |
| target_id | uuid | 多态弱引用 |
| action | text | CHECK `IN ('edit','publish','unpublish','archive','report','dismiss','adopt')` |
| actor_id | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| actor_role | text | CHECK `IN ('learner','content_admin','super')` |
| reason | text | CHECK len ≤ 500 |
| report_type | text | CHECK `(action='report' → IN ('wrong_answer','wrong_translation','wrong_audio','wrong_image','other')) AND (action<>'report' → NULL)` |
| diff | jsonb | 仅 `action='edit'` 时记录前后差异 |
| created_at | timestamptz |  |

- 索引:`idx_course_cal_target (target_type, target_id, created_at DESC)`、`idx_course_cal_action`、`idx_course_cal_actor`、`idx_course_cal_created`;
- RLS:
  - 学员仅 `INSERT WHERE action='report' AND actor_id=auth.uid()` 通过 RPC `fn_report_question`;
  - 管理端 `service_role` 全量;
- 24 小时去重举报由应用层 + `idx_course_cal_actor / target` 在 RPC 内 `EXISTS` 检查。
