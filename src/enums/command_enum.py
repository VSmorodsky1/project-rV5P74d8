from enum import Enum


class CLICommand(Enum):
    ADD_CONTACT = "add"
    DELETE_CONTACT = "delete"
    FIND_CONTACT = "find_contact"
    FIND_CONTACT_BY_PHONE = "find_contact_by_phone"
    ADD_PHONE = "add_phone"
    EDIT_PHONE = "edit_phone"
    DELETE_PHONE = "delete_phone"
    SHOW_PHONE = "phone"
    SHOW_ALL = "all"
    ADD_BIRTHDAY = "add_birthday"
    SHOW_BIRTHDAY = "show_birthday"
    BIRTHDAYS = "birthdays"
    ADD_NOTE = "add_note"
    ADD_ADDRESS = "add_address"
    ADD_EMAIL = "add_email"
    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
