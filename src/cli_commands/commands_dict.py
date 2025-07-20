from enums.command_enum import CLICommand
from cli_commands.contact_commands import (
    add_contact,
    find_contact,
    find_contact_by_phone,
    delete_contact,
    show_all,
    edit_name,
)
from cli_commands.phone_commands import show_phone, add_phone, edit_phone, delete_phone
from cli_commands.address_commands import add_address, edit_address, delete_address
from cli_commands.email_commands import add_email, edit_email, delete_email
from cli_commands.birthday_commands import add_birthday, birthdays, show_birthday
from cli_commands.note_commands import (
    show_notes,
    add_note,
    find_note,
    update_note,
    delete_note,
    add_tags_to_note,
    search_note_by_tag,
    updated_tags_from_note,
)

contact_commands_dict = {
    CLICommand.ADD_CONTACT.value: add_contact,
    CLICommand.FIND_CONTACT.value: find_contact,
    CLICommand.FIND_CONTACT_BY_PHONE.value: find_contact_by_phone,
    CLICommand.DELETE_CONTACT.value: delete_contact,
    CLICommand.SHOW_ALL.value: show_all,
    CLICommand.EDIT_NAME.value: edit_name,
    CLICommand.SHOW_PHONE.value: show_phone,
    CLICommand.ADD_PHONE.value: add_phone,
    CLICommand.EDIT_PHONE.value: edit_phone,
    CLICommand.DELETE_PHONE.value: delete_phone,
    CLICommand.ADD_ADDRESS.value: add_address,
    CLICommand.EDIT_ADDRESS.value: edit_address,
    CLICommand.DELETE_ADDRESS.value: delete_address,
    CLICommand.ADD_EMAIL.value: add_email,
    CLICommand.EDIT_EMAIL.value: edit_email,
    CLICommand.DELETE_EMAIL.value: delete_email,
    CLICommand.ADD_BIRTHDAY.value: add_birthday,
    CLICommand.BIRTHDAYS.value: birthdays,
    CLICommand.SHOW_BIRTHDAY.value: show_birthday,
}

note_commands_dict = {
    CLICommand.SHOW_NOTES.value: show_notes,
    CLICommand.ADD_NOTE.value: add_note,
    CLICommand.FIND_NOTE.value: find_note,
    CLICommand.UPDATE_NOTE.value: update_note,
    CLICommand.DELETE_NOTE.value: delete_note,
    CLICommand.ADD_TAGS_TO_NOTE.value: add_tags_to_note,
    CLICommand.SEARCH_NOTE_BY_TAG.value: search_note_by_tag,
    CLICommand.UPDATED_TAGS_FROM_NOTE.value: updated_tags_from_note,
}
