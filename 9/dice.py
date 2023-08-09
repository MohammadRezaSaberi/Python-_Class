import random
while True:
    dice1 = random.randint(1,6)
    print(dice1)
    if  dice1 == 6 :
      dice2 = random.randint(1,6)
      print(dice2)
      x = dice1 + dice2
      print('Sum =', x)
      break
    else :
       break