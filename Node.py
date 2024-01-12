import copy

from Graph import Graph
from name_tuppels import Point


class Node:
    def __init__(self, parent, action, state, depth):
        self.parent: Node = parent
        self.action: Point = action
        self.state: Graph = state
        self.depth: int = depth
        self.path_cost: int = None

    def step_cost(self, node):
        pass

    def __key(self):
        return self.parent, self.action, self.state, self.depth, self.path_cost

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__key() == other.__key()
        return False

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def find_successors(self) -> {Point, Graph}:
        successors = {}
        for available_point in self.state.available_moves(self.state.agents[0].point):
            new_graph = copy.deepcopy(self.state)
            new_graph.agents[0].thin_move(available_point)
            successors[available_point] = new_graph

        return successors
