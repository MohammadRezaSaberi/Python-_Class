# Create a list of numbers
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6, 5]

counts = {}

for number in numbers:
    if number not in counts:
        counts[number] = 0
    counts[number] += 1

print(counts)
