import pytest

from sd_bot.rpgrules.note import Note, NoteList


class TestNotes:
    def test_note(self):
        user = "USER"
        text = "TEXT"
        note = Note(user, text)
        assert note["user"] == user
        assert note["text"] == text

    def test_note_empty_user(self):
        with pytest.raises(ValueError) as excinfo:
            user = ""
            text = "TEXT"
            Note(user, text)
        assert "User cannot be empty on note" in str(excinfo.value)

    def test_note_empty_text(self):
        with pytest.raises(ValueError) as excinfo:
            user = "USER"
            text = ""
            Note(user, text)
        assert "Text cannot be empty on note" in str(excinfo.value)

    def test_add_note(self):
        notes = NoteList()
        user = "@123"
        text = "Test Note"
        note_id = notes.add_note(user, text)
        assert notes.get_note_text(note_id) == text

    def test_get_note_list(self):
        notes = NoteList()
        user_id = "@123"
        notes.add_note(user_id, "note1")
        notes.add_note(user_id, "note2")
        assert len(notes) == 2
