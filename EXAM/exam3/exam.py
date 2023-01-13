"""Exam3 (2023-01-10)."""
from typing import Optional


def split_string_into_ints(numbers: str) -> list:
    """
    Return list of integers from comma-separated string of integers.

    split_string_into_ints("1,2") => [1, 2]
    split_string_into_ints("") => []
    split_string_into_ints("0") => [0]
    split_string_into_ints("-1,-2,3") => [-1, -2, 3]
    """
    pass


def repeat_multiples(numbers: list) -> list:
    """
    Repeat every element divisible by 2 twice, and every element divisible by 3 three times.

    The element which is divisible by 2 and 3 should be repeated 4 times.

    repeat_multiples([1, 2, 3]) => [1, 2, 2, 3, 3, 3]
    repeat_multiples([1, 5, 7]) => [1, 5, 7]
    repeat_multiples([22, 33]) => [22, 22, 33, 33, 33]
    repeat_multiples([]) => []
    repeat_multiples([6]) => [6, 6, 6, 6]
    repeat_multiples([0, 2, 9]) => [0, 0, 0, 0, 2, 2, 9, 9, 9]
    """
    return_list = []

    for num in numbers:
        if num % 6 == 0:
            return_list.extend([num] * 3)
        else:
            if num % 3 == 0:
                return_list.extend([num] * 2)
            if num % 2 == 0:
                return_list.extend([num] * 1)
        return_list.append(num)

    return return_list


print(repeat_multiples([396, 6, 18, 66]))
print(repeat_multiples([1, 2, 3]))  # => [1, 2, 2, 3, 3, 3]
print(repeat_multiples([1, 5, 7]))   # => [1, 5, 7]
print(repeat_multiples([22, 33]))  #  => [22, 22, 33, 33, 33]
print(repeat_multiples([2, 2]))


def count_double_chars(s: str) -> int:
    """
    Count only double symbols.

    Count how many double symbols are in the text. You have to only count pairs.
    Therefore, a pair of symbols which is not preceded or followed by the same symbol.
    If there are three or more of the same symbol, then this is not a pair and doesn't count.
    Any printable symbol counts (letters, digits, punctuation, space etc.).

    assert count_double_chars("abc") == 0
    assert count_double_chars("aabc") == 1
    assert count_double_chars("aaabc") == 0  # (three "a"-s doesn't count)
    assert count_double_chars("aaaabc") == 0  # (four "a"-s also doesn't count)
    assert count_double_chars("aabbc") == 2
    assert count_double_chars("") == 0
    assert count_double_chars("abbcdd") == 2
    assert count_double_chars("aabbaa") == 3
    assert count_double_chars(",,!?") == 1
    assert count_double_chars("a  b  =") == 2
    """
    result = 0

    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                if (i == 0 or s[i - 1] != s[i]) and (i == len(s) - 2 or s[i + 1] != s[i + 2]):
                    result += 1
    return result


print(count_double_chars("ab"))  # == 0
print(count_double_chars("a"))  # == 0
print(count_double_chars(""))  # 0
print(count_double_chars("aa"))  # == 1
print(count_double_chars("aabc"))  # 1
print(count_double_chars("aaaabbbc")) # == 0
print(count_double_chars("aabbc"))  # 2
print(count_double_chars("aaabbcc"))   # 2
print(count_double_chars("124999"))  # 0


def reverse_list(input_strings: list) -> list:
    """
    Reverse the list and elements except for "python" and "java" and everything between.

    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    reverse_list(['apple', 'banana', 'onion']) -> ['noino', 'ananab', 'elppa']
    reverse_list(['lollipop', 'python', 'candy']) -> ['candy', 'python', 'popillol']
    reverse_list(['sky', 'python', 'candy', 'java', 'fly']) -> ['ylf', 'java', 'candy', 'python', 'yks']
    reverse_list(['sky', 'python', 'java', 'candy']) -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    reverse_mode = True
    ret_list = []
    for elem in input_strings:
        print(elem)
        if elem == "python" or elem == "java":
            rev_eml = elem
            if elem == "python":
                reverse_mode = False
                print(reverse_mode)

            if elem == "java":
                reverse_mode = True
                print(reverse_mode)
        else:
            if reverse_mode:
                rev_eml = elem[::-1]
            else:
                rev_eml = elem

        ret_list.append(rev_eml)
    print(ret_list)
    ret_list.reverse()
    return ret_list


print(reverse_list(['apple', 'banana', 'onion']))   # -> ['noino', 'ananab', 'elppa']
print(reverse_list(['lollipop', 'python', 'candy']))    # -> ['candy', 'python', 'popillol']
print(reverse_list(['sky', 'python', 'candy', 'java', 'fly']))   # -> ['ylf', 'java', 'candy', 'python', 'yks']
print(reverse_list(['sky', 'candy', 'java', 'fly']))   # -> ['ylf', 'java', 'candy', 'python', 'yks']


def substring(s: str, count: int) -> str:
    """
    Return first part of string with length of count.

    #06

    Function should be recursive, loops (for/while) are not allowed!
    count <= len(string)

    assert substring("hello", 2) == "he"
    assert substring("hi", 2) == "hi"
    assert substring("house", -1) == ""
    assert substring("house", 0) == ""

    :param s: input string.
    :param count: int, count <= len(string).
    :return: first count symbols from string.
    """
    if count <= 0:
        return ""
    # return s[0:count]
    return s[0] + substring(s[1:], count - 1)

print(substring("hello", 2))  # == "he"
print(substring("hi", 2))  # == "hi"
print(substring("house", -1))  # == ""
print(substring("house", 0))  # == ""



def plot_the_tangerines(integers: list[int]) -> str:
    """
    Create a bar graph with non-negative numbers.

    Recently you have noticed that your consumption of tangerines is too high.
    You want to monitor the situation so you try to make a bar graph of tangerines consumption in Excel.
    But Excel won't work, because you have just started using Linux.
    Oh well, it seems that you have to make your own program to plot graphs and do fancy calculations.

    Graph consists of scale (left) and stack of '#'s that represent integer in the list (consumed tangerines in a day).
    0 means stack of 0 '#', 1 means stack of 1 '#', 2 means stack of 2 '#' and so on.

    Graph max height should be the maximum value from the list, max is always at least 1.
    There is always at least one element in the list.
    Graph needs to be in a frame consisting of '|', '-' and '+' characters as shown in examples.
    There should be no newlines before or after the graph.


    plot_the_tangerines([1, 0, 2, 3, 4, 5, 4, 3, 2, 1, 0, 3, 2, 1]) =>
     +--------------+
    5|     #        |
    4|    ###       |
    3|   #####   #  |
    2|  #######  ## |
    1|# ######## ###|
    0+--------------+

    plot_the_tangerines([0]) =>
     +-+
    1+ +
    0+-+

    plot_the_tangerines([0, 0, 0, 0, 0, 0])) =>
     +------+
    1|      |
    0+------+

    plot_the_tangerines([1, 4, 5, 3, 1]) =>
     +-----+
    5|  #  |
    4| ##  |
    3| ### |
    2| ### |
    1|#####|
    0+-----+

    In case the maximum value is is more than 9, the left side should be wider, aligned to right:

       +-----
    100|
     99|
     ....
      9|#
      8|#
      ...
      0+-----
    """
    pass


class Student:
    """Represent student model."""

    def __init__(self, name: str, gpa: float, age: int):
        """
        Initialize student.

        Each student has name and gpa (Grade Point Average).

        :param name: student's name
        :param gpa: student's gpa
        :param age: student's age
        """
        self.age = age
        self.gpa = gpa
        self.name = name

    def __repr__(self):
        """Repr."""
        return "Name: " + self.name + " GPA: " + str(self.gpa) + " Age: " + str(self.age)


class University:
    """Represent university model."""

    def __init__(self, name: str, gpa_required: float):
        """
        Initialize university.

        Each university has name and gpa_required.

        University should also have a database to keep and track all students.
        :param name: university name
        :param gpa_required: university required gpa
        """
        self.name = name
        self.gpa_required = gpa_required
        self.students_list = []

    def __repr__(self):
        """Repr."""
        return "University name: " + self.name + " GPA required: " + str(self.gpa_required)


    def can_enroll_student(self, student: Student) -> bool:
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa (>=)
            * he/she is not already enrolled to this university
            * he/she is at least 16 years old
            * additionally, if student's name characters length is
            exactly 13 -> student can be added to university despite gpa (though still should not be
            already present in university and be younger)
        If the student cannot be enrolled, returns False. Otherwise returns True.

        :return: bool
        """
        if len(student.name) == 13:
            if student.age >= 16:
                if student not in self.students_list:
                    return True
        if student.gpa >= self.gpa_required:
            if student.age >= 16:
                if student not in self.students_list:
                    return True

        return False

    def enroll_student(self, student: Student):
        """
        Enroll new student to university if possible.

        Before enrolling, you have to check whether student can be enrolled.

        :param student: Student
        Function does not return anything
        """
        if self.can_enroll_student(student):   # is True
            self.students_list.append(student)

    def can_unenroll_student(self, student: Student) -> bool:
        """
        Check if student can leave from university.

        Student can be successfully leave if he/she actually studies in this university.

        Returns True, if the student can be unenrolled, False otherwise.

        :return: bool
        """
        if student in self.students_list:
            return True
        return False

    def unenroll_student(self, student: Student):
        """
        Unenroll student from University if possible.

        Before unenrolling, you have to make sure the student can be unenrolled.
        Function does not return anything
        """
        if self.can_unenroll_student(student):
            self.students_list.remove(student)

    def get_students(self) -> list:
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        return self.students_list

    def get_student_highest_gpa(self) -> list:
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        highest_gpa_list = []
        highest_gpa = 0
        for student in self.students_list:
            if student.gpa > highest_gpa:
                highest_gpa = student.gpa
        print("highest_gpa", highest_gpa)

        for student in self.students_list:
            if student.gpa == highest_gpa:
                highest_gpa_list.append(student)
        return highest_gpa_list




if __name__ == "__main__":
    Taltech = University("Taltech", 60)
    student1 = Student("Bob", 65, 18)
    student2 = Student("Mari", 59, 20)
    student3 = Student("Tom", 65, 22)
    student4A = Student("1234567890123", 30, 15)
    student4B = Student("1234567890123", 30, 16)


    print(student1, Taltech.can_enroll_student(student1))  # True
    print(student2, Taltech.can_enroll_student(student2))  # False
    print(student3, Taltech.can_enroll_student(student3))  # True
    print(student4A, Taltech.can_enroll_student(student4A))  # False
    print(student4B, Taltech.can_enroll_student(student4B))  # True

    Taltech.enroll_student(student1)
    print(student1, Taltech.can_enroll_student(student1))

    Taltech.enroll_student(student4B)
    print(student4B, Taltech.can_enroll_student(student4B))
    print(Taltech.students_list)
    Taltech.enroll_student(student3)

    print(student1, Taltech.can_unenroll_student(student1))  # True
    print(student2, Taltech.can_unenroll_student(student2))  # False

    """university.unenroll_student(student1)
    print(university.students_list)"""

    print(Taltech.get_students())  # [student]
    print(Taltech.get_student_highest_gpa())  # [student]; since this student is the only one

    print(Taltech.can_unenroll_student(student1))  # True
    Taltech.unenroll_student(student1)
    print(Taltech.get_students())  # []


class ComputerPart:
    """A computer part."""

    def __init__(self, name: str, cost: float):
        """
        Initialize computer part.

        Each computer part has a name and a cost.
        """
        self.name = name
        self.cost = round(cost, 2)

    def get_cost(self) -> float:
        """Return the cost of the computer part."""
        return self.cost

    def __repr__(self):
        """Repr."""
        return self.name


class Computer:
    """A computer at an internet cafe."""

    def __init__(self, name: str, total_parts_needed: int):
        """
        Initialize computer.

        Each computer has name and the amount of parts required for it to function.

        A computer should also keep track of all the parts that are in it.
        :param name: computer name
        :param total_parts_needed: the amount of parts needed for the computer to function
        """
        self.name = name
        self.total_parts_needed = total_parts_needed
        self.working = False
        self.parts_list = []
        self.cost = 0.00

    def add_part(self, part: ComputerPart):
        """
        Add a part to the computer.

        The parts cost is also added to the computers cost.

        The part is not added if the computer is already working.
        """
        if self.working:    # is True (is working)
            return
        self.parts_list.append(part)
        self.cost += part.cost

    def get_parts_needed(self) -> int:
        """
        Return the amount of parts that is needed to fully build this computer.

        If the computer needs a total of 3 parts and currently has 1 part, this should return 2.
        """
        if self.total_parts_needed == len(self.parts_list):
            return 0
        if self.total_parts_needed > len(self.parts_list):
            return self.total_parts_needed - len(self.parts_list)

    def is_working(self) -> bool:
        """Return if the computer has the correct amount of parts."""
        if self.get_parts_needed() == 0:
            return True
        return False
        # if self.total_parts_needed == len(self.parts_list):
        #   return True

    def get_parts(self) -> list[ComputerPart]:
        """
        Return a list of all parts that are in the computer.

        Parts should be in the same order as they were added.
        """
        return self.parts_list

    def get_cost(self) -> float:
        """Return the cost of the computer."""
        return round(self.cost, 2)

    def __repr__(self) -> str:
        """
        Return string representation of Computer.

        Returns string in form "A {name} for {cost}€ with {parts}"

        All the parts should be seperated with ", ".
        Parts should be in the same order as they were added.
        If there are no parts in the computer, there should be "nothing".
        Cost is always shown with 2 decimal places.

        Examples:
        "A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860"
        "A pc for 0.00€ with nothing"
        """
        computer_parts = "nothing"
        parts_name_list = []
        for elem in self.parts_list:
            parts_name_list.append(elem.name)

        if len(parts_name_list):
            computer_parts = ",".join(parts_name_list)

        return "A " + self.name + " for " + str(self.cost) + "€ with " + computer_parts


class Customer:
    """A customer at an internet cafe."""

    def __init__(self, name: str, money: float):
        """
        Initialize customer.

        Each customer must have a name, money and it should also keep track of owned computers.
        """
        self.name = name
        self.money = round(money, 2)
        self.computer_list = []

    def can_buy_computer(self, computer: Computer) -> bool:
        """Return if this customer has enough money to buy a computer."""
        if self.money >= computer.cost:
            return True
        return False

    def buy_computer(self, computer: Computer) -> bool:
        """
        Buy a computer if it can be done.

        This customer loses money equal to the cost of the computer.

        Returns True or False whether the computer was bought.
        """
        if self.can_buy_computer(computer):
            return True
        return False

    def get_computers(self) -> list[Computer]:
        """Return all computers owned by this customer."""
        return self.computer_list

    def __repr__(self) -> str:
        """
        Return string representation of a customer.

        Should be in format:
        "{name} with {money}€
        {computer1}
        {computer2}
        {computer3}
        ..."

        The money is always shown with 2 decimal places.

        example1:
        "Laura with 666.00€
        A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860
        A pc for 0.00€ with nothing"

        example2:
        "Karl with 0.00€"
        """
        for computer in self.computer_list:
            return self.name + " with " + str(self.money) + " €\n" + computer


class ComputerStore:
    """A store where people can buy computers."""

    def __init__(self):
        """Initialize computer store."""
        self.computer_store = []
        self.part_store = []
        self.working_computers_list = []

    def add_computer(self, computer: Computer):
        """Add a computer to the store."""
        self.computer_store.append(computer)

    def add_part(self, part: ComputerPart):
        """Add a computer part to the storage of the store."""
        self.part_store.append(part)

    def get_computers(self) -> list[Computer]:
        """Return all computers in the stores as a list."""
        return self.computer_store

    def get_parts(self) -> list[ComputerPart]:
        """Return all unused computer parts in the store."""
        return self.part_store

    def get_working_computers(self) -> list[Computer]:
        """Return all computers which are working."""
        for computer in self.computer_store:
            if computer.is_working():
                self.working_computers_list.append(computer)
        return self.working_computers_list

    def build_computer(self) -> Optional[Computer]:
        """
        Make the store build a computer.

        If the store has no non-functioning computers, return None.

        The store looks at the computer which have the least amount of parts missing.
        If two computers have the same amount of parts missing, then the store picks the one that is cheaper.
        (there aren't any cases where computers parts missing and costs are equal)

        example:
        computer1 costs 100 and 3 parts missing
        computer2 costs 300 and 3 parts missing
        computer3 costs 50 and 4 parts missing
        computer4 costs 10 and 0 parts missing (it is already functional)
        The store chooses to build computer1!

        If the store doesn't have enough spare parts to build a computer, return None.

        The store adds the cheapest available parts to the computer until it is built.

        If the computer is built successfully, return the built computer. Else return None.
        """
        pass

    def sell_customer_computer(self, customer: Customer):
        """
        Sell computer to customer.

        A customer walks into the store and wants the most expensive working computer that can be bought with their money.

        Note that the sold computer must work.

        If there are no such computers, the store tries to build a new computer.

        If a computer is successfully built and it is cheap enough to buy, then the customer buys that computer.
        """
        pass


if __name__ == '__main__':

    # Start of OOP2 ComputerStore
    computer1 = Computer("pc", 3)
    computer1.add_part(ComputerPart("cpu", 200))
    computer1.add_part(ComputerPart("mobo", 60.5))
    computer1.add_part(ComputerPart("case", 70))

    assert computer1.get_cost() == 330.5
    assert computer1.is_working() is True
    print(computer1)


    computer2 = Computer("laptop", 3)
    computer2.add_part(ComputerPart("display", 160))
    computer2.add_part(ComputerPart("keyboard", 20))
    print(computer2)
    #assert repr(computer2) == "A laptop for 180.00€ with display, keyboard"
    assert computer2.is_working() is False

    macAir = Computer("MacAir otstoj", 3)
    print(macAir)

    store = ComputerStore()
    store.add_part(ComputerPart("mousepad", 36))
    store.add_computer(computer1)
    store.add_computer(computer2)

    assert len(store.get_computers()) == 2  # 2 computers are in the store
    assert len(store.get_working_computers()) == 1  # 1 computer is working

    store.build_computer()  # add mousepad to laptop

    assert len(store.get_working_computers()) == 2  # both computers are working now

    laura = Customer("Laura", 1000)

    store.sell_customer_computer(laura)  # sell pc to laura

    # assert len(store.get_computers()) == 1  # only laptop left in store

    print(laura)   # == "Laura with 669.50€\nA pc for 330.50€ with cpu, mobo, case"  # Laura has a pc now
