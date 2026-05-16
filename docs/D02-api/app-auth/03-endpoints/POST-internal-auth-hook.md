<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-internal-auth-hook.md -->

# `POST /internal/auth-hook`

## 用途
GoTrue `before_user_created` webhook：注册（含 OAuth）落库 `profiles` + 校验业务规则（v2 邀请码）。

## 鉴权
- **不**走 authRequired；
- 必须有 header `X-Webhook-Signature: sha256=<hex(hmac(body, $SUPABASE_AUTH_HOOK_SECRET))>`；
- 签名失败 → 401 `INVALID_SIGNATURE`。

## 请求（GoTrue 投递）

```jsonc
{
  "type": "before_user_created",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "raw_user_meta_data": { "name": "...", "avatar_url": "...", "locale": "vi" },
    "app_metadata": { "provider": "google" | "email" }
  }
}
```

## 流程
1. 验签；
2. 落库（幂等）：
   ```sql
   INSERT INTO profiles (id, display_name, avatar_url, locale, role)
   VALUES ($id, COALESCE($meta.name, split_part($email,'@',1)), $meta.avatar_url, COALESCE($meta.locale,'zh'), 'user')
   ON CONFLICT (id) DO NOTHING;
   ```
3. 邀请码校验（v2 开启）：metadata 若含 `invite_code` 校验 + 写绑定关系；
4. 返 200。

## 响应

```json
{ "decision": "continue" }
```

> 出错时返非 200，GoTrue 会中止注册流程。

## 兜底
DB 触发器 `handle_new_user` 在 Hook 失败时仍兜底落 profiles（避免孤儿 user）；Hook 优先，触发器只在 `profiles` 行未存在时插入。
