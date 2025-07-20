from models.name import Name
from models.phone import Phone
from models.birthday import Birthday
from models.address import Address
from models.email import Email


class Record:
    """
    Represents contact name and list of phones, birthday, email, and address
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None
        self.address: Address = None
        self.email: Email = None

    def add_phone(self, phone: str) -> None:
        for phone_item in self.phones:
            if phone_item.value == phone:
                raise ValueError(f"Phone number {phone} already exists.")
        self.phones.append(Phone(phone))

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

    def delete_phone(self, phone: str) -> None:
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

    def add_address(self, address: str) -> None:
        """
        Add contact's address
        """
        self.address = Address(address)

    def add_email(self, email: str) -> None:
        """
        Add contact's email
        """
        self.email = Email(email)

    def delete_email(self) -> None:
        """
        Delete contact's email
        """
        self.email = None

    def edit_name(self, new_name: str) -> None:
        """
        Edit contact's name
        """
        self.name = Name(new_name)

    def delete_address(self) -> None:
        """
        Delete contact's address
        """
        self.address = None

    def __str__(self):

        return f"Contact name: {self.name}, birthday: {self.birthday}, email: {self.email}, address: {self.address}, phones: {'; '.join(str(p) for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name}, birthday: {self.birthday}, email: {self.email}, address: {self.address}, phones: {'; '.join(str(p) for p in self.phones)}"
