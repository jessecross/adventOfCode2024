import numpy as np

testA_data_path = "/home/jesse/projects/adventOfCode2024/data/day_01/test_data"
partA_data_path = "/home/jesse/projects/adventOfCode2024/data/day_01/data"


def day1A(data_path: str) -> None:
    """
    Parse 2 lists, order them ASC, find the diff between adjacent IDs, sum the total diff.
    """
    with open(data_path) as data_file:
        list_01 = []
        list_02 = []

        for line in data_file:
            i, j = line.rstrip().split()
            list_01.append(int(i))
            list_02.append(int(j))

    list_01.sort()
    list_02.sort()

    array_01 = np.array(list_01)
    array_02 = np.array(list_02)

    array_diff = abs(array_01 - array_02)

    total_diff = sum(array_diff)

    print(total_diff)


# day1A(testA_data_path)
# day1A(partA_data_path)

testB_data_path = "/home/jesse/projects/adventOfCode2024/data/day_01/test_data"
partB_data_path = "/home/jesse/projects/adventOfCode2024/data/day_01/data"


def day1B(data_path: str) -> None:
    """
    Parse 2 lists, count occurences of each ID in second list, multiply each ID in first list by number of occurences in second list and sum.
    """
    with open(data_path) as data_file:
        list_01 = []
        list_02 = []

        for line in data_file:
            i, j = line.rstrip().split()
            list_01.append(int(i))
            list_02.append(int(j))

    dict_02 = {}
    for id in list_02:
        if id not in dict_02:
            dict_02[id] = 1
        else:
            dict_02[id] += 1

    similarity_score = 0
    for id in list_01:
        if id not in dict_02:
            continue
        else:
            similarity_score += id * dict_02[id]

    print(similarity_score)


day1B(testB_data_path)
day1B(partB_data_path)
