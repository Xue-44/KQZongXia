# 图片识别技能 — 集团综合版

> **版本**: v2.0 | **更新日期**: 2026-05-23 | **适用 Agent**: 总虾 (xia-zong)
> **来源**: 市场虾 + 新媒体虾 合并去重

## 技能定位

面向汽车行业全场景的图片智能识别与分析，覆盖广告素材识别、活动物料识别、竞品分析、设计质量检测、车辆识别、数据图表识别六大场景，为集团7个部门提供视觉决策支持。

## 适用场景

- 市场部：广告合规检测、竞品广告分析、活动物料识别
- 新媒体部：车辆识别、活动照片分析、设计风格识别
- 销售部：车型识别、竞品车辆识别
- 售后部：车辆部件识别、维修场景识别
- 财务部：数据图表识别、发票识别
- 客服部：客户上传图片识别
- 行政部：活动照片分析、物料识别

## 识别体系

### 1. 广告素材识别（市场虾来源）

#### 1.1 广告类型分类

| 类型 | 特征 | 常见尺寸 | 投放平台 |
|------|------|---------|---------|
| 信息流广告 | 原生内容风格、软植入 | 多种尺寸 | 抖音/朋友圈/头条/百度 |
| Banner广告 | 强视觉冲击、短文案 | 1920×600 / 750×300 等 | 网站/小程序/APP |
| 开屏广告 | 全屏、3-5秒展示 | 1080×1920 | 抖音/微博/知乎 |
| 搜索广告 | 图文结合、关键词匹配 | 多种尺寸 | 百度/360/搜狗 |
| KOL种草图 | 生活化场景、产品植入 | 1:1 / 3:4 | 小红书/抖音/微博 |
| 详情页长图 | 信息密集、多屏滑动 | 750×高自适应 | 电商/小程序 |

#### 1.2 广告合规检测

检测广告图片中是否存在以下风险：
- 极限词使用（"第一""最好""绝对"等违反广告法）
- 价格标注不规范
- 品牌logo使用不合规
- 字体商用授权风险
- 图片素材版权风险
- 竞品对比中的贬低性表述

#### 1.3 广告效果预估分析

基于图片特征预估广告效果：

| 维度 | 评估指标 | 权重 |
|------|---------|------|
| 视觉吸引力 | 色彩对比度、构图冲击力、主体突出度 | 30% |
| 信息传达 | 文案清晰度、卖点突出度、阅读顺序合理性 | 35% |
| 品牌露出 | logo位置/大小、品牌色一致性 | 20% |
| 行动引导 | CTA按钮/文案的视觉突出度 | 15% |

### 2. 活动物料识别（市场虾来源）

#### 2.1 线下物料识别

| 物料类型 | 识别特征 | 用途 |
|---------|---------|------|
| 展架/X展架 | 竖版大幅、金属/塑料支架 | 活动现场入口/展区 |
| 易拉宝 | 卷轴式、可收纳 | 签到区/产品区 |
| 背景板 | 超大尺寸、拼接痕迹 | 舞台背景/拍照墙 |
| 宣传册 | 多页、装订、品牌色 | 接待台/礼品袋 |
| 车贴 | 车身覆盖、异形裁切 | 展示车辆/巡游车队 |
| 签到墙 | 大面积留白、签名区 | 活动现场入口 |
| 导视牌 | 箭头/方向指引 | 动线引导 |
| 工作证/证件 | 挂绳+卡套、人像区域 | 工作人员/嘉宾 |

#### 2.2 线上物料识别

| 物料类型 | 识别特征 | 用途 |
|---------|---------|------|
| 朋友圈海报 | 1:1 或 3:4、带二维码 | 社交传播 |
| 公众号封面 | 2.35:1 头图 | 公众号推文 |
| 小程序Banner | 750×宽 | 小程序首页 |
| H5邀请函 | 长图/多页滑动 | 活动邀请 |
| 倒计时海报 | 数字醒目、系列化 | 活动预热 |
| 战报/喜报 | 数据突出、喜庆色调 | 活动后传播 |

### 3. 车辆识别（新媒体虾来源）

#### 3.1 识别维度

| 维度 | 识别内容 | 输出格式 |
|------|---------|---------|
| 品牌 | 广汽传祺 / 上汽奥迪 / 广汽昊铂 / 广汽埃安 | 品牌名 |
| 车型 | 具体车型名称（如传祺GS8、奥迪A7L、昊铂GT、埃安Y Plus） | 车型名 |
| 颜色 | 车身主色调 + 配色方案 | 颜色描述 |
| 角度 | 前45°/正前/正侧/后45°/正后/内饰 | 拍摄角度 |
| 场景 | 城市/自然/展厅/赛道/夜间 | 场景分类 |

#### 3.2 四品牌车型特征库

**广汽传祺**
- **家族特征**：凌云翼前脸、贯穿式尾灯、悬浮式车顶
- **代表车型**：GS8（大型SUV）、M8（MPV）、影豹（轿车）、GS4（紧凑SUV）
- **辨识要点**：大面积镀铬中网、"G"字形日行灯

**上汽奥迪**
- **家族特征**：六边形大嘴格栅、矩阵式LED大灯、无框车门（部分车型）
- **代表车型**：A7L（轿跑）、Q5 e-tron（电动SUV）、Q6（大型SUV）
- **辨识要点**：四环logo位置、贯穿式OLED尾灯

**广汽昊铂**
- **家族特征**：封闭式前脸、剪刀门/鸥翼门（GT）、流线型车身
- **代表车型**：昊铂GT、昊铂SSR、昊铂HT
- **辨识要点**：低趴姿态、前后灯组设计语言

**广汽埃安**
- **家族特征**："人机共生美学"设计、贯穿式日行灯、隐藏式门把手
- **代表车型**：AION Y Plus、AION S、AION V、AION LX
- **辨识要点**："7"字形大灯、车身颜色双拼方案

### 4. 活动识别（新媒体虾来源）

#### 4.1 活动类型分类

| 活动类型 | 视觉特征 | 典型场景 |
|---------|---------|---------|
| 新车发布会 | 舞台、灯光、幕布、展车 | 大型场馆、户外发布会 |
| 试驾活动 | 车队、路线标识、体验区 | 赛道、公路、越野场地 |
| 车展 | 展台、人群、宣传物料 | 国际车展、地方车展 |
| 品牌体验日 | 互动装置、科技展示、茶歇区 | 展厅、体验中心 |
| 促销活动 | 价格牌、礼品堆、红地毯 | 4S店、商场中庭 |
| 车主活动 | 车队巡游、聚餐、合影 | 户外、餐厅 |

#### 4.2 活动关键信息提取

从活动图片中提取以下信息：
- 活动名称 / 主题
- 活动时间（从物料日期推断）
- 参与品牌及车型
- 活动规模预估（根据场地和人数）
- 物料质量评估

### 5. 设计识别（新媒体虾来源）

#### 5.1 设计类型识别

| 设计类型 | 尺寸特征 | 用途 |
|---------|---------|------|
| 海报 | 1080×1920 或 A3/A4 比例 | 线上传播、店内展示 |
| Banner | 超宽比例 (1920×600 等) | 网页、小程序 |
| 信息流广告 | 多种尺寸 | 抖音、朋友圈、头条 |
| 长图 | 超高比例 | 微信公众号 |
| 宣传册 | 多页PDF | 线下发放 |
| 展架/易拉宝 | 80×200cm 等比例 | 活动现场 |

#### 5.2 设计风格识别

- **科技感**：蓝色调、渐变光影、网格线、芯片纹样
- **豪华感**：黑金配色、大理石纹理、极简留白
- **年轻感**：高饱和度、撞色设计、动感线条
- **环保感**：绿色系、自然元素、叶片纹样

#### 5.3 品牌设计元素检测

识别图片中是否包含以下品牌元素：
- **传祺**：科技蓝色块、"GAC"标识、钻石切割纹
- **奥迪**：四环logo、金属质感、菱形格纹、红色S-line标识
- **昊铂**：Hyper标识、紫色渐变、极光色块
- **埃安**：AION字标、绿色科技元素、未来感线条

### 6. 数据图表识别（新媒体虾来源）

#### 6.1 图表类型
- 销量趋势图（折线图）
- 市场份额饼图
- 车型对比柱状图
- 用户画像雷达图
- 竞品分析矩阵图
- 满意度热力图

#### 6.2 数据提取要点
- 图表标题
- 坐标轴标签
- 数据系列名称
- 关键数据点数值
- 数据时间范围
- 数据来源标注

### 7. 竞品分析（市场虾来源）

#### 7.1 竞品广告素材分析

从竞品广告图片中提取：
- 创意方向与核心卖点
- 视觉风格与品牌调性
- 文案策略与话术体系
- 目标人群画像推断
- 投放渠道判断
- 差异化优势/劣势

#### 7.2 竞品设计对标

| 对标维度 | 我方 | 竞品A | 竞品B | 差距/优势 |
|---------|------|-------|-------|----------|
| 品牌辨识度 | - | - | - | - |
| 视觉冲击力 | - | - | - | - |
| 信息层级 | - | - | - | - |
| 文案吸引力 | - | - | - | - |
| CTA转化力 | - | - | - | - |
| 整体质感 | - | - | - | - |

### 8. 设计质量检测（市场虾来源）

#### 8.1 自动化检测项

```python
检测清单：
[ ] 分辨率达标（线上≥72dpi, 印刷≥300dpi）
[ ] 色彩模式正确（线上RGB, 印刷CMYK）
[ ] 出血位设置（印刷品≥3mm）
[ ] 文字安全区（距边缘≥5mm）
[ ] Logo清晰度（最小高度≥36px）
[ ] 字体嵌入/转曲（印刷文件）
[ ] 色彩偏差（与品牌VI对比ΔE≤5）
[ ] 图片压缩质量（JPEG≥85%）
```

## 代码示例

### 广告合规检测脚本
```python
import cv2
import numpy as np

def check_ad_compliance(image_path: str, brand: str = "") -> dict:
    """
    广告图合规检测
    检测极限词、价格标注、品牌元素等
    """
    img = cv2.imread(image_path)
    if img is None:
        return {"error": "无法读取图片"}
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width = img_rgb.shape[:2]
    
    result = {
        "file": image_path,
        "size": f"{width}x{height}",
        "warnings": [],
        "score": 100,
    }
    
    # 尺寸合规检查
    valid_sizes = {
        "抖音信息流": [(1080, 1920), (720, 1280)],
        "朋友圈广告": [(1080, 1920), (800, 800)],
        "公众号封面": [(900, 383), (600, 275)],
    }
    matched = False
    for platform, sizes in valid_sizes.items():
        for sw, sh in sizes:
            if abs(width / height - sw / sh) < 0.05:
                matched = True
                result["platform_match"] = platform
                break
    if not matched:
        result["warnings"].append("非标准广告尺寸，部分平台可能裁剪")
    
    # 分辨率检查
    min_pixels = {"线上": 1000000, "线下印刷": 8000000}
    total_pixels = width * height
    if total_pixels < min_pixels["线上"]:
        result["warnings"].append("分辨率不足，建议≥100万像素")
        result["score"] -= 15
    
    # Logo区域检测
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logo_zones = {
        "左上": img_rgb[20:120, 20:200],
        "右上": img_rgb[20:120, width - 220:width - 20],
        "底部居中": img_rgb[height - 100:height - 20, width // 3:2 * width // 3],
    }
    
    logo_detected = False
    for zone_name, zone in logo_zones.items():
        zone_gray = cv2.cvtColor(zone, cv2.COLOR_RGB2GRAY)
        zone_std = np.std(zone_gray)
        if zone_std > 40:  # 有内容
            logo_detected = True
            result["logo_position"] = zone_name
            break
    
    if not logo_detected:
        result["warnings"].append("未检测到明显logo区域，建议增加品牌露出")
        result["score"] -= 10
    
    return result
```

### 车辆识别脚本
```python
def detect_vehicle_brand(image_path: str) -> dict:
    """
    识别汽车图片中的品牌信息
    返回：品牌、颜色、场景等分析结果
    """
    img = cv2.imread(image_path)
    if img is None:
        return {"error": "无法读取图片"}
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width = img_rgb.shape[:2]
    
    result = {
        "image_size": f"{width}x{height}",
        "aspect_ratio": round(width / height, 2),
    }
    
    # 主色调提取
    pixels = img_rgb.reshape(-1, 3).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(
        pixels, 5, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    centers = centers.astype(np.uint8)
    
    # 按占比排序
    unique, counts = np.unique(labels, return_counts=True)
    sorted_indices = np.argsort(counts)[::-1]
    dominant_colors = []
    color_names = {
        (0, 0, 0): "黑色", (255, 255, 255): "白色",
        (255, 0, 0): "红色", (0, 0, 255): "蓝色",
        (0, 255, 0): "绿色", (128, 128, 128): "灰色",
        (192, 192, 192): "银色", (255, 215, 0): "金色",
    }
    for idx in sorted_indices[:3]:
        color = tuple(centers[idx].tolist())
        ratio = counts[idx] / len(labels)
        name = color_names.get(color, f"RGB{color}")
        dominant_colors.append({"color": f"RGB{color}", "name": name, "ratio": round(ratio, 2)})
    
    result["dominant_colors"] = dominant_colors
    
    # 场景判断
    mean_brightness = np.mean(img_rgb)
    if mean_brightness < 80:
        result["scene"] = "夜间/暗光场景"
    elif mean_brightness > 180:
        result["scene"] = "户外明亮场景"
    else:
        result["scene"] = "日常户外场景"
    
    return result
```

### 批量处理脚本
```python
def batch_identify_materials(image_paths: list) -> list:
    """
    批量识别活动物料类型
    """
    material_patterns = {
        "展架/X展架": {"min_ratio": 0.3, "max_ratio": 0.5, "min_height": 1500},
        "背景板": {"min_ratio": 1.5, "max_ratio": 4.0, "min_width": 3000},
        "海报": {"min_ratio": 0.5, "max_ratio": 0.7, "max_height": 2500},
        "Banner": {"min_ratio": 2.5, "max_ratio": 5.0, "max_height": 1000},
        "方形物料": {"min_ratio": 0.9, "max_ratio": 1.1},
        "长图": {"min_ratio": 0.3, "max_ratio": 0.5, "max_height": 5000},
    }
    
    results = []
    for path in image_paths:
        try:
            img = Image.open(path)
            w, h = img.size
            ratio = w / h
            
            identified = "其他"
            for mtype, pattern in material_patterns.items():
                ratio_ok = pattern.get("min_ratio", 0) < ratio < pattern.get("max_ratio", 999)
                if ratio_ok:
                    height_ok = True
                    width_ok = True
                    if "min_height" in pattern:
                        height_ok = h >= pattern["min_height"]
                    if "max_height" in pattern:
                        height_ok = h <= pattern["max_height"]
                    if "min_width" in pattern:
                        width_ok = w >= pattern["min_width"]
                    if height_ok and width_ok:
                        identified = mtype
                        break
            
            results.append({
                "file": path,
                "size": f"{w}x{h}",
                "type": identified,
                "ratio": round(ratio, 2),
            })
        except Exception as e:
            results.append({"file": path, "error": str(e)})
    
    return results
```

## 使用说明

| 功能 | 调用方式 | 输出 |
|------|---------|------|
| 广告合规检测 | `check_ad_compliance("ad.jpg", "trumpchi")` | 合规评分+警告列表 |
| 车辆识别 | `detect_vehicle_brand("car.jpg")` | 品牌/颜色/场景分析 |
| 竞品分析 | `detect_competitive_ad("comp.jpg")` | 视觉风格/构图/品牌分析 |
| 物料批量识别 | `batch_identify_materials(["a.jpg","b.jpg"])` | 类型分类+统计 |
| 活动照片分析 | `analyze_activity_photo("event.jpg")` | 氛围/参与度/品牌曝光 |
| 设计质量检测 | `check_design_quality("design.jpg")` | 质量检查清单 |

## 输出格式

| 场景 | 格式 | 交付渠道 |
|------|------|---------|
| 单张图片分析 | JSON | 直接返回 |
| 批量图片分析 | JSON + 统计摘要 | 文件输出 |
| 合规检测报告 | Markdown + 图表 | 合规部门 |
| 竞品分析报告 | PPTX + 对比表格 | 市场部会议 |