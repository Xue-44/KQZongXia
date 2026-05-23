# 记忆存储规范 — 总虾

## 记忆体系架构

总虾的记忆体系采用分层存储结构，确保历史数据、经验积累、最佳实践得到有效保存和快速检索。

### 1. 记忆分类

| 记忆类型 | 存储位置 | 保留周期 | 用途 |
|---------|---------|---------|------|
| **短期记忆** | `memory/short-term/` | 7天 | 临时数据、会话状态、当前任务 |
| **中期记忆** | `memory/medium-term/` | 30天 | 近期经验、临时决策、过程记录 |
| **长期记忆** | `memory/long-term/` | 永久 | 最佳实践、成功案例、失败教训 |
| **知识记忆** | `memory/knowledge/` | 永久 | 专业知识、流程规范、模板文件 |
| **数据记忆** | `memory/data/` | 按需 | 历史数据、统计报表、分析结果 |
| **人物记忆** | `memory/people/` | 永久 | 联系人、客户、团队成员信息 |
| **事件记忆** | `memory/events/` | 永久 | 重要事件、活动、会议记录 |

### 2. 记忆文件命名规范

```
{类型}_{日期}_{主题}_{版本}.md
示例：
- short-term_2026-05-23_market-campaign_v1.md
- long-term_best-practice_content-strategy_v2.md
- knowledge_process_expense-reimbursement_v1.md
- data_monthly_2026-04_sales-report_v1.md
- people_customer_张三_profile_v1.md
- events_2026-05-20_new-car-launch_v1.md
```

### 3. 记忆内容结构

每个记忆文件应包含以下部分：

```markdown
# {记忆标题}

## 基本信息
- **记忆ID**: {自动生成}
- **创建时间**: {YYYY-MM-DD HH:MM:SS}
- **更新时间**: {YYYY-MM-DD HH:MM:SS}
- **记忆类型**: {short-term/medium-term/long-term/knowledge/data/people/events}
- **相关主题**: {主题标签，逗号分隔}
- **重要程度**: {低/中/高/关键}

## 内容摘要
{简要描述记忆内容}

## 详细内容
{具体内容，结构化组织}

## 关键数据
{如有数据，以表格形式呈现}

## 经验教训
{成功经验、失败教训、改进建议}

## 相关链接
- 相关文件: {文件路径}
- 相关记忆: {其他记忆ID}
- 外部链接: {URL}

## 行动项
- [ ] {待办事项1}
- [ ] {待办事项2}

## 元数据
```json
{
  "memory_id": "memory_xxxxxxxxxxxx",
  "created_by": "xia-zong",
  "source_agent": "xia-shichang/xia-xinmeiti/...",
  "confidence": 0.95,
  "validation_status": "verified/pending/rejected",
  "access_level": "public/team/private"
}
```

## 记忆检索与使用

### 1. 检索方式

| 检索维度 | 检索方法 | 适用场景 |
|---------|---------|---------|
| 时间检索 | 按日期范围检索 | 历史数据分析、趋势对比 |
| 主题检索 | 按主题标签检索 | 专业知识查找、案例参考 |
| 类型检索 | 按记忆类型检索 | 特定类型信息查找 |
| 关键词检索 | 全文关键词检索 | 模糊查找、关联信息 |
| 关联检索 | 按相关链接检索 | 深度挖掘、上下文理解 |

### 2. 记忆更新机制

- **自动更新**：定期任务自动更新数据记忆
- **手动更新**：重要经验手动更新长期记忆
- **合并更新**：相似记忆合并，避免重复
- **归档更新**：过期记忆归档到历史目录

### 3. 记忆验证机制

| 验证级别 | 验证方法 | 验证人 |
|---------|---------|--------|
| 自动验证 | 数据一致性检查、格式检查 | 系统自动 |
| 人工验证 | 内容准确性检查、逻辑检查 | 相关责任人 |
| 专家验证 | 专业知识验证、最佳实践验证 | 领域专家 |
| 时间验证 | 长期效果验证、实际应用验证 | 时间检验 |

## 部门专属记忆

### 1. 市场部记忆
- **位置**: `memory/departments/marketing/`
- **内容**: 市场活动案例、费用核销经验、竞品分析、投放效果
- **关键文件**:
  - `campaign-success-cases.md`（成功活动案例）
  - `expense-reimbursement-best-practices.md`（费用核销最佳实践）
  - `competitor-analysis-history.md`（竞品分析历史）
  - `media-buying-performance.md`（媒体采购效果）

### 2. 新媒体部记忆
- **位置**: `memory/departments/new-media/`
- **内容**: 爆款内容分析、平台运营经验、用户行为数据
- **关键文件**:
  - `viral-content-analysis.md`（爆款内容分析）
  - `platform-operation-guide.md`（平台运营指南）
  - `user-behavior-data.md`（用户行为数据）
  - `content-calendar-history.md`（内容日历历史）

### 3. 销售部记忆
- **位置**: `memory/departments/sales/`
- **内容**: 销售技巧、客户谈判、库存管理、竞品对比
- **关键文件**:
  - `sales-techniques.md`（销售技巧）
  - `customer-negotiation-cases.md`（客户谈判案例）
  - `inventory-management-history.md`（库存管理历史）
  - `competitor-price-comparison.md`（竞品价格对比）

### 4. 售后部记忆
- **位置**: `memory/departments/after-sales/`
- **内容**: 维修案例、配件使用、客户投诉、服务质量
- **关键文件**:
  - `repair-cases.md`（维修案例）
  - `parts-usage-data.md`（配件使用数据）
  - `customer-complaint-handling.md`（客户投诉处理）
  - `service-quality-history.md`（服务质量历史）

### 5. 财务部记忆
- **位置**: `memory/departments/finance/`
- **内容**: 预算执行、费用核销、返利管理、财务分析
- **关键文件**:
  - `budget-execution-history.md`（预算执行历史）
  - `expense-reimbursement-data.md`（费用核销数据）
  - `rebate-management-records.md`（返利管理记录）
  - `financial-analysis-reports.md`（财务分析报告）

### 6. 客服部记忆
- **位置**: `memory/departments/customer-service/`
- **内容**: 客户反馈、投诉处理、满意度数据、话术优化
- **关键文件**:
  - `customer-feedback-analysis.md`（客户反馈分析）
  - `complaint-handling-cases.md`（投诉处理案例）
  - `satisfaction-data-history.md`（满意度数据历史）
  - `script-optimization-records.md`（话术优化记录）

### 7. 行政部记忆
- **位置**: `memory/departments/administration/`
- **内容**: 资产管理、文档归档、会议记录、采购流程
- **关键文件**:
  - `asset-management-records.md`（资产管理记录）
  - `document-archive-history.md`（文档归档历史）
  - `meeting-minutes.md`（会议纪要）
  - `procurement-process-guide.md`（采购流程指南）

## 品牌专属记忆

### 1. 传祺品牌记忆
- **位置**: `memory/brands/trumpchi/`
- **内容**: 传祺品牌活动、市场表现、客户反馈、竞品对比
- **关键文件**:
  - `campaign-history.md`（活动历史）
  - `market-performance.md`（市场表现）
  - `customer-feedback.md`（客户反馈）
  - `competitor-comparison.md`（竞品对比）

### 2. 奥迪品牌记忆
- **位置**: `memory/brands/audi/`
- **内容**: 奥迪品牌活动、圈层运营、客户体验、豪华竞品
- **关键文件**:
  - `circle-marketing-cases.md`（圈层营销案例）
  - `customer-experience-data.md`（客户体验数据）
  - `luxury-competitor-analysis.md`（豪华竞品分析）
  - `brand-image-evolution.md`（品牌形象演变）

### 3. 昊铂品牌记忆
- **位置**: `memory/brands/hyper/`
- **内容**: 昊铂技术传播、用户运营、科技竞品、创新案例
- **关键文件**:
  - `tech-communication-cases.md`（技术传播案例）
  - `user-community-data.md`（用户社区数据）
  - `tech-competitor-analysis.md`（科技竞品分析）
  - `innovation-cases.md`（创新案例）

### 4. 埃安品牌记忆
- **位置**: `memory/brands/aion/`
- **内容**: 埃安年轻化营销、社群运营、新能源竞品、直播案例
- **关键文件**:
  - `youth-marketing-cases.md`（年轻化营销案例）
  - `community-operation-data.md`（社群运营数据）
  - `new-energy-competitor-analysis.md`（新能源竞品分析）
  - `live-streaming-cases.md`（直播案例）

## 记忆清理与归档

### 1. 清理规则
- **短期记忆**: 7天后自动清理（重要内容手动转存）
- **中期记忆**: 30天后自动归档到历史目录
- **长期记忆**: 永久保留，定期优化
- **数据记忆**: 按数据保留政策清理（财务数据保留5年等）

### 2. 归档规则
- **时间归档**: 按月/季度/年归档
- **主题归档**: 按主题分类归档
- **部门归档**: 按部门分类归档
- **品牌归档**: 按品牌分类归档

### 3. 备份规则
- **本地备份**: 每日自动备份到备份目录
- **云端备份**: 每周自动同步到GitHub
- **异地备份**: 每月自动备份到异地存储

## 记忆使用指南

### 1. 新任务启动时
1. 检索相关历史记忆（类似任务、相同品牌、相同部门）
2. 参考最佳实践和失败教训
3. 建立本次任务记忆文件
4. 记录关键决策和依据

### 2. 任务执行过程中
1. 实时更新任务状态和进展
2. 记录遇到的问题和解决方案
3. 收集相关数据和证据
4. 标记重要节点和决策点

### 3. 任务完成后
1. 总结成功经验和失败教训
2. 更新相关长期记忆
3. 归档任务相关文件
4. 生成任务复盘报告

### 4. 定期回顾
1. 每周回顾近期记忆，提炼经验
2. 每月回顾部门记忆，优化流程
3. 每季度回顾品牌记忆，调整策略
4. 每年回顾全部记忆，制定规划

## 记忆安全与权限

### 1. 权限分级
- **公开记忆**: 所有部门可访问（最佳实践、模板文件）
- **部门记忆**: 仅本部门可访问（部门内部经验）
- **私人记忆**: 仅创建者可访问（个人工作记录）
- **机密记忆**: 加密存储，需授权访问（财务数据、客户隐私）

### 2. 安全措施
- 敏感数据加密存储
- 访问日志记录
- 定期安全审计
- 数据泄露防护

### 3. 合规要求
- 符合数据保护法规
- 保护客户隐私
- 遵守公司信息安全政策
- 定期合规检查