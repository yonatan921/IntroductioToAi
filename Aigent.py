import abc

from name_tuppels import Point


class Aigent(abc.ABC):
    def __init__(self, starting_point: Point):
        self.location = starting_point
        self.score = 0

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def make_move(self):
        pass


class GreedyAigent(Aigent):
    def make_move(self):
        pass

    def __str__(self):
        return "A"


class HumanAigent(Aigent):
    def make_move(self):
        pass

    def __str__(self):
        return "H"


class InterferingAigent(Aigent):
    def make_move(self):
        pass

    def __str__(self):
        return "I"
