from functools import wraps
import re
from datetime import datetime

from exceptions import PhoneFormatError, RequiredValueError, DateFormatError


def validate_phone(func):
    """
    Validate phone number
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        phone = kwargs.get('value') or (args[1] if len(args) > 1 else None)
        if not phone or not re.fullmatch(r"\+?\d{10,15}", phone):
            raise PhoneFormatError("Invalid phone number format")
        return func(*args, **kwargs)
    return wrapper


def required(func):
    """
    Validate phone number
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = kwargs.get('value') or (args[1] if len(args) > 1 else None)
        if not value or len(value) <= 0:
            raise RequiredValueError()
        return func(*args, **kwargs)
    return wrapper


def validate_date(func):
    """
    Validate date with format: %d.%m.%Y
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            value = kwargs.get('value') or (args[1] if len(args) > 1 else None)
            date_format = '%d.%m.%Y'
            datetime.strptime(value, date_format)
            return func(*args, **kwargs)
        except ValueError:
            raise DateFormatError(
                f"Value [{value}] doesn't not match to format: {date_format}")
    return wrapper


def validate_email(func):
    """
    Validate email format
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = kwargs.get('value') or (args[1] if len(args) > 1 else None)
        email_format = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.fullmatch(email_format, value):
            raise ValueError(f"Invalid email address: {value}")
        return func(*args, **kwargs)
    return wrapper
