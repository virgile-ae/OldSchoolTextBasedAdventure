from beings import Hero
from dataclasses import dataclass


__file_name = "history.txt"


@dataclass
class HeroData:
    """Contains all relevant data for the entry of a hero in the history of the game."""
    name: str
    max_health: int
    attack: int
    kills: int
    gold: int

    def __str__(self) -> str:
        return f"{self.name} {self.max_health} {self.attack} {self.kills} {self.gold}"

    def __repr__(self) -> str:
        return f"{self.name} - health: {self.max_health}, attack: {self.attack}, kills: {self.kills} , gold: {self.gold}"


def _hero_data_from_hero(h: Hero):
    """Creates a 'HeroData' object from a 'Hero' object."""
    return HeroData(h.name, h.max_health, h.attack, h.kills, h.gold)


def _parse_hero_data(s: str) -> HeroData:
    """Parses a string into a 'HeroData' object."""
    data = s.split()
    return HeroData(data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]))


def read_history() -> list[HeroData]:
    """Reads all hero entries in the history of the game and returns them."""
    with open(__file_name, 'r') as file:
        heroes = [_parse_hero_data(i) for i in file.readlines()]
        file.close()
        return heroes


def write_history(h: Hero) -> None:
    """Updates the history of the game with a new entry."""
    heroes = [*read_history(), _hero_data_from_hero(h)]
    string = ''.join(str(i) for i in heroes)
    with open(__file_name, 'w') as file:
        file.write(string)
        file.close()
