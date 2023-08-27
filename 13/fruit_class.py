class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def ripen(self):
        print(f"I am a {self.name} and I am ripening.")

    def rot(self):
        print(f"I am a {self.name} and I am rotting.")

f1 = Fruit("Apple", "Green", 0.2)
print(f1)        