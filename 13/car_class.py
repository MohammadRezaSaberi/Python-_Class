class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance
        print(f"I have driven {distance} miles. My total mileage is now {self.mileage} miles.")

    def paint(self, new_color):
        self.color = new_color
        print(f"My new color is {new_color}.")

c1 = Car("Toyota", "Camry", 2020, "Red", 10000)
print(c1)        