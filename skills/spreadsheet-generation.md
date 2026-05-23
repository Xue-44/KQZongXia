# 市场推广表格制作技能

## 技能定位
本技能用于生成市场推广相关的数据表格，面向集团和各品牌的市场管理人员，支持市场费用明细、预算追踪、活动评估、线索转化、竞品监测等多种场景。

## 支持场景
| 场景 | 说明 | 使用频率 |
|------|------|---------|
| 市场费用明细表 | 按品牌/区域/类型分类的费用明细 | 每月 |
| 预算执行追踪表 | 年度预算执行进度追踪 | 持续 |
| 活动效果评估表 | 单场/系列活动ROI评估 | 活动后 |
| 线索转化追踪表 | 线索获取到成交全链路追踪 | 每周 |
| 竞品动态监测表 | 竞品市场活动与费用动态记录 | 每月 |

## 表格规范

### 表头样式
- 背景色: 集团深蓝 (#1F3864)，白色加粗文字
- 行高: 28pt
- 对齐: 水平居中，垂直居中
- 字体: 微软雅黑 Bold，11pt

### 数字格式
- 金额: #,##0.00，千分位两位小数
- 百分比: 0.0%，一位小数
- 整数: #,##0，千分位无小数
- 日期: YYYY-MM-DD

### 条件格式
- 预算执行率 > 90%: 黄色背景警告
- 预算执行率 > 100%: 红色背景超预算告警
- ROI > 3: 绿色标记高效活动
- ROI < 1: 红色标记低效活动
- 核销超期: 红色字体加粗

### 结构化规范
- 首行冻结
- 筛选器开启（AutoFilter）
- 关键列分组（Group）
- 汇总行加粗边框加双线底部

## Python 代码模板 (openpyxl)

### 基础配置

```python
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side, NamedStyle, numbers
)
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime

# 集团配色
HEADER_FILL = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
HEADER_FONT = Font(name="微软雅黑", bold=True, color="FFFFFF", size=11)
ALT_ROW_FILL = PatternFill(start_color="DDEBF7", end_color="DDEBF7", fill_type="solid")
TOTAL_FILL = PatternFill(start_color="BDD7EE", end_color="BDD7EE", fill_type="solid")

# 告警色
WARNING_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
OVER_BUDGET_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
GOOD_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

# 数字格式
FMT_MONEY = '#,##0.00'
FMT_PCT = '0.0%'
FMT_INT = '#,##0'
FMT_DATE = 'YYYY-MM-DD'
```

### 通用工具函数

```python
def create_workbook(sheet_name="数据表"):
    """创建标准Workbook"""
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name
    return wb, ws


def write_headers(ws, headers, row=1):
    """写入表头"""
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[row].height = 30


def write_data(ws, data_rows, start_row=2, alt_fill=True):
    """写入数据行"""
    for row_idx, row_data in enumerate(data_rows):
        current_row = start_row + row_idx
        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=current_row, column=col_idx, value=value)
            cell.border = thin_border
            cell.alignment = Alignment(vertical="center")
            if alt_fill and row_idx % 2 == 1:
                cell.fill = ALT_ROW_FILL


def apply_number_format(ws, col_letter, start_row, end_row, fmt):
    """应用数字格式"""
    for row in range(start_row, end_row + 1):
        ws[f"{col_letter}{row}"].number_format = fmt


def setup_worksheet(ws, auto_filter=True, freeze=True):
    """工作表基础设置"""
    if auto_filter and ws.max_row > 1:
        ws.auto_filter.ref = f"A1:{get_column_letter(ws.max_column)}{ws.max_row}"
    if freeze:
        ws.freeze_panes = "A2"


def auto_fit_columns(ws, min_width=10, max_width=45):
    """自适应列宽"""
    for col in ws.columns:
        column = col[0].column_letter
        max_len = 0
        for cell in col:
            if cell.value:
                # 中文字符宽度按2计算
                text = str(cell.value)
                length = sum(2 if ord(c) > 127 else 1 for c in text)
                max_len = max(max_len, length)
        ws.column_dimensions[column].width = min(max(max_len + 4, min_width), max_width)
```

### 市场费用明细表

```python
def generate_expense_detail(data, output_path):
    """生成市场费用明细表
    data: {
        "month": "2026-05",
        "rows": [[品牌, 区域, 费用类型, 预算金额, 实际金额, 执行率, 核销状态, 备注], ...]
    }
    """
    wb, ws = create_workbook(f"{data.get('month', '')}市场费用明细")

    headers = [
        "品牌", "区域", "费用类型", "预算金额",
        "实际执行", "执行率", "核销状态", "申请日期", "备注"
    ]
    write_headers(ws, headers)
    write_data(ws, data["rows"])

    last_row = len(data["rows"]) + 1

    # 数字格式
    apply_number_format(ws, "D", 2, last_row, FMT_MONEY)
    apply_number_format(ws, "E", 2, last_row, FMT_MONEY)
    apply_number_format(ws, "F", 2, last_row, FMT_PCT)

    # 条件格式：执行率告警
    rate_col = "F"
    ws.conditional_formatting.add(
        f"{rate_col}2:{rate_col}{last_row}",
        CellIsRule(operator="greaterThan", formula=["1"],
                  fill=OVER_BUDGET_FILL, font=Font(bold=True, color="9C0006"))
    )
    ws.conditional_formatting.add(
        f"{rate_col}2:{rate_col}{last_row}",
        CellIsRule(operator="between", formula=["0.9", "1"],
                  fill=WARNING_FILL, font=Font(bold=True))
    )

    # 核销状态数据验证
    dv = DataValidation(
        type="list",
        formula1='"已核销,待核销,核销中,超期未核"',
        allow_blank=True
    )
    dv.add(f"G2:G{last_row}")
    ws.add_data_validation(dv)

    setup_worksheet(ws)
    auto_fit_columns(ws)

    wb.save(output_path)
    return output_path
```

### 预算执行追踪表

```python
def generate_budget_tracker(data, output_path):
    """生成预算执行追踪表"""
    wb, ws = create_workbook(f"{data.get('year', '')}年预算执行追踪")

    headers = [
        "月份", "年度预算", "累计预算", "当月执行",
        "累计执行", "累计执行率", "剩余预算", "剩余占比", "预警"
    ]
    write_headers(ws, headers)
    write_data(ws, data["rows"])

    last_row = len(data["rows"]) + 1

    # 数字格式
    for col_letter in ["B", "C", "D", "E", "G"]:
        apply_number_format(ws, col_letter, 2, last_row, FMT_MONEY)
    apply_number_format(ws, "F", 2, last_row, FMT_PCT)
    apply_number_format(ws, "H", 2, last_row, FMT_PCT)

    # 条件格式：累计执行率
    ws.conditional_formatting.add(
        f"F2:F{last_row}",
        CellIsRule(operator="greaterThan", formula=["1"],
                  fill=OVER_BUDGET_FILL, font=Font(bold=True, color="9C0006"))
    )
    ws.conditional_formatting.add(
        f"F2:F{last_row}",
        CellIsRule(operator="between", formula=["0.85", "1"],
                  fill=WARNING_FILL, font=Font(bold=True))
    )

    # 剩余占比告警：低于15%
    ws.conditional_formatting.add(
        f"H2:H{last_row}",
        CellIsRule(operator="lessThan", formula=["0.15"],
                  fill=OVER_BUDGET_FILL, font=Font(bold=True, color="9C0006"))
    )

    setup_worksheet(ws)
    auto_fit_columns(ws)

    wb.save(output_path)
    return output_path
```

### 活动效果评估表

```python
def generate_campaign_evaluation(data, output_path):
    """生成活动效果评估表"""
    wb, ws = create_workbook("活动效果评估")

    headers = [
        "活动名称", "品牌", "活动日期", "预算", "实际花费",
        "曝光量", "互动量", "线索数", "成交数", "CPL",
        "ROI", "目标达成率", "综合评分", "备注"
    ]
    write_headers(ws, headers)
    write_data(ws, data["rows"])

    last_row = len(data["rows"]) + 1

    # 数字格式
    apply_number_format(ws, "D", 2, last_row, FMT_MONEY)
    apply_number_format(ws, "E", 2, last_row, FMT_MONEY)
    apply_number_format(ws, "F", 2, last_row, FMT_INT)
    apply_number_format(ws, "G", 2, last_row, FMT_INT)
    apply_number_format(ws, "H", 2, last_row, FMT_INT)
    apply_number_format(ws, "I", 2, last_row, FMT_INT)
    apply_number_format(ws, "J", 2, last_row, FMT_MONEY)
    apply_number_format(ws, "K", 2, last_row, "0.00")
    apply_number_format(ws, "L", 2, last_row, FMT_PCT)

    # 条件格式
    # ROI >= 3 高效绿色
    ws.conditional_formatting.add(
        f"K2:K{last_row}",
        CellIsRule(operator="greaterThanOrEqual", formula=["3"],
                  fill=GOOD_FILL, font=Font(bold=True, color="006100"))
    )
    # ROI < 1 低效红色
    ws.conditional_formatting.add(
        f"K2:K{last_row}",
        CellIsRule(operator="lessThan", formula=["1"],
                  fill=OVER_BUDGET_FILL, font=Font(bold=True, color="9C0006"))
    )
    # 目标达成率 >= 100% 绿色
    ws.conditional_formatting.add(
        f"L2:L{last_row}",
        CellIsRule(operator="greaterThanOrEqual", formula=["1"],
                  fill=GOOD_FILL, font=Font(bold=True, color="006100"))
    )

    setup_worksheet(ws)
    auto_fit_columns(ws)

    wb.save(output_path)
    return output_path
```

### 线索转化追踪表

```python
def generate_lead_tracker(data, output_path):
    """生成线索转化追踪表"""
    wb, ws = create_workbook("线索转化追踪")

    headers = [
        "线索ID", "来源渠道", "品牌", "获取日期", "线索等级",
        "首次跟进日期", "跟进次数", "试驾日期", "成交日期",
        "转化周期(天)", "成交金额", "跟进销售", "状态"
    ]
    write_headers(ws, headers)
    write_data(ws, data["rows"])

    last_row = len(data["rows"]) + 1

    apply_number_format(ws, "K", 2, last_row, FMT_INT)
    apply_number_format(ws, "L", 2, last_row, FMT_MONEY)

    # 状态数据验证
    dv = DataValidation(
        type="list",
        formula1='"待跟进,跟进中,已试驾,已成交,已战败"',
        allow_blank=True
    )
    dv.add(f"M2:M{last_row}")
    ws.add_data_validation(dv)

    # 转化周期 <= 7天 绿色（高效转化）
    ws.conditional_formatting.add(
        f"K2:K{last_row}",
        CellIsRule(operator="lessThanOrEqual", formula=["7"],
                  fill=GOOD_FILL, font=Font(bold=True, color="006100"))
    )

    setup_worksheet(ws)
    auto_fit_columns(ws)

    wb.save(output_path)
    return output_path
```

### 竞品动态监测表

```python
def generate_competitor_monitor(data, output_path):
    """生成竞品动态监测表"""
    wb, ws = create_workbook("竞品动态监测")

    headers = [
        "日期", "竞品品牌", "活动类型", "活动主题",
        "活动区域", "预估费用(万)", "活动亮点", "效果评估",
        "对我方影响", "应对建议", "记录人"
    ]
    write_headers(ws, headers)
    write_data(ws, data["rows"])

    last_row = len(data["rows"]) + 1

    apply_number_format(ws, "F", 2, last_row, FMT_MONEY)

    # 影响等级数据验证
    dv = DataValidation(
        type="list",
        formula1='"高,中,低"',
        allow_blank=True
    )
    dv.add(f"I2:I{last_row}")
    ws.add_data_validation(dv)

    setup_worksheet(ws)
    auto_fit_columns(ws)

    wb.save(output_path)
    return output_path
```

## 质量标准检查清单

### 数据质量
- [ ] 原始数据可追溯，口径一致
- [ ] 公式正确无误，无循环引用
- [ ] 金额单位标注清晰（元/万元）

### 专业性
- [ ] 集团配色一致，商务风格
- [ ] 数字格式统一规范
- [ ] 条件格式正确标示异常

### 可用性
- [ ] 冻结首行，开启筛选
- [ ] 列宽适配，打印区域设置
- [ ] 关键列有数据验证
- [ ] 敏感数据标注"内部"

## 使用方式

在 Agent 指令中调用：

```
使用 spreadsheet-generation 技能生成 [类型] 表格:
- 类型: expense_detail / budget_tracker / campaign_eval / lead_tracker / competitor_monitor
- 数据: [提供具体数据]

生成脚本参考 scripts/make_excel.py
```
