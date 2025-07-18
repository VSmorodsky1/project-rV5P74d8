import sys

from colorama import Fore, init
from prompt_toolkit import prompt

from utils.parse_input import parse_input
from cli_commands.contact_commands import (
    add_contact,
    delete_contact,
    find_contact,
    find_contact_by_phone,
    show_all,
    user_hello,
    edit_name,
)
from cli_commands.phone_commands import show_phone, add_phone, edit_phone, delete_phone
from cli_commands.note_commands import add_note
from cli_commands.address_commands import add_address, edit_address, delete_address
from cli_commands.email_commands import add_email
from cli_commands.birthday_commands import add_birthday, birthdays, show_birthday
from address_book_data_management import load_data, save_data
from utils.command_completer import get_commands_list
from enums.command_enum import CLICommand

init(autoreset=True)


def main():
    book = load_data()
    noteBook = NoteBook()
    print("Welcome to Assistant Bot!")
    while True:
        try:
            user_input = (
                prompt("Enter a command >>> ", completer=get_commands_list()).strip().lower()
            )
            command, *args = parse_input(user_input)
            if command in [CLICommand.EXIT.value, CLICommand.CLOSE.value]:
                print(f"{Fore.GREEN}Goodbye!")
                break

            match command:
                case CLICommand.HELLO.value:
                    print(user_hello())
                case CLICommand.ADD_CONTACT.value:
                    print(add_contact(book))
                case CLICommand.FIND_CONTACT.value:
                    print(find_contact(book))
                case CLICommand.FIND_CONTACT_BY_PHONE:
                    print(find_contact_by_phone(book))
                case CLICommand.DELETE_CONTACT.value:
                    print(delete_contact(book))
                case CLICommand.SHOW_ALL.value:
                    print(show_all(book))
                case CLICommand.EDIT_NAME.value:
                    print(edit_name(book))
                case CLICommand.SHOW_PHONE.value:
                    print(show_phone(book))
                case CLICommand.ADD_PHONE.value:
                    print(add_phone(book))
                case CLICommand.EDIT_PHONE.value:
                    print(edit_phone(book))
                case CLICommand.DELETE_PHONE.value:
                    print(delete_phone(book))
                case CLICommand.ADD_ADDRESS.value:
                    print(add_address(book))
                case CLICommand.EDIT_ADDRESS.value:
                    print(edit_address(book))
                case CLICommand.DELETE_ADDRESS.value:
                    print(delete_address(book))
                case CLICommand.ADD_BIRTHDAY.value:
                    print(add_birthday(book))
                case CLICommand.SHOW_BIRTHDAY.value:
                    print(show_birthday(book))
                case CLICommand.BIRTHDAYS.value:
                    print(birthdays(book))
                case CLICommand.ADD_NOTE.value:
                    print(add_note(noteBook))
                case CLICommand.ADD_EMAIL.value:
                    print(add_email(book))
                case _:
                    raise ValueError(f"Command [{command}] doesn't exist")
        except TypeError as error:
            print(f"{Fore.RED}[Error] {str(error)}")
        except ValueError as error:
            print(f"{Fore.RED}[Error] {str(error)}")
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}Goodbye!")
            sys.exit(0)
        finally:
            save_data(book)


if __name__ == "__main__":
    main()
