import os
import sys

from colorama import Fore, init
from prompt_toolkit import prompt
from dotenv import load_dotenv

from utils.parse_input import parse_input
from cli_commands.commands_dict import contact_commands_dict, note_commands_dict
from save_data_management import load_data, save_data
from utils.command_completer import get_commands_list
from enums.command_enum import CLICommand
from cli_commands.help import help, suggest_command, user_hello
from models.note_book import NoteBook
from models.address_book import AddressBook

init(autoreset=True)
load_dotenv()

ADDRESS_BOOK_FILE_NAME = os.getenv("ADDRESS_BOOK_FILE_NAME", "contacts.pkl")
NOTE_BOOK_FILE_NAME = os.getenv("NOTE_BOOK_FILE_NAME", "notes.pkl")


def main():
    book = load_data(ADDRESS_BOOK_FILE_NAME, AddressBook)
    noteBook = load_data(NOTE_BOOK_FILE_NAME, NoteBook)
    print("Welcome to Assistant Bot!")
    help()
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
                case CLICommand.HELP.value:
                    help()
                case key if key in contact_commands_dict:
                    print(contact_commands_dict[key](book))
                case key if key in note_commands_dict:
                    print(note_commands_dict[key](noteBook))
                case _:
                    suggested_command = suggest_command(command)
                    if not suggested_command:
                        raise ValueError(f"Command [{command}] doesn't exist")
                    print(
                        f"{Fore.YELLOW}Maybe do you mean one of these commands: {suggested_command}?\nEnter `help` command to check whole command list."
                    )
        except TypeError as error:
            print(f"{Fore.RED}[Error] {str(error)}")
        except ValueError as error:
            print(f"{Fore.RED}[Error] {str(error)}")
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}Goodbye!")
            sys.exit(0)
        finally:
            save_data(ADDRESS_BOOK_FILE_NAME, book)
            save_data(NOTE_BOOK_FILE_NAME, noteBook)


if __name__ == "__main__":
    main()
