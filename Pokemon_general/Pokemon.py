from __future__ import annotations
from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        self.pokemon_name = pokemon_name
        self.pokemon_id = pokemon_id
        self.current_hp = current_hp
        self.max_hp = max_hp

        # additional info about pokemon
        self.primary_type = None
        self.alive = True
        self.experience_points = 0
        self.fight_status = False
        self.curr_lv_bond = None
        self.max_bond = None

    def level_up(self) -> Pokemon:
        pass

    def __str__(self):
        return f"{self.pokemon_name.capitalize()}:\n\n  * Pokemon type: {str(self.primary_type)[12:].lower()}\n  * HP: {self.current_hp}/{self.max_hp}\n"

    def feed(self):
        if self.current_hp < self.max_hp:
            self.current_hp += 5
            print(f"{self.pokemon_name.capitalize()} has now {self.current_hp} HP.")
        else:
            print(f"{self.pokemon_name} is full.")

    def battle(self, other):
        print(f"Battle: {self.pokemon_name} VS {other.pokemon_name}.")

        result = self.typewheel(str(self.primary_type)[12:].lower(), str(other.primary_type)[12:].lower())
        print(f"{self.pokemon_name.capitalize()} fought {other.pokemon_name.capitalize()} and the result is a {result}.")
        # call typewheel()

        # depending on the result, have effects
        if result == "lose":
            self.current_hp -= 20
            print(f"{self.pokemon_name} lost and now has {self.current_hp} HP.")
        elif result == "win":
            self.current_hp += 5

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", "-1": "tie"}

        # mapping between types and result conditions
        game_map = {"aqua": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1]  # grass
        ]

        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]
      
