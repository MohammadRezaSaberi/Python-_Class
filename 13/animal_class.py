class Animal:
    def __init__(self, species, name, age, weight):
        self.species = species
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        print(f"I am a {self.species} and I am eating {food}.")

    def sleep(self):
        print(f"I am a {self.species} and I am sleeping.")

a1 = Animal("Dog", "Rex", 5, 20)
print(a1)