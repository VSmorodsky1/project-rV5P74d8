from decorators import input_error
from models.address_book import AddressBook
from prompt_toolkit import prompt
from render_table import render_table


@input_error
def add_birthday(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    birthday = input("Enter contact's birthday (DD.MM.YYYY) >>> ")
    contact.add_birthday(birthday)
    return f"Birthday for {name} set to {birthday}."


@input_error
def show_birthday(book: AddressBook) -> str:
    """Show contact's birthday"""
    name = prompt("Enter contact full or partial name to find >>> ")
    contacts = book.find_matched(name)

    if len(contacts) == 0:
        raise ValueError(f"Contact with name [{name}] not found.")

    header = ["name", "birthday"]
    render_table(contacts, keys=header, title="Found birthday:")
    return ""


@input_error
def birthdays(book: AddressBook):
    celebrating_contacts = ""
    contacts = book.get_upcoming_birthdays()
    for contact in contacts:
        celebrating_contacts += f"Congratulation date for {contact.name} ({contact.birthday}): {contact.congratulation_date}\n"
    return celebrating_contacts
