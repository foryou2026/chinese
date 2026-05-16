<!-- TARGET-PATH: docs/A00-meta/questions/A-questions-round1-resolved.md -->

# B01 · A 架构 澄清提问 · 第 1 轮（已解）

> 本轮共 12 个问题（10 阻断 + 2 优化）。
> **本文件是反向工程产物**：既有 `grules/G1-架构与技术规范/` 与 `system/` 工程结构 = PM 实际决策结果。AI 据此倒推「当时本应提的问题 + PM 的回答」，让后续每一处架构定调都可追溯到一次显式拍板。

---

## A. 阻断级（必答）

### Q1. 项目运行环境是否锁定 Docker？是否禁止任何裸机/SaaS 托管业务服务？
- **背景**：影响后续部署/CI/测试策略与第三方依赖选型。
- **可选项**：A. Docker-only · B. Docker + 裸机混合 · C. 云托管（Vercel/Supabase Cloud）
- **推荐**：A
- **理由**：用户硬性要求 — 自动化测试要在容器内完成、Supabase 必须自托管。
- **影响范围**：`06-deploy-env.md`、`docker/compose.yaml`、CI 设计
- **答**：A。所有 dev/test 都在 Docker；生产由用户自行处理 Nginx + HTTPS。**不接 supabase.com 云服务**。

### Q2. 全栈语言是否锁定 TypeScript strict？是否禁止 `.js` / `.mjs` / JSDoc 替代？
- **背景**：影响"是否引入 JSDoc 折中方案"与代码可维护性基线。
- **可选项**：A. TS strict 全栈，禁止 `.js/.mjs/JSDoc` · B. TS + JSDoc 折中 · C. 后端 JS、前端 TS
- **推荐**：A
- **影响范围**：`01-tech-stack.md`、`05-coding-standards.md`、`tsconfig.base.json`
- **答**：A。脚本也走 `tsx` 执行 `.ts`，不允许 `.mjs`。

### Q3. 前端是否强制纯 CSR/SPA？是否禁止 SSR/SSG/数据预注入？
- **背景**：用户提出"反爬虫"硬性要求，业务数据不能出现在初始 HTML。
- **可选项**：A. 纯 CSR · B. Hybrid（部分页面 SSR）· C. 全 SSR（Next.js/Remix）
- **推荐**：A
- **影响范围**：`01-tech-stack.md §二`、`05-coding-standards.md §二`、所有 web-* 应用
- **答**：A。`index.html` 仅空壳；路由 loader 必须运行时 `fetch`；禁止 `<script>window.__INITIAL_STATE__=...` 等业务数据注入。

### Q4. 数据访问层是否禁止所有 ORM（Drizzle/Prisma/Kysely），统一走 `supabase-js` + RPC？
- **背景**：影响事务模型与 schema 管理工具链。
- **可选项**：A. 仅 supabase-js + Postgres RPC · B. Drizzle + supabase-js 混合 · C. Prisma 主导
- **推荐**：A
- **影响范围**：`03-database.md`、`05-coding-standards.md §三.8`、`packages/supabase-client/`
- **答**：A。schema 迁移走 Supabase CLI 的纯 SQL；复杂事务以 RPC 函数封装。**历史的 drizzle-jsonb 坑作废**（本项目不再使用 Drizzle）。

### Q5. 多端 surface 的清单与端口？是否需要 merchant / open 等额外端？
- **背景**：surface 数决定 C/D 阶段目录是否启用 `<surface>/` 变体。
- **可选项**：A. 仅 `app` + `admin`（2 端）· B. + `merchant` · C. + `open`（开放平台）
- **推荐**：A
- **影响范围**：`08-surfaces.md`、全部 C/D 阶段目录结构
- **答**：A。当前仅 `app` + `admin`，端口固定 fe=3100/4100，be=8100/9100；未来若加 merchant 再追加。

### Q6. 后端框架与运行时？业务 API 与鉴权/回调是否分层？
- **背景**：影响 monorepo 应用切分与 Edge Functions 使用范围。
- **可选项**：A. Hono 容器（业务 API）+ Supabase Edge Functions（鉴权/回调/轻量编排）· B. NestJS 单体 · C. 纯 Edge Functions
- **推荐**：A
- **影响范围**：`01-tech-stack.md §三/§四`、`02-project-structure.md §四/§六`、`09-auth-infra.md`
- **答**：A。Hono + `@hono/node-server` 跑 Node 容器；Auth/OAuth 回调/Paddle webhook 走 Edge Functions。

### Q7. AI 工作流如何拆？是否接受 LangGraph (beta)？
- **背景**：影响 `packages/ai-adapters/workflow/` 的实现路径。
- **可选项**：A. LangGraph TS (beta) + Vercel AI SDK 二分 · B. 自研编排 · C. 仅 Vercel AI SDK
- **推荐**：A
- **影响范围**：`01-tech-stack.md §六`
- **答**：A。复杂状态机/多智能体 → LangGraph；单次 prompt / 流式 → Vercel AI SDK。

### Q8. pgvector 默认是否启用？非 AI 业务能否使用 vector 类型？
- **背景**：影响 DB 初始扩展清单与字段类型政策。
- **可选项**：A. 默认不启用，仅 AI 向量场景按需 `create extension` · B. 默认启用 · C. 禁用
- **推荐**：A
- **影响范围**：`01-tech-stack.md §五`、`03-database.md §四`
- **答**：A。非 AI 业务严禁使用 vector；用前在该次迁移内显式 `create extension if not exists vector`。

### Q9. 第三方付费 API 缺 Key 的行为？是否影响 dev 启动？
- **背景**：本期 Paddle / Google OAuth / Anthropic / DeepSeek 多个 Key 未发。
- **可选项**：A. 全部 Adapter + mock fallback，dev 永不阻塞 · B. 缺 Key 启动失败 · C. 缺 Key 接口返 503
- **推荐**：A
- **影响范围**：`01-tech-stack.md §七`、`06-deploy-env.md §三.3`、`packages/ai-adapters/`
- **答**：A。`/health` 中 `adapters` 字段标注当前是 `real` 还是 `mock`，便于排查。

### Q10. 字体托管策略？是否允许 Google Fonts CDN？
- **背景**：用户硬性要求"Supabase 本地化"——字体也不外链 CDN。
- **可选项**：A. 自托管 `woff2`，预载关键字重 · B. Google Fonts CDN · C. CDN + 本地兜底
- **推荐**：A
- **影响范围**：`07-i18n-responsive.md §七`、`apps/web-*/public/fonts/`
- **答**：A。zh→Noto Sans/Serif SC、en→Inter、vi→Be Vietnam Pro、th→Noto Sans Thai Looped、id→Inter。

---

## B. 优化级（可不答，AI 走推荐）

### Q11. 端口冲突自动释放是否接受 `kill` 占用进程？
- **推荐**：A. 自动 `kill`（dev/CI 默认）
- **答**：A。`scripts/dev/free-ports.sh` 在 compose up 前执行。

### Q12. 单文件代码上限？
- **推荐**：1200 行硬上限，超出立即拆分
- **答**：采纳推荐。

---

## C. AI 主动声明（不可逆解读）

- D1. 「发现中国」与「课程」两个 feature 视为多端 feature（同时在 `app` 与 `admin` 出现），其 C/D 阶段按多端形态铺目录。
- D2. 鉴权基础设施落 `09-auth-infra.md`；具体登录/注册页与流程落在未来的 `app-auth` / `admin-auth` feature，不在 B 阶段输出。
- D3. dev 端口 fe=3100/4100 / be=8100/9100 与 `env.md` 中 ideas/foryou 项目占的 3100/3200/3300/3400 + 8100/8200/8300/8400 区段不冲突（按 4100/9100 错峰）。本项目 dev 共占用 3100、4100、8100、9100、6379 五个对外端口。
