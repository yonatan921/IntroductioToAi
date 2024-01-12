from Aigent import Aigent
from Graph import Graph
from Problem import Problem


class GameMaster:
    def __init__(self, graph: Graph, agents: [Aigent], packages):
        self.graph = graph
        self.agents = agents
        self.turn_index = 0
        self.timer = 0
        self.all_packages = packages
        self.update_packages()
        self.aiAigent = agents[0]
        problem = Problem(self.graph, self.aiAigent.make_move, self.graph.game_over, self.graph.edge_cost)

    def start_game(self):
        while not self.game_over():
            print(self)
            self.agents[self.turn_index % len(self.agents)].make_move(self.graph)
            self.timer += 1
            self.turn_index += 1
            self.update_packages()
        print(self)

    def game_over(self):
        return self.graph.game_over() and all([aigent.game_over() for aigent in self.agents])

    def update_packages(self):
        self.update_graph_packages()
        self.update_aigent_packages()

    def update_aigent_packages(self):
        for aigent in self.agents:
            aigent.update_packages(self.timer)

    def update_graph_packages(self):
        self.graph.update_packages(self.timer, self.all_packages)

    def __str__(self):
        return str(self.graph)

