from typing import List

from rich.console import Console
from rich.align import Align

from models.note import Note


def render_notes_list(notes: List[Note], title="🗒  Notes book", isNumbered=False):
    console = Console(record=True)
    console.print(Align(f"\n[b magenta]{title}:[/]", align="center"))
    for index, note in enumerate(notes, start=1):
        if isNumbered:
            console.print(f"[b green]{index}[/]")
        console.print(note.display())
    return console.export_text()
