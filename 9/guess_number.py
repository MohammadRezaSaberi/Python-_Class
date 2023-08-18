import random
s = 1

e = 100

n = random.randint(s, e)

print(n)

a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))

while True :
    if a == 1 :
        s = n
        print(n)
        a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))
    
    elif a == 2 :
        e = n
        print(n)
        a = int(input('is it correct ?\n 1. upper\n 2. lower\n 3. correct\n:' ))
        continue
    elif a == 3 :
        print('yessssss')
        break