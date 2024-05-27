from enum import Enum

Coordinate = tuple[int, int]
Material = Enum('Material', 'air rock source solid_sand falling_sand')
Object = tuple[Material, Coordinate]


class Grid:
    """The Grid class for the Advent of Code day 14 map"""

    __grid = [[]]
    __min_x = 0
    __max_x = 0
    __min_y = 0
    __max_y = 0

    def __init__(self, example: bool = False):
        self.load_grid(example)

    def add(self, object: Object):
        try:
            x = object[1][0] - self.__min_x + 1
            self.__grid[x][object[1][1]] = object[0]
        except ValueError:
            print("""Failed to insert object:""" + str(object))
        except IndexError:
            print("""Failed to insert object: (IndexError) """ + str(object))

    def remove(self, coord: Coordinate):
        try:
            self.__grid[coord[0] - self.__min_x + 1][coord[1]] = Material.air
        except ValueError:
            print("""Failed to remove from coordinates:""" + str(coord))
        except IndexError:
            print("""Failed to remove from coordinates: (IndexError) """
                  + str(object))

    def is_empty_at(self, coord: Coordinate):
        try:
            return self.__grid[coord[0] - self.__min_x + 1][coord[1]] == Material.air
        except ValueError:
            print("""Failed to check at coordinates:""" + str(coord))
        except IndexError:
            print("""Failed to check at coordinates: (IndexError) """
                  + str(coord))
            print(self.__min_x)
            print(self.__min_y)
            print(self.__max_x)
            print(self.__max_y)
            print(coord[0] - self.__min_x + 1)
            print(coord[1])

    def at(self, coord: Coordinate):
        try:
            self.__grid[coord[0] - self.__min_x + 1][coord[1]] = Material.air
        except ValueError:
            print("""Failed to get from coordinates:""" + str(coord))
        except IndexError:
            print("""Failed to get at coordinates: (IndexError) """
                  + str(coord))

    def get_last_row(self):
        if len(self.__grid) != 0:
            return len(self.__grid[0])
        else:
            return 0

    def extract_objects(self, s: str):
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

    def calc_min_max_coords(self, coord_list):
        """extracts min_x, max_x, min_y, max_y from list of coordinates"""
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
        self.__min_x = min(min_x_list, default=0)
        self.__max_x = max(max_x_list, default=self.__min_x)
        self.__min_y = min(min_y_list, default=0)
        self.__max_y = max(max_y_list, default=self.__min_y)

    def generate_grid(self, coord_list):
        # compute the size of the structure
        self.calc_min_max_coords(coord_list)
        width = self.__max_x - self.__min_x + 2
        height = self.__max_y + 2

        # create the structur array
        self.__grid = [
                [Material.air for x in range(height)] for y in range(width)
                ]

        try:
            self.add(Object((Material.source, Coordinate((500, 0)))))

            # fill the grid with the rock positions
            for structure_coord_list in coord_list:
                prev = None
                for c in structure_coord_list:
                    if prev:
                        if c[0] - prev[0]:
                            for i in range(
                                    min(c[0], prev[0]),
                                    max(c[0], prev[0]) + 1):
                                self.add(Object((
                                    Material.rock, Coordinate((i, c[1])))))
                        elif c[1] - prev[1]:
                            for i in range(
                                    min(c[1], prev[1]),
                                    max(c[1], prev[1]) + 1):
                                self.add(Object((
                                    Material.rock, Coordinate((c[0], i)))))
                    prev = c
        except ValueError:
            print("Error: failed to generate grid! Check the input")

    def load_grid(self, example: bool):
        """loads the structures from the input file"""
        file_location = "input.txt"
        if example:
            file_location = "example.txt"
        shape_list = list()
        with open(file_location, 'r') as file:
            shapes = file.readlines()
            for shape in shapes:
                shape_list.append(self.extract_objects(shape))
        coord_list = [[s[1] for s in list] for list in shape_list]

        self.generate_grid(coord_list)
