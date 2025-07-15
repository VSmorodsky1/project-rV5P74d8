from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:
    """
    Represents contact name and list of phones
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list(Phone) = []
        self.birthday: Birthday = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def edit_phone(self, phone: str, new_phone: str) -> None:
        """
        Update contact's phone

        Args:
            phone(str): Phone number to replace
            new_phone(str): New phone number
        """
        for phone_item in self.phones:
            if phone_item.value == phone:
                phone_item.value = new_phone
                return
        raise ValueError(f"There is no phone with value: {phone}")

    def find_phone(self, phone: str) -> Phone:
        """
        Find contact's phone number

        Args:
            phone(str): Phone number to find
        """
        for phone_item in self.phones:
            if phone_item.value == phone:
                return phone_item
        raise ValueError(f"There is no phone with value: {phone}")

    def delete_phone(self, phone) -> None:
        """
        Delete contact's phone number

        Args:
            phone(str): Phone number to delete
        """
        for phone_item in self.phones:
            if phone_item.value == phone:
                self.phones.remove(phone_item)
                return
        raise ValueError(f"There is no phone with value: {phone}")

    def add_birthday(self, birthday: str) -> None:
        """
        Add contact's birthday 
        """
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name}, birthday: {self.birthday}, phones: {'; '.join(str(p) for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name}, birthday: {self.birthday}, phones: {'; '.join(str(p) for p in self.phones)}"
