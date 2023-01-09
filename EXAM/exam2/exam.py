
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
