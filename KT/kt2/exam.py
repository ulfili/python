"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) <= 3:
        return s[::-1]
    else:
        first_two = s[0:2]
        last_two = s[-2:]
        new_string = last_two + s[2:-2] + first_two
        return new_string


print(switch_lasts_and_firsts("123456"))
print(switch_lasts_and_firsts("ambulance"))


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    my_dict = {}
    new_dict = {}
    letters_list = list(text)
    for elem in letters_list:
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1
    for key, value in my_dict.items():
        new_dict[value] = [key]
        print(new_dict)


print(get_symbols_by_occurrences("hello"))


def min_diff(nums: list) -> int:
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    n = len(nums)
    diff = 10 ** 20
    for i in range(n - 1):
        for j in range(i+1, n):
            if abs(nums[i] - nums[j]) < diff:
                diff = abs(nums[i] - nums[j])
    return diff
