from models.field import Field
from validations import validate_email


class Email(Field):
    def init(self, value: str):
        self._value = None
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    @validate_email
    def value(self, value):
        self._value = value

    def str(self):
        return self.value