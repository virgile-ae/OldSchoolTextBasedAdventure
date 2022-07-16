from random import randint
from enum import Enum

from map import Coord


class PurchaseType(Enum):
    """Represents a type of purchase that the hero will make at a shop."""
    REPLENISH_HEALTH = 1
    INCREASE_MAX_HEALTH = 2
    INCREASE_ATTACK = 3


class Hero:
    """
    Represents a hero in the game.

    Properties
    ----------
    name       : str
        the name of the hero.
    health     : int
        the amount of health of the hero.
    max_health : int
        the maximum amount of health the hero can have.
    attack     : int
        the attack stat of the hero.
    lives      : int
        the number of remaining lives the hero has.
    kills      : int
        the number of monsters the hero has killed.
    gold       : int
        the amount of gold the hero owns.
    """

    __gold_cost = 10

    def __init__(self, name="", health=100, max_health=100, attack=10, lives=3, kills=0, gold=0) -> None:
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.lives = lives
        self.kills = kills
        self.gold = gold

    def __str__(self) -> str:
        """
        String representation of a 'Hero' object.

        Example use
        -----------
        >>> str(Hero())
        " 100 10 0 0"
        >>> str(Hero("jeff", 100, 120, 12, 2, 14, 103))
        "jeff 120 12 14 103"
        """
        return f"{self.name} {self.max_health} {self.attack} {self.kills} {self.gold}"

    def __repr__(self) -> str:
        return str(self)

    def is_alive(self) -> bool:
        """
        Checks if the hero is alive. Used during battle.

        Example use
        -----------
        >>> Hero(health=0).is_alive()
        False
        >>> Hero().is_alive()
        True
        """
        return self.health > 0

    def make_purchase(self, type: PurchaseType) -> list:
        """
        To be used when the hero is at a shop. All purchases cost 10 gold.
        An empty list represents the failure of the purchase.
        A list with one element contains the new Hero object.

        Example use
        -----------
        >>> Hero(health=10, gold=10).make_purchase(PurchaseType.REPLENISH_HEALTH)[0].health
        100
        >>> Hero().make_purchase(PurchaseType.REPLENISH_HEALTH)
        []
        """
        if self.gold < self.__gold_cost:  # Cost of purchase
            return []  # Represents failure
        self.gold -= self.__gold_cost

        if type == PurchaseType.REPLENISH_HEALTH:
            return [self.replenish_health()]
        elif type == PurchaseType.INCREASE_MAX_HEALTH:
            return [self.increase_max_health()]
        else:  # PurchaseType.INCREASE_ATTACK
            return [self.increase_attack()]

    def replenish_health(self):
        """
        Increases the hero's 'health' property to 'max_health'.

        Example use
        -----------
        >>> Hero(health=5).replenish_health().health
        100
        >>> Hero(health=5, max_health=120).replenish_health().health
        120
        """
        n = self
        n.health = n.max_health
        return n

    def increase_max_health(self):
        """
        Increases the hero's 'max_health' property by 20%.

        Example use
        -----------
        >>> Hero().increase_max_health().max_health
        120
        >>> Hero(max_health=200).increase_max_health().max_health
        240
        """
        n = self
        n.max_health += n.max_health // 5
        return n

    def increase_attack(self):
        """
        Increases the hero's 'attack' property by 20%.

        Example use
        -----------
        >>> Hero().increase_attack().attack
        12
        >>> Hero(attack=100).increase_attack().attack
        120
        """
        n = self
        n.attack += n.attack // 5
        return n

    def take_damage(self, damage: int):
        """
        Decreases the hero's health property by 'damage'.
        If the hero's health property goes at or below 0, its lives property gets decremented.
        If the lives property goes to 0, an empty list is returned.
        Otherwise, a list with the new hero is returned.

        Example use
        -----------
        >>> Hero().take_damage(21)[0].health
        79
        >>> Hero(lives=2).take_damage(105)[0].lives
        1
        >>> Hero(lives=1).take_damage(105)
        []
        """
        diff = self.health - damage
        if diff < 1:
            if self.lives == 1:
                return []
            n = self
            n.lives -= 1
            return [n]
        n = self
        n.health = diff
        return [n]

    def do_damage(self) -> int:
        """
        Returns a random integer which represents damage done to the monster.
        The random integer is calculated using a random number and the attack property.

        (No doctests due to random int)
        """
        return int(self.attack * float(f'1.{randint(0, 25)}'))

    def final_score(self) -> None:
        """Will eventually calculate score based on TIME, GOLD, HEALTH"""
        pass


class MonsterStrength(Enum):
    BASIC = 0
    INTERMEDIATE = 1
    DIFFICULT = 2
    ADVANCED = 3
    FINAL = 4


class Monster:
    """
    Represents a monster in the game.

    Properties
    ----------
    health : int
        the amount of health of the monster.
    attack : int
        the attack stat of the monster.
    gold   : int
        the amount of gold the monster deposits when it is killed.
    """

    def __init__(self, level: MonsterStrength, coords: Coord, char: str) -> None:
        self.attack = 6 + level
        self.char = char
        self.coords = coords
        self.gold = 10 + 2 * level
        self.health = 65 + 5 * level

    def do_damage(self) -> int:
        return int(self.attack * float(f'1.{randint(0, 25)}'))

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> list:
        diff = self.health - damage
        if diff < 1:
            return []
        self.health = diff
        return [self]


if __name__ == '__main__':
    from doctest import testmod
    testmod()
