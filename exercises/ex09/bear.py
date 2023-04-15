"""File to define Bear class."""
__author__ = "730552002"


class Bear:
    """Bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the bears."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """A day in the life of a bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Eat."""
        self.hunger_score += num_fish