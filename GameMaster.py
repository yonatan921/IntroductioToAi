from Aigent import Aigent, AiAigent
from Graph import Graph
from MST import MST
from Problem import Problem
from SearchALgo import GreedySearch, AStar


class GameMaster:
    def __init__(self, graph: Graph, packages):
        self.graph = graph
        self.turn_index = 0
        self.all_packages = packages
        self.update_packages()
        problem = Problem(self.graph, lambda g: g.game_over())
        ai_algo = GreedySearch()
        last_node = ai_algo.run_algo(problem, lambda g: MST().run_algo(g))
        self.graph.agents[0].parse_move(last_node)

    def start_game(self):
        while not self.game_over():
            print(self)
            self.graph.timer += 1
            self.turn_index += 1
            self.update_packages()
            self.graph.agents[self.turn_index % len(self.graph.agents)].make_move(self.graph)

        print(self)

    def game_over(self):
        return self.graph.game_over()

    def update_packages(self):
        self.update_graph_packages()
        self.update_aigent_packages()

    def update_aigent_packages(self):
        for aigent in self.graph.agents:
            aigent.update_packages(self.graph.timer)

    def update_graph_packages(self):
        self.graph.update_packages()

    def __str__(self):
        return str(self.graph)
