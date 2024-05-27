from grid import Grid, Coordinate, Material, Object


class Engine:
    """The engine that simulates the falling sand"""

    def __init__(self, grid: Grid):
        self.grid = grid

    def spawn(self, part2: bool = False):
        """spawns a piece of sand at the source at (500, 0) and
        simulates it falling"""

        # drop sand
        num = 0
        while True:
            sand = (500, 0)
            while True:
                if self.grid.is_empty_at(Coordinate((sand[0], sand[1] + 1))):
                    sand = (sand[0], sand[1] + 1)
                elif self.grid.is_empty_at(Coordinate((sand[0] - 1, sand[1] + 1))):
                    sand = (sand[0] - 1, sand[1] + 1)
                elif self.grid.is_empty_at(Coordinate((sand[0] + 1, sand[1] + 1))):
                    sand = (sand[0] + 1, sand[1] + 1)
                else:
                    self.grid.add(Object((Material.solid_sand, Coordinate(sand))))
                    break
                if sand[1] == self.grid.get_last_row() + 1:
                    if not part2:
                        return num
                    self.grid.add(Object((Material.solid_sand, Coordinate(sand))))
                    break
            num += 1
            if sand == (500, 0):
                return num
