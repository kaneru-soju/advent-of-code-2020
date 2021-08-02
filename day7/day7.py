"""Day 7 of Advent of Code 2020"""

import pkgutil
from collections import deque, defaultdict

# PARENTS[x] are the bags that contain x
PARENTS = defaultdict(list)
# CONTENTS[x] are which bags x contains and how many of each
CONTENTS = defaultdict(list)
target = 'shinygoldbag'


def get_dictionaries(data_set: list[list[str]]):
    """
    Creates 2 dictionaries. PARENTS which has a key, value pair (bag, parents)
    and CONTENTS which has a key, value pair (bag, contents).

    :param data_set: the input list[list[str]] holding the ruleset for
    each bag
    """
    for data in data_set:
        container = "".join(data[:3])  # the container bag
        container = container[:-1]  # remove trailing 's' in 'bags'
        if data[-3] == 'no':  # doesn't contain any other bags
            continue
        else:
            # start after the word contains, then iterates to the next
            # 4 words for how ever long the line is
            idx = 4
            while idx < len(data):
                # grabs 4 words after contains and places them in bag
                bag = data[idx]+data[idx+1]+data[idx+2]+data[idx+3]
                # if bag ends with . , or s then we remove it (in order)
                if bag.endswith('.'):
                    bag = bag[:-1]
                if bag.endswith(','):
                    bag = bag[:-1]
                if bag.endswith('s'):
                    bag = bag[:-1]

                # strips off initial digit and assigns it to num, ensure
                # that there are no double-digit numbers
                num = int(bag[0])
                assert bag[1] not in '0123456789'
                while any([bag.startswith(d) for d in '0123456789']):
                    bag = bag[1:]

                # PARENTS lists all the bags the bag is contained in
                PARENTS[bag].append(container)
                # CONTENTS lists the contents of each container
                CONTENTS[container].append((num, bag))
                idx += 4


def part1() -> int:
    """
    Calculates how many bag colors can eventually contain at least one
    shiny gold bag. Uses BFS

    :return: The number of bag colors that can contain one shiny gold
    bag
    """
    seen = set()  # set of all possible parents
    q = deque([target])  # BFS from the target
    while q:
        bag = q.popleft()  # grab something from the deque
        if bag in seen:  # if we've already seen it, ignore it
            continue
        seen.add(bag)
        # append all the parents of the current bag we're looking at
        # to the deque
        for parent in PARENTS[bag]:
            q.append(parent)
    # print the length of our set - 1 to remove the initial shinygoldbag
    return len(seen) - 1


def part2(target_bag: str) -> int:
    """
    Calculates how many individual bags are required inside a shiny gold
    bag. Uses DFS

    :return: The number of bags contained in one shiny gold bag
    """
    ans = 1  # answer starts at 1 (shinygoldbag)
    # for all of the contents in target_bag, recursively call part2()
    # until the bag has no more contents and recursively add the number
    # of bags that the target_bag would end up containing
    for (num, bag) in CONTENTS[target_bag]:
        ans += num*part2(bag)
    return ans


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day7', 'day7data.txt')
    problem = [string.split() for string in raw_data.decode().splitlines()]
    get_dictionaries(problem)

    answer1 = part1()
    answer2 = part2(target) - 1  # subtract 1 to disregard original bag
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
