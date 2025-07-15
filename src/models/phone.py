import re

from models.field import Field
from exceptions import PhoneFormatError


def validate_phone_attr(cls):
    """
    Validate value when it tries to be saved (set value in constructor or using set methods)
    """
    original_setattr = cls.__setattr__

    def custom_setattr(self, name, value):
        if re.match(r'^\d{10}$', value) is None:
            raise PhoneFormatError("Phone value must consists of 10 digits")
        original_setattr(self, name, value)

    cls.__setattr__ = custom_setattr
    return cls


@validate_phone_attr
class Phone(Field):
    pass
