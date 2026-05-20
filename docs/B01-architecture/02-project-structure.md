# 项目目录结构

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack
> **冻结状态**：未冻结

---

## 产出目录

```
docs/
  B01-architecture/                          # 共享
  _shared/
    D01-data/<module>/<feature>/             # 共享
  app/
    B02-experience-design/
    C01-requirements/
      permissions/
      <module>/<feature>/
    C02-ia-interaction/<module>/<feature>/
    D02-api/<module>/<feature>/
  admin/
    B02-experience-design/
    C01-requirements/
      permissions/
      <module>/<feature>/
    C02-ia-interaction/<module>/<feature>/
    D02-api/<module>/<feature>/

C03-prototype/
  index.html
  app/
    index.html
    <module-id>/
      index.html
      <feature-id>/
        index.html
    <page-id>.html
  admin/
    index.html
    <module-id>/
      index.html
      <feature-id>/
        index.html
    <page-id>.html
```

## 源代码目录树

> **强制约束**：所有开发源代码必须置于项目根目录的 `system/` 下。根目录禁止直接放置源代码，仅允许 `docs/`、`C03-prototype/`、`system/` 及项目配置文件。

```
/                                    # 项目根
  package.json                       # workspace 根配置
  docker-compose.yml
  .env.example
  docs/                              # 规范产出
  C03-prototype/                     # HTML 原型
  system/                            # 全部源代码
    package.json                     # npm workspaces 根
    tsconfig.base.json               # 共享 TS 配置
    apps/
      web-app/                       # app 系统前端
        package.json
        vite.config.ts
        tsconfig.json
        index.html
        src/
          main.tsx
          app/
            i18n.ts
            router.tsx
            Layout.tsx
          pages/                     # 按模块分子目录
            auth/
            home/
            ...
          components/                # app 专属组件
          hooks/
          lib/                       # app 工具函数
          styles/
            globals.css
      admin-app/                     # admin 系统前端
        package.json
        vite.config.ts
        tsconfig.json
        index.html
        src/
          main.tsx
          app/
            i18n.ts
            router.tsx
            Layout.tsx
          pages/
          components/
          hooks/
          lib/
          styles/
            globals.css
      api-server/                    # 统一后端 API
        package.json
        tsconfig.json
        Dockerfile
        src/
          index.ts                   # 入口
          app.ts                     # Hono app 组装
          config/
            env.ts                   # 环境变量校验
          middleware/
            auth.ts                  # JWT 验签
            error-handler.ts         # 全局异常拦截
            logger.ts
          routes/
            app/                     # /api/app/* 路由
              auth.ts
              ...
            admin/                   # /api/admin/* 路由
              auth.ts
              ...
          services/                  # 业务逻辑层
          repositories/              # 数据访问层（Drizzle）
          db/
            schema/                  # Drizzle schema 定义
              index.ts
            migrations/              # Drizzle 迁移文件
            client.ts                # DB 连接池
            redis.ts                 # Redis 连接
          jobs/                      # BullMQ 任务定义
          utils/
    packages/
      shared-config/                 # 共享配置
        package.json
        src/
          locales.ts                 # 语言列表
          constants.ts               # 全局常量
      shared-i18n/                   # 共享 i18n 资源
        package.json
        scripts/
          verify-i18n.ts
        src/
          index.ts
          en.ts
          zh.ts
          ...
      shared-types/                  # 共享 TypeScript 类型
        package.json
        src/
          index.ts
          api.ts                     # API 响应/请求类型
          db.ts                      # 数据库实体类型
      shared-utils/                  # 共享工具函数
        package.json
        src/
          index.ts
      ui-kit/                        # 共享 UI 组件（基于 shadcn/ui 封装）
        package.json
        src/
          components/
          index.ts
    supabase/
      migrations/                    # SQL 迁移文件（Git 留痕）
```

## 前端工程策略

AI 推荐：**单仓双 app + 共享包**。app 和 admin 各自独立 Vite 应用，通过 workspace packages 共享类型、i18n、UI 组件和工具函数。理由：构建隔离、部署独立、代码复用。

## 模块边界规则

| 规则 | 说明 |
|------|------|
| app 间禁止互相导入 | `web-app` 和 `admin-app` 不可交叉引用 |
| 共享代码走 packages | 两个 app 共用的逻辑必须抽入 `packages/*` |
| 后端分层禁止跳层 | routes -> services -> repositories，禁止 route 直接访问 DB |
| 包间依赖单向 | `shared-types` 不可依赖 `shared-utils`，反向可以 |

## 文件命名规则

| 对象 | 规则 | 示例 |
|------|------|------|
| React 组件 | PascalCase.tsx | `UserProfile.tsx` |
| 页面文件 | PascalCase.tsx 或 kebab-case 目录 | `pages/auth/Login.tsx` |
| 工具/Hook | camelCase.ts | `useAuth.ts`, `formatDate.ts` |
| 路由文件 | kebab-case.ts | `auth.ts`, `user-settings.ts` |
| 类型文件 | kebab-case.ts | `api-types.ts` |
| 配置文件 | kebab-case | `vite.config.ts` |
| DB schema | kebab-case.ts | `user-profiles.ts` |
| 迁移文件 | `YYYYMMDDHHMMSS_description.sql` | `20260520120000_create_users.sql` |

## 单文件行数上限：1200

---

## 99. 待确认问题

无
