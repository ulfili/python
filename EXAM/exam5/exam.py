"""Exam5 (2023-01-14)."""
from enum import Enum


def count_camel_case_words(text: str) -> int:
    """
    Count the words in the text.

    The text uses camel case. There are no spaces between words.
    Each new word starts with a capital letter.
    The first word can start with a small or a capital letter.

    count_camel_case_words("hello") => 1
    count_camel_case_words("") => 0
    count_camel_case_words("helloWorld") => 2
    count_camel_case_words("HelloWorld") => 2
    count_camel_case_words("aBC") => 3
    count_camel_case_words("ABC") => 3
    count_camel_case_words("a") => 1
    count_camel_case_words("What") => 1
    """
    if len(text) == 0:
        return 0
    result = 0
    if text[0] == text[0].upper() or text[0] == text[0].lower():
        result += 1
    for i in range(1, len(text)):
        if text[i] == text[i].upper():
            result += 1
    return result


print(count_camel_case_words("hello"))   # => 1
print(count_camel_case_words(""))  # => 0
print(count_camel_case_words("helloWorld"))   #  => 2
print(count_camel_case_words("HelloWorld"))   # => 2
print(count_camel_case_words("aBC"))   # => 3
print(count_camel_case_words("ABC"))    #=> 3
print(count_camel_case_words("a"))    #=> 1
print(count_camel_case_words("What"))    # => 1


def odd_index_sum(nums: list) -> int:
    """
    Find sum of elements with odd indices.

    odd_index_sum([1, 2, 3]) => 2
    odd_index_sum([]) => 0
    odd_index_sum([1]) => 0
    odd_index_sum([2, 3]) => 3
    odd_index_sum([0, -1, -4, -3]) => -4
    odd_index_sum([0, -1, -4, -3, 6, 7]) => 3
    """
    result = 0
    for i in range(1, len(nums), 2):
        result += nums[i]
    return result


print(odd_index_sum([1, 2, 3]))   # => 2
print(odd_index_sum([]))   # => 0
print(odd_index_sum([1]))     # => 0
print(odd_index_sum([2, 3]))    # => 3
print(odd_index_sum([0, -1, -4, -3]))    # => -4
print(odd_index_sum([0, -1, -4, -3, 6, 7]))    # => 3


def prettify_string(input_string: str) -> str:
    """
    Prettify string.

    - After every punctuation (,.!?:;-) there should be at least one space.
    - Every sentence should start with an uppercase letter.
    - Sentence starts after .!?
    - Also in the beginning of the string a new sentence starts

    There are no consecutive punctuation in the input string.

    Examples:
    "Hello,I am the input of this function.please make me pretty!" => "Hello, I am the input of this function. Please
    make me pretty!"
    "there should be space after me-and also space after me;next sentence should be capitalized! i need to be capitalized but
    no new space should be added." => "There should be space after me- and also space after me; next sentence should be capitalized! I need to be capitalized but
    no new space should be added."
    """
    space = False
    result = ""
    for c in input_string:
        if space:
            if c != " ":
                result += " "
            space = False
        if c in ",.!?:;-":
            space = True
        result += c
    cap = True
    input_string = result
    result = ""
    for c in input_string:
        if cap:
            if c != " ":
                c = c.upper()
                cap = False
        if c in ".!?-":
            cap = True
        result += c
    return result


print(prettify_string("hello.im string."))   # Hello. Im string
print(prettify_string("Hello!i am input of this func,make me pretty."))   # Hello! I am input of this func, make me pretty.


def get_max_nums(nums: list) -> list:
    """
    Return list with maximum numbers from the original list.

    print(get_max_nums([1, 2, 34, 4, 5, 34, 34])) => [34, 34, 34]
    print(get_max_nums([-1, -1, -1, -1, -1, -6])) => [-1, -1, -1, -1, -1]
    print(get_max_nums([3, 4, 5, 6, 3])) => [6]
    print(get_max_nums([6])) => [6]
    print(get_max_nums([])) => []

    :param nums: list of integers.
    :return: list of maximum numbers from the original list.
    """
    """if nums == []:
        return []
    max_nr = max(nums)
    return [nr for nr in nums if nr == max_nr]"""
    highest_num = -1000000000
    highest_nums_list = []
    for num in nums:
        if num > highest_num:
            highest_num = num
    for num in nums:
        if num == highest_num:
            highest_nums_list.append(num)
    return highest_nums_list


print(get_max_nums([1, 2, 34, 4, 5, 34, 34]))   # => [34, 34, 34]
print(get_max_nums([-1, -1, -1, -1, -1, -6]))   # => [-1, -1, -1, -1, -1]
print(get_max_nums([3, 4, 5, 6, 3]))  # => [6]
print(get_max_nums([6]))  # => [6]
print(get_max_nums([]))   # => []


def mirror_ends(s: str) -> str:
    """
    Return the first non-matching symbol pair from both ends.

    The function has to be recursive. No loops allowed!

    Starting from the beginning and end, find the first symbol pair which does not match.
    If the input string is a palindrome (the same in reverse) then return "" (empty string).

    mirror_ends("abc") => "ac"
    mirror_ends("aba") => ""
    mirror_ends("abca") => "bc"
    mirror_ends("abAAca") => "bc"
    mirror_ends("") => ""
    """
    if len(s) < 2:
        return ""
    if s[0] == s[-1]:
        return mirror_ends(s[1:-1])
    return s[0] + s[-1]


def invert_repetitions(s: str) -> str:
    """
    Remove repeated characters and repeat single characters.

    Repeated character (2 or more consecutive same characters) has to be replaced with single character.

    Easier option: repeat single characters twice. (gives 60% points )

    Harder option: add 1 additional character each time you need to repeat the same char.
    "abbabba" => "aabaaabaaaa"
    The first time "a" becomes "aa", the second time it becomes "aaa", and then "aaaa" etc.

    Result of empty string is also empty string.

    Examples:
    '' -> ''
    'a' -> 'aa'
    'aa' -> 'a'
    'aaaaaaa' -> 'a'
    'bc' -> 'bbcc'
    'bcc' -> 'bbc'
    'bbc' -> 'bcc'
    'bbcbcc' -> 'bccbbc'
    'kloo' -> 'kkllo'
    'ababbab' -> 'aabbaabaabb' (easier) or 'aabbaaabaaaabbb' (harder)
    """
    # easier option
    result = ""
    prev_char = ""
    for char in s:
        if char != prev_char:
            result += char * 2
        prev_char = char
    return result
    # harder option
    result = ""
    prev_char = ""
    repeat_count = 1
    for char in s:
        if char == prev_char:
            repeat_count += 1
        else:
            result += prev_char * repeat_count
            repeat_count = 1
        prev_char = char
    result += prev_char * repeat_count
    return result


print(invert_repetitions(""))  # ""
print(invert_repetitions("a"))   # aa
print(invert_repetitions("abc"))  # aabbcc
print(invert_repetitions("aabc"))  # aabbcc

class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Initialize car.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size

    def __repr__(self):
        """Repr."""
        return "Car make: " + self.make + ", color: " + self.color + ", engine size: " + str(self.engine_size)


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """
        Initialize service.

        Car service should also have a database to keep and track all cars standing in queue for repair.
        :param name: service name
        :param max_car_num: max car number service can take for repair at one time
        """
        self.name = name
        self.max_car_num = max_car_num
        self.cars_in_service = []

    def can_add_to_service_queue(self, car: Car) -> bool:
        """
        Check if it is possible to add car to service queue.

        Car can be added if:
        1. after adding new car, total car number in service does not exceed max_car_number (allowed car number in service)
        2. there is no car with the same color and make present in this service (yes, this world works this way).

        If car can be added, return True. Otherwise return False.
        """
        for c in self.cars_in_service:
            if c.make == car.make and c.color == car.color:
                return False
        if len(self.cars_in_service) < self.max_car_num:
            return True
        return False

    def add_car_to_service_queue(self, car: Car):
        """
        Add car to service if it is possible.

        The function does not return anything.
        """
        if self.can_add_to_service_queue(car):   # if True
            self.cars_in_service.append(car)

    def get_service_cars(self) -> list:
        """Get all cars is service."""
        return self.cars_in_service

    def repair(self) -> Car:
        """
        Repair car in service queue.

        Normally, the first car in queue is repaired.
        However, if there is a car in queue which color + make characters length is exactly 13 ->
        this car is chosen and is repaired (might be multiple suitable cars -> choose any).
        After the repair, car is no longer in queue (is removed).
        :return: chosen and repaired car
        """
        repaired_car = ""
        for car in self.cars_in_service:
            if len(car.make) + len(car.color) == 13:
                self.cars_in_service.remove(car)
                return car
        if len(self.cars_in_service) >= 1:
            repaired_car = self.cars_in_service[0]
            self.cars_in_service.remove(repaired_car)
        return repaired_car

    def get_the_car_with_the_biggest_engine(self) -> list:
        """
        Return a list of cars (car) with the biggest engine size.

        :return: car (cars) with the biggest engine size
        """
        biggest_engine = 0
        biggest_engine_cars = []
        for car in self.cars_in_service:
            if car.engine_size > biggest_engine:
                biggest_engine = car.engine_size
        for car in self.cars_in_service:
            if car.engine_size == biggest_engine:
                biggest_engine_cars.append(car)
        return biggest_engine_cars


if __name__ == "__main__":
    # Car service

    car1 = Car("blue", "honda", 1800)
    car2 = Car("blue", "honda", 1500)
    car3 = Car("yellow", "peugeot", 2000)
    car4 = Car("black", "lamborgini", 50000)
    car5 = Car("white", "toyota", 2500)
    whiteToyota = Car("purple", "toyotaChr", 2500)

    service = Service("autoLUX", 3)
    garazService = Service("Garaz u dadi Vasya", 1)

    print(service.can_add_to_service_queue(car1))
    print(service.can_add_to_service_queue(car2))
    print(service.can_add_to_service_queue(car3))
    service.add_car_to_service_queue(car1)
    service.add_car_to_service_queue(car4)
    service.add_car_to_service_queue(car3)
    print(service.get_the_car_with_the_biggest_engine())
    print("DADYA VASYA")
    print(garazService.can_add_to_service_queue(whiteToyota))
    print(str(garazService.get_service_cars()))
    garazService.repair()
    print(str(garazService.get_service_cars()))


class Species(Enum):
    """Different species."""

    Dragon = 1
    Vampire = 2
    Beast = 3


class Monster:
    """Monster class."""

    def __init__(self, species: Species, bounty: int):
        """Initialize monster."""
        self.species = species
        self.bounty = bounty
        self.is_dead = False

    def get_species(self) -> Species:
        """Return the species of the monster."""
        return self.species

    def get_bounty(self) -> int:
        """Return the bounty for this monster."""
        return self.bounty

    def is_alive(self) -> bool:
        """Whether the monster is alive."""
        return True

    def slay(self) -> bool:
        """
        Slay the monster.

        If monster is already dead, return False.
        Otherwise kill the monster and return True.
        """
        if self.is_dead:
            return False
        else:
            self.is_dead = True
            return True

    def __repr__(self) -> str:
        """
        Return string representation.

        "A {species} worth {bounty} coins"
        """
        return "A " + str(self.species.name) + " worth " + str(self.bounty) + " coins"


class Village:
    """
    Village class.

    Village starts with 100 money and 0 age.
    Each day population is lowered by 1 for each monster in the village.
    Population cannot be lower than 0.
    If the population is 0, witcher cannot work there.
    """

    def __init__(self, name: str, initial_population: int):
        """Initialize village."""
        self.name = name
        self.initial_population = initial_population
        self.monsters = []
        self.village_money = 100
        self.village_age = 0

    def get_name(self) -> str:
        """Return name of the village."""
        return self.name

    def get_population(self) -> int:
        """Return population of the village."""
        return self.initial_population

    def get_monsters(self) -> list:
        """
        Return a list of monsters bothering the village.

        If there are no population, no monsters are not bothering the village.
        """
        if self.initial_population == 0:
            return []
        else:
            return self.monsters

    def add_monster(self, monster: Monster) -> None:
        """Add monster to the village."""
        self.monsters.append(monster)

    def add_money(self, amount) -> None:
        """Add money to the village."""
        if amount > 0:
            self.village_money += amount

    def advance_day(self) -> None:
        """
        Advance time by one day.

        The age of the village is increased by one.
        """
        self.village_age += 1
        self.initial_population = max(0, self.initial_population - len(self.monsters))

    def pay(self, amount: int) -> bool:
        """
        Pay the required amount.

        If the village does not have enough money, return False.
        Otherwise spend the amount and return True.
        """
        if (amount > 0) and (self.village_money >= amount):
            self.village_money -= - amount
            return True
        return False

    def __repr__(self) -> str:
        """
        Return string representation of the village.

        "{name}, population {population}, age {age}"
        """
        return self.name + ", population " + str(self.initial_population) + ", age " + str(self.village_age)


class Witcher:
    """
    Witcher class.

    Witcher starts with 0 money.
    """

    def __init__(self, name: str, school: str):
        """Initialize witcher."""
        self.name = name
        self.school = school
        self.witcher_money = 0
        self.slain_monsters = []

    def get_money(self) -> int:
        """Return the amount of money the witcher has."""
        return self.witcher_money

    def get_slain(self) -> list:
        """Return a list of slain monsters in the order they are slain."""
        return self.slain_monsters

    def get_hunted_species(self) -> list:
        """
        Return a list of Species objects of the slain monsters ordered alphabetically.

        Each value should be in the list once, so there can be max 3 objects in the result.
        """
        if len(self.slain_monsters) == 0:
            return []
        hunted_species = []
        for monster in self.slain_monsters:
            hunted_species.append(monster.get_species())
        hunted_species_set = set(hunted_species)
        return sorted(hunted_species_set, key=lambda species: species.name)

    def hunt_most_expensive(self, village: Village) -> bool:
        """
        Hunt the most expensive monster.

        Try to hunt the most expensive monster (the one who has the highest bounty) in the given village.
        The monster is slain and then the village tries to pay the witcher.
        If there is a monster to kill and the village can pay the money, return True.
        Otherwise return False.
        The monster is slain even if there is no money to pay.
        """
        if village.monsters:
            most_expensive_monster = max(village.monsters, key=lambda monster: monster.bounty)
            if village.pay(most_expensive_monster.bounty):
                most_expensive_monster.slay()
                self.slain_monsters.append(most_expensive_monster)
                self.witcher_money += most_expensive_monster.bounty
                return True
            else:
                most_expensive_monster.slay()
                self.slain_monsters.append(most_expensive_monster)
        return False

    def __repr__(self) -> str:
        """
        Return string representation.

        "{name} of {school} school with {number of monsters} monsters slain"
        """
        return self.name + " of " + self.school + " school with " + str(len(self.slain_monsters)) + " monsters slain"


if __name__ == '__main__':
    # Witcher
    tallinn = Village("Tallinn", 7)
    godzilla_species = Species.Beast
    godzilla = Monster(godzilla_species, 200)
    dracula = Monster(Species.Vampire, 100)
    print("we will try to kill dracula")
    print(dracula.slay())
    print(dracula.slay())
    print(godzilla.get_species() == Species.Beast)  # True
    print(str(godzilla.get_species()))  # Species.Beast
    modzilla = Monster(Species.Dragon, 200)
    dracula = Monster(Species.Vampire, 100)
    frankenstein = Monster(Species.Beast, 300)
    tallinn.add_monster(godzilla)
    tallinn.add_monster(modzilla)
    tallinn.add_monster(dracula)
    tallinn.add_monster(frankenstein)

    print(tallinn.get_population())  # 7
    tallinn.advance_day()
    tallinn.add_money(500)
    print(tallinn.get_population())  # 3
    ago = Witcher("Ago", "TalTech")
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 300
    print(tallinn.get_monsters())  # [A Beast worth 200 coins, A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 500
    print(tallinn.get_monsters())  # [A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # False
    print(ago.get_money())  # 500
    print(ago.hunt_most_expensive(tallinn))  # True
    print(tallinn.get_monsters())  # []

    print(ago.get_hunted_species())  # [<Species.Beast: 3>, <Species.Dragon: 1>, <Species.Vampire: 2>]
    print(ago.get_hunted_species()[0] == Species.Beast)  # True

    # enum examples
    species_list = [Species.Beast, Species.Vampire, Species.Beast]
    print(species_list[0] == species_list[1])  # False
    print(species_list[0] == species_list[2])  # True
