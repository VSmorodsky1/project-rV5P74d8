from prompt_toolkit import prompt

from decorators import input_error
from render_notes_list import render_notes_list
from models.note import Note
from models.note_book import NoteBook


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
    title = prompt("Enter note's title >>> ")

    notes = noteBook.find_matched_by_title(title)

    if len(notes) == 0:
        raise ValueError(f"Note with title [{title}] not found.")

    title = f"Notes which include the '{title}'"
    render_notes_list(notes, title=title)
    return ""
