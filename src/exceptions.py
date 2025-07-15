class PhoneFormatError(Exception):
    """Exception raised for errors in the phone number format."""

    def __init__(self, message="Phone number format is incorrect."):
        self.message = message
        super().__init__(self.message)


class BirthdayFormatError(Exception):
    """Exception raised for errors in the birthday format."""

    def __init__(self, message="Birthday format is incorrect."):
        self.message = message
        super().__init__(self.message)