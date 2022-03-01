class Building:

    def __init__(self, name, num_floors):

        self.name = name
        self.num_floors = num_floors
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_description(self):
        print(f"[Location description: ] {self.description}")
