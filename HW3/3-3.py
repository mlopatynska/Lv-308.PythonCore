#Quadratic formula
from math import *
a = float(input("Enter a:\n"))
b = float(input("Enter b:\n"))
c = float(input("Enter c:\n"))
D = b**2 - 4*a*c
if a == 0:
    print("This is not quadratic equation ")
elif D == 0:
   x = (-b/2*a)
   print('x = {} '.format(x))
elif D > 0:
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print('x1 = {},\nx2 = {}'.format(x1, x2))

elif D < 0:
    print("No valid roots")
print('D = {}'.format(D))
