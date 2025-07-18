from prompt_toolkit import prompt
from colorama import Fore, init

from decorators import input_error
from models.address_book import AddressBook
from render_table import render_table

init(autoreset=True)


@input_error
def add_phone(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    phones = prompt("Enter phone numbers, use ',' like delimiter >>> ").strip()
    if phones:
        phones = phones.split(",")
        for phone in phones:
            try:
                phone = phone.strip()
                contact.add_phone(phone)
                print(f"{Fore.GREEN}Added phone: {phone}")
            except Exception as e:
                print(f"{Fore.RED}Error occurs on phone value:{phone}")
                print(f"{Fore.RED}{e}")
    return f"Added phones for contact: {name}"


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
    name = prompt("Enter contact full or partial name to find >>> ")
    contacts = book.find_matched(name)

    if len(contacts) == 0:
        raise ValueError(f"Contact with name [{name}] not found.")

    header = ["name", "phones"]
    render_table(contacts, keys=header, title=f"Found phones:")
    return ""


@input_error
def delete_phone(book: AddressBook) -> None:
    """Delete phone from the contact list"""
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

        deleted_phone = contact.phones[id]
        confirm = (
            input(f"Are you sure you want to delete '{deleted_phone.value}'? (y/n): ")
            .strip()
            .lower()
        )
        if confirm not in ["yes", "y"]:
            return "Deletion cancelled."
        contact.delete_phone(deleted_phone.value)

        return f"Phone number {deleted_phone.value} is deleted for contact {name}"
    except IndexError:
        raise IndexError(f"Phone doesn't exist.")
