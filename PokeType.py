from enum import Enum

class PokemonType(Enum):
    AQUA = 0
    FIRE = 1
    GRASS = 2

    def __eq__(self, other):
        return True if self.pokemon_name == other.pokemon_name else False

    def __ne__(self, other):
        return True if self.pokemon_name != other.pokemon_name else False

    def __lt__(self, other):
        if self.pokemon_name == other.pokemon_name:
            return False
        elif self.pokemon_name == "GRASS" and other.pokemon_name == "FIRE":
            return True
        elif self.pokemon_name == "GRASS" and other.pokemon_name == "AQUA":
            return False
        elif self.pokemon_name == "AQUA" and other.pokemon_name == "GRASS":
            return True
        elif self.pokemon_name == "AQUA" and other.pokemon_name == "FIRE":
            return False
        elif self.pokemon_name == "FIRE" and other.pokemon_name == "AQUA":
            return True
        elif self.pokemon_name == "FIRE" and other.pokemon_name == "GRASS":
            return True

    def __gt__(self, other):
        return not self.__lt__(other)

    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", "-1": "tie"}

        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1]  # grass
        ]

        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


