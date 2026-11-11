
from mcp.server import MCPServer

from personal_utility_mcp import database


def register_task_tools(mcp: MCPServer) -> None:
    """Register all SQLite CRUD operations as MCP tools."""

    # CREATE
    mcp.add_tool(database.add_task)

    # READ
    mcp.add_tool(database.list_tasks)
    mcp.add_tool(database.get_task)

    # UPDATE
    mcp.add_tool(database.update_task)
    mcp.add_tool(database.complete_task)

    # DELETE
    mcp.add_tool(database.delete_task)
