"""Test of solutions."""
import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_student_study__evening_not_coffee_needed():
    """In the evening it doesn't matter whether we have coffee."""
    assert students_study(20, True) is True
    assert students_study(20, False) is True


def test_student_study__night_coffee_needed():
    """At night studens are sleeping."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False


def test_student_study__day_coffee_needed():
    """Coffee is needed in the morning."""
    assert students_study(9, True) is True
    assert students_study(9, False) is False


def test_lottery__all_same():
    """All numbers are same, but not 5."""
    assert lottery(3, 3, 3) == 5
    assert lottery(0, 0, 0) == 5
    assert lottery(-1, -1, -1) == 5


def test_lottery__all_five():
    """All numbers are 5."""
    assert lottery(5, 5, 5) == 10


def test_lottery__a_b_same_c_diff():
    """A and b are same, c is different."""
    assert lottery(2, 2, 3) == 0


def test__lottery_a_c_same_b_diff():
    """A and c are same, b is different."""
    assert lottery(2, 3, 2) == 0


def test_lottery__all_different():
    """All numbers are different."""
    assert lottery(1, 2, 2) == 1
    assert lottery(1, 2, 3) == 1


def test_fruit_order__all_zero():
    """All numbers are zero."""
    assert fruit_order(0, 0, 0) == 0
