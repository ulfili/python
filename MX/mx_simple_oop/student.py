"""Simple OOP."""


class Student:
    """Student class."""

    def __init__(self, name, finished):
        """Student constructor."""
        self.name = name
        self.finished = finished


student = Student("John", False)
print(student.name)
print(student.finished)
