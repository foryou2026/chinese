# 游戏化动效与微交互

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：01-tokens.md（动效令牌）, 04-status-colors.md, 05-components/01-buttons.md（涟漪）
> **同源约束**：`prototype-style/parts/08-gamification.css` + `prototype-style/app.js` 与本文件逐条一致
> **冻结状态**：未冻结

---

## 设计理念

参照 Duolingo 的游戏化体验，在学习全流程中嵌入即时反馈、成就奖励和打击感，让用户在答题和学习中获得游戏般的愉悦感。所有动效均为可选增强层，`prefers-reduced-motion: reduce` 下降级为静态展示。

---

## 1. 公共动效组件清单

| 组件 | CSS class | JS API | 触发场景 | 对应音效 |
|------|----------|--------|---------|---------|
| 涟漪扩散 | `.proto-ripple-ink` | 自动（click 事件委托） | 所有按钮点击 | `sfx-tap` |
| 星星爆发 | `.proto-star-burst` | `proto.starBurst(el)` | 答题正确 | `sfx-correct` |
| 正确闪绿 | `.proto-flash-correct` | `proto.flashCorrect(el)` | 答题正确（容器级） | — |
| 错误抖动 | `.proto-shake` | `proto.shake(el)` | 答题错误 | `sfx-wrong` |
| 错误闪红 | `.proto-flash-wrong` | `proto.flashWrong(el)` | 答题错误（容器级） | — |
| XP 飘字 | `.proto-xp-float` | `proto.showXP(text, el)` | 答对/完成动作后 | `sfx-xp` |
| 关卡完成 | `.proto-level-complete-bg` / `.proto-level-complete-icon` | `proto.levelComplete()` | 最后一题完成 | `sfx-complete` |
| 五彩纸屑 | `.proto-confetti-piece` | `proto.confetti()` | 成就解锁/等级提升 | `sfx-levelup` |
| Combo 连击 | `.proto-combo` | 手动控制显隐 | 连续 ≥3 次答对 | `sfx-streak` |
| 进度条高光 | `.proto-progress-shimmer` | 添加 class 即可 | 每完成一步 | — |

---

## 2. 涟漪扩散（Ripple）

Ant Design 6 风格的点击涟漪，提供清晰的操作确认感。

| 属性 | 值 |
|------|-----|
| 触发 | `click` 事件委托，匹配 `.proto-btn` 及 `[class*="proto-btn-"]` |
| 形状 | 从点击坐标向外扩散的圆形 |
| 颜色 | `currentColor` 15% 透明度 |
| 持续时间 | 400ms |
| 缓动 | `var(--easing-out)` |
| 实现 | JS 动态创建 `<span class="proto-ripple-ink">`，动画结束后自动移除 |
| 溢出 | 按钮 `overflow: hidden` 裁切 |

```css
@keyframes proto-ripple {
  0%   { transform: translate(-50%, -50%) scale(0); opacity: 0.35; }
  100% { transform: translate(-50%, -50%) scale(4); opacity: 0; }
}
.proto-ripple-ink {
  position: absolute;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.15;
  pointer-events: none;
  animation: proto-ripple 400ms var(--easing-out) forwards;
}
```

---

## 3. 星星爆发（Star Burst）

| 属性 | 值 |
|------|-----|
| 触发 | 答题正确 |
| JS | `proto.starBurst(anchorElement)` |
| 粒子数量 | 8 个星形碎片 |
| 粒子颜色 | 交替使用 `var(--color-warning-500)` 金色 + `var(--color-brand-default)` 品牌色 |
| 爆发原点 | 传入元素的中心坐标 |
| 运动轨迹 | 从中心 360° 均匀径向扩散 40-70px，带轻微随机偏移 |
| 旋转 | 每个粒子随机旋转 0-360° |
| 持续时间 | 600ms |
| 缓动 | `var(--easing-out)` |
| 清理 | 700ms 后自动移除 DOM |

```css
@keyframes star-burst {
  0%   { transform: translate(-50%, -50%) scale(0) rotate(0deg); opacity: 1; }
  60%  { opacity: 1; }
  100% { transform: translate(var(--burst-x), var(--burst-y)) scale(1) rotate(var(--burst-r)); opacity: 0; }
}
```

---

## 4. 正确/错误反馈

### 4.1 正确闪绿

| 属性 | 值 |
|------|-----|
| JS | `proto.flashCorrect(containerElement)` |
| 效果 | 容器背景从 `var(--color-success-50)` 渐变至 transparent |
| 持续时间 | 400ms |
| 清理 | 450ms 后移除 class |

### 4.2 错误抖动

| 属性 | 值 |
|------|-----|
| JS | `proto.shake(element)` |
| 目标 | 错误的答案选项/输入框 |
| 幅度 | 左右 ±6px |
| 次数 | 3 次往返 |
| 持续时间 | 400ms |
| 清理 | `animationend` 事件后自动移除 class |

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 50%, 90% { transform: translateX(-6px); }
  30%, 70% { transform: translateX(6px); }
}
```

### 4.3 错误闪红

| 属性 | 值 |
|------|-----|
| JS | `proto.flashWrong(containerElement)` |
| 效果 | 容器背景从 `var(--color-danger-50)` 渐变至 transparent |
| 持续时间 | 300ms |
| 通常与 shake 同时触发 |

---

## 5. XP 飘字（Float Up）

| 属性 | 值 |
|------|-----|
| JS | `proto.showXP(text, anchorElement)` |
| 内容 | 如 "+10 XP"、"+5 XP" |
| 字体 | `var(--font-display)`, `var(--weight-extrabold)`, 20px |
| 颜色 | `var(--color-warning-500)` 金色 |
| 起点 | 锚点元素正上方 |
| 运动 | 弹簧缩放进入 `scale(0.5→1.2→1)` + 向上飘移 48px + 淡出 |
| 持续时间 | 900ms |
| 音效 | `sfx-xp` |
| 清理 | 950ms 后移除 DOM |

```css
@keyframes xp-float-up {
  0%   { opacity: 0; transform: translateY(0) scale(0.5); }
  20%  { opacity: 1; transform: translateY(-8px) scale(1.2); }
  40%  { opacity: 1; transform: translateY(-14px) scale(1); }
  100% { opacity: 0; transform: translateY(-48px) scale(0.9); }
}
```

---

## 6. 关卡完成（Level Complete）

| 属性 | 值 |
|------|-----|
| JS | `proto.levelComplete()` |
| 效果1 | 全屏半透 `var(--color-success-500)` 15% 绿色闪光，800ms 渐隐 |
| 效果2 | 自动触发 `proto.confetti()`（五彩纸屑） |
| 音效 | `sfx-complete` |
| 清理 | 900ms 后移除背景 DOM |

### 完成 ✓ 图标动画（可选叠加）

```css
@keyframes level-complete-check {
  0%   { transform: scale(0) rotate(-20deg); opacity: 0; }
  60%  { transform: scale(1.2) rotate(5deg); opacity: 1; }
  100% { transform: scale(1) rotate(0); opacity: 1; }
}
```

---

## 7. 五彩纸屑（Confetti）

| 属性 | 值 |
|------|-----|
| JS | `proto.confetti()` |
| 粒子数量 | 40 个矩形碎片 |
| 尺寸 | 8×14px，圆角 2px |
| 颜色 | 随机取自 Google 四色 + 橙 + 紫：`#EA4335, #FBBC04, #4285F4, #34A853, #FF6D01, #AB47BC` |
| 起始位置 | 随机分布于视口顶部上方 |
| 运动 | 加速下落至视口底部 + 随机旋转 ±720° |
| 持续时间 | 800-1400ms（每个粒子随机） |
| 延迟 | 0-200ms 随机错开 |
| 清理 | 1600ms 后移除 DOM |

---

## 8. Combo 连击计数器

| 属性 | 值 |
|------|-----|
| 显示条件 | 连续答对 ≥3 次 |
| 位置 | 学习卡/题目卡右上角 |
| 内容 | 🔥 + 连击数 + "x"（如 "🔥 5x"） |
| 进入动画 | `scale(0.6→1.3→1)` 弹簧，300ms |
| 音效 | `sfx-streak`（音高随连击数递增） |
| 重置 | 答错时隐藏，连击数归零 |

```css
@keyframes combo-pop {
  0%   { transform: scale(0.6); opacity: 0; }
  50%  { transform: scale(1.3); }
  100% { transform: scale(1); opacity: 1; }
}
```

---

## 9. 进度条高光扫过（Shimmer）

| 属性 | 值 |
|------|-----|
| 触发 | 进度条宽度变化时添加 `.proto-progress-shimmer` |
| 效果 | 白色高光条从左到右扫过进度填充区 |
| 持续时间 | 1.5s |
| 自动移除 | 不需要，动画播放一次即停 |

---

## 10. 音效系统

### 10.1 公共音效清单

| 音效 ID | 触发场景 | 时长 | 默认音量 | 描述 |
|---------|---------|------|---------|------|
| `sfx-correct` | 答题正确 | ≤300ms | 0.6 | 清脆上扬音 |
| `sfx-wrong` | 答题错误 | ≤400ms | 0.5 | 低沉短促音 |
| `sfx-tap` | game/primary 按钮点击 | ≤100ms | 0.3 | 微弱弹跳音 |
| `sfx-complete` | 关卡完成 | ≤800ms | 0.7 | 胜利号角 |
| `sfx-levelup` | 等级提升/成就解锁 | ≤1000ms | 0.8 | 渐强号角 |
| `sfx-xp` | 获得 XP | ≤200ms | 0.4 | 金币叮当音 |
| `sfx-streak` | 连续答对 combo | ≤300ms | 0.5 | 递进上扬音 |
| `sfx-card-flip` | 卡片切换 | ≤200ms | 0.3 | 纸牌翻转音 |

### 10.2 JS API

```javascript
proto.sfx('correct');           // 播放音效，默认音量
proto.sfx('correct', 0.4);     // 指定音量
proto.sfxEnabled = true;        // 全局开关（默认 false，用户设置开启）
```

### 10.3 播放规则

1. **防抖**：同一音效 100ms 内不重复
2. **优先级**：complete > correct > tap，高优先级打断低优先级
3. **减弱模式**：`prefers-reduced-motion: reduce` 不影响音效（音效非动画）
4. **实现**：HTML 中预埋 `<audio id="sfx-xxx" preload="auto">` 标签，JS 通过 `getElementById` 缓存引用

---

## 11. 非公共特效（不纳入 design-system）

以下特效与特定业务数据/页面强耦合，直接写在对应 HTML 中：

| 场景 | 所属页面 | 耦合原因 |
|------|---------|---------|
| 汉字笔画动画 | stroke/practice | SVG path 与笔顺数据绑定 |
| 拼音声调曲线 | pinyin/tone | 声调曲线 SVG 绘制 |
| 对话角色气泡 | dialogue/roleplay | 对话流程状态机驱动 |
| 成语故事翻页 | idiom/story-card | 3D 翻书效果，单页特殊 |
| 听力波形可视化 | listening/* | AudioContext 实时渲染 |

---

## 12. 动效组合模式（典型场景）

### 答题正确完整链路
```
用户选择 → 点击提交按钮 → 涟漪扩散
→ 正确选项边框变绿 + 容器闪绿(flashCorrect)
→ 星星爆发(starBurst, 从正确选项中心)
→ XP飘字(showXP, "+10 XP")
→ sfx-correct 播放
→ 如果 combo ≥3: combo 计数器弹入 + sfx-streak
```

### 答题错误完整链路
```
用户选择 → 点击提交按钮 → 涟漪扩散
→ 错误选项抖动(shake) + 容器闪红(flashWrong)
→ sfx-wrong 播放
→ combo 归零，隐藏计数器
→ 正确选项边框变绿（提示正确答案）
```

### 关卡完成完整链路
```
最后一题答对 → 正确链路动效
→ 800ms 延迟
→ 全屏绿闪(levelComplete)
→ 五彩纸屑(confetti)
→ sfx-complete 播放
→ 完成 ✓ 图标弹簧进入
```

---

## 13. 减弱动效适配

```css
@media (prefers-reduced-motion: reduce) {
  .proto-star-burst .star,
  .proto-confetti-piece,
  .proto-shake,
  .proto-level-complete-icon,
  .proto-level-complete-bg,
  .proto-progress-shimmer::after {
    animation: none !important;
  }
  .proto-xp-float {
    animation-duration: 0.01ms !important;
    opacity: 1;
  }
}
```

降级策略：粒子/抖动/闪光全部禁用，XP 飘字改为静态显示 1 秒后淡出，音效不受影响。

---

## 99. 待确认问题

无
