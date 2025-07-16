class Address:
    def __init__(self, value: str):
        if not value:
            raise ValueError("Address cannot be empty.")
        self.value = value

    def __str__(self):
        return self.value
