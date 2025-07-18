from decorators import input_error
from models.address_book import AddressBook
from prompt_toolkit import prompt
from render_table import render_table


@input_error
def add_birthday(book: AddressBook) -> str:
    name = input("Enter contact's name >>> ").strip()
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")

    birthday = input("Enter contact's birthday (DD.MM.YYYY) >>> ").strip()
    contact.add_birthday(birthday)
    return f"Birthday for {name} set to {birthday}."


@input_error
def show_birthday(book: AddressBook) -> str:
    """Show contact's birthday"""
    name = prompt("Enter contact full or partial name to find >>> ").strip()
    contacts = book.find_matched(name)

    if not contacts:
        raise ValueError(f"Contact with name [{name}] not found.")

    header = ["name", "birthday"]
    render_table(contacts, keys=header, title="Found birthday:")
    return ""


@input_error
def birthdays(book: AddressBook):
    upcoming_days_count = int(input("Enter upcoming days count  >>> "))
    contacts = book.get_upcoming_birthdays(upcoming_days_count)
    if not contacts:
        return (
            f"There are no contacts with upcoming birthday for nearest {upcoming_days_count} days."
        )

    header = ["name", "congratulation_date"]
    render_table(contacts, keys=header, title=f"Upcoming birthdays:")
    return ""
