import abc

from Tile import Tile
from name_tuppels import Point
from Dijkstra import Dijkstra


class Aigent(abc.ABC, Tile):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.score = 0
        self.pakages = set()

    @abc.abstractmethod
    def make_move(self):
        """
        Consider fragile.
        Consider update packages.


        :return:
        """
        pass

    def update_packages(self, timer):
        self.pakages = {package for package in self.pakages if package.from_time <= timer <= package.dead_line}

    def game_over(self):
        return len(self.pakages) == 0


class GreedyAigent(Aigent):

    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "A"

    def make_move(self):
        pass


class HumanAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "H"

    def make_move(self):
        pass


class InterferingAigent(Aigent):

    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "I"

    def make_move(self):
        pass
