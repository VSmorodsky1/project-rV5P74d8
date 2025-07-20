import difflib

from ui.render_table import render_table

from enums.command_enum import CLICommand

commands_with_description = [
    {"command_name": CLICommand.HELP.value, "description": "Show list of available commands"},
    {
        "command_name": CLICommand.SHOW_ALL.value,
        "description": "Show all contacts info (name, phones, email, address, birthday) from the contact book.",
    },
    {
        "command_name": CLICommand.ADD_CONTACT.value,
        "description": "Create a contact with name and phones (optional, separated by comma) from the contact book.",
    },
    {
        "command_name": CLICommand.FIND_CONTACT.value,
        "description": "Find a contact from the contact book by full or partial name.",
    },
    {
        "command_name": CLICommand.FIND_CONTACT_BY_PHONE.value,
        "description": "Find a contact from the contact book by phone.",
    },
    {"command_name": CLICommand.EDIT_NAME.value, "description": "Edit a contact name."},
    {
        "command_name": CLICommand.DELETE_CONTACT.value,
        "description": "Delete a contact from the contact book.",
    },
    {"command_name": CLICommand.SHOW_PHONE.value, "description": "Show all contact's phones."},
    {
        "command_name": CLICommand.ADD_PHONE.value,
        "description": "Add phones, separated by comma, to contact.",
    },
    {"command_name": CLICommand.EDIT_PHONE.value, "description": "Edit contact's phone."},
    {"command_name": CLICommand.DELETE_PHONE.value, "description": "Delete contact's phone."},
    {
        "command_name": CLICommand.BIRTHDAYS.value,
        "description": "Show upcoming contact birthdays within the specified number of days from today.",
    },
    {
        "command_name": CLICommand.SHOW_BIRTHDAY.value,
        "description": "Show all contacts birthday, matched by name partially or full.",
    },
    {"command_name": CLICommand.ADD_BIRTHDAY.value, "description": "Add contact's birthday."},
    {"command_name": CLICommand.ADD_EMAIL.value, "description": "Add contact's email."},
    {"command_name": CLICommand.EDIT_EMAIL.value, "description": "Edit contact's email."},
    {"command_name": CLICommand.DELETE_EMAIL.value, "description": "Delete contact's email."},
    {"command_name": CLICommand.ADD_ADDRESS.value, "description": "Add contact's address."},
    {"command_name": CLICommand.EDIT_ADDRESS.value, "description": "Edit contact's address."},
    {"command_name": CLICommand.DELETE_ADDRESS.value, "description": "Delete contact's address."},
    {"command_name": CLICommand.SHOW_NOTES.value, "description": "Show all notes."},
    {
        "command_name": CLICommand.SEARCH_NOTE_BY_TAG.value,
        "description": "Search note by tagst.",
    },
    {
        "command_name": CLICommand.ADD_NOTE.value,
        "description": "Add note with title and description.",
    },
    {
        "command_name": CLICommand.FIND_NOTE.value,
        "description": "Find notes by title, matching partially or fully.",
    },
    {
        "command_name": CLICommand.UPDATE_NOTE.value,
        "description": "Update note by title, matching partially or fully.",
    },
    {
        "command_name": CLICommand.DELETE_NOTE.value,
        "description": "Delete note by title, matching partially or fully.",
    },
    {
        "command_name": CLICommand.ADD_TAGS_TO_NOTE.value,
        "description": "Add tagst by note title, matching partially or fully.",
    },
    {
        "command_name": CLICommand.UPDATED_TAGS_FROM_NOTE.value,
        "description": "Update tagst by note title, matching partially or fully.",
    },
    {
        "command_name": f"{CLICommand.EXIT.value} / {CLICommand.CLOSE.value}",
        "description": "Close the app.",
    },
]


def user_hello() -> str:
    return "How can I help you?"


def help() -> None:
    """
    Return command list with description
    """
    render_table(
        commands_with_description, keys=["command_name", "description"], title="Available commands:"
    )


def suggest_command(user_input: str) -> list[str]:
    """
    Guess what command client means by analysing input.

    Args
        user_input(str): User input command
    Return
        list[str]: the best matched result
    """
    return difflib.get_close_matches(
        user_input, [command.value for command in CLICommand], n=4, cutoff=0.4
    )
