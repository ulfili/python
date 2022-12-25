"""EXAM."""
import re


def find_capital_letters(text: str) -> str:
    """Function that finds capital letters."""
    pattern = r"[A-Z]"
    capital_letters = ""
    for match in re.finditer(pattern, text):
        capital_letters += match.group()
    return capital_letters


def close_far(a: int, b: int, c: int) -> bool:
    """Docstring."""
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    if abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2:
        return True
    return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """Given a string of names and scores, return a list of names where the score is higher than or equal to min_result."""
    name_and_score = results_string.split(",")
    winners = []
    for elem in name_and_score:
        token_list = elem.split(" ")
        if len(token_list) > 1:
            score = token_list.pop()
            name = " ".join(token_list)
            if int(score) >= min_result:
                winners.append(name)
    return winners


print(get_names_from_results("ago 123,peeter 11", 0)) # ["ago", "peeter"]
print(get_names_from_results("ago 123,peeter 11,33", 10)) # ["ago", "peeter"]  # 33 does not have the name
print(get_names_from_results("ago 123,peeter 11", 100)) # ["ago"]
print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11)) # ["ago", "peeter",  "kitty11!!"]
print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12)) # ["ago", "kusti riin"]


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    first_line = game[0]
    second_line = game[1]
    third_line = game[2]
    if first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1:
        return 1
    if first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1:
        return 1
    if first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1:
        return 1
    if first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1:
        return 1
    if first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1:
        return 1
    if first_line[0] == 1 and first_line[1] == 1 and first_line[2] == 1:
        return 1
    if second_line[0] == 1 and second_line[1] == 1 and second_line[2] == 1:
        return 1
    if third_line[0] == 1 and third_line[1] == 1 and third_line[2] == 1:
        return 1

    if first_line[0] == 2 and second_line[0] == 2 and third_line[0] == 2:
        return 2
    if first_line[1] == 2 and second_line[1] == 2 and third_line[1] == 2:
        return 2
    if first_line[2] == 2 and second_line[2] == 2 and third_line[2] == 2:
        return 2
    if first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2:
        return 2
    if first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2:
        return 2
    if first_line[0] == 2 and first_line[1] == 2 and first_line[2] == 2:
        return 2
    if second_line[0] == 2 and second_line[1] == 2 and second_line[2] == 2:
        return 2
    if third_line[0] == 2 and third_line[1] == 2 and third_line[2] == 2:
        return 2

    else:
        return 0


print(tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]))   # => 1
print(tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]))   # => 0
print(tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]))   # => 2