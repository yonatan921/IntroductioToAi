from Graph import Graph
from Parser import Parser
from GameMaster import GameMaster


def main():
    parser = Parser()
    graph = Graph(parser.max_x, parser.max_y, parser.packages, parser.blocks, parser.fragile, parser.agents)
    game_master = GameMaster(graph, parser.agents)
    game_master.start_game()


if __name__ == '__main__':
    main()
