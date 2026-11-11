import pytest

from personal_utility_mcp.tools import (
    add,
    multiply,
    subtract,
    divide,
    get_server_status,
)


def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(5, 4) == 20


def test_subtract():
    assert subtract(20, 8) == 12


def test_divide():
    assert divide(20, 4) == 5


def test_divide_decimal():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_server_status():
    result = get_server_status()

    assert result["server_name"] == "Personal Utility Hub"
    assert result["status"] == "running"
    assert result["transport"] == "STDIO"