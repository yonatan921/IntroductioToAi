import copy
import sys

from Dijkstra import Dijkstra
from name_tuppels import Point


class MST:

    def add_edge(self, new_edges, source, dest, weight):
        if source not in new_edges:
            new_edges[source] = {dest: weight}
        new_edges[source][dest] = weight
        if dest not in new_edges:
            new_edges[dest] = {source: weight}
        new_edges[dest][source] = weight
        return new_edges

    def extruct_relevant_points(self, graph):
        vertex = set()
        for agent in graph.agents:
            vertex.add(agent.point)
        for package in graph.relevant_packages:
            vertex.add(package.point)
            vertex.add(package.point_dst)
        return vertex

    def create_relevant_vertex_graph(self, graph):
        new_graph = copy.deepcopy(graph)
        new_edges = {}
        dijkstra = Dijkstra(graph.grid, graph.edges)
        relevant_vertex = self.extruct_relevant_points(graph)
        for vertex in relevant_vertex:
            dist = dijkstra.dijkstra_for_all_vertex(vertex, relevant_vertex)
            for point, distance in dist.items():
                if point in relevant_vertex:
                    new_edges = self.add_edge(new_edges, vertex, point, distance)
        new_graph.update_edges(new_edges)
        return new_graph

    def find_mst(self, graph):
        new_graph = copy.deepcopy(graph)
        new_edges = {}
        vertex = self.extruct_relevant_points(new_graph)
        num_of_vertices = 0
        visited = set()
        list_vertex = list(vertex)
        first = list_vertex[0]
        visited.add(first)

        while num_of_vertices < len(vertex) - 1:
            minimum = float('inf')
            a, b = Point(0, 0), Point(0, 0)

            for m in visited:
                for n in vertex:
                    if n not in visited and new_graph.edges[m][n] is not None:
                        if minimum > new_graph.edges[m][n]:
                            minimum = new_graph.edges[m][n]
                            a, b = m, n

            if b is not None:
                new_edges = self.add_edge(new_edges, a, b, new_graph.edges[a][b])
                visited.add(b)
                num_of_vertices += 1
            else:
                break

        new_graph.update_edges(new_edges)
        return new_graph




