def read_data(data_path: str) -> list:
    """Read the data into an 2D dimensional grid."""
    grid = []
    with open(data_path) as data_file:
        for line in data_file:
            row = []
            for letter in line.strip():
                row.append(letter)
            grid.append(row)
    return grid


def collect_letter_coordinates(grid: list) -> dict:
    """Parse the grid for the letter coordinates and collect into a dict."""
    xmas_dict = {"X": [], "M": [], "A": [], "S": []}
    for letter in xmas_dict.keys():
        for x, row in enumerate(grid):
            for y, l in enumerate(row):
                if l == letter:
                    xmas_dict[letter].append([x, y])
    return xmas_dict


def stepper(start_coord: list, step: list) -> list:
    """Move start_coord [x, y] in the direction of step [v, w]."""
    end_coord = [None, None]
    end_coord[0] = start_coord[0] + step[0]
    end_coord[1] = start_coord[1] + step[1]
    return end_coord


def count_number_of_xmas(xmas_dict: dict) -> int:
    """For each direction, see if you can spell XMAS by travelling along that direction."""
    directions = {
        "N": [0, 1],
        "NE": [1, 1],
        "E": [1, 0],
        "SE": [1, -1],
        "S": [0, -1],
        "SW": [-1, -1],
        "W": [-1, 0],
        "NW": [-1, 1],
    }

    counter = 0
    for _, step in directions.items():
        for x_coord in xmas_dict["X"]:
            step_coord = stepper(x_coord, step)
            if step_coord in xmas_dict["M"]:
                step_coord = stepper(step_coord, step)
                if step_coord in xmas_dict["A"]:
                    step_coord = stepper(step_coord, step)
                    if step_coord in xmas_dict["S"]:
                        counter += 1

    return counter


def day_04_A(data_path: str) -> None:
    grid = read_data(data_path)
    xmas_dict = collect_letter_coordinates(grid)
    number_of_xmas = count_number_of_xmas(xmas_dict)
    print(number_of_xmas)


test_data_path = "/home/jesse/projects/adventOfCode2024/data/day_04/test_data"
test_data_02_path = "/home/jesse/projects/adventOfCode2024/data/day_04/test_data_02"
data_path = "/home/jesse/projects/adventOfCode2024/data/day_04/data"

# day_04_A(test_data_path)
# day_04_A(test_data_02_path)
# day_04_A(data_path)


def collect_letter_coordinates_v2(grid: list) -> dict:
    """Parse the grid for the letter coordinates and collect into a dict."""
    mas_dict = {"M": [], "A": [], "S": []}
    for letter in mas_dict.keys():
        for x, row in enumerate(grid):
            for y, l in enumerate(row):
                if l == letter:
                    mas_dict[letter].append([x, y])
    return mas_dict


def count_number_of_mas(mas_dict: dict) -> int:
    """For each 'A' coordinate,
    - Take a step in each diagonal direction
    - Match each diagonal coordinate pair with each letter pair
    - Match each combo condition
    - Where they match to form an X count them
    """
    directions = {
        "NE": [1, 1],
        "SE": [1, -1],
        "SW": [-1, -1],
        "NW": [-1, 1],
    }

    counter = 0
    for a_coord in mas_dict["A"]:
        top_right = stepper(a_coord, directions["NE"])
        bottem_left = stepper(a_coord, directions["SW"])
        bottom_right = stepper(a_coord, directions["SE"])
        top_left = stepper(a_coord, directions["NW"])

        cond_1 = (top_right in mas_dict["M"]) and (bottem_left in mas_dict["S"])
        cond_2 = (top_right in mas_dict["S"]) and (bottem_left in mas_dict["M"])
        cond_3 = (bottom_right in mas_dict["M"]) and (top_left in mas_dict["S"])
        cond_4 = (bottom_right in mas_dict["S"]) and (top_left in mas_dict["M"])

        match_1 = cond_1 and cond_3
        match_2 = cond_1 and cond_4
        match_3 = cond_2 and cond_3
        match_4 = cond_2 and cond_4

        counter += match_1 or match_2 or match_3 or match_4
    return counter


def day_04_B(data_path: str) -> None:
    grid = read_data(data_path)
    mas_dict = collect_letter_coordinates_v2(grid)
    number_of_mas = count_number_of_mas(mas_dict)
    print(number_of_mas)


test_data_b_path = "/home/jesse/projects/adventOfCode2024/data/day_04/test_data_b"
test_data_b_02_path = "/home/jesse/projects/adventOfCode2024/data/day_04/test_data_b_02"

day_04_B(test_data_b_path)
day_04_B(test_data_b_02_path)
day_04_B(data_path)
