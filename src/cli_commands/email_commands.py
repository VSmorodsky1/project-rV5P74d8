from ui.decorators import input_error
from models.address_book import AddressBook
from prompt_toolkit import prompt


@input_error
def add_email(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ").strip()
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    email = input("Enter contact's email >>> ")
    contact.add_email(email)
    return f"Email for {name} added."


@input_error
def edit_email(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ").strip()
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    contact_email = contact.email if contact.email.value else ""
    new_email = prompt("Edit your email >>> ", default=contact_email)
    contact.add_email(new_email)
    return f"Email for {name} updated."
