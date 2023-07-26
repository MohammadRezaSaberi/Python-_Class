n = int(input('please enter your number :'))

m = ((n // 7) * 7 )  +7

if n % 7 == 0:
    print ('it is 7 multiple')
else:
    print ('the next 7 multiple: ', m)
