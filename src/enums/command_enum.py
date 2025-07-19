from enum import Enum


class CLICommand(Enum):
    SHOW_ALL = "show_all"
    ADD_CONTACT = "create_contact"
    FIND_CONTACT = "find_contact"
    FIND_CONTACT_BY_PHONE = "find_contact_by_phone"
    EDIT_NAME = "edit_name"
    DELETE_CONTACT = "delete_contact"

    SHOW_PHONE = "show_phones"
    ADD_PHONE = "add_phone"
    EDIT_PHONE = "edit_phone"
    DELETE_PHONE = "delete_phone"

    BIRTHDAYS = "birthdays"
    SHOW_BIRTHDAY = "show_birthday"
    ADD_BIRTHDAY = "add_birthday"

    ADD_EMAIL = "add_email"
    EDIT_EMAIL = "edit_email"
    DELETE_EMAIL = "delete_email"

    ADD_ADDRESS = "add_address"
    EDIT_ADDRESS = "edit_address"
    DELETE_ADDRESS = "delete_address"

    SHOW_NOTES = "show_notes"
    SEARCH_NOTE_BY_TAG = "search_note_by_tag"
    ADD_NOTE = "add_note"
    FIND_NOTE = "find_note"
    UPDATE_NOTE = "update_note"
    DELETE_NOTE = "delete_note"
    ADD_TAGS_TO_NOTE = "add_tags_to_note"
    UPDATED_TAGS_FROM_NOTE = "updated_tags_from_note"

    EXIT = "exit"
    CLOSE = "close"
    HELLO = "hello"
    HELP = "help"
