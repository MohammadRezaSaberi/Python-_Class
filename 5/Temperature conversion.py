print( '1. centigrade to fahrenheit ' )
print( '2. fahrenheit to centigrade' )
print( '3. centigrade to kelvin' )
print( '4. kelvin to centigrade' )
print( '5. kelvin to fahrenheit' )
print( '6. fahrenheit to kelvin' )

user_op = input( 'please enter your operation number : ')

if user_op == '1':
    c = float(input('please enter the temperature in centigrade : '))
    f = c * 1.8 + 32

    print('Fahrenheit degree = ', f)

elif user_op == '2':
    f = float(input('please enter the temperature in fahrenheit : '))
    c = ( f - 32 ) / 1.8

    print('Centigrade degree = ', c)

elif user_op == '3':
    c = float(input('please enter the temperature in centigrade : '))
    k = ( c + 273 )

    print('Kelvin degree = ', k)

elif user_op == '4':
    k = float(input('please enter the temperature in kelvin : '))
    c = ( k - 273 )

    print('Centigrade degree = ', c)     

elif user_op == '5':
    k = float(input('please enter the temperature in kelvin : '))
    c = ( k - 273 )
    f = c * 1.8 + 32

    print('Fahrenheit degree = ', f)

elif user_op == '6':
    f = float(input('please enter the temperature in fahrenheit : '))
    c = ( f - 32 ) / 1.8
    k = ( c + 273 )

    print('Kelvin degree = ', k)                