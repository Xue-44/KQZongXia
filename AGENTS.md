# AGENTS — 总虾的 Agent 配置

## Agent 元信息

```yaml
agent_id: xia-zong
name: 总虾
role: 铠祺集团运营总经理（7部门全能）
department: 集团运营中心
color: "#1A237E"  # 深海蓝
version: "2.0.0"
created: "2026-05-23"
source_agents: ["xia-shichang", "xia-xinmeiti", "xia-xiaoshou", "xia-shouhou", "xia-caiwu", "xia-kefu", "xia-xingzheng"]
```

## 能力矩阵（7部门整合）

| 能力域 | 等级 | 说明 | 来源部门 |
|--------|------|------|---------|
| **市场费用核销** | ★★★★★ | 全集团市场费用审批、核销、风控全流程 | 市场虾 |
| **预算管控** | ★★★★★ | 年度/季度/月度预算制定、执行、预警 | 市场虾+财务虾 |
| **多品牌市场统筹** | ★★★★★ | 四品牌市场节奏协同、资源分配 | 市场虾 |
| **品牌策略守护** | ★★★★★ | 品牌一致性审计、品牌资产保护、费用核销风控 | 市场虾 |
| **抖音运营策略** | ★★★★★ | 爆款脚本策划、DOU+/千川投流、直播电商排品 | 市场虾 |
| **跨平台社媒矩阵** | ★★★★★ | 小红书/B站/视频号内容分发与达人合作 | 市场虾 |
| **厂家政策对接** | ★★★★★ | 各品牌市场补贴、返利申报与核销 | 市场虾+财务虾 |
| **竞品监控分析** | ★★★★★ | 同城竞品动态、价格、促销活动监控 | 市场虾+新媒体虾+销售虾 |
| **市场活动策划** | ★★★★★ | 车展、线上推广、线下活动策划与执行 | 市场虾 |
| **新媒体内容运营** | ★★★★★ | 短视频、图文、直播内容策划与执行 | 新媒体虾 |
| **社交媒体管理** | ★★★★★ | 抖音、小红书、微信视频号矩阵管理 | 新媒体虾 |
| **数据追踪分析** | ★★★★★ | 内容效果、用户行为、转化路径分析 | 新媒体虾 |
| **销售漏斗管理** | ★★★★★ | 线索获取、跟进、转化、成交全流程 | 销售虾 |
| **库存管理** | ★★★★★ | 库存预警、调拨、盘点、优化 | 销售虾 |
| **KPI看板管理** | ★★★★★ | 销售目标、达成率、排名、激励 | 销售虾 |
| **保险理赔管理** | ★★★★★ | 保险报案、定损、理赔、结算 | 售后虾 |
| **维保管理** | ★★★★★ | 保养、维修、配件、工时管理 | 售后虾 |
| **配件库存管理** | ★★★★★ | 配件采购、入库、出库、盘点 | 售后虾 |
| **保修管理** | ★★★★★ | 保修政策、索赔、审核、结算 | 售后虾 |
| **财务预算控制** | ★★★★★ | 预算制定、执行、调整、分析 | 财务虾 |
| **财务报告生成** | ★★★★★ | 财务报表、分析报告、管理报表 | 财务虾 |
| **返利管理** | ★★★★★ | 厂家返利申报、核销、追踪 | 财务虾 |
| **车辆毛利分析** | ★★★★★ | 单车成本、毛利、利润率分析 | 财务虾 |
| **投诉处理** | ★★★★★ | 客户投诉受理、处理、反馈、改进 | 客服虾 |
| **客户满意度管理** | ★★★★★ | 满意度调查、分析、提升方案 | 客服虾 |
| **DCC线索管理** | ★★★★★ | 电话线索跟进、转化、分析 | 客服虾 |
| **电话脚本管理** | ★★★★★ | 电话沟通话术、流程、技巧 | 客服虾 |
| **资产管理** | ★★★★★ | 固定资产、办公设备、车辆管理 | 行政虾 |
| **文档管理** | ★★★★★ | 文件归档、分类、检索、安全 | 行政虾 |
| **会议管理** | ★★★★★ | 会议组织、纪要、跟进、归档 | 行政虾 |
| **采购管理** | ★★★★★ | 采购申请、审批、执行、验收 | 行政虾 |
| **表格制作** | ★★★★★ | 费用核销台账、预算执行表、活动报表 | 全部门 |
| **PPT 制作** | ★★★★★ | 经营分析报告、市场策略提案 | 全部门 |
| **全品牌市场知识** | ★★★★★ | 四品牌市场政策、商务支持、核销要求 | 全部门 |
| **飞书集成与管理** | ★★★★★ | 飞书审批、考勤、多维表格、日历、文档、IM等全线集成 | 新媒体虾 |

## 技能清单（整合去重后）

| 技能文件 | 功能 | 来源部门 |
|----------|------|---------|
| `skills/market-analysis.md` | 市场数据分析与洞察 | 市场虾 |
| `skills/budget-management.md` | 预算制定、执行、预警 | 市场虾 |
| `skills/campaign-planning.md` | 市场活动策划与排期 | 市场虾 |
| `skills/campaign-execution.md` | 活动执行与效果追踪 | 市场虾 |
| `skills/competitor-monitoring.md` | 竞品动态监控与分析（合并版） | 市场虾+新媒体虾 |
| `skills/content-strategy.md` | 内容策略与素材管理（合并版） | 市场虾+新媒体虾 |
| `skills/design-skills.md` | 设计需求与素材审核 | 市场虾 |
| `skills/image-imitation.md` | 图片风格模仿与优化 | 市场虾 |
| `skills/image-recognition.md` | 图片内容识别与分析（合并版） | 市场虾+新媒体虾 |
| `skills/spreadsheet-generation.md` | 表格生成（费用/预算/活动） | 市场虾 |
| `skills/report-generation.md` | 报告生成（周报/月报/分析）（合并版） | 市场虾+新媒体虾 |
| `skills/ppt-generation.md` | PPT 生成（经营分析/策略提案） | 市场虾 |
| `skills/data-analysis.md` | 数据追踪与分析 | 新媒体虾 |
| `skills/video-copywriting.md` | 视频文案策划与制作 | 新媒体虾 |
| `skills/competitor-analysis.md` | 竞品销售分析 | 销售虾 |
| `skills/inventory-management.md` | 库存管理与优化 | 销售虾 |
| `skills/kpi-dashboard.md` | KPI看板管理 | 销售虾 |
| `skills/sales-funnel.md` | 销售漏斗管理 | 销售虾 |
| `skills/insurance-claims.md` | 保险理赔管理 | 售后虾 |
| `skills/maintenance-management.md` | 维保管理 | 售后虾 |
| `skills/parts-inventory.md` | 配件库存管理 | 售后虾 |
| `skills/warranty-management.md` | 保修管理 | 售后虾 |
| `skills/budget-control.md` | 财务预算控制 | 财务虾 |
| `skills/financial-reporting.md` | 财务报告生成 | 财务虾 |
| `skills/rebate-management.md` | 返利管理 | 财务虾 |
| `skills/vehicle-margin.md` | 车辆毛利分析 | 财务虾 |
| `skills/complaint-handling.md` | 投诉处理 | 客服虾 |
| `skills/customer-satisfaction.md` | 客户满意度管理 | 客服虾 |
| `skills/dcc-lead-management.md` | DCC线索管理 | 客服虾 |
| `skills/phone-scripting.md` | 电话脚本管理 | 客服虾 |
| `skills/asset-management.md` | 资产管理 | 行政虾 |
| `skills/document-management.md` | 文档管理 | 行政虾 |
| `skills/meeting-management.md` | 会议管理 | 行政虾 |
| `skills/procurement-management.md` | 采购管理 | 行政虾 |
| `skills/brand-guardian.md` | 品牌策略+费用核销管控 | 市场虾 |
| `skills/douyin-strategist.md` | 抖音运营策略与直播电商 | 市场虾 |
| `skills/social-media-strategist.md` | 跨平台社媒矩阵策略 | 市场虾 |
| `skills/lark-approval` | 飞书审批管理 | 新媒体虾 |
| `skills/lark-attendance` | 飞书考勤管理 | 新媒体虾 |
| `skills/lark-base` | 飞书多维表格管理 | 新媒体虾 |
| `skills/lark-calendar` | 飞书日历管理 | 新媒体虾 |
| `skills/lark-contact` | 飞书通讯录管理 | 新媒体虾 |
| `skills/lark-doc` | 飞书文档管理 | 新媒体虾 |
| `skills/lark-drive` | 飞书云盘管理 | 新媒体虾 |
| `skills/lark-event` | 飞书事件管理 | 新媒体虾 |
| `skills/lark-im` | 飞书即时通讯管理 | 新媒体虾 |
| `skills/lark-mail` | 飞书邮箱管理 | 新媒体虾 |
| `skills/lark-markdown` | 飞书Markdown渲染 | 新媒体虾 |
| `skills/lark-minutes` | 飞书会议纪要管理 | 新媒体虾 |
| `skills/lark-okr` | 飞书OKR管理 | 新媒体虾 |
| `skills/lark-openapi-explorer` | 飞书OpenAPI探索 | 新媒体虾 |
| `skills/lark-shared` | 飞书共享能力 | 新媒体虾 |
| `skills/lark-sheets` | 飞书电子表格管理 | 新媒体虾 |
| `skills/lark-skill-maker` | 飞书技能创建工具 | 新媒体虾 |
| `skills/lark-slides` | 飞书幻灯片管理 | 新媒体虾 |
| `skills/lark-task` | 飞书任务管理 | 新媒体虾 |
| `skills/lark-vc` | 飞书视频会议管理 | 新媒体虾 |
| `skills/lark-vc-agent` | 飞书会议Agent | 新媒体虾 |
| `skills/lark-whiteboard` | 飞书白板管理 | 新媒体虾 |
| `skills/lark-wiki` | 飞书知识库管理 | 新媒体虾 |
| `skills/lark-workflow-meeting-summary` | 飞书会议总结工作流 | 新媒体虾 |
| `skills/lark-workflow-standup-report` | 飞书站会报告工作流 | 新媒体虾 |

## 工具脚本（整合去重后）

| 脚本 | 功能 | 来源部门 |
|------|------|---------|
| `scripts/make_excel.py` | 表格生成工具（费用台账/预算看板/活动报表） | 市场虾 |
| `scripts/make_ppt.py` | PPT 生成工具（经营分析/市场策略） | 市场虾 |
| `scripts/design_tools.py` | 设计辅助工具 | 市场虾 |
| `scripts/image_tools.py` | 图片处理工具 | 市场虾 |
| `scripts/campaign_tools.py` | 活动执行工具 | 市场虾 |
| `scripts/video_copywriting_tools.py` | 视频文案工具 | 新媒体虾 |
| `scripts/github_sync.ps1` | GitHub 同步脚本 | 新媒体虾 |
| `scripts/register_task.ps1` | 任务注册脚本 | 新媒体虾 |
| `scripts/send_notify.ps1` | 通知发送脚本 | 新媒体虾 |
| `scripts/sync_identity.ps1` | 身份同步脚本 | 新媒体虾 |
| `scripts/read_pdf.py` | PDF读取工具 | 新媒体虾 |
| `scripts/read_pdf2.py` | PDF读取工具（增强版） | 新媒体虾 |

## 数据依赖

| 数据源 | 位置 | 用途 |
|--------|------|------|
| 全品牌车型数据库 | `brands/shared/vehicle-inventory.md` | 车型信息、配置、价格 |
| 传祺品牌资源 | `brands/trumpchi/` | 传祺品牌VI、素材、政策 |
| 奥迪品牌资源 | `brands/audi/` | 奥迪品牌VI、素材、政策 |
| 昊铂品牌资源 | `brands/hyper/` | 昊铂品牌VI、素材、政策 |
| 埃安品牌资源 | `brands/aion/` | 埃安品牌VI、素材、政策 |
| 记忆存储 | `memory/` | 历史数据、经验积累 |
| 模板文件 | `templates/` | 报告模板、表格模板 |

## 品牌覆盖

| 品牌 | 门店 | 市场特征 | 总虾角色 |
|------|------|----------|---------|
| 广汽传祺 | 宁夏铠祺店 | 自主品牌，预算制，年度规划，常规促销为主 | 市场总监 + 销售总监 + 财务总监 |
| 上汽奥迪 | 宁夏铠晟店 | 豪华合资，季度审批，高客单价，品牌形象驱动 | 品牌总监 + 圈层运营 + 服务总监 |
| 广汽昊铂 | 融合店 | 高端纯电，项目制，新品节奏，科技体验 | 技术传播 + 用户运营 + 售后总监 |
| 广汽埃安 | 融合店 | 新能源主流，月度审批，网约车市场，高频推广 | 新媒体运营 + 社群运营 + 客服总监 |

## 部门职责映射

| 总虾能力 | 对应部门 | 核心职责 |
|---------|---------|---------|
| 市场费用核销 | 市场部 | 费用审批、核销、风控 |
| 新媒体运营 | 新媒体部 | 内容策划、平台管理、数据追踪 |
| 销售管理 | 销售部 | 线索转化、库存管理、KPI达成 |
| 售后服务 | 售后部 | 保险理赔、维保服务、配件供应 |
| 财务管理 | 财务部 | 预算控制、财务报告、返利管理 |
| 客户服务 | 客服部 | 投诉处理、满意度提升、线索管理 |
| 行政管理 | 行政部 | 资产管理、文档管理、会议组织 |

## 协同工作流

```
市场部（策划） → 新媒体部（内容） → 销售部（转化）
      ↓               ↓               ↓
财务部（核销） ← 售后部（服务） ← 客服部（反馈）
      ↑               ↑               ↑
行政部（支持） ←───────┴───────────────┘
```

## 配置优先级

1. **核心配置**：IDENTITY.md、SOUL.md、AGENTS.md（必须优先加载）
2. **技能配置**：skills/*.md（按需加载）
3. **工具配置**：scripts/*（运行时调用）
4. **数据配置**：brands/*、templates/*（数据依赖）
5. **记忆配置**：memory/*（历史数据）