
from personal_utility_mcp.auth import valid_bearer_token

TEST_TOKEN = "a" * 48


def test_valid_token():
    header = f"Bearer {TEST_TOKEN}".encode()
    assert valid_bearer_token(header, TEST_TOKEN)


def test_wrong_token():
    header = b"Bearer wrong-secret"
    assert not valid_bearer_token(header, TEST_TOKEN)


def test_missing_token():
    assert not valid_bearer_token(None, TEST_TOKEN)


def test_invalid_auth_scheme():
    header = f"Basic {TEST_TOKEN}".encode()
    assert not valid_bearer_token(header, TEST_TOKEN)
