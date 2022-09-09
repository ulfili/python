"""Math."""


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


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    act_1 = (a * d) + (c * b)
    act_2 = d * b
    return str(act_1) + "/" + str(act_2)


print(average(1, 2, 3, 4))
print(school_pressure(1, 1))
print(add_fractions(3, 1, 1, 1))
