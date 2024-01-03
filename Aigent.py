import abc

from Tile import Tile
from name_tuppels import Point
from Dijkstra import Dijkstra


class Aigent(abc.ABC, Tile):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.score = 0
        self.pakages = set()

    @abc.abstractmethod
    def make_move(self, graph):
        """
        Consider fragile.
        Consider update packages.


        :return:
        """
        pass

    def update_packages(self, timer):
        self.pakages = {package for package in self.pakages if package.from_time <= timer <= package.dead_line}

    def game_over(self):
        return len(self.pakages) == 0

    def no_op(self):
        pass

    def move_agent(self, new_location):
        #todo:
        """
        here move the location- check if can deliver package or take one and make sure if the edge
        we went through is fragile.
        if take or deliver package update the packages list.
        """
        edge_crossed =

    def move_agent_without_packages(self, new_location):



class StupidAigent(Aigent):

    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "A"

    def make_move(self, graph):
        dijkstra = Dijkstra(graph.grid, graph.edges)
        if len(self.pakages) == 0:
            packages_to_take = graph.get_packages_to_take()
            path = dijkstra.dijkstra(self.point, packages_to_take)
            if len(path) == 0:
                self.no_op()
            else:
                new_location = path[0]
        else:
            min_distance = 1e7
            picked_dest = None
            for package in self.pakages:
                dest_point, distance = Dijkstra.dijkstra_with_dest(self.point, package.point_dst)
                if distance < min_distance:
                    min_distance = distance
                    picked_dest = dest_point
            if min_distance == 1e7:
                self.no_op()
            else:
                new_location = picked_dest
        self.move_agent(new_location)



class HumanAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "H"


    def make_move(self, graph):
        graph.__str__()
        x = input("Enter your move: 'w' = up, 'a' = left, 'd' = right, 's' = down")
        if x == 'w':
            new_location = Point(self.point.x + 1, self.point.y)
        elif x == 'a':
            new_location = Point(self.point.x, self.point.y - 1)
        elif x == 'd':
            new_location = Point(self.point.x, self.point.y + 1)
        elif x == 's':
            new_location = Point(self.point.x - 1, self.point.y)
        if graph.can_move(self.point, new_location):
            self.move_agent(new_location)


class InterferingAigent(Aigent):

    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "I"

    def make_move(self, graph):
        dijkstra = Dijkstra(graph.grid, graph.edges)
        points_of_fragile = set()
        for point in graph.fragile:
            points_of_fragile.update(point)
        path = dijkstra.dijkstra(self.point, points_of_fragile)
        if len(path) == 0:
            self.no_op()
        else:
            new_location = path[0]
            self.move_agent_without_packages(new_location)
