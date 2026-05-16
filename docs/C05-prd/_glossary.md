<!-- TARGET-PATH: docs/C05-prd/_glossary.md -->

# C05 PRD · 全局术语表

> 项目层共享术语。feature 局部术语写入各 `<feature>/02-glossary.md` 与各 surface PRD,不重复在此。

## A. 平台 / 架构

| 术语 | 定义 |
|------|------|
| **surface(端)** | 部署独立的前端 + 后端组合,本项目两端:`app`(`apps/web-app` + `apps/api-app`)、`admin`(`apps/web-admin` + `apps/api-admin`) |
| **feature** | C 阶段产出的最小业务单元;一个 feature 可横跨多 surface;auth 退化为单 surface |
| **退化形态** | feature 仅在 1 个 surface 出产物(目录仍按 `<feature>/<surface>/`);`app-auth` 与 `admin-auth` 属此类 |
| **monorepo** | `pnpm-workspace.yaml` 管理的 `system/{apps,packages,scripts,supabase}` 结构 |
| **Supabase 自托管** | 通过 `system/docker/compose.yaml` 拉起 PG16 + GoTrue + Realtime + Storage + PostgREST |

## B. 角色(↑ [G3-角色定义](../../grules/G3-权限与认证规范/01-角色定义.md))

| 角色 | 端 | 说明 |
|------|---|------|
| `anonymous` | app / admin | 未登录访问者 |
| `learner` | app | 注册即获;C 端默认角色 |
| `readonly` | admin | 只读管理员;不可写 |
| `content_admin` | admin | 受 `tracks_scope` / `categories_scope` 限制的内容编辑 |
| `super` | admin | 全权限 + 高危操作(unpublish 30 天+ / 重置密码 / 邀请管理员) |

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
| **轨道(track)** | course 顶层学习路径 | [function/02-course/prd/01-课程目录骨架.md](../../function/02-course/prd/01-课程目录骨架.md) |
| **阶段(stage) / 章节(chapter) / 节(lesson)** | 轨道下的 3 层骨架 | 同上 |
| **KP(知识点)** | 与"节"多对多关联的最小知识单元 | [function/02-course/prd/02-知识点与题型内容模板.md](../../function/02-course/prd/02-知识点与题型内容模板.md) |
| **SRS** | 间隔重复(Spaced Repetition System);本项目用简化 SM-2 | 同上 |
| **句子(sentence)** | discover-china 文章的最小播放单元;每句独立 TTS 缓存 | [function/01-china/prd/F1-用户-数据与业务规则.md](../../function/01-china/prd/F1-用户-数据与业务规则.md) |
| **分类树(category)** | discover-china 文章分类,最多 3 层 | 同上 |
