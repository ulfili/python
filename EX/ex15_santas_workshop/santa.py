"""SANTA'S WORKSHOP."""
import csv
from typing import Dict, Any

import requests
# import json


class Child:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.type = "unknown"    # nice or naughty
        self.wishlist = []       # kingitused

    def __repr__(self):
        return "Child name: " + self.name + ", Country: " + self.country + ", Type: " + self.type + ", Wishlist: " + str(self.wishlist)

    def set_child_type(self, type):
        self.type = type

    def add_wishlist(self, gifts: list):
        self.wishlist = gifts


class ChildrenStorage:
    all_children: dict[Any, Any]

    def __init__(self):
        self.all_children = {}

    def read_csv_children(self, file_name: str, child_type: str):
        with open(file_name, "rt") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                ch = Child(row[0], row[1].strip())
                ch.set_child_type(child_type)
                self.all_children[ch.name] = ch

    def read_wishlist_csv(self, file_name: str):
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
        default_gift = ["teddy bear"]
        for name, ch in self.all_children.items():
            if len(ch.wishlist) == 0:
                ch.add_wishlist(default_gift)
            if ch.wishlist == ["-"]:
                ch.add_wishlist(default_gift)


class Gift:

    def __init__(self, name: str, cost=0, time=0, weight=0):
        self.name = name
        self.cost = cost
        self.time = time
        self.weight = weight

    def __repr__(self):
        return "Gift : " + self.name + ", cost: " + str(self.cost) + ", time: " + str(self.time) + ", weight: " + str(self.weight)


class GiftStorage:

    def __init__(self):
        self.all_gifts = {}

    def add_gift(self, gift_name: str):
        self.all_gifts[gift_name] = Gift(gift_name)

    def print_all_gifts(self):
        ret_list = []
        for name, gift in self.all_gifts.items():
            ret_list.append(str(name) + " " + str(gift))
        return ret_list

    def get_info_from_server(self, gift_name: str):
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


"""if __name__ == "__main__":
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
    gift_storage.print_all_gifts()"""
