"""Day 8 of Advent of Code 2020"""

import pkgutil
import itertools


def part1(data: list[int]) -> int:
    """
    Finds the first number that does not have the property. The property
    is that the current number is the sum of two of the 25 numbers
    before it. The two numbers cannot be the same.

    :param data: a list of numbers to use as the data
    :return: the first number that does not have the property
    """
    for i in range(25, len(data)):
        flag = False
        # prev is a list that has the 25 numbers before data[i]
        prev = data[i-25:i]

        # use itertools to check all combinations of 2 in prev to see if
        # there is a sum that equals the number at data[i]
        for j, k in itertools.combinations(prev, 2):
            if j + k == data[i]:
                flag = True
        if not flag:
            return data[i]


def part2(data: list[int], first_answer: int) -> int:
    """
    Finds the contiguous set of 2 or more numbers that sum up to the
    answer from part 1. Iterates through data using 2 for loops.

    :param data: a list of numbers to use as the data
    :param first_answer: the answer to part 1
    :return: the sum of the smallest number and biggest number in the
    contiguous data set
    """
    for i in range(len(data)):
        # continues to test lists [i:j] while incrementing j to see if
        # there is a contiguous sum that will equal the first answer
        for j in range(i + 2, len(data)):
            test = data[i:j]
            if sum(test) == first_answer:
                return min(test) + max(test)


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day9', 'day9data.txt')
    problem = [int(n) for n in raw_data.decode().splitlines()]

    answer1 = part1(problem)
    answer2 = part2(problem, answer1)

    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
