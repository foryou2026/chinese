/* TARGET-PATH: docs/B04-design/prototype-style/app.js
 *
 * 占位文件 · 2026-04-28
 * 待 C04 第一次原型时填充。
 *
 * 内容应翻译自 docs/B04-design/design-system/05-interactions.md：
 *
 * 1. 主题与品牌色 FOUC 处理（同步执行块；本应内联在 <head>，此处保留 export 供原型 <script defer>）：
 *    - localStorage 读 theme / brand-color
 *    - matchMedia('(prefers-color-scheme: dark)') 兜底
 *    - 写 document.documentElement.dataset.theme + style.setProperty('--brand', ...)
 *
 * 2. 主题切换按钮：[data-action="toggle-theme"] 监听，循环 light ↔ dark
 *
 * 3. 顶栏滚动阴影：scroll > 4 时给 .topnav 加 is-scrolled
 *
 * 4. 全局快捷键：
 *    '?' → 弹快捷键帮助 modal
 *    'g h' → location.href = '/'
 *    'g a' → location.href = '/admin'（仅管理端原型）
 *    '/' → 聚焦顶部搜索
 *    ESC → 关闭最上层 modal/drawer/toast
 *
 * 5. 演示用交互：
 *    - 按钮点击进入 loading 态（btn.classList.add('is-loading')，3s 自动恢复）
 *    - Toast 出现 / 自动消失 / 上限 3
 *    - Modal open/close（焦点陷阱）/ Drawer 同
 *    - 表单字段 onBlur 触发样例错误展示
 *    - 列表行 hover / 选中切换
 *
 * 6. prefers-reduced-motion: reduce → 自动跳过所有 transition / animation
 *
 * 注意：本文件仅作"原型可视化"用，不是产品代码。
 *      最终产品在 system/packages/ui-kit/ 用 React + Tailwind 实现；二者必须保持视觉等价。
 */
