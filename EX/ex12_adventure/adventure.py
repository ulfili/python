"""Dungeons and Pythons."""


class Adventurer:
    """Gamers."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Player information."""
        self.name = name
        type_list = ["Fighter", "Druid", "Wizard", "Paladin"]
        if class_type in type_list:
            self.class_type = class_type
        else:
            self.class_type = "Fighter"
        if power > 99:
            self.power = 10
        else:
            self.power = power
        self.experience = experience

    def __repr__(self):
        """Something."""
        return self.name + ", the " + self.class_type + ", Power: " + str(self.power) + ", Experience: " + str(self.experience) + "."

    def add_power(self, power: int):
        """Power add."""
        self.power += power
        return power

    def add_experience(self, exp: int):
        """Adding experience."""
        if exp >= 0:
            self.experience += exp
            if self.experience > 99:
                more_power = self.experience / 10
                self.power += int(more_power)
                self.experience = 0
        return exp


class Monster:
    """Adventurer opponent."""

    def __init__(self, name: str, type: str, power: int):
        """Monsters information."""
        self.name = name
        if type == "Zombie":
            self.name = self.zombie_name
        self.type = type
        self.power = power

    @property
    def zombie_name(self) -> str:
        """Undead + name."""
        return "Undead " + str(self.name)

    def __repr__(self):
        """Something."""
        return self.name + " of type " + self.type + ", Power: " + str(self.power) + "."


class World:
    """Game logic hides here."""

    def __init__(self, python_master: str):
        """Python master is a friend."""
        self.python_master = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []
        self.active_adventurers = []
        self.active_monsters = []
        self.necromancers = False

    def get_python_master(self):
        """Get python master."""
        return self.python_master

    def get_adventurer_list(self) -> list:
        """Adventurer list."""
        return self.adventurer_list

    def get_monster_list(self) -> list:
        """Monster list."""
        return self.monster_list

    def add_adventurer(self, name: Adventurer):
        """Adding adventurers into list."""
        if isinstance(name, Adventurer):
            self.adventurer_list.append(name)

    def add_monster(self, name: Monster):
        """Adding monsters into list."""
        if isinstance(name, Monster):
            self.monster_list.append(name)

    def get_graveyard(self):
        """Graveyard."""
        return self.graveyard

    def add(self, mons: Monster, adv: Adventurer):
        """Something."""
        if isinstance(mons, Monster):
            self.graveyard.append(mons)
        if isinstance(adv, Adventurer):
            self.graveyard.append(adv)

    def remove_character(self, name):
        """Something."""
        for person in self.adventurer_list:
            if person.name == name:
                self.graveyard.append(person)
                return self.adventurer_list.remove(person)
        for person in self.monster_list:
            if person.name == name:
                self.graveyard.append(person)
                return self.monster_list.remove(person)
        for person in self.graveyard:
            if person.name == name:
                return self.graveyard.remove(person)

    def necromancers_active(self, necromancers: bool):
        """We are gonna check if players are alive."""
        self.necromancers = necromancers

    def revive_graveyard(self):
        """Use this function if graveyard is not empty."""
        if not self.necromancers:
            return
        for creature in self.graveyard:
            if isinstance(creature, Monster):
                creature.type = "Zombie"
                self.monster_list.append(creature)
            if isinstance(creature, Adventurer):
                new_monster_name = "Undead " + creature.name
                new_monster_type = "Zombie " + creature.class_type
                new_monster_power = creature.power
                undead_person = Monster(new_monster_name, new_monster_type, new_monster_power)
                self.monster_list.append(undead_person)
        self.necromancers = False
        self.graveyard.clear()

    def get_active_adventurers(self):
        """Sorting pers."""
        return sorted(self.active_adventurers, key=lambda exp: exp.experience, reverse=True)

    def add_strongest_adventurer(self, class_type: str):
        """Adding pers by most power."""
        max_power = 0
        for person in self.adventurer_list:
            if person.class_type == class_type:
                # print("We found adventurer with type: ", class_type)
                if person.power > max_power:
                    max_power = person.power
        for person in self.adventurer_list:
            if (person.power == max_power) and (person.class_type == class_type):
                self.active_adventurers.append(person)
                # print("We move adventurer: ", person.name, " from one list to another.")
                self.adventurer_list.remove(person)
                return

    def add_weakest_adventurer(self, class_type: str):
        """Adding pers by least power."""
        min_power = 5000
        for person in self.adventurer_list:
            if person.class_type == class_type:
                if person.power < min_power:
                    min_power = person.power
        for person in self.adventurer_list:
            if (person.power == min_power) and (person.class_type == class_type):
                self.active_adventurers.append(person)
                self.adventurer_list.remove(person)
                return

    def add_most_experienced_adventurer(self, class_type: str):
        """Adding pers by most exp."""
        max_exp = 0
        for person in self.adventurer_list:
            if person.class_type == class_type:
                if person.experience > max_exp:
                    max_exp = person.experience
        for person in self.adventurer_list:
            if (person.experience == max_exp) and (person.class_type == class_type):
                self.active_adventurers.append(person)
                self.adventurer_list.remove(person)
                return

    def add_least_experienced_adventurer(self, class_type: str):
        """Adding pers by least exp."""
        min_exp = 5000
        for person in self.adventurer_list:
            if person.class_type == class_type:
                if person.experience < min_exp:
                    min_exp = person.experience
        for person in self.adventurer_list:
            if (person.experience == min_exp) and (person.class_type == class_type):
                self.active_adventurers.append(person)
                self.adventurer_list.remove(person)
                return

    def add_adventurer_by_name(self, name: str):
        """Adding pers by name."""
        for person in self.adventurer_list:
            if person.name == name:
                self.active_adventurers.append(person)
                self.adventurer_list.remove(person)
                return

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Adding persons by type."""
        remove_elements = []
        for person in self.adventurer_list:
            if person.class_type == class_type:
                self.active_adventurers.append(person)
                remove_elements.append(person)
        for person in remove_elements:
            self.adventurer_list.remove(person)
        return

    def add_all_adventurers(self):
        """Adding all persons."""
        remove_elements = []
        for person in self.adventurer_list:
            self.active_adventurers.append(person)
            remove_elements.append(person)
        for person in remove_elements:
            self.adventurer_list.remove(person)
        return

    def get_active_monsters(self):
        """Sorting active monsters."""
        return sorted(self.active_monsters, key=lambda pow: pow.power, reverse=True)

    def add_monster_by_name(self, name: str):
        """Adding persons by name."""
        for person in self.monster_list:
            if person.name == name:
                self.active_monsters.append(person)
                self.monster_list.remove(person)
                return

    def add_strongest_monster(self):
        """Adding by most power."""
        if len(self.monster_list) == 0:
            return
        sorted_list = sorted(self.monster_list, key=lambda pow: pow.power, reverse=True)
        self.active_monsters.append(sorted_list[0])
        self.monster_list.remove(sorted_list[0])

    def add_weakest_monster(self):
        """Adding by least power."""
        if len(self.monster_list) == 0:
            return
        sorted_list = sorted(self.monster_list, key=lambda pow: pow.power)
        self.active_monsters.append(sorted_list[0])
        self.monster_list.remove(sorted_list[0])

    def add_all_monsters_of_type(self, type: str):
        """Adding by type."""
        remove_list = []
        for person in self.monster_list:
            if person.type == type:
                self.active_monsters.append(person)
                remove_list.append(person)
        for person in remove_list:
            self.monster_list.remove(person)
        return

    def add_all_monsters(self):
        """Adding all."""
        remove_list = []
        for person in self.monster_list:
            self.active_monsters.append(person)
            remove_list.append(person)
        for person in remove_list:
            self.monster_list.remove(person)
        return


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    # world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    # world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
