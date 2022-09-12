"""Math."""


def average(a: int, b: int, c: int, d: int) -> float:            # find average
    a = a * 1
    b = b * 2
    c = c * 3
    d = d * 4
    return (a + b + c + d) / 4


def school_pressure(ects: int, weeks: int) -> float:             # find eap
    hours_to_work = (ects*26)/weeks
    week_limit = hours_to_work * weeks
    if week_limit > 168:
        return -1
    if week_limit < 168:
        return hours_to_work


def add_fractions(a: int, b: int, c: int, d: int) -> str:        # find fraction answer
    act_1 = (a * d) + (c * b)
    act_2 = d * b
    return str(act_1) + "/" + str(act_2)


print(average(1, 2, 3, 4))
print(school_pressure(1, 1))
print(add_fractions(3, 1, 1, 1))
