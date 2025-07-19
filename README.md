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

### 💾  Persistance Feature
- Store contacts and notes into files on your disk.

---

## Installation

1. Run command to install package:
```shell
pip install project-rV5P74d8
```

2. Run application:
```shell
cli-assistant
```

### Command Reference

| Command Name          | Description                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------|
| `create_contact`      | Create a contact with name and phones (optional, separated by commas) in the contact book. |
| `find_contact`        | Find a contact from the contact book by full or partial name.                               |
| `find_contact_by_phone` | Find a contact from the contact book by phone.                                            |
| `delete_contact`      | Delete a contact from the contact book.                                                     |
| `show_all`            | Show all contact info (name, phones, email, address, birthday) from the contact book.       |
| `edit_name`           | Edit a contact's name.                                                                      |
| `show_phones`         | Show all phone numbers for a contact.                                                       |
| `add_phone`           | Add phone numbers (comma-separated) to a contact.                                           |
| `edit_phone`          | Edit a contact's phone number.                                                              |
| `delete_phone`        | Delete a contact's phone number.                                                            |
| `add_address`         | Add a contact's address.                                                                    |
| `edit_address`        | Edit a contact's address.                                                                   |
| `add_birthday`        | Add a contact's birthday.                                                                   |
| `add_email`           | Add a contact's email address.                                                              |
| `edit_email`          | Edit a contact's email address.                                                             |
| `delete_email`        | Delete a contact's email address.                                                           |
| `show_birthday`       | Show all contact birthdays, matched by name (partial or full).                              |
| `birthdays`           | Show upcoming contact birthdays within a specified number of days from today.               |
| `find_note`           | Find notes by title, matching partially or fully.                                           |
| `show_notes`          | Show all notes.                                                                             |
| `add_note`            | Add a note with title and description.                                                      |
| `help`                | Show help information about available commands.  


