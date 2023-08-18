import random

length = int(input("Enter the length of the list: "))


start = int(input('please enter the start of the range :'))

end = int(input('please enter the end of the range :'))

if length > (end - start):
    print("Length of the list cannot be greater than the range of numbers.")
else:
    list = random.sample(range( start, end + 1 ), length)
    print(list)