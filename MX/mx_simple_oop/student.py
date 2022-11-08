"""Simple OOP."""


class Student:
    """Student class."""

    def __init__(self, name="Blablabla", finished=False, age=13):
        """Student constructor."""
        self.name = name
        self.finished = finished
        self.age = age


student = Student()
print(student.name)
print(student.finished)
print(student.age)
student2 = Student(finished = True)
print(student2.name)
print(student2.finished)
