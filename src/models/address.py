from models.field import Field
from validations import required

class Address(Field):
    @required
    def __init__(self, value: str):
        super().__init__(value)

    @Field.value.setter
    @required
    def value(self, value: str) -> None:
        super().value = value
