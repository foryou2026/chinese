# 部署与环境

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack
> **冻结状态**：✅ 已冻结

---

## 部署形态

Docker Compose 唯一部署方式。

## 环境列表

| 环境 | 用途 | 数据库 | 说明 |
|------|------|--------|------|
| dev | 开发与测试 | 本地 Supabase | Docker Compose 启动全套服务 |
| prod | 生产 | 独立服务器 | 用户自行管理，不在本项目范围 |

> CI/CD：无。生产环境部署由用户自行处理。

## 端口约定

| 服务 | 端口 | 说明 |
|------|------|------|
| web-app (前端-用户) | 3000 | Vite dev / Nginx 静态 |
| admin-app (前端-管理) | 3001 | Vite dev / Nginx 静态 |
| api-server (后端) | 8000 | Hono HTTP 服务 |
| Supabase Studio | 54323 | Supabase 自带管理界面 |
| Supabase API | 54321 | Supabase REST/Auth API |
| PostgreSQL | 54322 | 直连数据库 |
| Redis | 6379 | 缓存与队列 |
| Nginx | 80/443 | 反向代理网关，按域名分流 app/admin |

## 环境变量清单

| 变量 | 必须 | 默认 | 说明 |
|------|------|------|------|
| `NODE_ENV` | 是 | `development` | 运行环境 |
| `DATABASE_URL` | 是 | — | PostgreSQL 连接串 |
| `SUPABASE_URL` | 是 | — | Supabase API 地址 |
| `SUPABASE_ANON_KEY` | 是 | — | Supabase 匿名 Key |
| `SUPABASE_SERVICE_ROLE_KEY` | 是 | — | Supabase 服务端 Key |
| `SUPABASE_JWT_SECRET` | 是 | — | JWT 本地验签密钥 |
| `REDIS_URL` | 是 | `redis://redis:6379` | Redis 连接串 |
| `API_PORT` | 否 | `8000` | 后端监听端口 |
| `PADDLE_API_KEY` | 否 | — | Paddle 收款密钥 |
| `PADDLE_WEBHOOK_SECRET` | 否 | — | Paddle Webhook 签名密钥 |
| `GOOGLE_SMTP_USER` | 否 | — | Google 邮件发送账号 |
| `GOOGLE_SMTP_PASS` | 否 | — | Google 邮件应用密码 |
| `VOLCENGINE_ACCESS_KEY` | 否 | — | 火山引擎 Access Key |
| `VOLCENGINE_SECRET_KEY` | 否 | — | 火山引擎 Secret Key |
| `ADMIN_DOMAIN` | 是 | — | admin 系统独立子域名（不可预测命名，禁止使用路径区分） |
| `APP_DOMAIN` | 是 | — | app 系统主域名 |

> 环境变量通过 `.env` 文件注入 Docker Compose。`.env` 不入 Git，提供 `.env.example` 模板。

## 容器与编排

```yaml
# docker-compose.yml 服务清单
services:
  nginx:          # 反向代理
  web-app:        # 用户前端
  admin-app:      # 管理前端
  api-server:     # 后端 API
  redis:          # 缓存与队列
  # Supabase 相关容器由 supabase 自托管方案提供
```

## Nginx 域名路由策略

| 域名 | 转发目标 | 说明 |
|------|---------|------|
| `${APP_DOMAIN}` | web-app:3000 | 用户系统主域名 |
| `${ADMIN_DOMAIN}` | admin-app:3001 | admin 独立子域名，不可预测命名 |
| 两个域名 `/api/v1/*` | api-server:8000 | 统一后端 API |

> admin 子域名禁止使用路径 `/admin` 区分，原因：Cookie 作用域污染 + 扫描器探测风险。admin 子域名应配合 IP 白名单或 VPN 进行访问限制。

| 规则 | 说明 |
|------|------|
| 网络 | 所有服务在同一 Docker network |
| 数据持久化 | PostgreSQL、Redis 数据挂载宿主机 volume |
| 健康检查 | 每个服务配置 healthcheck |
| 重启策略 | `restart: unless-stopped` |
| 构建 | 多阶段构建，生产镜像仅含运行时 |

## 备份与回滚

| 项目 | 策略 |
|------|------|
| 数据库备份 | 用户自行配置 pg_dump 定时任务 |
| 代码回滚 | Git tag + Docker 镜像版本 |
| 迁移回滚 | Drizzle Kit down 迁移 |

---

## 99. 待确认问题

无
