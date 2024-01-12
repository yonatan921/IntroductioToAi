from typing import Callable, Tuple

from Graph import Graph
from name_tuppels import Point


class Problem:
    def __init__(self, init_state: Graph, successor_function: Callable[[Graph], Tuple[Point, Graph]], goal_state: Callable, path_cost):
        self.init_state = init_state
        self.successor_function = successor_function
        self.goal_state = goal_state
        self.path_cost = path_cost
