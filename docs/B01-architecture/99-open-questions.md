# 待确认问题

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：所有 B01 文件
> **冻结状态**：未冻结

---

| 编号 | 问题 | AI 默认方案 | 影响 |
|------|------|-----------|------|
| Q-01 | admin 系统是否需要独立域名/端口，还是通过 Nginx 路径区分？ | 默认独立端口 3001，Nginx 按路径 `/admin` 代理 | 06-deploy-env, 08-systems |
| Q-02 | Paddle 收款的 Webhook 回调路径和签名验证方案是否已确定？ | 默认 `/api/v1/app/webhooks/paddle`，使用 Paddle SDK 验签 | 04-api-conventions |
| Q-03 | 火山引擎语音模型的调用方式（HTTP/WebSocket）和响应延迟预期？ | 暂按 HTTP 方式，耗时操作走 BullMQ 异步 | 04-api-conventions |
| Q-04 | app 和 admin 的用户体系是否完全隔离（独立注册），还是共用 Supabase Auth 实例按角色区分？ | 默认共用实例 + 角色区分，admin 用户需手动授予角色 | 08-systems, 09-auth-infra |
| Q-05 | i18n 语言列表是否沿用模板的 5 语言（zh/en/vi/th/id），还是需要调整？ | 沿用 5 语言 | 07-i18n-responsive |
