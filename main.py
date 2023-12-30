from collections import namedtuple
import argparse

Point = namedtuple("Point", "x, y")
Package = namedtuple("Package", "point_org, from_time, point_dst, dead_line")
Edge = namedtuple("Edge", "point_org, point_dst")


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Pickup and Delivery")
    parser.add_argument('filename', help="Input file path for the program")
    args = parser.parse_args()
    filename = args.filename

    max_x = None
    max_y = None
    packages: [Package] = []
    blocks: [Edge] = []
    fragile: [Edge] = []
    normal_aigent: Point = None
    human_aigent: Point = None
    interfering_aigent: Point = None
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        words = line.split()
        if words:
            if command_word(words) == "X":
                max_x = parse_x(words)
            elif command_word(words) == "Y":
                max_y = parse_y(words)
            elif command_word(words) == "P":
                packages.append(parse_package(words))
            elif command_word(words) == "B":
                blocks.append(parse_blocks(words))
            elif command_word(words) == "F":
                fragile.append(parse_fragile(words))
            elif command_word(words) == "A":
                normal_aigent = parse_normal_aigent(words)
            elif command_word(words) == "H":
                human_aigent = parse_human_aigent(words)
            elif command_word(words) == "I":
                interfering_aigent = parse_interfering_aigent(words)


def command_word(words: [str]) -> str:
    return words[0][1]


def parse_x(words: [str]) -> int:
    return int(words[1])


def parse_y(words: [str]) -> int:
    return int(words[1])


def parse_package(words: [str]) -> Package:
    org_point = Point(int(words[1]), int(words[2]))
    from_time = int(words[3])
    dst_point = Point(int(words[5]), int(words[6]))
    dead_line = int(words[7])
    return Package(org_point, from_time, dst_point, dead_line)


def parse_blocks(words: [str]) -> Edge:
    org_point = Point(int(words[1]), int(words[2]))
    dst_point = Point(int(words[3]), int(words[4]))
    return Edge(org_point, dst_point)


def parse_fragile(words: [str]) -> Edge:
    org_point = Point(int(words[1]), int(words[2]))
    dst_point = Point(int(words[3]), int(words[4]))
    return Edge(org_point, dst_point)


def parse_normal_aigent(words: [str]) -> Point:
    return Point(int(words[1]), int(words[2]))


def parse_human_aigent(words: [str]) -> Point:
    return Point(int(words[1]), int(words[2]))


def parse_interfering_aigent(words: [str]) -> Point:
    return Point(int(words[1]), int(words[2]))


if __name__ == '__main__':
    main()
