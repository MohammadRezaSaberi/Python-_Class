def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input('enter your first number :'))
b = int(input('enter your second number :'))

print(f"The GCD of {a} and {b} is {gcd(a, b)}")
print(f"The LCM of {a} and {b} is {lcm(a, b)}")
