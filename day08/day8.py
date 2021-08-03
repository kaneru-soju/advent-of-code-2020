"""Day 8 of Advent of Code 2020"""

import pkgutil
from copy import deepcopy


def run(instructions: list[list[str]], ptr: int, acc: int) -> [int, int]:
    """
    Runs a set of instructions and keeps track of the instruction line
    number and accumulator.

    :param instructions: the set of instructions
    :param ptr: the current line of instruction
    :param acc: the accumulator value
    :return: the pointer and the accumulator values
    """
    instr = instructions[ptr]
    if 'acc' in instr:
        acc += int(instr[1])
        ptr += 1
    elif 'nop' in instr:
        ptr += 1
    elif 'jmp' in instr:
        ptr += int(instr[1])

    return ptr, acc


def part1(data_set: list[list[str]]) -> int:
    """
    Runs a set of instructions until an instruction line is repeated.
    Returns the value of the accumulator right before that occurence.

    :param data_set: the input data
    :return: the accumulator value right before any instruction is
    repeated twice
    """
    p = 0
    a = 0
    seen = set()

    while True:
        if p in seen:
            return a
        seen.add(p)
        p, a = run(data_set, p, a)


def part2(data_set: list[list[str]]) -> int:
    """
    Runs every instruction in a set of instructions. Rewrites
    instructions one-by-one to find the proper solution. Brute force.

    :param data_set: the input data
    :return: the accumulator value after all instructions have been run
    """
    for i in range(len(data_set)):
        # deep copy of the data_set as to not modify original values
        copy = deepcopy(data_set)
        if 'nop' in copy[i][0]:
            copy[i][0] = 'jmp'
        elif 'jmp' in copy[i][0]:
            copy[i][0] = 'nop'
        else:
            continue

        x = 0
        p = 0
        a = 0
        # if pointer is invalid then the loop terminates, x stops the
        # program from infinitely looping. Returns whenever p finally
        # hits the end of the instructions which gives us the correct
        # value
        while p < len(copy) and x < len(copy):
            x += 1
            p, a = run(copy, p, a)
        if p == len(copy):
            return a


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day8', 'day8data.txt')
    problem = [string.split() for string in raw_data.decode().splitlines()]

    answer1 = part1(problem)
    answer2 = part2(problem)

    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
