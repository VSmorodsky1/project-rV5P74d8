from collections import UserList

from models.note import Note


class NoteBook(UserList):
    """Represents a storage for Notes"""

    def add_note(self, note: Note) -> None:
        """Add note into the NoteBook"""

        self.data.append(note)

    def find_matched_by_title(self, title: str) -> list[Note] | None:
        """Find note with matched name"""
        matched_notes = [note for note in self.data if title.lower() in note.title.lower()]
        return matched_notes

    def find_by_title(self, title: str) -> Note | None:
        """Find note by title in the NoteBook"""

        for note in self.data:
            if note.title == title:
                return note

    def remove_by_note_id(self, id: int) -> None:
        """Remove note by id from the book"""

        for note in self.data:
            if note.id.value == id:
                self.data.remove(note)
                return
