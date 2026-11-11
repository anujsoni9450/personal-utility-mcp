
import sqlite3
import pytest

from personal_utility_mcp import database


@pytest.fixture(autouse=True)
def isolated_database(tmp_path, monkeypatch):
    """Create a fresh test database for each test."""

    test_db = tmp_path / "test_tasks.db"

    monkeypatch.setattr(
        database,
        "DB_PATH",
        test_db
    )

    database.init_db()


# Test 1: Database initialization
def test_init_db():
    task_id = database.add_task("Learn SQLite")

    # Running initialization again must not delete tasks
    database.init_db()

    assert database.get_task(task_id)["title"] == "Learn SQLite"


# Test 2: Add and retrieve a task
def test_add_task():
    task_id = database.add_task("Learn MCP")

    task = database.get_task(task_id)

    assert task["id"] == task_id
    assert task["title"] == "Learn MCP"
    assert task["completed"] == 0


# Test 3: List tasks
def test_list_tasks():
    database.add_task("Learn Python")
    database.add_task("Learn SQLite")

    tasks = database.list_tasks()

    assert len(tasks) == 2
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[1]["title"] == "Learn SQLite"


# Test 4: Complete a task
def test_complete_task():
    task_id = database.add_task("Complete project")

    result = database.complete_task(task_id)

    assert result is True
    assert database.get_task(task_id)["completed"] == 1


# Test 5: Update a task
def test_update_task():
    task_id = database.add_task("Learn Python")

    result = database.update_task(
        task_id,
        "Learn Advanced Python"
    )

    assert result is True
    assert database.get_task(task_id)["title"] == "Learn Advanced Python"


# Test 6: Delete a task
def test_delete_task():
    task_id = database.add_task("Temporary Task")

    result = database.delete_task(task_id)

    assert result is True
    assert database.get_task(task_id) is None


# Test 7: Reject empty task titles
def test_empty_title():
    with pytest.raises(ValueError):
        database.add_task("   ")

    task_id = database.add_task("Valid Task")

    with pytest.raises(ValueError):
        database.update_task(task_id, "")


# Test 8: Nonexistent task
def test_nonexistent_task():
    assert database.get_task(999999) is None
    assert database.update_task(999999, "New title") is False
    assert database.complete_task(999999) is False
    assert database.delete_task(999999) is False


# Test 9: Database persistence
def test_persistence():
    task_id = database.add_task("Persistent Task")

    # Open a separate connection to verify data on disk
    with sqlite3.connect(database.DB_PATH) as conn:
        row = conn.execute(
            "SELECT title FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

    assert row[0] == "Persistent Task"
