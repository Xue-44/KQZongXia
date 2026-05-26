# 原创视觉设计技能 (Canvas Design)

## 技能定位

为集团四品牌提供从文字描述直接生成原创视觉设计的能力，覆盖海报、社交媒体素材、活动主KV、品牌视觉等场景。**区别于 image-imitation（需要参考图仿制），本技能完全从零创作**。

## 核心能力

| 能力 | 说明 | 输出格式 |
|------|------|----------|
| 海报创作 | 品牌活动海报、产品发布海报、节日营销海报 | PNG / PDF |
| 社交媒体视觉 | 朋友圈广告、小红书封面、抖音封面 | PNG |
| 活动主KV | 车展背景板、发布会主视觉 | PNG / PDF |
| 品牌视觉元素 | Logo组合、品牌色卡、装饰图形 | PNG / SVG |
| 信息图 | 产品卖点图、对比图、流程图 | PNG |

---

## 1. 四品牌设计参数（商务轻奢浅色版）

### 1.1 广汽传祺 — 珍珠白×铂金 | 极简商务

```python
TRUMPCHI_DESIGN = {
    "bg_color": "#FFFEF9",
    "primary": "#A8A8A8",
    "secondary": "#7D7D7D",
    "accent": "#D4D4D4",
    "text_primary": "#2C2C2C",
    "text_secondary": "#7D7D7D",
    "font_title": "思源黑体 CN Bold",
    "font_body": "思源黑体 CN Regular",
    "style": "minimalist, clean lines, modern tech, platinum accents",
    "decor_elements": ["细线几何图形", "铂金渐变条", "留白大量"],
    "mood": "专业、科技、克制"
}
```

### 1.2 上汽奥迪 — 象牙×玫瑰金 | 优雅轻奢

```python
AUDI_DESIGN = {
    "bg_color": "#FDFBF7",
    "primary": "#B76E79",
    "secondary": "#9B8E8A",
    "accent": "#E8C4B8",
    "text_primary": "#1C1C1C",
    "text_secondary": "#9B8E8A",
    "font_title": "Arial Black",
    "font_body": "Arial",
    "style": "elegant, luxurious, refined, rose gold highlights",
    "decor_elements": ["玫瑰金细线", "象牙纹理", "柔光渐变"],
    "mood": "优雅、精致、高端"
}
```

### 1.3 广汽昊铂 — 奶油×暗金 | 沉稳大气

```python
HYPER_DESIGN = {
    "bg_color": "#F5F0EB",
    "primary": "#B8860B",
    "secondary": "#A0522D",
    "accent": "#DEB887",
    "text_primary": "#333333",
    "text_secondary": "#A0522D",
    "font_title": "阿里巴巴普惠体 Bold",
    "font_body": "阿里巴巴普惠体 Regular",
    "style": "premium, confident, modern luxury, dark gold accents",
    "decor_elements": ["暗金边框", "赭色点缀", "几何块面"],
    "mood": "沉稳、大气、商务"
}
```

### 1.4 广汽埃安 — 暖白×香槟金 | 商务亲和

```python
AION_DESIGN = {
    "bg_color": "#FAF8F5",
    "primary": "#C9A96E",
    "secondary": "#8B7355",
    "accent": "#D4A574",
    "text_primary": "#2D2D2D",
    "text_secondary": "#8B7355",
    "font_title": "微软雅黑 Bold",
    "font_body": "微软雅黑 Regular",
    "style": "warm, approachable, modern eco, champagne gold highlights",
    "decor_elements": ["香槟金弧线", "暖棕渐变", "柔和光晕"],
    "mood": "亲和、温暖、现代"
}
```

---

## 2. 生成方案

### 2.1 方案 A：HTML/CSS → 截图（推荐）

使用 HTML + CSS 构建设计稿，通过浏览器截图输出 PNG。

```python
# 生成流程
def create_branded_design(brand: str, design_type: str, content: dict, output_path: str):
    """
    1. 根据 brand 加载对应 DESIGN 参数
    2. 根据 design_type 选择布局模板
    3. 将 content（标题/副标题/日期/文案）填入 HTML 模板
    4. 使用 Playwright 截图输出 PNG
    """
```

**可用布局模板**：
| 模板名 | 适用场景 | 规格 |
|--------|---------|------|
| `poster_a` | 产品发布海报 | 1080×1920px |
| `poster_b` | 活动预告海报 | 800×800px |
| `kv_main` | 活动主KV / 背景板 | 1920×1080px |
| `social_cover` | 社交媒体封面 | 800×800px |
| `banner_ad` | 信息流广告 | 1080×1920px |
| `infographic` | 产品卖点图 | 750×不限 |

### 2.2 方案 B：Python Pillow 直接绘制

使用 Pillow 库逐元素绘制。适合简单图形和文字排版。

```python
from PIL import Image, ImageDraw, ImageFont

def draw_poster(brand, title, subtitle, output_path, width=1080, height=1920):
    design = get_brand_design(brand)
    img = Image.new('RGB', (width, height), design['bg_color'])
    draw = ImageDraw.Draw(img)
    # 标题、副标题、品牌装饰元素逐层绘制
    img.save(output_path, 'PNG', quality=95)
```

---

## 3. 常用场景 Prompt 模板

### 3.1 产品发布海报
```
为 [品牌] 的 [车型] 创建一张产品发布海报。
主标题：[标题]
副标题：[副标题]
发布日期：[日期]
要求：商务轻奢浅色风格，突出产品名称和发布信息
```

### 3.2 活动主KV
```
为 [品牌] [活动名称] 创建活动主视觉。
主题：[主题]
时间：[日期]
地点：[地点]
规格：1920×1080px 横版
要求：大气商务风格，留白充足，品牌色点缀
```

### 3.3 节日营销海报
```
为 [品牌] 创建 [节日] 营销海报。
活动：[促销信息]
要求：节日氛围融入品牌商务轻奢风格，避免过度花哨
```

### 3.4 社交媒体封面
```
为 [品牌] 创建新媒体平台封面图（800×800px）。
品牌Slogan：[Slogan]
要求：简洁有力，品牌辨识度高
```

---

## 4. 质量检查清单

生成后逐项验证：

- [ ] 底色为浅色（暖白/象牙白/珍珠白/奶油白系）
- [ ] 主文字色为深灰/炭黑，对比度 ≥ 4.5:1
- [ ] 强调色仅用于点缀（线条/边框/小面积装饰），占比 ≤ 15%
- [ ] Logo 位置正确，安全间距达标
- [ ] 字体使用品牌指定字体
- [ ] 输出分辨率达标（屏幕 72PPI，印刷 300PPI）
- [ ] 文件名包含品牌+日期，便于归档

---

## 5. 与 image-imitation 的区别

| 维度 | image-imitation | canvas-design |
|------|----------------|---------------|
| 输入 | 必须有参考图 | 仅需文字描述 |
| 风格来源 | 从参考图提取 | 从品牌设计参数生成 |
| 灵活性 | 受参考图限制 | 完全自由创作 |
| 适用场景 | 已有满意参考风格 | 全新创意需求 |
| 速度 | 快（有模板） | 中等（需构建布局） |