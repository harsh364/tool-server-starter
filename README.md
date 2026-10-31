# Tool server starter

![CI](https://github.com/harsh364/tool-server-starter/actions/workflows/ci.yml/badge.svg)

A **minimal [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) tool server** that exposes a tiny in-memory **notes** API. Use it to learn how agents discover tools, call them over stdio, and keep state between calls.

## Tools exposed

| Tool | Description |
|------|-------------|
| `add_note` | Create a note for a user id |
| `list_notes` | List notes for a user id |
| `search_notes` | Keyword search within a user's notes |

## Run the server (stdio)

```bash
cd tool-server-starter
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

notes-mcp-server
```

Wire the server into any MCP-compatible client using **stdio** transport (see your client’s MCP config docs).

## Design

- **State:** in-process dict (swap for SQLite/Postgres in your fork)  
- **Scope:** each note belongs to a `user_id` string — mirrors multi-tenant agent setups  
- **Tests:** store/unit tests + optional MCP stdio integration (`RUN_MCP_INTEGRATION=1 pytest -m integration`)  

## License

MIT
