"""Tool implementations (testable without a live MCP session)."""

from __future__ import annotations

from notes_server.store import NoteStore


def add_note(store: NoteStore, user_id: str, text: str) -> dict:
    note = store.add(user_id, text)
    return {"id": note.id, "user_id": note.user_id, "text": note.text}


def list_notes(store: NoteStore, user_id: str) -> list[dict]:
    return [{"id": n.id, "text": n.text} for n in store.list_for_user(user_id)]


def search_notes(store: NoteStore, user_id: str, query: str) -> list[dict]:
    return [{"id": n.id, "text": n.text} for n in store.search(user_id, query)]
