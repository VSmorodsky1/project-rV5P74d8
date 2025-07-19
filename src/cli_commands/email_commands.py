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

    contact_email = contact.email.value if contact.email else ""
    new_email = prompt("Edit your email >>> ", default=contact_email)
    contact.add_email(new_email)
    return f"Email for {name} updated."


@input_error
def delete_email(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ").strip()
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    email = contact.email.value if contact.email else ""
    confirm = input(f"Are you sure you want to delete email '{email}'? (y/n): ").strip().lower()
    if confirm not in ["yes", "y"]:
        return "Deletion cancelled."

    contact.delete_email()
    return f"Email for contact [{name}] is deleted."
