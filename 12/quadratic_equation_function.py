import math

def quadratic_equation(a, b, c):
    # Calculate the discriminant
    d = (b**2) - (4*a*c)
    # Calculate the two solutions
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)
    return (x1, x2)

a = int(input('please enter the a :'))
b = int(input('please enter the b :'))
c = int(input('please enter the c :'))

x1, x2 = quadratic_equation(a, b, c)

print(f"The solutions are {x1} and {x2}")
