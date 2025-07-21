from functools import wraps

from colorama import Fore, init

from exceptions import (
    PhoneFormatError,
    DateFormatError,
    RequiredValueError,
    EmailFormatError,
    TagFormatError,
)

init(autoreset=True)


def input_error(fn: callable):
    """Decorator to handle input errors for command functions."""

    @wraps(fn)
    def inner_fn(*args, **kwargs):
        try:
            return f"{Fore.GREEN}{fn(*args, **kwargs)}"
        except RequiredValueError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except PhoneFormatError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except DateFormatError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except EmailFormatError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except TagFormatError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except KeyError as error:
            return f"{Fore.RED}[Error] Enter the name"
        except ValueError as error:
            return f"{Fore.RED}[Error] {str(error)}"
        except IndexError as error:
            return f"{Fore.RED}[Error] Item not found"

    return inner_fn
