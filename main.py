import copy

from Graph import Graph
from Node import Node
from Parser import Parser
from GameMaster import GameMaster


def main():
    parser = Parser()
    graph = Graph(parser.max_x, parser.max_y,  parser.blocks, parser.fragile, parser.agents, 0, parser.packages)
    game_master = GameMaster(graph, parser.agents, parser.packages)
    game_master.start_game()


if __name__ == '__main__':
    main()
