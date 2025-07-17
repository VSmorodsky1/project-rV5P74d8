from prompt_toolkit import prompt
from colorama import Fore, init

from decorators import input_error
from validations import validate_phone
from models.address_book import AddressBook
from models.phone import Phone
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
    contact = book.find(name)
    message = "Contact updated."

    if not contact:
        contact = Record(name)
        book.add_record(contact)
        message = "Contact added."

    phones = prompt("Enter phone numbers, use ',' like delimiter >>> ").strip()

    if phones:
        phones = phones.split(",")

        for phone in phones:
            try:
                contact.add_phone(phone.strip())
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
def find_contact_by_phone(book: AddressBook):
    phone = Phone(input("Enter phone number >>> ").strip()).value

    contacts = book.find_by_phone(phone)
    if not contacts:
        raise ValueError(f"Contact with phone [{phone}] not found.")
    render_table(contacts, keys=["name", "phones", "birthday"], title="Found contacts:")
    return ""


@input_error
def delete_contact(book: AddressBook, contact_data: list):
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    book.delete_record(contact.name.value)
    return f"Contact {contact.name.value} is removed."
