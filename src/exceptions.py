class PhoneFormatError(Exception):
    """Exception raised for errors in the phone number format."""

    def __init__(self, message="Phone number format is incorrect."):
        self.message = message
        super().__init__(self.message)


class DateFormatError(Exception):
    """Exception raised for errors in the birthday format."""

    def __init__(self, message="Birthday format is incorrect."):
        self.message = message
        super().__init__(self.message)


class RequiredValueError(Exception):
    """Exception raised when value is empty."""

    def __init__(self, message="Value cannot be empty."):
        self.message = message
        super().__init__(self.message)


class EmailFormatError(Exception):
    """Exception raised for errors in the email format."""

    def __init__(self, message="Email address format is incorrect."):
        self.message = message
        super().__init__(self.message)


class TagFormatError(Exception):
    """Exception raised for errors in the tag format."""

    def __init__(self, message="Tag format is incorrect."):
        self.message = message
        super().__init__(self.message)
