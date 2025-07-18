from rich.console import Console

from decorators import input_error
from models.note import Note
from models.note_book import NoteBook


@input_error
def show_notes(noteBook: NoteBook):
    if not noteBook.data:
        return "Note book is empty."

    notes = list(noteBook.data)

    console = Console(record=True)
    console.print("\n[b magenta][ali]Notes book:[/]")
    for note in notes:
        console.print(note.display(), "\n")
    console.export_text()
    return ""


@input_error
def add_note(noteBook: NoteBook):
    title = input("Enter note's title >>> ")
    note = Note(title)
    noteBook.add_note(note)

    description = input("Enter note's description >>> ")
    if description:
        note.description = description

    note_card = note.display()
    console = Console(record=True)
    console.print("\nYour notes:\n", note_card)
    console.export_text()
    return ""
