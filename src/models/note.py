from rich import print
from rich.panel import Panel

from validations import required
from models.tag import Tag


class Note:
    """Represents note title and description"""

    def __init__(self, title: str):
        self.title = title
        self.description = ""
        self.tags: list[Tag] = []

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @required
    def title(self, value: str) -> None:
        self._title = value

    def add_tag(self, tag: str) -> None:
        for tag_item in self.tags:
            if tag_item.value == tag:
                raise ValueError(f"Tag {tag} already exists.")
        self.tags.append(Tag(tag))

    def display(self):
        tags_str = ", ".join(f"#{tag.value}" for tag in self.tags)
        tags_in_panel = f"[bright_black]\n\n{tags_str}[/]" if tags_str else ""
        return Panel(f"[bold magenta]{self.title}[/]\n\n{self.description}{tags_in_panel}")

    def __str__(self):
        return f"Note title: {self.title}, description: {self.description}"

    def __repr__(self):
        return f"Note title: {self.title}, description: {self.description}"
