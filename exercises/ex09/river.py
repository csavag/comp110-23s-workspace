"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear
__author__ = "730552002"


class River:
    """River."""
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Age check."""
        fish_list = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_list.append(fish)
        bear_list = []
        for bear in self.bears:
            if bear.age <= 5:
                bear_list.append(bear)
        self.fish = fish_list
        self.bears = bear_list

    def remove_fish(self, amount: int):
        """The fish have been bad."""
        for i in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """Hungry bears."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Are the bears hungry?"""
        bear_list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_list.append(bear)
        self.bears = bear_list
        
    def repopulate_fish(self):
        """Tbere must be more fish!"""
        n = (len(self.fish) // 2) * 4
        for i in range(n):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Bears +=."""
        n = len(self.bears) // 2
        for i in range(n):
            self.bears.append(Bear())
    
    def view_river(self):
        """Looking at a river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bears eating
        self.bears_eating()
        # Remove hungry Bears from River
        self.check_hunger()
        # Remove old Fish and Bears from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """A whole week of river!"""
        for i in range(7):
            self.one_river_day()