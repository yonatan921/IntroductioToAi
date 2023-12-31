from Aigent import Aigent
from Graph import Graph


class GameMaster:
    def __init__(self, graph: Graph, agents: [Aigent]):
        self.graph = graph
        self.agents = agents
        self.turn_index = 0

    def start_game(self):
        while not self.game_over():
            print(self)
            self.agents[self.turn_index % len(self.agents)].make_move()
            self.turn_index += 1

    def game_over(self):
        return self.graph.game_over()

    def __str__(self):
        return str(self.graph)

