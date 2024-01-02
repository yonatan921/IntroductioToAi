from Aigent import Aigent
from Tile import Tile
from name_tuppels import Package, Point


class Graph:
    def __init__(self, max_x: int, max_y: int, blocks: {frozenset}, fragile: {frozenset}, agents: [Aigent]):
        self.grid = None
        self.egdes = None
        self.relevant_packages = set()
        self.fragile = fragile
        self.agents = agents
        self.init_grid(max_x, max_y, blocks)
        x = None

    def init_grid(self, max_x, max_y, blocks: {frozenset}):
        self.grid = [[Tile(Point(i, j)) for i in range(max_x + 1)] for j in range(max_y + 1)]
        for aigent in self.agents:
            self.add_aigent(aigent)
        self.egdes = self.create_neighbor_set() - blocks

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

    def can_move(self, location, new_location):
        pass

    def get_packages_to_take(self):


    def __str__(self):
        matrix_string = "\n".join(" ".join(str(tile) for tile in row) for row in self.grid)
        return matrix_string

    def get_neighbors(self, row, col):
        neighbors = set()
        num_rows, num_cols = len(self.grid), len(self.grid[0])

        # Check and add neighbors in the top row
        if row > 0:
            neighbors.add(Point(row - 1, col))
        # Check and add neighbors in the bottom row
        if row < num_rows - 1:
            neighbors.add(Point(row + 1, col))
        # Check and add neighbors in the left column
        if col > 0:
            neighbors.add(Point(row, col - 1))
        # Check and add neighbors in the right column
        if col < num_cols - 1:
            neighbors.add(Point(row, col + 1))

        return neighbors

    def create_neighbor_set(self):
        neighbor_set = set()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                neighbors = self.get_neighbors( i, j)
                neighbor_set.update({frozenset({Point(j, i), point}) for point in neighbors})

        return neighbor_set
