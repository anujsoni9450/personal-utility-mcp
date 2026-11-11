
import pytest
from mcp import Client

from personal_utility_mcp import database
from personal_utility_mcp.main import mcp


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    """Use a temporary SQLite database."""

    test_db = tmp_path / "mcp_test.db"

    monkeypatch.setattr(
        database,
        "DB_PATH",
        test_db
    )

    database.init_db()


@pytest.mark.anyio
async def test_mcp_tool_discovery(isolated_db):
    """Verify all 11 tools are discoverable."""

    async with Client(mcp, raise_exceptions=True) as client:
        response = await client.list_tools()

        tool_names = {
            tool.name for tool in response.tools
        }

        expected_tools = {
            "add",
            "multiply",
            "subtract",
            "divide",
            "get_server_status",
            "add_task",
            "list_tasks",
            "get_task",
            "update_task",
            "complete_task",
            "delete_task",
        }

        assert expected_tools == tool_names


@pytest.mark.anyio
async def test_mcp_add_and_list_tasks(isolated_db):
    """Test database tools through MCP."""

    async with Client(mcp, raise_exceptions=True) as client:

        # Call add_task using MCP
        created = await client.call_tool(
            "add_task",
            {"title": "Learn MCP Integration"}
        )

        assert created.is_error is False

        task_id = created.structured_content["result"]

        # Call list_tasks using MCP
        listed = await client.call_tool(
            "list_tasks",
            {}
        )

        assert listed.is_error is False

        tasks = listed.structured_content["result"]

        assert any(
            task["id"] == task_id
            and task["title"] == "Learn MCP Integration"
            for task in tasks
        )
