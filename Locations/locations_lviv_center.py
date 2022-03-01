import random
from Locations.locations import Building

class Lviv_Arsenal(Building):

    def __init__(self, name, num_floors):
        super().__init__(name, num_floors)

    def poke_age(self, user_poke):
        pokemon_age = random.randint(1, 30)
        print(f"Try to guess age of {user_poke.pokemon_name.capitalize()}.")

        count = 0

        while True:

            count += 1
            try:
                prediction = int(input("Your guess: "))
            except:
                print("Only integers!")
                prediction = int(input("Your guess: "))


            if prediction > pokemon_age:
                print(f"[{user_poke.pokemon_name.capitalize()} :] I am not so old!")
            elif prediction < pokemon_age:
                print(f"[{user_poke.pokemon_name.capitalize()} :] I am not so young! But it is a compliment for me.")
            else:
                print(f"[{user_poke.pokemon_name.capitalize()} :] Trainer, you are Captain Obvious! My age is {pokemon_age}")
                break

        return count

class HouseOfScientists(Building):

    def __init__(self, name, num_floors):
        super().__init__(name, num_floors)

    def guess_poke_gender(self, user_poke):
        correct_answr = 0
        print(f"[{user_poke.pokemon_name} :] Hi-hi, trainer, try to guess my sex!")
        poke_gender = random.choice(["male", "female"])
        user_poke_gender = input('Pokemon is "male" or "female": ')
        while user_poke_gender not in ["male", "female"]:
            print(f"[{user_poke.pokemon_name} :] Trainer, I do not understand this option!")
            user_poke_gender = input('Pokemon is "male" or "female": ')
        if user_poke_gender == poke_gender:
            print(f"[{user_poke.pokemon_name} :] Hey, trainer, you're so smart. I am {poke_gender}.")
            correct_answr += 1
        else:
            print(f"[{user_poke.pokemon_name} :] Nooo, trainer, I am {poke_gender}.")

        return correct_answr

class HighCastle(Building):

    def __init__(self, name, num_floors, num_sxodinkas):
        super().__init__(name, num_floors)
        self.num_sxodinkas = num_sxodinkas