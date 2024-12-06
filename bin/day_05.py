def read_data(data_path: str) -> list:
    """Read the data a list of rules and list of pages."""
    rules = []
    updates = []
    with open(data_path) as data_file:
        is_rules = True
        for line in data_file:
            if not line.strip():
                is_rules = False
                continue
            if is_rules:
                rules.append([int(page) for page in line.strip().split("|")])
            else:
                updates.append([int(page) for page in line.strip().split(",")])
    return rules, updates


def day_05_A(data_path: str) -> None:
    rules, updates = read_data(data_path)

    correct_updates = []
    correct_middle_pages = []
    for update in updates:
        is_correct_order = True

        for rule in rules:
            small_page, big_page = rule

            if (small_page in update) and (big_page in update):
                for idx, page in enumerate(update):
                    if page == small_page:
                        small_idx = idx
                    if page == big_page:
                        big_idx = idx

                is_correct_order = small_idx < big_idx
                if not is_correct_order:
                    break

        if is_correct_order:
            correct_updates.append(update)

            middle_page = update[len(update) // 2]
            correct_middle_pages.append(middle_page)

    middle_page_sum = sum(correct_middle_pages)

    print(middle_page_sum)


test_data_path = "/home/jesse/projects/adventOfCode2024/data/day_05/test_data"
data_path = "/home/jesse/projects/adventOfCode2024/data/day_05/data"

day_05_A(test_data_path)
day_05_A(data_path)
