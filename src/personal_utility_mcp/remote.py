
import os
import uvicorn

from personal_utility_mcp.main import mcp
from personal_utility_mcp.auth import BearerTokenMiddleware


def create_app():
    """Create the authenticated MCP HTTP application."""
    mcp_app = mcp.streamable_http_app()
    return BearerTokenMiddleware(mcp_app)


if __name__ == "__main__":
    uvicorn.run(
        create_app(),
        host=os.getenv("MCP_HOST", "127.0.0.1"),
        port=int(os.getenv("MCP_PORT", "8000")),
    )

