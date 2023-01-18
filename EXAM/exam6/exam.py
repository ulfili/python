"""Exam 6 (2023-01-17)."""


def double_letters(text: str) -> str:
    """
    Double every letter in text.

    Latin letters (a-z and A-Z) have to be doubled for the output.
    All other symbols should remain the same.

    double_letters("abc") => "aabbcc"
    double_letters("hello world") => "hheelllloo wwoorrlldd"
    double_letters("Hi!?") => "HHii!?"
    """

    result = ""
    for char in text:
        if char.isalpha():
            result += char * 2
        else:
            result += char
    return result


def count_digits_chars_symbols(string: str) -> str:
    """
    Count digits, characters and other symbols.

    Count all the letters, numbers and special symbols from the given string.
    If the input is an empty string, return "".

    There is no difference whether the count is 1 or more, we use plural nouns ("1 symbols", "1 digits", "1 chars").
    Depending on the input, the output has to be in The format:

    count_digits_chars_symbols("aa") => The input has 2 chars
    count_digits_chars_symbols("33") => The input has 2 digits
    count_digits_chars_symbols("¤") => The input has 1 symbols
    count_digits_chars_symbols("sbf56") => The input has 3 chars, 2 digits
    count_digits_chars_symbols("db/") => The input has 2 chars, 1 symbols
    count_digits_chars_symbols("545#¤%") => The input has 3 digits and 3 symbols
    count_digits_chars_symbols("545dd#¤%") => The input has 2 chars, 3 digits and 3 symbols
    """
    if len(string) == 0:
        return ""
    nums = 0
    char = 0
    symb = 0
    return_str = "The input has"
    for elem in string:
        if elem.isalpha():
            char += 1
        else:
            if elem.isdigit():
                nums += 1
            else:
                symb += 1

    if char:
        return_str += " " + str(char) + " chars"
    if nums:
        return_str += " " + str(nums) + " digits"
    if symb:
        return_str += " " + str(symb) + " symbols"

    if char and nums and symb:
        return_str = F"The input has {char} chars, {nums} digits and {symb} symbols"
        return return_str

    if nums and symb:
        return_str = F"The input has {nums} digits and {symb} symbols"
        return return_str
    if char and nums:
        return_str = F"The input has {char} chars, {nums} digits"
        return return_str
    if char and symb:
        return_str = F"The input has {char} chars, {symb} symbols"
        return return_str
    return return_str


print(count_digits_chars_symbols(""))
print(count_digits_chars_symbols("545#¤%"))    # => The input has 3 digits and 3 symbols
print(count_digits_chars_symbols("545dd#¤%"))    # => The input has 2 chars, 3 digits and 3 symbols


def mix_string(s1: str, s2: str) -> str:
    """
    Given two strings s1 and s2, create a mixed string by alternating between str1 and str2 chars.

    mix_string("AAA", "bbb") -> "AbAbAb"
    mix_string("AA", "") -> "AA"
    mix_string("mxdsrn", "ie tig") -> "mixed string"
    """

    result_str = ""
    short_str = s1
    long_str = s2
    if len(s1) > len(s2):
        long_str = s1
        short_str = s2

    if len(short_str) == 0:
        return long_str

    # print("short", short_str, "long", long_str)
    i = 0
    for i in range(len(short_str)):
        ch1 = s1[i]
        ch2 = s2[i]
        result_str += ch1 + ch2
    if len(s1) == len(s2):
        return result_str
    # print(long_str[i:])
    result_str += long_str[i+1:]
    # print(result_str)
    return result_str


print(mix_string("AAA", "bbb"))  # "AbAbAb"

print(mix_string("AAAAA", "BBbb"))  # "AbAbAb"
print(mix_string("AAAA", "BBbbB"))  # "AbAbAb"
print(mix_string("AAA", ""))  # "AAA"
print(mix_string("AAA", "B"))  # "ABAA"



def bingo(matrix: list, numbers: list) -> tuple:
    """
    Whether the matrix has winning combinations with the given numbers.

    Check if player got any winning combinations:
    1. Corners - all 4 corners contain winning numbers
    2. Diagonals - all diagonals contain winning numbers
    3. Full game - all numbers in the matrix/ticket are in the winning numbers
    Example matrix:
    [
        [ 5,  7, 11, 15, 21],
        [22, 25, 26, 27,  9],
        [34,  2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37,  3,  6, 32],
    ]

    :param matrix: 5 x 5 bingo ticket of numbers
    :param numbers: list of winning numbers (size always at least 4)
    :return: tuple of booleans (corners, diagonals, full_game)
    """
    ret_tuple = []
    corners = []
    corner_win = False
    corners.append(matrix[0][0])
    corners.append(matrix[0][4])
    corners.append(matrix[4][0])
    corners.append(matrix[4][4])
    for num in corners:
        if num in numbers:
            ret_tuple.append(True)
        else:
            ret_tuple.append(False)
    if ret_tuple[0] and ret_tuple[1] and ret_tuple[2] and ret_tuple[3]:
        corner_win = True

    diagonal = []
    for i in range(5):
        diagonal.append(matrix[i][i])
        diagonal.append(matrix[4-i][i])
    # print("diagonal", diagonal)
    # print("winning nr ", numbers)

    diag_win = True
    for elem in diagonal:
        if elem not in numbers:
            # print("This elem not on numbers!!!", elem)
            diag_win = False
            break

    full_win = False
    matrix_list = []
    for row in matrix:
        matrix_list.extend(row)
    print(matrix_list)

    if len(numbers) >= 25:
        full_win = True
        for elem in matrix_list:
            if elem not in numbers:
                # print("This elem not on numbers!!!", elem)
                full_win = False
                break

    result = (corner_win, diag_win, full_win)
    return result


print(bingo([[ 5,  7, 11, 15, 21],
        [22, 25, 26, 27,  9],
        [34,  2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37,  3,  6, 32],], [5, 7, 11, 15, 21, 22, 25, 26, 27, 9, 34, 2, 48, 54, 58, 59, 61, 33, 81, 24, 90, 37, 3, 6, 32]))


def reverse_substring(s: str, substring: str) -> str:
    """
    Reverse every substring in the string.

    Reverse every occurrence of substring and return the modified string.

    The function has to be recursive.
    No loops allowed!
    Also, "x in y" not allowed.

    reverse_subword("abcde", "bc") => "acbde"
    reverse_subword("abcabc", "bc") => "acbacb"
    reverse_subword("abcabc", "ac") => "abcabc"

    :param s: original string
    :param substring: len(substring) > 0
    :return:
    """
    pass


def valid_parentheses(sequence: str) -> bool:
    """
    Determine if the input string has valid parentheses.

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine whether the string is valid.

    The input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:
    Input: sequence = "()"
    Output: true

    Example 2:
    Input: sequence = "()[]{}"
    Output: true

    Example 3:
    Input: sequence = "(]"
    Output: false

    Example 4:
    Input: sequence = "([)]"
    Output: false

    Example 5:
    Input: sequence = "{[]}"
    Output: true

    :return boolean whether sequence is valid or not
    """
    pass


class Patient:
    """Patient."""

    def __init__(self, name: str, illness: str, age: int):
        """
        Patient class constructor.

        :param name: patient's name
        :param illness: patient's illness
        :param age: patient's age
        """
        self.name = name
        self.illness = illness
        self.age = age


class Hospital:
    """Hospital."""

    def __init__(self, address: str, illnesses_to_cure: list[str]):
        """Hospital class constructor."""
        pass

    def add_patients(self, patients: list[Patient]):
        """
        Add patients if their illness can be cured in this hospital.

        If the same patient is already in the hospital, do not add.

        :param patients: list of patients to add
        :return:
        """
        pass

    def add_patient(self, patient: Patient):
        """
        Add patient if their illness can be cured in this hospital.

        If the same patient is already in the hospital, do not add.

        :param patient: patient to add
        :return:
        """
        pass

    def add_new_illness_to_cure(self, illness: str):
        """
        Add an illness if it is new to this hospital.

        :param illness: illness to add
        :return:
        """
        pass

    def get_patients(self) -> list[Patient]:
        """
        Return list of all patients in the hospital.

        :return: list of all patients
        """
        pass

    def get_illnesses(self) -> list[str]:
        """
        Return list of all illnesses that can be treated in this hospital.

        :return: list of all illnesses
        """
        pass

    def get_patients_by_illness(self, illness: str) -> list[Patient]:
        """
        Get list of patients that have the same illness as given in parameter value.

        :return: list
        """
        pass

    def sort_patients_by_illness(self) -> list[Patient]:
        """
        Return list of patients sorted by illness in alphabetical order.

        If illness is the same, then sort by age in descending order.

        :return: sorted list of patients
        """
        pass

    def collect_patients_by_illness(self) -> dict[str, list[Patient]]:
        """
        Group patients by illness.

        Method should return dict with patients divided by illness, where dict key is illness and dict value is list
        of patients with this illness.
        {illness: [patient1, patient2]}

        :return: dict of patients divided by illness
        """
        pass


class Grade:
    """Grade."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Initialize grade."""
        self.assignment = assignment
        self.value = grade
        self.weight = weight
        self.date = date
        self.previous_grades = {}

    def change_grade(self, new_grade: int, date: str):
        """
        Change a previous grade.

        This function should save the previous grade in a dictionary previous_grades, where key is the date and value
        is the value of the grade. Value and date should be updated.
        """
        self.previous_grades[self.date] = self.value
        self.value = new_grade
        self.date = date
        # self.previous_grades[date] = self.value


class Student:
    """Student."""

    def __init__(self, name: str):
        """Initialize student."""
        self.name = name
        self.grades = {}

    def grade(self, grade: Grade):
        """
        Add a grade for an assignment that a students has done.

        Grades are kept in a dictionary where assignment name is the key and Grade object is the value (All previous
        grades for the same assignment are kept in the Grade object previous grades dictionary).
        Note that this function is only used when a student does an assignment for the first time.
        """
        self.grades[grade.assignment] = grade

    def redo_assignment(self, new_grade: int, assignment: str, date: str):
        """
        Update the grade for given assignment.

        This function is only used when an assignment has been attempted at least once before. Keep in mind that you
        need to also keep the history of grades, not create a new grade!
        """
        self.grades[assignment].change_grade(new_grade, date)

    def calculate_weighted_average(self):
        """
        Calculate the weighted average of grades.

        You should take into account the weights. There are three weights: 1, 2 and 3, where 3 means that one grade of
        weight 3 is the same as three grades of weight 1.

        For example:
        if there are grades 4 with weight 3 and 3 with weight 1, then the resulting value will be
                (4 * 3 + 3 * 1) / (3 + 1) = 15 / 4 = 3.75
        which will be rounded to 4.

        Also make sure not to miss out when a grade is noted as "!". If there is no attempt to redo this, then "!"
        should be equivalent to grade "1".
        """
        summ = 0
        count = 0
        for assig, grade in self.grades.items():
            if grade.value == "!":
                grade.value = 1
            summ += grade.weight * grade.value
            count += grade.weight
        return round(summ / count)


class Class:
    """Class."""

    def __init__(self, teacher: str, students: list):
        """Initialize class."""
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        """Add student to the class."""
        self.students.append(student)

    def add_students(self, students: list):
        """Add several students to the class."""
        self.students.extend(students)

    def remove_student(self, student: Student):
        """Remove student from the class."""
        self.students.remove(student)

    def get_grade_sheet(self):
        """
        Return grade sheet as a table.

        Grade sheet includes information of all the students in the class and their final grades.
        All edges should be either "|" or "-".
        First column is student's name and the second column is the final grade (weighted average).
        First, second and third row should look something like this (notice the capital letters):
        ----------------------
        | Name | Final grade |
        ----------------------

        Make sure that all the columns are correctly aligned after the longest element.
        For example, consider following rows:
        | Ago                   |  5  |
        | Some really long name |  3  |

        Rules are following:
        Each row (except for "-----" rows) starts with "|" and a space " " and ends with a space " " and "|".
        Text in "Name" column needs to be aligned to left
        Grades in "Final grade" column need to be centered

        Students in the table should follow the order which they were added to the class.

        The whole table would look something like this:
        ---------------------------------------
        | Name                  | Final grade |
        ---------------------------------------
        | Ago                   |      5      |
        | Johannes              |      4      |
        | Mari                  |      5      |
        | Some really long name |      3      |
        ---------------------------------------
        """
        longest_name = "Name"
        for st in self.students:
            if len(st.name) > len(longest_name):
                longest_name = st.name
        longest_name += " "
        table_line = "-"*(len(longest_name)+len(" | Final grade | "))
        name_line = "| Name" + (" "*(len(longest_name) - 4)) + "| Final grade |"

        table_header = table_line + "\n" + name_line + "\n"+table_line
        table_students = ""
        for student in self.students:
            student_name = student.name
            final_grade = student.calculate_weighted_average()
            padding = " " * (len(longest_name) - len(student_name))
            table_students += "| " + student_name + padding + "|      " + str(final_grade) + "      |\n"

        grade_sheet = table_header + "\n" + table_students + table_line
        return grade_sheet


if __name__ == '__main__':

    # Teacher, grade, student
    mari = Student("M")
    annamaria = Student("Anna Maria Jurgenson - Ivanova")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    #cl = Class("Anna", [mari, jyri, teele, annamaria])
    cl = Class("Anna", [])


    #cl.remove_student(annamaria)

    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    annamaria.grade(Grade(5, 5, "KT", "01/05/2028"))
    mari.calculate_weighted_average()
    gr = Grade(1, 3, "OOP", "01/09/2020")
    mari.grade(gr)
    mari.calculate_weighted_average()
    mari.redo_assignment(5, "KT", "02/09/2020" )
    mari.calculate_weighted_average()

    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))

    print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

    jyri.redo_assignment(3, "KT", "14/09/2020")
    print(len(gr.previous_grades))  # 1

    print(f"Jyri keskmine hinne on nyyd {jyri.calculate_weighted_average()}.")  # 3
    print()

    mari.grade(Grade(5, 1, "TK", "30/11/2020"))
    jyri.grade(Grade(4, 1, "TK", "30/11/2020"))
    teele.grade(Grade(3, 1, "TK", "30/11/2020"))

    print(f"Teele keskmine hinne on {teele.calculate_weighted_average()}.")  # 4
    print(cl.get_grade_sheet())
    print()

    tuuli = Student("Tuuli Karu")
    cl.add_student(tuuli)
    print(len(cl.students))  # 4
