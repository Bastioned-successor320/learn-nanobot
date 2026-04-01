# 项目三：MCP Server - 给 AI 插上工具的翅膀

## 项目简介

MCP（Model Context Protocol）是 Anthropic 提出的模型上下文协议，它定义了 AI 模型与外部工具之间的标准通信方式。本项目演示如何用 Python 开发自定义 MCP Server，并将其接入 Nanobot。

## 什么是 MCP Server？

你可以把 MCP Server 理解为 AI 的"手和脚"：

```
用户 → Nanobot (AI 大脑) → MCP Server (工具) → 外部世界
                ↑                    |
                └────── 结果返回 ─────┘
```

**核心概念**：
- **MCP Server**：提供工具的服务端，通过 stdio 或 HTTP 与 Nanobot 通信
- **Tool（工具）**：MCP Server 暴露的具体功能，如"查询天气"、"添加待办"
- **Schema**：每个工具的输入参数定义，告诉 AI 如何调用该工具

## 项目中的 MCP Server

### 1. 天气查询服务 (`weather_server.py`)
提供三个工具：
| 工具名 | 功能 | 参数 |
|--------|------|------|
| `get_weather` | 查询单个城市天气 | `city`: 城市名 |
| `compare_weather` | 对比两个城市天气 | `city1`, `city2` |
| `list_cities` | 列出支持的城市 | 无 |

### 2. 待办事项服务 (`todo_server.py`)
提供四个工具：
| 工具名 | 功能 | 参数 |
|--------|------|------|
| `add_todo` | 添加待办事项 | `title`, `priority` |
| `list_todos` | 列出所有待办 | `status`（可选） |
| `complete_todo` | 完成待办事项 | `todo_id` |
| `delete_todo` | 删除待办事项 | `todo_id` |

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 测试 MCP Server 独立运行
```bash
# 测试天气服务
python weather_server.py

# 测试待办服务
python todo_server.py
```

### 3. 接入 Nanobot
```bash
export OPENAI_API_KEY=your-key
nanobot
```

对话示例：
```
> 北京今天天气怎么样？
> 对比一下北京和上海的天气
> 帮我添加一个待办：完成 MCP 项目报告
> 列出我的所有待办事项
```

## 开发自己的 MCP Server

### 基本模板

```python
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

server = Server("my-server")

@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="my_tool",
            description="工具描述",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {"type": "string", "description": "参数说明"}
                },
                "required": ["param1"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "my_tool":
        result = do_something(arguments["param1"])
        return [types.TextContent(type="text", text=result)]
    return [types.TextContent(type="text", text=f"未知工具: {name}")]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)

if __name__ == "__main__":
    asyncio.run(main())
```

### 开发步骤
1. 定义工具清单（`list_tools`）
2. 实现工具逻辑（`call_tool`）
3. 在 `config.json` 中注册 MCP Server
4. 在 `AGENTS.md` 中描述 Agent 可使用的工具

## 目录结构

```
03-mcp-server/
├── README.md            # 本文件
├── AGENTS.md            # Agent 定义
├── config.json          # Nanobot 配置（注册 MCP Server）
├── requirements.txt     # Python 依赖
├── weather_server.py    # 天气查询 MCP Server
└── todo_server.py       # 待办事项 MCP Server
```

## 面试话术

> "我深入研究了 MCP（Model Context Protocol）并开发了自定义 MCP Server。MCP 是 Anthropic 提出的标准化协议，解决了 AI 与外部工具集成的碎片化问题。我实现了天气查询和待办事项管理两个 MCP Server，每个 Server 通过 stdio 与 Nanobot 通信，暴露标准化的工具接口。AI 模型根据用户意图自动选择并调用合适的工具，实现了 Agent 的工具使用能力（Tool Use）。这种架构的好处是工具开发与 AI 模型解耦，符合单一职责原则。"
