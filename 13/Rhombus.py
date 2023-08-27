diameter = int(input("Enter the diameter of the rhombus: "))
for i in range(diameter):
    print(' ' * (diameter - i - 1) + '*' * (2 * i + 1))
for i in range(diameter - 2, -1, -1):
    print(' ' * (diameter - i - 1) + '*' * (2 * i + 1))
