# 密码管理

## `PUT /api/v1/admin/auth/password` · 修改密码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-change-password |
| SM 转移 | 无 |
| R-ID | R-auth-005, R-auth-009 |
| 角色 | Bearer JWT + admin |
| 行级权限 | auth.uid() = 自身 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Header | Authorization | string | 是 | Bearer JWT | — |
| Body | old_password | string | 是 | 非空 | — |
| Body | new_password | string | 是 | ≥8字符含字母+数字 | — |

> admin 系统无 Google 登录，修改密码始终需要旧密码。

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  participant DB
  FE->>BE: PUT /password {old_password, new_password}
  BE->>SupaAuth: signInWithPassword(email, old_password)验旧
  alt 旧密码错误
    BE-->>FE: 401 旧密码错误
  end
  BE->>BE: 检查 new≠old
  BE->>SupaAuth: updateUser({password: new_password})
  BE->>DB: 其他 user_sessions(admin) is_active=false
  BE->>SupaAuth: signOut(scope=others)
  BE->>DB: 写 audit_logs(password_change)
  BE-->>FE: {code:0, msg:"密码修改成功"}
```

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-001 | 密码强度 | 40001 |
| BR-008 | 需验证旧密码 | 40104 |
| BR-009 | 新密码≠旧密码 | 40002 |

**成功响应**

```json
{ "code": 0, "data": null, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 密码强度不足 | 不满足要求 |
| 400 | 40002 | 新密码与旧密码相同 | new=old |
| 401 | 40101 | Token无效 | JWT过期 |
| 401 | 40104 | 旧密码错误 | 旧密码不匹配 |

**副作用**
- 其他 user_sessions(admin) is_active=false + Supabase signOut(scope=others)
- 写入 audit_logs(password_change)
