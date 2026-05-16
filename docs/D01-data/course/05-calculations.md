<!-- TARGET-PATH: docs/D01-data/course/05-calculations.md -->

# 05 · 计算与算法 · course

## 5.1 SRS Leitner 5 盒(`fn_srs_update`)

```
答对:
  box_new        = min(box + 1, 5)
  correct_streak = correct_streak + 1
  due_at         = now() + interval [1, 3, 7, 14, 30] days  -- 按 box_new

答错:
  box_new        = 1
  correct_streak = 0
  wrong_count    = wrong_count + 1
  due_at         = now() + interval '1 day'

无论对错:
  last_seen_at = now()
  last_q_type  = <q_type>
```

- 触发场景:`context_type IN ('lesson_quiz','chapter_test','stage_exam','hsk_mock','srs_review')` → 调用;`context_type='practice'` 不更新 SRS;
- 一次答题仅更新该题对应 1 个 KP 的 SRS 行;
- UPSERT 原子化,无双计风险。

## 5.2 SRS 单日发卡预算(BR-AS-03)

```sql
remaining_today = 50 - (
  select count(*) from course_user_answers
  where user_id = $user_id
    and context_type = 'srs_review'
    and answered_at >= date_trunc('day', now() at time zone 'Asia/Shanghai')
)
```

返发卡数量 = `min(limit, remaining_today)`;= 0 时返 `COURSE_SRS_DAILY_LIMIT_EXCEEDED`(C 端展示为友好提示)。

## 5.3 节末小测评分(`fn_lesson_pass`)

```
quiz_score = sum(each_question.score / 10 * 100) / question_count   -- 0..100
passed     = quiz_score >= pass_score   -- 默认 60
best_score = greatest(coalesce(best_score, 0), quiz_score)
attempts   = attempts + 1
若 passed:
  status     = 'passed'
  passed_at  = now()
否则:
  status     = 'in_progress'(允许重试)
```

## 5.4 试卷评分(`fn_submit_exam`)

```
单题分 = total_score / array_length(snapshot.q_ids)
attempt.score  = round(sum(per_question_score), 2)
attempt.passed = attempt.score >= exam.pass_score
attempt.state  = 'submitted'
attempt.finished_at = now()
```

- `state='expired'`:cron 标,不主动算分;学员查 attempt 详情时若 `state='expired'` 且 `finished_at IS NULL` → 应用层补算 + 写库;
- `state='abandoned'`:`score=0, passed=false`;
- 阶段考 `passed=true` → 触发器 `tg_after_stage_exam_passed_unlock_next_stage` 解锁下阶段所有节(`status='unlocked'`)。

## 5.5 版本号自增

- 触发器 `tg_*_before_update_bump_version`:`OLD.payload IS DISTINCT FROM NEW.payload` → `NEW.version = OLD.version + 1`;
- 仅 payload / content 变动才自增;is_published / report_count 等不触发;
- `course_user_answers.question_version` 在 INSERT 时由 RPC 写入 = `course_questions.version`(当时值)。

## 5.6 月分区(`course_user_answers`)

- 工具:`pg_partman`(默认安装);
- 命名:`course_user_answers_yYYYY_mMM`(如 `course_user_answers_y2026_m05`);
- 创建:`pg_partman.create_parent` 一次,后续 cron(`run_maintenance_proc`)每天 02:00 预创 3 个月分区;
- 归档:超过 24 个月分区移交对象存储(后续 P2 实现,本期保留 SQL stub);
- 不允许 UPDATE/DELETE(RLS 拒,且生产 service 也不需要)。

## 5.7 cron 频率

| Job | 频率 | 用途 |
|-----|------|------|
| `expire-exam-attempts.ts` | 每分钟 | `state='in_progress' AND now()>expires_at → 'expired'` |
| `purge-soft-deleted-course.ts` | 每天 00:30 | `DELETE WHERE deleted_at < now() - interval '30 days'` |
| `purge-pending-media.ts` | 每天 02:00 | 7 天保留窗后 CDN 物理删 |
| `REFRESH MV mv_course_user_daily` | 每 5 分钟 | CONCURRENTLY |
| `REFRESH MV mv_course_track_stats` | 每 10 分钟 | CONCURRENTLY |
| `pg_partman run_maintenance_proc` | 每天 02:00 | 预创月分区 |

## 5.8 学员举报 24 小时去重(`fn_report_question`)

```sql
exists (
  select 1 from course_content_action_log
  where action = 'report'
    and actor_id = $user_id
    and target_type = 'question'
    and target_id = $question_id
    and created_at > now() - interval '24 hours'
)
→ true → 返 COURSE_REPORT_DUPLICATE
→ false → INSERT log + UPDATE report_count + 1
```
