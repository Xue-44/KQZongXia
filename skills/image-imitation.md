# 图片仿作技能 — 市场推广视角 (Image Imitation for Marketing)

## 定位

基于参考图片的视觉风格提取与仿作，面向市场推广场景。支持广告素材仿作、活动物料仿作、社交媒体素材仿作，适配四品牌差异化视觉体系，提升市场团队素材产出效率。

---

## 1. 仿作场景

### 1.1 广告素材仿作

**场景**：参考竞品/行业爆款广告图，创作同风格的本品牌广告

**流程**：
```
爆款广告参考 → 风格提取 → 品牌VI适配 → 文案替换 → 合规检查 → 输出
```

**关键适配**：
| 维度 | 参考提取 | 品牌应用 |
|------|---------|---------|
| 配色 | 主色/辅色/强调色 | 映射为品牌色体系 |
| 排版 | 图文比例/阅读顺序 | 保持排版逻辑 |
| 字体 | 字重/字号层级 | 替换为品牌字体 |
| 元素 | 装饰图形/icon风格 | 替换为品牌元素库 |
| 文案 | 卖点逻辑/语气 | 适配品牌调性与合规 |

### 1.2 活动物料仿作

**场景**：参考成功活动的物料设计，快速生成同风格新活动物料

**物料类型**：
- 活动主KV（背景板、签到墙、导视系统）
- 邀请函（线上H5、线下纸质）
- 现场物料（展架、易拉宝、桌牌、工作证）
- 活动后传播物料（战报、感谢信、精彩回顾）

### 1.3 社交媒体素材仿作

**场景**：参考高互动率社媒素材，生成适配四品牌调性的内容

**平台适配**：

| 平台 | 尺寸 | 风格要求 |
|------|------|---------|
| 抖音/快手 | 1080×1920 | 视觉冲击、快节奏、大字报风格 |
| 小红书 | 1080×1440 (3:4) | 精致、种草感、生活化 |
| 朋友圈 | 1080×1920 / 800×800 | 原生感、不突兀 |
| 微博 | 1200×675 (16:9) | 话题性、传播性 |
| 公众号 | 900×383 (头图) | 信息明确、品牌感 |

---

## 2. 四品牌视觉体系映射

### 2.1 广汽传祺 — 科技·品质

```python
TRUMPCHI_VI = {
    "brand": "广汽传祺",
    "primary": "#0066CC",
    "secondary": "#C0C0C0",
    "accent": "#FF6600",
    "gradient": ["#0066CC", "#004C99"],
    "font_primary": "思源黑体 Bold",
    "font_body": "思源黑体 Regular",
    "decor_elements": ["钻石切割线", "几何色块", "光效粒子"],
    "image_style": "明亮、清晰、品质感",
    "tone": "稳重可靠中带有科技温度",
    "keywords": ["品质出行", "智能安全", "全能家用"],
}
```

### 2.2 上汽奥迪 — 豪华·性能

```python
AUDI_VI = {
    "brand": "上汽奥迪",
    "primary": "#000000",
    "secondary": "#D4AF37",
    "accent": "#CC0000",
    "gradient": ["#1A1A1A", "#000000"],
    "font_primary": "Arial Bold / 思源黑体 Bold",
    "font_body": "Arial / 思源黑体 Light",
    "decor_elements": ["四环徽章纹", "菱形格纹理", "金属拉丝底纹"],
    "image_style": "暗调、质感、光影层次丰富",
    "tone": "精英克制、低调奢华",
    "keywords": ["驾驭之美", "豪华新境", "从容进取"],
}
```

### 2.3 广汽昊铂 — 先锋·极致

```python
HYPER_VI = {
    "brand": "广汽昊铂",
    "primary": "#8A2BE2",
    "secondary": "#FFD700",
    "accent": "#00FFFF",
    "gradient": ["#1A0033", "#2A004D", "#0D0020"],
    "font_primary": "Futura Bold / 思源黑体 Bold",
    "font_body": "Futura Book / 思源黑体 Light",
    "decor_elements": ["极光光效", "粒子流", "赛博网格", "能量环"],
    "image_style": "未来感、暗调炫彩、赛博朋克",
    "tone": "先锋极客、颠覆创新",
    "keywords": ["极致性能", "智能先锋", "未来已来"],
}
```

### 2.4 广汽埃安 — 环保·年轻

```python
AION_VI = {
    "brand": "广汽埃安",
    "primary": "#00B050",
    "secondary": "#FFFFFF",
    "accent": "#00D4FF",
    "gradient": ["#00B050", "#008040"],
    "font_primary": "PingFang SC Bold / 思源黑体 Bold",
    "font_body": "PingFang SC Regular / 思源黑体 Regular",
    "decor_elements": ["叶片脉络", "充电波", "圆润几何", "环保符号"],
    "image_style": "明亮、清新、年轻活力",
    "tone": "青春共鸣、轻松自信",
    "keywords": ["潮玩出行", "绿色智能", "年轻首选"],
}
```

---

## 3. 仿作流水线

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ 参考输入  │ → │ 风格提取  │ → │ 品牌适配  │ → │ 内容替换  │
│ 图片+文案 │    │ 配色/排版 │    │ VI映射    │    │ 元素+文案 │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                       ↓
┌──────────┐    ┌──────────┐    ┌──────────┐
│ 最终输出  │ ← │ 合规检查  │ ← │ 合成导出  │
│ 成品素材  │    │ 品牌规范  │    │ 多格式    │
└──────────┘    └──────────┘    └──────────┘
```

---

## 4. 代码示例

### 4.1 参考风格提取器

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageStat
import cv2
import numpy as np
from collections import Counter


def extract_marketing_style(image_path: str) -> dict:
    """
    从参考图片（广告/海报/社媒素材）中提取市场推广风格特征
    """
    img = cv2.imread(image_path)
    if img is None:
        return {"error": f"无法读取图片: {image_path}"}

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.open(image_path).convert("RGBA")
    height, width = img_rgb.shape[:2]

    style = {
        "file": image_path,
        "size": f"{width}x{height}",
        "ratio": round(width / height, 2),
    }

    # --- 配色方案提取 (K-Means, 6色) ---
    pixels = img_rgb.reshape(-1, 3).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1.0)
    _, labels, centers = cv2.kmeans(pixels, 6, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = centers.astype(np.uint8)
    unique, counts = np.unique(labels, return_counts=True)

    palette = []
    for idx in np.argsort(counts)[::-1]:
        color = tuple(centers[idx].tolist())
        hex_color = "#{:02X}{:02X}{:02X}".format(*color)
        ratio = round(counts[idx] / len(labels), 3)
        palette.append({"hex": hex_color, "rgb": list(color), "ratio": ratio})

    style["palette"] = palette
    style["dominant"] = palette[0]["hex"]

    # --- 色调分析 ---
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mean_hue = np.mean(hsv[:, :, 0])
    mean_sat = np.mean(hsv[:, :, 1])
    mean_val = np.mean(hsv[:, :, 2])

    style["hue_mean"] = round(mean_hue, 1)
    style["sat_mean"] = round(mean_sat, 1)
    style["val_mean"] = round(mean_val, 1)

    # --- 排版布局分析 ---
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 40, 120)

    # 四象限内容密度
    h_half, w_half = height // 2, width // 2
    quadrants = {
        "左上": edges[:h_half, :w_half],
        "右上": edges[:h_half, w_half:],
        "左下": edges[h_half:, :w_half],
        "右下": edges[h_half:, w_half:],
    }
    layout = {}
    for name, quad in quadrants.items():
        layout[name] = round(np.sum(quad > 0) / quad.size, 4)

    style["layout_density"] = layout
    max_quad = max(layout, key=layout.get)
    style["visual_weight"] = f"视觉重心偏{max_quad}"

    # --- 清晰度/质感 ---
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    if laplacian_var > 500:
        style["sharpness"] = "高（高清/专业摄影）"
    elif laplacian_var > 100:
        style["sharpness"] = "中（正常质量）"
    else:
        style["sharpness"] = "低（可能模糊/压缩过度）"

    return style
```

### 4.2 品牌风格应用器

```python
def apply_brand_overlay(
    base_image_path: str,
    brand: str,
    output_path: str,
    headline: str = "",
    subheadline: str = "",
    cta_text: str = "",
    logo_path: str = "",
) -> str:
    """
    为图片应用品牌视觉叠加层

    参数:
        base_image_path: 底图路径
        brand: 品牌 (trumpchi/audi/hyper/aion)
        output_path: 输出路径
        headline: 主标题
        subheadline: 副标题
        cta_text: 行动号召文字
        logo_path: logo文件路径（可选）
    """
    brand_configs = {
        "trumpchi": {
            "name": "广汽传祺",
            "primary": (0, 102, 204),
            "secondary": (192, 192, 192),
            "accent": (255, 102, 0),
            "gradient_top": (0, 102, 204, 60),
            "gradient_bot": (0, 51, 102, 180),
        },
        "audi": {
            "name": "上汽奥迪",
            "primary": (0, 0, 0),
            "secondary": (212, 175, 55),
            "accent": (204, 0, 0),
            "gradient_top": (0, 0, 0, 20),
            "gradient_bot": (0, 0, 0, 200),
        },
        "hyper": {
            "name": "广汽昊铂",
            "primary": (138, 43, 226),
            "secondary": (255, 215, 0),
            "accent": (0, 255, 255),
            "gradient_top": (26, 0, 51, 40),
            "gradient_bot": (42, 0, 77, 190),
        },
        "aion": {
            "name": "广汽埃安",
            "primary": (0, 176, 80),
            "secondary": (255, 255, 255),
            "accent": (0, 212, 255),
            "gradient_top": (0, 176, 80, 40),
            "gradient_bot": (0, 102, 51, 180),
        },
    }

    brand = brand.lower()
    if brand not in brand_configs:
        raise ValueError(f"不支持的品牌: {brand}")

    config = brand_configs[brand]
    img = Image.open(base_image_path).convert("RGBA")
    w, h = img.size

    # 创建遮罩层（底部渐变 + 品牌色调）
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 底部渐变
    gradient_height = h // 3
    for y in range(h - gradient_height, h):
        ratio = (y - (h - gradient_height)) / gradient_height
        alpha = int(180 * ratio)
        draw.rectangle([0, y, w, y + 1], fill=(0, 0, 0, alpha))

    img = Image.alpha_composite(img, overlay)

    # 绘制文字
    draw = ImageDraw.Draw(img)
    try:
        font_headline = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", min(w // 12, 80))
        font_sub = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", min(w // 20, 42))
        font_cta = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", min(w // 22, 36))
    except OSError:
        font_headline = font_sub = font_cta = ImageFont.load_default()

    # --- 主标题 ---
    if headline:
        bbox = draw.textbbox((0, 0), headline, font=font_headline)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (w - tw) // 2
        ty = h - gradient_height + 40
        # 文字阴影
        draw.text((tx + 2, ty + 2), headline, fill=(0, 0, 0, 120), font=font_headline)
        draw.text((tx, ty), headline, fill=config["secondary"], font=font_headline)

    # --- 副标题 ---
    if subheadline:
        bbox = draw.textbbox((0, 0), subheadline, font=font_sub)
        tw = bbox[2] - bbox[0]
        tx = (w - tw) // 2
        ty = h - gradient_height + 40 + (font_headline.size if headline else 0) + 20
        draw.text((tx, ty), subheadline, fill=config["secondary"], font=font_sub)

    # --- CTA ---
    if cta_text:
        bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (w - tw) // 2
        ty = h - 80
        # CTA 背景条
        padding = 30
        draw.rounded_rectangle(
            [tx - padding, ty - padding // 2,
             tx + tw + padding, ty + th + padding // 2],
            radius=10, fill=config["primary"]
        )
        draw.text((tx, ty), cta_text, fill=(255, 255, 255), font=font_cta)

    # --- 品牌角标 ---
    draw.text((30, 30), config["name"], fill=config["secondary"], font=font_sub)

    img = img.convert("RGB")
    img.save(output_path, quality=95)
    return output_path


def create_social_media_variant(
    image_path: str,
    brand: str,
    platform: str,
    output_path: str,
    text: str = "",
) -> str:
    """
    根据平台生成适配尺寸的社交媒体素材

    参数:
        image_path: 原始图片
        brand: 品牌
        platform: 平台 (douyin/xiaohongshu/wechat/weibo/gongzhonghao)
        output_path: 输出路径
        text: 叠加文案
    """
    platform_sizes = {
        "douyin": (1080, 1920),
        "xiaohongshu": (1080, 1440),
        "wechat_feed": (1080, 1920),
        "wechat_square": (800, 800),
        "weibo": (1200, 675),
        "gongzhonghao": (900, 383),
    }

    if platform not in platform_sizes:
        raise ValueError(f"不支持的平台: {platform}")

    target_w, target_h = platform_sizes[platform]
    img = Image.open(image_path).convert("RGBA")

    # 裁剪填充
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        new_w = int(img.height * target_ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width / target_ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, img.width, top + new_h))

    img = img.resize((target_w, target_h), Image.LANCZOS)

    # 应用品牌样式
    output = apply_brand_overlay(
        image_path, brand, output_path,
        headline=text if platform in ("douyin", "xiaohongshu") else "",
    )
    return output


def batch_generate_materials(
    reference_image: str,
    brand: str,
    output_dir: str,
    headlines: list,
    platforms: list = None,
) -> dict:
    """
    基于一张参考图，批量生成多平台多文案素材

    参数:
        reference_image: 参考底图
        brand: 目标品牌
        output_dir: 输出目录
        headlines: 文案列表
        platforms: 平台列表，默认全部
    """
    import os
    os.makedirs(output_dir, exist_ok=True)

    if platforms is None:
        platforms = ["douyin", "xiaohongshu", "wechat_feed", "weibo"]

    results = []
    for i, headline in enumerate(headlines):
        for platform in platforms:
            output_name = f"{brand}_{platform}_v{i+1}.jpg"
            output_path = os.path.join(output_dir, output_name)
            create_social_media_variant(
                reference_image, brand, platform, output_path, headline
            )
            results.append({"platform": platform, "headline": headline, "output": output_path})

    return {
        "total": len(results),
        "brand": brand,
        "files": results,
    }
```

---

## 5. 使用说明

### 典型工作流

```python
# 1. 分析参考图的风格
style = extract_marketing_style("竞品爆款海报.jpg")

# 2. 基于风格生成品牌素材
apply_brand_overlay(
    "底图.jpg", "trumpchi",
    "output.jpg",
    headline="传祺GS8 春季焕新",
    subheadline="大7座 · 超低油耗 · 智能安全",
    cta_text="立即预约试驾 →"
)

# 3. 批量生成社交媒体版本
batch_generate_materials(
    "底图.jpg", "aion", "./output/",
    headlines=["年轻人的第一台电车", "月薪8K也养得起", "一周充一次电"],
    platforms=["douyin", "xiaohongshu"]
)
```

### 命令行快速使用

```bash
# 风格分析
python -c "from image_imitation import extract_marketing_style; print(extract_marketing_style('ref.jpg'))"

# 品牌叠加
python -c "from image_imitation import apply_brand_overlay; apply_brand_overlay('base.jpg','audi','out.jpg','奥迪A7L')"
```