"""
天气查询 MCP Server

一个简单的 MCP Server 示例，提供天气查询功能。
用于演示如何开发自定义 MCP Server 并接入 Nanobot。

运行方式: python weather_server.py
"""
import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

WEATHER_DATA = {
    "北京": {"temp": 25, "weather": "晴", "humidity": 40, "wind": "北风3级"},
    "上海": {"temp": 28, "weather": "多云", "humidity": 65, "wind": "东南风2级"},
    "广州": {"temp": 32, "weather": "雷阵雨", "humidity": 80, "wind": "南风4级"},
    "深圳": {"temp": 30, "weather": "阴", "humidity": 75, "wind": "西南风2级"},
    "杭州": {"temp": 26, "weather": "晴转多云", "humidity": 55, "wind": "东风2级"},
}

server = Server("weather-server")


@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="get_weather",
            description="查询指定城市的天气信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如：北京、上海、广州",
                    }
                },
                "required": ["city"],
            },
        ),
        types.Tool(
            name="compare_weather",
            description="比较两个城市的天气",
            inputSchema={
                "type": "object",
                "properties": {
                    "city1": {"type": "string", "description": "第一个城市"},
                    "city2": {"type": "string", "description": "第二个城市"},
                },
                "required": ["city1", "city2"],
            },
        ),
        types.Tool(
            name="list_cities",
            description="列出所有支持查询的城市",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_weather":
        city = arguments.get("city", "")
        if city in WEATHER_DATA:
            data = WEATHER_DATA[city]
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(
                        {
                            "city": city,
                            "temperature": f"{data['temp']}°C",
                            "weather": data["weather"],
                            "humidity": f"{data['humidity']}%",
                            "wind": data["wind"],
                        },
                        ensure_ascii=False,
                        indent=2,
                    ),
                )
            ]
        return [
            types.TextContent(
                type="text",
                text=f"未找到城市 '{city}' 的天气数据。支持的城市: {', '.join(WEATHER_DATA.keys())}",
            )
        ]

    elif name == "compare_weather":
        city1 = arguments.get("city1", "")
        city2 = arguments.get("city2", "")
        results = {}
        for city in [city1, city2]:
            if city not in WEATHER_DATA:
                return [
                    types.TextContent(type="text", text=f"未找到城市 '{city}'")
                ]
            results[city] = WEATHER_DATA[city]

        diff = results[city1]["temp"] - results[city2]["temp"]
        comparison = f"{city1}比{city2}{'高' if diff > 0 else '低'}{abs(diff)}°C"
        return [
            types.TextContent(
                type="text",
                text=json.dumps(
                    {
                        city1: results[city1],
                        city2: results[city2],
                        "温差对比": comparison,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
            )
        ]

    elif name == "list_cities":
        return [
            types.TextContent(
                type="text",
                text=f"支持的城市: {', '.join(WEATHER_DATA.keys())}",
            )
        ]

    return [types.TextContent(type="text", text=f"未知工具: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)


if __name__ == "__main__":
    asyncio.run(main())
