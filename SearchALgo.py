import abc
import heapq
from typing import Callable

from Node import Node
from Problem import Problem


class SearchALgo(abc.ABC):

    def run_algo(self, problem: Problem, heuristic: Callable):
        heap: [Node] = []
        closed: {Node: int} = {}
        while heap:
            node = heapq.heappop(heap)
            if problem.goal_state == node.state or self.check_expansion_limit(node.depth):
                return node
            if node not in closed or self.evaluation(node, heuristic) < closed[node]:
                closed[node] = self.evaluation(node, heuristic)
            successors = self.expand(node, problem)
            for successor in successors:
                heapq.heappush(heap, successor)

    def expand(self, node: Node, problem: Problem) -> {Node}:
        successors = set()
        for action, result in node.find_successors():
            s = Node(node, action, result, node.depth + 1)
            s.path_cost = node.path_cost + problem.path_cost(node.action, action)
            successors.add(s)
        return successors

    @abc.abstractmethod
    def evaluation(self, node: Node, heuristic: Callable) -> int:
        pass

    def check_expansion_limit(self, depth: int) -> bool:
        return False


class GreedySearch(SearchALgo):
    def evaluation(self, node: Node, heuristic: Callable) -> int:
        return heuristic(node)


class AStar(SearchALgo):
    def evaluation(self, node: Node, heuristic: Callable) -> int:
        return node.path_cost + heuristic(node)


class RealTimeAStar(AStar):
    def __init__(self, expansion_limit=10):
        self.expansion_limit = expansion_limit

    def check_expansion_limit(self, depth: int) -> bool:
        return self.expansion_limit == depth
