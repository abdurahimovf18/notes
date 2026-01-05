from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NoteFilter:
    title_contains: str | None = None
