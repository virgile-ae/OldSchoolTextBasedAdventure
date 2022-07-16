from beings import Hero, Monster
from random import getrandbits


def fight_monster(h: Hero, monster: Monster) -> list[Hero]:
    """
    Simulates a fight between the hero and a monster of random strength.
    """
    continue_fighting = True
    while continue_fighting:
        if bool(getrandbits(1)):  # random boolean to see who goes first
            m = monster.take_damage(h.do_damage())
            if len(m) == 0:
                h.gold += monster.gold
                return [h]
            monster = m[0]
            hs = h.take_damage(monster.do_damage())
            if len(hs) == 0:
                return []
            h = hs[0]
        else:
            hs = h.take_damage(monster.do_damage())
            if len(hs) == 0:
                return []
            h = hs[0]
            m = monster.take_damage(h.do_damage())
            if len(m) == 0:
                h.gold += monster.gold
                return [h]
            monster = m[0]
