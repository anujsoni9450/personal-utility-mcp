
import asyncio
from mcp import Client


SERVER_URL = "http://127.0.0.1:8000/mcp"


async def main():

    async with Client(SERVER_URL) as client:

        print("Connected to MCP server!")

        # 1. Discover available tools
        response = await client.list_tools()

        print("\nAvailable MCP Tools:")

        for tool in response.tools:
            print("-", tool.name)

        # 2. Execute calculator tool
        result = await client.call_tool(
            "add",
            {"a": 10, "b": 20}
        )

        if result.is_error:
            print("Tool error:", result.content)
        else:
            print("\nAddition result:")
            print(result.structured_content)

        # 3. Retrieve database tasks
        tasks_result = await client.call_tool(
            "list_tasks",
            {}
        )

        if tasks_result.is_error:
            print("Task error:", tasks_result.content)
        else:
            print("\nSaved tasks:")
            print(tasks_result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())
