# the problem can be found here: https://adventofcode.com/2022/day/14
from enum import Enum

Coordinate = tuple[int, int]
Material = Enum('Material', 'rock solid_sand falling_sand')
Object = tuple[Material, Coordinate]


def print_header():
    """prints the header for the terminal output"""
    header = "====== Advent of Code 2022 - Day 14 ======"
    print("=" * len(header))
    print(header)
    print("=" * len(header))


def extract_objects(s: str):
    """convert a string sturcture into list of coordinates"""
    object_list = list()

    # split structure
    coords = s.split(' -> ')
    for c in coords:
        x, y = c.split(',')
        try:
            o = Object((Material.rock, Coordinate((int(x), int(y)))))
            object_list.append(o)
        except ValueError:
            print("""Error:\tCould not extract coordinates!
\tPlease check the input file!""")
            return []

    return object_list


def min_max_coords(coord_list):
    """extracts ((min_x, max_x), (min_y, max_y)) from list of coordinates"""
    # Initialize lists to store extracted x and y coordinates
    x_coords = []
    y_coords = []
    min_x_list = []
    max_x_list = []
    min_y_list = []
    max_y_list = []

    # Iterate over each inner list of coordinates
    for coords in coord_list:
        # Extract the first and second parts of each coordinate tuple
        x_coords = [coord[0] for coord in coords]
        y_coords = [coord[1] for coord in coords]

        # Save min and max values of this list
        if len(x_coords) != 0:
            min_x_list.append(min(x_coords))
            max_x_list.append(max(x_coords))
        if len(y_coords) != 0:
            min_y_list.append(min(y_coords))
            max_y_list.append(max(y_coords))

    # Find the smallest and largest values of the first and second parts
    min_x = min(min_x_list, default=0)
    max_x = max(max_x_list, default=min_x)
    min_y = min(min_y_list, default=0)
    max_y = max(max_y_list, default=min_y)

    return ((min_x, max_x), (min_y, max_y))


def load_structure():
    """loads the structures from the input file"""
    shape_list = list()
    with open("input.txt", 'r') as file:
        shapes = file.readlines()
        for shape in shapes:
            shape_list.append(extract_objects(shape))
    coord_list = [[s[1] for s in list] for list in shape_list]
    print(min_max_coords(coord_list))


def main():
    print_header()
    load_structure()
    # todo solve part 1
    # todo solve part 2


if __name__ == "__main__":
    main()
