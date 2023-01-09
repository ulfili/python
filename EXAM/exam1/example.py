"""Exam1 (2023-01-04)."""
from typing import Optional
import re
from operator import attrgetter


def count_digits(text: str) -> int:
    """
    Return the count of digits in a string.

    count_digits("123") => 3
    count_digits("a") => 0
    count_digits("") => 0
    count_digits("0a9r44") => 4
    """
    pattern = r"\d"
    match = re.findall(pattern, text)
    return len(match)


print(count_digits("123"))  # = > 3
print(count_digits("a"))  # = > 0
print(count_digits(""))  # = > 0
print(count_digits("0a9r44"))  # = > 4


def pairwise_min(numbers: list[int]) -> list[int]:
    """
    Return a list where for every element pair in the input list the minimum of those is used.

    If there are odd number of elements, ignore the last lonely element.

    pairwise_min([1, 2, 3, 4]) => [1, 3]
    pairwise_min([]) => []
    pairwise_min([1, 9, 2]) => [1]
    pairwise_min([9, 9, 2, 2]) => [9, 2]
    """
    small_num_list = []
    if len(numbers) == 0:
        return []
    if len(numbers) % 2 == 1:
        numbers = numbers[:-1]
    for i in range(0, len(numbers), 2):  # võtab i elemente üle 2. ehk esimene i on 0, neine 2 jne
        min_val = min(numbers[i], numbers[i + 1])
        small_num_list.append(min_val)
    return small_num_list


print(pairwise_min([1, 2, 3, 4]))   # => [1, 3]
print(pairwise_min([]))      # => []
print(pairwise_min([1, 9, 2]))   # => [1]
print(pairwise_min([9, 9, 2, 2]))  # => [9, 2]



def same_length(texts: list[str]) -> list[str]:
    """
    Normalize the lengths of the elements and return a list of those normalized elements in reverse order.

    You have to find the longest element in the list.
    Append "_" to every shorter element so that all the lengths are equal.
    Return a list of those equal-length elements in reverse alphabetical order.

    same_length(["a", "ab", "abc"]) => ["abc", "ab_", "a__"]
    same_length([]) => []
    same_length(["_", "ab_", "a"]) => ["ab_", "a__", "___"]
    """
    if len(texts) == 0:
        return []

    # Find the longest element in the list
    max_length = max(len(text) for text in texts)

    # Append "_" to every shorter element so that all the lengths are equal
    equal_length_texts = [text + "_" * (max_length - len(text)) for text in texts]

    # Return a list of those equal-length elements in reverse alphabetical order
    return sorted(equal_length_texts, reverse=True)


def max_average(data: list, n: int) -> float:
    """
    Find maximum average with window width of n.

    max_average([1, 2, 3], 2) = (2 + 3) / 2
      possible variants with window 2: [1, 2], [2, 3]
    max_average([1, 7, 4, 5, 6], 3) = (7 + 4 + 5) / 3 = 5.333333
      possible variants with window 3: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    :param data - data with at least n + 1 elements.
    :param n - Window width. Amount of consecutive numbers to take into calculation. n > 0.

    :return Maximum average achievable with current parameters.
    """
    # Calculate the maximum average using a window width of n
    max_average = sum(data[:n]) / n
    for i in range(1, len(data) - n + 1):
        max_average = max(max_average, sum(data[i:i + n]) / n)
    return max_average


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    The solution has to be recursive! (no loops allowed)

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    # Base case: fuel is negative or zero
    if fuel <= 0:
        return 0
    # Recursive case: fuel is positive
    else:
        # Calculate fuel needed for the current mass
        current_fuel = max(0, fuel // 3 - 2)
        # Calculate fuel needed for the fuel itself
        additional_fuel = fuel_calculator(current_fuel)
        # Return the total fuel needed
        return current_fuel + additional_fuel
    """Here is solution that uses loop:
    total_fuel = 0
    while fuel > 0:
        # Calculate fuel needed for the current mass
        current_fuel = max(0, fuel // 3 - 2)
        # Add fuel needed for the current mass to the total fuel
        total_fuel += current_fuel
        # Update fuel to be the fuel needed for the fuel itself
        fuel = current_fuel
    return total_fuel
    """

def longest_alphabet(text: str) -> str:
    """
    Find the longest substring which contains consecutive letters from alphabet.

    The input contains only lower case ascii letters (a - z).
    If there are several matches with the longest length, return the one which is lower alphabetically.

    longest_alphabet("abc") => "abc"
    longest_alphabet("abcklmn") => "klmn"
    longest_alphabet("klmabcopq") => "abc"
    longest_alphabet("a") => "a"
    longest_alphabet("xyab") => "ab"
    """
    # Initialize the result to the first character
    result = text[0]
    current_substring = text[0]
    for i in range(1, len(text)):
        # Check if the current character is consecutive with the previous character
        if ord(text[i]) == ord(text[i - 1]) + 1:
            # If it is, add it to the current substring
            current_substring += text[i]
        else:
            # If it's not, check if the current substring is longer than the result
            if len(current_substring) > len(result):
                result = current_substring
            # Reset the current substring to the current character
            current_substring = text[i]
    # Check if the final current substring is longer than the result
    if len(current_substring) > len(result):
        result = current_substring
    return result


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param filling: donut filling
        :param icing: donut icing
        """
        self.filling = filling
        self.icing = icing

    def __repr__(self):
        return "Donut with " + self.filling + " filling and " + self.icing + " icing."


class DonutFactory:
    """DonutFactory class."""

    def __init__(self):
        """DonutFactory class constructor."""
        self.donuts = []

    def __repr__(self):
        return "Donuts: ", str(self.donuts)

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        self.donuts.extend(donuts)

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        return self.donuts

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Method should return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        donuts_by_filling_and_icing = {}
        for donut in self.donuts:
            filling = donut.filling
            icing = donut.icing
            key = (filling, icing)
            if key not in donuts_by_filling_and_icing:
                donuts_by_filling_and_icing[key] = []
            donuts_by_filling_and_icing[key].append(donut)
        self.donuts = []
        return donuts_by_filling_and_icing

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Method should return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        sorted_donuts = sorted(self.donuts, key=lambda donut: (donut.icing, donut.filling))
        return sorted_donuts

    def get_most_popular_donut(self) -> dict:
        """
        Method should return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        Hint: you could use the result similar to pack_donuts_by_filling_and_icing method,
        but you cannot empty the production line of donuts.
        So, a common custom method can help here, which returns the dict.
        The most popular combination is the one element of the dict which has the most donuts
        (len on dict value is the highest).

        :return: dict with icing and filling of most pop donut
        """
        donuts_by_filling_and_icing = self.pack_donuts_by_filling_and_icing()
        most_pop_filling, most_pop_icing = max(donuts_by_filling_and_icing, key=lambda x: len(donuts_by_filling_and_icing[x]))
        return {"icing": most_pop_icing, "filling": most_pop_filling}

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        donuts_by_flavour = []
        for donut in self.donuts:
            if donut.icing == flavour or donut.filling == flavour:
                donuts_by_flavour.append(donut)
        return donuts_by_flavour




if __name__ == '__main__':
    donut_factory = DonutFactory()
    donut1 = Donut('chocolate', 'sugar')
    donut2 = Donut('caramel', 'chocolate')
    donut3 = Donut('cherry', 'marshmallow')
    donut4 = Donut('chocolate', 'sugar')
    donut5 = Donut('vanilla', 'cream')
    donut6 = Donut('vanilla', 'cream')
    donut7 = Donut('cherry', 'marshmallow')
    donut8 = Donut('chocolate', 'sugar')

    donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8]

    donut_factory.add_donuts(donuts)

    print(donut_factory.get_donuts_by_flavour("marshmallow"))  # == [donut3, donut7]
    print(donut_factory.get_most_popular_donut())  # == {'icing': 'sugar', 'filling': 'chocolate'}
    print(donut_factory.sort_donuts_by_icing_and_filling())  # == [donut2, donut5, donut6, donut3, donut7, donut1, donut4, donut8]
    print(donut_factory.pack_donuts_by_filling_and_icing())  # == {('chocolate', 'sugar'): [donut1, donut4, donut8],('caramel', 'chocolate'): [donut2],('cherry', 'marshmallow'): [donut3, donut7],('vanilla', 'cream'): [donut5, donut6]


class TravelItem:
    """Travel item."""

    def __init__(self, location: str, duration: int):
        """Initialize travel item with location and duration."""
        self.location = location
        self.duration = duration

    def get_location(self) -> str:
        """Return location."""
        return self.location

    def get_duration(self) -> int:
        """Return duration."""
        return self.duration


class TravelPackage:
    """Travel package combines multiple travel items."""

    def __init__(self, name: str):
        """Initialize the package with the given name."""
        self.name = name
        self.items = []

    def create_duplicate(self, new_name: str) -> 'TravelPackage':
        """
        Create a duplicate travel package.

        The new package will be created with the new name.
        Also, all the items should be copied to the new package.
        """
        new_package = TravelPackage(new_name)
        new_package.items = self.items[:]
        return new_package

    def get_total_duration(self) -> int:
        """Return the total duration of travel items in the package."""
        total_duration = 0
        for item in self.items:
            total_duration += item.get_duration()
        return total_duration

    def get_items(self) -> list[TravelItem]:
        """Return list of TravelItem objects."""
        return self.items

    def get_name(self) -> str:
        """Return the name of the package."""
        return self.name


class TravelAgency:
    """Travel agency coordinates travel items and packages."""

    def __init__(self):
        """Initialize the agency."""
        self.packages = []

    def add_item_to_package(self, package_name: str, item: TravelItem) -> bool:
        """
        Add an item to the travel package.

        If this item already exists in the package with the given name,
        the method returns False (and the item is not added).

        Otherwise:
        If there is no package with the given name, then the package is created.
        The item is added to the package with the given name.
        The method returns True.
        """
        for package in self.packages:
            if package.get_name() == package_name:
                if item in package.get_items():
                    return False
                package.get_items().append(item)
                return True
        new_package = TravelPackage(package_name)
        new_package.get_items().append(item)
        self.packages.append(new_package)
        return True

    def get_packages(self) -> list[TravelPackage]:
        """Return list of packages in the insertion order."""
        return self.packages

    def get_packages_by_location(self, location: str) -> list[TravelPackage]:
        """Return a list of TravelPackage objects where at least one item has the given location."""
        packages = []
        for package in self.packages:
            for item in package.get_items():
                if item.get_location() == location:
                    packages.append(package)
                    break
        return packages

    def search_package(self, locations: list, min_duration: int = None, max_duration: int = None) -> Optional[TravelPackage]:
        """
        Find a package which has all the locations specified in the list.

        If min_duration or max_duration is specified, then filter out packages,
        where total duration is between those values.

        If only min_duration is specified, use only those packages where total duration is greater or equal to that.
        If only max_duration is specified, use only those packages where total duration is less or equal to that.
        If both are specified, use packages where total duration is between those values.
        If none are specified, use all the packages.

        If locations list is empty, then every package matches.

        If multiple packages match, it doesn't matter which one to return.

        Return the found packages. If nothing matches, return None.
        """
        for package in self.packages:
            if not locations:
                matching_package = package
            else:
                matching_locations = [item.get_location() for item in package.get_items()]
                if set(locations).issubset(set(matching_locations)):
                    matching_package = package
                else:
                    continue
            total_duration = package.get_total_duration()
            if min_duration is not None and total_duration > max_duration:
                continue
            return matching_package
        return None

    def get_package_overview_by_locations(self) -> str:
        """
        Create an overview where for every location all the packages are listed.

        The overview contains locations (strings) ordered alphabetically.
        And for every location a list of package names where this location is included, also ordered alphabetically.

        The format:

        location1:
         - package1
         - package2
        location2:
         - package1
         - package3

        The location has no spaces in front of it and is followed by the colon.
        The package has space, minus and space in front of it.
        There is no new line in the end of the string.

        If there are no packages, return empty string.
        """
        location_dict = {}
        for package in self.packages:
            for item in package.get_items():
                location = item.get_location()
                if location in location_dict:
                    location_dict[location].append(package.get_name())
                else:
                    location_dict[location] = [package.get_name()]
        sorted_locations = sorted(location_dict.keys())
        overview = ""
        for location in sorted_locations:
            overview += "f{location}:\n"
            sorted_package_names = sorted(location_dict[location])
            for package_name in sorted_package_names:
                overview += f"f{package_name}\n"
        return overview


"""if __name__ == '__main__':


    item_tallinn = TravelItem("Tallinn", 200)
    item_tartu = TravelItem("Tartu", 150)

    agency = TravelAgency()
    assert agency.get_packages() == []

    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is True
    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is False

    assert agency.add_item_to_package("Estonian trip", item_tallinn) is True
    assert agency.add_item_to_package("Estonian trip", item_tartu) is True

    assert len(agency.get_packages()) == 2
    assert agency.get_packages()[0].get_name() == "Shorty in Tallinn"
    assert agency.get_packages()[1].get_name() == "Estonian trip"

    assert agency.get_packages()[1].get_total_duration() == 350

    packages = agency.get_packages_by_location("Tallinn")
    assert len(packages) == 2
    assert packages[0].get_name() == "Shorty in Tallinn"
    assert packages[1].get_name() == "Estonian trip"

    assert agency.get_packages_by_location("Narva") == []

    package = agency.search_package(["Tartu"])
    assert package.get_name() == "Estonian trip"
    package = agency.search_package(["Tallinn"])
    assert package.get_name() in ["Estonian trip", "Shorty in Tallinn"]
    package = agency.search_package(["Tallinn"], min_duration=300)
    assert package.get_name() == "Estonian trip"

    assert agency.get_package_overview_by_locations() == "Tallinn:\n - Estonian trip\n - Shorty in Tallinn\nTartu:\n - Estonian trip"
"""


class Candy:
    """Candy."""

    def __init__(self, name: str, filling: str):
        """
        Candy class constructor.

        :param name: candy name
        :param filling: candy filling
        """
        self.name = name
        self.filling = filling

    def __repr__(self):
        """Repr."""
        return "Candy name: " + self.name + ", Filling: " + self.filling


class CandyShop:
    """Candy shop."""

    def __init__(self):
        """Initialize candy Shop."""
        self.candies = []

    def add_candies(self, candies: list):
        """
        Add list of fresh candies to already existing ones.

        :param candies: list of candies to add
        :return:
        """
        self.candies.extend(candies)

    def get_candies(self) -> list:
        """
        Return list of all candies existing in the shop.

        :return: list of all candies
        """
        return self.candies

    def get_candies_by_filling(self, filling: str) -> list:
        """
        Get list of candies that have the same filling as given in parameter value.

        :return: list
        """
        candies_by_filling = []
        for candy in self.candies:
            if candy.filling == filling:
                candies_by_filling.append(candy)
        return candies_by_filling

    def sort_candies_by_filling(self) -> list:
        """
        Return list of candies sorted by filling in alphabetical order.

        If filling is the same, then sort
        by name in alphabetical order.

        :return: sorted list of candies
        """
        sorted_by_filling = sorted(self.candies, key=lambda candy: (candy.filling, candy.name))
        return sorted_by_filling

    def get_most_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the most popular candy name and filling.

        Method should return dict with name and filling of the most popular candy in the shop (type of candy which name
        and filling is present the most in the shop). NB! You should consider the most popular combination of name and filling.
        {name: most_pop_candy_name, filling: most_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of most pop candy
        """
        candy_counts = {}
        for candy in self.candies:
            name_filling = (candy.name, candy.filling)
            if name_filling in candy_counts:
                candy_counts[name_filling] += 1
            else:
                candy_counts[name_filling] = 1
        most_popular_candy = max(candy_counts, key=candy_counts.get)
        return {"name": most_popular_candy[0], "filling": most_popular_candy[1]}

    def get_least_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the least popular candy name and filling.

        Method should return dict with name and filling of the least popular candy in the shop (type of candy which name
        and filling is present the least in the shop). NB! You should consider the least popular combination of name and filling.
        {name: least_pop_candy_name, filling: least_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of least pop candy
        """
        candy_counts = {}
        for candy in self.candies:
            name_filling = (candy.name, candy.filling)
            if name_filling in candy_counts:
                candy_counts[name_filling] += 1
            else:
                candy_counts[name_filling] = 1
        least_popular_candy = min(candy_counts, key=candy_counts.get)
        return {"name": least_popular_candy[0], "filling": least_popular_candy[1]}


def collect_candies_by_filling(self) -> dict[str, list[Candy]]:
        """
        Group candies by filling.

        Method should return dict with candies divided by filling, where dict key is filling and dict value is list
        of candies with this filling.
        {candy_filling: [candy1, candy2]}

        :return: dict of candies divided by filling
        """
        pass

if __name__ == '__main__':
    # Candy shop
    candy_shop = CandyShop()
    candy1 = Candy('candy1', 'chocolate')
    candy2 = Candy('candy2', 'caramel')
    candy3 = Candy('candy3', 'nut')
    candy4 = Candy('candy1', 'chocolate')
    candy5 = Candy('candy2', 'vanilla')
    candy6 = Candy('candy2', 'vanilla')
    candy7 = Candy('candy3', 'nut')
    candy8 = Candy('candy1', 'chocolate')

    candies = [candy1, candy2, candy3, candy4, candy5, candy6, candy7, candy8]

    candy_shop.add_candies(candies)
    print(candies)

    print(candy_shop.get_candies_by_filling('chocolate'))  # == [candy1, candy4, candy8]
    print(candy_shop.get_least_popular_candy_name_and_filling())  # == {"name": "candy2", "filling": "caramel"}
    print(candy_shop.get_most_popular_candy_name_and_filling())   # == {"name": "candy1", "filling": "chocolate"}
    print(candy_shop.sort_candies_by_filling())  # == [candy2, candy1, candy4, candy8, candy7, candy3, candy6, candy5]
    print(candy_shop.collect_candies_by_filling())   # == {"chocolate": [candy1, candy4, candy8],"caramel": [candy2],"nut": [candy3, candy7],"vanilla": [candy5, candy6]}
