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

    def remove_tag(self, tag) -> None:
        """Remove tag from taglist"""
        for tag_item in self.phones:
            if tag_item.value == tag:
                self.phones.remove(tag_item)
                return
        raise ValueError(f"There is no tag with value: {tag}")

    def remove_tags(self) -> None:
        """Remove all tags"""
        self.tags = []

    def display(self):
        tags_str = (
            f"[bright_black]\n\n{', '.join(f'#{tag.value}' for tag in self.tags)}[/]"
            if self.tags
            else ""
        )
        desc = f"\n\n{self.description}" if self.description else ""
        return Panel(f"[bold magenta]{self.title}[/]{desc}{tags_str}")

    def __str__(self):
        return f"Note title: {self.title}, description: {self.description}"

    def __repr__(self):
        return f"Note title: {self.title}, description: {self.description}"
