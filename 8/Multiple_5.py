# Get a list of numbers from the user (in one line) and store them in a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Display the numbers that are multiples of 5
print("Numbers that are multiples of 5:")
for number in numbers:
    if number % 5 == 0:
        print(number)
