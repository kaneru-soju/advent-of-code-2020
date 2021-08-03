"""Day 5 of Advent of Code 2020"""

import pkgutil
import math

ROWS = list(range(0, 128))
COLUMNS = list(range(0, 8))


def highest_id(boarding_passes: list[str]) -> [int, int]:
    """
    Iterates through all the boarding passes and finds the highest seat
    ID among them.

    :param boarding_passes: The input list[str] holding all the boarding
    passes
    :return: The highest seat ID and the ID of your seat
    """
    max_id = 0
    my_id = 0
    pass_list = []

    # iterate through the boarding passes and reset the pool for rows
    # and columns
    for bp in boarding_passes:
        rows = ROWS
        columns = COLUMNS

        # go through each character in a boarding pass, and assign the
        # proper slice to rows/columns
        for char in bp:
            if char == 'F':
                rows = rows[:-math.ceil(len(rows)/2)]
            elif char == 'B':
                rows = rows[math.floor(len(rows)/2):]
            elif char == 'L':
                columns = columns[:-math.ceil(len(columns)/2)]
            elif char == 'R':
                columns = columns[math.floor(len(columns)/2):]

        # find the max_id and append all IDs to a list
        calc = rows[0] * len(COLUMNS) + columns[0]
        pass_list.append(calc)
        if calc > max_id:
            max_id = calc

    # sort the list and iterate through it to find your ID
    pass_list.sort()
    current = len(pass_list) - 1
    while current - 1 > 0:
        if pass_list[current] - pass_list[current - 1] != 1:
            my_id = pass_list[current] - 1
        current -= 1

    return max_id, my_id


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day5', 'day5data.txt')
    problem = raw_data.decode().splitlines()
    answer1, answer2 = highest_id(problem)
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
