"""MCP stdio server exposing scoped note tools."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from notes_server.store import NoteStore
from notes_server import tools as tool_api

mcp = FastMCP("notes-tool-server")
store = NoteStore()


def reset_store() -> None:
    """Test helper."""
    global store
    store = NoteStore()


@mcp.tool()
def add_note(user_id: str, text: str) -> dict:
    """Create a note for the given user."""
    return tool_api.add_note(store, user_id, text)


@mcp.tool()
def list_notes(user_id: str) -> list[dict]:
    """List all notes for the given user."""
    return tool_api.list_notes(store, user_id)


@mcp.tool()
def search_notes(user_id: str, query: str) -> list[dict]:
    """Search notes for a user containing the query substring."""
    return tool_api.search_notes(store, user_id, query)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
