<!-- TARGET-PATH: docs/B01-architecture/02-project-structure.md -->

# 02 · 项目目录结构

> **阶段**：B01-A 架构  
> **角色**：架构师  
> **feature**：全局  
> **上游依赖**：`01-tech-stack.md`、`_input/preferences.md`  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：所有 D 阶段、`docker/compose.yaml`、`pnpm-workspace.yaml`

---

## 0. 摘要

- **代码根硬约束**：所有可运行 / 可构建代码位于 `/opt/projects/zhiyu/system/`；顶层 `/opt/projects/zhiyu/` 只放文档与素材（`docs/`、`prompt/`、`env.md`）。
- monorepo 用 **pnpm workspaces**。
- 4 个应用：`web-app` / `web-admin` / `api-app` / `api-admin`。
- 7 个共享包：`shared-schemas` / `shared-config` / `shared-utils` / `shared-i18n` / `ui-kit` / `supabase-client` / `ai-adapters`。

---

## 1. 顶层布局

```
/opt/projects/zhiyu/
├── docs/                       ← 本框架所有 AI 产出物（B/C/D 阶段）
├── prompt/                     ← /prompt 框架模板（A/B/C/D 四子目录）
├── env.md                      ← 凭证 / 端口 / 基础设施现状
│
└── system/                     ← ★ 唯一开发根（pnpm workspace 根）
    ├── apps/                   ← 可独立部署的应用
    │   ├── web-app/            ← 应用端前端（C 端，3100，CSR/SPA）
    │   ├── web-admin/          ← 管理后台前端（4100，CSR/SPA）
    │   ├── api-app/            ← 应用端后端（Hono，8100）
    │   └── api-admin/          ← 管理后台后端（Hono，9100）
    │
    ├── supabase/               ← 自托管 Supabase 工程
    │   ├── config.toml
    │   ├── migrations/         ← SQL 迁移
    │   ├── seed.sql            ← 初始化数据
    │   ├── tests/rls/          ← pgTAP / 自定义 RLS 测试
    │   └── functions/          ← Edge Functions（Deno + TS）
    │       ├── _shared/
    │       ├── auth-signup/
    │       ├── auth-google/
    │       ├── webhook-paddle/
    │       └── health/
    │
    ├── packages/               ← 跨应用共享代码（全部 TS）
    │   ├── shared-schemas/     ← Zod schema → z.infer 类型
    │   ├── shared-config/      ← 常量 / 错误码 / 枚举
    │   ├── shared-utils/       ← 纯函数工具
    │   ├── shared-i18n/        ← 5 语言文案（zh/en/vi/th/id）
    │   ├── ui-kit/             ← 基于 shadcn/ui 的项目级组件 + 毛玻璃主题
    │   ├── supabase-client/    ← 封装 supabase-js（browser/server/admin）+ MCP
    │   └── ai-adapters/        ← LLM / Workflow / TTS / ASR 适配器 + mock fixture
    │
    ├── docker/                 ← Docker 配置（唯一 dev 环境）
    │   ├── compose.yaml
    │   ├── Dockerfile.web
    │   ├── Dockerfile.api
    │   ├── postgres/           ← 占位：DB 复用主机 supabase-db
    │   ├── redis/redis.conf
    │   ├── nginx/              ← 仅生产参考样例（dev 不用）
    │   └── env/
    │       ├── .env.example    ← 全部变量模板（必交付）
    │       └── README.md       ← Key 来源 / 申请方式
    │
    ├── scripts/                ← 一次性脚本，全 TS（tsx 执行）
    │   ├── db/                 ← dump.sh / restore.sh / 数据回填
    │   ├── dev/                ← free-ports.sh 等
    │   └── e2e/                ← Playwright 容器内脚本
    │
    ├── pnpm-workspace.yaml
    ├── package.json
    ├── tsconfig.base.json
    ├── .editorconfig
    ├── .gitignore
    └── README.md
```

**注意**：
- 所有 `pnpm` / `docker compose` / `supabase` 命令 cwd 都是 `system/`。
- 顶层只放文档/素材，便于 Docker 构建上下文裁剪与 `.dockerignore` 过滤。
- 仓库**不存在**：Drizzle、`packages/db`、`.mjs` 后缀。

---

## 2. `system/apps/web-app`（应用端，C 端，CSR/SPA）

```
system/apps/web-app/
├── src/
│   ├── main.tsx                ← 唯一入口；禁止注入业务数据
│   ├── app/                    ← provider、错误边界、根布局
│   ├── routes/                 ← TanStack Router 文件路由
│   │   ├── _public/            ← 未登录可见（落地页、营销）
│   │   ├── _auth/              ← 登录后
│   │   └── games/              ← 游戏专区
│   ├── features/               ← 按 feature 与 PRD 对齐
│   │   ├── discover-china/
│   │   ├── course/
│   │   ├── games/
│   │   ├── user-account/
│   │   ├── economy/
│   │   ├── referral/
│   │   ├── payment/
│   │   ├── customer-service/
│   │   └── i18n/
│   ├── components/             ← 跨 feature 展示组件
│   ├── hooks/
│   ├── lib/                    ← supabase client、http、analytics
│   ├── styles/
│   └── assets/
├── public/
├── index.html                  ← 仅空壳
├── vite.config.ts
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

**feature 内部统一三层**：`api/`（请求 hooks）+ `ui/`（组件）+ `model/`（store / derive）。

**反爬虫强制**：`index.html` 禁止 `<script>window.__*` 数据注入；列表 / 详情数据必须客户端运行时拉取。

---

## 3. `system/apps/web-admin`（管理后台前端）

结构同 `web-app`，差异：
- `routes/` 全在 `_admin/` 守卫下；
- `features/` 与 admin PRD 模块一一对齐（discover-china、course、user-mgmt、order-mgmt、content-review、…）；
- 引入 `TanStack Table` + `Tiptap` + `Recharts`；
- 不引入 `framer-motion`（保持轻量）。

---

## 4. `system/apps/api-app`（应用端后端，Hono）

```
system/apps/api-app/
├── src/
│   ├── server.ts               ← 入口
│   ├── app.ts                  ← Hono 实例 + 中间件装配
│   ├── env.ts                  ← Zod 校验环境变量
│   ├── routes/                 ← Hono sub-app
│   │   ├── index.ts
│   │   ├── discover-china.routes.ts
│   │   ├── course.routes.ts
│   │   └── ...
│   ├── handlers/               ← 解析 c.req → service → c.json
│   ├── services/               ← 业务逻辑，纯函数优先
│   ├── repositories/           ← supabase-js 调用封装（service-role）
│   ├── adapters/               ← 外部 / AI 调用入口
│   ├── middlewares/            ← auth / rateLimit / i18n / errorHandler / requestId
│   ├── jobs/                   ← BullMQ 队列与 worker
│   ├── crons/                  ← node-cron
│   ├── ws/                     ← Realtime 桥接（如有）
│   ├── errors/                 ← AppError 与业务错误类
│   └── utils/
├── tests/                      ← Vitest + app.request()
├── package.json
└── tsconfig.json
```

---

## 5. `system/apps/api-admin`（管理后台后端，Hono）

结构同 `api-app`，差异：
- `middlewares/rbac.ts` 强制 `admin` 角色校验；
- 不暴露 C 端业务接口，仅审核 / 配置 / 统计。

---

## 6. `system/supabase/`

```
system/supabase/
├── config.toml
├── migrations/                 ← SQL 迁移
│   └── YYYYMMDD_HHMMSS_<verb>_<object>.sql
├── seed.sql                    ← 字典 / 初始管理员 / 演示数据
├── tests/rls/                  ← RLS 正反例（pgTAP / 自定义）
└── functions/                  ← Edge Functions
    ├── _shared/                ← 由 scripts/sync-shared-to-edge.ts 从 packages/shared-schemas 同步
    ├── auth-signup/index.ts
    ├── auth-google/index.ts
    ├── webhook-paddle/index.ts
    └── health/index.ts
```

**Schema 与迁移规则**：
- 新建表/字段 → `pnpm supabase migration new <name>` → 写 SQL → `pnpm supabase db reset`（dev）→ 提交；
- **禁止**手改已合入迁移，变更只能新增；
- 复杂查询封装为 SQL 函数（RPC），由 `supabase.rpc('fn_name', args)` 调用。

---

## 7. `system/packages/supabase-client`（统一封装）

```
src/
├── browser.ts                  ← 浏览器侧匿名 client（前端用）
├── server.ts                   ← 服务端 service-role client（后端用）
├── admin.ts                    ← 后台管理操作（auth.admin.*）
├── mcp.ts                      ← Supabase MCP 执行 schema 查询 / 调试
├── helpers/
│   ├── jsonb.ts                ← jsonb 写入 / 读取助手（详见 03-database §9）
│   ├── soft-delete.ts
│   └── pagination.ts
└── types/
    └── database.ts             ← supabase gen types 自动生成
```

---

## 8. `system/packages/ai-adapters`

```
src/
├── llm/
│   ├── index.ts                ← createLLMAdapter()
│   ├── claude.ts
│   ├── deepseek.ts
│   └── mock.ts                 ← 缺 Key 时使用
├── workflow/
│   ├── langgraph.ts            ← LangGraph TS（beta）
│   ├── vercel-ai.ts            ← Vercel AI SDK
│   └── mock.ts
├── tts/                        ← mock + 真实
├── asr/
├── embedding/
└── factory.ts                  ← 根据 env 自动选择实现
```

---

## 9. 命名规则汇总

| 对象 | 规则 | 示例 |
|------|------|------|
| 目录 | kebab-case | `web-admin/`、`shared-schemas/` |
| TS 普通文件 | kebab-case | `course-list.handler.ts` |
| React 组件文件 | PascalCase | `CourseCard.tsx` |
| Hook 文件 | camelCase + `use` 前缀 | `useCourseProgress.ts` |
| Zustand store | camelCase + `.store.ts` | `gameSession.store.ts` |
| 测试文件 | `*.test.ts(x)` | `course-list.handler.test.ts` |
| Edge Function 目录 | kebab-case，与路径同名 | `supabase/functions/webhook-paddle/` |
| SQL 迁移 | `YYYYMMDD_HHMMSS_<verb>_<object>.sql` | `20260428_120000_add_user_referral_code.sql` |

---

## 10. 禁止事项

1. 跨 app 直接 import：必须通过 `packages/*`。
2. 绕过 `packages/supabase-client` 直接 `createClient`：禁止。
3. 绕过 adapter 直接 fetch 第三方 LLM：禁止。
4. 新增 ORM（Drizzle/Prisma/Kysely 等）：禁止。
5. `.js` / `.mjs` 写源码：禁止；脚本用 `tsx` 执行 `.ts`。
6. 新增顶层目录：除非更新本规范，否则一律拒绝。
7. 前端 SSR / SSG / 业务数据预渲染：禁止（反爬虫）。

---

## 99. 待确认问题
（无）
