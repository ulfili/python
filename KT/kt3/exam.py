"""KT3."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if s == "":
        return ""
    if len(s) == 2:
        return s[::-1]
    last_symbol = s[len(s) - 1]
    print("last symbol is: ", last_symbol)
    new_string = last_symbol + s[0:len(s) - 1]
    return new_string


print(last_to_first("hello"))
print(last_to_first(""))
print(last_to_first("ab"))


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    no_duplicates = list(set(numbers))
    # print(no_duplicates)
    for a in no_duplicates:
        numbers.remove(a)
    # print(numbers)
    if len(numbers) == 1:
        return True
    else:
        return False


print(only_one_pair([1, 2, 3, 1]))
print(only_one_pair([1, 2, 3, 3]))
print(only_one_pair([1, 2, 1, 3, 1]))
