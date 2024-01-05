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

    def move_agent(self, graph, new_location):
        """
        here move the location- check if can deliver package or take one and make sure if the edge
        we went through is fragile.
        if take or deliver package update the packages list.
        """
        edge_crossed = frozenset({self.point, new_location})
        if edge_crossed in graph.fragile:
            graph.remove_edge(edge_crossed)
            graph.remove_fragile_edge(edge_crossed)
        # pick package from new location
        taken_packages = set()
        for package in graph.relevant_packages:
            if package.point == new_location:
                taken_packages.add(package)
                self.pakages.add(package)
                package.picked_up = True
                graph.remove_tile(package.point)
        graph.relevant_packages -= taken_packages
        # deliver package
        if len(self.pakages) > 0:
            for package in self.pakages:
                if package.point_dst == new_location:
                    self.pakages.remove(package)
                    graph.remove_tile(package.point_dst)

        # move the agent

        graph.move_agent(self.point, new_location)
        self.point = new_location

    def move_agent_without_packages(self, graph, new_location):
        edge_crossed = {self.point, new_location}
        if edge_crossed in graph.fragile:
            graph.remove_edge(edge_crossed)
            graph.remove_fragile_edge(edge_crossed)
        # move the agent
        graph.move_agent(self.point, new_location)
        self.point = new_location


class StupidAigent(Aigent):

    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "A"

    def make_move(self, graph):
        dijkstra = Dijkstra(graph.grid, graph.edges)
        new_location = self.point
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
        self.move_agent(graph, new_location)



class HumanAigent(Aigent):
    def __init__(self, starting_point: Point):
        super().__init__(starting_point)
        self.symbol = "H"


    def make_move(self, graph):
        x = input("Enter your move: 'w' = up, 'a' = left, 'd' = right, 's' = down")
        if x == 'w':
            new_location = Point(self.point.x, self.point.y - 1)
        elif x == 'a':
            new_location = Point(self.point.x - 1, self.point.y)
        elif x == 'd':
            new_location = Point(self.point.x + 1, self.point.y)
        elif x == 's':
            new_location = Point(self.point.x, self.point.y + 1)
        if graph.can_move(self.point, new_location):
            self.move_agent(graph, new_location)


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
            self.move_agent_without_packages(graph, new_location)
