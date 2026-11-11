
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    return a - b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def get_server_status() -> dict[str, str]:
    """Get the current application server status."""
    return {
        "server_name": "Personal Utility Hub",
        "status": "running",
        "transport": "STDIO",
        "version": "1.0.0"
    }


def register_tools(mcp):
    """Register all calculator tools with the MCP server."""
    mcp.tool()(add)
    mcp.tool()(multiply)
    mcp.tool()(subtract)
    mcp.tool()(divide)
    mcp.tool()(get_server_status)
