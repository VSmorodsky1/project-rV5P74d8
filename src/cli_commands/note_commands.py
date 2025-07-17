from rich.console import Console

from decorators import input_error
from models.note import Note


@input_error
def add_note():
    title = input("Enter note's title >>> ")
    note = Note(title)

    description = input("Enter note's description >>> ")
    if description:
        note.description = description

    note_card = note.display()
    console = Console(record=True)
    console.print("\nYour notes:\n", note_card)
    console.export_text()
    return ""
