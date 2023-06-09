"""Exam4 (2023-01-13)."""
import re
import string
from operator import attrgetter


def find_names_from_text(text: str) -> list:
    """
    Return list of names from the text.

    In the text, words are separated by single space.
    A word which starts with a capital letter is considered a name.
    Put all the words in to the result list.
    The text contains only latin letters (a-z, A-Z) and spaces.

    The names in the result should appear in the same order as in the input text.

    find_names_from_text("hello World")  => ["World"]
    find_names_from_text("hello World and John Smith")  => ["World", "John", "Smith"]
    find_names_from_text("hello world")  => []
    find_names_from_text("")  => []
    find_names_from_text("Exam")  => ["Exam"]
    find_names_from_text("YES")  => ["YES"]
    """
    names_list = []
    if len(text) == 0:
        return []

    words_list = text.split(" ")
    for word in words_list:
        if word[0] == word[0].upper():
             names_list.append(word)
    return names_list


"""print(find_names_from_text('AAAddddd BBB CC'))   #   =>
print(find_names_from_text("hello World and John Smith"))    #  => ["World", "John", "Smith"]
print(find_names_from_text("hello world"))   #  => []
print(find_names_from_text(""))    # => []
print(find_names_from_text("CrjSTYZvSTyRsKPfLqh RLrRsFSQEysEjYm ZGepflEvpXmRKGI"))     # => ["Exam"]
print(find_names_from_text("YES"))     # => ["YES"]"""


def growing_triplets(numbers: list) -> list:
    """
    Add elements where the previous value is lower and the next value is larger into a new list.

    Function has to create a new list, where the middle value of three consecutive numbers are added
    if the three numbers are growing in value (the first number is smaller than the second number and
    the third number is larger than the second number).

    growing_triplets([1, 2, 3]) => [2]
    growing_triplets([1, 2, 3, 4]) => [2, 3]
    growing_triplets([1, 5, 3, 4]) => []
    growing_triplets([1, 2]) => []
    growing_triplets([]) => []
    :param numbers:
    :return:
    """
    return_list = []
    if len(numbers) < 3:
        return []
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] < numbers[i + 1]:
            return_list.append(numbers[i])
    return return_list


print(growing_triplets([1, 2, 3]))    # => [2]
print(growing_triplets([1, 2, 3, 4]))   # => [2, 3]
print(growing_triplets([1, 2, 3, 4, 5, 6, 4]))   # => [2, 3, 4, 5]
print(growing_triplets([1, 2]))     # => []
print(growing_triplets([]))   # => []


def encode_string_with_hex_key(input_str: str, key: str) -> str:
    """
    Encode string using key.

    :param input_str - string to encode. Non-alphabetic characters are left as is.
    Caps are encoded into caps.
    :param key - hex key in which n-th number tells how much should n-th char in input_str be shifted.
    Works as round buffer, eg. if z is reached start from a again.
    The input_str and key are always the same length.

    Alphabet: abcdefghijklmnopqrstuvwxyz
    Upper case: ABCDEFGHIJKLMNOPQRSTUVWXYZ

    encode_string_with_hex_key("a", "1") -> "b"
    encode_string_with_hex_key("z", "1") -> "a"
    encode_string_with_hex_key("abc", "101") -> "bbd"
    encode_string_with_hex_key("Abc", "101") -> "Bbd"
    encode_string_with_hex_key("z.z.z", "fffff") -> "o.o.o"

    :return Encoded string
    """
    alphabet = string.ascii_lowercase
    result = ""
    for i, c in enumerate(input_str):
        if c in string.ascii_letters:
            shift = key[i]
            if shift.isdigit():
                shift_nr = int(shift)
            else:
                shift_nr = 10 + alphabet.index(shift)
            current_pos = alphabet.index(c)
            new_pos = current_pos + shift_nr

            if new_pos >= len(alphabet):
                new_pos = new_pos - len(alphabet)
            result += alphabet[new_pos]
        else:
            result += c
    return result


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to find all the multipliers of two given numbers within the limit.
    Then, find the sum of those multipliers where duplicates are removed.

    All the numbers are positive integers.

    sum_of_multipliers(3, 5, 20) => 98
    We get: [3, 6, 9, 12, 15, 18] (21 is over the limit)
    and [5, 10, 15, 20]
    15 is in both lists, we only use it once, sum is 98

    sum_of_multipliers(3, 3, 20) => 63
    sum_of_multipliers(3, 1, 20) => 210

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    result = 0
    mult_list = []
    for i in range(first_num, limit + 1, first_num):
        mult_list.append(i)
    for u in range(second_num, limit + 1, second_num):
        mult_list.append(u)
    print(sorted(mult_list))
    print(set(mult_list))
    for i in set(mult_list):
        result += i
    return result

print(sum_of_multipliers(3, 3, 20))  #  => 63
print(sum_of_multipliers(3, 1, 20))   # => 210


def count_the_dumplings(day: int) -> int:
    """
    Count the dumplings.

    You are the production engineer of new dumpling factory.
    Each day the factory has to double it's dumpling production.
    Your manager asked you how many dumplings are we making on day X.
    As a lazy software engineer you decided to write a recursive program to count it.
    This function CANNOT contain any while/for loops.
    NB: The factory started working on day one and before that it made 0 dumplings.
    count_the_dumplings(0) => 0
    count_the_dumplings(1) => 1
    count_the_dumplings(2) => 2
    count_the_dumplings(3) => 4
    count_the_dumplings(30) ==> 536870912
    """
    if day <= 0:
        return 0
    if day == 1:
        return 1
    return 2 * count_the_dumplings(day - 1)


print(count_the_dumplings(30))    # ==> 536870912)


def prime_factorization(number: int) -> int:
    """
    Return the prime factorization of the number.

    Return dict, where the key is a prime factor and the value is count of this factor.

    12 = 2 * 2 * 3 => {2: 2, 3:1}
    1960 = 2 * 2 * 2 * 5 * 7 * 7 => {2: 3, 5: 1, 7: 2}
    79 = 71 * 1 => {79: 1}

    Prime number is a number which is divisible only by 1 and the number itself.
    For example 2, 3, 5, 7, 11, 13, 17, 19, 23 are prime numbers.

    Examples:
    2 => { 2: 1 }
    12 => { 2: 2, 3: 1 }
    1960 => { 2: 3, 5: 1, 7: 2 }
    1024 => { 2: 10 }
    79 => { 79: 1 }
    121 => { 11: 2 }

    :param number: a number greater than 1
    :return: dict of prime factors and their counts.
    """
    factors = {}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors[i] = 0
            while number % i == 0:
                factors[i] += 1
                number = number // i
    if number > 1:
        factors[number] = 1
    return factors

class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Initialize book.

        Each book has title, author and price.
        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        """Repr."""
        return "Book: " + self.title + " Author: " + self.author + " with price: " + str(self.price) + " rating: " + str(self.rating)


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Initialize store.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.book_storage = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        for b in self.book_storage:
            if b.author == book.author and b.title == book.title:
                return False
        if book.rating >= self.rating:
            return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.book_storage.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if book in self.book_storage:
            return True
        return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.book_storage.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.book_storage

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        sorted_by_price = sorted(self.book_storage, key=lambda book: book.price)
        return sorted_by_price

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        books_with_highest_rating = []
        highest_rating = 0
        for book in self.book_storage:
            if book.rating > highest_rating:
                highest_rating = book.rating
        for book in self.book_storage:
            if book.rating == highest_rating:
                books_with_highest_rating.append(book)
        return books_with_highest_rating


class Accessory:
    """Accessory."""

    def __init__(self, name: str, value: int):
        """Initialize accessory."""
        self.name = name
        self.value = value

    def __repr__(self):
        """
        Return string representation of accessory.

        Returns string in form "{name}, value : {value}."
        """
        return self.name + ", value : " + str(self.value) + "."


class Car:
    """Car."""

    def __init__(self, name: str, color: str):
        """Initialize car."""
        self.name = name
        self.color = color
        self.accessory_list = []
        self.premium = False
        self.fuel = 100

    def add_accessory(self, accessory: Accessory):
        """Add accessory to the car."""
        self.accessory_list.append(accessory)

    def get_value(self) -> int:
        """
        Get the value of the car.

        Regular car base price is 9500, for premium car its 42 500.
        All the values of accessories are summed up.
        """
        return len(self.accessory_list)

    def get_fuel_left(self):
        """Return how much fuel is left in percentage."""
        return self.fuel

    def get_accessories_by_value(self):
        """Return accessories sorted by value (descending i.e. higher to lower)."""
        return_list = sorted(self.accessory_list, key=lambda ac: ac.value, reverse=True)
        return return_list

    def __repr__(self):
        """
        Return string representation of the car.

        Should return "This {color} {name} contains {accessory_amount} accessories and has {fuel}% fuel left."
        """
        return "This " + self.color + self.name + " contains " + str(self.get_value()) + " accessories and has " + str(self.fuel) + "% fuel left."


class Customer:
    """Customer."""

    def __init__(self, name: str, wish: str):
        """
        Initialize customer.

        The wish consists of two words.
        The first word is either "Cheap" or "Expensive".
        In case of "Cheap", the customer wants to get the car with the lowest value.
        In case of "Expensive", the customer wants to get the car with the highest value.
        The second word is the color. Customer does not want a car with another color.
        For premium customer a car with the given color is searched for from the premium cars.
        If there is no such car with the wished color, the cheapest car is taken from the premium cars.

        For example: "Cheap Red", "Expensive Yellow".
        """
        self.name = name
        self.wish = wish
        self.garage = []

    def get_garage(self):
        """
        Return all the cars of the customer sorted by the value (ascending i.e. from lower to higher).

        Both regular and premium cars are kept in garage.
        """
        return sorted(self.garage, key=lambda value: len(self.garage))

    def make_premium(self):
        """Make customer a premium customer, premium cars can be sold to the customer now."""
        pass

    def drive_with_car(self, driving_style: str):
        """
        Go for a drive.

        A car with the highest fuel percentage should be taken.
        If several cars have the same percentage, use the most expensive one.

        If the driving_style is "Rally", the customer takes the cheapest car instead.
        Regular driving takes 15 percentage points of fuel, "Rally" takes 35 percentage points (85% - 35% => 50%).
        If the fuel gets to zero during the drive, the car is left behind (it is no longer part of garage).
        """
        pass


class Dealership:
    """Dealership."""

    def __init__(self, name: str):
        """Initialize dealership."""
        self.name = name
        self.storage = []

    def add_car(self, car: Car):
        """Add car to the dealership."""
        self.storage.append(car)

    def get_all_regular_cars(self):
        """Return all the regular cars sorted by value (ascending, lower to higher)."""
        pass

    def make_car_premium(self, car: Car):
        """Make a car premium, which can can be sold only to premium customers."""
        pass

    def get_all_premium_cars(self):
        """Return all the premium cars sorted by value (ascending, lower to higher)."""
        pass

    def sell_car_to_customer(self, customer: Customer):
        """
        Sell a car to customer depending on his/her wishes.

        After selling, the car is removed from the dealership and moved into customer's garage.
        In the given exercise, there is always a matching car.
        """
        pass


if __name__ == '__main__':
    """
    assert find_names_from_text("hello World and John Smith") == ["World", "John", "Smith"]
    assert find_names_from_text("hello world") == []
    assert find_names_from_text("") == []
    assert find_names_from_text("Exam") == ["Exam"]
    assert find_names_from_text("YES") == ["YES"]

    assert growing_triplets([1, 2, 3]) == [2]
    assert growing_triplets([1, 2, 3, 4]) == [2, 3]
    assert growing_triplets([1, 5, 3, 4]) == []
    assert growing_triplets([1, 2]) == []
    assert growing_triplets([]) == []

    assert encode_string_with_hex_key("a", "1") == "b"
    assert encode_string_with_hex_key("z", "1") == "a"
    assert encode_string_with_hex_key("abc", "101") == "bbd"
    assert encode_string_with_hex_key("z.z.z", "fffff") == "o.o.o"

    assert sum_of_multipliers(3, 3, 20) == 63
    assert sum_of_multipliers(3, 1, 20) == 210

    assert count_the_dumplings(3) == 4
    assert count_the_dumplings(0) == 0
    assert count_the_dumplings(30) == 536870912

    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(1960) == {2: 3, 5: 1, 7: 2}"""

    # Book store
    print("BOOK STORE")
    store = Store("Apollo", 98.9)
    book = Book("War & Peace", "Leo Tolstoy", 10.5, 99)

    print(store.can_add_book(book))  # True

    store.add_book(book)
    print(store.get_all_books())  # [book]

    book2 = Book("War & Peace", "Leo Tolstoy", 10.5, 99)
    assert store.can_add_book(book2) is False  # cannot add book with the same title and author

    book3 = Book("War", "Leo Tolstoy", 10.5, 80)
    assert store.can_add_book(book3) is False  # cannot add book since its rating is too low
    print(store.get_most_popular_book())

    # dealership

    blue_car = Car("Audi R4", "blue")
    green_car = Car("Ford", "green")
    wheel = Accessory("Sport wheel", 100)
    blue_car.add_accessory(wheel)
    car_dealer = Dealership("Ago Carfriend")
    car_dealer.add_car(blue_car)
    car_dealer.add_car(green_car)

    print(car_dealer.get_all_regular_cars())
    # [This green Ford contains 0 accessories and has 100% fuel left.,
    # This blue Audi R4 contains 1 accessories and has 100% fuel left.]
    print(car_dealer.get_all_premium_cars())  # []

    customer = Customer("Ago", "Cheap green")
    car_dealer.sell_car_to_customer(customer)
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 100% fuel left.]
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 65% fuel left.]
    customer.drive_with_car("Rally")
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # []]

    car_dealer.make_car_premium(blue_car)
    print(car_dealer.get_all_premium_cars())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]

    customer_premium = Customer("Ago", "Expensive black")
    customer_premium.make_premium()
    car_dealer.sell_car_to_customer(customer_premium)
    print(customer_premium.get_garage())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]
