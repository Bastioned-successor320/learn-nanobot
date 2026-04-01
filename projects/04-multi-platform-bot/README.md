# 项目四：多平台机器人 - 一次开发，多端部署

## 项目简介

Nanobot 支持将同一个 Agent 同时部署到多个聊天平台。本项目演示如何将 AI 助手同时接入 Telegram 和飞书（Feishu），实现"一次配置，多端服务"。

## 架构概览

```
                    ┌─── Telegram Bot ──→ Telegram 用户
                    │
Nanobot Agent ──────┤
                    │
                    └─── 飞书 Bot ──────→ 飞书用户
```

所有平台共享同一个 Agent 定义（AGENTS.md）和技能（Skills），只需在 `config.json` 中配置各平台的接入参数。

## Telegram Bot 配置指南

### 1. 创建 Bot
1. 在 Telegram 中找到 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot` 创建新 Bot
3. 按提示设置名称，获取 Bot Token

### 2. 设置环境变量
```bash
export TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

### 3. 配置说明
在 `config.json` 的 `channels.telegram` 中配置：
- `bot_token`: Bot Token（通过环境变量引用）
- `allowed_users`: 允许使用的用户 ID 列表（可选，留空表示所有人可用）

## 飞书（Feishu）Bot 配置指南

### 1. 创建应用
1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 创建企业自建应用
3. 在"机器人"页面开启机器人能力
4. 获取 App ID 和 App Secret

### 2. 配置权限
在飞书开放平台中为应用添加以下权限：
- `im:message:receive_v1` — 接收消息
- `im:message:send_v1` — 发送消息

### 3. 设置环境变量
```bash
export FEISHU_APP_ID=your-app-id
export FEISHU_APP_SECRET=your-app-secret
```

### 4. 配置事件订阅
- 请求地址：`https://your-domain/feishu/webhook`
- 订阅事件：`im.message.receive_v1`

## 快速开始

```bash
# 1. 安装依赖
pip install nanobot-ai

# 2. 设置环境变量
export OPENAI_API_KEY=your-openai-key
export TELEGRAM_BOT_TOKEN=your-telegram-token
export FEISHU_APP_ID=your-feishu-app-id
export FEISHU_APP_SECRET=your-feishu-app-secret

# 3. 启动服务
nanobot
```

## 目录结构

```
04-multi-platform-bot/
├── README.md                    # 本文件
├── AGENTS.md                    # Agent 定义
├── config.json                  # 多平台配置
└── skills/
    └── daily-report/
        └── SKILL.md             # 日报生成技能
```

## 多平台开发要点

### 消息适配
不同平台的消息格式不同，Nanobot 会自动处理：
- **Telegram**: 支持 Markdown 格式
- **飞书**: 支持富文本卡片消息

### 用户鉴权
- 可通过 `allowed_users` 限制特定用户使用
- 飞书支持基于组织架构的权限控制

### 注意事项
- 每个平台的 Bot Token / App Secret 务必保密
- 建议使用环境变量管理敏感信息，不要硬编码到配置文件
- 飞书需要公网可访问的回调地址（开发时可用 ngrok）

## 面试话术

> "我实现了 Nanobot 的多平台部署方案，将同一个 AI Agent 同时接入 Telegram 和飞书。核心思路是 Agent 逻辑与通信渠道解耦——Agent 定义和技能共享，只需在配置文件中声明各平台的接入参数。我还开发了日报生成技能，帮助团队自动汇总每日工作内容。这个项目让我深入理解了 Bot 架构设计中的关注点分离原则。"
