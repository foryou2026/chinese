<!-- TARGET-PATH: docs/B01-architecture/01-tech-stack.md -->

# 01 · 技术栈

> **阶段**：B01-A 架构  
> **角色**：架构师  
> **功能**：全局  
> **上游依赖**：`_input/preferences.md`、`A-questions-round1-resolved.md`  
> **冻结状态**：已冻结 · 2026-04-28 · 签字: PM  

---

## 0. 摘要

- 全栈 TS strict；后端 = Hono 容器 + Supabase Edge Functions；前端 = React 19 + Vite 6 纯 CSR/SPA。
- 数据访问统一 `@supabase/supabase-js` + Postgres RPC，**禁止 ORM**。
- AI 工作流二分：复杂状态机 → LangGraph(TS, beta)；单次 prompt / 流式 → Vercel AI SDK。
- pgvector 默认**不启用**，仅 AI 向量检索按需 `create extension`；非 AI 业务严禁使用 vector 列。
- 第三方 / AI 缺 Key 走 mock fallback，dev 永不阻塞。

---

## 1. 整体原则

1. 全栈 TypeScript strict（前端 + 后端 + 共享包 + 脚本 + Edge Functions），**禁止 `.js` / `.mjs` / JSDoc**。
2. Docker-only：依赖 / 构建 / 测试 / 运行均在容器内。
3. Supabase 自托管（复用主机 `supabase_default` 网络），**不使用 supabase.com 云服务**。
4. 数据访问统一 supabase-js + Supabase MCP；schema/迁移由 Supabase CLI 管理。
5. 前端纯 CSR / SPA；**禁止 SSR / SSG / 数据预注入**（反爬虫硬性要求）。
6. 缺 Key 不阻塞：第三方走 Adapter，缺 Key 自动 fallback 到 mock。
7. AI 工作流二分：复杂 → LangGraph；简单/流式 → Vercel AI SDK。

---

## 2. 前端栈（`app` / `admin` 共用核心）

| 层 | 选型 | 版本 | 备注 |
|----|------|------|------|
| 框架 | React | 19.x | 并发渲染 |
| 语言 | TypeScript | 5.x strict | — |
| 渲染 | **纯 CSR / SPA** | — | 反爬虫硬约束 |
| 构建 | Vite | 6.x | HMR 快、对 Docker 卷友好 |
| 路由 | TanStack Router | 1.x | 类型安全 |
| HTTP / 数据 | TanStack Query + Supabase JS SDK | 5.x / 2.x | 缓存 + 直连 Supabase |
| 状态 | Zustand | 5.x | 轻量；复杂场景再扩 |
| 表单 | React Hook Form + Zod | 7.x / 3.x | 与后端共享 schema |
| CSS | Tailwind CSS | 4.x | 与 shadcn/ui 原生兼容 |
| UI 组件 | shadcn/ui（Radix 原语）| latest | 可复制源码，可裁剪 |
| 图标 | lucide-react | latest | — |
| 动效 | Framer Motion | 11.x | 游戏页与转场 |
| i18n | i18next + react-i18next | 23.x / 14.x | 5 语言 |
| 游戏引擎（仅 app） | PixiJS + Matter.js + Howler.js | 8.x / 0.20.x / 2.x | 2D 渲染 + 物理 + 音频 |
| 图表（仅 admin）| Recharts | 2.x | 报表 |
| 表格（仅 admin）| TanStack Table | 8.x | 虚拟滚动 |
| 富文本（仅 admin）| Tiptap | 2.x | 课程/文章编辑 |
| 日期 | date-fns | 3.x | tree-shake 友好 |
| 测试 | Vitest + RTL | latest | 容器内执行 |

**反爬虫细则**：
- `index.html` 禁止 `<script>window.__INITIAL_STATE__=...` 等业务数据脚本注入；
- 路由 loader 必须运行时 `fetch`，不可在打包阶段读 DB / 文件系统业务数据；
- 静态营销文案走 i18n 文件（属品牌内容）；
- 用户 / 课程 / 订单 / 小说 / 文章等业务数据严禁出现在初始 HTML。

---

## 3. 后端栈（`api-app` / `api-admin` 共用核心）

| 层 | 选型 | 版本 | 备注 |
|----|------|------|------|
| 运行时 | Node.js | 20 LTS（`node:20-alpine`）| — |
| 语言 | TypeScript strict | 5.x | — |
| Web 框架 | **Hono** | 4.x | 类型一流，与 Edge 同构 |
| Node 适配 | `@hono/node-server` | latest | 容器内 HTTP |
| 入参 / 出参 | Zod + `@hono/zod-validator` | 3.x | 与前端表单共用 |
| 数据访问 | `@supabase/supabase-js` (service-role) | 2.x | 不引 ORM |
| 复杂查询 | Postgres RPC（SQL 函数 / 视图）| — | Supabase MCP 管理 |
| 队列 | BullMQ | 5.x | 复用 Redis |
| 调度 | node-cron | 3.x | 周期任务 |
| 日志 | pino + `hono-pino` | 9.x | 结构化 JSON |
| 实时 | Supabase Realtime | — | 通知 / IM |
| 文件存储 | Supabase Storage SDK | latest | — |
| 测试 | Vitest + Hono `app.request()` | latest | 端到端 |

---

## 4. Edge Functions（鉴权 / 回调 / 轻量编排）

> Hono 容器与 Edge Functions **职责互补，不重叠**。

| 用途 | 落地 | 说明 |
|------|------|------|
| 用户鉴权（注册/登录/OAuth/找回密码）| Edge Functions | 与 Supabase Auth 同进程；Google + 邮箱本期均 mock |
| 第三方回调（Paddle webhook、Google OAuth callback）| Edge Functions | 边缘转发后落 BullMQ；缺 Key 走 mock 验签 |
| 轻量、无状态、低 QPS 接口（健康、版本、配置）| Edge Functions | — |
| 业务 API（课程、文章、KP、SRS、考试、IM 等）| **Hono 容器** | 需要队列、长连接、复杂事务 |
| AI 工作流编排（LangGraph）| Hono 容器 + BullMQ worker | Edge 不适合长任务 |

> Edge 与 Hono 通过 `packages/shared-schemas` 共享 Zod 与错误码。

---

## 5. 数据 / 认证 / 存储（统一自托管 Supabase）

| 用途 | 技术 | 备注 |
|------|------|------|
| 关系型主库 | Supabase Postgres 16 | schema `zhiyu`（dev/prod 同名，按实例隔离）|
| 用户认证 | Supabase Auth (GoTrue) | 邮箱 + Google OAuth（本期均 mock）|
| 后台认证 | 复用 Auth + RBAC 表 | `admin` 角色 |
| 文件存储 | Supabase Storage | bucket：`avatars` / `course-media` / `user-upload` / `system` |
| 向量检索 | pgvector（**默认不启用**，AI 场景按需 `create extension`）| 非 AI 业务严禁 vector 列 |
| 全文检索 | Postgres FTS | v1 用 zh/vi/th/id 简化分词 |
| 实时推送 | Supabase Realtime | 通知 / IM |
| 缓存 / 队列 | Redis 7 | 复用 Docker；BullMQ + 短期缓存 |
| Edge Functions | Supabase Edge Functions（Deno）| 见 §4 |
| Schema 管理 | **Supabase CLI + MCP** | 不使用任何 ORM |

> **不引入**：Pinecone、Upstash、Meilisearch、Cloudflare KV、Drizzle、Prisma、Kysely、TypeORM。

---

## 6. AI 工作流

| 用途 | 选型 | 备注 |
|------|------|------|
| 复杂工作流编排 | **LangGraph (TS, beta)** | 封装在 `packages/ai-adapters/workflow/` |
| 简单 LLM 调用 / 流式 | **Vercel AI SDK** | 纯 prompt → 单次/流式 |
| 向量数据库 | Supabase pgvector | 仅 AI 向量场景按需启用 |
| Adapter 层 | `LLMAdapter` / `WorkflowAdapter` / `EmbeddingAdapter` / `TTSAdapter` / `ASRAdapter` | 缺 Key 自动 fallback 到 fixture |
| 主创作模型 | Anthropic Claude Sonnet（待 Key）| 缺 → mock |
| 副创作模型 | DeepSeek V3（待 Key）| 缺 → mock |
| 评估 | LangSmith（可选）| v1 不强制 |

> **禁用**：Dify、NocoBase、OpenClaw。

---

## 7. 支付与第三方

| 类目 | 选型 | 本期实现 | 未来 |
|------|------|---------|------|
| 支付 | Paddle | **全量 mock**（沙箱也不接）| Paddle Billing v1，Hono + Edge webhook |
| 邮件 | Adapter | console + 落 `outbox` 表 | Resend / SES |
| 短信 | Adapter | console | 按地区接本地服务商 |
| 第三方登录 | Google OAuth | **mock**（生成假用户）| 真接入 |
| 对象存储备份 | 暂不实现 | — | S3 兼容 |

---

## 8. 部署与基础设施

| 项目 | 选型 | 备注 |
|------|------|------|
| 容器化 | Docker + Compose | 唯一 dev 环境 |
| 镜像基础 | `node:20-alpine` / Supabase 全套官方镜像 | — |
| dev 反向代理 | **不使用**，直接 `IP:端口` 访问 | — |
| 生产反向代理 | Nginx（用户自行接 HTTPS）| 不在本仓库交付 |
| CI | 仅 Docker compose，**不集成 GitHub Actions** | user memory `zhiyu-docker-policy.md` |

详见 [06-deploy-env.md](./06-deploy-env.md)。

---

## 9. 版本锁定与升级

1. 依赖在 `package.json` 中**精确版本**（不写 `^` / `~`），由 `pnpm-lock.yaml` 锁定。
2. 主版本升级须在 PR 描述列出 breaking change，经 PM 单点放行。
3. 每月一次安全补丁批量升级，CI 跑全量测试通过后合入。
4. LangGraph 处于 beta，每次升级前在 `packages/ai-adapters/workflow/__bench__/` 跑回归用例。

---

## 99. 待确认问题
（无）
