from models.field import Field
from validations import validate_phone


class Phone(Field):
    @validate_phone
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    @validate_phone
    def value(self, value):
        super().value = value
