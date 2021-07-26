# day 1 of Advent of Code 2020

# function to calculate report repair
def report_repair(filename):

    # open the file
    file = open(filename, 'r')

    # read the lines and add it to a list
    lines = file.readlines()
    all_lines = []
    for line in lines:
        all_lines.append(line.split('\n')[0])

    """use 2 for loops to find the two numbers in the list that sum to 2020
    then return the two numbers and their product"""
    start = 0
    iterator = 0
    goal = 2020
    for line in all_lines:
        iterator = start + 1
        while (iterator < len(all_lines)):
            if (int(line) + int(all_lines[iterator]) == goal):
                return int(line), int(all_lines[iterator]), int(line) * int(all_lines[iterator])
            iterator += 1
        start += 1

first_num, second_num, answer = report_repair('day1data.txt')
print(f"The 2 numbers that add up to 2020 are {first_num} and {second_num}.\nThe answer is {answer}")