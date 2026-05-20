# API 接口规范

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack, 08-systems
> **冻结状态**：未冻结

---

## 基础约定

| 项目 | 约定 |
|------|------|
| 风格 | REST |
| 基础路径 | `/api/v1/{system}` |
| 请求/响应格式 | JSON |
| 时间格式 | ISO 8601 (`2026-05-20T12:00:00Z`) |
| Content-Type | `application/json` |
| 字符编码 | UTF-8 |

## 版本策略

AI 推荐：**URL 路径前缀**

| 项目 | 决定 |
|------|------|
| 格式 | `/api/v1/...` |
| 升级时机 | 破坏性变更时递增 |
| 理由 | 显式、可路由、易调试 |

## URL 命名规则

| 操作 | 方法 | 格式 | 示例 |
|------|------|------|------|
| 列表 | GET | `/api/v1/{sys}/{resources}` | `GET /api/v1/app/articles` |
| 详情 | GET | `/api/v1/{sys}/{resources}/:id` | `GET /api/v1/app/articles/:id` |
| 创建 | POST | `/api/v1/{sys}/{resources}` | `POST /api/v1/app/articles` |
| 全量修改 | PUT | `/api/v1/{sys}/{resources}/:id` | `PUT /api/v1/admin/articles/:id` |
| 部分修改 | PATCH | `/api/v1/{sys}/{resources}/:id` | `PATCH /api/v1/app/users/:id` |
| 删除 | DELETE | `/api/v1/{sys}/{resources}/:id` | `DELETE /api/v1/admin/articles/:id` |

> 资源名使用 kebab-case 复数形式。嵌套资源最多两层：`/articles/:id/sentences`。

## 统一响应格式

AI 推荐：`{ code, data, msg }` 三字段外壳

成功：
```json
{ "code": 0, "data": { ... }, "msg": "ok" }
```

分页：
```json
{
  "code": 0,
  "data": {
    "items": [...],
    "total": 100,
    "page": 1,
    "page_size": 20
  },
  "msg": "ok"
}
```

错误：
```json
{ "code": 40001, "msg": "参数校验失败", "details": { "field": "email", "reason": "格式不正确" } }
```

## 错误码体系

AI 推荐：**5 位数字，按模块分段**

| 范围 | 说明 |
|------|------|
| 0 | 成功 |
| 40001-40099 | 通用参数错误 |
| 40101-40199 | 认证错误（Token 过期、无效等） |
| 40301-40399 | 权限不足 |
| 40401-40499 | 资源不存在 |
| 40901-40999 | 冲突（重复、并发） |
| 42901-42999 | 限流 |
| 50001-50099 | 服务器内部错误 |
| 50301-50399 | 第三方服务异常 |

> 模块级错误码在 D02 阶段按功能定义，此处仅定义范围。

## 分页/排序/筛选

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `page` | number | 1 | 页码，从 1 开始 |
| `page_size` | number | 20 | 每页条数，上限 100 |
| `sort` | string | — | 排序字段，如 `created_at` |
| `order` | string | `desc` | `asc` / `desc` |
| `q` | string | — | 全文搜索关键词 |
| `filter[field]` | string | — | 字段级精确筛选 |

## 幂等策略

| 方法 | 幂等性 | 策略 |
|------|--------|------|
| GET | 天然幂等 | — |
| PUT | 天然幂等 | 全量替换 |
| DELETE | 天然幂等 | 软删除 |
| POST | 非幂等 | 关键操作使用 `X-Idempotency-Key` 请求头 |
| PATCH | 非幂等 | 使用 `updated_at` 乐观锁 |

## 限流策略

| 维度 | 策略 |
|------|------|
| 全局 | Nginx 层 IP 限流 |
| 接口级 | Hono 中间件 + Redis 滑动窗口 |
| 认证接口 | 更严格限流（登录 5次/分钟，注册 3次/分钟） |
| 响应头 | `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` |

## 长任务处理

| 场景 | 策略 |
|------|------|
| 耗时操作 | 返回 `202 Accepted` + 任务 ID |
| 进度查询 | `GET /api/v1/{sys}/tasks/:taskId` |
| 底层实现 | BullMQ 队列异步处理 |

---

## 99. 待确认问题

无
