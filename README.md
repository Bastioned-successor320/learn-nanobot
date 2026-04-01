```
 _                              _   _                   _           _   
| |    ___  __ _ _ __ _ __     | \ | | __ _ _ __   ___ | |__   ___ | |_ 
| |   / _ \/ _` | '__| '_ \   |  \| |/ _` | '_ \ / _ \| '_ \ / _ \| __|
| |__|  __/ (_| | |  | | | |  | |\  | (_| | | | | (_) | |_) | (_) | |_ 
|_____\___|\__,_|_|  |_| |_|  |_| \_|\__,_|_| |_|\___/|_.__/ \___/ \__|
```

<p align="center">
  <strong>🤖 面向小白的面试导向 Nanobot + MiniMind 学习指南</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/HKUDS/nanobot"><img src="https://img.shields.io/badge/HKUDS-nanobot-orange.svg" alt="HKUDS/nanobot"></a>
  <a href="https://github.com/HKUDS/nanobot"><img src="https://img.shields.io/github/stars/HKUDS/nanobot?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/jingyaogong/minimind"><img src="https://img.shields.io/badge/MiniMind-LLM-green.svg" alt="MiniMind"></a>
</p>

---

## 项目简介

本项目是一份**面向零基础求职者**的 AI Agent 学习指南，以香港大学开源的超轻量级 AI Agent 框架 **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)**（37K+ Stars）为核心，结合 **[MiniMind](https://github.com/jingyaogong/minimind)** 大语言模型项目，帮助你：

- **彻底理解** AI Agent 的核心概念与设计思想
- **深入掌握** Nanobot 源码架构与实现细节
- **熟练运用** MCP 协议、记忆系统、技能系统等关键技术
- **从容应对** AI Agent 方向的技术面试

> 💡 **为什么选择 Nanobot？** 仅 4000 行 Python 代码，却涵盖了工业级 Agent 框架的所有核心设计——这是面试中最好的"以小见大"素材。

---

## 学习路线图

```
┌─────────────────────────────────────────────────────────────────┐
│                        学习路线图                                │
│                                                                 │
│   Phase 1              Phase 2            Phase 3    Phase 4    │
│  ┌──────────┐      ┌──────────┐      ┌─────────┐  ┌─────────┐ │
│  │ 基础概念  │ ──→  │ 动手实践  │ ──→  │ 项目实战 │→ │ 面试冲刺 │ │
│  └──────────┘      └──────────┘      └─────────┘  └─────────┘ │
│  ·什么是Agent       ·安装配置          ·接入MiniMind  ·八股文   │
│  ·Nanobot概览       ·记忆系统          ·多平台部署    ·简历模板 │
│  ·架构深入          ·技能与工具        ·安全与部署    ·STAR话术 │
│  ·源码走读          ·MCP协议实践       ·子Agent       ·市场分析 │
│  ·MCP协议                                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 目录

### Phase 1：基础概念（必读）

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [01 - 什么是 AI Agent](docs/01-what-is-agent/README.md) | Agent 定义、核心三要素、ReAct 框架、主流框架对比 | 2 小时 |
| [02 - Nanobot 项目概览](docs/02-nanobot-overview/README.md) | 项目背景、核心特性、为什么选 Nanobot 学习 | 1.5 小时 |
| [03 - 架构深入解析](docs/03-architecture-deep-dive/README.md) | 五层架构、四大核心模块、设计模式分析 | 3 小时 |
| [04 - 源码逐行解读](docs/04-source-code-walkthrough/README.md) | 核心文件解读、关键代码片段、执行流程 | 4 小时 |
| [05 - MCP 协议详解](docs/05-mcp-protocol/README.md) | MCP 架构、三大原语、与 Function Calling 对比 | 2 小时 |

### Phase 2：动手实践

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [06 - 安装与上手](docs/06-install-and-hands-on/README.md) | 环境搭建、第一个 Agent、配置详解 | 2 小时 |
| [07 - 记忆系统实战](docs/07-memory-system/README.md) | MEMORY.md、HISTORY.md、记忆压缩 | 2 小时 |
| [08 - 技能与工具](docs/08-skills-and-tools/README.md) | Skill 系统、MCP 工具、自定义工具 | 2 小时 |
| [09 - 多平台接入](docs/09-multi-platform/README.md) | Telegram、Discord、飞书、钉钉、微信 | 2 小时 |
| [10 - 子Agent与定时任务](docs/10-subagent-and-cron/README.md) | SubAgent 机制、CronJob 配置 | 1.5 小时 |

### Phase 3：项目实战

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [11 - 安全与部署](docs/11-security-and-deploy/README.md) | 安全策略、Docker 部署、生产环境 | 2 小时 |
| [12 - MiniMind 完整指南](docs/12-minimind-complete-guide/README.md) | MiniMind 训练、微调、接入 Nanobot | 4 小时 |

### Phase 4：面试冲刺

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [13 - 面试八股文](docs/13-interview-bagua/README.md) | 高频面试题与标准答案 | 3 小时 |
| [14 - 就业市场分析](docs/14-job-market-analysis/README.md) | AI Agent 岗位趋势、薪资、技能要求 | 1 小时 |
| [15 - 简历模板](docs/15-resume-template/README.md) | 项目经验写法、简历优化技巧 | 1 小时 |
| [16 - STAR 面试话术](docs/16-star-interview-script/README.md) | 行为面试、项目阐述话术 | 1 小时 |
| [17 - 学习资源](docs/17-learning-resources/README.md) | 论文、博客、视频、社区资源 | 0.5 小时 |

---

## 快速开始

### 1. 克隆本仓库

```bash
git clone https://github.com/your-username/learn-nanobot.git
cd learn-nanobot
```

### 2. 按顺序阅读文档

建议从 [01 - 什么是 AI Agent](docs/01-what-is-agent/README.md) 开始，按顺序阅读。

### 3. 动手实践

跟随 [06 - 安装与上手](docs/06-install-and-hands-on/README.md) 安装 Nanobot，开始你的第一个 Agent。

### 4. 面试准备

完成前 12 章后，进入 [13 - 面试八股文](docs/13-interview-bagua/README.md) 进行面试冲刺。

---

## 目录结构

```
learn-nanobot/
├── README.md                          # 本文件
├── LICENSE                            # MIT 许可证
├── assets/                            # 图片资源
├── comics/                            # 漫画学习素材
├── projects/                          # 实战项目代码
│   ├── basic-agent/                   # 基础 Agent 示例
│   ├── memory-demo/                   # 记忆系统 Demo
│   └── mcp-server/                    # MCP Server 示例
└── docs/                              # 文档目录
    ├── 01-what-is-agent/              # 什么是 AI Agent
    ├── 02-nanobot-overview/           # Nanobot 项目概览
    ├── 03-architecture-deep-dive/     # 架构深入解析
    ├── 04-source-code-walkthrough/    # 源码逐行解读
    ├── 05-mcp-protocol/              # MCP 协议详解
    ├── 06-install-and-hands-on/       # 安装与上手
    ├── 07-memory-system/             # 记忆系统实战
    ├── 08-skills-and-tools/          # 技能与工具
    ├── 09-multi-platform/            # 多平台接入
    ├── 10-subagent-and-cron/         # 子Agent与定时任务
    ├── 11-security-and-deploy/       # 安全与部署
    ├── 12-minimind-complete-guide/   # MiniMind 完整指南
    ├── 13-interview-bagua/           # 面试八股文
    ├── 14-job-market-analysis/       # 就业市场分析
    ├── 15-resume-template/           # 简历模板
    ├── 16-star-interview-script/     # STAR 面试话术
    └── 17-learning-resources/        # 学习资源
```

---

## Star History

如果这个项目对你有帮助，请给一个 Star ⭐

你的 Star 是我持续更新的动力！

---

## 参考项目

- [HKUDS/nanobot](https://github.com/HKUDS/nanobot) - 超轻量级 AI Agent 框架（37K+ Stars）
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) - 极简大语言模型项目

---

## License

本项目采用 [MIT License](LICENSE) 开源。

学习内容仅供参考，Nanobot 和 MiniMind 的版权归原作者所有。
