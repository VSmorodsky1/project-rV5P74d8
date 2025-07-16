from functools import wraps

from colorama import Fore, init

from exceptions import PhoneFormatError, DateFormatError, RequiredValueError

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
        except KeyError as error:
            return f"{Fore.RED}[Error] Enter the name"
        except ValueError:
            return f"{Fore.RED}[Error] Enter the argument for the command"
        except IndexError:
            return f"{Fore.RED}[Error] Enter the command with arguments"

    return inner_fn
