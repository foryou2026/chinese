<!-- TARGET-PATH: docs/D01-data/course/01-er-diagram.md -->

# 01 · ER 图 · course

```mermaid
erDiagram
  course_tracks ||--o{ course_stages : "track_code"
  course_stages ||--o{ course_chapters : "stage_id"
  course_chapters ||--o{ course_lessons : "chapter_id"
  course_lessons ||--o{ course_lesson_kp : "lesson_id"
  course_knowledge_points ||--o{ course_lesson_kp : "kp_id"
  course_knowledge_points ||--o{ course_questions : "kp_id"
  course_tracks ||--o{ course_knowledge_points : "primary_track"
  course_tracks ||--o{ course_import_batches : "track"
  course_import_batches ||--o{ course_knowledge_points : "source_batch_id"
  course_import_batches ||--o{ course_questions : "source_batch_id"
  course_knowledge_points ||--o{ course_media_assets : "ref_kp_id"
  course_questions ||--o{ course_media_assets : "ref_q_id"
  course_exams }o--o{ course_lessons : "scope_ref_id 多态"
  course_exams }o--o{ course_chapters : "scope_ref_id 多态"
  course_exams }o--o{ course_stages : "scope_ref_id 多态"
  course_lessons ||--o{ course_user_progress : "lesson_id"
  course_questions ||--o{ course_user_answers : "question_id"
  course_knowledge_points ||--o{ course_user_answers : "kp_id"
  course_knowledge_points ||--o{ course_user_srs : "kp_id"
  course_exams ||--o{ course_user_exam_attempts : "exam_id"
  course_content_action_log }o..o{ course_questions : "target_id 多态"
  course_content_action_log }o..o{ course_knowledge_points : "target_id 多态"
  course_content_action_log }o..o{ course_lessons : "target_id 多态"
  course_content_action_log }o..o{ course_exams : "target_id 多态"
```

## 主键 / 外键策略
- 全表主键 `uuid`(`gen_random_uuid()`);业务唯一键单独 UNIQUE;
- 父子链 (`tracks → stages → chapters → lessons`) FK `ON DELETE RESTRICT`(禁止误删父级);
- 学员相关 (`user_*`) FK `ON DELETE CASCADE`(账号注销级联清理);
- 多态弱引用(`exams.scope_ref_id`, `content_action_log.target_id`, `media_assets.ref_*`)无 FK 约束,由应用层 + 触发器保证;
- 角色字段 (`created_by / updated_by / created_admin_id / actor_id`) FK → `auth.users(id) ON DELETE SET NULL`(参考 B02 `AUTH_USE_USER_ENTRY=false` 阶段策略,后续如启用扩展表则随之迁移)。
