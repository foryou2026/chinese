# 编码规范

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack, 02-project-structure
> **冻结状态**：✅ 已冻结

---

## 前端

### 文件命名

| 对象 | 规则 | 示例 |
|------|------|------|
| React 组件 | PascalCase.tsx | `UserCard.tsx` |
| Hook | `use` 前缀 camelCase | `useAuth.ts` |
| 工具函数 | camelCase.ts | `formatDate.ts` |
| 类型文件 | kebab-case.ts | `api-types.ts` |
| 样式文件 | 与组件同名 | `UserCard.module.css`（仅特殊情况） |

### 组件规范

| 规则 | 说明 |
|------|------|
| 导出方式 | 具名导出，禁止 `export default`（页面入口除外） |
| Props 类型 | `interface XxxProps`，与组件同文件 |
| 组件粒度 | 单文件 ≤ 300 行，超出则拆分 |
| 状态管理 | 局部状态 `useState`；跨组件 Zustand store |
| 副作用 | `useEffect` 仅用于同步外部系统，禁止作为派生状态 |

### CSS 组织

| 规则 | 说明 |
|------|------|
| 默认方案 | Tailwind CSS class |
| 动态样式 | Tailwind `cn()` 工具合并 |
| 全局样式 | 仅 `globals.css`，定义 CSS 变量和 reset |
| 主题 | CSS 变量 + Tailwind `dark:` 前缀 |

### 类型定义

| 规则 | 说明 |
|------|------|
| API 类型 | 统一定义在 `shared-types` 包 |
| 组件 Props | 与组件同文件 |
| 禁止 `any` | 严格模式，必要时使用 `unknown` + 类型守卫 |
| 禁止 `as` 断言 | 仅在类型系统无法推断时使用，需注释原因 |

## 后端

### 分层架构

```
routes (Controller) → services (业务逻辑) → repositories (数据访问)
```

| 层 | 职责 | 禁止 |
|------|------|------|
| routes | 请求解析、参数校验、调用 service、组装响应 | 直接操作 DB |
| services | 业务逻辑、事务编排、权限判断 | 直接返回 HTTP 响应 |
| repositories | Drizzle 查询、数据映射 | 业务逻辑判断 |

### 错误处理

| 规则 | 说明 |
|------|------|
| 自定义异常类 | `AppError(code, msg, httpStatus)` |
| 全局拦截 | Hono `onError` 中间件统一捕获 |
| 生产环境 | 禁止暴露内部 stack trace |
| 参数校验 | 使用 Zod schema，route 层统一校验 |

### 日志格式与级别

| 级别 | 场景 |
|------|------|
| error | 未预期异常、第三方服务失败 |
| warn | 可恢复异常、限流触发 |
| info | 请求日志、业务关键节点 |
| debug | 仅开发环境，SQL 查询等 |

> 格式：JSON 结构化日志，字段包含 `timestamp`, `level`, `msg`, `requestId`, `userId`。

## 通用

### Lint / Format

AI 推荐：

| 工具 | 版本 | 配置 |
|------|------|------|
| Prettier | 3.x | 单引号、无分号、尾逗号 all、printWidth 120 |
| ESLint | 9.x (flat config) | `@eslint/js` + `typescript-eslint`，严格模式 |

### 测试金字塔

AI 推荐：

| 层级 | 工具 | 覆盖率门槛 | 说明 |
|------|------|-----------|------|
| 单元测试 | Vitest | 核心逻辑 80% | services、utils |
| 集成测试 | Vitest + Supertest | 关键路径 | API 路由 + DB |
| E2E | gstack `/qa` + `/browse` | 主流程 | Docker 端口测试 |

### Git 分支与提交规范

AI 推荐：**Conventional Commits**

| 项目 | 约定 |
|------|------|
| 主分支 | `main` |
| 功能分支 | `feat/<module>-<description>` |
| 修复分支 | `fix/<module>-<description>` |
| 提交格式 | `<type>(<scope>): <description>` |
| type 枚举 | `feat`, `fix`, `refactor`, `docs`, `style`, `test`, `chore` |
| scope | 模块名或包名 |

---

## 99. 待确认问题

无
