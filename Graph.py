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
            self.add_package(package)

        for aigent in self.agents:
            self.add_aigent(aigent)

    def game_over(self):
        return len(self.packages) == 0

    def add_aigent(self, aigent: Aigent):
        self.grid[aigent.location.y][aigent.location.x] += str(aigent)

    def add_package(self, package: Package):
        self.grid[package.point_org.y][package.point_org.x] += "P"

    def __str__(self):
        result = ""
        for row in self.grid:
            for cell in row:
                if cell == "":
                    result += ".".ljust(2) + " "  # Replace empty cells with "."
                else:
                    result += cell.ljust(2) + " "  # Keep non-empty cells as they are
            result += "\n"  # Move to the next line after each row
        return result
