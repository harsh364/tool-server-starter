from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Note:
    id: int
    user_id: str
    text: str


@dataclass
class NoteStore:
    _next_id: int = 1
    _notes: list[Note] = field(default_factory=list)

    def add(self, user_id: str, text: str) -> Note:
        note = Note(id=self._next_id, user_id=user_id, text=text.strip())
        self._next_id += 1
        self._notes.append(note)
        return note

    def list_for_user(self, user_id: str) -> list[Note]:
        return [n for n in self._notes if n.user_id == user_id]

    def search(self, user_id: str, query: str) -> list[Note]:
        q = query.lower()
        return [n for n in self.list_for_user(user_id) if q in n.text.lower()]
