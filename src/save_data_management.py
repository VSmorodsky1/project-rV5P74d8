import pickle
from pathlib import Path
from typing import Type, TypeVar, Union

T = TypeVar("T")


def save_data(filename: Union[str, Path], data: T) -> None:
    """
    Save class data to disk
    """
    path = Path(filename)

    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("wb") as f:
        pickle.dump(data, f)


def load_data(filename: Union[str, Path], cls: Type[T]) -> T:
    """
    Load class data from disk if file exists.
    If file not found, return new object.
    """
    path = Path(filename)
    try:
        with path.open("rb") as f:
            obj = pickle.load(f)
        if not isinstance(obj, cls):
            raise TypeError("Invalid object type provided")
        return obj
    except FileNotFoundError:
        return cls()
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")
