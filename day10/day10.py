"""Day 8 of Advent of Code 2020"""

import pkgutil
import itertools
from copy import deepcopy


def copy(og_data: list[int]):
    """
    Makes a copy of the origial data set and returns it with the proper
    start and end values as defined by the problem (also sorted).

    :param og_data: the original data set
    :return: a sorted copy with proper start and end values
    """
    c = deepcopy(og_data)
    c.append(0)
    c.sort()
    c.append(max(c) + 3)
    return c


def part1(data: list[int]) -> int:
    """
    Counts the # of times the difference is 3 and 1 for the numbers in
    ascending order and multiplies the length of each amount of
    occurences

    :param data: takes in a data set
    :return: the product of the # of times the difference is 3 and 1
    """
    l1 = 0
    l3 = 0
    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        if diff == 1:
            l1 += 1
        elif diff == 3:
            l3 += 1

    return l1 * l3


def part2(data: list[int]) -> int:
    """
    Dynamic programming solution to find how many ways there are to
    complete the adapter chain from a start point.

    :param data: takes in a data set
    :return: # of distinct ways to get from start to end
    """
    dp = [1]
    for i in range(1, len(data)):
        ans = 0
        for j in range(i):
            if data[j] + 3 >= data[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day10', 'day10data.txt')
    problem = [int(n) for n in raw_data.decode().splitlines()]

    copy_data = copy(problem)

    answer1 = part1(copy_data)
    answer2 = part2(copy_data)

    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
