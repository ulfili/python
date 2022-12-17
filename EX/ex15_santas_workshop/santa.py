"""SANTA'S WORKSHOP."""
import csv
import requests
import json


class Child:
    def __init__(self, name, country):
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
    def __init__(self):
        self.all_children = {}

    def read_csv_children(self, file_name: str, child_type: str):
        with open(file_name, "rt") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                ch = Child(row[0], row[1])
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

    def add_cost(self, cost: int):
        self.cost = cost

    def add_time(self, time: int):
        self.time = time

    def add_weight(self, weight: int):
        self.weight = weight

class GiftStorage:

    def __init__(self):
        self.all_gifts = {}

    def add_gift(self, gift_name: str):
        self.all_gifts[gift_name] = Gift(gift_name)

    def print_all_gifts(self):
        for name, gift in self.all_gifts.items():
            print(name, gift)

    def get_info_from_server(self, gift_name: str):
        add = "%20"
        url_name = gift_name.replace(" ", add)
        adres = "https://cs.ttu.ee/services/xmas/gift?name=" + url_name
        r = requests.get(adres)
        gift_json = r.json()
        #print(gift_json)
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

        print(self.all_gifts)


    def write_to_csv(self, filename: str, data: dict):
        fieldnames = ['name', 'cost', 'time', 'weight']
        print( len(data))
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

    filename = "short_naugty.csv"
    ch_storage.read_csv_children(filename, "naughty")

    filename = "short_nice.csv"
    ch_storage.read_csv_children(filename, "nice")

    filename = "short_wishlist.csv"
    ch_storage.read_wishlist_csv(filename)

    ch_storage.set_default_gift()

    # for name, ch in ch_storage.all_children.items():
    #   print(ch)

    gift_storage = GiftStorage()
    #teddy = Gift("My Teddy", 10, 10, 5)
    gift_storage.add_gift("teddy")

    for name, ch in ch_storage.all_children.items():
        wishlist = ch.wishlist
        for gift in wishlist:
            gift_storage.add_gift(gift)

    #gift_storage.print_all_gifts()

    for gift in gift_storage.all_gifts:
        gift_storage.get_info_from_server(gift)

    gift_storage.write_to_csv("data_base.csv", gift_storage.all_gifts)
