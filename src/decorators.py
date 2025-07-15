from functools import wraps

from colorama import Fore, Style

from exceptions import PhoneFormatError, DateFormatError, RequiredValueError


def input_error(fn: callable):
    """Decorator to handle input errors for command functions."""
    @wraps(fn)
    def inner_fn(*args, **kwargs):
        try:
            return f"{Fore.GREEN}{fn(*args, **kwargs)}{Style.RESET_ALL}"
        except RequiredValueError as error:
            return f"{Fore.RED}[Error] {str(error)} {Style.RESET_ALL}"
        except PhoneFormatError as error:
            return f"{Fore.RED}[Error] {str(error)} {Style.RESET_ALL}"
        except DateFormatError as error:
            return f"{Fore.RED}[Error] {str(error)} {Style.RESET_ALL}"
        except KeyError as error:
            return f"{Fore.RED}[Error] Enter the name {Style.RESET_ALL}"
        except ValueError:
            return f"{Fore.RED}[Error] Enter the argument for the command {Style.RESET_ALL}"
        except IndexError:
            return f"{Fore.RED}[Error] Enter the command with arguments {Style.RESET_ALL}"
    return inner_fn
