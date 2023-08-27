def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


x = int(input('please enter the x :'))
y = int(input('please enter the y :'))

result = gcd(x, y)
print(f"The GCD is {result}")
