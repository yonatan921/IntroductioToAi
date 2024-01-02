from Aigent import Aigent
from Tile import Tile
from name_tuppels import Package, Edge, Point


class Graph:
    def __init__(self, max_x: int, max_y: int, blocks: {Edge}, fragile: {Edge}, agents: [Aigent]):
        self.grid = None
        self.relevant_packages = set()
        self.blocks = blocks
        self.fragile = fragile
        self.agents = agents
        self.init_grid(max_x, max_y)

    def init_grid(self, max_x, max_y):
        self.grid = [[Tile(Point(i, j)) for i in range(max_x + 1)] for j in range(max_y + 1)]
        for aigent in self.agents:
            self.add_aigent(aigent)

    def game_over(self):
        return len(self.relevant_packages) == 0

    def add_aigent(self, aigent: Aigent):
        self.grid[aigent.point.y][aigent.point.x] = aigent

    def add_package(self, package: Package):
        self.grid[package.point_org.y][package.point_org.x] = package

    def update_packages(self, timer, packages):
        self.relevant_packages = {package for package in packages if package.from_time <= timer <= package.dead_line}
        for package in self.relevant_packages:
            self.add_package(package)

    def __str__(self):
        matrix_string = "\n".join(" ".join(str(tile) for tile in row) for row in self.grid)
        return matrix_string
