# 技术栈

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：无
> **冻结状态**：未冻结

---

| 层级 | 选型 | 版本 | 理由 |
|------|------|------|------|
| 前端框架 | React + TypeScript | React 19, TS 5.7+ | 用户指定 |
| UI 组件库 | shadcn/ui | latest | 用户指定 |
| CSS 方案 | Tailwind CSS | v4 | 用户指定 |
| 状态管理 | Zustand | 5.x | AI 推荐：轻量零样板、TS 原生 |
| 路由 | TanStack Router | 1.x | 类型安全路由、文件路由 |
| HTTP 客户端 | ky | 1.x | AI 推荐：轻量、TS 友好 |
| 构建工具 | Vite | 6.x | 用户指定 |
| 后端语言 | TypeScript | 5.7+ | 用户指定 |
| 后端框架 | Hono | 4.x | AI 推荐：轻量极速、TS 类型安全 |
| 数据库 | PostgreSQL | 15+ | 用户指定 |
| 数据库托管 | Supabase（本地化） | 自托管 | 用户指定，MCP 可连接 |
| 数据访问 | Drizzle ORM | 0.38+ | AI 推荐：零运行时、TS 类型映射 |
| 缓存 | Redis | 7.x | 用户指定 |
| 任务队列 | BullMQ | 5.x | AI 推荐：Redis 原生、成熟稳定 |
| 文件存储 | Supabase Storage | 自托管 | 复用 Supabase 基础设施 |
| 鉴权 | Supabase Auth | 自托管 | 用户指定，详见 09-auth-infra |
| AI/LLM | 火山引擎接口 | — | 用户自行接入 |
| AI 工作流 | LangGraph(TS) / Vercel AI SDK | — | 用户指定，复杂/简单分治 |
| 测试 | Vitest | 3.x | AI 推荐：Vite 原生、极速 |
| 包管理器 | npm | 10+ | 用户指定 |
| Node 版本 | Node.js | 22 LTS | 当前 LTS，原生 TS 支持 |

---

## 99. 待确认问题

无
