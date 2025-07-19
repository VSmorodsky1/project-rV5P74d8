from functools import wraps


def normalize_tag(func):
    """Decorator normalize tag"""

    @wraps(func)
    def wrapper(self, value):
        tag = value.replace(" ", "_")
        if tag.startswith("#"):
            tag = tag[1:]
        return func(self, tag)

    return wrapper
