from collections import UserList

from models.note import Note


class NoteBook(UserList):
    """Represents a storage for Notes"""

    @property
    def note_tags(self) -> set[str]:
        return {tag.value for note in self.data for tag in note.tags}

    def add_note(self, note: Note) -> None:
        """Add note into the NoteBook"""

        self.data.append(note)

    def find_matched_by_title(self, title: str) -> list[Note] | None:
        """Find note with matched name"""

        matched_notes = [note for note in self.data if title.lower() in note.title.lower()]
        return matched_notes

    def find_matched_by_tag(self, tag: str) -> list[Note] | None:
        """Find note with matched tag"""

        normalized = tag.lower().lstrip("#")
        matched_notes = []
        for note in self.data:
            for t in note.tags:
                if t.value.lower().lstrip("#") == normalized:
                    matched_notes.append(note)
                    break
        return matched_notes

    def find_by_title(self, title: str) -> Note | None:
        """Find note by title in the NoteBook"""

        for note in self.data:
            if note.title == title:
                return note

    def remove_by_title(self, title: str) -> None:
        """Remove note by id from the book"""

        for note in self.data:
            if note.title == title:
                self.data.remove(note)
                return
