# 📒 Contacts and Notes Manager

A simple CLI application for managing your personal contacts and notes. Designed to keep your address book and daily thoughts organized and accessible.

---

## 📌 Menu

- [✨ Features](#features)
- [📦 Installation](#installation)
- [📘 Command Reference](#command-reference)

## Features

### 👥 Contact Management

- Add contacts
- Store, edit, delete phone numbers per contact
- Store, edit, delete contact's email
- Store, edit, delete contact's birthday
- Store, edit, delete contact's address
- Track upcoming birthdays in defined days
- Search contacts by name (partial or full match) and phone

### 📝 Notes Management

- Add, edit, and delete notes
- Tag notes with keywords
- Search notes by title (partial or full match)

### 💾 Persistance Feature

- Store contacts and notes into files on your disk.

---

## Installation

Suggestion: You can create a virtual environment to use the package encapsulated from the system-wide Python on your OS:

```shell
python -m venv .venv
```

1. Run command to install package:

```shell
pip install project-rV5P74d8
```

### ENV variables

If variables are not set, files will be create by default in current branch with default name.

- **ADDRESS_BOOK_FILE_NAME**: custom path to address book file.
- **NOTE_BOOK_FILE_NAME**: custom path to note book file.

2. Run application:

```shell
cli-assistant
```

Alternatively, you can run assistant with your file path using next command example:

```shell
ADDRESS_BOOK_FILE_NAME=<address_book_file_path> NOTE_BOOK_FILE_NAME=<note_book_file_path> cli-assistant
```

### Command Reference

| Command Name           | Description                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| help                   | Show list of available commands                                                             |
| show_all               | Show all contacts info (name, phones, email, address, birthday) from the contact book.      |
| create_contact         | Create a contact with name and phones (optional, separated by comma) from the contact book. |
| find_contact           | Find a contact from the contact book by full or partial name.                               |
| find_contact_by_phone  | Find a contact from the contact book by phone.                                              |
| edit_name              | Edit a contact name.                                                                        |
| delete_contact         | Delete a contact from the contact book.                                                     |
| show_phones            | Show all contact's phones.                                                                  |
| add_phone              | Add phones, separated by comma, to contact.                                                 |
| edit_phone             | Edit contact's phone.                                                                       |
| delete_phone           | Delete contact's phone.                                                                     |
| birthdays              | Show upcoming contact birthdays within the specified number of days from today.             |
| show_birthday          | Show all contacts' birthdays, matched by name partially or full.                            |
| add_birthday           | Add contact's birthday.                                                                     |
| add_email              | Add contact's email.                                                                        |
| edit_email             | Edit contact's email.                                                                       |
| delete_email           | Delete contact's email.                                                                     |
| add_address            | Add contact's address.                                                                      |
| edit_address           | Edit contact's address.                                                                     |
| delete_address         | Delete contact's address.                                                                   |
| show_notes             | Show all notes.                                                                             |
| search_note_by_tag     | Search notes by tags.                                                                       |
| add_note               | Add note with title and description.                                                        |
| find_note              | Find notes by title, matching partially or fully.                                           |
| update_note            | Update note by title, matching partially or fully.                                          |
| delete_note            | Delete note by title, matching partially or fully.                                          |
| add_tags_to_note       | Add tags by note title, matching partially or fully.                                        |
| update_tags_from_note | Update tags by note title, matching partially or fully.                                     |
| exit / close           | Close the app.                                                                              |
