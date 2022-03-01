from Pokemon_general.Pokemon import Pokemon
from Pokemon_general.PokemonTypes.FirePokemon import FirePokemon
from Pokemon_general.PokeType import PokemonType

class Charmander(FirePokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return charmaleon

class Charmaleon(Charmander):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return charizard

class Charizard(Charmaleon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

# charmander evolution
charmander = Charmander("charmander", "004", 39, 188)
charmaleon = Charmaleon("charmaleon", "005", 58, 226)
charizard = Charizard("charizard", "006", 78, 266)