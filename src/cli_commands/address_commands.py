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
