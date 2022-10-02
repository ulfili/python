"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    my_dict = dict()
    my_persons_list = data.split()
    for person in my_persons_list:
        person_name, person_hobbie = person.split(":")
        print(f"Person with name {person_name} has hobbie {person_hobbie}")
        if person_name not in my_dict:
            my_dict[person_name] = [person_hobbie]
        else:
            person_hobbie_list = my_dict[person_name]
            if person_hobbie not in person_hobbie_list:
                person_hobbie_list.append(person_hobbie)
                my_dict[person_name] = person_hobbie_list
    return my_dict


print(create_dictionary("Jack:crafting(a)\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nJack:crafting\nPeter:hiking"))


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for person_name, person_hobbie in dic.items():
        person_hobbie.sort()
    return dic


print(sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}))
