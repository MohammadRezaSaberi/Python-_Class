def multiplication_table(x, y):
    # Determine the width of each column
    width = len(str(x * y)) + 1
    # Print the header row
    print(" " * width, end="")
    for i in range(1, y + 1):
        print(f"{i:{width}}", end="")
    print()
    # Print the table rows
    for i in range(1, x + 1):
        print(f"{i:{width}}", end="")
        for j in range(1, y + 1):
            print(f"{i * j:{width}}", end="")
        print()
        
x = int(input('please enter the length :'))
y = int(input('please enter the width :'))

multiplication_table(x, y)
