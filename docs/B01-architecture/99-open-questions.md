# 待确认问题（已全部决议）

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：所有 B01 文件
> **冻结状态**：✅ 已冻结

---

| 编号 | 问题 | 决议 | 已落实到 |
|------|------|------|---------|
| Q-01 | admin 系统域名策略 | 独立子域名（不可预测命名）+ IP/VPN 访问限制。禁止使用路径 `/admin` 区分（Cookie 作用域污染 + 扫描器探测风险） | 06-deploy-env, 08-systems |
| Q-02 | Paddle Webhook 回调与安全 | 路径 `/api/v1/app/webhooks/paddle`；强制 Paddle SDK `verifyWebhookSignature` 验签；`transaction_id` 唯一索引 + 事务检查订单状态实现幂等性，防止重发导致重复处理 | 04-api-conventions |
| Q-03 | 火山引擎语音调用方式 | 统一 HTTP 模式，不使用 WebSocket，减小服务器长连接压力 | 04-api-conventions |
| Q-04 | app/admin 用户体系 | 共用 Supabase Auth 实例 + `app_metadata.role` 角色区分；admin 角色需手动授予 | 08-systems, 09-auth-infra |
| Q-05 | i18n 语言列表 | 沿用 5 语言：zh/en/vi/th/id | 07-i18n-responsive |
