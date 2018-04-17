from math import sqrt
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))
#a, b, c = map(float, input('Enter sides of triangle: ').split())
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print(f'Triangle with sides {a}, {b}, {c} does not exist')
else:
    halfPer = (a + b + c)/2
    print(f'Perimeter of triangle: {a + b + c}\n'
          f'Area of triangle: {sqrt(halfPer*(halfPer-a)*(halfPer-b)*(halfPer-c)):.5}')


