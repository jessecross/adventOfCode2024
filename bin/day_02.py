import numpy as np


def is_diff_safe(i: int, j: int) -> bool:
    diff = abs(i - j)
    if diff >= 1 and diff <= 3:
        return True
    return False


def is_increasing(i: int, j: int) -> bool:
    return i < j


def is_decreasing(i: int, j: int) -> bool:
    return i > j


def day2A(data_path: str) -> None:
    # Read reports
    with open(data_path) as data_file:
        reports = []
        for line in data_file:
            report = []
            for x in line.strip().split():
                report.append(int(x))
            reports.append(tuple(report))

    report_safety_dict = {}
    for report in reports:
        # Check if report safe: Difference condition
        diff_safe = True
        for i in range(1, len(report)):
            diff_safe = is_diff_safe(report[i - 1], report[i])
            if not diff_safe:
                break

        # Check if report safe: monotonicity condition
        all_increasing = all(
            is_increasing(report[i - 1], report[i]) for i in range(1, len(report))
        )
        all_decreasing = all(
            is_decreasing(report[i - 1], report[i]) for i in range(1, len(report))
        )
        monotonic_safe = (all_increasing or all_decreasing) and not (
            all_increasing and all_decreasing
        )

        report_safety_dict[report] = diff_safe and monotonic_safe

    safe_count = sum(value for value in report_safety_dict.values())
    print(safe_count)


test_data_path = "/home/jesse/projects/adventOfCode2024/data/day_02/test_data"
data_path = "/home/jesse/projects/adventOfCode2024/data/day_02/data"

# day2A(test_data_path)
# day2A(data_path)


def is_difference_safe(report: list) -> bool:
    diff_safe_list = [
        is_diff_safe(report[i - 1], report[i]) for i in range(1, len(report))
    ]
    return all(diff_safe_list)


def is_monotonic_safe(report: list) -> bool:
    all_increasing = all(
        is_increasing(report[i - 1], report[i]) for i in range(1, len(report))
    )
    all_decreasing = all(
        is_decreasing(report[i - 1], report[i]) for i in range(1, len(report))
    )
    return (all_increasing or all_decreasing) and not (
        all_increasing and all_decreasing
    )


def day2B(data_path: str) -> None:
    # Read reports
    with open(data_path) as data_file:
        reports = []
        for line in data_file:
            report = []
            for x in line.strip().split():
                report.append(int(x))
            reports.append(tuple(report))

    report_safety_dict = {}
    for report in reports:
        diff_safe = is_difference_safe(report)
        monotonic_safe = is_monotonic_safe(report)

        idx = 0
        while idx < len(report):
            tmp_report = list(report)

            if not (diff_safe and monotonic_safe):
                del tmp_report[idx]
            else:
                break

            diff_safe = is_difference_safe(tmp_report)
            monotonic_safe = is_monotonic_safe(tmp_report)

            idx += 1

        report_safety_dict[report] = diff_safe and monotonic_safe

    safe_count = sum(value for value in report_safety_dict.values())
    print(report_safety_dict)
    print(safe_count)


day2B(test_data_path)
day2B(data_path)
