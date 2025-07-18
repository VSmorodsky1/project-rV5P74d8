from prompt_toolkit import prompt

from ui.decorators import input_error
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
    contact_address = contact.address.value if contact.address else ""
    address = prompt("Edit your address  >>> ", default=contact_address)
    contact.add_address(address)
    return f"Address for {name} updated."


@input_error
def delete_address(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    address = contact.address.value if contact.address else ""
    confirm = input(f"Are you sure you want to delete address '{address}'? (y/n): ").strip().lower()
    if confirm not in ["yes", "y"]:
        return "Deletion cancelled."
    contact.delete_address()
    return f"Address for contact {name} is deleted."
