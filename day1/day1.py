"""Day 1 of Advent of Code 2020."""

import pkgutil


def report_repair(all_lines: list[int], goal: int = 2020) -> int:
    """
    Calculate report repair (2sum).

    :param all_lines: Input data
    :param goal: Target goal
    :return: Result
    """

    # use 2 for loops to find the two numbers in the list that sum to 2020
    # then return the two numbers and their product
    for start, n in enumerate(all_lines):
        for m in all_lines[start + 1:]:
            if n + m == goal:
                return n * m
    
    raise ValueError('Invalid input')


def part2(all_lines: list[int]) -> int:
    """
    Calculate report repair (3sum).

    :param all_lines: Input data
    :return: Result
    """
    for n in all_lines:
        try:
            p1_solution = report_repair(all_lines, goal=2020 - n)
        except ValueError:
            pass
        else:
            return n * p1_solution
    
    raise ValueError('Invalid input')


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day1', 'day1data.txt')
    problem = [int(n) for n in raw_data.splitlines()]

    answer1 = report_repair(problem)
    answer2 = part2(problem)
    print(f"The first answer is {answer1}")
    print(f"The second answer is {answer2}")
