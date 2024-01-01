from name_tuppels import Point


class Tile:
    def __init__(self, point: Point):
        self.point = point
        self.symbol = "."

    def __str__(self):
        return self.symbol.ljust(2) + " "

