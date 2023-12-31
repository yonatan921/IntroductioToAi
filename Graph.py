from Aigent import Aigent
from name_tuppels import Package, Edge


class Graph:
    def __init__(self, max_x: int, max_y: int, packages: {Package}, blocks: {Edge}, fragile: {Edge}, agents: [Aigent]):
        self.grid = None
        self.packages = packages
        self.blocks = blocks
        self.fragile = fragile
        self.agents = agents
        self.init_grid(max_x, max_y)

    def init_grid(self, max_x, max_y):
        self.grid = [["" for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for package in self.packages:
            self.grid[package.point_org.y][package.point_org.x] += "P"

        for aigent in self.agents:
            self.grid[aigent.location.x][aigent.location.y] += str(aigent)

    def game_over(self):
        return len(self.packages) == 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
