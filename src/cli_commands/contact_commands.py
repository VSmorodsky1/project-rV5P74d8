from prompt_toolkit import prompt
from colorama import Fore, init

from decorators import input_error
from models.address_book import AddressBook
from models.record import Record
from render_table import render_table

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
    name = input("Enter contact name >>> ")
    contacts = book.find_matched(name)
    if len(contacts) == 0:
        raise ValueError(f"Contact with name [{name}] not found.")
    header = ["name", "phones", "birthday"]
    render_table(contacts, keys=header, title=f"Found contacts:")
    return


@input_error
def delete_contact(book: AddressBook):
    name = input("Enter contact name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    confirm = (
        input(f"Are you sure you want to delete '{contact.name.value}'? (y/n): ").strip().lower()
    )
    if confirm not in ["yes", "y"]:
        return "Deletion cancelled."
    book.delete_record(contact.name.value)
    return f"Contact {contact.name.value} is removed."
