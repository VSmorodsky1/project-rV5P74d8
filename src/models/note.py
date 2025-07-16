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
        self.__contact_id = None
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

    @property
    def contact_id(self) -> int:
        """Get contact id"""
        return self.__contact_id

    @contact_id.setter
    def contact_id(self):
        self.__contact_id = self.value

    def change_descriptin(self, text):
        pass

    def change_title(self, text):
        pass

    def add_contact_depends(self, id):
        pass

    def display(self):
        return Panel(f"[bold magenta]{self.title}[/]\n\n{self.description}")

    def __str__(self):
        return f"Id: {self.note_id}, Note title: {self.title}, description: {self.description}, depens to contact: {self.contact_id}"

    def __repr__(self):
        return f"Id: {self.note_id}, Note title: {self.title}, description: {self.description}, depens to contact: {self.contact_id}"
