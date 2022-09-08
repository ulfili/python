"""Math."""
import math


def average(a: int, b: int, c: int, d: int) -> float:
    a = a * 1
    b = b * 2
    c = c * 3
    d = d * 4
    return (a + b + c + d) / 4

def school_pressure(ects: int, weeks: int) -> float:
    ects = ects * 26
    weeks = weeks * 168
    eap = weeks / ects
    if ects > weeks:
        return -1
    if weeks > ects:
        return eap


def add_fractions(a: int, b: int, c: int, d: int) -> float:
    act_1 = int(a) + "/" + int(b)
    act_2 = int(c) + "/" + int(d)
    return act_1 + act_2

print(add_fractions(1, 2, 1, 2))