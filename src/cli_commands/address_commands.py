from prompt_toolkit import prompt

from decorators import input_error
from models.address_book import AddressBook


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
def edit_address(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    address = prompt("Edit your address  >>> ", default=contact.address.value)
    contact.add_address(address)
    return f"Address for {name} updated."


@input_error
def delete_address(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    confirm = (
        input(f"Are you sure you want to delete '{contact.name.value}'? (y/n): ").strip().lower()
    )
    if confirm not in ["yes", "y"]:
        return "Deletion cancelled."
    contact.delete_address()
    return f"Address for contact {name} is deleted."
