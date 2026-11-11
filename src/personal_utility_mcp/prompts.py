
def explain_calculation(a: int, b: int) -> str:
    """Generate a prompt explaining an addition."""
    return f"Explain the calculation {a} + {b} step by step."


def register_prompts(mcp):
    """Register application prompts."""
    mcp.prompt()(explain_calculation)
