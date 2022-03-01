from Pokemon_general.Pokemon import Pokemon
from Pokemon_general.PokemonTypes.GrassPokemon import GrassPokemon
from Pokemon_general.PokeType import PokemonType


class Bulbasaur(GrassPokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return ivysaur

class Ivysaur(Bulbasaur):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return venusaur

class Venusaur(Ivysaur):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

# bulbasaur evolution
bulbasaur = Bulbasaur("bulbasaur", "001", 45, 200)
ivysaur = Ivysaur("ivysaur", "002", 60, 230)
venusaur = Venusaur("venusaur", "003", 80, 270)
