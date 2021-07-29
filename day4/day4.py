"""Day 4 of Advent of Code 2020."""

import pkgutil


def dictionary(passport: list[str]) -> dict:
    """
    Converts a list[str] into a python dictionary.

    :param passport: The input list[str] holding multiple fields
    :return: A dictionary containing key, value pairs for the fields
    """
    d = {}
    for field in passport:
        k, v = field.split(':')
        d[k] = v
    return d


def valid_passport(passport_dict: dict) -> bool:
    """
    Determines if the passport is valid by checking if it has the
    required fields.

    :param passport_dict: Individual passport
    :return: True or False
    """
    return ('byr' in passport_dict and 'iyr' in passport_dict and
            'eyr' in passport_dict and 'hgt' in passport_dict and
            'hcl' in passport_dict and 'ecl' in passport_dict and
            'pid' in passport_dict)


def valid_values(potential_pass: dict) -> bool:
    """
    Determines if the supposedly valid passport has valid values.

    :param potential_pass: Potential valid passport
    :return: True or False
    """
    # byr, iyr, and eyr are all just date ranges, trivial to check
    valid_byr = 1920 <= int(potential_pass['byr']) <= 2002
    valid_iyr = 2010 <= int(potential_pass['iyr']) <= 2020
    valid_eyr = 2020 <= int(potential_pass['eyr']) <= 2030

    # hgt requires checking if the value to the key is 'cm' or 'in',
    # then check if the measurement is in the appropriate range
    valid_hgt = False
    if potential_pass['hgt'].count('cm') == 1:
        # assigns the digits before the 'cm'
        height = int(potential_pass['hgt'][:-2])
        valid_hgt = 150 <= height <= 193
    elif potential_pass['hgt'].count('in') == 1:
        # assigns the digits before the 'in'
        height = int(potential_pass['hgt'][:-2])
        valid_hgt = 59 <= height <= 76

    def valid_hcl_string(hex_string: str) -> bool:
        """
        Determines if the hcl_string is valid.

        :param hex_string: The value for the 'hcl' key in the passport
        :return: True or False
        """
        # only returns false if hex_string has an unexpected character
        valid_hex = True
        for character in hex_string:
            if character not in '0123456789abcdef':
                valid_hex = False
                break
        return valid_hex

    valid_hcl = False
    if len(potential_pass['hcl']) == 7:
        # assigns the 6 digits after the # in the hex value
        hex_digits = potential_pass['hcl'][1:]
        valid_hcl = valid_hcl_string(hex_digits)

    # trivial check for ecl
    valid_ecl = potential_pass['ecl'] in ['amb', 'blu', 'brn', 'gry',
                                         'grn', 'hzl', 'oth']

    def pid_string(digits: str) -> bool:
        """
        Determines if the pid_string is valid.

        :param digits: The value for the 'pid' key in the passport
        :return: True or False
        """
        valid_digits = True
        for digit in digits:
            if digit not in '0123456789':
                valid_digits = False
                break
        return valid_digits

    valid_pid = False
    if len(potential_pass['pid']) == 9:
        valid_pid = pid_string(potential_pass['pid'])

    return (valid_byr and valid_iyr and valid_eyr and valid_hgt and
            valid_hcl and valid_ecl and valid_pid)


if __name__ == '__main__':
    raw_data = pkgutil.get_data('day4', 'day4data.txt')
    # turns the data file into a list of list[str] with each list[str]
    # containing all the fields in a passport
    problem = [string.split() for string in (raw_data.decode().
                                             replace('\r\n', ' ').
                                             split('  '))]
    # converts the list[str] in problem to a python dictionary
    passports = [dictionary(data) for data in problem]
    valid = []
    true_valid = []
    for pp in passports:
        if valid_passport(pp):
            valid.append(pp)
    for pp in valid:
        if valid_values(pp):
            true_valid.append(pp)

    answer1 = len(valid)
    answer2 = len(true_valid)
    print(f'The first answer is {answer1}')
    print(f'The second answer is {answer2}')
