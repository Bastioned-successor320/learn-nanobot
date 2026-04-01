"""
待办事项 MCP Server

提供待办事项的增删改查功能，数据存储在内存中（运行期间有效）。
用于演示 MCP Server 如何管理有状态的数据。

运行方式: python todo_server.py
"""
import asyncio
import json
import uuid
from datetime import datetime
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types


todo_store: dict[str, dict] = {}

server = Server("todo-server")


@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="add_todo",
            description="添加一个新的待办事项",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "待办事项标题",
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["high", "medium", "low"],
                        "description": "优先级：high(高)、medium(中)、low(低)",
                        "default": "medium",
                    },
                },
                "required": ["title"],
            },
        ),
        types.Tool(
            name="list_todos",
            description="列出所有待办事项，可按状态筛选",
            inputSchema={
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "enum": ["all", "pending", "completed"],
                        "description": "筛选状态：all(全部)、pending(未完成)、completed(已完成)",
                        "default": "all",
                    }
                },
            },
        ),
        types.Tool(
            name="complete_todo",
            description="将指定待办事项标记为已完成",
            inputSchema={
                "type": "object",
                "properties": {
                    "todo_id": {
                        "type": "string",
                        "description": "待办事项的 ID",
                    }
                },
                "required": ["todo_id"],
            },
        ),
        types.Tool(
            name="delete_todo",
            description="删除指定的待办事项",
            inputSchema={
                "type": "object",
                "properties": {
                    "todo_id": {
                        "type": "string",
                        "description": "待办事项的 ID",
                    }
                },
                "required": ["todo_id"],
            },
        ),
    ]


def _format_priority(p: str) -> str:
    return {"high": "🔴 高", "medium": "🟡 中", "low": "🟢 低"}.get(p, p)


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "add_todo":
        todo_id = uuid.uuid4().hex[:8]
        title = arguments.get("title", "")
        priority = arguments.get("priority", "medium")
        todo_store[todo_id] = {
            "id": todo_id,
            "title": title,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
        }
        return [
            types.TextContent(
                type="text",
                text=json.dumps(
                    {
                        "message": "待办事项添加成功",
                        "todo": todo_store[todo_id],
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
            )
        ]

    elif name == "list_todos":
        status_filter = arguments.get("status", "all")
        if status_filter == "all":
            filtered = list(todo_store.values())
        else:
            filtered = [t for t in todo_store.values() if t["status"] == status_filter]

        if not filtered:
            return [
                types.TextContent(type="text", text="当前没有待办事项。")
            ]

        lines = [f"共 {len(filtered)} 条待办事项：\n"]
        for t in filtered:
            status_icon = "✅" if t["status"] == "completed" else "⬜"
            lines.append(
                f"{status_icon} [{t['id']}] {t['title']} "
                f"(优先级: {_format_priority(t['priority'])})"
            )
        return [types.TextContent(type="text", text="\n".join(lines))]

    elif name == "complete_todo":
        todo_id = arguments.get("todo_id", "")
        if todo_id not in todo_store:
            return [
                types.TextContent(
                    type="text", text=f"未找到 ID 为 '{todo_id}' 的待办事项"
                )
            ]
        todo_store[todo_id]["status"] = "completed"
        todo_store[todo_id]["completed_at"] = datetime.now().isoformat()
        return [
            types.TextContent(
                type="text",
                text=json.dumps(
                    {
                        "message": f"待办 '{todo_store[todo_id]['title']}' 已标记为完成",
                        "todo": todo_store[todo_id],
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
            )
        ]

    elif name == "delete_todo":
        todo_id = arguments.get("todo_id", "")
        if todo_id not in todo_store:
            return [
                types.TextContent(
                    type="text", text=f"未找到 ID 为 '{todo_id}' 的待办事项"
                )
            ]
        deleted = todo_store.pop(todo_id)
        return [
            types.TextContent(
                type="text",
                text=f"已删除待办事项: {deleted['title']}",
            )
        ]

    return [types.TextContent(type="text", text=f"未知工具: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)


if __name__ == "__main__":
    asyncio.run(main())
