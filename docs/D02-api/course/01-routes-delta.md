<!-- TARGET-PATH: docs/D02-api/course/01-routes-delta.md -->

# 01 · 路由增量 · course

> 与 [discover-china D02](../discover-china/01-routes-delta.md) 同构,本期新增 `course` 子域。

## 新增 prefix

| Prefix | 部署 app | 用途 |
|--------|---------|------|
| `/api/v1/course/*` | `apps/api-app` | C 端 19 个 endpoint |
| `/admin/v1/course/*` | `apps/api-admin` | 24 个管理端 endpoint |
| `/internal/v1/course/*` | `apps/api-app` 内部子路由 | 3 个 cron / 健康 endpoint |

## 路由文件落点

| 路径 | 实现位置 |
|------|---------|
| `/api/v1/course/tracks` | `apps/api-app/src/routes/course/tracks.ts` |
| `/api/v1/course/me/*` | `apps/api-app/src/routes/course/me.ts` |
| `/api/v1/course/lessons/*` | `apps/api-app/src/routes/course/lessons.ts` |
| `/api/v1/course/kps/*` | `apps/api-app/src/routes/course/kps.ts` |
| `/api/v1/course/answers` | `apps/api-app/src/routes/course/answers.ts` |
| `/api/v1/course/srs/*` | `apps/api-app/src/routes/course/srs.ts` |
| `/api/v1/course/exams/*` / `/exam-attempts/*` | `apps/api-app/src/routes/course/exams.ts` |
| `/api/v1/course/questions/*:report` | `apps/api-app/src/routes/course/reports.ts` |
| `/admin/v1/course/{tracks,stages,chapters,lessons}` | `apps/api-admin/src/routes/course/catalog.ts` |
| `/admin/v1/course/{kps,questions}` | `apps/api-admin/src/routes/course/kp-question.ts` |
| `/admin/v1/course/import-batches` | `apps/api-admin/src/routes/course/import.ts` |
| `/admin/v1/course/*:publish|*:unpublish` | `apps/api-admin/src/routes/course/publish.ts` |
| `/admin/v1/course/{reports,action-log}` | `apps/api-admin/src/routes/course/audit.ts` |
| `/admin/v1/course/{media,exams,search,stats}` | `apps/api-admin/src/routes/course/ops.ts` |
| `/internal/v1/course/*` | `apps/api-app/src/routes/internal/course.ts` |

## 命名约定

- 资源复数:`/lessons`、`/kps`、`/questions`、`/exams`;
- 动作用冒号后缀(非 RESTful 标准但项目统一):
  - `POST /lessons/:id/quiz:submit`、`POST /exams/:id:start`、`POST /:id:publish`、`POST /:id:abandon` 等;
- 子资源浅层:`/exam-attempts/:attempt_id`、`/me/wrong-questions`、`/me/stats`;
- 内部:`/internal/v1/course/exam-attempts:expire`、`/media:purge-pending`、`/health`。
