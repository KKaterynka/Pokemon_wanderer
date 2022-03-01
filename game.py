from Pokemon_general.Pokemon import Pokemon
from Pokemon_general.PokemonTypes.AquaPokemon import AquaPokemon
from Pokemon_general.PokeType import PokemonType
from Pokemon_general.PokemonTypes.FirePokemon import FirePokemon
from Pokemon_general.PokemonTypes.GrassPokemon import GrassPokemon
from Locations.locations_ucu import SheptytskiyCenter, Trapezna, Collegium
from Locations.locations_lviv_center import Lviv_Arsenal, HouseOfScientists, HighCastle
from Pokemon_general.Starter_Pokemons.Squirtle import Squirtle, Blastoise, Wartortle
from Pokemon_general.Starter_Pokemons.Charmander import Charmander, Charmaleon, Charizard
from Pokemon_general.Starter_Pokemons.Bulbasaur import Bulbasaur, Ivysaur, Venusaur
from Pokemon_general.Starter_Pokemons.Bulbasaur import bulbasaur, ivysaur, venusaur
from Pokemon_general.Starter_Pokemons.Charmander import charmander, charmaleon, charizard
from Pokemon_general.Starter_Pokemons.Squirtle import squirtle, blastoise, wartortle
import random
import time

# first level locations
sheptytsky_center = SheptytskiyCenter(name="Sheptytsky Center" , num_floors=4)
sheptytsky_center.set_description("A leading public space to combine culture, science and education.\n")
trapezna = Trapezna(name="Trapezna", num_floors=4, num_sandwiches_to_eat=7)
trapezna.set_description("Remember your Pokémon omnivorous diet. Too much temptation here!\n")
collegium = Collegium(name="Collegium" ,num_floors=6 , num_people=230)
collegium.set_description(f"{collegium.num_people} people are living here. Do not mistake student with Pokémon!\n")

# second level locations
lviv_arsenal = Lviv_Arsenal(name="Lviv Arsenal", num_floors=2)
lviv_arsenal.set_description("The oldest arsenal building in Lviv.\n")
house_of_scientists = HouseOfScientists(name="House Of Scientists", num_floors=3)
house_of_scientists.set_description("Former casino for Lvivs' elite.\n")
high_castle = HighCastle(name="High Castle", num_floors=None, num_sxodinkas=324)
high_castle.set_description("The best vantage point for a panoramic view of Lviv.\n")

def validation(user_input, validate_range):
    user_option = input(user_input)
    while user_option not in validate_range:
        print("No such option!")
        print("Available options:\n")
        for i in validate_range:
            print("   * " + i)
        user_option = input("\nYour option: ")
    return user_option

available_pokes = [bulbasaur, charmander, squirtle]

def choose_poke(user_name):

    time.sleep(1)
    print(f"{user_name}, do you want to choose your Pokémon or will you rely on fate?\n")
    time.sleep(2)
    message_opt_poke = 'Enter "poke" for Pokémon or "fate" alternatively: '
    user_option = validation(message_opt_poke, ["poke", "fate"])

    if user_option == "poke":
        print(f"\nAvailable Pokémons:\n1. {bulbasaur.pokemon_name.capitalize()}\n2. {charmander.pokemon_name.capitalize()}\n3. {squirtle.pokemon_name.capitalize()}\n")
        time.sleep(2)
        print(f"Follow your heart, {user_name}!\n")
        time.sleep(1)
        user_poke = validation("Enter full name of Pokémon: ", ["bulbasaur", "Bulbasaur", "charmander", "Charmander", "squirtle", "Squirtle"])
    else:
        print("\nWait for typewheel to choose the right Pokémon for you.\n")
        time.sleep(2)
        user_poke = random.choice(available_pokes)
        print(f"My congratulations! Your Pokémon is {user_poke.pokemon_name.capitalize()}.\n")

    return user_poke

def first_level_move(user_poke, first_level_locations, poke_friend):

    not_gone_to = first_level_locations

    while len(not_gone_to) > 0:

        frst_location = validation("\nEnter location to go to: ", [sheptytsky_center.name, trapezna.name, collegium.name])

        if frst_location == "Sheptytsky Center":
            frst_location = sheptytsky_center
            frst_location.get_description()
            if sheptytsky_center not in not_gone_to:
                print(f"\n[{user_poke.pokemon_name.capitalize()} :] Trainer, we've already found {poke_friend.pokemon_name.capitalize()}. No need to go to {frst_location.name}\n")
                first_level_move(user_poke, first_level_locations, poke_friend)
            else:
                time.sleep(1)
                print(f"\n{user_name}, try to guess the floor, where {poke_friend.pokemon_name.capitalize()} is.\n")
                frst_location.find_poke_friend()
                time.sleep(1)
                print(f"[{user_poke.pokemon_name.capitalize()} :] Oh, I hear {poke_friend.pokemon_name.capitalize()}\n. We found him!")
                not_gone_to.remove(sheptytsky_center)

        elif frst_location == "Trapezna":
            if trapezna.get_num_sandwiches() <= 0:
                time.sleep(1)
                print("No sandwiches left\n")
                first_level_move(user_poke, first_level_locations, poke_friend)
                break
            time.sleep(2)
            print(f"\n[{user_poke.pokemon_name.capitalize()} :] Trainer, high time to feed me?\n")
            time.sleep(2)
            print(f'{user_name}, to feed  {user_poke.pokemon_name.capitalize()} type in "food".\n')
            time.sleep(1)
            print('To exit Trapezna type in "exit".\n')
            time.sleep(2)
            while True:
                user_feed = input(">>> ")
                if user_feed == "food":
                    user_poke.feed()
                    trapezna.num_sandwiches()
                    if trapezna.get_num_sandwiches() <= 0:
                        break
                    try:
                        not_gone_to.remove(trapezna)
                    except:
                        continue
                elif user_feed == "exit":
                    first_level_move(user_poke, first_level_locations, poke_friend)
                    break
                else:
                    print(f"There is no such option! You're out of {trapezna.name}.\n")
                    first_level_move(user_poke, first_level_locations, poke_friend)
                    break

        else:
            frst_location = collegium
            frst_location.get_description()
            if collegium in not_gone_to:
                poke_enemy = random.choice(available_pokes)
                while poke_enemy.pokemon_name == user_poke.pokemon_name:
                    poke_enemy = random.choice(available_pokes)
                available_pokes.remove(poke_enemy)
                time.sleep(1)
                print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, there is an enemy {poke_enemy}  Are we ready to fight him?\n")
                time.sleep(2)
                user_fight = validation('Type in "yes" or "no": ', ["yes", "no", "y", "n", "Yes", "No", "Y", "N"])
                if user_fight in ["yes", "y", "Yes", "Y"]:
                    print(str(user_poke)[12:].lower(), str(poke_enemy)[12:].lower())
                    user_poke.battle(poke_enemy)
                    not_gone_to.remove(collegium)
                    time.sleep(3)
                else:
                    time.sleep(1)
                    print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, but {poke_enemy.pokemon_name} started attack! I will defeat him now!")
                    print(str(user_poke)[12:].lower(), str(poke_enemy)[12:].lower())
                    time.sleep(2)
                    user_poke.battle(poke_enemy)
                    not_gone_to.remove(collegium)
            else:
                time.sleep(1)
                print(f"[{user_poke.pokemon_name.capitalize()} :] We've already had a fight! I do not want more!")
                first_level_move(user_poke, first_level_locations, poke_friend)
                break

def first_level(user_poke):
    first_level_locations = [sheptytsky_center, trapezna, collegium]
    poke_friend = random.choice(available_pokes)
    available_pokes.remove(poke_friend)
    time.sleep(1)
    print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, we need to find my friend {poke_friend.pokemon_name.capitalize()} at UCU Campus.\n")
    time.sleep(1)
    print("Locations to explore: \n")
    time.sleep(1)
    for first_level_location in first_level_locations:
        print("   * " + first_level_location.name)
    time.sleep(2)

    first_level_move(user_poke, first_level_locations, poke_friend)

def scnd_level_move(user_poke, scnd_level_locations):

    trainer_experience = 0
    not_gone_to = scnd_level_locations

    while len(not_gone_to) > 0:
        time.sleep(1)
        scnd_location = validation("\nEnter location to go to: ", [lviv_arsenal.name, high_castle.name, house_of_scientists.name])
        time.sleep(2)
        if scnd_location == high_castle.name:
            high_castle.get_description()
            if high_castle in not_gone_to:
                available_products = ["sunlight", "insects", "apples", "fish", "dinosaurs"]
                print("\nNow you have a chance to strengthen friendship with your Pokémon.\n")
                time.sleep(2)

                print(
                    f"[{user_poke.pokemon_name.capitalize()} :] Trainer, it takes too long to get to the top of High Castle!\n")
                time.sleep(2)
                print(f"[{user_poke.pokemon_name.capitalize()} :] Would you buy me something tasty when we are done?\n")
                time.sleep(2)
                print(f"Now, decide what to buy for {user_poke.pokemon_name}. Remember, your choice impacts your bond.\n")
                time.sleep(1)
                for product in available_products:
                    print("   * " + product)
                user_buy_food = validation("Your option: ", available_products)
                poke_to_food = {bulbasaur.pokemon_name: available_products[0],
                                charmander.pokemon_name: available_products[2],
                                squirtle.pokemon_name: available_products[3],
                                wartortle.pokemon_name: available_products[3], ivysaur.pokemon_name: available_products[0],
                                charmaleon.pokemon_name: available_products[2]}
                poke_fav_food = poke_to_food[user_poke.pokemon_name]
                if user_buy_food == poke_fav_food:
                    time.sleep(1)
                    print(
                        f"[{user_poke.pokemon_name.capitalize()} :] Trainer, you know that I adore {poke_fav_food}. It's so sweet!\n")
                else:
                    time.sleep(1)
                    print(
                        f"[{user_poke.pokemon_name.capitalize()} :] Trainer, I hate {user_buy_food}. It's so disgusting to me!\n")
                not_gone_to.remove(high_castle)
            else:
                time.sleep(1)
                print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, we've already been to {high_castle.name}!\n")
                scnd_level_move(user_poke, scnd_level_locations)

        elif scnd_location == house_of_scientists.name:
            house_of_scientists.get_description()
            if house_of_scientists in not_gone_to:
                scnd_amount_counter = house_of_scientists.guess_poke_gender(user_poke)
                if scnd_amount_counter:
                    trainer_experience += 5
                else:
                    time.sleep(1)
                    print("Unfortunately, you did not gained any experience points.\n")
                time.sleep(1)
                print(f"Your Trainer Experince: {trainer_experience} out of 15\n")
                not_gone_to.remove(house_of_scientists)
            else:
                time.sleep(1)
                print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, we've already been to {house_of_scientists.name}!\n")
                scnd_level_move(user_poke, scnd_level_locations)

        else:
            lviv_arsenal.get_description()
            if lviv_arsenal in not_gone_to:
                frst_amount_counter = lviv_arsenal.poke_age(user_poke)
                if frst_amount_counter == 1:
                    trainer_experience += 10
                elif frst_amount_counter > 1 and frst_amount_counter < 6:
                    trainer_experience += 8
                elif frst_amount_counter > 6 and frst_amount_counter < 20:
                    trainer_experience += 6
                elif frst_amount_counter > 20 and frst_amount_counter < 25:
                    trainer_experience += 4
                elif frst_amount_counter > 25:
                    trainer_experience += 2
                time.sleep(1)
                print(f"Your Trainer Experince: {trainer_experience} out of 15.\n")
                time.sleep(2)
                not_gone_to.remove(lviv_arsenal)
            else:
                time.sleep(1)
                print(
                    f"[{user_poke.pokemon_name.capitalize()} :] Trainer, we've already been to {lviv_arsenal.name}!\n")
                scnd_level_move(user_poke, scnd_level_locations)

    return trainer_experience

def second_level(user_poke):
    scnd_level_locations = [high_castle, house_of_scientists, lviv_arsenal]
    time.sleep(1)
    print("Locations to explore: ")
    time.sleep(2)
    for scnd_level_location in scnd_level_locations:
        print("* " + scnd_level_location.name)

    bond_points = scnd_level_move(user_poke, scnd_level_locations)
    time.sleep(2)
    print(f"Congrats! You trained {user_poke.pokemon_name.capitalize()} good enough!\n")

    return bond_points

def pokemon_evolution(curr_feature, feature_min, user_poke):
    if curr_feature > feature_min:
        print(f"Good job! {user_poke.pokemon_name.capitalize()} has evolved to {user_poke.level_up().pokemon_name.capitalize()}.\n")
        return user_poke.level_up()
    else:
        print(f"Unfortunately, {user_poke.pokemon_name.capitalize()}'s hp is too low to evolve.\n")
        return user_poke

def playground():
    print(
        "There are bad ways to win and good ways to lose. What’s interesting and troubling is that it’s not always clear which is which.\n")
    time.sleep(5)
    print("Try to succeed!\n")
    time.sleep(1)
    user_poke = choose_poke(user_name)
    if user_poke in ["bulbasaur", "Bulbasaur"]:
        user_poke = bulbasaur
        available_pokes.remove(bulbasaur)
    elif user_poke in ["charmander", "Charmander"]:
        user_poke = charmander
        available_pokes.remove(charmander)
    elif user_poke in ["squirtle", "Squirtle"]:
        user_poke = squirtle
        available_pokes.remove(squirtle)

    time.sleep(2)
    print(f"\nNow, it is time to start with {user_poke.pokemon_name.capitalize()}.\n")

    # level 1
    time.sleep(1)
    print("\nLEVEL 1")
    time.sleep(1)
    print(
        """
        Your tasks here:
         * Find a second Pokémon
         * Eat all sandwiches to increase Pokémon's power
         * Win a battle
        """)
    time.sleep(3)
    first_level(user_poke)
    user_poke = pokemon_evolution(user_poke.current_hp, 60, user_poke)

    # level 2
    print("\nLEVEL 2\n")
    time.sleep(1)
    print(
        """
        In this level you should gain as much experience as possible.
    
        Your tasks here:
         * Train your Pokémon
         * Quiz: Pokémon's age
         * Quiz: Pokémon's gender
        """)
    time.sleep(3)
    bond_points = second_level(user_poke)
    time.sleep(2)
    user_poke = pokemon_evolution(bond_points, 7, user_poke)
    time.sleep(2)
    print(f"{user_name}, you leveled up your starter Pokémon to {user_poke.pokemon_name.capitalize()}.\n")
    time.sleep(2)
    print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, thank you! Now I am a big boy!\n")

# introduction
time.sleep(1)
print("Some trainers have no fear. To them, this is just one more challenge.\n")
time.sleep(2)
print("Trainer, are you ready to start your journey?\n")
time.sleep(2)
user_name = input("Enter your name: ")
playground()