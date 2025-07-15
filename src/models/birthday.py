from datetime import datetime

from models.field import Field
from exceptions import BirthdayFormatError


def validate_birthday_attr(cls):
    """
    Validate birthday value when it tries to be saved (set value in constructor or using set methods)
    """
    original_setattr = cls.__setattr__

    def custom_setattr(self, name, value):
        try:
            date_format = '%d.%m.%Y'
            date_obj = datetime.strptime(value, date_format)
            original_setattr(self, name, date_obj.strftime(date_format))
        except ValueError:
            raise BirthdayFormatError(
                f"Value [{value}] doesn't not match to format: {date_format}")

    cls.__setattr__ = custom_setattr
    return cls


@validate_birthday_attr
class Birthday(Field):
    pass
