
from mcp.server import MCPServer

from personal_utility_mcp.tools import register_tools
from personal_utility_mcp.resources import register_resources
from personal_utility_mcp.prompts import register_prompts
from personal_utility_mcp.task_tools import register_task_tools
from personal_utility_mcp.database import init_db


# Initialize MCP server
mcp = MCPServer("Personal Utility Hub")


# Initialize SQLite database
init_db()


# Register calculator tools
register_tools(mcp)


# Register SQLite CRUD tools
register_task_tools(mcp)


# Register resources
register_resources(mcp)


# Register prompts
register_prompts(mcp)


if __name__ == "__main__":
    mcp.run()
