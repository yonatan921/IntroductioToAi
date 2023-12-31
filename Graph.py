from Aigent import Aigent
from Tile import Tile, Package
from name_tuppels import  Point


class Graph:
    def __init__(self, max_x: int, max_y: int, blocks: {frozenset}, fragile: {frozenset}, agents: [Aigent]):
        self.grid = None
        self.edges = None
        self.relevant_packages = set()
        self.fragile = fragile
        self.agents = agents
        self.init_grid(max_x, max_y, blocks)

    def init_grid(self, max_x, max_y, blocks: {frozenset}):
        self.grid = [[Tile(Point(i, j)) for i in range(max_x + 1)] for j in range(max_y + 1)]
        for aigent in self.agents:
            self.add_aigent(aigent)
        self.edges = self.create_neighbor_dict()
        for edge in blocks:
            self.remove_edge(edge)

    def game_over(self):
        return len(self.relevant_packages) == 0

    def add_aigent(self, aigent: Aigent):
        self.grid[aigent.point.y][aigent.point.x] = aigent

    def add_package(self, package: Package):
        self.grid[package.point.y][package.point.x] = package

    def update_packages(self, timer, packages):
        self.relevant_packages = {package for package in packages if package.from_time <= timer <= package.dead_line and not package.picked_up}
        for package in self.relevant_packages:
            self.add_package(package)

    def can_move(self, location: Point, new_location: Point):
        return self.edges[location].get(new_location) is not None

    def get_packages_to_take(self):
        return {package.point for package in self.relevant_packages}

    def get_packages_to_deliver(self):
        return {package.point_dst for package in self.relevant_packages}

    def __str__(self):
        matrix_string = "\n".join(" ".join(str(tile) for tile in row) for row in self.grid)
        return matrix_string + '\n'

    def remove_edge(self, edge: {Point}):
        p1, p2 = list(edge)
        if p1 in self.edges:
            del self.edges[p1][p2]
            del self.edges[p2][p1]

    def create_neighbor_dict(self):
        num_rows, num_cols = len(self.grid), len(self.grid[0])

        neighbor_dict = {
            Point(j, i): {
                Point(j, i - 1): 1 if i > 0 else None,
                Point(j, i + 1): 1 if i < num_rows - 1 else None,
                Point(j - 1, i): 1 if j > 0 else None,
                Point(j + 1, i): 1 if j < num_cols - 1 else None
            }
            for i in range(num_rows)
            for j in range(num_cols)
        }
        neighbor_dict = {coord: {k: v for k, v in neighbors.items() if v is not None} for coord, neighbors in
                         neighbor_dict.items()}

        return neighbor_dict

    def remove_fragile_edge(self, edge: {Point}):
        self.fragile.remove(edge)

    def remove_tile(self, point: Point):
        # remove agent
        self.grid[point.y][point.x] = Tile(point)

    def move_agent(self, org_point: Point, new_point: Point):
        # Add agent to new place
        get_agent = self.grid[org_point.y][org_point.x]
        self.grid[new_point.y][new_point.x] = get_agent

        # remove agent
        self.remove_tile(org_point)


