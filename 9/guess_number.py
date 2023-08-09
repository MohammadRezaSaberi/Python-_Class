import random

n = random.randint(1, 100)

print(n)

a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))

while True :
    if a == 1 :
        n = random.randint(n, n + 10)
        print(n)
        a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))
        continue
    elif a == 2 :
        n = random.randint(n - 10, n)
        print(n)
        a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))
        continue
    elif a == 3 :
        print('yessssss')
        break