"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """                       # kood kontrollib ja tagastab korrektse isikukoodi
    number = ""              # number in str
    for ch in text:
        if ch.isdigit():         # kas ch on number
            # print("this is isdigit " + ch)
            number = number + ch
    # print("number is " + number)
    if len(number) > 11:
        return "Too many numbers!"
    if len(number) < 11:
        return "Not enough numbers!"
    return number

# print(find_id_code("60106fff260245"))

def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    new_code = find_id_code(text)
    if len(new_code) > 11:  # kood kontrollib kas isikukood on korrektne ning kontrollib "moodul 11" 1 astme meetodiga
        return "1Incorrect ID code!"     # kui tektsi pikkus on rohkem kui 11 või väiksem siis kood ei ole korrektne
    if len(new_code) < 11:
        return "2Incorrect ID code!"
    summ = 0
    control = 1
    number_to_check = new_code[:10]       # numbers_to_check on 10 isikukoodi numbrit
    # print(number_to_check)
    for num in number_to_check:
        mult = int(num) * control
        summ = summ + mult               # liidab korrutised kokku
        print("id_code " + num + " control is " + str(control) + " multiply is " + str(mult) + " sum is " + str(summ))
        control = control + 1
        if control > 9:
            control = 1
    rem = summ % 11  # summa ja arvu jääk
    print("rem is " + str(rem))
    if rem >= 10:
        return "Needs the second algorithm!"
    last_digit = new_code[10]
    print("last digit is " + last_digit)
    if str(rem) != last_digit:
        return "3Incorrect ID code!"

    return new_code       # end of function control_1


text = "50006170231"

# print(the_first_control_number_algorithm(my_id_code))
print(the_first_control_number_algorithm("60106260fff245"))
