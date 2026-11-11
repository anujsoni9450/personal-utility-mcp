
# Personal Utility Hub — MCP Server

A Python-based **Model Context Protocol (MCP) server** featuring calculator utilities, SQLite task management, and a custom MCP client. Supports both STDIO and Streamable HTTP transports.

## Tech Stack

- **Language:** Python 3.13
- **MCP:** Official Python MCP SDK
- **Database:** SQLite
- **Transport:** STDIO, Streamable HTTP
- **Tools:** uv, pytest, MCP Inspector

## Features

- 11 MCP tools (5 utilities + 6 task management tools)
- Complete SQLite CRUD operations
- 1 MCP resource and 1 prompt
- Custom Python MCP client with dynamic tool discovery
- Modular server architecture
- 18 passing automated tests
- Input validation and database persistence

## Architecture

```text
MCP Inspector / Custom Python Client
                |
       STDIO / Streamable HTTP
                |
           MCP Server
                |
       Tools / Resources / Prompts
                |
           SQLite Database
```

## Project Structure

```text
personal-utility-mcp/
├── clients/
│   └── http_client.py
├── src/personal_utility_mcp/
│   ├── main.py
│   ├── remote.py
│   ├── tools.py
│   ├── task_tools.py
│   ├── database.py
│   ├── resources.py
│   └── prompts.py
├── tests/
│   ├── test_tools.py
│   ├── test_database.py
│   └── test_mcp.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

```bash
git clone https://github.com/anujsoni9450/personal-utility-mcp.git
cd personal-utility-mcp
uv sync
```

## Run the Server

**Local STDIO:**
```bash
uv run mcp dev src/personal_utility_mcp/main.py
```

**Streamable HTTP:**
```bash
uv run python -m personal_utility_mcp.remote
```

HTTP endpoint: `http://127.0.0.1:8000/mcp`

## Run Custom MCP Client

Start the HTTP server first, then run:

```bash
uv run python clients/http_client.py
```

## Testing

```bash
uv run pytest -v
```

**Results:** 18 tests passed (7 utility, 9 database, 2 MCP integration).

## Future Improvements

- Docker containerization
- Cloud deployment on AWS
- Authentication and persistent cloud storage
- Claude MCP integration
- CI/CD with GitHub Actions

## Author

**[Anuj Soni](https://github.com/anujsoni9450)**

*Built to explore MCP server development, client-server communication, and AI tool infrastructure.*
