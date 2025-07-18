from rich import print
from rich.panel import Panel

from validations import required


class Note:
    """Represents note title and description"""

    _id_counter = 1

    def __init__(self, title: str):
        self.title = title
        self.description = ""
        self.__note_id = Note._id_counter
        Note._id_counter += 1

    @property
    def note_id(self) -> int:
        """Get contact id"""
        return self.__note_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @required
    def title(self, value: str) -> None:
        self._title = value

    def display(self):
        return Panel(f"[bold magenta]{self.title}[/]\n\n{self.description}")

    def __str__(self):
        return f"Id: {self.note_id}, Note title: {self.title}, description: {self.description}"

    def __repr__(self):
        return f"Id: {self.note_id}, Note title: {self.title}, description: {self.description}"
