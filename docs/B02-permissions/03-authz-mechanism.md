<!-- TARGET-PATH: docs/B02-permissions/03-authz-mechanism.md -->

# 03 · 权限校验机制

> **阶段**：B02-P  
> **上游**：`01-roles.md`、`02-auth-flow.md`、`B01-architecture/04-api-conventions.md`  
> **下游**：所有 D02 L 接口、`packages/shared-config/src/auth.ts`  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 前端：TanStack Router `_authed` / `_admin` 布局路由作为守卫；菜单源数据按 `requireAuth` / `requireRole` 过滤；按钮"无权直接不渲染"。
- 后端：4 个中间件 `authRequired` / `adminRequired` / `csrfRequired` / `optionalAuth`；RLS 兜底；service_role 仅在通过中间件后使用。
- 错误码统一 `AUTH_*`，权威清单 §4。

---

## 1. 前端

### 1.1 路由守卫（TanStack Router）

`system/apps/web-app/src/routes/_authed.tsx`：

```ts
export const Route = createFileRoute('/_authed')({
  beforeLoad: ({ context, location }) => {
    const { user } = context.auth;
    if (!user) {
      throw redirect({ to: '/auth/login', search: { redirect: location.href } });
    }
  },
  component: Outlet,
});
```

`system/apps/web-admin/src/routes/_admin.tsx`：

```ts
export const Route = createFileRoute('/_admin')({
  beforeLoad: ({ context }) => {
    const { user } = context.auth;
    if (!user) throw redirect({ to: '/admin/auth/login' });
    if (user.role !== 'super_admin') {
      throw redirect({ to: '/admin/auth/login', search: { reason: 'not_admin' } });
    }
  },
  component: AdminLayout,
});
```

- 受保护路由全部放 `_authed/` / `_admin/` 子目录，自动继承。
- 公开路由（`/auth/*`、`/discover` 前 3 主题、`/403`、`/404`）放守卫外。

### 1.2 菜单过滤

源数据：`system/packages/shared-config/src/menus.ts`

```ts
type MenuItem = {
  key: string;
  i18nKey: string;
  path: string;
  icon: LucideIconName;
  requireAuth?: boolean;
  requireRole?: 'super_admin';
};
```

`<TopNav />` 按当前 `useAuth().user.role` 过滤；未登录看应用端公共菜单（详见 `B04-design/design-system/03-navigation.md §1.2`）。

### 1.3 按钮 / 操作级控制

- **无权按钮直接不渲染**（不"灰显禁用"）；
- 例外：登录但所有权不匹配（如别人帖子的"删除"按钮）→ 不渲染；
- 危险操作即便按钮可见，**后端必须二次校验**，前端不可信。

### 1.4 Token 过期处理

```
supabase-js auto refresh 失败
  → onAuthStateChange('SIGNED_OUT')
  → authStore.reset()
  → 全局 fetch 拦截器收到 401 / AUTH_TOKEN_EXPIRED
  → Toast "登录已过期，请重新登录"
  → router.navigate('/auth/login', { search: { redirect: currentPath } })
```

TanStack Query 全局禁止重试 `AUTH_TOKEN_EXPIRED`：
```ts
queryClient.setDefaultOptions({
  queries: { retry: (n, err) => err?.code !== 'AUTH_TOKEN_EXPIRED' && n < 2 }
});
```

### 1.5 全局 `useAuth` 契约

```ts
type AuthState = {
  user: { id: string; email: string; role: 'user' | 'super_admin'; avatar?: string } | null;
  loading: boolean;
  signIn: (email: string, password: string) => Promise<void>;
  signInWithGoogle: () => Promise<void>;   // 仅应用端有效
  signOut: () => Promise<void>;
};
```

Zustand 实现，挂在 `packages/shared-utils/src/auth/useAuth.ts`，应用端 / 管理端共用。

---

## 2. 后端

### 2.1 中间件分层

| 中间件 | 作用 | 失败响应 |
|--------|------|---------|
| `authRequired` | 从 `zhiyu-at` Cookie（优先）或 `Authorization: Bearer` Header 读 JWT；校签名 + exp + `zhiyu.profiles.is_active`；写 `c.set('user', {...})` | 401 `AUTH_TOKEN_MISSING` / `AUTH_TOKEN_EXPIRED` / `AUTH_TOKEN_INVALID` / `AUTH_ACCOUNT_DISABLED` |
| `adminRequired` | 在 `authRequired` 之后；要求 `user.role === 'super_admin'` | 403 `AUTH_FORBIDDEN`（前端按 reason 文案显示 `AUTH_NOT_ADMIN`）|
| `csrfRequired` | POST / PUT / PATCH / DELETE 必加；比对 `X-CSRF-Token` Header 与 `zhiyu-csrf` Cookie | 403 `AUTH_CSRF_INVALID` |
| `optionalAuth` | 解析 JWT 但不强制；用于"未登录可浏览"路由 | 不报错；`c.get('user')` 可能为 null |

注册示例：

```ts
const app = new Hono();
app.use('/admin/v1/*', authRequired, adminRequired);
app.use('/api/v1/me/*', authRequired);
app.use('/api/v1/discover/*', optionalAuth);
app.use('*', csrfRequired);  // 仅写方法生效，路由内部按需 opt-out
```

### 2.2 `authRequired` 实现要点

```ts
import { jwtVerify } from 'jose';
import { getCookie } from 'hono/cookie';

const KEY = new TextEncoder().encode(process.env.SUPABASE_JWT_SECRET!);
const disabledCache = new LRU<string, boolean>({ max: 5_000, ttl: 30_000 });

export const authRequired: MiddlewareHandler = async (c, next) => {
  const cookieTok = getCookie(c, 'zhiyu-at');
  const auth = c.req.header('authorization');
  const token = cookieTok ?? (auth?.startsWith('Bearer ') ? auth.slice(7) : null);
  if (!token) return jsonError(c, 401, 'AUTH_TOKEN_MISSING');

  let payload: any;
  try {
    ({ payload } = await jwtVerify(token, KEY));
  } catch (e: any) {
    const code = e?.code === 'ERR_JWT_EXPIRED' ? 'AUTH_TOKEN_EXPIRED' : 'AUTH_TOKEN_INVALID';
    return jsonError(c, 401, code);
  }

  const userId = payload.sub as string;
  let disabled = disabledCache.get(userId);
  if (disabled === undefined) {
    const { data } = await supabaseAdmin
      .schema('zhiyu')
      .from('profiles').select('is_active').eq('id', userId).single();
    disabled = data?.is_active === false;
    disabledCache.set(userId, disabled);
  }
  if (disabled) return jsonError(c, 401, 'AUTH_ACCOUNT_DISABLED');

  c.set('user', {
    id: userId,
    email: payload.email,
    role: payload.app_metadata?.role ?? 'user',
  });
  await next();
};
```

- 缓存目的：避免每请求查 DB；30s 内被禁用最多继续访问 30s，业务可接受。
- 主动清缓存：管理端禁用 / 启用动作调 `disabledCache.delete(userId)`；多实例时切 Redis pubsub。

### 2.3 RLS（行级安全）兜底

- Supabase 表默认开 RLS；`profiles` / `user_sessions` / 业务表均按 `auth.uid()` 限制读写；
- Hono 后端使用 `service_role` key（绕 RLS）；**仅在通过 `authRequired` 校验后**调 `supabaseAdmin`；
- **不**直接转发用户 access_token 给 Supabase（避免双重校验开销 + 防止 token 经服务器中转）；
- 公网直连 Supabase（前端 anon key）：本期暂不开放，所有业务走 Hono。

### 2.4 Cookie 代理接口（supabase-js 适配器配套）

前端 supabase-js 初始化时传入自定义 `auth.storage`，**不读写 localStorage**；所有 read/write 转发到同域：

| 接口 | 方法 | 行为 |
|------|------|------|
| `/api/auth/cookie/get` | GET | 返回 `{ accessToken: present(bool), refreshToken: present(bool), user: { id,email,role } }` —— **不回传实际 token**，仅声明存在性 + 解码出 user payload |
| `/api/auth/cookie/set` | POST | body `{ access_token, refresh_token }` → Set-Cookie：`zhiyu-at` (HttpOnly 3600s) + `zhiyu-rt` (HttpOnly 2592000s) + `zhiyu-csrf` (非 HttpOnly 32B 随机) |
| `/api/auth/cookie/clear` | POST | 三个 Cookie 全部 `Max-Age=0` |

supabase-js 在 `signInWithPassword` / `exchangeCodeForSession` / `refreshSession` 后由适配器拦截，转调 `cookie/set` 同步到后端。

---

## 3. 统一错误响应格式

与 `B01-architecture/04-api-conventions.md §3.3` 完全一致：

```json
{
  "code": 40100,
  "message": "登录已过期，请重新登录",
  "errors": [{ "field": null, "code": "AUTH_TOKEN_EXPIRED", "message": "..." }],
  "data": null,
  "request_id": "req_01HX...",
  "server_time": "2026-04-28T10:00:00+08:00"
}
```

- 前端按 `errors[0].code` 重新映射 i18n 文案，**不直接展示后端 message**（除 `AUTH_OAUTH_FAILED` 等需要透传 provider 信息的场景）。
- HTTP 状态：401 = 未认证 / 登录过期 / 账号禁用；403 = 已登录但权限不足。

---

## 4. AUTH_* 错误码权威清单

| Code | HTTP | 触发场景 | 前端默认提示（zh）|
|------|------|---------|------------------|
| `AUTH_TOKEN_MISSING` | 401 | 请求无 Cookie / Header | 请先登录 |
| `AUTH_TOKEN_INVALID` | 401 | JWT 签名错 / 格式错 | 登录已失效，请重新登录 |
| `AUTH_TOKEN_EXPIRED` | 401 | JWT exp 过期 | 登录已过期，请重新登录 |
| `AUTH_INVALID_CREDENTIALS` | 401 | 邮箱 / 密码错 | 邮箱或密码错误 |
| `AUTH_EMAIL_NOT_VERIFIED` | 401 | 注册后未点验证邮件 | 请先验证邮箱 |
| `AUTH_ACCOUNT_DISABLED` | 401 | profiles.is_active=false | 账号已被停用，请联系客服 |
| `AUTH_NOT_ADMIN` | 403 | 非 super_admin 进管理端 | 该账号无管理员权限 |
| `AUTH_FORBIDDEN` | 403 | 角色不足 / 资源所有权不符 | 没有访问权限 |
| `AUTH_OAUTH_FAILED` | 400 | Google OAuth 异常 | Google 登录失败：{provider_error} |
| `AUTH_RESET_TOKEN_INVALID` | 400 | 重置链接过期 / 已用 | 链接已失效，请重新申请 |
| `AUTH_LOGIN_RATE_LIMITED` | 429 | 5 次失败 / 15 min | 失败次数过多，请 {minutes} 分钟后重试 |
| `AUTH_FORGOT_RATE_LIMITED` | 429 | 忘密 60s/1h throttle | 操作过于频繁，请稍后再试 |
| `AUTH_REGISTER_RATE_LIMITED` | 429 | 注册 IP 1h ≤ 5 | 注册过于频繁，请稍后再试 |
| `AUTH_SESSION_KICKED` | 401 | 被其他设备挤掉 | 您的账号在其他设备登录，已被退出 |
| `AUTH_SUPER_ADMIN_SELF_DELETE` | 400 | 超管尝试删除 / 禁用自己 | 超级管理员账号不能删除或禁用自己 |
| `AUTH_EMAIL_TAKEN` | 400 | 注册时邮箱已存在 | 该邮箱已注册，请直接登录或找回密码 |
| `AUTH_WEAK_PASSWORD` | 400 | 密码不符合规则 | 密码不符合规则，请重新输入 |
| `AUTH_CSRF_INVALID` | 403 | CSRF Header 与 Cookie 不一致 | 页面已过期，请刷新重试 |
| `AUTH_EMAIL_BLOCKED` | 400 | GoTrue Hook 邮箱黑名单 | 该邮箱不允许注册 |
| `AUTH_IP_BLOCKED` | 400 | GoTrue Hook IP 黑名单 | 当前网络环境不允许注册 |
| `AUTH_INVITE_INVALID` | 400 | 邀请码无效（仅 `INVITE_ONLY=true` 时）| 邀请码无效或已使用 |

> 所有 code 必须 5 语 i18n（zh / en / vi / th / id）；登记位置 `packages/shared-i18n/src/<locale>/auth.json`。

---

## 5. 并发与一致性

- 30s LRU 缓存被禁用状态；
- 多实例切 Redis pubsub（key=`auth:disabled:{userId}` TTL 30s）；
- Token 撚销依赖 Supabase 自带机制；不维护单独黑名单。

---

## 99. 待确认问题
（无）
