from models.field import Field
from validations import validate_tag
from ui.normalize_tag import normalize_tag


class Tag(Field):

    @normalize_tag
    @validate_tag
    def __init__(self, value):

        super().__init__(value)

    @Field.value.setter
    @normalize_tag
    @validate_tag
    def value(self, value):
        super().value = value
