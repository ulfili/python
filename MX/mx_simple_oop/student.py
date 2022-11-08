"""Simple OOP."""


class Student:
    """Student class."""

    def __init__(self, name, finished=False):
        """Student constructor."""
        self.name = name
        self.finished = finished


student = Student("John")
print(student.name)
print(student.finished)
