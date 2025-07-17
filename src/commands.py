from rich.console import Console

from decorators import input_error
from render_table import render_table
from models.address_book import AddressBook
from models.record import Record
from models.note import Note


def user_hello() -> str:
    return "How can I help you?"


@input_error
def show_all(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."
    headers = ["name", "birthday", "phones"]
    records = list(book.data)
    render_table(records, keys=headers, title="📒 Address Book")


@input_error
def add_contact(book: AddressBook, contact_data: list[str]) -> str:
    name = contact_data[0]
    phone = contact_data[1] if len(contact_data) > 1 else None
    record = book.find(name)
    message = "Contact updated."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def find_contact(book: AddressBook):
    name = input("Enter contact full or partial name to find >>> ")
    contacts = book.find_matched(name)
    if len(contacts) == 0:
        raise ValueError(f"Contact with name [{name}] not found.")
    header = ["name", "phones", "birthday"]
    render_table(contacts, keys=header, title=f"Found contacts:")
    return


@input_error
def delete_contact(book: AddressBook, contact_data: list):
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    book.delete_record(contact.name.value)
    return f"Contact {contact.name.value} is removed."


@input_error
def change_contact(book: AddressBook, contact_data: list[str]) -> str:
    name, phone = contact_data
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    contact.add_phone(phone)
    return "Contact updated."


@input_error
def show_phone(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"{name.upper()}: {'; '.join(str(p) for p in contact.phones)}"


@input_error
def add_birthday(book: AddressBook, contact_data: list) -> str:
    name, birthday = contact_data
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    contact.add_birthday(birthday)
    return "Contact's birthday added."


@input_error
def show_birthday(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"Birthday for {name}: {contact.birthday.value}"


@input_error
def birthdays(book: AddressBook):
    celebrating_contacts = ""
    contacts = book.get_upcoming_birthdays()
    for contact in contacts:
        celebrating_contacts += f"Congratulation date for {contact.name} ({contact.birthday}): {contact.congratulation_date}\n"
    return celebrating_contacts


@input_error
def add_note():
    title = input("Please provide the note title >>> ")
    note = Note(title)

    description = input("Please provide the note description >>> ")
    if description:
        note.description = description

    note_card = note.display()
    console = Console(record=True)
    console.print("\nYour notes:\n", note_card)
    console.export_text()
    return ""
