class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! I am now {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, gender, height, weight, school, grade):
        super().__init__(name, age, gender, height, weight)
        self.school = school
        self.grade = grade

    def study(self):
        print(f"I am studying for my exams at {self.school}.")

    def graduate(self):
        self.grade += 1
        print(f"I have graduated to grade {self.grade}.")

p1 = Person("Alice", 25, "Female", 1.7, 60)
s1 = Student("Bob", 18, "Male", 1.8, 70, "Harvard", 12)
print(p1)        
print(s1)