"""Day 6 of Advent of Code 2020"""

import pkgutil


def count_sum(forms: list[list[str]]) -> [int, int]:
    """
    Finds the sum of the questions which anybody answered in each group
    and finds the sum of the questions which everybody answered yes to
    in each group.

    :param forms: The input list[list[str]] holding all the question
    forms for each group
    :return: The first sum and second sum
    """
    s1 = 0
    s2 = 0
    p1list = []
    p2list = []
    p2dupe = []

    # iterate through all the questionnaire forms
    for form in forms:
        for answer in form:
            for character in answer:
                # if char is in the alphabet and hasn't been answerd yes
                # to yet, add to p1list; also add all chars to p2list
                if (character in 'abcdefghijklmnopqrstuvwxyz' and
                        p1list.count(character) == 0):
                    p1list.append(character)
                p2list.append(character)

        # iterate through each char in p2list and check to see if the
        # count for that letter is equal to the number of people on the
        # form to ensure everybody said yes for that question; need a
        # second dupe list to prevent duplicate letters from adding to
        # the sum
        for letter in p2list:
            if (p2list.count(letter) == len(form) and
                    p2dupe.count(letter) < 1):
                p2dupe.append(letter)
                s2 += 1

        # adds the length of p1list, which is the total # of unique
        # questions anybody answered yes to for that form
        s1 += len(p1list)

        # reset the lists for each new form
        p1list = []
        p2list = []
        p2dupe = []

    return s1, s2


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day6', 'day6data.txt')
    problem = [string.split() for string in (raw_data.decode().
                                             replace('\r\n', ' ').
                                             split('  '))]
    answer1, answer2 = count_sum(problem)
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
