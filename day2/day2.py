""" Day 2 of Advent of Code 2020."""

import pkgutil


def valid_passwords(all_lines: list[str]) -> int:
    """
    Calculate the # of valid passwords in the data file.

    :param all_lines: Input data
    :return: Valid passwords
    """
    valid = 0

    # use a for loop to iterate the list and find the total amount of
    # valid passwords
    for line in all_lines:
        current = line.split(' ')
        policy_lower = int(current[0].split('-')[0])
        policy_upper = int(current[0].split('-')[1])
        letter = current[1].rstrip(':')
        pw = current[2]

        if policy_upper >= pw.count(letter) >= policy_lower:
            valid += 1

    return valid


def part2(all_lines: list[str]) -> int:
    """
    Calculate the # of valid passwords with a different ruleset.

    :param all_lines: Input data
    :return: Valid passwords
    """
    valid = 0

    # use a for loop to iterate the list and find the total amount of
    # valid passwords
    for line in all_lines:
        current = line.split(' ')
        policy_f = int(current[0].split('-')[0]) - 1
        policy_s = int(current[0].split('-')[1]) - 1
        letter = current[1].rstrip(':')
        pw = current[2]

        if (pw[policy_f] == letter) ^ (pw[policy_s] == letter):
            valid += 1

    return valid


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day2', 'day2data.txt')
    problem = raw_data.decode().splitlines()

    answer1 = valid_passwords(problem)
    answer2 = part2(problem)
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
