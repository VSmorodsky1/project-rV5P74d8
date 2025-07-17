import sys

from colorama import Fore, init

from utils import parse_input
from cli_commands.contact_commands import (
    add_contact,
    delete_contact,
    find_contact,
    show_all,
    user_hello,
)
from cli_commands.phone_commands import show_phone, add_phone, edit_phone
from cli_commands.note_commands import add_note
from cli_commands.address_commands import add_address
from cli_commands.email_commands import add_email
from cli_commands.birthday_commands import add_birthday, birthdays, show_birthday
from address_book_data_management import load_data, save_data

init(autoreset=True)


def main():
    book = load_data()
    print("Welcome to Assistant Bot!")
    while True:
        try:
            user_input = input("Enter a command >>> ").strip().lower()
            command, *args = parse_input(user_input)
            if command in ["exit", "close"]:
                print(f"{Fore.GREEN}Goodbye!")
                break

            match command:
                case "hello":
                    print(user_hello())
                case "add":
                    print(add_contact(book))
                case "find_contact":
                    find_contact(book)
                case "add_phone":
                    print(add_phone(book))
                case "edit_phone":
                    print(edit_phone(book))
                case "delete":
                    print(delete_contact(book, args))
                case "phone":
                    print(show_phone(book, args))
                case "all":
                    show_all(book)
                case "add_birthday":
                    print(add_birthday(book))
                case "show-birthday":
                    print(show_birthday(book, args))
                case "birthdays":
                    print(birthdays(book))
                case "add_note":
                    print(add_note())
                case "add_address":
                    print(add_address(book))
                case "add_email":
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
