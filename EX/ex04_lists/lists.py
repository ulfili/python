"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if len(all_cars) == 0:
        return []
    list = all_cars.split(",")
    return list


print(list_of_cars(" "))


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    all_cars_with_spaces = all_cars.replace(",", " ")   # asendan (replay) komad tühikutega
    words_list = all_cars_with_spaces.split()          # tühikute asemel on komad
    cars = (words_list[::2])         # võtan arvesse ainult paarisarvud (alustab lubemist 0st)
    return list(set(cars))          # set teeb listi, kui ei ole kordusi


print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    all_cars_with_spaces = all_cars.replace(",", " ")       # asendan komad tühikutega
    words_list = all_cars_with_spaces.split()               # tühikute asemele komad
    models = (words_list[1::2])                             # alustan lugemist 1st ja jagan 2ga
    return list(set(models))                                # list ilma korduseta


print(car_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
