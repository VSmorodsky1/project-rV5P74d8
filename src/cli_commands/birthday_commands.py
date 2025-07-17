from decorators import input_error
from models.address_book import AddressBook
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
def show_birthday(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"Birthday for {name}: {contact.birthday.value}"


@input_error
def birthdays(book: AddressBook):
    upcoming_days_count = int(input("Enter upcoming days count  >>> "))
    contacts = book.get_upcoming_birthdays(upcoming_days_count)

    header = ["id", "name", "congratulation_date"]
    render_table(contacts, keys=header, title=f"Upcoming birthdays:")
    return ""
