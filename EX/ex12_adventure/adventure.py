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
        """This is string.."""
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
        """This is string."""
        return self.name + " of type " + self.type + ", Power: " + str(self.power) + "."


class World:
    """Game logic hides here."""

    def __init__(self, python_master: str):
        """Python master is a friend."""
        self.python_master = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []

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
        """Somethingю"""
        if isinstance(mons, Monster):
            self.graveyard.append(mons)
        if isinstance(adv, Adventurer):
            self.graveyard.append(adv)


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
    smart_cheater = Adventurer("T00ts", "Wizard", 40, 157)
    print(smart_cheater)

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
    print("Toots, some more expa for u!!!")
    another_friend.add_experience(100)
    print(another_friend)
    print()
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

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
    world.add_monster(zombie)
    world.add_monster(goblin_archer)
    print(world.get_monster_list())

    """
    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()

    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
    """
