from rich.console import Console
from rich.align import Align
from prompt_toolkit import prompt

from decorators import input_error
from models.note import Note
from models.note_book import NoteBook


@input_error
def show_notes(noteBook: NoteBook):
    if not noteBook.data:
        return "Note book is empty."

    notes = list(noteBook.data)

    console = Console(record=True)
    console.print(Align("\n[b magenta]🗒 Notes book:[/]\n", align="center"))
    for note in notes:
        console.print(note.display(), "\n")
    console.export_text()
    return ""


@input_error
def add_note(noteBook: NoteBook):
    title = prompt("Enter note's title >>> ")
    note = Note(title)
    noteBook.add_note(note)

    description = prompt("Enter note's description >>> ")
    if description:
        note.description = description

    note_card = note.display()
    console = Console(record=True)
    console.print("\nYour notes:\n", note_card)
    console.export_text()
    return ""
