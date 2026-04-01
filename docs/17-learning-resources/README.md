# 第17章 学习资源汇总

> 🎯 本章定位：汇总 AI Agent 学习所需的优质资源，包括开源项目、博客文章、论文、视频教程、社区平台和学习路线图，帮助学习者高效构建知识体系。

---

## 目录

- [一、核心 GitHub 仓库推荐](#一核心-github-仓库推荐)
- [二、博客文章推荐](#二博客文章推荐)
- [三、DeepWiki 文档链接](#三deepwiki-文档链接)
- [四、必读论文清单](#四必读论文清单)
- [五、视频教程推荐](#五视频教程推荐)
- [六、社区与交流](#六社区与交流)
- [七、工具与平台](#七工具与平台)
- [八、学习路线图](#八学习路线图)
- [九、书籍推荐](#九书籍推荐)

---

## 一、核心 GitHub 仓库推荐

### 1.1 Agent 框架类

| 仓库 | Stars | 定位 | 推荐理由 |
|------|-------|------|---------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 37K+ | 轻量级 Agent 框架 | 本项目的核心学习对象，4000 行代码涵盖完整 Agent 能力 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 95K+ | 全功能 LLM 框架 | 最主流的 Agent 框架，生态最丰富 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 8K+ | 图结构 Agent 编排 | LangChain 团队的新一代 Agent 框架，更灵活 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 35K+ | 多 Agent 对话框架 | 微软开源，多 Agent 协作的代表项目 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 22K+ | 多 Agent 协作 | 角色扮演式多 Agent 框架，易上手 |
| [phidatahq/phidata](https://github.com/phidatahq/phidata) | 15K+ | Agent 开发工具包 | 提供内存、知识库、工具等开箱即用组件 |

**学习建议**：先深入学习 Nanobot（理解原理），再横向了解 LangChain/AutoGen（理解生态）。

---

### 1.2 MCP 协议类

| 仓库 | Stars | 定位 | 推荐理由 |
|------|-------|------|---------|
| [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification) | 5K+ | MCP 协议规范 | 官方规范文档，理解协议必读 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 15K+ | 官方 MCP Server 集合 | 学习 MCP Server 开发的最佳参考 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 3K+ | Python MCP SDK | 开发 MCP Server 的官方工具包 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 3K+ | TypeScript MCP SDK | JS/TS 生态的 MCP 开发包 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 10K+ | MCP Server 合集 | 社区维护的 MCP Server 精选列表 |
| [wong2/mcp-cli](https://github.com/wong2/mcp-cli) | 2K+ | MCP 调试工具 | 命令行 MCP 测试工具，开发调试必备 |

**学习建议**：先读 specification 理解协议设计，再用 python-sdk 开发自己的第一个 MCP Server。

---

### 1.3 大模型训练类

| 仓库 | Stars | 定位 | 推荐理由 |
|------|-------|------|---------|
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 45K+ | 从零训练小型 LLM | 本项目的模型训练学习对象，教学质量极高 |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 38K+ | 最简 GPT 实现 | Karpathy 出品，极致简洁的 GPT 训练代码 |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | 25K+ | C 语言 LLM 训练 | 理解 LLM 训练的底层实现 |
| [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 40K+ | LLM 微调工具箱 | 一站式微调框架，支持 100+ 模型 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 135K+ | 模型库标准 | 最主流的预训练模型库和推理框架 |
| [huggingface/trl](https://github.com/huggingface/trl) | 10K+ | RLHF/DPO 训练 | HuggingFace 官方的对齐训练工具 |

**学习建议**：先跟 MiniMind 走完全流程，再用 LLaMA-Factory 在开源大模型上做微调实践。

---

### 1.4 RAG 与知识检索类

| 仓库 | Stars | 定位 | 推荐理由 |
|------|-------|------|---------|
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 15K+ | 嵌入式向量数据库 | 最易上手的向量数据库，适合学习和原型 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 30K+ | 分布式向量数据库 | 生产级向量数据库，功能最全 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 37K+ | LLM 数据连接框架 | RAG 场景下最受欢迎的数据接入框架 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 25K+ | 开源 RAG 引擎 | 国产开源，深度文档理解 + 模板化分块 |

---

### 1.5 推理与部署类

| 仓库 | Stars | 定位 | 推荐理由 |
|------|-------|------|---------|
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 30K+ | LLM 推理引擎 | PagedAttention 技术，推理性能最优 |
| [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | 70K+ | CPU/端侧推理 | C/C++ 实现，量化推理的标杆项目 |
| [ollama/ollama](https://github.com/ollama/ollama) | 100K+ | 本地 LLM 运行器 | 一键运行本地大模型，体验极佳 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 50K+ | LLM Web 界面 | 开源的 ChatGPT 风格界面，支持 Ollama |

---

## 二、博客文章推荐

### 2.1 Agent 与 Nanobot 相关

| 文章标题 | 平台 | 内容概述 |
|---------|------|---------|
| 深入解析 Nanobot AgentLoop 源码 | CSDN/掘金 | AgentLoop 的逐行代码分析 |
| Nanobot + 通义千问实战：搭建飞书 AI 助手 | 技术博客 | 实战教程，从配置到部署 |
| 2026 大模型 Agent 面试全攻略 | 知乎 | 面试准备综合指南 |
| Anthropic：Building Effective Agents | Anthropic 官方博客 | Agent 设计模式权威总结 |
| AI Agent 架构设计：从 ReAct 到 Multi-Agent | 微信公众号 | Agent 架构演进综述 |
| Nanobot 源码中的设计模式分析 | 掘金 | 设计模式视角的源码解读 |

### 2.2 MCP 协议相关

| 文章标题 | 平台 | 内容概述 |
|---------|------|---------|
| MCP 协议完全教程 | 技术老金 | MCP 从入门到精通的系统教程 |
| 从零开发你的第一个 MCP Server | CSDN | 手把手教程，附完整代码 |
| MCP vs Function Calling：一文搞清区别 | 知乎 | 高频面试题的详细解读 |
| MCP 生态年度报告 2025 | Anthropic 官方 | MCP 生态发展数据和趋势 |
| 企业级 MCP Server 开发最佳实践 | 技术博客 | 安全、性能、可维护性指南 |

### 2.3 大模型原理相关

| 文章标题 | 平台 | 内容概述 |
|---------|------|---------|
| The Illustrated Transformer | Jay Alammar 博客 | Transformer 可视化经典教程 |
| Attention Is All You Need 论文精读 | 李沐（B站） | 论文逐段讲解 |
| 直觉理解 LoRA：为什么低秩分解有效 | 知乎 | LoRA 原理的直觉解释 |
| RLHF 全流程详解：从 SFT 到 PPO | 微信公众号 | RLHF 三阶段完整技术解析 |
| DPO vs PPO：偏好对齐方法对比 | 技术博客 | 两种对齐方法的全方位对比 |
| Flash Attention 原理解析 | 知乎 | IO-aware 算法设计的详细讲解 |
| KV Cache 与推理优化全解 | CSDN | 推理优化技术的系统综述 |

### 2.4 RAG 相关

| 文章标题 | 平台 | 内容概述 |
|---------|------|---------|
| RAG 实战全攻略 | 知乎专栏 | 从基础到高级的 RAG 技术 |
| 混合检索 + Rerank：RAG 效果提升指南 | CSDN | 检索优化的工程实践 |
| Chunk 策略大全：如何切分文档最有效 | 技术博客 | 多种 Chunk 策略的对比和选型 |
| Self-RAG：让模型自己决定要不要检索 | 知乎 | Self-RAG 论文解读 |

---

## 三、DeepWiki 文档链接

DeepWiki 是基于 AI 自动生成的开源项目文档平台，对 Nanobot 和 MiniMind 都有系统性的文档：

### 3.1 Nanobot DeepWiki

- [项目概览与架构](https://deepwiki.com/HKUDS/nanobot)
- [AgentLoop 详解](https://deepwiki.com/HKUDS/nanobot/agent-loop)
- [ContextBuilder 与上下文管理](https://deepwiki.com/HKUDS/nanobot/context-builder)
- [MemoryConsolidator 记忆系统](https://deepwiki.com/HKUDS/nanobot/memory)
- [ToolRegistry 工具注册](https://deepwiki.com/HKUDS/nanobot/tool-registry)
- [MCP 集成](https://deepwiki.com/HKUDS/nanobot/mcp-integration)
- [SubagentManager 子 Agent](https://deepwiki.com/HKUDS/nanobot/subagent)
- [Channel 适配器](https://deepwiki.com/HKUDS/nanobot/channel-adapter)
- [配置系统](https://deepwiki.com/HKUDS/nanobot/configuration)
- [Skills 系统](https://deepwiki.com/HKUDS/nanobot/skills)

### 3.2 MiniMind DeepWiki

- [项目概览](https://deepwiki.com/jingyaogong/minimind)
- [模型架构](https://deepwiki.com/jingyaogong/minimind/architecture)
- [Pretrain 预训练](https://deepwiki.com/jingyaogong/minimind/pretrain)
- [SFT 监督微调](https://deepwiki.com/jingyaogong/minimind/sft)
- [LoRA 微调](https://deepwiki.com/jingyaogong/minimind/lora)
- [DPO 偏好对齐](https://deepwiki.com/jingyaogong/minimind/dpo)
- [MoE 混合专家](https://deepwiki.com/jingyaogong/minimind/moe)

> 注：DeepWiki 的 URL 可能会更新，如果链接失效请直接在 deepwiki.com 搜索项目名。

---

## 四、必读论文清单

### 4.1 Transformer 与基础架构

| 论文 | 年份 | 核心贡献 | 优先级 |
|------|------|---------|--------|
| **Attention Is All You Need** (Vaswani et al.) | 2017 | 提出 Transformer 架构 | ★★★★★ |
| **RoFormer: Enhanced Transformer with Rotary Position Embedding** (Su et al.) | 2021 | 提出 RoPE 旋转位置编码 | ★★★★ |
| **Flash Attention** (Dao et al.) | 2022 | IO-aware 注意力计算，O(n) 内存 | ★★★★ |
| **GQA: Training Generalized Multi-Query Transformer** (Ainslie et al.) | 2023 | 提出 GQA 注意力机制 | ★★★★ |
| **GLU Variants Improve Transformer** (Shazeer) | 2020 | 提出 SwiGLU 等激活函数 | ★★★ |
| **Root Mean Square Layer Normalization** (Zhang & Sennrich) | 2019 | 提出 RMSNorm | ★★★ |
| **YaRN: Efficient Context Window Extension** (Peng et al.) | 2023 | 长度扩展方法 | ★★★ |

### 4.2 训练与对齐

| 论文 | 年份 | 核心贡献 | 优先级 |
|------|------|---------|--------|
| **Training Language Models to Follow Instructions** (Ouyang et al., InstructGPT) | 2022 | RLHF 三阶段训练框架 | ★★★★★ |
| **LoRA: Low-Rank Adaptation of Large Language Models** (Hu et al.) | 2021 | 参数高效微调方法 | ★★★★★ |
| **Direct Preference Optimization (DPO)** (Rafailov et al.) | 2023 | 无需 RM 的偏好对齐 | ★★★★★ |
| **QLoRA** (Dettmers et al.) | 2023 | 4-bit 量化 + LoRA | ★★★★ |
| **Scaling Laws for Neural Language Models** (Kaplan et al.) | 2020 | 模型缩放规律 | ★★★★ |
| **Training Compute-Optimal LLMs (Chinchilla)** (Hoffmann et al.) | 2022 | 最优训练配比 | ★★★★ |
| **Constitutional AI** (Bai et al.) | 2022 | RLAIF 方法 | ★★★ |
| **DeepSeek-Math: GRPO** (DeepSeek) | 2024 | 无 Critic 的 RL 方法 | ★★★ |

### 4.3 Agent 与推理

| 论文 | 年份 | 核心贡献 | 优先级 |
|------|------|---------|--------|
| **ReAct: Synergizing Reasoning and Acting** (Yao et al.) | 2022 | 推理+行动交替框架 | ★★★★★ |
| **Reflexion** (Shinn et al.) | 2023 | Agent 自我反思机制 | ★★★★ |
| **Toolformer** (Schick et al.) | 2023 | 模型自学工具使用 | ★★★★ |
| **Chain-of-Thought Prompting** (Wei et al.) | 2022 | 思维链推理 | ★★★★ |
| **Tree of Thoughts** (Yao et al.) | 2023 | 树形推理搜索 | ★★★ |
| **Self-RAG** (Asai et al.) | 2023 | 自适应检索增强生成 | ★★★ |
| **HuggingGPT** (Shen et al.) | 2023 | LLM 作为任务规划器 | ★★★ |
| **Lost in the Middle** (Liu et al.) | 2023 | 长上下文位置偏差 | ★★★★ |

### 4.4 MCP 与协议

| 文档/规范 | 类型 | 核心内容 | 优先级 |
|-----------|------|---------|--------|
| **MCP Specification** | 协议规范 | MCP 完整协议定义 | ★★★★★ |
| **JSON-RPC 2.0 Specification** | 协议规范 | MCP 底层消息格式 | ★★★ |
| **OpenAPI Specification 3.1** | API 标准 | REST API 描述标准（对比学习） | ★★ |

### 4.5 论文阅读建议

1. **按优先级阅读**：先读 ★★★★★ 的论文，确保核心概念理解
2. **不需要读公式推导**：对工程岗位，理解核心 idea 和方法论足够
3. **配合博客解读**：每篇论文先看中文博客解读建立直觉，再看原文细节
4. **关注实验部分**：论文中的实验设置、消融实验和对比结果对面试很有用
5. **推荐阅读顺序**：Attention Is All You Need → LoRA → ReAct → DPO → MCP Spec

---

## 五、视频教程推荐

### 5.1 大模型原理

| 视频/系列 | 平台 | 讲师 | 推荐理由 |
|-----------|------|------|---------|
| Attention Is All You Need 论文精读 | B站 | 李沐 | 最好的 Transformer 论文讲解 |
| 动手学深度学习 (d2l) | B站/课程网站 | 李沐团队 | 系统性的深度学习入门 |
| Neural Networks: Zero to Hero | YouTube | Andrej Karpathy | 从零实现 GPT 的最佳教程 |
| Let's build GPT | YouTube | Andrej Karpathy | 手把手实现 GPT 的经典视频 |
| MiniMind 项目讲解 | B站 | 项目作者 | 配套本项目的训练实战讲解 |
| 3Blue1Brown 深度学习系列 | YouTube/B站 | Grant Sanderson | 最直观的数学可视化讲解 |

### 5.2 Agent 与 LLM 应用

| 视频/系列 | 平台 | 讲师 | 推荐理由 |
|-----------|------|------|---------|
| LangChain 官方教程系列 | YouTube | LangChain 团队 | 最权威的 Agent 框架教程 |
| Building AI Agents | YouTube | Andrew Ng / DeepLearning.AI | 吴恩达的 Agent 课程 |
| MCP 协议入门实战 | B站 | 技术博主 | 中文 MCP 实战教程 |
| RAG 从入门到精通 | B站 | 各技术博主 | 搜索「RAG 实战」即可找到大量教程 |
| AI Agent 项目实战 | B站 | 各技术博主 | 搜索「AI Agent 实战」 |

### 5.3 面试准备

| 视频/系列 | 平台 | 推荐理由 |
|-----------|------|---------|
| 大模型面试八股文讲解 | B站 | 覆盖 Transformer、训练、推理等高频题 |
| AI 算法岗面试经验分享 | B站/知乎 | 一线面试者的真实经验分享 |
| 系统设计面试教程 | YouTube | 学习系统设计题的思维框架 |
| LeetCode 刷题指南 | B站/YouTube | 算法面试准备 |

---

## 六、社区与交流

### 6.1 GitHub 社区

| 平台 | 用途 | 建议 |
|------|------|------|
| Nanobot Issues | 问题反馈和功能讨论 | 关注 bug 修复和新 feature 讨论 |
| Nanobot Discussions | 社区交流 | 可以提问和分享经验 |
| MCP specification Issues | 协议讨论 | 跟踪 MCP 协议的演进方向 |
| MiniMind Issues | 训练问题交流 | 遇到训练问题可以搜索已有 issue |

### 6.2 社交平台

| 平台 | 关注对象 | 获取信息类型 |
|------|---------|-------------|
| **即刻** | AI Agent 圈子、MCP 话题 | 行业动态、内推、产品发布 |
| **X/Twitter** | @AnthropicAI, @OpenAI, @kaborofficial | 技术前沿、论文发布 |
| **知乎** | AI/LLM 相关话题和专栏 | 技术深度分析、面经分享 |
| **微信公众号** | 量子位、机器之心、AI前线 | 行业新闻和技术解读 |
| **Discord** | LangChain Discord, Anthropic Discord | 英文技术社区，问题解答快 |
| **掘金** | AI/LLM 标签 | 中文技术博客、实战教程 |
| **CSDN** | AI/大模型专栏 | 中文技术文章、面试经验 |

### 6.3 参与开源的建议

参与开源贡献是简历上最有说服力的加分项之一：

1. **从小事做起**：修 typo、改文档、补充测试用例
2. **报告高质量的 Issue**：包含复现步骤、环境信息、期望行为
3. **提交实用的 PR**：修复 bug 或添加小功能
4. **写使用教程**：为项目写中文教程或使用指南
5. **贡献 MCP Server**：开发一个有用的 MCP Server 并贡献到 awesome-mcp-servers

---

## 七、工具与平台

### 7.1 开发工具

| 工具 | 用途 | 推荐度 |
|------|------|--------|
| **Cursor IDE** | AI 辅助编程 IDE | ★★★★★ |
| **VS Code** | 通用代码编辑器 | ★★★★★ |
| **Jupyter Notebook** | 交互式实验环境 | ★★★★ |
| **MCP Inspector** | MCP Server 调试工具 | ★★★★ |
| **Postman** | API 测试工具 | ★★★ |
| **Docker Desktop** | 容器化开发环境 | ★★★★ |

### 7.2 AI 模型平台

| 平台 | 提供的能力 | 定价参考 |
|------|-----------|---------|
| **OpenAI API** | GPT-4o/GPT-4 模型 | GPT-4o: $2.5-10/M tokens |
| **Anthropic API** | Claude 3.5/4 模型 | Claude Sonnet: $3-15/M tokens |
| **阿里云 DashScope** | 通义千问系列 | 按量计费，有免费额度 |
| **百度千帆** | 文心一言系列 | 按量计费，有免费额度 |
| **硅基流动 (SiliconFlow)** | 多种开源模型推理 | 性价比高的推理平台 |
| **Ollama** | 本地模型运行 | 免费，需要本地 GPU |

### 7.3 向量数据库

| 数据库 | 部署方式 | 适用场景 |
|--------|---------|---------|
| **ChromaDB** | 嵌入式/本地 | 学习和原型开发 |
| **Milvus** | 分布式/云端 | 生产级大规模检索 |
| **Pinecone** | 全托管云服务 | 快速上手，免运维 |
| **Weaviate** | 开源分布式 | 多模态检索 |
| **Qdrant** | 开源分布式 | Rust 实现，性能优秀 |

### 7.4 监控与可观测性

| 工具 | 用途 | 推荐度 |
|------|------|--------|
| **LangSmith** | LLM 应用追踪和调试 | ★★★★★ |
| **Weights & Biases** | 模型训练实验跟踪 | ★★★★★ |
| **Prometheus + Grafana** | 系统指标监控 | ★★★★ |
| **Langfuse** | 开源 LLM 可观测性 | ★★★★ |

---

## 八、学习路线图

### 8.1 四周速成计划（每天 4-6 小时）

适合有 Python 基础、想快速入门 AI Agent 的开发者。

#### 第 1 周：大模型与 Agent 基础

| 天 | 学习内容 | 产出 |
|----|---------|------|
| Day 1 | 阅读本项目第 1 章（什么是 Agent） + 第 2 章（Nanobot 概览） | 理解 Agent 基本概念 |
| Day 2 | 阅读第 3 章（架构深度解析），画出 Nanobot 架构图 | 架构笔记 |
| Day 3 | 动手安装 Nanobot（第 6 章），跑通基本对话 | 成功运行 Nanobot |
| Day 4 | 阅读 Transformer 入门博客 + 看 3Blue1Brown 视频 | 理解注意力机制 |
| Day 5 | 阅读第 12 章 MiniMind 完全指南的架构部分 | 理解 Transformer 架构组件 |
| Day 6-7 | 阅读第 5 章（MCP 协议），跑通一个 MCP Server 示例 | 理解 MCP 基本概念 |

#### 第 2 周：源码研读与 MCP 实践

| 天 | 学习内容 | 产出 |
|----|---------|------|
| Day 8-9 | 阅读第 4 章（源码逐行解析）—— AgentLoop 部分 | AgentLoop 流程图 |
| Day 10-11 | 阅读第 4 章 —— MemoryConsolidator、ToolRegistry 部分 | 模块分析笔记 |
| Day 12-13 | 用 MCP Python SDK 开发第一个 MCP Server | 可运行的 MCP Server |
| Day 14 | 将自己的 MCP Server 集成到 Nanobot 中测试 | 端到端验证成功 |

#### 第 3 周：模型训练与 RAG 实践

| 天 | 学习内容 | 产出 |
|----|---------|------|
| Day 15-16 | 跟着 MiniMind 完成模型架构实现 + Pretrain | 理解训练流程 |
| Day 17-18 | 完成 SFT + LoRA 训练 | 理解微调原理 |
| Day 19-20 | 用 LangChain + ChromaDB 搭建简单 RAG 系统 | 可运行的 RAG demo |
| Day 21 | 阅读第 7 章（记忆系统）和第 8 章（Skills 和工具） | 深化 Agent 理解 |

#### 第 4 周：面试准备与项目包装

| 天 | 学习内容 | 产出 |
|----|---------|------|
| Day 22-24 | 刷本项目第 13 章面试八股文（重点 Q1-Q50） | 核心概念牢固 |
| Day 25-26 | 准备简历（参考第 15 章模板）+ 写项目 STAR 话术 | 简历定稿 |
| Day 27-28 | 模拟面试练习 + 查漏补缺 | 面试话术流畅 |

---

### 8.2 八周深入计划（每天 3-4 小时）

适合时间更充裕、想建立更深厚基础的学习者。

#### 第 1-2 周：基础概念与环境搭建

- 学习本项目第 1-6 章
- 动手安装和使用 Nanobot
- 阅读 Transformer 入门材料
- 完成 5 道基础面试题（Q1-Q5）

#### 第 3-4 周：源码深入研读

- 精读 Nanobot 核心源码（第 4 章）
- 重点理解 AgentLoop、MemoryConsolidator、ToolRegistry
- 开发 2 个自定义 MCP Server
- 学习第 7-10 章（记忆、工具、多平台、子 Agent）

#### 第 5-6 周：模型原理与训练实践

- 阅读 Attention Is All You Need 论文（配合视频讲解）
- 跟着 MiniMind 完成全流程训练（Pretrain → SFT → LoRA → DPO）
- 阅读 LoRA 和 DPO 论文
- 做 GQA vs MHA 对比实验

#### 第 7 周：RAG 与系统设计

- 搭建完整的 RAG 系统（混合检索 + Rerank）
- 学习系统设计（第 13 章 Q119-Q126）
- 阅读 MCP 协议规范
- 开发飞书/钉钉 AI 助手

#### 第 8 周：面试冲刺

- 刷完第 13 章全部 134 道面试题
- 完善简历和项目话术
- 进行 3 次以上模拟面试
- 开始投递和面试

---

### 8.3 持续学习建议

AI Agent 领域变化极快，保持学习需要：

1. **每日**：浏览 AI 新闻（即刻、X/Twitter），了解最新动态
2. **每周**：阅读 1-2 篇技术博客或论文，保持知识更新
3. **每月**：完成一个小的技术实验或项目（如新的 MCP Server、新的 RAG 优化方案）
4. **每季度**：回顾和更新技术栈认知，关注新出现的框架和工具
5. **持续**：在 GitHub 上维护自己的项目，写技术博客记录学习心得

---

## 九、书籍推荐

### 9.1 大模型与 NLP

| 书名 | 作者 | 推荐理由 |
|------|------|---------|
| 《动手学深度学习》 | 李沐等 | 深度学习入门最佳教材，有在线互动版本 |
| 《Speech and Language Processing》 | Jurafsky & Martin | NLP 经典教材，免费在线版 |
| 《Deep Learning》 | Goodfellow et al. | 深度学习理论基础，花书 |
| 《大模型应用开发极简入门》 | 社区作者 | 中文入门书，实践导向 |

### 9.2 系统设计与工程

| 书名 | 作者 | 推荐理由 |
|------|------|---------|
| 《设计数据密集型应用》 | Martin Kleppmann | 分布式系统设计经典 |
| 《System Design Interview》 | Alex Xu | 系统设计面试圣经 |
| 《Clean Architecture》 | Robert C. Martin | 架构设计原则 |
| 《Python 工程实践》 | 社区作者 | Python 工程化最佳实践 |

### 9.3 面试准备

| 书名 | 作者 | 推荐理由 |
|------|------|---------|
| 《Cracking the Coding Interview》 | Gayle McDowell | 编程面试经典 |
| 《百面机器学习》 | 诸葛越等 | ML 面试题精选 |
| 《百面深度学习》 | 诸葛越等 | DL 面试题精选 |

---

## 总结

学习 AI Agent 的资源生态已经非常丰富，关键是**选择合适的路径并坚持执行**：

1. **源码为王**：Nanobot 的 4000 行源码是理解 Agent 原理的最佳教材
2. **实践驱动**：每学一个概念都要动手做实验，看 10 篇博客不如写一个 demo
3. **论文精选**：不需要读很多论文，但必读论文要精读
4. **社区参与**：加入社区讨论、提交 Issue/PR，是最快的学习加速器
5. **持续更新**：AI 领域日新月异，保持学习习惯比任何单项技能更重要

> 💡 **最终目标**：不是成为「会用 100 个工具的人」，而是成为「理解原理、能解决新问题的人」。框架会过时，但对 Agent 系统的深入理解永远有价值。

---

*上一章：[第16章 STAR 面试话术](../16-star-interview-script/README.md)*
*本章是 learn-nanobot 项目的最后一章。祝你面试顺利！*
