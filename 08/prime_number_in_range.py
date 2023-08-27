a = int(input('a :'))
b = int(input('b :'))
    
print('prime numbers :')   
 
for number in range (a, b + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)