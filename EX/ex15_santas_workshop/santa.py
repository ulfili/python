"""SANTA'S WORKSHOP."""
import csv
from typing import Dict, Any

import requests
# import json


class Child:
    """
    A class representing a child.

    Attributes:
        name (str): The name of the child.
        country (str): The country of the child.
        type (str): The type of the child ("nice" or "naughty").
        wishlist (list): A list of gifts that the child wants.

    Methods:
        __repr__(): Returns a string representation of the child.
        set_child_type(type): Sets the type of the child.
        add_wishlist(gifts): Adds a list of gifts to the child's wishlist.
    """
    def __init__(self, name: str, country: str):
        """
        The constructor for Child.

        Parameters:
            name (str): The name of the child.
            country (str): The country the child is from.
        """
        self.name = name
        self.country = country
        self.type = "unknown"    # nice or naughty
        self.wishlist = []       # kingitused

    def __repr__(self):
        """
        A method that returns a string representation of the child.

        Returns:
            str: A string representation of the child.
        """
        return "Child name: " + self.name + ", Country: " + self.country + ", Type: " + self.type + ", Wishlist: " + str(self.wishlist)

    def set_child_type(self, type):
        """Sets child type."""
        self.type = type

    def add_wishlist(self, gifts: list):
        """Adding gifts to wishlist."""
        self.wishlist = gifts


class ChildrenStorage:
    """
    A class for storing children and their wishlists.

    Attributes:
        all_children (dict): A dictionary mapping child names to child objects.

    Methods:
       __init__(): Initializes an empty ChildrenStorage.
        read_csv_children(file_name, child_type): Reads children from a CSV file and stores them in all_children.
       read_wishlist_csv(file_name): Reads wishlists from a CSV file and updates the corresponding child objects in all_children.
       set_default_gift(): Sets a default gift for children with empty or invalid wishlists.
    """
    all_children: dict[Any, Any]

    def __init__(self):
        """Initializes an empty ChildrenStorage."""
        self.all_children = {}

    def read_csv_children(self, file_name: str, child_type: str):
        """
        Reads children from a CSV file and stores them in all_children.

        Parameters:
            file_name (str): The name of the CSV file to read.
            child_type (str): The type of the children ("nice" or "naughty").
        """
        with open(file_name, "rt") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                ch = Child(row[0], row[1].strip())
                ch.set_child_type(child_type)
                self.all_children[ch.name] = ch

    def read_wishlist_csv(self, file_name: str):
        """
        Reads wishlists from a CSV file and updates the corresponding child objects in all_children.

        Parameters:
            file_name (str): The name of the CSV file to read.
        """
        with open(file_name, "rt") as csv_file:
            for row in csv_file:
                gifts_list_2 = []
                name, gifts = row.split(",", 1)
                gifts = gifts.strip()
                gifts_list = gifts.split(",")
                for gift in gifts_list:
                    gifts_list_2.append(gift.strip())   # eemaldab tühikud
                if name in self.all_children:
                    ch = self.all_children[name]
                    ch.add_wishlist(gifts_list_2)

    def set_default_gift(self):
        """Sets a default gift for children with empty or invalid wishlists."""
        default_gift = ["teddy bear"]
        for name, ch in self.all_children.items():
            if len(ch.wishlist) == 0:
                ch.add_wishlist(default_gift)
            if ch.wishlist == ["-"]:
                ch.add_wishlist(default_gift)


class Gift:
    """
    A class representing a gift.

    Attributes:
        name (str): The name of the gift.
       cost (int): The cost of the gift.
       time (int): The time required to make the gift.
        weight (int): The weight of the gift.

    Methods:
        __repr__(): Returns a string representation of the gift.
       """

    def __init__(self, name: str, cost=0, time=0, weight=0):
        """The constructor for Gift. Sets gift name, cost, time and weight."""
        self.name = name
        self.cost = cost
        self.time = time
        self.weight = weight

    def __repr__(self):
        """Returns a string representation of the gift."""
        return "Gift : " + self.name + ", cost: " + str(self.cost) + ", time: " + str(self.time) + ", weight: " + str(self.weight)


class GiftStorage:
    """
    A class for storing gifts.

    Attributes:
        all_gifts (dict): A dictionary mapping gift names to gift objects.

    Methods:
        __init__(): Initializes an empty GiftStorage.
    """

    def __init__(self):
        """Initializes an empty GiftStorage."""
        self.all_gifts = {}

    def add_gift(self, gift_name: str):
        """
        Adds a gift to all_gifts.

        Args:
            gift_name (str): The name of the gift to add.
        """
        self.all_gifts[gift_name] = Gift(gift_name)

    def print_all_gifts(self):
        """
        Returns a list of strings representing all gifts in all_gifts.

        Returns:
            A list of strings representing all gifts in all_gifts. Each string is in the format "name cost time weight".
        """
        ret_list = []
        for name, gift in self.all_gifts.items():
            ret_list.append(str(name) + " " + str(gift))
        return ret_list

    def get_info_from_server(self, gift_name: str):
        """
        This function queries the server at the given URL for information about the gift specified by the gift_name parameter.
        If the gift already exists in the all_gifts dictionary, its information is updated.
        Otherwise, a new gift object is created and added to the dictionary.

        :param gift_name: str, the name of the gift to query
        """
        add = "%20"
        url_name = gift_name.replace(" ", add)
        adres = "https://cs.ttu.ee/services/xmas/gift?name=" + url_name
        r = requests.get(adres)
        gift_json = r.json()
        # print(gift_json)
        if gift_name in self.all_gifts:
            gift = self.all_gifts[gift_name]
            gift.cost = gift_json.get("material_cost", -1)
            gift.time = gift_json.get("production_time", -1)
            gift.weight = gift_json.get("weight_in_grams", -1)
        else:
            gift = Gift(gift_name)
            gift.cost = gift_json.get("material_cost", -1)
            gift.time = gift_json.get("production_time", -1)
            gift.weight = gift_json.get("weight_in_grams", -1)
            self.all_gifts[gift_name] = gift

        # print(self.all_gifts)

    def get_info_from_file(self, filename: str, gift_name: str) -> bool:
        """
        Gets gift information for the given gift name from a CSV file. If the gift is found in the file, the cost, time, and weight of the gift are updated in the all_gifts dictionary. If the gift is not found in the file, this function does not modify the all_gifts dictionary.

        @param filename: the name of the CSV file to read from
        @param gift_name: the name of the gift to look for in the file
        @return: True if the gift is found in the file, False otherwise
        """
        with open(filename, "rt") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                # print("Name is: ", row[0])
                if gift_name == row[0]:
                    # print("We get this gift in csv db!")
                    if gift_name in self.all_gifts:
                        gift = self.all_gifts[gift_name]
                        gift.cost = float(row[1].strip())   # material_cost
                        gift.time = float(row[2].strip())   # production_time
                        gift.weight = float(row[3].strip())   # weight_in_grams
                    else:
                        gift = Gift(gift_name)
                        gift.cost = float(row[1].strip())  # material_cost
                        gift.time = float(row[2].strip())  # production_time
                        gift.weight = float(row[3].strip())   # weight_in_grams
                        self.all_gifts[gift_name] = gift
                    return True
        return False

    def write_to_csv(self, filename: str, data: dict):
        """Writes info from server to new csv file."""

        fieldnames = ['name', 'cost', 'time', 'weight']
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(fieldnames)
            for k, v in data.items():
                row = []
                row.append(v.name)
                row.append(v.cost)
                row.append(v.time)
                row.append(v.weight)
                csv_writer.writerow(row)
        pass


if __name__ == "__main__":
    print("Hello Santa!")

    ch_storage = ChildrenStorage()
    print("We created a ChildrenStorage")

    filename = "ex15_naughty_list.csv"
    ch_storage.read_csv_children(filename, "naughty")

    filename = "ex15_nice_list.csv"
    ch_storage.read_csv_children(filename, "nice")

    filename = "ex15_wish_list.csv"
    ch_storage.read_wishlist_csv(filename)
    print("We had read all 3 files and sava all to ChildrenStorage")

    ch_storage.set_default_gift()

    gift_storage = GiftStorage()
    print("We created a GiftStorage")
    for name, ch in ch_storage.all_children.items():
        wishlist = ch.wishlist
        for gift in wishlist:
            gift_storage.add_gift(gift)

    for gift in gift_storage.all_gifts:
        print("Get info about gift: ", gift)
        if gift_storage.get_info_from_file("data_base.csv", gift):
            print("Update info from DB")
        else:
            gift_storage.get_info_from_server(gift)
            print("Update info from Server")

    gift_storage.write_to_csv("data_base.csv", gift_storage.all_gifts)
    gift_storage.print_all_gifts()
