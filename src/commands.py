from prompt_toolkit import prompt
from rich.console import Console
from colorama import Fore, init

from decorators import input_error
from render_table import render_table
from models.address_book import AddressBook
from models.record import Record
from models.note import Note
from models.email import Email
from exceptions import PhoneFormatError

init(autoreset=True)


def user_hello() -> str:
    return "How can I help you?"


@input_error
def show_all(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."
    headers = ["name", "birthday", "phones", "address", "email"]
    records = list(book.data)
    render_table(records, keys=headers, title="📒 Address Book")


@input_error
def add_contact(book: AddressBook) -> str:
    name = prompt("Enter contact name >>> ")
    record = book.find(name)
    message = "Contact updated."

    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    phones = prompt("Enter phone numbers, use ',' like delimiter >>> ").strip()

    if phones:
        phones = phones.split(",")

        for phone in phones:
            try:
                record.add_phone(phone.strip())
                print(f"{Fore.GREEN}Added phone: {phone}")
            except Exception as e:
                print(f"{Fore.RED}{e}")

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
def add_phone(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    phone = input("Enter phone number:")
    contact.add_phone(phone)
    return f"Phone {phone} added for {name}."


@input_error
def edit_phone(book: AddressBook):
    """Edit contact's phone number"""
    try:
        name = input("Enter contact's name  >>> ")
        contact = book.find(name)
        if not contact:
            raise ValueError(f"Contact with name [{name}] not found.")

        header = ["id", "phone"]
        render_table(
            [{"id": index, "phone": phone} for index, phone in enumerate(contact.phones)],
            keys=header,
            title=f"{name}'s phones:",
        )

        id = int(input("Enter phone id to edit  >>> "))
        replaced_phone = contact.phones[id]
        new_phone = prompt("Enter new phone number  >>> ", default=replaced_phone.value)
        contact.add_phone(new_phone)
        del contact.phones[id]
        return f"Phone number updated for {name}"
    except IndexError:
        raise IndexError(f"Phone doesn't exist.")


@input_error
def show_phone(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"{name.upper()}: {'; '.join(str(p) for p in contact.phones)}"


@input_error
def add_birthday(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    birthday = input("Enter contact's birthday (YYYY-MM-DD) >>> ")
    contact.add_birthday(birthday)
    return f"Birthday for {name} set to {birthday}."


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


@input_error
def add_address(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    address = input("Enter contact's address >>> ")
    contact.add_address(address)
    return f"Address for {name} added."


@input_error
def add_email(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    email = input("Enter contact's email >>> ")
    contact.add_email(email)
    return f"Email for {name} added."
