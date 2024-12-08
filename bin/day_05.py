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

# day_05_A(test_data_path)
# day_05_A(data_path)


def filter_for_incorrect_updates(updates: list, rules: list) -> list:
    incorrect_updates = []

    for update in updates:
        is_incorrect_order = False

        for rule in rules:
            small_page, big_page = rule

            if (small_page in update) and (big_page in update):
                small_idx = update.index(small_page)
                big_idx = update.index(big_page)

                is_incorrect_order = not (small_idx < big_idx)
                if is_incorrect_order:
                    break

        if is_incorrect_order:
            incorrect_updates.append(update)

    return incorrect_updates


def order_update_recursion(update: list, rules: list) -> list:
    for rule in rules:
        small_page, big_page = rule

        if (small_page in update) and (big_page in update):
            small_idx = update.index(small_page)
            big_idx = update.index(big_page)

            if not (small_idx < big_idx):
                update[small_idx], update[big_idx] = update[big_idx], update[small_idx]
                order_update_recursion(update, rules)

    return update


def day_05_B(data_path: str) -> None:
    rules, updates = read_data(data_path)

    incorrect_updates = filter_for_incorrect_updates(updates, rules)

    ordered_incorrect_updates = []
    for update in incorrect_updates:
        update = order_update_recursion(update, rules)
        ordered_incorrect_updates.append(update)

    middle_pages = []
    for update in ordered_incorrect_updates:
        middle_page = update[len(update) // 2]
        middle_pages.append(middle_page)

    middle_page_sum = sum(middle_pages)
    print(middle_page_sum)


day_05_B(test_data_path)
day_05_B(data_path)
