from Tile import Tile
from name_tuppels import Point


class Dijkstra:
    def __init__(self, grid):  # todo: add block edges
        self.V = grid
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.V:
            self.V.append(u)
        if v not in self.V:
            self.V.append(v)
        if u in self.graph:
            self.graph[u][v] = w
        else:
            self.graph[u] = {v: w}

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
            path.append(j)
            return
        self.storePath(parent, parent[j], path)
        path.append(j)

    def dijkstra(self, source: Point, points: [Point]):
        self.V = [vertex for vertex in self.V if vertex in points]
        dist = {vertex: 1e7 for vertex in self.V}
        dist[source] = 0
        spt_set = {vertex: False for vertex in self.V}


        for _ in range(len(self.V)):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            if u in self.graph:
                for v in self.graph[u].keys():
                    if (self.graph[u][v] > 0 and
                            spt_set[v] is False and
                            dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)
        return dist

    def dijkstra_with_dest(self, source: Point, dest: Point):
        dist = {vertex: 1e7 for vertex in self.V}
        parent = {vertex: -1 for vertex in self.V}  # NEW: to store the shortest path tree
        dist[source] = 0
        spt_set = {vertex: False for vertex in self.V}

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
        path = []
        self.storePath(parent, dest, path)
        return path


grid = [[Tile(Point(i, j)) for i in range(5)] for j in range(4)]
d = Dijkstra(grid)
d.add_edge((1, 2), (1, 3), 10)
d.add_edge((1, 2), (2, 2), 5)
d.add_edge((1, 2), (2, 1), 1)
d.add_edge((1, 3), (1, 4), 2)
points = [(1, 1), (2, 2), (1, 3)]

d.dijkstra((1, 2), points)


# # usage:
# d = Dijkstra({(1, 2)})
# d.add_edge((1, 2), (2, 2), 5)
# d.dijkstra_with_dest((1, 2), (2, 2))
