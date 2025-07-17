import pickle
from pathlib import Path
from models.address_book import AddressBook

DATA_FILE = Path("contacts.pkl")

def save_data(book, filename=DATA_FILE):
    """
    Save contact records to disk
    """
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename=DATA_FILE):
    """
    Load contact records from disk if file exists.
    If file not found, return new AddressBook object.
    """
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()