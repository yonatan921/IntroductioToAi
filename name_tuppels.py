from collections import namedtuple

Point = namedtuple("Point", "x, y")
Package = namedtuple("Package", "point_org, from_time, point_dst, dead_line")
Package.__str__ = lambda self: "P".ljust(2) + " "

