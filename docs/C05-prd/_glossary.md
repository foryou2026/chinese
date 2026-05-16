<!-- TARGET-PATH: docs/C05-prd/_glossary.md -->

# C05 PRD · 全局术语表

> 项目层共享术语。feature 局部术语写入各 `<feature>/02-glossary.md` 与各 surface PRD,不重复在此。

## A. 平台 / 架构

| 术语 | 定义 |
|------|------|
| **surface(端)** | 部署独立的前端 + 后端组合,本项目两端:`app`(`apps/web-app` + `apps/api-app`)、`admin`(`apps/web-admin` + `apps/api-admin`) |
| **feature** | C 阶段产出的最小业务单元;一个 feature 可横跨多 surface |
| **多端单 feature** | 同一 feature 同时在多个 surface 出产物;目录形如 `<feature>/{baseline.md,_shared/,app/,admin/}`(A00-04 §四.5);`course`、`discover-china`、`auth` 均属此类 |
| **monorepo** | `pnpm-workspace.yaml` 管理的 `system/{apps,packages,scripts,supabase}` 结构 |
| **Supabase 自托管** | 通过 `system/docker/compose.yaml` 拉起 PG16 + GoTrue + Realtime + Storage + PostgREST |

## B. 角色（↑ [B02-permissions/01-roles.md](../B02-permissions/01-roles.md)）

| 角色 | 端 | 说明 |
|------|---|------|
| `super_admin` | admin | 全站唯一管理员角色，全权 |
| `user` | app | 学员 / 终端用户，注册即获 |

> 仅此 2 角色，全系硬约束。不存在 `readonly` / `content_admin` / `super` 等子角色。匿名访问者由路由层处理（重定向到登录），不视为角色。

## C. 标识符约定

| 前缀 | 含义 | 示例 |
|------|------|------|
| `R-` | 业务规则编号 | `R-013` |
| `M-` | 功能模块编号 | `M-course-learning` |
| `P-` | 页面编号 | `P-app-course-001` |
| `SM-` | 状态机编号 | `SM-course-publish` |
| `D-` | 弹窗 / 浮层编号 | `D-14`(答题反馈) |
| `F-` | 流程编号(C02 内) | `F-app-course-1` |

## D. 5 语字段

- 固定 5 key:`{zh, en, vi, th, id}`;写入必须全 key 齐;读取始终返完整 5 key,客户端按 UI 语种选取。

## E. 路由前缀(项目级约定)

- C 端:`/api/app/v1/*`(规范) ≡ `/api/v1/*`(短路径别名)
- 后台:`/api/admin/v1/*`(规范) ≡ `/admin/v1/*`(短路径别名)
- 内部:`/internal/v1/*`(走 `X-Internal-Token`,不出公网)

## F. 主要业务术语

| 术语 | 定义 | 来源 |
|------|------|------|
| **轨道(track)** | course 顶层学习路径 | 〔历史素材〕 |
| **阶段(stage) / 章节(chapter) / 节(lesson)** | 轨道下的 3 层骨架 | 同上 |
| **KP(知识点)** | 与"节"多对多关联的最小知识单元 | 〔历史素材〕 |
| **SRS** | 间隔重复(Spaced Repetition System);本项目用简化 SM-2 | 同上 |
| **句子(sentence)** | discover-china 文章的最小播放单元;每句独立 TTS 缓存 | 〔历史素材〕 |
| **分类树(category)** | discover-china 文章分类,最多 3 层 | 同上 |
