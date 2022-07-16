from dataclasses import dataclass
from beings import MonsterStrength, Monster

LAND = ' '
ROAD = 'R'
FOREST = 'F'


@dataclass
class Coord:
    x: int
    y: int


monsters = [
    Monster(MonsterStrength.BASIC,        Coord(3, 4), 'Ξ'),
    Monster(MonsterStrength.BASIC,        Coord(3, 4), 'Ψ'),
    Monster(MonsterStrength.INTERMEDIATE, Coord(3, 4), 'Π'),
    Monster(MonsterStrength.INTERMEDIATE, Coord(3, 4), 'Ξ'),
    Monster(MonsterStrength.DIFFICULT,    Coord(3, 4), 'Ξ'),
    Monster(MonsterStrength.DIFFICULT,    Coord(3, 4), 'Ξ'),
    Monster(MonsterStrength.ADVANCED,     Coord(3, 4), 'Ξ'),
    Monster(MonsterStrength.FINAL,        Coord(3, 4), 'Ξ'),
]


class GameMap:
    def __init__(self) -> None:
        width = 100
        self.playerChar = "Ο"
        self.monsters = "ΞΨΠΔΘΣΦΩ"
        self.value = [
            "$$$─╮▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
            "    ├──$$$──╮▒▒▒▒▒▒▒▒▒",
            "│   │       ├───────╮▒",
            "│ Ξ │ Δ │ Θ │       │▒",
            "│   │   │   │ Φ │   │▒",
            "│   │   │   │   │ Ω │▒",
            "│   │ Π │ Σ │   │   │▒",
            "│ Ψ │   │       ├─F─╯▒",
            "│       ├──$$$──╯▒▒▒▒▒",
            "╰──$$$──╯▒▒▒▒▒▒▒▒▒▒▒▒▒",
        ]
        self.width = width

    def __str__(self) -> str:
        return '\n'.join(self.value)

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, i: int) -> list[int]:
        return self.value[i]


if __name__ == '__main__':
    print(GameMap())
