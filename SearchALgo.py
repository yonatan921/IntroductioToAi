import abc
import heapq
from typing import Callable, Optional, Any

from Graph import Graph
from MST import MST
from Node import Node
from Problem import Problem
from name_tuppels import Point


class SearchALgo(abc.ABC):

    def run_algo(self, problem: Problem, heuristic: Callable[[Graph], int]) -> Optional[Node]:
        heap: [Node] = []
        init_node = Node(None, problem.init_state.agents[0].point, problem.init_state, 0, 0, heuristic, self.evaluation)
        heapq.heappush(heap, init_node)
        closed: {Node: int} = {}
        while heap:
            node = heapq.heappop(heap)
            if all(len(node.state.grid[i]) != 5 for i in range(4)):
                x=  6
            if problem.goal_state(node.state) or self.check_expansion_limit(node.depth):
                return node
            if node not in closed or node.evaluation < closed[node]:
                closed[node] = node.evaluation
            successors = self.expand(node)
            for successor in successors:
                if successor not in closed:
                    heapq.heappush(heap, successor)

        return None

    def expand(self, node: Node) -> {Node}:
        successors = set()
        for action, result in node.find_successors().items():
            successor = Node(parent=node, action=action, state=result, depth=node.depth + 1,
                             path_cost=node.path_cost + node.state.edge_cost(node.action, action),
                             heuristic=node.heuristic, evaluation_func=self.evaluation)
            successors.add(successor)
        return successors

    @abc.abstractmethod
    def evaluation(self, node: Node, heuristic: Callable[[Graph], int]) -> int:
        pass

    def check_expansion_limit(self, depth: int) -> bool:
        return False


class GreedySearch(SearchALgo):
    def evaluation(self, node: Node, heuristic: Callable[[Graph], int]) -> int:
        return heuristic(node.state)


class AStar(SearchALgo):
    def evaluation(self, node: Node, heuristic: Callable[[Graph], int]) -> int:
        return node.path_cost + heuristic(node.state)


class RealTimeAStar(AStar):
    def __init__(self, expansion_limit=10):
        self.expansion_limit = expansion_limit

    def check_expansion_limit(self, depth: int) -> bool:
        return self.expansion_limit == depth
