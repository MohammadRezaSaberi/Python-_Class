import math

print( '1. +' )
print( '2. -' )
print( '3. *' )
print( '4. ÷' )
print( '5. ^' )
print( '6. √' )
print( '7. | |' )
print( '8. ceil' )
print( '9. floor' )
print( '10. mod' )
print( '11. n!' )
print( '12. sin' )
print( '13. cos' )
print( '14. tan' )
print( '15. cot' )
print( '16. asin' )
print( '17. acos' )
print( '18. atan' )
print( '19.log' ) 

user_op = input( 'please inter your operation number ')

if user_op == '1':
    a = float(input('a: '))
    b = float(input('b: '))

    answer = a + b

elif user_op == '2':
    a = float(input('a: '))
    b = float(input('b: '))

    answer = a - b

elif user_op == '3':
    a = float(input('a: '))
    b = float(input('b: '))

    answer = a * b    

elif user_op == '4':
    a = float(input('a: '))
    b = float(input('b: '))

    if b != 0:
        answer = a / b    
    else:
        print('wrong input: b is zero!')

elif user_op == '5':
    a = float(input('a: '))
    b = float(input('b: '))
    
    answer = math.pow(a, b)  
     

elif user_op == '6':
    a = float(input('a: '))

    if a>=0:
        answer = math.sqrt(a)
    else:
        print('wrong input: The radical sub must not be negative')      

elif user_op == '7':
    a = float(input('a: '))

    answer = math.fabs(a)

elif user_op == '8':
    a = float(input('a: '))

    answer = math.ceil(a) 

elif user_op == '9':
    a = float(input('a: '))

    answer = math.floor(a)   

elif user_op == '10':
    a = float(input('a: '))
    b = float(input('b: '))

    answer = math.fmod(a, b)   

elif user_op == '11':
    a = int(input('a: '))

    answer = math.factorial(a)

elif user_op == '12':
    a = float(input('a: '))

    answer = math.sin(a)

elif user_op == '13':
    a = float(input('a: '))

    answer = math.cos(a)   

elif user_op == '14':
    a = float(input('a: '))

    answer = math.tan(a)   

elif user_op == '15':
    a = float(input('a: '))

    s = math.cos(a) 
    d = math.sin(a)

    answer = s / d

elif user_op == '16':
    a = float(input('a: '))

    answer = math.asin(a)

elif user_op == '17':
    a = float(input('a: '))

    answer = math.acos(a)   

elif user_op == '18':
    a = float(input('a: '))

    answer = math.atan(a) 

elif user_op == '19':
    a = int(input('a: ')) 
    b = int(input('b: '))

    answer = math.log(a, b)

print('answer= ', answer)