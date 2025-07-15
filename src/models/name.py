from models.field import Field
from validations import required


class Name(Field):
    @required
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    @required
    def value(self, value):
        super().value = value
