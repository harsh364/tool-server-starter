import asyncio
import os

import pytest

from notes_server import tools as tool_api
from notes_server.server import add_note, list_notes, reset_store, search_notes
from notes_server.store import NoteStore


def test_tool_api_isolation() -> None:
    s = NoteStore()
    tool_api.add_note(s, "u1", "alpha")
    tool_api.add_note(s, "u2", "beta")
    assert len(tool_api.list_notes(s, "u1")) == 1


def test_mcp_tool_functions() -> None:
    reset_store()
    out = add_note("alice", "meet at noon")
    assert out["text"] == "meet at noon"
    assert len(list_notes("alice")) == 1
    assert search_notes("alice", "noon")


@pytest.mark.integration
def test_stdio_lists_tools() -> None:
    if os.environ.get("RUN_MCP_INTEGRATION") != "1":
        pytest.skip("set RUN_MCP_INTEGRATION=1 to run MCP stdio integration")
    pytest.importorskip("mcp")

    async def _run() -> None:
        from mcp.client.session import ClientSession
        from mcp.client.stdio import StdioServerParameters, stdio_client

        params = StdioServerParameters(
            command="python",
            args=["-m", "notes_server"],
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                listed = await session.list_tools()
                names = {t.name for t in listed.tools}
                assert names >= {"add_note", "list_notes", "search_notes"}

    asyncio.run(_run())
