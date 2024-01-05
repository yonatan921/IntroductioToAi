from Tile import Tile, Package
from name_tuppels import Point


class Dijkstra:
    def __init__(self, grid, edges):  # todo: add block edges
        # vertex = []
        # for tile_list in grid:
        #     for tile in tile_list:
        #         if isinstance(tile, Tile):
        #             vertex.append(tile.point)
        #         elif isinstance(tile, Package):
        #             vertex.append(tile.point)
        # self.V = vertex

        self.V = [[tile.point for tile in tile_list if isinstance(tile, Tile)] for tile_list in grid]
        self.graph = edges

    def add_edge(self, u, v):
        if u not in self.V:
            self.V.append(u)
        if v not in self.V:
            self.V.append(v)
        if u in self.graph:
            self.graph[u][v] = 1
        else:
            self.graph[u] = {v: 1}

    def printSolution(self, dist):
        min = 1e7
        node1 = None
        for node in self.V:
            if dist[node] < min and dist[node] != 0:
                min = dist[node]
                node1 = node
        print(f"dist: {min} node {node1}")

    def min_distance(self, dist, spt_set):
        min = 1e7
        min_index = None
        for v in self.V:
            x = dist[v]
            if x == 0:
                pass
            if dist[v] < min and spt_set[v] is False:
                min = dist[v]
                min_index = v

        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1:
            print(j, end=" ")
            return
        self.printPath(parent, parent[j])
        print(j, end=" ")

    def storePath(self, parent, j, path):
        if parent[j] == -1:
            # path.append(j)
            return
        self.storePath(parent, parent[j], path)
        path.append(j)

    def pick_best_dest(self, dist):
        return min(dist, key=lambda k: (dist[k], k.x, k.y))

    def dijkstra(self, source: Point, points: {Point}):
        spt_set = {point: False for point in self.V}
        # self.V = {vertex for vertex in self.V if isinstance(vertex, Point)}
        dist = {vertex: 1e7 for vertex in self.V}
        parent = {vertex: -1 for vertex in self.V}
        dist[source] = 0

        for _ in range(len(self.V)):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            if u in self.graph:
                for v in self.graph[u].keys():
                    if (self.graph[u][v] > 0 and
                            v in spt_set and spt_set[v] is False and
                            dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]
                        parent[v] = u

        dist = {point: value for point, value in dist.items() if point in points}
        dest = self.pick_best_dest(dist)
        path = []
        self.storePath(parent, dest, path)
        return path

    def dijkstra_with_dest(self, source: Point, dest: Point):
        spt_set = {point: False for row in self.V for point in row}
        # self.V = {vertex for row in self.V for vertex in row }
        dist = {vertex: 1e7 for vertex in self.V}
        parent = {vertex: -1 for vertex in self.V}  # NEW: to store the shortest path tree
        dist[source] = 0

        for _ in range(len(self.V)):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            if u in self.graph:
                for v in self.graph[u].keys():
                    if (self.graph[u][v] > 0 and
                            spt_set[v] is False and
                            dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u  # NEW: to store the shortest path tree

        # print the shortest distance and path
        print(f"The shortest distance from {source} to {dest} is {dist[dest]}.")
        return dest, dist[dest]

#
# grid = [[Tile(Point(i, j)) for i in range(5)] for j in range(4)]
# d = Dijkstra(grid)
# d.add_edge((1, 1), (1, 2))
# d.add_edge((1, 1), (2, 1))
# d.add_edge((1, 2), (1, 3))
# d.add_edge((1, 2), (2, 2))
# d.add_edge((2, 2), (3, 2))
# d.add_edge((2, 1), (3, 1))
# d.add_edge((3, 1), (3, 2))
# d.add_edge((3, 1), (4, 1))
# points = [Point(1, 3), Point(3, 2), Point(4, 1)]
#
# # d.dijkstra((1, 1), points)
# d.dijkstra_with_dest(Point(1, 1), Point(1, 3))
#
# # # usage:
# # d = Dijkstra({(1, 2)})
# # d.add_edge((1, 2), (2, 2), 5)
# # d.dijkstra_with_dest((1, 2), (2, 2))
