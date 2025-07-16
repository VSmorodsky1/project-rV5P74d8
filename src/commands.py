from decorators import input_error
from models.address_book import AddressBook
from models.record import Record
from render_table import render_table


def user_hello() -> str:
    return "How can I help you?"


@input_error
def show_all(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."
    headers = ["name", "birthday", "phones"]
    records = list(book.data)
    render_table(records, keys=headers, title="📒 Address Book")


@input_error
def add_contact(book: AddressBook, contact_data: list[str]) -> str:
    name = contact_data[0]
    phone = contact_data[1] if len(contact_data) > 1 else None
    record = book.find(name)
    message = "Contact updated."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def find_contact(book: AddressBook, contact_data: list):
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return contact


@input_error
def delete_contact(book: AddressBook, contact_data: list):
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    book.delete_record(contact.name.value)
    return f"Contact {contact.name.value} is removed."


@input_error
def add_phone(book: AddressBook) -> str:
    name = input("Enter contact's name:")
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    phone = input("Enter phone number:")
    contact.add_phone(phone)
    return f"Phone {phone} added for {name}."


@input_error
def edit_phone(book: AddressBook):
    """Edit contact's phone number"""
    try:
        name = input("Enter contact's name:")
        contact = book.find(name)
        if not contact:
            raise ValueError(f"Contact with name [{name}] not found.")

        header = ["id", "phone"]
        render_table(
            [{"id": index, "phone": phone} for index, phone in enumerate(contact.phones)],
            keys=header,
            title=f"{name}'s phones:",
        )

        id = int(input("Enter phone id to edit:"))
        new_phone = input("Enter new phone number:")
        contact.delete_phone(contact.phones[id].value)
        contact.add_phone(new_phone)
        return f"Phone number updated for {name}"
    except IndexError:
        raise IndexError(f"Phone doesn't exist.")


@input_error
def show_phone(book: AddressBook, contact_data: list) -> str:
    name = contact_data[0]
    contact = book.find(name)
    if not contact:
        raise ValueError(f"Contact with name [{name}] not found.")
    return f"{name.upper()}: {'; '.join(str(p) for p in contact.phones)}"


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
