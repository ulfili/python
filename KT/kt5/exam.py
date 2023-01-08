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
