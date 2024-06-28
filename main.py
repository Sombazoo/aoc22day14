# the problem can be found here: https://adventofcode.com/2022/day/14
from grid import Grid
from engine import Engine
import argparse


def print_header():
    """prints the header for the terminal output"""
    header = "====== Advent of Code 2022 - Day 14 ======"
    print("=" * len(header))
    print(header)
    print("=" * len(header))


def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2022 day 14.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    parser.add_argument('-e', '--example', action='store_true', help='Enable example mode')
    parser.add_argument('-i', '--interrupt', action='store_true', help='Enable interrupt mode')
    parser.add_argument('-t', '--time', type=float, help='Set verbose render speed')

    args = parser.parse_args()

    print_header()

    grid1 = Grid(args.example)
    grid2 = Grid(args.example)

    engine1 = Engine(grid1, args.time, args.verbose)
    engine2 = Engine(grid2, args.time, args.verbose)

    # todo solve part 1
    if args.interrupt:
        input("Press Enter to start part 1...")
    part1 = engine1.spawn()
    print(f"Part 1: {part1}")

    # todo solve part 2
    if args.interrupt:
        print("==========================================")
        input("Press Enter to start part 2...")
    part2 = engine2.spawn(part2=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
