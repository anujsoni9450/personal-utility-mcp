
# 1. Python base image
FROM python:3.13-slim

# 2. Install uv
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /bin/

# 3. Set working directory
WORKDIR /app

# 4. Runtime configuration
ENV UV_PYTHON_DOWNLOADS=0
ENV UV_NO_DEV=1
ENV PYTHONUNBUFFERED=1

# 5. Copy dependency and project files
COPY pyproject.toml uv.lock README.md ./
COPY src ./src

# 6. Install locked dependencies and project
RUN uv sync --locked --no-dev

# 7. Document the HTTP port
EXPOSE 8000

# 8. Start the MCP server
CMD ["uv", "run", "--no-sync", "python", "-m", "personal_utility_mcp.remote"]
