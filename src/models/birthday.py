from models.field import Field
from validations import validate_date


class Birthday(Field):
    @validate_date
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    @validate_date
    def value(self, value):
        super().value = value
