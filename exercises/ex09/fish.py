"""File to define Fish class."""
__author__ = "730552002"


class Fish:
    """Fish."""
    age: int

    def __init__(self):
        """Begin fish."""
        self.age = 0

    def one_day(self):
        """Fish day."""
        self.age += 1