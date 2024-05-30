# aoc22day14
Advent of Code 2022 Day 14 Solution in Python

This project is part of a proseminar at the Eberhard Karls University of Tübingen.

The Advent of Code problem can be found [here](https://adventofcode.com/2022/day/14 "Advent of Code 2022 Day 14")

## project structure
The project has a main function that is responsible for running part 1 and part 2 and taking in the flags. It also creates / generates a grid using either the example or the main input.
The grid is responsible for loading the rock structure into an 2D array and providing methodes like adding a Material to a coordinate or printing the grid to the terminal.
Finally there is the engine that simulates the fallung sand and also calculates the number of solid sand while simulating.

## running the project
To run the project execute the main file:
```
python main.py
```

It is also possible to set the following flags:
- -v, --verbose
  - Description: Enable verbose mode.
  - Usage: When this flag is set, the program will enable the output renderer.

- -e, --example
  - Description: Enable example mode.
  - Usage: Activates the example mode, which will select the example input instead of the main input for the rock structure.

- -t, --time
  - Description: Set verbose render speed in seconds.
  - Type: float
  - Usage: Specifies the speed at which verbose output is rendered in seconds. The value should be a floating-point number.

```
python main.py -vet 2
```
