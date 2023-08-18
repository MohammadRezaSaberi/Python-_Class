n = int(input('please enter your number :'))

m = ((n // 7) * 7 )  +7

if n % 7 == 0:
    print ('it is 7 multiple')
else:
    print('it is not 7 multiple')
    print ('the next 7 multiple: ', m)