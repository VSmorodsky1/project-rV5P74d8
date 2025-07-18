from prompt_toolkit import prompt
from rich import print

from ui.decorators import input_error
from ui.render_notes_list import render_notes_list
from models.note import Note
from models.note_book import NoteBook


def find_matched_notes(noteBook: NoteBook, input_text: str = "Enter note's title >>> "):
    title = prompt(input_text)
    notes = noteBook.find_matched_by_title(title)
    if not notes:
        raise ValueError(f"Note with title [{title}] not found.")
    return (notes, title)


@input_error
def show_notes(noteBook: NoteBook):
    if not noteBook.data:
        return "Note book is empty."

    notes = list(noteBook.data)
    render_notes_list(notes)
    return ""


@input_error
def add_note(noteBook: NoteBook):
    title = prompt("Enter note's title >>> ")
    note = Note(title)
    noteBook.add_note(note)

    description = prompt("Enter note's description >>> ")
    if description:
        note.description = description
    render_notes_list([note], title="Your notes")
    return ""


@input_error
def find_note(noteBook: NoteBook):
    notes, title = find_matched_notes(noteBook)

    list_title = f"Notes which include the '{title}'"
    render_notes_list(notes, title=list_title)
    return ""


@input_error
def update_note(noteBook: NoteBook):
    notes, title = find_matched_notes(
        noteBook, input_text="Enter note's title which you want to update >>> "
    )

    if len(notes) == 1:
        note = notes[0]
    elif len(notes) > 1:
        render_notes_list(notes, title=title, isNumbered=True)
        user_number = prompt("\nEnter numder of note which you want to update  >>> ")
        idx = int(user_number) - 1
        note = notes[idx]

    new_title = prompt("\nEdit note title >>> ", default=note.title)
    note.title = new_title

    new_desc = prompt("\nEdit note description >>> ", default=note.description)
    note.description = new_desc

    render_notes_list([note], title="Note updated")
    return ""
