from Pokemon_general.Pokemon import Pokemon
from Pokemon_general.PokemonTypes.AquaPokemon import AquaPokemon
from Pokemon_general.PokeType import PokemonType

class Squirtle(AquaPokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return wartortle

class Wartortle(AquaPokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

    def level_up(self):
        return blastoise

class Blastoise(AquaPokemon):

    def __init__(self, pokemon_name, pokemon_id, current_hp, max_hp):

        # basic info about pokemon
        super().__init__(pokemon_name, pokemon_id, current_hp, max_hp)

# squirtle evolution
squirtle = Squirtle("squirtle", "007", 44, 198)
wartortle = Wartortle("wartortle", "007", 59, 228)
blastoise = Blastoise("blastoise", "009", 79, 268)