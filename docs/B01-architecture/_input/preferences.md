<!-- TARGET-PATH: docs/B01-architecture/_input/preferences.md -->

# B01 · A 用户输入 · 技术偏好

> 本文件是反向工程产物：基于 `env.md`、`system/` 既有工程结构、用户口述偏好，重写为 B01-A01 用户输入模板的填表结果。

---

## 1. 项目定位

- **项目名**：知语（Zhiyu）
- **目标用户**：东南亚（越南、泰国、印尼）成年汉语学习者，兼顾英文母语者。
- **核心场景**：
  1. 主线学习：主题 → 阶段 → 章 → 节，逐节学 KP（汉字/词/语法），节末小测，错题进 SRS 复习池，全阶段过关后考试。
  2. 副线内容：「发现中国」频道，按类目浏览中国主题短文，支持句子级 TTS 朗读，沉浸式输入。
  3. 配套：用户账户、积分/钱包、邀请、支付、客服 IM、游戏化激励。
- **运营节奏**：单团队、单仓库、单 dev 环境；2026 Q2 内端到端跑通核心两 feature。

## 2. 技术偏好（硬性）

| 项目 | 偏好 | 备注 |
|------|------|------|
| 语言 | TypeScript strict 全栈 | 禁止 `.js` / `.mjs` / JSDoc |
| 前端框架 | React 19 + Vite 6 + TanStack Router/Query + shadcn/ui + Tailwind 4 | 纯 CSR/SPA，反爬虫 |
| 后端框架 | Hono 4 + `@hono/node-server`，Node 20 LTS | 容器内运行 |
| 数据库 | 自托管 Supabase Postgres 16 + Auth + Storage + Realtime + Edge Functions | 不使用 supabase.com |
| 数据访问 | `@supabase/supabase-js` + Postgres RPC | 禁止 ORM |
| 包管理 | pnpm workspaces | monorepo |
| AI 工作流 | LangGraph TS (beta) + Vercel AI SDK | 接受 beta |
| 部署 | Docker-only；生产由我自己接 Nginx + HTTPS | dev 不挂反向代理 |
| 字体 | 自托管 woff2，不走 Google Fonts CDN | 配合本地化 |

## 3. 已确定的非技术约束

- **多语言**：5 语（zh/en/vi/th/id），AI 自动翻译占位 + 人工校对。
- **第三方登录**：本期 Google + 邮箱，**全部 mock**。
- **支付**：Paddle，本期**全量 mock**（沙箱也不接）。
- **AI Key**：Anthropic / DeepSeek / OpenAI / LangSmith 等缺 Key 一律 mock。
- **反爬虫**：HTML 不得预注入业务数据。
- **端口**：app=3100/8100, admin=4100/9100, redis=6379；占用即强制释放。
- **代码根**：`/opt/projects/zhiyu/system/`；顶层只放文档/素材。

## 4. 不偏好（明确拒绝）

- 任何 ORM（Drizzle/Prisma/Kysely/TypeORM）
- 任何 SSR / SSG 方案（Next.js / Remix / Vite SSR plugin）
- 任何低代码平台（Dify / NocoBase / OpenClaw 已在 `env.md` 标注停用）
- 任何 GitHub Actions / 第三方 SaaS CI（user memory `zhiyu-docker-policy.md`）
- 任何 PG enum 类型（用 `text` + `CHECK` 替代）
- 任何 `.mjs` 文件

## 5. 留给 AI 拍板的点（请在澄清提问中列出）

- 后端分层细则（handler/service/repository 命名约定）
- 错误码段位分配
- 限流默认阈值
- Storage 桶命名
- 测试覆盖率目标
- 日志字段约定

---

> 见 `docs/A00-meta/questions/A-questions-round1-resolved.md` 获取澄清问答全文。
