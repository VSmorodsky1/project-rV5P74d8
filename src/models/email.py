from models.field import Field
from validations import validate_email


class Email(Field):
    @validate_email
    def __init__(self, value: str):
        super().__init__(value)

    @Field.value.setter
    @validate_email
    def value(self, value):
        super().value = value
        