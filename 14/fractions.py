numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

fraction1 = {"numerator": numerator, "denominator": denominator}

def add_fractions(fraction1, fraction2):
    numerator = fraction1["numerator"] * fraction2["denominator"] + fraction2["numerator"] * fraction1["denominator"]
    denominator = fraction1["denominator"] * fraction2["denominator"]
    return {"numerator": numerator, "denominator": denominator}

def subtract_fractions(fraction1, fraction2):
    numerator = fraction1["numerator"] * fraction2["denominator"] - fraction2["numerator"] * fraction1["denominator"]
    denominator = fraction1["denominator"] * fraction2["denominator"]
    return {"numerator": numerator, "denominator": denominator}

def multiply_fractions(fraction1, fraction2):
    numerator = fraction1["numerator"] * fraction2["numerator"]
    denominator = fraction1["denominator"] * fraction2["denominator"]
    return {"numerator": numerator, "denominator": denominator}

def divide_fractions(fraction1, fraction2):
    numerator = fraction1["numerator"] * fraction2["denominator"]
    denominator = fraction1["denominator"] * fraction2["numerator"]
    return {"numerator": numerator, "denominator": denominator}

numerator = int(input("Enter the numerator of the second fraction: "))
denominator = int(input("Enter the denominator of the second fraction: "))

fraction2 = {"numerator": numerator, "denominator": denominator}

result = add_fractions(fraction1, fraction2)
print(f"The result of addition is {result['numerator']}/{result['denominator']}")

result = subtract_fractions(fraction1, fraction2)
print(f"The result of subtraction is {result['numerator']}/{result['denominator']}")

result = multiply_fractions(fraction1, fraction2)
print(f"The result of multiplication is {result['numerator']}/{result['denominator']}")

result = divide_fractions(fraction1, fraction2)
print(f"The result of division is {result['numerator']}/{result['denominator']}")
