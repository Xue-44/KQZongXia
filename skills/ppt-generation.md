# 市场推广PPT制作技能

## 技能定位
本技能用于生成市场推广相关的演示文稿，面向集团和各品牌的市场总监、区域经理，支持市场分析报告、营销活动方案、费用报告、年度计划、品牌策略等多种场景。

## 支持场景
| 场景 | 典型内容 | 使用频率 |
|------|---------|---------|
| 市场分析报告PPT | 区域市场洞察、消费趋势、份额分析 | 每月/季度 |
| 营销活动方案PPT | 活动策划、执行计划、预算分配 | 活动前 |
| 费用执行报告PPT | 预算使用情况、核销进度、费效分析 | 每月/季 |
| 年度推广计划PPT | 全年市场策略、预算规划、时间表 | 年度 |
| 品牌策略PPT | 品牌定位、差异化策略、传播规划 | 按需 |

## 标准结构模板

### 1. 封面页
- 集团/品牌Logo + 报告标题 + 副标题
- 报告日期 + 汇报人 + 密级标注
- 简约商务风格

### 2. 目录页
- 核心议题预览（4-6个部分）
- 每部分预计时长
- 导航指引

### 3. 市场分析页
- 宏观市场环境（PEST分析）
- 区域市场数据对比
- 消费趋势与洞察
- 市场份额分析

### 4. 竞品对标页
- 竞品动态扫描
- 竞争优劣势对比
- 市场份额变化趋势
- 竞品费用投入分析

### 5. 策略规划页
- 核心策略概述
- 分品牌/分区域策略
- 资源分配方案
- 关键里程碑

### 6. 费用分析页
- 预算执行概览
- 费用结构分析
- 费效比分析
- 核销进度追踪

### 7. 总结页
- 核心结论
- 风险提示
- 下一步行动
- Q&A

## PPT质量标准检查清单

### 内容质量
- [ ] 所有数据有明确来源和统计口径
- [ ] 分析结论有数据支撑，不含主观臆断
- [ ] 逻辑严密，因果链条清晰
- [ ] 建议方案具有可操作性
- [ ] 风险识别全面，应对措施具体

### 视觉设计
- [ ] 商务专业风格，配色克制
- [ ] 字体统一（建议微软雅黑/思源黑体）
- [ ] 每页核心信息不超过3个要点
- [ ] 图表清晰可读，标注完整

### 技术规范
- [ ] 文件大小 < 50MB
- [ ] 兼容 Office 2016+ 和 WPS
- [ ] 敏感数据标注"内部资料"
- [ ] 所有图表可编辑（非截图）

## Python 代码模板 (python-pptx)

### 基础配置

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from datetime import datetime

# 集团商务配色
COLOR_SCHEME = {
    "primary": RGBColor(31, 56, 100),      # 深蓝
    "secondary": RGBColor(68, 114, 196),    # 中蓝
    "accent": RGBColor(237, 125, 49),       # 橙色强调
    "light": RGBColor(221, 235, 247),       # 浅蓝背景
    "dark": RGBColor(23, 42, 75),           # 深色强调
    "text": RGBColor(51, 51, 51),           # 正文
    "gray": RGBColor(128, 128, 128),        # 辅助文字
    "white": RGBColor(255, 255, 255),
}
```

### 封面页

```python
def create_cover_page(prs, title, subtitle, date=None, presenter=None, dept=None):
    """创建市场推广报告封面页"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # 顶部装饰条
    top_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.12)
    )
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_SCHEME["primary"]
    top_bar.line.fill.background()

    # 左侧装饰竖条
    left_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.06), Inches(7.5)
    )
    left_bar.fill.solid()
    left_bar.fill.fore_color.rgb = COLOR_SCHEME["accent"]
    left_bar.line.fill.background()

    # 主标题
    title_box = slide.shapes.add_textbox(
        Inches(1.5), Inches(2.0), Inches(7.5), Inches(1.2)
    )
    tf = title_box.text_frame
    p = tf.add_paragraph()
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]

    # 副标题
    sub_box = slide.shapes.add_textbox(
        Inches(1.5), Inches(3.3), Inches(7.5), Inches(0.8)
    )
    tf = sub_box.text_frame
    p = tf.add_paragraph()
    p.text = subtitle
    p.font.size = Pt(22)
    p.font.color.rgb = COLOR_SCHEME["secondary"]

    # 底部信息
    if date is None:
        date = datetime.now().strftime("%Y年%m月%d日")

    info_lines = [f"报告日期: {date}"]
    if presenter:
        info_lines.append(f"汇报人: {presenter}")
    if dept:
        info_lines.append(f"部门: {dept}")
    info_lines.append("内部资料，请勿外传")

    info_box = slide.shapes.add_textbox(
        Inches(1.5), Inches(5.5), Inches(7.5), Inches(1.2)
    )
    tf = info_box.text_frame
    for line in info_lines:
        p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_SCHEME["gray"]
        p.space_after = Pt(4)
```

### 目录页

```python
def create_toc_slide(prs, sections):
    """创建目录页
    sections: [{"title": "标题", "duration": "5min"}, ...]
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(
        Inches(0.8), Inches(0.4), Inches(8.4), Inches(0.7)
    )
    tf = title_box.text_frame
    p = tf.add_paragraph()
    p.text = "目  录"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]

    for idx, section in enumerate(sections, 1):
        y = Inches(1.5) + Inches(idx * 0.9)
        # 序号块
        num_shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.8), y, Inches(0.6), Inches(0.5)
        )
        num_shape.fill.solid()
        num_shape.fill.fore_color.rgb = COLOR_SCHEME["primary"]
        num_shape.line.fill.background()
        tf = num_shape.text_frame
        p = tf.add_paragraph()
        p.text = f"0{idx}"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_SCHEME["white"]
        p.alignment = PP_ALIGN.CENTER

        # 标题
        content_box = slide.shapes.add_textbox(
            Inches(1.6), y, Inches(6.5), Inches(0.5)
        )
        tf = content_box.text_frame
        p = tf.add_paragraph()
        p.text = section.get("title", "")
        p.font.size = Pt(18)
        p.font.color.rgb = COLOR_SCHEME["text"]

        # 时长
        if section.get("duration"):
            dur_box = slide.shapes.add_textbox(
                Inches(8.2), y, Inches(1), Inches(0.5)
            )
            tf = dur_box.text_frame
            p = tf.add_paragraph()
            p.text = section["duration"]
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_SCHEME["gray"]

        # 分隔线
        line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), y + Inches(0.7), Inches(8.4), Inches(0.01)
        )
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_SCHEME["light"]
        line.line.fill.background()
```

### 市场分析页

```python
def create_market_analysis_slide(prs, title, metrics, insights):
    """创建市场分析页
    metrics: [{"label": "指标名", "value": "数值", "change": "变化"}, ...]
    insights: ["洞察1", "洞察2", ...]
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # 标题
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.3), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.add_paragraph()
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]

    # 指标卡片（横向排列，最多4个）
    card_width = Inches(2.1)
    gap = Inches(0.2)
    start_x = Inches(0.5)

    for idx, metric in enumerate(metrics[:4]):
        x = start_x + idx * (card_width + gap)
        y = Inches(1.3)

        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, x, y, card_width, Inches(1.5)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_SCHEME["light"]
        card.line.fill.background()

        # 指标名
        label_box = slide.shapes.add_textbox(
            x + Inches(0.15), y + Inches(0.1), card_width - Inches(0.3), Inches(0.3)
        )
        tf = label_box.text_frame
        p = tf.add_paragraph()
        p.text = metric.get("label", "")
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_SCHEME["gray"]

        # 数值
        val_box = slide.shapes.add_textbox(
            x + Inches(0.15), y + Inches(0.4), card_width - Inches(0.3), Inches(0.5)
        )
        tf = val_box.text_frame
        p = tf.add_paragraph()
        p.text = str(metric.get("value", ""))
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = COLOR_SCHEME["primary"]

        # 变化
        change = metric.get("change", "")
        change_box = slide.shapes.add_textbox(
            x + Inches(0.15), y + Inches(1.0), card_width - Inches(0.3), Inches(0.3)
        )
        tf = change_box.text_frame
        p = tf.add_paragraph()
        p.text = change
        p.font.size = Pt(10)
        if change.startswith("+"):
            p.font.color.rgb = RGBColor(0, 128, 0)
        elif change.startswith("-"):
            p.font.color.rgb = RGBColor(192, 0, 0)
        else:
            p.font.color.rgb = COLOR_SCHEME["gray"]

    # 核心洞察
    insight_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(3.2), Inches(9), Inches(3.5)
    )
    tf = insight_box.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = "核心洞察"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]
    p.space_after = Pt(12)

    for insight in insights:
        p = tf.add_paragraph()
        p.text = f"  {chr(9654)} {insight}"
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_SCHEME["text"]
        p.space_after = Pt(8)
```

### 费用分析页

```python
def create_budget_analysis_slide(prs, title, budget_data, fee_ratio_data):
    """创建费用分析页"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.3), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.add_paragraph()
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]

    # 预算执行表格（左侧）
    headers = ["项目", "预算", "已执行", "执行率", "剩余"]
    num_rows = len(budget_data) + 1
    table_shape = slide.shapes.add_table(
        num_rows, 5, Inches(0.5), Inches(1.3), Inches(4.5), Inches(0.4) * num_rows
    )
    table = table_shape.table

    for col, h in enumerate(headers):
        cell = table.cell(0, col)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_SCHEME["primary"]
        for p in cell.text_frame.paragraphs:
            p.font.color.rgb = COLOR_SCHEME["white"]
            p.font.bold = True
            p.font.size = Pt(9)
            p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(budget_data, 1):
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = str(val)
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(9)
                p.alignment = PP_ALIGN.CENTER

    # 费效比分析（右侧）
    ratio_box = slide.shapes.add_textbox(
        Inches(5.5), Inches(1.3), Inches(4), Inches(5)
    )
    tf = ratio_box.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = "费效比分析"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_SCHEME["primary"]
    p.space_after = Pt(12)

    for item in fee_ratio_data:
        p = tf.add_paragraph()
        p.text = f"  {item.get('label', '')}: {item.get('value', '')}"
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_SCHEME["text"]
        p.space_after = Pt(6)
```

### 完整示例：生成市场分析报告

```python
def generate_market_report(data, output_path):
    """生成完整的市场推广PPT"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # 封面
    create_cover_page(
        prs,
        title=data.get("title", "市场推广分析报告"),
        subtitle=data.get("subtitle", ""),
        date=data.get("date"),
        presenter=data.get("presenter"),
        dept=data.get("dept"),
    )

    # 目录
    create_toc_slide(prs, data.get("sections", []))

    # 市场分析
    create_market_analysis_slide(
        prs,
        "市场环境概览",
        data.get("market_metrics", []),
        data.get("market_insights", []),
    )

    # 竞品对标（使用表格格式）
    if data.get("competitor_data"):
        headers = ["品牌", "区域", "份额", "同比变化", "费用投入", "综合评价"]
        create_table_slide(prs, "竞品对标分析", headers, data["competitor_data"])

    # 费用分析
    if data.get("budget_data"):
        create_budget_analysis_slide(
            prs,
            "市场费用执行报告",
            data["budget_data"],
            data.get("fee_ratio_data", []),
        )

    # 策略规划
    if data.get("strategies"):
        headers = ["策略方向", "具体措施", "时间节点", "预期效果", "责任人"]
        create_table_slide(prs, "市场策略规划", headers, data["strategies"])

    # 总结
    slides_count = len(prs.slides)
    # (总结页实现略，参考 xinmeiti 版本)

    prs.save(output_path)
    return output_path
```

## 使用方式

在 Agent 指令中调用：

```
使用 ppt-generation 技能生成 [类型] 市场PPT:
- 类型: market_analysis / campaign_plan / budget_report / annual_plan / brand_strategy
- 数据: [提供具体数据]

生成脚本参考 scripts/make_ppt.py
```
