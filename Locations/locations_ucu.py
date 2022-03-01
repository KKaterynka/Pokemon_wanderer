from Locations.locations import Building
import random

class SheptytskiyCenter(Building):

    def __init__(self, name, num_floors):
        super().__init__(name, num_floors)

    def find_poke_friend(self):
        floor = random.randint(1, self.num_floors)
        user_floor = int(input("Guess floor: "))
        while user_floor != floor:
            print("Everybody makes a wrong turn once in a while.")
            user_floor = int(input("Try again: "))


class Trapezna(Building):

    def __init__(self, name, num_floors, num_sandwiches_to_eat):
        super().__init__(name, num_floors)
        self.num_sandwiches_to_eat = num_sandwiches_to_eat

    def num_sandwiches(self):
        self.num_sandwiches_to_eat -= 1
        if self.num_sandwiches_to_eat <= 0:
            print("No more sandwiches to eat.")
        else:
            print(f"Sandwiches left {self.num_sandwiches_to_eat}")

    def get_num_sandwiches(self):
        return self.num_sandwiches_to_eat

class Collegium(Building):

    def __init__(self, num_floors, name, num_people):
        super().__init__(name, num_floors)
        self.num_people = num_people