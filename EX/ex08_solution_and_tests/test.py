import pytest

from solution import students_study


def test_student_study__evening_not_coffee_needed():
    """In the evening it doesn't matter whether we have coffee."""
    assert students_study(19, True) is True
    assert students_study(19,False) is True


def test_student_study__night_study():
    """At night in doesn't matter whether we have coffee."""
    assert students_study(1, True) is True
    assert students_study(1, False) is False


def test_student_study__day_study():
    """Coffee is needed in the morning."""
    assert students_study(14, True) is True
    assert students_study(14, False) is False
