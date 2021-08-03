"""Day 3 of Advent of Code 2020."""

import pkgutil

# length of each line from the data file
LINE_LENGTH = 31


def count_trees(slope_x: int, slope_y: int, gmap: list[str]) -> int:
    """
    Count the # of trees that the toboggan will encounter.

    :param slope_x: How many times to move right
    :param slope_y: How many times to move down
    :param gmap: Map of the data set
    :return: The number of trees the toboggan encounters
    """
    x, y, count = 0, 0, 0

    # until the end of the list is hit, keep checking for trees and
    # moving the x, y position
    while y < len(gmap):
        if problem[y][x % LINE_LENGTH] == '#':
            count += 1
        x += slope_x
        y += slope_y

    return count


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day3', 'day3data.txt')
    problem = raw_data.decode().splitlines()

    answer1 = count_trees(3, 1, problem)
    answer2 = (count_trees(1, 1, problem) * answer1
               * count_trees(5, 1, problem) * count_trees(7, 1, problem)
               * count_trees(1, 2, problem))
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
