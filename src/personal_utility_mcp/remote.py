
import os
import uvicorn

from mcp.server.transport_security import TransportSecuritySettings
from personal_utility_mcp.main import mcp
from personal_utility_mcp.auth import BearerTokenMiddleware


def create_app():
    """Create the authenticated MCP HTTP application."""

    # Configure trusted hosts and origins
    security = TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "127.0.0.1:*",
            "localhost:*",
            "personal-utility-mcp.duckdns.org",
            "personal-utility-mcp.duckdns.org:*",
        ],
        allowed_origins=[
            "https://personal-utility-mcp.duckdns.org",
            "http://127.0.0.1:6274",
            "http://localhost:6274",
        ],
    )

    # Create Streamable HTTP MCP application
    mcp_app = mcp.streamable_http_app(
        transport_security=security
    )

    # Protect MCP endpoints using bearer token
    return BearerTokenMiddleware(mcp_app)


if __name__ == "__main__":
    uvicorn.run(
        create_app(),
        host=os.getenv("MCP_HOST", "127.0.0.1"),
        port=int(os.getenv("MCP_PORT", "8000")),
    )

