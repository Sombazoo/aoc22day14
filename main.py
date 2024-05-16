# the problem can be found here: https://adventofcode.com/2022/day/14
from grid import Grid


def print_header():
    """prints the header for the terminal output"""
    header = "====== Advent of Code 2022 - Day 14 ======"
    print("=" * len(header))
    print(header)
    print("=" * len(header))


def main(example: bool = False):
    print_header()

    grid = Grid(example)

    # todo solve part 1
    # todo solve part 2


if __name__ == "__main__":
    main()
