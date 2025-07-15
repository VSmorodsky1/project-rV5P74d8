import sys

from colorama import Fore, Style

from utils import parse_input
from commands import add_contact, change_contact, show_phone, user_hello, add_birthday, birthdays, find_contact, delete_contact, show_birthday
from models.address_book import AddressBook


def main():
    book = AddressBook()
    print("Welcome to Assistant Bot!")
    while True:
        try:
            user_input = input("Enter a command:").strip().lower()
            command, *args = parse_input(user_input)
            if command in ["exit", "close"]:
                print(f"{Fore.GREEN}Good bye! {Style.RESET_ALL}")
                break

            match command:
                case 'hello':
                    print(user_hello())
                case 'add':
                    print(add_contact(book, args))
                case 'change':
                    print(change_contact(book, args))
                case 'find':
                    print(find_contact(book, args))
                case 'delete':
                    print(delete_contact(book, args))
                case 'phone':
                    print(show_phone(book, args))
                case 'all':
                    for contact in book:
                        print(f"{Fore.GREEN}- {contact} {Style.RESET_ALL}")
                case 'add-birthday':
                    print(add_birthday(book, args))
                case 'show-birthday':
                    print(show_birthday(book, args))
                case 'birthdays':
                    print(birthdays(book))
                case _:
                    raise ValueError(f"Command [{command}] doesn't exist")
        except TypeError as error:
            print(f"{Fore.RED}[Error] {str(error)} {Style.RESET_ALL}")
        except ValueError as error:
            print(f"{Fore.RED}[Error] {str(error)} {Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}Good bye! {Style.RESET_ALL}")
            sys.exit(0)


if __name__ == '__main__':
    main()
