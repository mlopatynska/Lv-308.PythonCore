"""Find out if we can build a triangle
from three arbitrary values. If possible,
find it's area and perimeter"""

from math import sqrt
a = float(input("Enter a:\n"))
b = float(input("Enter b:\n"))
c = float(input("Enter c:\n"))

if a <= 0 or b <= 0 or c <= 0:
    print('Wrong incoming data, the values must be > 0')
elif a+b <= c or b+c <= a or a+c <= b:
    print('The sum of two sides of triangle'
           'must be lager then the third side.Triangle can\'t be created!' )
else:
#Perimeter
    P = a + b + c

#Area by Heron's formula
    s = (a + b + c)/2
    A = sqrt(s*(s - a)*(s - b)*(s - c))

    print(f'Triangles perimeter:\nP = {P}\nTriangles area:\nA = {A}')

