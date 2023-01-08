"""KT5."""


def get_date_string(date: list) -> str:
    """Pretty print the date."""
    if len(date) == 0 or len(date) > 3:
        return "The date is unknown!"

    else:
        return "The date is -> " + str(date[0]) + "/" + str(date[1]) + "/" + str(date[2])


print(get_date_string([3, 3, 2000]))  # -> "The date is -> 3/3/2000"
print(get_date_string([20, 12, 5677]))  # -> "The date is -> 20/12/5677"
print(get_date_string([2, 2, 3, 200]))  # -> "The date is unknown!"
print(get_date_string([]))  # -> "The date is unknown!"


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """
    Return list of odd sums of consecutive elements.

    Consider all consecutive elements in the input list. Return a list of all the odd sums of consecutive elements.

    odd_sums_of_consecutive_elements([1, 2, 3, 5]) => [3, 5]
    odd_sums_of_consecutive_elements([8, 10]) => []
    odd_sums_of_consecutive_elements([9]) => []
    odd_sums_of_consecutive_elements([11, 8]) => [19]

    :param nums:
    :return:
    """
    odd_nums = []
    for i in range(len(nums) - 1):
        if (nums[i] + nums[i + 1]) % 2 == 1:
            odd_nums.append(nums[i] + nums[i + 1])
    return odd_nums


print(odd_sums_of_consecutive_elements([1, 2, 3, 5]))  # => [3, 5]
print(odd_sums_of_consecutive_elements([8, 10]))  # => []
print(odd_sums_of_consecutive_elements([9]))  # => []
print(odd_sums_of_consecutive_elements([11, 8]))  # => [19]
print(odd_sums_of_consecutive_elements([3, 5]))  # => []


def g_happy(s: str) -> bool:
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    pass