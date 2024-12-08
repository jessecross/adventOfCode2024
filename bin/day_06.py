import numpy as np
from collections import OrderedDict
import itertools


def read_data(data_path: str) -> list:
    """Read the data into an 2D dimensional grid."""
    grid = []
    with open(data_path) as data_file:
        for line in data_file:
            row = []
            for letter in line.strip():
                row.append(letter)
            grid.append(row)
    return np.array(grid)


def get_coords(grid: np.array, symbol: str) -> np.array:
    return np.stack(np.where(grid == symbol), axis=1)


def stepper(start_coord: list, step: list) -> list:
    """Move start_coord [x, y] in the direction of step [v, w]."""
    end_coord = [None, None]
    end_coord[0] = start_coord[0] + step[0]
    end_coord[1] = start_coord[1] + step[1]
    return end_coord


def day_06A(data_path: str) -> None:
    grid = read_data(data_path)

    guard_start_coord = get_coords(grid, "^")[0].tolist()
    obstical_coords = get_coords(grid, "#").tolist()

    # NEWS directions are based on moving through nested lists
    directions = OrderedDict(
        {
            "N": [-1, 0],
            "E": [0, 1],
            "S": [1, 0],
            "W": [0, -1],
        }
    )
    NESW = itertools.cycle(directions.keys())

    # Grid bounds
    x_max, y_max = grid.shape
    bounds = [0, 0, x_max - 1, y_max - 1]  # x_min, y_min, x_max, y_max

    def check_within_bounds(coord: list, bounds: list) -> bool:
        return (
            (coord[0] >= bounds[0])
            and (coord[0] <= bounds[2])
            and (coord[1] >= bounds[1])
            and (coord[1] <= bounds[3])
        )

    guard_coord = guard_start_coord
    direction = directions[next(NESW)]
    is_within_bounds = check_within_bounds(guard_coord, bounds)

    guard_coord_cache = []
    while is_within_bounds:
        if stepper(guard_coord, direction) in obstical_coords:
            direction = directions[next(NESW)]
        else:
            guard_coord = stepper(guard_coord, direction)
            guard_coord_cache.append(tuple(guard_coord))

        is_within_bounds = check_within_bounds(stepper(guard_coord, direction), bounds)

    distinct_guard_positions = set(guard_coord_cache)
    distinct_guard_positions_count = len(distinct_guard_positions)
    print(distinct_guard_positions_count)


test_data_path = "/home/jesse/projects/adventOfCode2024/data/day_06/test_data"
data_path = "/home/jesse/projects/adventOfCode2024/data/day_06/data"

day_06A(test_data_path)
day_06A(data_path)
