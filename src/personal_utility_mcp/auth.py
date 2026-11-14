
import hmac
import os

from starlette.responses import JSONResponse


def valid_bearer_token(header: bytes | None, expected_token: str) -> bool:
    """Check an Authorization: Bearer header."""
    if not header:
        return False

    try:
        scheme, token = header.decode("ascii").split(" ", 1)
    except (UnicodeDecodeError, ValueError):
        return False

    return (
        scheme.lower() == "bearer"
        and hmac.compare_digest(token, expected_token)
    )


class BearerTokenMiddleware:
    """Protect every HTTP request to the MCP application."""

    def __init__(self, app):
        self.app = app
        self.token = os.getenv("MCP_API_TOKEN")

        if not self.token or len(self.token) < 32:
            raise RuntimeError(
                "MCP_API_TOKEN must be set to a strong secret."
            )

    async def __call__(self, scope, receive, send):
        # Let ASGI startup/shutdown events work normally.
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        headers = [
            value
            for name, value in scope.get("headers", [])
            if name.lower() == b"authorization"
        ]

        if len(headers) != 1 or not valid_bearer_token(
            headers[0], self.token
        ):
            response = JSONResponse(
                {"error": "Unauthorized"},
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"},
            )
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)
