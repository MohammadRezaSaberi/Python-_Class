numbers1 = []
for i in range (10) :
    n = int(input('please enter your number : '))
    numbers1.append(n)

numbers2 = []

counter = 0
while counter < len(numbers1) :
    numbers2.append(numbers1[counter] + 2)

    counter += 1

print('numbers1 = ', numbers1)
print('numbers2 = ', numbers2)