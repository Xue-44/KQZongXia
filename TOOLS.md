# 工具与脚本清单 — 总虾

## 工具分类

总虾整合了7个部门的所有工具脚本，分为以下5大类：

### 1. 数据生成类工具
用于生成各种格式的数据报告、表格、演示文稿

### 2. 内容创作类工具
用于内容策划、设计、视频制作等创意工作

### 3. 流程自动化工具
用于自动化重复性工作流程

### 4. 数据分析类工具
用于数据清洗、分析、可视化

### 5. 系统集成工具
用于与外部系统集成和数据同步

## 工具清单

### 1. 数据生成类工具

| 工具文件 | 功能描述 | 来源部门 | 使用场景 | 输入 | 输出 |
|----------|---------|---------|---------|------|------|
| `scripts/make_excel.py` | 表格生成工具 | 市场虾 | 费用台账、预算看板、活动报表 | 数据字典 | Excel文件 |
| `scripts/make_ppt.py` | PPT生成工具 | 市场虾 | 经营分析报告、市场策略提案 | 内容大纲 | PPTX文件 |

#### make_excel.py 详细说明
```python
# 主要功能
1. 费用核销台账生成
2. 预算执行表生成
3. 市场活动报表生成
4. 销售数据报表生成
5. 财务数据报表生成

# 支持模板
- 费用台账模板（含公式校验）
- 预算执行模板（含进度条）
- 活动报表模板（含ROI计算）
- 销售日报模板（含环比对比）
- 财务月报模板（含图表）

# 调用方式
python make_excel.py --type expense --data data.json --output 费用台账.xlsx
```

#### make_ppt.py 详细说明
```python
# 主要功能
1. 经营分析报告生成
2. 市场策略提案生成
3. 竞品分析报告生成
4. 月度总结报告生成
5. 专项活动复盘生成

# 支持模板
- 传祺品牌模板（蓝白配色）
- 奥迪品牌模板（黑白金配色）
- 昊铂品牌模板（紫黑配色）
- 埃安品牌模板（绿色系）
- 集团通用模板（深海蓝）

# 调用方式
python make_ppt.py --type monthly --brand trumpchi --data data.json --output 月度报告.pptx
```

### 2. 内容创作类工具

| 工具文件 | 功能描述 | 来源部门 | 使用场景 | 输入 | 输出 |
|----------|---------|---------|---------|------|------|
| `scripts/design_tools.py` | 设计辅助工具 | 市场虾 | 海报设计、物料设计、广告设计 | 设计需求 | 设计稿/建议 |
| `scripts/image_tools.py` | 图片处理工具 | 市场虾 | 图片优化、尺寸调整、格式转换 | 原始图片 | 处理后图片 |
| `scripts/video_copywriting_tools.py` | 视频文案工具 | 新媒体虾 | 短视频脚本、直播话术、口播文案 | 产品信息 | 视频脚本 |

#### design_tools.py 详细说明
```python
# 主要功能
1. 海报设计建议生成
2. 物料设计规范检查
3. 广告设计合规检查
4. 品牌VI一致性检查
5. 设计稿质量评估

# 支持检查项
- 尺寸规范检查
- 色彩规范检查
- 字体规范检查
- Logo使用规范
- 文案合规检查

# 调用方式
python design_tools.py --check compliance --image ad.jpg --brand trumpchi
```

#### image_tools.py 详细说明
```python
# 主要功能
1. 图片尺寸批量调整
2. 图片格式批量转换
3. 图片质量优化
4. 图片水印添加
5. 图片批量重命名

# 支持格式
- JPG/JPEG
- PNG
- WebP
- GIF
- BMP

# 调用方式
python image_tools.py --resize 1080x1920 --format webp --input images/ --output optimized/
```

#### video_copywriting_tools.py 详细说明
```python
# 主要功能
1. 短视频脚本生成
2. 直播话术生成
3. 口播文案生成
4. 视频标题建议
5. 话题标签建议

# 支持平台
- 抖音
- 快手
- 小红书
- 微信视频号
- B站

# 调用方式
python video_copywriting_tools.py --platform douyin --product "传祺GS8" --style "科技感" --output script.md
```

### 3. 流程自动化工具

| 工具文件 | 功能描述 | 来源部门 | 使用场景 | 输入 | 输出 |
|----------|---------|---------|---------|------|------|
| `scripts/campaign_tools.py` | 活动执行工具 | 市场虾 | 活动策划、执行、跟踪、复盘 | 活动计划 | 执行报告 |
| `scripts/github_sync.ps1` | GitHub同步脚本 | 新媒体虾 | 代码/文档同步到GitHub | 本地文件 | GitHub仓库 |
| `scripts/register_task.ps1` | 任务注册脚本 | 新媒体虾 | 自动化任务注册到系统 | 任务配置 | 任务ID |
| `scripts/send_notify.ps1` | 通知发送脚本 | 新媒体虾 | 多渠道通知发送 | 通知内容 | 发送状态 |
| `scripts/sync_identity.ps1` | 身份同步脚本 | 新媒体虾 | 多系统身份同步 | 身份信息 | 同步状态 |

#### campaign_tools.py 详细说明
```python
# 主要功能
1. 活动策划模板生成
2. 活动预算计算
3. 活动进度跟踪
4. 活动效果评估
5. 活动复盘报告

# 活动类型
- 新车上市活动
- 促销团购活动
- 品牌体验活动
- 车展活动
- 车主活动

# 调用方式
python campaign_tools.py --type launch --product "昊铂GT" --budget 50000 --output campaign_plan.md
```

#### github_sync.ps1 详细说明
```powershell
# 主要功能
1. 自动提交代码到GitHub
2. 自动同步文档到GitHub
3. 自动处理冲突
4. 自动生成提交信息
5. 自动备份重要文件

# 使用方式
.\github_sync.ps1 -RepoUrl "https://github.com/username/repo" -Branch "main" -CommitMessage "更新内容"
```

#### register_task.ps1 详细说明
```powershell
# 主要功能
1. 注册定时任务到Windows任务计划
2. 注册定时任务到cron（Linux）
3. 任务状态监控
4. 任务日志记录
5. 任务异常告警

# 使用方式
.\register_task.ps1 -TaskName "每日数据同步" -ScriptPath "sync_data.ps1" -Schedule "Daily" -Time "09:00"
```

#### send_notify.ps1 详细说明
```powershell
# 主要功能
1. 飞书消息发送
2. 微信消息发送
3. 邮件发送
4. 短信发送
5. 电话通知

# 支持渠道
- 飞书（Webhook/机器人）
- 微信（企业微信）
- 邮件（SMTP）
- 短信（阿里云/腾讯云）
- 电话（语音通知）

# 使用方式
.\send_notify.ps1 -Channel "Feishu" -Message "库存预警：传祺GS8库存深度>2.5" -To "sales-team"
```

#### sync_identity.ps1 详细说明
```powershell
# 主要功能
1. 用户身份信息同步
2. 权限同步
3. 组织架构同步
4. 单点登录配置
5. 身份验证集成

# 支持系统
- 飞书
- 企业微信
- OA系统
- CRM系统
- 财务系统

# 使用方式
.\sync_identity.ps1 -Source "Feishu" -Target "CRM" -UserGroup "sales"
```

### 4. 数据分析类工具

| 工具文件 | 功能描述 | 来源部门 | 使用场景 | 输入 | 输出 |
|----------|---------|---------|---------|------|------|
| `scripts/data_analysis_tools.py` | 数据分析工具 | 全部门 | 数据清洗、分析、可视化 | 原始数据 | 分析报告 |

（注：此工具需要根据具体需求开发，目前为预留位置）

### 5. 系统集成工具

| 工具文件 | 功能描述 | 来源部门 | 使用场景 | 输入 | 输出 |
|----------|---------|---------|---------|------|------|
| `scripts/api_integration.py` | API集成工具 | 全部门 | 与外部系统API集成 | API配置 | 集成状态 |

（注：此工具需要根据具体需求开发，目前为预留位置）

## 工具使用规范

### 1. 调用规范
```python
# Python工具调用规范
1. 使用绝对路径调用
2. 提供完整的参数说明
3. 处理异常情况
4. 记录执行日志
5. 返回结构化结果

# PowerShell工具调用规范
1. 使用管理员权限（如需要）
2. 设置执行策略
3. 处理错误情况
4. 记录执行日志
5. 返回退出代码
```

### 2. 参数规范
```python
# 通用参数
--help/-h: 显示帮助信息
--version/-v: 显示版本信息
--verbose: 详细输出模式
--quiet: 安静模式
--log: 日志文件路径

# 数据参数
--data: 数据文件路径
--output: 输出文件路径
--format: 输出格式
--encoding: 文件编码

# 品牌参数
--brand: 品牌名称（trumpchi/audi/hyper/aion）
--template: 模板名称
--color: 配色方案
```

### 3. 错误处理规范
```python
# 错误代码定义
0: 成功
1: 参数错误
2: 文件错误
3: 网络错误
4: 权限错误
5: 系统错误
6: 业务逻辑错误

# 错误信息格式
{
  "code": 错误代码,
  "message": "错误描述",
  "detail": "详细错误信息",
  "suggestion": "解决建议"
}
```

### 4. 日志规范
```python
# 日志级别
DEBUG: 调试信息
INFO: 一般信息
WARNING: 警告信息
ERROR: 错误信息
CRITICAL: 严重错误

# 日志格式
[时间] [级别] [模块] [函数] - 消息内容
示例: [2026-05-23 10:30:00] [INFO] [make_excel] [generate] - 开始生成费用台账
```

## 工具开发规范

### 1. 代码规范
- 遵循PEP 8规范（Python）
- 遵循PowerShell最佳实践
- 添加详细的文档字符串
- 添加类型注解（Python）
- 添加单元测试

### 2. 文档规范
每个工具必须包含以下文档：
- README.md：工具概述、安装说明、使用示例
- API.md：API接口说明（如有）
- CHANGELOG.md：版本更新记录
- LICENSE：许可证信息

### 3. 测试规范
- 单元测试覆盖核心功能
- 集成测试覆盖端到端流程
- 性能测试确保工具效率
- 安全测试确保工具安全

### 4. 发布规范
- 版本号遵循语义化版本规范
- 发布前进行完整测试
- 更新文档和示例
- 发布到内部工具仓库

## 工具维护计划

### 1. 日常维护
- 每日检查工具运行状态
- 每日备份工具配置
- 每日清理工具日志

### 2. 每周维护
- 每周更新工具依赖
- 每周检查工具安全
- 每周优化工具性能

### 3. 每月维护
- 每月进行工具审计
- 每月更新工具文档
- 每月培训工具使用

### 4. 每季度维护
- 每季度评估工具效果
- 每季度优化工具流程
- 每季度开发新工具

## 工具权限管理

### 1. 权限分级
| 权限级别 | 可执行操作 | 适用人员 |
|---------|-----------|---------|
| 管理员 | 所有操作 | 系统管理员 |
| 开发者 | 开发、测试、部署 | 工具开发者 |
| 使用者 | 正常使用 | 普通用户 |
| 只读者 | 查看、下载 | 审计人员 |

### 2. 权限控制
- 文件系统权限控制
- 网络访问权限控制
- 数据库访问权限控制
- API调用权限控制

### 3. 审计日志
- 记录所有工具执行
- 记录所有参数输入
- 记录所有输出结果
- 记录所有错误信息

## 工具部署环境

### 1. 开发环境
- Python 3.9+
- PowerShell 7+
- Git
- Visual Studio Code

### 2. 测试环境
- 与生产环境一致
- 独立数据库
- 独立网络
- 自动化测试框架

### 3. 生产环境
- 高可用部署
- 负载均衡
- 数据备份
- 监控告警

### 4. 依赖管理
```python
# requirements.txt
# Python依赖
pandas>=1.5.0
openpyxl>=3.1.0
python-pptx>=0.6.21
Pillow>=9.5.0
opencv-python>=4.7.0

# PowerShell模块
Import-Module PSScriptAnalyzer
Import-Module PSReadLine
Import-Module Pester
```