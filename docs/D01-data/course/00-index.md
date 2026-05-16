<!-- TARGET-PATH: docs/D01-data/course/00-index.md -->

# D01 · 数据规范索引 · course

> **阶段**:D01-D · **feature**:`course` · **冻结状态**:已冻结 · 2026-05-16
> **schema**:`zhiyu`(表名前缀 `course_*`)
> **上游**:[C05 PRD](../../C05-prd/course/PRD.md) · F1 课程数据模型规范
> **下游**:D02 接口 / D03 校验

## 子文件导航

| 文件 | 内容 |
|------|------|
| [01-er-diagram.md](./01-er-diagram.md) | 15 张表 ER 图 |
| [02-entities/01-catalog.md](./02-entities/01-catalog.md) | 5 课程目录表(tracks/stages/chapters/lessons/lesson_kp) |
| [02-entities/02-kp-question.md](./02-entities/02-kp-question.md) | KP + Question 主表 |
| [02-entities/03-exam.md](./02-entities/03-exam.md) | 试卷模板 + 学员答卷 |
| [02-entities/04-progress.md](./02-entities/04-progress.md) | 节进度 + 答题流水 + SRS |
| [02-entities/05-import-media-audit.md](./02-entities/05-import-media-audit.md) | 导入批次 + 媒资 + 内容操作日志 |
| [03-business-rules.md](./03-business-rules.md) | 数据层业务规则(级联 / 发布 / SRS)|
| [04-validations.md](./04-validations.md) | 字段校验汇总 |
| [05-calculations.md](./05-calculations.md) | SRS 算法 / 考试评分 / cron / 分区 |
| [06-indexes.md](./06-indexes.md) | UNIQUE / partial / GIN 索引清单 |
| [07-volume-growth.md](./07-volume-growth.md) | 数据量级与增长基线 |
| [08-seed-data.md](./08-seed-data.md) | 种子数据(5 主题 + 25 阶段 + 占位媒资)|
| [99-open-questions.md](./99-open-questions.md) | 待确认(已清空)|

## 关键约束

- **5 主题码白名单**:`share / ec / fc / hsk / dl`(CHECK 固化,需 DDL 变更才能扩展);
- **5 语 jsonb 必填集**:`zh / en / vi / th / id`(`?& array['zh','en','vi','th','id']`);
- **3 套编码序列**:
  - lesson code = `<track>-<stage>-<chapter>-<lesson>`(前端拼,RPC 二次校验);
  - kp_code = `kp_<track>_<type>_<6 位>`(35 个 sequence,触发器生成);
  - q_code = `q_<track>_<8 位>`(5 个 sequence,触发器生成);
- **软删 30 天**:KP / Question / Lesson / Chapter / Exam 走 `deleted_at` 软删,cron 每天 00:30 物理清理;
- **流水分区**:`course_user_answers` 按 `answered_at` 月分区(`pg_partman`);
- **RLS 双层**:
  - 学员只能读 `is_published=true AND deleted_at IS NULL` 且祖先链全发布;
  - 学员对 `user_*` 表自读自写,基于 `auth.uid()`;
  - 管理端写入走 `service_role` 绕过 RLS,依赖应用层 `admins.tracks_scope` 过滤;
- **乐观锁**:KP / Question / Lesson / Exam 编辑通过 `If-Match: updated_at` 校验;不一致返 `COURSE_STALE_VERSION`;
- **物化视图**:`mv_course_user_daily`(5 分钟刷)/ `mv_course_track_stats`(10 分钟刷),CONCURRENTLY 刷新避免锁。
