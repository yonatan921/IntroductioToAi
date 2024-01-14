from Aigent import Aigent, AiAigent
from Graph import Graph
from MST import MST
from Problem import Problem
from SearchALgo import GreedySearch, AStar


class GameMaster:
    def __init__(self, graph: Graph, agents: [Aigent], packages):
        self.graph = graph
        self.agents = agents
        self.turn_index = 0
        self.timer = 0
        self.all_packages = packages
        self.update_packages()
        self.aiAigent = agents[0]
        problem = Problem(self.graph, lambda g: g.game_over())
        ai_algo = AStar()
        last_node = ai_algo.run_algo(problem, lambda g: MST().run_algo(g))
        self.aiAigent.parse_move(last_node)

    def start_game(self):
        while not self.game_over():
            print(self)
            self.agents[self.turn_index % len(self.agents)].make_move(self.graph)
            self.timer += 1
            self.turn_index += 1
            self.update_packages()
        print(self)

    def game_over(self):
        return self.graph.game_over()

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
