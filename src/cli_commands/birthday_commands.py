from decorators import input_error
from models.address_book import AddressBook


@input_error
def add_birthday(book: AddressBook, contact_data: list) -> str:
    name, birthday = contact_data
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    contact.add_birthday(birthday)
    return "Contact's birthday added."


@input_error
def show_birthday(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"Birthday for {name}: {contact.birthday.value}"


@input_error
def birthdays(book: AddressBook):
    celebrating_contacts = ""
    contacts = book.get_upcoming_birthdays()
    for contact in contacts:
        celebrating_contacts += f"Congratulation date for {contact.name} ({contact.birthday}): {contact.congratulation_date}\n"
    return celebrating_contacts
