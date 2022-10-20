"""Test of solutions."""
import pytest
from solution import students_study


def test_student_study__evening_not_coffee_needed():
    """In the evening it doesn't matter whether we have coffee."""
    assert students_study(20, True) is True
    assert students_study(20, False) is True


def test_student_study__night_coffee_needed():
    """At night studens are sleeping."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
