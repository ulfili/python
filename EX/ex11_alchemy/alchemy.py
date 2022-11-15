"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Alchemical element name."""
        self.name = name

    def __repr__(self):
        """Element is name."""
        return "<AE: " + self.name + ">"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.storage = []

    def __repr__(self):
        """Storage content."""
        return "alchemical storage content is: " + str(self.storage)

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.storage.append(element)
        else:
            raise TypeError

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        index = -1    # et aru saada millal elementi ei ole
        i = 0         # elemendi loetelu algab nullist
        for element in self.storage:
            # print("element is: " + str(element))
            if element.name == element_name:
                index = i  # kui element on leitud, siis me salvestame indeksi numbri
                # print("element presents in our storage! " + str(element))
            i = i + 1    # iga elemendi indeks, salvestab viimase
        # print("index is :" + str(index))
        if index == -1:
            return None
        return self.storage.pop(index)

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        return_list = self.storage
        self.storage = []
        return return_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        elem_dict = {}
        content = "Content:"
        for element in self.storage:
            if element.name not in elem_dict:
                elem_dict[element.name] = 0
            if element.name in elem_dict:
                elem_dict[element.name] += 1
        # print("elem dict is: " + str(elem_dict))
        for elem, num in sorted(elem_dict.items()):
            content += "\n" + " * " + elem + " x " + str(num)
        if len(elem_dict) == 0:
            content += "\n" + " Empty."
        return content


if __name__ == '__main__':
    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_six = AlchemicalElement('Earth')
    element_three = AlchemicalElement('Water')
    element_four = AlchemicalElement('Air')
    element_seven = AlchemicalElement('Air')
    storage = AlchemicalStorage()
    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>
    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_six)
    storage.add(element_three)
    storage.add(element_four)
    print(storage)
    print(storage.pop("WATRE"))
    print(storage)
    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage)
    print(storage.get_content())
    # Content:
    #  * Fire x 1
    #  * Water x 1
    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage.get_content())
    # Content:
    #  Empty
    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)
    print(storage.pop('Water') == element_three)  # True
    print(storage.pop('Water') == element_two)  # True
