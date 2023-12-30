import abc

from main import Point


class Aigent(abc.ABC):
    def __init__(self, starting_point: Point):
        self.location = starting_point

    @abc.abstractmethod
    def make_move(self):
        pass


class GreedyAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)

    def make_move(self):
        pass


class HumanAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)

    def make_move(self):
        pass


class InterferingAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)

    def make_move(self):
        pass
