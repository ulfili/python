"""EXAM."""
import re
from operator import attrgetter


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


print(get_names_from_results("ago 123,peeter 11", 0))  # ["ago", "peeter"]
print(get_names_from_results("ago 123,peeter 11,33", 10))  # ["ago", "peeter"]  # 33 does not have the name
print(get_names_from_results("ago 123,peeter 11", 100))  # ["ago"]
print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11))  # ["ago", "peeter",  "kitty11!!"]
print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12))  # ["ago", "kusti riin"]


def check_line(game, line_nr):
    line = game[line_nr]
    for playr in range(1, 3):
        if line[0] == playr and line[1] == playr and line[2] == playr:
            return playr
    return 0


def check_colum(game, colum_nr):
    colum = [game[0][colum_nr], game[1][colum_nr], game[2][colum_nr]]
    print(colum)
    for player in range(1, 3):
        if colum[0] == player and colum[1] == player and colum[2] == player:
            return player
    return 0


def check_diag(game):
    diag_1 = [game[0][0], game[1][1], game[2][2]]
    diag_2 = [game[0][2], game[1][1], game[2][0]]
    print("diag1 ", diag_1)
    print("diag2 ", diag_2)
    for player in range(1, 3):
        if diag_1[0] == player and diag_1[1] == player and diag_1[2] == player:
            return player
        if diag_2[0] == player and diag_2[1] == player and diag_2[2] == player:
            return player
    return 0


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

    tic_tac_toe(
    [[1, 2, 1],
     [2, 1, 2],
     [2, 2, 1] ]) => 1

     tic_tac_toe(
     [[2, 2, 2],
      [0, 2, 0],
      [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for i in range(3):
        win = check_line(game, i)
        print("Check line ", i)
        if win:
            print("Win p:", win)
            return win

    for i in range(3):
        win = check_colum(game, i)
        print("Check colum ", i)
        if win:
            print("Win p:", win)
            return win

    win = check_diag(game)
    print("Check giag ")
    if win:
        print("Win p:", win)
        return win

    return 0


"""print(tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]))   # => 1
print(tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]))   # => 0
print(tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]))   # => 2

print(tic_tac_toe([[2, 2, 0], [0, 2, 0], [1, 1, 1]]))   # => 1
print(tic_tac_toe([[2, 2, 0], [0, 2, 0], [1, 2, 1]]))   # => 2

print(tic_tac_toe([[2, 2, 0], [0, 2, 0], [1, 1, 2]]))   # => 2
print(tic_tac_toe([[2, 2, 1], [0, 1, 0], [1, 1, 2]]))   # => 1
print(tic_tac_toe([[2, 2, 1], [1, 0, 0], [1, 1, 2]]))   # => 1
"""

def rainbows(field: str) -> int:
    """
    Count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel sümboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    if len(field) < 7:
        return 0
    if field[:7].lower() == "rainbow":
        return 1 + rainbows(field[7:])
    return rainbows(field[1:])


print(rainbows("rainbowThisIsJustSomeNoise"))  # 1
print(rainbows("WoBniar"))  # 1
print(rainbows("rainbowobniar"))  # 1


def longest_substring(text: str) -> str:
    """Find the longest substring."""
    s_list = []
    if len(text) == 0:
        return ""
    for j in range(len(text)):
        # print("big loop")
        start = j
        for i in range(len(text) - start):
            # print("small loop")
            finish = i + 1 + start
            s = text[start:finish]
            s_upper = s.upper()
            letters_set = set(s_upper)
            print(letters_set)
            if len(s) == len(letters_set):
                s_list.append(s)
            print(s)
        # end of small loop
    # end of big loop
    lengths_list = []
    for s in s_list:
        print(s, len(s))
        lengths_list.append(len(s))
    print(lengths_list)
    max_len = max(lengths_list)
    print(max_len)

    for s in s_list:
        if len(s) == max_len:
            print(s)
            return s


# print(longest_substring("abBcd "))


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Initialize student."""
        self.name = name
        self.average_grade = average_grade
        self.credit_points = credit_points

    def __repr__(self):
        """Repr."""
        return "Student name: " + self.name + " Average grade: " + str(self.average_grade) + " Credit points: " + str(self.credit_points)


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    summa = 0
    if len(grades) == 0:
        average = 0
    else:
        for grade in grades:
            summa += grade
        average = round((summa / len(grades)), 3)
    return Student(name, average, credit_points)


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    good_students = []
    grades_list = []
    print("get_top_student_with_credit_points")
    for student in students:
        print(student.credit_points)
        if student.credit_points >= min_credit_points:
            good_students.append(student)
            grades_list.append(student.average_grade)
    print(good_students)
    if len(grades_list):  # > 0
        max_grade = max(grades_list)
        print("max grade ", max_grade)
        for student in good_students:
            if student.average_grade == max_grade:
                return student
    return None


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    summ = student.average_grade * grades_count
    new_average = round(((summ + new_grade) / (grades_count + 1)), 3)
    student.average_grade = new_average
    old_points = student.credit_points
    student.credit_points = old_points + credit_points
    return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    return_list = sorted(students, key=attrgetter("name"))
    return_list_2 = sorted(return_list, key=attrgetter("credit_points", "average_grade"), reverse=True)

    return return_list_2


if __name__ == "__main__":
    """
    mari = Student("Mari", 4.5, 6)
    elsa = Student("Elsa", 3.75, 5)
    toomas = Student("Toomas", 5.0, 6)
    anna = Student("Anna", 5.0, 6)
    print(toomas)
    simple_marija = create_student("Maria", [2, 4, 5, 5, 3], 5)
    print(simple_marija)

    georg = create_student("Georg", [2, 3, 5, 1, 3], 0)
    print(georg)

    mark = create_student("Mark", [], 1)
    print(mark)

    bob = create_student("Bob", [5, 3, 2], 4)
    print(bob)

    student_list = [mari, elsa, toomas, simple_marija, georg, mark, anna]
    top_student = get_top_student_with_credit_points(student_list, 6)
    print(top_student)

    print(simple_marija)
    add_result_to_student(simple_marija, 5, 5, 5)
    print(simple_marija)

    print(georg)

    print(add_result_to_student(georg, 5, 4, 3))

    print(student_list)
    sorted_list = get_ordered_students(student_list)
    print(sorted_list)
    
    """