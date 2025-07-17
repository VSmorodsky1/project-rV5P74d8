from decorators import input_error
from models.address_book import AddressBook


@input_error
def add_email(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    email = input("Enter contact's email >>> ")
    contact.add_email(email)
    return f"Email for {name} added."
