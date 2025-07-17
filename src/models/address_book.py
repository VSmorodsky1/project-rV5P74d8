from collections import UserList
from datetime import datetime, timedelta

from models.record import Record


class AddressBook(UserList):
    """
    Represents a storage for Records
    """

    def add_record(self, contact_record: Record) -> None:
        """
        Add contact into the book

        Args:
            contact_record(Record): contact data
        """
        self.data.append(contact_record)

    def find(self, name: str) -> Record | None:
        """
        Find contact in the book

        Args:
            name (str): contact name
        Return:
            Record: recorn contact data
        """
        for record in self.data:
            if record.name.value.lower() == name.lower():
                return record

    def find_by_contact_id(self, contact_id: int) -> Record | None:
        """Find contact in the book by contact_id"""

        for record in self.data:
            if record.contact_id == contact_id:
                return record

    def delete_record(self, name: str) -> None:
        """
        Remove contact from the book

        Args:
            name (str): contact name
        """
        for record in self.data:
            if record.name.value.lower() == name.lower():
                self.data.remove(record)
                return

    def get_upcoming_birthdays(self):
        """
        Get users with upcoming birthday (one week)

        Returns:
            list[dict[str, str]]: list of contacts with upcoming birthdays
        """
        birthday_limit = timedelta(weeks=1)
        birthdays_on_week = []
        current_date = datetime.today().date()
        for record in self.data:
            if not record.birthday:
                continue
            birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_congratulation_date = datetime(
                year=current_date.year, month=birthday_date.month, day=birthday_date.day
            ).date()
            birthday_next_year = datetime(
                year=current_date.year + 1,
                month=birthday_date.month,
                day=birthday_date.day,
            ).date()
            if birthday_congratulation_date < current_date:
                if birthday_next_year - current_date > birthday_limit:
                    continue
                birthday_congratulation_date = birthday_next_year
            match birthday_congratulation_date.weekday():
                case 5:
                    birthday_congratulation_date += timedelta(days=2)
                case 6:
                    birthday_congratulation_date += timedelta(days=1)
            birthdays_on_week.append(
                {
                    "name": record.name.value,
                    "birthday": record.birthday.value,
                    "congratulation_date": birthday_congratulation_date.strftime("%d.%m.%Y"),
                }
            )
        return birthdays_on_week
