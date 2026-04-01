# 项目二：自定义技能（Custom Skill）

## 项目简介

Nanobot 的核心扩展机制之一就是 **技能（Skill）**。技能是一组可复用的指令集，可以赋予 Agent 特定的专业能力。本项目演示如何创建和使用自定义技能。

## 什么是技能？

技能（Skill）本质上是一个 `SKILL.md` 文件，定义了 Agent 在特定场景下的行为模式。你可以把它理解为 Agent 的"专业知识模块"：

- **可复用**：一个技能可以被多个 Agent 引用
- **可组合**：一个 Agent 可以同时具备多个技能
- **声明式**：通过 Markdown 文件定义，无需编写代码

## SKILL.md 格式说明

```markdown
---
name: 技能名称
description: "技能的简短描述"
---

# 技能标题

## 使用方法
描述何时以及如何使用这个技能...

## 具体步骤
1. 步骤一
2. 步骤二
...

## 输出格式
定义输出的格式模板...
```

### 关键组成部分

| 部分 | 说明 |
|------|------|
| `Front Matter` | YAML 格式的元数据（name, description） |
| `使用方法` | 告诉 Agent 什么情况下触发该技能 |
| `具体步骤` | 技能执行的详细流程 |
| `输出格式` | 标准化的输出模板 |

## 目录结构

```
02-custom-skill/
├── README.md          # 本文件
├── AGENTS.md          # Agent 定义，引用技能
├── config.json        # 基础配置
└── skills/
    └── code-reviewer/
        └── SKILL.md   # 代码审查技能定义
```

## 如何测试你的技能

1. 安装依赖：`pip install nanobot-ai`
2. 设置 API Key：`export OPENAI_API_KEY=your-key`
3. 启动 Nanobot：`nanobot`
4. 测试对话示例：
   ```
   > 请帮我审查以下代码：
   > def login(user, pwd):
   >     query = f"SELECT * FROM users WHERE name='{user}' AND pass='{pwd}'"
   >     return db.execute(query)
   ```
5. Agent 应该能识别 SQL 注入漏洞并给出修复建议

## 创建自己的技能

1. 在 `skills/` 目录下创建新文件夹
2. 编写 `SKILL.md` 文件
3. 在 `AGENTS.md` 中引用该技能
4. 重启 Nanobot 测试

## 面试话术

> "我在 Nanobot 中实现了自定义技能系统。技能本质是声明式的 Markdown 文件，通过 SKILL.md 定义 Agent 在特定场景下的行为模式。例如我开发的代码审查技能，可以从安全性、性能、可维护性等维度分析代码，输出标准化的审查报告。这种设计的好处是技能可复用、可组合，多个 Agent 可以共享同一套技能。"
