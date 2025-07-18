from rich import print
from rich.panel import Panel

from validations import required


class Note:
    """Represents note title and description"""

    def __init__(self, title: str):
        self.title = title
        self.description = ""

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
        return f"Note title: {self.title}, description: {self.description}"

    def __repr__(self):
        return f"Note title: {self.title}, description: {self.description}"
