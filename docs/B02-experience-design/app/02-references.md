# 参考清单

> **阶段**：B02-XS 体验设计
> **角色**：体验总监 + 设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app（admin 引用本文件）
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-direction.md
> **冻结状态**：未冻结

---

## REF-1：Linear（linear.app）

- **链接**：https://linear.app
- **借这一点**：键盘可达 100% 主流程；命令面板即时反馈；表格 `tabular-nums` 数字对齐；hover 浮起 1px
- **不借**：纯暗色冷工程感；零装饰的"工具属性"

## REF-2：Apple Human Interface Guidelines · Vision Pro Glass

- **链接**：https://developer.apple.com/design/human-interface-guidelines
- **借这一点**：玻璃面板的"近实远虚"层级感；`backdrop-filter` 的边缘高光（顶部 1px 暖白渐变）；玻璃投影的"墨色淡阴影"
- **不借**：3D 空间感 / 深度推拉动效；圆角全 999px 的胶囊化

## REF-3：宋代汝窑天青釉 · 故宫博物院藏品

- **链接**：故宫博物院 · 宋代汝窑天青釉
- **借这一点**：主色 `#1B3A5C`（宋瓷墨青）的明度饱和度区间；釉面"半透+微反光"质感映射到毛玻璃材质；"开片纹"启发 1px 浅描边
- **不借**：器物造型 / 3D 还原；古董色的褪色感

## REF-4：明代宣德宣纸（暖米色背景）

- **链接**：宣纸制造工艺参考
- **借这一点**：背景渐变 `#F8F2E0→#F2EBD3→#E8EFF5`（老宣纸→米色→月白瓷）；长时间阅读不疲劳
- **不借**：宣纸褶皱纹理大量铺底（最多 6% opacity 的纤维纹）

## REF-5：ForYouTech 官网（内部模板参考）

- **链接**：内部模板 `/template/foryoutech`
- **借这一点**：毛玻璃面板体系（glass/glass-strong/glass-dark）；按钮渐变+浮起交互；Light/Dark 双模 CSS 变量全覆盖架构
- **不借**：具体品牌色（cyan+sky+amber）；药丸形按钮 9999px；Cherry Blossom 粒子动效

---

## 共同模式：`借` 的可被自动验证

| 借鉴维度 | 我们的具体值 | 来源 |
|---------|------------|------|
| 表格数字对齐 | `font-variant-numeric: tabular-nums` | Linear / Stripe |
| 玻璃面板顶高光 | `inset 0 1px 0 rgba(255,250,235,.65)` | Apple visionOS |
| 主色色相 | HSL(212, 53%, 23%) ≈ `#1B3A5C` | 宋瓷天青 |
| 背景温度 | 暖米→冷月白渐变 | 宣纸 |
| 焦点环 | `0 0 0 4px rgba(46,92,138,.18)` | Linear / Stripe |

---

## 99. 待确认问题

无
