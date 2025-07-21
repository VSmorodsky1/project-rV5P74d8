from typing import List

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
from rich import print

from ui.decorators import input_error
from ui.render_notes_list import render_notes_list
from ui.render_table import render_table
from models.note import Note
from models.note_book import NoteBook


def find_matched_notes(noteBook: NoteBook, input_text: str = "Enter note's title >>> "):
    title = prompt(input_text)
    notes = noteBook.find_matched_by_title(title.strip())
    if not notes:
        raise ValueError(f"Note with title [{title}] not found.")
    return (notes, title)


def render_note_list_by_title(notes: NoteBook, title: str, isNumbered: bool = False) -> None:
    list_title = f"Notes which include the '{title}'"
    render_notes_list(notes, title=list_title, isNumbered=isNumbered)


def choose_note(notes: List[Note], title: str, action: str) -> Note:

    if len(notes) == 1:
        return notes[0]

    render_note_list_by_title(notes, title, isNumbered=True)

    prompt_text = f"\nEnter number of note which you want to {action} >>> "
    user_number = prompt(prompt_text)
    idx = int(user_number) - 1
    return notes[idx]


def add_note_tags(note: Note, tags: str, noPrint: bool = False) -> Note:
    tags = tags.split(",")
    for tag in tags:
        try:
            note.add_tag(tag.strip())
            if not noPrint:
                print(f"[green]Added tag: {tag}[/]")
        except Exception as e:
            if not noPrint:
                print(f"[red]{e}[/]")


def update_tag_list(note: Note) -> None:
    old_tags = ", ".join([tag.value for tag in note.tags]) if list(note.tags) else ""
    tags = prompt(f"\nUpdate a tags list >>> ", default=old_tags).strip()
    if not tags == old_tags:
        note.remove_tags()
        add_note_tags(note, tags)


@input_error
def show_notes(noteBook: NoteBook) -> str:
    if not noteBook.data:
        return "Note book is empty."

    notes = list(noteBook.data)
    render_notes_list(notes)
    return ""


@input_error
def add_note(noteBook: NoteBook) -> str:
    title = prompt("Enter note's title >>> ")
    note = Note(title)
    noteBook.add_note(note)

    description = prompt("Enter note's description >>> ")
    if description:
        note.description = description

    tags = prompt(f"Enter tags to '{title}', use ',' like delimiter >>> ").strip()
    if tags:
        add_note_tags(note, tags)

    render_notes_list([note], title="Your notes")
    return ""


@input_error
def find_note(noteBook: NoteBook):
    notes, title = find_matched_notes(noteBook)

    render_note_list_by_title(notes, title)
    return ""


@input_error
def update_note(noteBook: NoteBook) -> str:
    notes, title = find_matched_notes(
        noteBook, input_text="Enter note's title which you want to update >>> "
    )

    note = choose_note(notes, title, "update")

    new_title = prompt("\nEdit note title >>> ", default=note.title)
    note.title = new_title

    new_desc = prompt("\nEdit note description >>> ", default=note.description)
    note.description = new_desc

    update_tag_list(note)

    render_notes_list([note], title="Updated note")
    return ""


@input_error
def delete_note(noteBook: NoteBook) -> str:
    notes, title = find_matched_notes(
        noteBook, input_text="Enter note's title which you want to delete >>> "
    )

    note = choose_note(notes, title, "delete")

    confirm = (
        prompt(f"Are you sure you want to delete note '{note.title}'? (y/n): ").strip().lower()
    )
    if confirm not in ["yes", "y"]:
        return "Canceled deletion note."
    noteBook.remove_by_title(note.title)
    return f"Note {note.title} is deleted."


@input_error
def add_tags_to_note(noteBook: NoteBook) -> str:
    notes, title = find_matched_notes(
        noteBook, input_text="Enter note's title which you want to update >>> "
    )

    note = choose_note(notes, title, "add tags")
    tags = prompt(f"Enter tags to '{title}', use ',' like delimiter >>> ").strip()

    add_note_tags(note, tags)

    render_notes_list([note], title="Note with updated tag")
    return ""


@input_error
def search_note_by_tag(noteBook: NoteBook) -> str:
    tags_list = noteBook.note_tags
    tags = WordCompleter(tags_list, ignore_case=True, sentence=True)
    tag = prompt("Enter a tag >>> ", completer=tags, complete_while_typing=True).strip().lower()

    notes = noteBook.find_matched_by_tag(tag)

    if not notes:
        return f"No note with tag '{tag}'."

    render_note_list_by_title(notes, title=f"Note with tag {tag}")
    return ""


@input_error
def updated_tags_from_note(noteBook: NoteBook) -> str:
    """Updated tag from the note list"""

    notes, title = find_matched_notes(
        noteBook, input_text="Enter note's title which you want to delete >>> "
    )

    note = choose_note(notes, title, "update tags")

    update_tag_list(note)

    render_notes_list([note], title="Updated note")
    return ""
