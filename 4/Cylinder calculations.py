import math

r = float(input('please inter the radius : '))
h = float(input('please inter the height : '))

la = 2 * math.pi * r * h
v = math.pi * ( r**2 ) * h

# S cylinder = ( 2 * S circle ) + S Rectangle
s = ( 2 * ((r ** 2) * math.pi)) + 2 * r * math.pi * h

print('lateral area = ', la)
print('Volume = ', v)
print('Space = ', s)