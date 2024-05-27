# the problem can be found here: https://adventofcode.com/2022/day/14
from grid import Grid
from engine import Engine


def print_header():
    """prints the header for the terminal output"""
    header = "====== Advent of Code 2022 - Day 14 ======"
    print("=" * len(header))
    print(header)
    print("=" * len(header))


def main(example: bool = True):
    print_header()

    grid = Grid(example)

    engine = Engine(grid)

    # todo solve part 1
    part1 = engine.spawn()
    print(f"Part 1: {part1}")

    # todo solve part 2
    part2 = engine.spawn(part2=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
