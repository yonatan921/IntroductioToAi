
from Aigent import AiAigent
from Graph import Graph
from Parser import Parser
from GameMaster import GameMaster
from name_tuppels import Point


def main():
    parser = Parser()
    # graph = Graph(parser.max_x, parser.max_y,  parser.blocks, parser.fragile, parser.agents, 0, parser.packages)
    graph = Graph(parser.max_x, parser.max_y, parser.blocks, parser.fragile, [AiAigent(Point(0, 0))], 0,
                  parser.packages)
    game_master = GameMaster(graph, parser.packages, parser.algo)
    game_master.start_game()


if __name__ == '__main__':
    main()
