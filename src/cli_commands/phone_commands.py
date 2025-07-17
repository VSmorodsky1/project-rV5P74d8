from prompt_toolkit import prompt

from exceptions import PhoneFormatError
from decorators import input_error
from models.address_book import AddressBook
from render_table import render_table


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
def show_phone(book: AddressBook) -> str:
    """Show contact's phone"""
    name = input("Enter contact full or partial name to find >>> ")
    contacts = book.find_matched(name)

    if len(contacts) == 0:
        raise ValueError(f"Contact with name [{name}] not found.")

    header = ["name", "phones"]
    render_table(contacts, keys=header, title=f"Found phones:")
    return ""
