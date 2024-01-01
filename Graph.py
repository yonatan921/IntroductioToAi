class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        min = 1e7
        node1 = None
        for node in range(self.V):
            if dist[node] < min and dist[node] != 0:
                min = dist[node]
                node1 = node
        print(f"dist: {min} node {node1}")


    def min_distance(self, dist, spt_set):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and spt_set[v] is False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, source):

        dist = [1e7] * self.V
        dist[source] = 0
        spt_set = [False] * self.V

        for x in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        spt_set[v] is False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(7)
