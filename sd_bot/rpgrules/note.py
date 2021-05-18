import uuid
from datetime import datetime


class Note(dict):
    def __init__(self, user, text):
        self.set_note_id()
        self.set_note_date()
        self.set_note_user(user)
        self.set_note_text(text)

    def set_note_id(self) -> None:
        super(Note, self).__setitem__("id", str(uuid.uuid1()))

    def set_note_date(self) -> None:
        super(Note, self).__setitem__(
            "date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    def set_note_user(self, user: str) -> None:
        if not user.strip():
            raise ValueError("User cannot be empty on note")
        super(Note, self).__setitem__("user", user)

    def set_note_text(self, text: str) -> None:
        if not text.strip():
            raise ValueError("Text cannot be empty on note")
        super(Note, self).__setitem__("text", text)


class NoteList(list):
    def add_note(self, user: str, text: str) -> str:
        note = Note(user, text)
        super(NoteList, self).append(note)
        return note["id"]

    def get_note_text(self, note_id: str) -> str:
        note_data = next(item for item in self if item["id"] == note_id)
        return note_data["text"]
