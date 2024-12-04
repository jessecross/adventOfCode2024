import math
import re


def day_03_A(data_path: str) -> None:
    regex = "mul\(\d{1,3}\,\d{1,3}\)"

    multipliers = []
    with open(data_path) as data_file:
        for line in data_file:
            data = line.rstrip()
            multipliers.extend(re.findall(regex, data))

    sum = 0
    for multiplier in multipliers:
        halves = multiplier.split(",")

        int_pair = []
        for half in halves:
            int_pair.append(int("".join(x for x in half if x.isdigit())))

        product = math.prod(int_pair)

        sum += product

    print(sum)


test_data = "/home/jesse/projects/adventOfCode2024/data/day_03/test_data"
data = "/home/jesse/projects/adventOfCode2024/data/day_03/data"

# day_03_A(test_data)
# day_03_A(data)

test_data_b = "/home/jesse/projects/adventOfCode2024/data/day_03/test_data_b"


def day_03_B(data_path: str) -> None:
    regex = "mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)"

    keys = []
    with open(data_path) as data_file:
        for line in data_file:
            data = line.rstrip()
            keys.extend(re.findall(regex, data))

    multipliers = []
    do_multiply = True
    for key in keys:
        if key == "don't()":
            do_multiply = False
        elif key == "do()":
            do_multiply = True

        if do_multiply and ("mul" in key):
            multipliers.append(key)

    print(keys)
    print(multipliers)

    sum = 0
    for multiplier in multipliers:
        halves = multiplier.split(",")

        int_pair = []
        for half in halves:
            int_pair.append(int("".join(x for x in half if x.isdigit())))

        product = math.prod(int_pair)

        sum += product

    print(sum)


day_03_B(test_data_b)
day_03_B(data)
