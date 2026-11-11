
def get_app_info() -> str:
    """Get information about this application."""
    return "Personal Utility Hub - Local MCP Server"


def register_resources(mcp):
    """Register application resources."""
    mcp.resource("app://info")(get_app_info)
