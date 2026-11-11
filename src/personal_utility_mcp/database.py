
import sqlite3
from pathlib import Path
from contextlib import closing


# Database location
DB_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "tasks.db"
)


# 1. Initialize Database
def init_db() -> None:
    """Initialize the SQLite database."""

    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
                    CHECK (completed IN (0, 1)),
                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()

    finally:
        connection.close()


# 2. Add Task
def add_task(title: str) -> int:
    """Add a new task and return its ID."""

    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            cursor = conn.execute(
                "INSERT INTO tasks (title) VALUES (?)",
                (title,)
            )

            task_id = cursor.lastrowid

            if task_id is None:
                raise RuntimeError("Failed to create task.")

            return task_id


# 3. List Tasks
def list_tasks() -> list[dict[str, object]]:
    """Retrieve all saved tasks."""

    with closing(sqlite3.connect(DB_PATH)) as conn:

        conn.row_factory = sqlite3.Row

        cursor = conn.execute("""
            SELECT id, title, completed, created_at
            FROM tasks
            ORDER BY id
        """)

        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    
def get_task(task_id: int) -> dict[str, object] | None:
    """Retrieve a task using its ID."""

    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.execute(
            """
            SELECT id, title, completed, created_at
            FROM tasks
            WHERE id = ?
            """,
            (task_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return dict(row)



def complete_task(task_id: int) -> bool:
    """Mark an existing task as completed."""

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            cursor = conn.execute(
                """
                UPDATE tasks
                SET completed = 1
                WHERE id = ?
                """,
                (task_id,)
            )

            return cursor.rowcount > 0


def update_task(task_id: int, title: str) -> bool:
    """Update the title of an existing task."""

    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            cursor = conn.execute(
                """
                UPDATE tasks
                SET title = ?
                WHERE id = ?
                """,
                (title, task_id)
            )

            return cursor.rowcount > 0



def delete_task(task_id: int) -> bool:
    """Delete a task using its ID."""

    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            cursor = conn.execute(
                """
                DELETE FROM tasks
                WHERE id = ?
                """,
                (task_id,)
            )

            return cursor.rowcount > 0

