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
    cars_list = all_cars.split(",")
    return cars_list


print(list_of_cars("Tesla Model S,a b,c d e g f,Skoda Super Lux Sport"))


def car_makes_models(all_cars: str) -> tuple[list, list]:
    """ This is a general function to return list of makers and models. """
    cars_list = list_of_cars(all_cars)
    # print("car list is: ", cars_list)
    maker_list = list()
    model_list = list()
    for car in cars_list:
        # print("now car is: ", car)
        maker, model = car.split(" ", 1)
        # print("maker is: " + maker + " model is: " + model)
        maker_list.append(maker)
        model_list.append(model)
        # print("maker list is: " + str(maker_list) + " model list is: " + str(model_list))
    return maker_list, model_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    car_makes_list, car_models_list = car_makes_models(all_cars)
    unique_makes_list = list()
    for maker in car_makes_list:
        if maker not in unique_makes_list:
            unique_makes_list.append(maker)           # lisab listi listi sisse
    return unique_makes_list


print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Tesla Model S,Skoda Super Lux Sport"))


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    car_makes_list, car_models_list = car_makes_models(all_cars)
    unique_model_list = list()
    for model in car_models_list:
        if model not in unique_model_list:
            unique_model_list.append(model)
    return unique_model_list


print(car_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Tesla Model S,Skoda Super Lux Sport"))


def search_by_make(all_cars: str, maker: str) -> list:
    """ This function is for searching cars by manufactor. """
    car = ""
    car_list = list()
    car_makes_list, car_models_list = car_makes_models(all_cars)
    for i in range(len(car_makes_list)):
        makes = car_makes_list[i]
        model = car_models_list[i]
        # print("makes is: ", makes, " model is: ", model, " i is: " , i)
        if makes.capitalize() == maker.capitalize():
            # print("makes is: ", makes, " model is: ", model)
            car = makes + " " + model
            car_list.append(car)
    return car_list


print(search_by_make("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,tesla Model S,Skoda Super Lux Sport", "TESLA"))
print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "audi"))


def search_by_model(all_cars: str, model: str) -> list:
    """ This function is for searching cars by model. """
    car = ""
    car_list = list()
    car_makes_list, car_models_list = car_makes_models(all_cars)
    for i in range(len(car_models_list)):
        makes = car_makes_list[i]
        car_model = car_models_list[i]
        # print("makes is: ", makes, " model is: ", model, " i is: " , i)
        # if car_model.capitalize() == model.capitalize():
        model_word_list = car_model.split()
        # print("model word list is: ", model_word_list)
        for m in model_word_list:
            if m.upper() == model.upper():
                # print("makes is: ", makes, " model is: ", car_model)
                car = makes + " " + car_model
                car_list.append(car)
    return car_list


print(search_by_model("Audi A4 ,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,tesla Model S,Skoda Super Lux Sport", "lux"))
print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4"))
